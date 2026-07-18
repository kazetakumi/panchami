"""Lahiri/Chitrapaksha ayanamsha — implemented from the published definition.

Definition (Calendar Reform Committee 1956; refined in Indian Astronomical
Ephemeris 1985/1989): the ayanamsha was decreed to be 23°15'00.658" on
1956 March 21.0 ET (JD 2435553.5), a value that INCLUDES nutation in
longitude at that instant. The star Chitra (Spica) sits at 180° of the
sidereal zodiac. Sources:
  - Indian Astronomical Ephemeris 1989, p. 556 (anchor value)
  - Swiss Ephemeris sweph.h ayanamsa table (documents the same anchor and
    the nutation subtraction -0.004658035 deg per Wahr 1980):
    https://github.com/aloistr/swisseph/blob/master/sweph.h
  - Accumulated general precession in longitude p_A: IAU 2006 precession,
    Capitaine, Wallace & Chapront (2003), A&A 412, 567 — polynomial as
    given in the IERS Conventions / Meeus (2nd ed.) update.
  - Nutation in longitude: truncated IAU 1980 series, Meeus,
    "Astronomical Algorithms" (2nd ed.), ch. 22 (largest 13 terms;
    truncation error < 0.5", far inside the arc-minute tolerance).

ayanamsha_true(t) = mean_anchor + [p_A(t) - p_A(t0)] + delta_psi(t)

This file is OUR implementation — no astrology library is used.
"""

import math

J2000 = 2451545.0
T0_LAHIRI = 2435553.5  # 1956 March 21.0 ET
# 23°15'00.658" minus nutation at t0 (Wahr 1980) -> the MEAN anchor:
AYAN_T0_MEAN_DEG = 23.250182778 - 0.004658035

ARCSEC = 1.0 / 3600.0


def _centuries_tt(jd_tt: float) -> float:
    return (jd_tt - J2000) / 36525.0


def general_precession_longitude_arcsec(jd_tt: float) -> float:
    """Accumulated general precession in ecliptic longitude p_A since J2000,
    in arcseconds. IAU 2006 (Capitaine et al. 2003, eq. for p_A)."""
    t = _centuries_tt(jd_tt)
    return (5028.796195 * t
            + 1.1054348 * t * t
            + 0.00007964 * t ** 3
            - 0.000023857 * t ** 4
            - 0.0000000383 * t ** 5)


def nutation_longitude_arcsec(jd_tt: float) -> float:
    """Nutation in longitude (delta-psi), arcseconds.
    Truncated IAU 1980 series per Meeus AA ch. 22 — 13 largest terms."""
    t = _centuries_tt(jd_tt)
    d2r = math.radians

    # Fundamental arguments (Meeus 22.1-22.5, degrees)
    D = 297.85036 + 445267.111480 * t - 0.0019142 * t * t + t ** 3 / 189474.0
    M = 357.52772 + 35999.050340 * t - 0.0001603 * t * t - t ** 3 / 300000.0
    Mp = 134.96298 + 477198.867398 * t + 0.0086972 * t * t + t ** 3 / 56250.0
    F = 93.27191 + 483202.017538 * t - 0.0036825 * t * t + t ** 3 / 327270.0
    Om = 125.04452 - 1934.136261 * t + 0.0020708 * t * t + t ** 3 / 450000.0

    # (D, M, M', F, Om, coeff0 [0.0001"], coeff_t [0.0001"/cy])
    terms = [
        (0, 0, 0, 0, 1, -171996, -174.2),
        (-2, 0, 0, 2, 2, -13187, -1.6),
        (0, 0, 0, 2, 2, -2274, -0.2),
        (0, 0, 0, 0, 2, 2062, 0.2),
        (0, 1, 0, 0, 0, 1426, -3.4),
        (0, 0, 1, 0, 0, 712, 0.1),
        (-2, 1, 0, 2, 2, -517, 1.2),
        (0, 0, 0, 2, 1, -386, -0.4),
        (0, 0, 1, 2, 2, -301, 0.0),
        (-2, -1, 0, 2, 2, 217, -0.5),
        (-2, 0, 1, 0, 0, -158, 0.0),
        (-2, 0, 0, 2, 1, 129, 0.1),
        (0, 0, -1, 2, 2, 123, 0.0),
    ]
    dpsi = 0.0
    for d, m, mp, f, om, c0, ct in terms:
        arg = d2r(d * D + m * M + mp * Mp + f * F + om * Om)
        dpsi += (c0 + ct * t) * math.sin(arg)
    return dpsi * 0.0001


def lahiri_ayanamsha_deg(jd_tt: float, true_of_date: bool = True) -> float:
    """Lahiri ayanamsha in degrees at jd (TT). true_of_date=True includes
    nutation — this is what JHora/Drik display and apply."""
    p_now = general_precession_longitude_arcsec(jd_tt)
    p_t0 = general_precession_longitude_arcsec(T0_LAHIRI)
    ayan = AYAN_T0_MEAN_DEG + (p_now - p_t0) * ARCSEC
    if true_of_date:
        ayan += nutation_longitude_arcsec(jd_tt) * ARCSEC
    return ayan


def format_dms(deg: float) -> str:
    sign = "-" if deg < 0 else ""
    deg = abs(deg)
    d = int(deg)
    m = int((deg - d) * 60)
    s = ((deg - d) * 60 - m) * 60
    return f"{sign}{d}°{m:02d}'{s:04.1f}\""
