"""Lagna (ascendant) — computed by us from first principles.

Chain: UT -> GMST (IAU 1982 expression, Meeus AA 2nd ed. ch. 12,
eq. 12.4) -> local apparent sidereal time (+ east longitude, + equation
of the equinoxes) -> RAMC -> tropical ascendant (standard spherical-
astronomy formula, Meeus ch. on rising signs / any astrology-math text):

    asc = atan2( cos(RAMC), -(sin(RAMC)*cos(eps) + tan(phi)*sin(eps)) )

Obliquity: mean obliquity IAU 2006 polynomial (Meeus 22.2 update) +
nutation in obliquity omitted (< 10 arcsec effect on eps; ascendant
sensitivity keeps the error well under the arc-minute budget; noted as
a refinement for the production engine).
Sidereal lagna = tropical asc - ayanamsha.
"""

import math

from ayanamsha import J2000, nutation_longitude_arcsec


def gmst_deg(jd_ut: float) -> float:
    """Greenwich mean sidereal time in degrees (IAU 1982 / Meeus 12.4)."""
    t = (jd_ut - J2000) / 36525.0
    gmst = (280.46061837 + 360.98564736629 * (jd_ut - J2000)
            + 0.000387933 * t * t - t ** 3 / 38710000.0)
    return gmst % 360.0


def mean_obliquity_deg(jd_tt: float) -> float:
    """Mean obliquity of the ecliptic, IAU 2006 polynomial (arcsec)."""
    t = (jd_tt - J2000) / 36525.0
    eps_arcsec = (84381.406 - 46.836769 * t - 0.0001831 * t * t
                  + 0.00200340 * t ** 3 - 0.000000576 * t ** 4
                  - 0.0000000434 * t ** 5)
    return eps_arcsec / 3600.0


def tropical_ascendant_deg(jd_ut: float, jd_tt: float,
                           lat_deg: float, lon_east_deg: float) -> float:
    eps = math.radians(mean_obliquity_deg(jd_tt))
    # equation of the equinoxes: dpsi * cos(eps) -> apparent sidereal time
    eqeq_deg = (nutation_longitude_arcsec(jd_tt) / 3600.0) * math.cos(eps)
    last = math.radians((gmst_deg(jd_ut) + eqeq_deg + lon_east_deg) % 360.0)
    phi = math.radians(lat_deg)
    asc = math.atan2(
        math.cos(last),
        -(math.sin(last) * math.cos(eps) + math.tan(phi) * math.sin(eps)),
    )
    return math.degrees(asc) % 360.0
