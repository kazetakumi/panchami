# Astronomy layer spike

Asset for wayfinder ticket [Astronomy layer spike](../../docs/wayfinder/engineering/tickets/001-astronomy-layer-spike.md)
(engineering map). Throwaway code — findings matter, not the code.

## What it proves

The from-scratch line holds: **Skyfield (MIT) + JPL DE421 supply raw
apparent positions only; every astrological computation here is ours**,
implemented from published definitions with citations in the source:

| Component | Ours? | Source cited in code |
|---|---|---|
| Tropical longitudes (9 grahas) | Skyfield/DE421 (astronomy data) | — |
| Lahiri ayanamsha | **ours** | IAE 1989 anchor via SE `sweph.h` table; IAU 2006 precession (Capitaine et al. 2003); nutation Meeus ch. 22 |
| Sidereal conversion, rashi, nakshatra/naal, pada | **ours** | fixed conventions (BPHS) |
| Rahu mean node | **ours** | Meeus AA ch. 47 |
| Rahu true node | **ours** | osculating node from Moon state vectors (Vallado node-vector method) |
| Lagna | **ours** | GMST Meeus 12.4; standard ascendant formula; IAU 2006 obliquity |

## Results (2026-07-17)

1. **Ayanamsha: ours vs the JHora-published Lahiri table — within 0.6″
   across 2000–2026** (tolerance was 60″). Model: mean anchor
   23.245524743° at JD 2435553.5 ET + Δ(accumulated general precession
   in longitude) + nutation of date.
2. **Drik Panchang cross-check (1 Jan 2000, Kochi):** our Moon nakshatra
   (Chothi/Swati), tithi window, chandra rashi (Thulam), Sun rashi
   (Dhanu) all agree.
3. **Conventions-ledger finding:** Drik Panchang *displays* ayanamsha
   23.863781° for that date while JHora's table says 23°51′12″
   (23.8533°) — a ~38″ spread between two SE-based tools' displayed
   values. Users comparing apps will see such deltas; our engine must
   document its exact model (feeds the validation-strategy ticket).
4. Retrograde flags (finite-difference speed) match history (Mercury R
   May 1990, Saturn R Jan 2000).
5. True vs mean Rahu differ by ~1° in the test births — enough to flip
   a pada, occasionally a nakshatra: the convention choice is visible
   to users and must be pinned (JHora default = true node).

## Pending manual verification (HITL)

Graha longitudes and lagna for the three test births await arc-minute
comparison against Jagannatha Hora (Lahiri, true node, whole signs) by
the founder. Ayanamsha itself is already JHora-validated via the
published table.

## Run it

```
python -m venv .venv && .venv\Scripts\pip install skyfield
.venv\Scripts\python run_spike.py   # downloads de421.bsp (~17 MB) once
```
