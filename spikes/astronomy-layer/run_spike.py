"""Astronomy-layer spike runner.

Part 1 validates OUR Lahiri ayanamsha against the JHora-published table
(https://jagannathhora.com/lahiri-ayanamsa-value/, computed from Swiss
Ephemeris). Part 2 computes full graha positions + lagna for 3 Kerala
test births, for manual verification against Jagannatha Hora.
"""

from ephemeris import ts, tropical_longitudes, moon_state_ecliptic
from ayanamsha import lahiri_ayanamsha_deg, format_dms
from jyothisham import (to_sidereal, rashi_of, nakshatra_of,
                        mean_rahu_tropical, true_rahu_tropical)
from lagna import tropical_ascendant_deg

IST = 5.5 / 24.0


def dms_to_deg(d, m, s):
    return d + m / 60.0 + s / 3600.0


print("=" * 72)
print("PART 1 — Lahiri ayanamsha vs JHora reference table (true of date)")
print("=" * 72)
REF = [  # (label, year, month, day, JHora table value)
    ("2000-01-01", 2000, 1, 1, dms_to_deg(23, 51, 12)),
    ("2010-01-01", 2010, 1, 1, dms_to_deg(24, 0, 5)),
    ("2020-01-01", 2020, 1, 1, dms_to_deg(24, 7, 55)),
    ("2026-01-01", 2026, 1, 1, dms_to_deg(24, 13, 19)),
    ("2026-04-01", 2026, 4, 1, dms_to_deg(24, 13, 32)),
]
for label, y, mo, d, ref in REF:
    t = ts.tt(y, mo, d, 0, 0, 0)
    ours = lahiri_ayanamsha_deg(t.tt)
    diff = (ours - ref) * 3600.0
    print(f"  {label}: ours {format_dms(ours)}  ref {format_dms(ref)}  "
          f"diff {diff:+6.1f}\"")

print()
print("=" * 72)
print("PART 2 — Test births (verify in Jagannatha Hora, Lahiri, true node)")
print("=" * 72)

BIRTHS = [
    ("Birth A — 1990-05-15 06:30 IST, Thiruvananthapuram",
     (1990, 5, 15, 6, 30), 8.4855, 76.9492),
    ("Birth B — 1985-11-02 23:45 IST, Kozhikode",
     (1985, 11, 2, 23, 45), 11.2588, 75.7804),
    ("Birth C — 2000-01-01 12:00 IST, Kochi",
     (2000, 1, 1, 12, 0), 9.9312, 76.2673),
]

for title, (y, mo, d, h, mi), lat, lon in BIRTHS:
    # IST -> UT
    t = ts.ut1(y, mo, d, h - 5, mi - 30, 0)
    ayan = lahiri_ayanamsha_deg(t.tt)
    print(f"\n{title}")
    print(f"  JD(UT) {t.ut1:.6f}   ayanamsha {format_dms(ayan)}")
    print(f"  {'Graha':22s} {'sidereal':>12s}  {'rashi':28s} "
          f"{'naal':30s} pada")

    longs = tropical_longitudes(t)
    for name, (trop, speed) in longs.items():
        sid = to_sidereal(trop, ayan)
        _, rashi, deg_in = rashi_of(sid)
        _, naal, pada, _ = nakshatra_of(sid)
        retro = " R" if speed < 0 else ""
        print(f"  {name:22s} {format_dms(sid):>12s}  {rashi:28s} "
              f"{naal:30s} {pada}{retro}")

    # Rahu/Ketu — both conventions
    r, v = moon_state_ecliptic(t)
    for label, trop_node in (
            ("Rahu (true node)", true_rahu_tropical(r, v)),
            ("Rahu (mean node)", mean_rahu_tropical(t.tt))):
        sid = to_sidereal(trop_node, ayan)
        _, rashi, _ = rashi_of(sid)
        _, naal, pada, _ = nakshatra_of(sid)
        print(f"  {label:22s} {format_dms(sid):>12s}  {rashi:28s} "
              f"{naal:30s} {pada}")

    # Lagna
    trop_asc = tropical_ascendant_deg(t.ut1, t.tt, lat, lon)
    sid_asc = to_sidereal(trop_asc, ayan)
    _, rashi, _ = rashi_of(sid_asc)
    _, naal, pada, _ = nakshatra_of(sid_asc)
    print(f"  {'LAGNA':22s} {format_dms(sid_asc):>12s}  {rashi:28s} "
          f"{naal:30s} {pada}")
