---
title: "Birth chart (jathakam) computation logic — a build-from spec"
date: 2026-07-18
ticket: 004-engine-architecture
status: complete
method: "Verifies and extends docs/research/kerala-astrology-domain-research.md §3–4 and the closed astronomy-layer spike (spikes/astronomy-layer/) against primary sources: Meeus Astronomical Algorithms, IAU 2006 precession (Capitaine et al. 2003), BPHS (Santhanam translation + a second public-domain BPHS transcription on archive.org, cross-checked), Surya Siddhanta (Burgess translation), Sewell & Dikshit's The Indian Calendar (1896), the IANA tz database source, and Swiss Ephemeris documentation (as the cross-validation oracle, not a dependency). Tagged [FACT] / [TRADITION] / [ENG] per the domain doc's convention; secondary-only claims are explicitly flagged as lower-confidence."
---

# Birth chart (jathakam) computation logic

**Purpose:** a step-by-step spec an engineer can implement directly, from raw inputs (birth date, time, place) to a complete jathakam: graha positions, lagna, whole-sign bhavas, nakshatra/pada, navamsha (D9), panchanga (tithi/vara/yoga/karana), rahukalam/gulikakalam/yamakanda, and the Vimshottari dasha tree. It builds on, and does not repeat, [`kerala-astrology-domain-research.md`](kerala-astrology-domain-research.md) §3–4 and the closed [astronomy-layer spike](../../spikes/astronomy-layer/README.md) (ticket [001](../wayfinder/engineering/tickets/001-astronomy-layer-spike.md)). Where this doc adds or corrects something, it says so explicitly (§9).

**Tagging convention (reused from the domain doc):** **[FACT]** verifiable fact. **[TRADITION]** doctrine reported neutrally. **[ENG]** engineering recommendation. Added here: **[PINNED]** a convention this repo has already chosen (per the closed spike), **[OPEN]** a convention still undecided, and **[LOW-CONF]** a claim sourced only from secondary/practitioner sites because no primary text was locatable — treated as provisional, not authoritative.

---

## 1. Inputs and the timezone problem

**Required:** `{ birth_date, birth_time (local, claimed clock-face reading), place }`. Place must resolve to `(lat, lon, IANA tz id)` — not a raw UTC offset — because the offset itself is a function of date, not just place. [ENG]

### 1.1 Why a raw "+5:30" is wrong for historical births [FACT]

India's clock history is not a flat UTC+5:30 back to year zero:

