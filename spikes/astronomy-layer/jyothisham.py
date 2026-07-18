"""The astrology layer — entirely ours, from the published conventions.

- Sidereal conversion: sidereal = tropical - ayanamsha (mod 360).
- Rashi: 12 x 30° from sidereal 0° (Mesha/Medam).
- Nakshatra: 27 x 13°20' from sidereal 0° (Ashwini/Ashwathi); pada = quarter
  of 3°20'. Fixed convention, e.g. BPHS; Malayalam naal names are the
  Kerala names for the same 27 stars (product decision: Latin script).
- Rahu (mean node): Meeus, "Astronomical Algorithms" 2nd ed., ch. 47
  (longitude of the Moon's mean ascending node). Ketu = Rahu + 180°.
- Rahu (true node): computed by US from the Moon's osculating orbital
  plane — node = intersection of the plane normal (r x v) with the
  ecliptic. Standard orbital mechanics, no astrology library involved.
"""

import math

from ayanamsha import J2000

RASHI_ML = [
    "Medam (Mesha/Aries)", "Edavam (Vrishabha/Taurus)",
    "Midhunam (Mithuna/Gemini)", "Karkidakam (Karka/Cancer)",
    "Chingam (Simha/Leo)", "Kanni (Kanya/Virgo)",
    "Thulam (Tula/Libra)", "Vrischikam (Vrischika/Scorpio)",
    "Dhanu (Dhanus/Sagittarius)", "Makaram (Makara/Capricorn)",
    "Kumbham (Kumbha/Aquarius)", "Meenam (Meena/Pisces)",
]

# 27 nakshatras — Malayalam naal (Sanskrit) in traditional order.
NAAL_ML = [
    "Ashwathi (Ashwini)", "Bharani (Bharani)", "Karthika (Krittika)",
    "Rohini (Rohini)", "Makayiram (Mrigashira)", "Thiruvathira (Ardra)",
    "Punartham (Punarvasu)", "Pooyam (Pushya)", "Ayilyam (Ashlesha)",
    "Makam (Magha)", "Pooram (Purva Phalguni)", "Uthram (Uttara Phalguni)",
    "Atham (Hasta)", "Chithira (Chitra)", "Chothi (Swati)",
    "Vishakham (Vishakha)", "Anizham (Anuradha)", "Thrikketta (Jyeshtha)",
    "Moolam (Mula)", "Pooradam (Purva Ashadha)", "Uthradam (Uttara Ashadha)",
    "Thiruvonam (Shravana)", "Avittam (Dhanishta)", "Chathayam (Shatabhisha)",
    "Pooruruttathi (Purva Bhadrapada)", "Uthrattathi (Uttara Bhadrapada)",
    "Revathi (Revati)",
]


def to_sidereal(tropical_deg: float, ayanamsha_deg: float) -> float:
    return (tropical_deg - ayanamsha_deg) % 360.0


def rashi_of(sidereal_deg: float):
    idx = int(sidereal_deg // 30.0)
    return idx, RASHI_ML[idx], sidereal_deg - idx * 30.0


def nakshatra_of(sidereal_deg: float):
    span = 360.0 / 27.0  # 13°20'
    idx = int(sidereal_deg // span)
    frac = (sidereal_deg - idx * span) / span
    pada = int(frac * 4) + 1
    return idx, NAAL_ML[idx], pada, frac


def mean_rahu_tropical(jd_tt: float) -> float:
    """Longitude of the Moon's mean ascending node (tropical, deg).
    Meeus AA 2nd ed. ch. 47 (Omega polynomial)."""
    t = (jd_tt - J2000) / 36525.0
    om = (125.0445479 - 1934.1362891 * t + 0.0020754 * t * t
          + t ** 3 / 467441.0 - t ** 4 / 60616000.0)
    return om % 360.0


def true_rahu_tropical(r, v) -> float:
    """True (osculating) ascending node from the Moon's geocentric state
    vectors in the ecliptic-of-date frame. The orbit-plane normal is
    h = r x v; the ascending node direction is n = z-hat x h. Longitude
    of node = atan2(n_y, n_x). Vallado, 'Fundamentals of Astrodynamics',
    node-vector method — standard orbital mechanics."""
    hx = r[1] * v[2] - r[2] * v[1]
    hy = r[2] * v[0] - r[0] * v[2]
    hz = r[0] * v[1] - r[1] * v[0]
    # n = k x h = (-hy, hx, 0)
    node = math.degrees(math.atan2(hx, -hy)) % 360.0
    return node
