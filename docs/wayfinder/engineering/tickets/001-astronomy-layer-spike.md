---
id: 001
title: Astronomy layer spike — positions in, sidereal conversion ours, validated against JHora
label: wayfinder:prototype
status: closed
assignee: akhil (claimed 2026-07-17, spike session; resolved 2026-07-17)
blocked-by: []
---

## Question

Pick the astronomy data source and prove our sidereal conversion before anything is built on it. Build a throwaway spike: Skyfield (or JPL kernels directly, or another MIT-licensed astronomy route) → tropical longitudes for the 9 grahas + lagna inputs at 3 test birth instants → **our own** Lahiri/Chitrapaksha ayanamsha correction → sidereal longitudes, rashi, nakshatra/pada. Assert arc-minute agreement with Jagannatha Hora for the same births (JHora is the practitioner-standard oracle). Decisions this resolves: which astronomy library/data source the spec names; where the published Lahiri definition comes from (cite it); true-vs-mean Rahu convention (match JHora's default); whether lagna computation (sidereal time → ascendant) is accurate enough from first principles. The spike is a discussion artifact, not production code — its findings and citations go in the resolution; the code is linked as an asset.

## Resolution (2026-07-17)

Asset: [`spikes/astronomy-layer/`](../../../../spikes/astronomy-layer/README.md) (Skyfield + our ayanamsha/rashi/nakshatra/lagna/node code, all cited).

Decisions this resolves:

1. **Astronomy source: Skyfield (MIT) + JPL DE421** (1900–2050 coverage; upgrade path to DE440 if ever needed). It supplies apparent geocentric ecliptic-of-date longitudes only — the same frame Swiss Ephemeris uses, hence JHora-comparable. This is the single seam where external data enters the engine.
2. **Lahiri model pinned and validated:** mean anchor 23.245524743° at JD 2435553.5 ET (IAE 1989's 23°15′00.658″ minus nutation at epoch, per the SE `sweph.h` documentation of the primary source) + accumulated general precession in longitude (IAU 2006, Capitaine et al. 2003) + nutation of date (truncated IAU 1980 series, Meeus ch. 22). **Agrees with the JHora-published Lahiri table to ≤0.6″ across 2000–2026** — tolerance was 60″.
3. **Lagna from first principles works:** GMST (Meeus 12.4) + equation of the equinoxes + standard ascendant formula. Nutation-in-obliquity refinement noted for the production engine.
4. **Node convention: implement both, default TRUE node** (JHora's default; computed ourselves from Moon state vectors via the osculating node-vector method; mean node per Meeus ch. 47 also implemented). True vs mean differ ~1° — visibly flips padas; the choice must appear in the conventions ledger.
5. **Cross-validation:** Drik Panchang (1 Jan 2000, Kochi) confirms our Moon nakshatra, tithi, chandra rashi, Sun rashi. **Conventions-ledger finding:** Drik *displays* ayanamsha 23.8638° where JHora's table says 23.8533° (~38″ apart) — even SE-based apps show variant "Lahiri" values; our engine documents its exact model.
6. Closed on this evidence by founder decision; **full graha/lagna arc-minute verification of the 3 test births in JHora itself is carried as a to-do into the validation-strategy ticket** (JHora golden fixtures were already its subject).