- **Pre-1906:** Madras, Calcutta (Howrah), and Bombay ran on distinct local mean times (Madras Observatory fixed Madras time at +5:30:21 in 1802; Calcutta and Bombay used their own meridians) ([Wikipedia, *Indian Standard Time*](https://en.wikipedia.org/wiki/Indian_Standard_Time)).
- **1 Jan 1906:** IST (UTC+5:30, meridian 82.5°E near Allahabad) adopted as the national standard — but **Calcutta Time persisted locally until 1948 and Bombay Time until 1955** ([Wikipedia, *Time in India*](https://en.wikipedia.org/wiki/Time_in_India)); a birth record from a Calcutta or Bombay hospital in that window may reflect the *local*, not national, clock.
- **WWII "war time":** the IANA tz database's own `Zone Asia/Kolkata` table encodes two wartime UTC+6:30 ("double summer time"–style) shifts — 1941 Oct to 1942 May 15, and 1942 Sep to 1945 Oct 15 — before settling permanently at UTC+5:30 ([IANA tz database, `asia` source file, `Zone Asia/Kolkata`](https://github.com/eggert/tz/blob/main/asia)). A 1942 birth converted with a flat +5:30 will be off by an hour.

**[ENG, PINNED-by-implication]** Never hardcode `+05:30`. Resolve place → IANA tz id (`Asia/Kolkata` for all of modern India; there is only one zone, but its *historical offset table* carries the above transitions) and convert local→UTC through a maintained tz database (e.g. `zoneinfo`/`tzdata`, not a hand-rolled offset table) so pre-1906, 1906–1955 regional, and WWII-era anomalies resolve correctly without special-casing them in app code. This is the concern the domain doc's §3.0 already flagged generically ("use the IANA tz database... never a hardcoded offset"); this section pins down *why*, with the specific historical windows that would silently corrupt a chart if skipped.

### 1.2 UTC → Julian Day [FACT, PINNED]

Standard Julian Day conversion from the Gregorian calendar date and UT fraction-of-day, per Meeus, *Astronomical Algorithms* 2nd ed., ch. 7 (the same formula `swe_julday()` implements, and the same one Skyfield's `timescale().utc()`/`ut1()` wraps internally — the spike's `run_spike.py` calls `ts.ut1(...)`). Ephemeris lookups additionally need **JD(TT)** (Terrestrial Time), i.e. JD(UT) + ΔT; both Skyfield and Swiss Ephemeris carry their own ΔT tables so this does not need reimplementing. No open question here — this step is identical regardless of which astronomy source is used.

### 1.3 Unknown birth time [ENG]

Per the domain doc: if birth time is unknown, lagna/bhavas/dasha balance are unavailable (all need the exact instant), but rashi (from Sun/Moon date-level position) and — if the date is known precisely enough — the Moon's nakshatra are usually still computable to within a pada or so of uncertainty (the Moon moves ~13°/day, i.e. a full nakshatra in about a day, so a day-only birth date leaves real ambiguity here too — flag it in the UI rather than silently picking a default time).

---

## 2. Raw ephemeris positions

Per the closed spike (ticket 001): **Skyfield (MIT) + JPL DE421**, apparent geocentric ecliptic-of-date longitudes (light-time + aberration + nutation applied) — the same frame Swiss Ephemeris uses by default, which is why the spike's outputs are JHora-comparable. This is the **one seam** where external astronomical data enters the engine (`spikes/astronomy-layer/ephemeris.py`). Everything from here down (ayanamsha, rashi, nakshatra, lagna, nodes, vargas, panchanga, dasha) is arithmetic this repo owns. **[PINNED]**

Retrograde flag: finite-difference speed (1-hour forward difference in the spike; production should use a symmetric or analytic derivative for better precision near stations) — sign of `dλ/dt` gives direct/retrograde. **[FACT, PINNED as method; implementation detail — finite-difference step size — OPEN for refinement]**

---

## 3. Ayanamsha / sidereal conversion

**Sidereal longitude = tropical longitude − ayanamsha (mod 360°).** [FACT]

**Model pinned by the spike** (`spikes/astronomy-layer/ayanamsha.py`), reproduced here because it's load-bearing for every downstream step:

```
ayanamsha_true(t) = mean_anchor + [p_A(t) − p_A(t0)] + Δψ(t)
```

- **Anchor:** 23°15′00.658″ at JD 2435553.5 ET (1956 Mar 21.0), from the **Indian Astronomical Ephemeris 1989** (the Lahiri/Chitrapaksha defining epoch — Spica at 180° sidereal), converted to a *mean* anchor by removing nutation-at-epoch (documented in Swiss Ephemeris's own `sweph.h` ayanamsha table, which cites the same IAE anchor and nutation subtraction per Wahr 1980).
- **Accumulated general precession p_A(t):** IAU 2006 precession, **Capitaine, Wallace & Chapront (2003), A&A 412, 567** — the polynomial the spike's `general_precession_longitude_arcsec()` implements verbatim.
- **Nutation Δψ(t):** truncated IAU 1980 series (13 largest terms), **Meeus, *Astronomical Algorithms* 2nd ed., ch. 22**.

**Validated result (already in the spike's README):** agrees with the JHora-published Lahiri table to **≤0.6″ across 2000–2026** (tolerance budget was 60″). **[FACT, PINNED]**

**Ayanamsha choice itself** — Lahiri/Chitrapaksha as default, Raman/KP offered as settings — is a **[TRADITION-as-convention, PINNED default]** decision already made in the domain doc §3.2/§6.2; nothing in this research changes it. One nuance worth carrying into the conventions ledger: the spike found Drik Panchang *displaying* a ~38″ different "Lahiri" value than JHora's table for the same date even though both are Swiss-Ephemeris-based — meaning "Lahiri" is not a single universally-agreed number even among mainstream tools, so documenting *this repo's exact model* (as above) is the only real defense against "your app doesn't match X" support tickets.

Rashi, degrees-in-sign, and retrograde/combustion flags follow mechanically as already specified in domain doc §3.2 — no changes.

---

## 4. Lagna (ascendant)

Pinned by the spike (`spikes/astronomy-layer/lagna.py`), first-principles chain:

1. **GMST** — Meeus AA 2nd ed. eq. 12.4 (IAU 1982 expression), a polynomial in Julian centuries since J2000.
2. **Local apparent sidereal time (LAST)** = GMST + east longitude + equation of the equinoxes (`Δψ·cos ε`).
3. **Obliquity ε** — mean obliquity, IAU 2006 polynomial (Meeus 22.2 update); **nutation-in-obliquity omitted** (< 10″ effect on ε) — noted in the spike as a refinement candidate for production, currently inside the arc-minute error budget. **[OPEN — low-priority refinement]**
4. **Tropical ascendant:**
   `asc = atan2( cos(LAST), −(sin(LAST)·cos ε + tan φ·sin ε) )`
   — the standard spherical-astronomy rising-sign formula (given in Meeus and any astronomical-almanac treatment of horoscope houses; not BPHS-specific, since it's pure geometry of the ecliptic crossing the eastern horizon).
5. **Sidereal lagna** = tropical ascendant − ayanamsha (§3).

**[FACT, PINNED]** Already cross-validated: Drik Panchang agreement on chandra rashi/Sun rashi for the 1 Jan 2000 Kochi test case (spike README, finding 2). Full arc-minute verification of lagna against JHora for the 3 test births is still an open to-do carried into the validation-strategy ticket, not this one.

**High-latitude edge case** (ascendant math breaks >66°) — irrelevant for Kerala births, relevant for diaspora users; guard with a bounds check and a clear error rather than silent garbage. **[ENG]**

---

## 5. Whole-sign bhavas (houses)

This is one of the two gaps flagged as under-specified. Verified:

**The rule:** the rashi containing the lagna *is* the 1st bhava, in its entirety (not just the degrees past the ascendant point); the next rashi (in zodiacal order) is the 2nd bhava; and so on around all 12 signs. A planet's bhava = its rashi's offset from the lagna rashi, full stop — there is no separate cusp calculation. **[FACT as a fixed convention]**

```
bhava_number(sidereal_rashi_index) = ((rashi_index − lagna_rashi_index) mod 12) + 1
```

**Sourcing, honestly assessed:**

- Every Parashari-tradition text applies house-results directly to whichever rashi occupies that position from the lagna (e.g. BPHS's "Judgement of Houses" chapter — chapter 11 in the Santhanam translation's table of contents — reasons entirely in terms of "the Nth sign from lagna," never in terms of a separately-computed cusp). This is the operative convention throughout BPHS, Brihat Jataka, and Phaladeepika, but no classical text states "we hereby define houses = whole signs" as an explicit axiom to quote — it's the assumption everything else is built on, which makes it *harder* to pin to one verse than to a broader body of practice. **[TRADITION, FACT-level confidence in the convention itself]**
- The best explicit historical/technical treatment of *why* whole-sign houses are the original system (not a simplification of something else) is **Robert Hand, *Whole Sign Houses: The Oldest House System*** (ARHAT Publications, 2000) — a study of Hellenistic astrology showing the sign-house (whole-sign) system predates quadrant/cuspal systems, a lineage that carried into Indian astrology via the Hellenistic-Indian astrological exchange. This is offered as corroborating historical context, not as the source of the Indian convention itself, which is independently and universally attested in the Sanskrit texts. ([Hand's paper, hosted copy](https://ia800503.us.archive.org/2/items/244115255horaryastrologywholesignhousesbyroberthandpdf/244115255-Horary-Astrology-Whole-Sign-Houses-By-Robert-Hand-pdf.pdf))
- **Bhava-chalit / Sripati (cuspal) houses** exist as a documented alternative in later/regional practice (mentioned in domain doc §3.3) but are explicitly out of scope for v1 — whole-sign is the default and the only system this doc specifies.

**[PINNED]** Default whole-sign, per domain doc §3.3 — this research confirms the rule is exactly the mechanical offset above and finds no variant reading worth worrying about for Kerala practice specifically.

---

## 6. Nakshatra and pada

No changes from domain doc §3.4 — confirmed against the spike's `jyothisham.py`:

```
nakshatra_index = floor(sidereal_deg / (360/27))     # 0 = Ashwathi … 26 = Revathi
pada = floor((sidereal_deg mod (360/27)) / (360/27/4)) + 1
```

The Moon's nakshatra is the janma nakshatram/naal; every graha and the lagna also fall in a nakshatra (used in KP-style and some prashna rules). **[FACT, PINNED]**

---

## 7. Navamsha (D9) — verified in detail

This was the other explicitly flagged gap. Verified directly against BPHS chapter 6 text (two independent public-domain transcriptions cross-checked: the Santhanam-translation table of contents titles chapter 6 **"The Sixteen Divisions of a Sign"**; a second BPHS transcription on archive.org gives the operative verse, **sloka 12**, in almost these words: *"The Navamsa calculations are for a Movable Rasi from there itself, for a Fixed Rasi from the 9th thereof and for a Dual Rasi from the 5th thereof"* — [archive.org, *Parashara Hora Sastra*](https://archive.org/stream/ParasharaHoraSastra/BrihatParasharaHoraSastraVedicAstrologyEbook_djvu.txt)). This confirms the domain doc §3.5 sketch is complete and gives it a verse-level citation it previously lacked.

**The rule, spelled out as an algorithm:**

1. Each 30° rashi divides into 9 navamsha-padas of 3°20′ each (`30/9`).
2. `navamsha_pada_in_sign = floor(deg_in_sign / 3°20′)`, an index 0–8.
3. Pick a **starting sign** based on the rashi's *mode* (chara/sthira/dwiswabhava — movable/fixed/dual):
   - **Movable** (Mesha/Aries, Karkidakam/Cancer, Thulam/Libra, Makaram/Capricorn) → start counting from **the sign itself**.
   - **Fixed** (Edavam/Taurus, Chingam/Leo, Vrischikam/Scorpio, Kumbham/Aquarius) → start from **the 9th sign from it**.
   - **Dual** (Midhunam/Gemini, Kanni/Virgo, Dhanu/Sagittarius, Meenam/Pisces) → start from **the 5th sign from it**.
4. `navamsha_sign = (start_sign_index + navamsha_pada_in_sign) mod 12`.

Equivalently — and this is a useful implementation shortcut worth stating explicitly since it isn't spelled out in most secondary write-ups — **all three starting-sign rules collapse to counting from Aries for fire-triplicity signs, Capricorn for earth, Libra for air, and Cancer for water** (i.e., from whichever movable sign shares the graha's sign's element), which is mathematically identical to the movable/fixed/dual rule above and is how most implementations actually code it. Both framings are given so the engineer can sanity-check one against the other.

**Vargottama** (graha in the same sign in D1 and D9 — a strength marker) is a direct byproduct of this computation, no extra logic needed.

**Ship order** — per domain doc §3.5: D1, D9 first; D10/D7/D12/D30 and the full shodashavarga can follow later, using the identical "N equal slices, fixed starting-sign rule" pattern generalized per varga (each has its own starting-sign table in BPHS ch. 6 — out of scope to fully enumerate here since only D9 was the flagged gap; **[OPEN]** for whichever varga ships next).

---

## 8. Panchanga elements

### 8.1 Formulas, with a firmer citation than "Meeus" alone

Meeus's *Astronomical Algorithms* does **not** actually cover the Hindu tithi/karana/yoga system (it's a book about positional/dynamical astronomy, not calendrics) — this is a correction to the task brief's assumption. The correct primary-adjacent citations are:

- **Surya Siddhanta** (the classical Sanskrit astronomical treatise underlying Hindu calendrics; **Ebenezer Burgess's 1860 English translation** is public domain — [archive.org](https://archive.org/details/SuryaSiddhantaTranslation/)) defines the *ahoratra* (civil day) as running sunrise-to-sunrise, and the tithi as 1/30 of the Moon's synodic month.
- **Robert Sewell & Sankara Balkrishna Dikshit, *The Indian Calendar*** (Swan Sonnenschein, 1896) — the standard 19th-century academic reconciliation of Hindu lunisolar calendrics with the Julian/Gregorian calendar, public domain, full text on [archive.org](https://archive.org/stream/IndianCalendarSewelDikshit/Indian%20calendar-Sewel-Dikshit_djvu.txt) — states the formulas in exactly the form needed:
  - *"A tithi = 1/30th of the moon's synodic revolution"* (i.e. 12° of Moon−Sun elongation).
  - *"A karana is half a tithi, or the time during which the difference of the longitudes of the sun and moon is increased by 6 degrees."*
  - *"The period of time during which the joint motion in longitude, or the sum of the motions, of the sun and moon is increased by 13°20′, is called a yoga."*
- **Nachum Dershowitz & Edward Reingold, *Calendrical Calculations*** (and their standalone paper "Calendrical Calculations for the Indian Calendar") give the same three definitions in directly implementable pseudocode form and are the standard modern computer-science reference for this — treat as a secondary/technical source that corroborates Sewell & Dikshit rather than a competing primary source.

With sidereal longitudes S (Sun), M (Moon), all mod 360°:

```
tithi   = floor(((M − S) mod 360) / 12°) + 1                     # 1..30
karana  = floor(((M − S) mod 360) / 6°) + 1                       # 1..60 within the lunar month
yoga    = floor(((M + S) mod 360) / (13+1/3)°) + 1                # 1..27
vara    = weekday of the sunrise-to-sunrise civil day (Sun=1 … Sat=7), ruler sequence Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn
```

**Karana naming** — 11 named karanas over 60 half-tithi slots per lunar month: **4 "fixed" karanas** (Kimstughna, Shakuni, Chatushpada, Naga) occur exactly once each, always adjacent to new moon; **7 "movable" karanas** (Bava, Balava, Kaulava, Taitila, Gara, Vanija, Vishti/Bhadra) repeat cyclically 8× to fill the remaining 56 slots. Concretely: half-tithi index 1 in the lunar month → Kimstughna; indices 58–60 → Shakuni, Chatushpada, Naga; indices 2–57 cycle through the 7 movable karanas in fixed order. **[FACT, per Sewell & Dikshit and corroborated by the standard secondary treatment, e.g. the [Wikipedia *Karana (Hindu astrology)*](https://en.wikipedia.org/wiki/Karana_(Hindu_astrology)) summary]**

### 8.2 The sunrise convention — a pinned choice, not a free variable

**Vara (weekday) boundaries, and by extension "which day's panchanga" a birth or a query falls under, run sunrise-to-sunrise, not midnight-to-midnight** — this is the *ahoratra* definition from Surya Siddhanta and is universal Indian panchanga practice (also why a birth at 1am is "yesterday's" nakshatra/tithi-day in some traditional reckonings until sunrise). **[FACT, PINNED]** Sunrise/sunset for a given date and place is itself a standard astronomical computation (the domain doc already names `swe_rise_trans()`; Skyfield has an equivalent almanac-search routine) — no new formula needed, just noting that this dependency exists and must use *true* (refraction-corrected, local-horizon) sunrise, not a generic "6am" approximation, because rahukalam/gulikakalam (§8.3) and pirannal (naal-based birthday) both key off it.

### 8.3 Rahukalam / Gulikakalam / Yamakanda — sourced, but flagged lower-confidence

**Shared formula (well-corroborated, [FACT]):** divide the sunrise-to-sunset daylight span into **8 equal segments**. Each of the three "kalams" occupies one segment, chosen by a fixed weekday→segment-index lookup. Night-time (sunset-to-sunrise) versions exist in principle by the same method but are not used in mainstream daily panchanga practice.

**The weekday→segment tables**, as reported consistently across the panchanga-software ecosystem:

| Weekday | Rahukalam segment | Gulikakalam segment | Yamakanda segment |
|---|---|---|---|
| Sunday | 8 | 7 | 5 |
| Monday | 2 | 6 | 4 |
| Tuesday | 7 | 5 | 3 |
| Wednesday | 5 | 4 | 2 |
| Thursday | 6 | 3 | 1 |
| Friday | 4 | 2 | 7 |
| Saturday | 3 | 1 | 6 |

(Segment 1 = sunrise to sunrise+1/8 of daylight, …, segment 8 = the last eighth before sunset.)

**Confidence assessment, per the sourcing standard:**

- The **Rahukalam** column is **[FACT-level confidence]** — it is reproduced identically and independently across every source checked (Wikipedia's *Rāhukāla* article, Prokerala, and multiple panchanga-calculator sites), which is strong convergent evidence even though none of them cites a specific classical verse by chapter/number. Wikipedia's article names *Muhurta Chintamani* and *Brihat Parashara Hora Shastra* as the doctrinal home of Rahukala generally, but does not pin the specific 8-segment table to a verse.
- The **Gulikakalam** and **Yamakanda** columns are **[LOW-CONF]** — sourced only from practitioner/panchanga-software sites (e.g. a Gulika-Kaal calculator page, a Yamagandam explainer), not from a classical text I could independently verify chapter-and-verse. They are *internally consistent* (each descends by one segment per weekday in a clean arithmetic pattern — Gulika starting at Saturday=1 and counting backward, matching the folk etymology "Gulika/Maandi is Saturn's portion, and Saturn rules Saturday" — Yamakanda showing a similar but offset pattern), which suggests a real underlying rule rather than random noise, but I could not confirm the rule's classical source text directly (candidates named by secondary sources: *Muhurta Chintamani*, *Kalaprakashika* — neither confirmed by direct inspection).
- **[ENG]** Because this feeds the home-screen daily card (per ticket [009](../wayfinder/tickets/009-daily-practice-card-design.md), which explicitly wants "practical, factual, never ominous" kalam display), **validate this table against the Mathrubhumi/Manorama printed Kerala panchangam for a real sample week before shipping** — this is exactly the kind of claim the domain doc's own sourcing standard (§5.1) says to downgrade rather than present as settled, and it's user-facing enough that a wrong table will visibly disagree with what Kerala users already own on their wall calendar.

---

## 9. Vimshottari dasha tree

### 9.1 Mahadasha assignment and balance-at-birth — verified against BPHS ch. 46

**Nakshatra-lord cycle:** the 27 nakshatras map cyclically (repeating 3×) onto the fixed 9-lord sequence — **Ketu(7) → Venus(20) → Sun(6) → Moon(10) → Mars(7) → Rahu(18) → Jupiter(16) → Saturn(19) → Mercury(17)**, years summing to 120, starting with Ketu at Ashwini/Ashwathi. **[FACT, fixed convention, BPHS ch. 46 "Dashas of Planets" — confirmed via the chapter's presence and title in the Santhanam translation's contents and a second transcription's chapter heading.]**

**Balance-of-dasha formula — directly quoted from a public-domain BPHS transcription, verse 16 of chapter 46** (paraphrased, not reproduced verbatim per the copyright posture in domain doc §5.1): multiply the birth-lord's full dasha-years by the **fraction of the janma nakshatra the Moon has already traversed** at birth; that gives the *elapsed* portion of the first mahadasha; subtract from the full period to get the **balance** — the remaining mahadasha length carried into the chart. Equivalently:

```
elapsed_fraction = moon_deg_traversed_in_nakshatra / (360/27)     # 0..1
elapsed_years     = elapsed_fraction × lord's_full_dasha_years
balance_years     = lord's_full_dasha_years − elapsed_years
                  = (1 − elapsed_fraction) × lord's_full_dasha_years
```

This is exactly the domain doc §4.1 formula ("fraction of the nakshatra not yet traversed × that lord's full period") — now confirmed to trace to a specific, locatable verse rather than only to a general chapter reference. The classical text works the calculation in *palas* (a traditional time subunit) rather than degrees, but it is the same fraction either way since palas-elapsed / palas-total = degrees-elapsed / degrees-total.

### 9.2 Antardasha (bhukti) subdivision — chapter located, exact verse not independently recovered

BPHS dedicates a **separate later chapter — chapter 51, titled "Working out of Antar Dashas of Grahas and Rasis in Vimshottari etc. Dasha systems"** in the transcription checked — to this step, distinct from chapter 46's mahadasha-period table. I was not able to pull the specific verse's operative sentence from the available online transcriptions (search access to that chapter's body text was incomplete), so the exact subdivision rule below is **[TRADITION, near-universally implemented this way, but not independently verse-verified here — treat as high-confidence-secondary rather than primary-confirmed]**:

- Within a mahadasha of lord X (full length `Y_X` years), the 9 antardashas run in the **same fixed 9-lord cyclic sequence, starting from X itself**, each antardasha lord Z's length proportional to Z's own share of the 120-year cycle:

```
antardasha_length(Z within X's mahadasha) = Y_X × (Y_Z / 120)
```

  Sum of all 9 antardashas within X's mahadasha = `Y_X × (120/120) = Y_X` — the subdivisions exactly exhaust the mahadasha, which is the internal-consistency check worth asserting in tests.
- **Pratyantardasha** (and further sub-levels) apply the identical proportional rule recursively one level down, per domain doc §4.1 — not separately re-derived here since it's the same formula at a smaller scope.

**[ENG]** Precompute the full mahadasha→antardasha (optionally →pratyantardasha) tree at chart-build time, per domain doc §4.1 — it's pure arithmetic off the Moon's birth longitude, no external dependency.

### 9.3 Dasha year length: 365.25 vs 360 days — this research upgrades the domain doc's framing

The domain doc (§4.1, §6.3) treats 365.25-vs-360 as a software-convention question ("software differs; pick 365.25 and document it"). **There is in fact a classical-text argument for 365.25**, which is worth knowing when defending the choice: secondary scholarship on this exact question (Shyamasundara Dasa, *"How Long is a Year In Vimsottari Mahadasa?"*, citing **Phaladeepika** and the **Siddhanta Shiromani**) reports both classical texts stating the dasha year should be the **365.25-day solar (saura) year** — the time for the Sun to return to the same point — rather than the 360-day *savana* (civil-count) year. The practical stakes are real: the two conventions diverge by ~5 days/year, compounding to roughly a full year of drift by a person's 70s, which is exactly the kind of error a user comparing two apps' dasha tables would notice immediately. **[TRADITION with a locatable secondary-scholarship citation for the classical basis; 365.25 was already the pinned default per the spike's conventions-ledger concern, and this section gives that default a firmer doctrinal footing than "most software does it this way."]**

---

## 10. Conventions ledger — pinned vs. open (feeds ticket 004)

| Convention | Status | Value pinned | Source |
|---|---|---|---|
| Astronomy source | **PINNED** | Skyfield (MIT) + JPL DE421 | Spike, ticket 001 |
| Ayanamsha model | **PINNED** | Lahiri, IAE-1989 anchor + IAU 2006 precession + truncated IAU 1980 nutation | Spike `ayanamsha.py`; validated ≤0.6″ vs JHora table |
| Ayanamsha choice (vs Raman/KP) | **PINNED default**, others exposed as settings | Lahiri/Chitrapaksha | Domain doc §3.2, §6.2 |
| Rahu/Ketu node | **PINNED** | True node default (osculating, node-vector method); mean node also implemented | Spike `jyothisham.py`; JHora's documented default |
| Lagna method | **PINNED** | GMST (Meeus 12.4) + eq. of equinoxes + standard ascendant formula; nutation-in-obliquity omitted | Spike `lagna.py` |
| House system | **PINNED** | Whole-sign (bhava = rashi from lagna); bhava-chalit/Sripati out of scope for v1 | §5 above; domain doc §3.3 |
| Navamsha (D9) starting-sign rule | **PINNED, now verse-cited** | Movable: same sign; fixed: 9th; dual: 5th | §7 above, BPHS ch. 6 sloka 12 |
| Tithi/karana/yoga formulas | **PINNED** | 12°/6°/13°20′ thresholds on M−S and M+S | §8.1, Sewell & Dikshit 1896 |
| Vara/day boundary | **PINNED** | Sunrise-to-sunrise civil day | §8.2, Surya Siddhanta *ahoratra* |
| Rahukalam weekday table | **PINNED, FACT-confidence** | Table in §8.3 | Convergent secondary sources |
| Gulikakalam / Yamakanda weekday tables | **OPEN pending validation** | Table in §8.3 (best available) | **[LOW-CONF]** — validate against Mathrubhumi/Manorama printed panchangam |
| Dasha year length | **PINNED**, now with doctrinal backing | 365.25-day solar year | §9.3, Phaladeepika/Siddhanta Shiromani per secondary scholarship |
| Vimshottari balance/antardasha formulas | **PINNED** | §9.1–9.2 | BPHS ch. 46 (verse-cited), ch. 51 (chapter-cited, verse not independently confirmed) |
| Timezone handling | **PINNED as a requirement, not a value** | Resolve via IANA tzdata, never a hardcoded offset | §1.1, IANA `asia` source file |

---

## 11. What this changes or adds versus the domain research doc

1. **Meeus does not cover panchanga arithmetic** — the domain doc's §3.6 header implies Swiss-Ephemeris/Meeus-style sourcing throughout; the correct citations for tithi/karana/yoga are Surya Siddhanta (Burgess translation) and Sewell & Dikshit's *The Indian Calendar* (1896), with Dershowitz & Reingold as a modern computational corroboration. Worth a small correction if §3.6 is ever revised.
2. **Navamsha now has a verse-level citation** (BPHS ch. 6, sloka 12) instead of a general "see Santhanam translation" pointer — confirms the domain doc's §3.5 sketch was already correct and complete, nothing to change there.
3. **Whole-sign houses**: the domain doc states the convention correctly but doesn't source it; this doc adds the Robert Hand historical citation as corroborating context and locates BPHS's operative practice (ch. 11) as the doctrinal home, while being honest that no verse says "houses are whole signs" as a bare axiom — it's the assumption the whole tradition runs on.
4. **Vimshottari balance formula is now verse-located** (BPHS ch. 46, verse 16) rather than only chapter-referenced; the antardasha rule's *chapter* is located (ch. 51) but its exact verse wasn't independently recoverable through the transcriptions checked — flagged honestly rather than overclaimed.
5. **The 365.25-vs-360 dasha-year choice has a classical-text argument behind it** (Phaladeepika, Siddhanta Shiromani, per secondary scholarship), upgrading it from "pick one, most software agrees" to a doctrinally defensible default — still the same pinned value, better justified.
6. **Rahukalam/gulikakalam/yamakanda is the weakest-sourced section in this whole document** — the domain doc doesn't cover it at all (it's new territory this research was asked to fill), and the honest finding is that only Rahukalam's table converges strongly across sources; Gulikakalam and Yamakanda's tables are plausible and internally consistent but not independently verse-verified. Given this feeds a shipped home-screen feature (ticket 009), it's the single most important item to validate against a real printed Kerala panchangam before launch.
7. **The IST/timezone historical-anomaly detail (Calcutta/Bombay time to 1948/1955, WWII "war time" in the tz database itself)** is new and concrete — the domain doc gestured at "historical timezone handling matters" without specifics; this doc gives the actual windows and shows the IANA tz database already encodes them, so the engineering answer is "use a real tz library," not "build a lookup table."
