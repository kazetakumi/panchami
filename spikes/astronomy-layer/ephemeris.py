"""Astronomy layer: raw geocentric apparent positions via Skyfield (MIT)
+ JPL DE421. This is the ONE place external astronomical data enters.
Everything downstream (ayanamsha, rashi, nakshatra, lagna, nodes) is ours.

Skyfield: https://rhodesmill.org/skyfield/ (MIT license)
DE421: JPL planetary ephemeris, public NASA data (1900-2050).

Output frame: TRUE ecliptic and equinox of date, apparent positions
(light-time + aberration + nutation) — the same frame Swiss Ephemeris
uses by default, hence comparable with JHora.
"""

from skyfield.api import Loader, wgs84
from skyfield.framelib import ecliptic_frame

_load = Loader("./skydata")  # caches de421.bsp next to the spike

ts = _load.timescale()
eph = _load("de421.bsp")

EARTH = eph["earth"]

# Graha -> DE421 target. Surya..Shani are apparent geocentric positions.
GRAHA_TARGETS = {
    "Surya (Sun)": eph["sun"],
    "Chandra (Moon)": eph["moon"],
    "Budha (Mercury)": eph["mercury"],
    "Shukra (Venus)": eph["venus"],
    "Kuja (Mars)": eph["mars"],
    "Guru (Jupiter)": eph["jupiter barycenter"],
    "Shani (Saturn)": eph["saturn barycenter"],
}


def tropical_longitudes(t):
    """Apparent geocentric ecliptic-of-date longitudes (deg) for the 7
    classical grahas at Skyfield time t. Also returns speed sign for
    retrograde detection (deg/day, from a 1-hour finite difference)."""
    out = {}
    t2 = ts.tt_jd(t.tt + 1.0 / 24.0)
    for name, target in GRAHA_TARGETS.items():
        lon = _lon(t, target)
        lon2 = _lon(t2, target)
        speed = ((lon2 - lon + 540.0) % 360.0 - 180.0) * 24.0
        out[name] = (lon, speed)
    return out


def _lon(t, target):
    astrometric = EARTH.at(t).observe(target).apparent()
    _, lon, _ = astrometric.frame_latlon(ecliptic_frame)
    return lon.degrees % 360.0


def moon_state_ecliptic(t):
    """Geocentric Moon position & velocity vectors in the ecliptic-of-date
    frame (au, au/day) — raw inputs for OUR true-node computation."""
    pos = EARTH.at(t).observe(eph["moon"]).apparent()
    r, v = pos.frame_xyz_and_velocity(ecliptic_frame)
    return r.au, v.au_per_d
