# Kerala Astrology (Jyothisham) — Domain Research for an AI Astrologer App

**Date:** 2026-07-17
**Purpose:** Seed the domain knowledge base for an Astrotalk-style consultation app where the astrologer is an AI, focused on Kerala-style astrology.

**Epistemic framing used throughout this document:**
- **[FACT]** — verifiable historical, bibliographic, astronomical, or software fact.
- **[TRADITION]** — interpretive doctrine reported neutrally ("the tradition holds…"). These are practitioner beliefs, not empirically validated claims. The app should present them as traditional interpretation, never as guaranteed prediction.
- **[ENG]** — engineering recommendation for the app.

---

## 1. Executive summary

- Kerala jyothisham sits inside mainstream Indian sidereal (nirayana) astrology but has a distinct identity built on three pillars: (a) an exceptionally strong **prashna (horary)** tradition codified in the 1649 CE Kerala text **Prashna Marga**, including temple-centred **Ashtamangala/Deva Prashna** rituals with cowrie-shell (kavadi) divination; (b) a deep **commentarial tradition on Varahamihira's Brihat Jataka** (the *Dashadhyayi*); and (c) the historical **Kerala school of astronomy/mathematics** (Parameshvara's drig-ganita observational corrections, Nilakantha Somayaji's Tantrasangraha), whose computational rigor shaped Kerala panchanga practice. Kerala daily life additionally runs on the **Kollavarsham (Malayalam solar calendar)** and the **birth star (naal/janma nakshatram)** — a Malayali's traditional birthday (*pirannal*) is nakshatra-based, not date-based.
- The **birth-chart computation pipeline** is fully deterministic and implementable: birth time → UTC → Julian Day → planetary ecliptic longitudes (Swiss Ephemeris) → subtract ayanamsha (Lahiri/Chitrapaksha is the Indian government standard) → rashi/nakshatra/pada, lagna from local sidereal time, bhavas, vargas (navamsha etc.), panchanga elements, and Vimshottari dasha periods. Render in the **South Indian square chart** format (fixed signs, read clockwise), which is what Kerala users expect.
- The **interpretive layer** (dasha phala, gochara/Sade Sati, yogas, porutham marriage matching with the South Indian 10-porutham system, prashna judgment) is doctrine, sourced from classical texts with good English translations: BPHS (Santhanam), Brihat Jataka (Subrahmanya Sastri), Prashna Marga (B.V. Raman, 2 vols), Phaladeepika, Krishneeyam (N.E. Muthuswami).
- **Biggest engineering decisions/risks:** Swiss Ephemeris dual licensing (AGPL vs ~CHF 750 professional license) directly affects a commercial closed-source app; ayanamsha choice (default Lahiri, expose as setting); and Indian consumer-protection/ASCI advertising exposure if the app makes absolute predictive claims.

---

## 2. Kerala's astrological tradition — what makes it distinct

### 2.1 The Kerala school of astronomy and mathematics [FACT]

- The [Kerala school of astronomy and mathematics](https://en.wikipedia.org/wiki/Kerala_school_of_astronomy_and_mathematics) flourished ~14th–17th centuries, founded by Madhava of Sangamagrama; members included Parameshvara, Nilakantha Somayaji, Jyeshtadeva, and Achyuta Pisharati.
- [Vatasseri Parameshvara Nambudiri](https://en.wikipedia.org/wiki/Parameshvara_Nambudiri) (c. 1380–1460) founded the **drig-ganita** ("observation-based computation") system, revising planetary parameters against ~55 years of his own eclipse observations. Drig-ganita shifted Kerala practice from precomputed *vakya* (mnemonic sentence) tables toward direct, observation-corrected computation — an ethos that carried into Kerala panchanga making.
- Parameshvara taught the lineage leading to **Nilakantha Somayaji** (1444–1544), author of the *Tantrasangraha*, whose planetary model improved on the standard Aryabhatan scheme. Panchanga computation (timekeeping for rituals and astrological consultation) was the school's principal applied output.
- Definitive academic treatment: **K.V. Sarma, *A History of the Kerala School of Hindu Astronomy (in Perspective)*, Vishveshvaranand Institute, Hoshiarpur, 1972** — documents ~80 astronomers and 752 works of the school ([Wikipedia entry on the book](https://en.wikipedia.org/wiki/A_History_of_the_Kerala_School_of_Hindu_Astronomy), [Stanford catalog record](https://searchworks.stanford.edu/view/875819), [K.V. Sarma](https://en.wikipedia.org/wiki/K._V._Sarma)). A scanned copy circulates on [archive.org](https://archive.org/stream/KeralaSchoolOfAstronomy/Kerala%20School%20of%20Astronomy_djvu.txt).
- **Relevance to the app [ENG]:** you will *not* implement drig-ganita; modern ephemerides (Swiss Ephemeris/JPL) exceed its accuracy. Its value is narrative/branding authenticity and explaining why Kerala practitioners historically prized computational accuracy.

### 2.2 Prashna — Kerala's signature branch [FACT for the texts; TRADITION for the method]

- **Prashna Marga** ("The Path of Horary Astrology") was composed in **1649 CE by a Namboodiri Brahmin of Edakkad, near Thalassery, Kerala**. It is the most comprehensive treatise on prashna and covers horary, natal, muhurta, remedial astrology (parihara), and omens (nimitta). English translation with notes: **B.V. Raman, *Prasna Marga*, 2 volumes, Motilal Banarsidass** ([publisher page pt. 1](https://www.motilalbanarsidass.com/en-us/products/prasna-marga-part-1-english-translation-with-original-text-in-devanagari-and-notes), [pt. 2](https://www.motilalbanarsidass.com/en-us/products/prasna-marga-part-2-english-translation-with-original-text-in-devanagari-and-notes), [AstroAmerica listing](https://astroamerica.com/text/prasnamarga.html)). Scans exist on [archive.org](https://archive.org/stream/PrasnaMargaBVR/Prasna%20Marga%202_djvu.txt).
- **Krishneeyam** (attributed to Krishna Acharya) is an **older, shorter Kerala horary text** — both Prashna Marga and the Dashadhyayi quote it. It focuses on selected horary topics (notably *nashta prashna*, lost-object queries) and has some doctrinal differences (drekkana lords, planetary friendships). English edition: **N.E. Muthuswami, *Krishneeyam of Shree Krishna Acharya*** ([listing](https://jyotishbooks.wordpress.com/2021/12/14/krishneeyam-of-shree-krishna-acharya-by-n-e-muthuswami/), [Sagar Publications edition](https://sagarpublications.com/astrology/krishneeyam/), overview at [IndiaDivine Kerala Texts thread](https://www.indiadivine.org/content/topic/1417855-kerala-texts/)). Other published Kerala prashna works mentioned in the same tradition: *Prashnanushtana Paddhati*, *Prashnayanam* (verify specific editions before citing in-app).
- **[TRADITION] Core prashna idea:** instead of the birth chart, a chart is cast for the **moment the question is asked** (or the moment the astrologer takes up the query), and judged with special significators — the **arudha** (sign indicated by the querent, e.g., where the querent touches or where a lot falls) alongside the ascendant of the moment.

### 2.3 Ashtamangala Prashna / Deva Prashna [TRADITION, practice verifiably exists]

- [Ashtamangala prasnam](https://en.wikipedia.org/wiki/Ashtamangala_prasnam) is an elaborate Kerala/Tulu Nadu prashna ritual using **eight auspicious objects** (ghee lamp, mirror, gold, milk, curd, fruits, book, white cloth). Its methodology is documented in Prashna Marga.
- **Cowrie shells (kavadi):** the astrologer uses ~108 sanctified cowries; after invocation, they are divided into piles and counted off in multiples of eight; remainders yield the **ashtamangala number** (a 3-digit figure whose digits are read for omens) and the **arudha rashi**. A detailed practitioner account is Shyamasundara Dasa's four-part series ([part 1](https://shyamasundaradasa.com/jyotish/resources/articles/adp/ashtamangala_deva_prasna_1.html), [part 2](https://shyamasundaradasa.com/jyotish/resources/articles/adp/ashtamangala_deva_prasna_2.html), [part 3](https://shyamasundaradasa.com/jyotish/resources/articles/adp/ashtamangala_deva_prasna_3.html), [part 4](https://shyamasundaradasa.com/jyotish/resources/articles/adp/ashtamangala_deva_prasna_4.html)).
- **Deva Prashnam** is the temple variant: conducted in temple premises to diagnose issues concerning the deity, temple administration, or community/ancestral matters ([practitioner overview](https://bestkeralaastrologer.com/blog/kerala-astrologer-tradition-prasna-deva-prashnam-explained), [example service pages](http://astrologer.swayamvaralaya.com/prasnams/)).
- **[ENG]** For the app, a "quick prashna" mode can be honest and mechanizable: cast a chart for the question timestamp; simulate the cowrie division with a random draw the user triggers (tap to "cast"), yielding an arudha sign and ashtamangala number, then interpret per Prashna Marga rules. Label clearly as a digital adaptation of the ritual; full Ashtamangala/Deva Prashna is a multi-day human ritual and should not be impersonated.

### 2.4 Kollavarsham, naal, and the birth star [FACT]

- The **Malayalam calendar (Kollavarsham)** is Kerala's traditional **solar** calendar (months = Sun's transit through sidereal signs: Chingam, Kanni, … Karkidakam); it anchors festivals, agricultural timing, and traditional birthdays ([Prokerala Malayalam calendar](https://www.prokerala.com/general/calendar/), [usvishakh Malayalam calendar 1900–2049](https://malayalam.usvishakh.net/calendars/150calendars.html)).
- **Naal / janma nakshatram:** Kerala practice emphasizes the **birth star** above the birth date. The 27 nakshatras carry Malayalam names (Ashwathi, Bharani, Karthika, Rohini, Makayiram, Thiruvathira, Punartham, Pooyam, Aayilyam, Makam, Pooram, Uthram, Atham, Chithira, Chothi, Vishakham, Anizham, Thrikketta, Moolam, Pooradam, Uthradam, Thiruvonam, Avittam, Chathayam, Poororuttathi, Uthrattathi, Revathi) ([HinduPad Malayalam nakshatra list](https://hindupad.com/malayalam-nakshatra-list-27-janma-naal-in-malayali-calendar/), [Prokerala nakshatra finder](https://www.prokerala.com/astrology/nakshatra-finder/)).
- **Pirannal:** the traditional Malayali birthday is the recurrence of one's **janma nakshatram in one's birth Malayalam month**, so it drifts against the Gregorian date each year ([Nalla Naal pirannal finder](https://nallanaal.in/pirannal-finder)).
- **[ENG]** The app must speak this idiom: display nakshatras with Malayalam names (with IAST/English equivalents), compute pirannal dates, and show Kollavarsham dates alongside Gregorian. This is a differentiator vs. generic Hindi-market astrology apps.

### 2.5 The Kerala commentarial tradition on Brihat Jataka [FACT]

- Varahamihira's [Brihat Jataka](https://en.wikipedia.org/wiki/Brihat_Jataka) (6th c. CE) is the natal-astrology classic most revered in Kerala. The Kerala commentary [**Dashadhyayi**](https://en.wikipedia.org/wiki/Dasadhyayi) (on its first ten chapters) is traditionally attributed to [**Talakkulathur Govinda Bhattathiri**](https://en.wikipedia.org/wiki/Govinda_Bhattathiri) (c. 1237–1295); recent scholarship suggests Govinda wrote the earlier *Nauka* commentary and the Dashadhyayi is a 15th-century abridgment/rearrangement, with the attribution popularized by the 19th-century *Aithihyamala*. Kerala students traditionally memorized Brihat Jataka *with* the Dashadhyayi, and its interpretations are treated as authoritative in Kerala.
- The pan-Indian commentator **Bhattotpala** (10th c.) also remains a standard gateway to Brihat Jataka ([Bhattotpaliya edition listing](https://jyotishbooks.wordpress.com/2018/10/14/varahamihiras-brihat-jataka-with-bhattotpaliya-sanskrit-vivritti-classic-hindi-by-amit-kumar-shukla/)).
- **[ENG]** For English knowledge-base ingestion, use V. Subrahmanya Sastri's Brihat Jataka translation (which draws on Bhattotpala) — see §5.1.

---

## 3. Birth chart (jataka / grahanila) construction — computational pipeline

Everything in this section is standard, deterministic astronomy + fixed convention. All formulas are implemented by [Swiss Ephemeris](https://www.astro.com/swisseph/swephinfo_e.htm) and documented in its [programmer docs](https://www.astro.com/swisseph/swisseph.htm) and [programming interface reference](https://www.astro.com/swisseph/swephprg.htm). [FACT] unless noted.

### 3.0 Inputs

`{ birth_date, birth_time (local), place (lat, lon) }`. For India after 1948, timezone = IST (UTC+5:30), but **historical timezone handling matters** (pre-independence local times, DST elsewhere for diaspora users) — use the IANA tz database via the platform's datetime library, never a hardcoded offset. Unknown birth time is common; the app needs a fallback mode (Moon-chart/nakshatra-only readings, or prashna).

### 3.1 Local time → UTC → Julian Day

1. Resolve place → (lat, lon, IANA timezone) via a geocoding service.
2. Convert local civil time → UTC using the tz database.
3. Convert UTC → **Julian Day (JD)**; Swiss Ephemeris provides `swe_julday()` and internally handles ΔT (UT vs. TT) for ephemeris lookups ([swisseph docs](https://www.astro.com/swisseph/swisseph.htm)).

### 3.2 Planetary longitudes (grahas)

- Compute geocentric **ecliptic longitudes** for Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn via `swe_calc_ut()`.
- **Rahu/Ketu** = lunar nodes. Convention choice: **mean node** vs **true node** (Swiss Ephemeris offers both; Indian practice is split — many traditional panchangas use the mean node; expose as a setting, default **mean** or **true** but be consistent). Ketu = Rahu + 180°.
- **Sidereal conversion:** sidereal longitude = tropical longitude − **ayanamsha**. Set with `swe_set_sid_mode(SE_SIDM_LAHIRI, …)` — Swiss Ephemeris ships 40+ ayanamsha modes ([sidereal mode docs in pyswisseph manual](https://github.com/astrorigin/pyswisseph/blob/master/docs/programmers_manual/sidereal_mode.rst)).
- **Ayanamsha default: Lahiri (Chitrapaksha)** — the standard of the **Indian Astronomical Ephemeris / Rashtriya Panchang** published by the **Positional Astronomy Centre, Kolkata** (founded from the Nautical Almanac Unit whose first officer-in-charge was N.C. Lahiri). Its defining condition: the star Spica/Chitra at 180° sidereal (0° Libra). Value ≈ 24°07′–24°08′ in 2026 and increasing ~50.3″/yr ([developer explainer](https://roxyapi.com/blogs/ayanamsa-lahiri-raman-kp-developers), [reference values](https://jagannathhora.com/lahiri-ayanamsa-value/), [comparative academic paper on ayanamshas](https://casa-acharya.com/Orissa%20Journal%20of%20Physics/OJP_PDF_Files/31_2_4_FP.pdf)).
- **Kerala nuance [FACT/TRADITION]:** Kerala historically applied its own drig-ganita corrections rather than a single national ayanamsha; modern Kerala panchangams and software overwhelmingly use Lahiri, so default Lahiri and note the history. Offer Raman and KP (Krishnamurti) ayanamshas as options for users who follow those schools.
- Each longitude then yields: **rashi** = `floor(long / 30°)` (Medam/Aries … Meenam/Pisces, Malayalam names), degrees-in-sign, retrograde flag (from speed), and combustion (proximity to Sun — doctrinal orb values from BPHS).

### 3.3 Lagna (ascendant) and houses

- Ascendant = ecliptic degree rising on the eastern horizon at (JD, lat, lon): computed from local sidereal time + obliquity + latitude; Swiss Ephemeris `swe_houses_ex()` returns ascendant, MC, and cusps in one call, with sidereal flag applied ([house cusp docs](https://github.com/astrorigin/pyswisseph/blob/master/docs/programmers_manual/house_cusp_calculation.rst)).
- **House system:** Indian practice predominantly uses **whole-sign houses** (bhava = the whole rashi; 1st house = the entire rising sign) — use this as default. Traditional bhava-chalit (Sripati/Porphyry-style cusp charts) can be a later add-on. [TRADITION for the choice; FACT for the math.]
- High latitudes (>66°) break ascendant math — irrelevant for Kerala but guard for diaspora edge cases.

### 3.4 Nakshatra and pada

- The 27 nakshatras each span **13°20′** (800′); each divides into 4 **padas** of 3°20′.
- `nakshatra_index = floor(moon_sidereal_long / 13°20′)` (0 = Ashwathi/Ashwini … 26 = Revathi); `pada = floor(moon_sidereal_long / 3°20′) mod 4 + 1`.
- Every graha and the lagna also occupy a nakshatra (used in KP and in some prashna rules), but the **Moon's** nakshatra is *the* janma nakshatram/naal.

### 3.5 Divisional charts (vargas)

- A varga D-n maps each sign's 30° into n equal slices assigned to signs by fixed rules. Most important: **Navamsha (D9)** — each pada = one navamsha (3°20′); for movable signs count from the sign itself, fixed signs from the 9th sign, dual signs from the 5th (equivalently: from Aries/Capricorn/Libra/Cancer for fire/earth/air/water signs). Navamsha is mandatory for marriage analysis and planetary strength (vargottama = same sign in D1 and D9). [TRADITION for usage; the mapping is a fixed convention documented in BPHS ch. on vargas — see Santhanam translation, §5.1.]
- Ship at minimum: D1 (rashi), D9 (navamsha), D10 (dashamsha, career), D7 (children), D12 (parents), D30 (misfortunes) — the BPHS shodashavarga list can come later. PyJHora implements the full varga set if you want a reference implementation ([PyJHora](https://github.com/naturalstupid/PyJHora)).

### 3.6 Panchanga elements (the "five limbs") [FACT for formulas]

With sidereal longitudes `S` (Sun) and `M` (Moon):
- **Tithi** (lunar day, 30 per month): `floor(((M − S) mod 360°) / 12°) + 1`.
- **Vara** (weekday): from sunrise-to-sunrise local day; ruler sequence Sun…Saturn.
- **Nakshatra** (of the Moon): as in §3.4.
- **Yoga** (27): `floor(((M + S) mod 360°) / 13°20′) + 1`.
- **Karana** (half-tithi, 11 named): `floor(((M − S) mod 360°) / 6°)` mapped to the 4 fixed + 7 rotating karanas.
- Kerala panchangams present these daily plus muhurta windows (rahukalam etc.); see [Prokerala Malayalam panchangam](https://www.prokerala.com/astrology/malayalam-panchangam/) for the expected user-facing shape, and the [Mathrubhumi Panchangam](https://www.mbibooks.com/product/mathrubhumi-panchangam-2025-2026/) (compiled by Sadanam Narayanan Pothuval) as the printed reference Malayali users trust. Sunrise (needed for vara/dasha day boundaries and pirannal) comes from `swe_rise_trans()`.

### 3.7 Chart rendering [FACT for conventions]

- **South Indian square format**: 12 fixed boxes around an empty centre; **signs are fixed** (Aries always in the same box — second cell of the top row), read **clockwise**; the lagna is marked with a diagonal stroke in its box. This is the format used across Kerala/Tamil Nadu/Karnataka/AP, vs. the **North Indian diamond** format where **houses** are fixed and reading is counter-clockwise ([chart formats overview](https://www.vedicplanet.com/jyotish/learn-jyotish/chart-formats-in-jyotish-astrology/), [comparison article](https://www.gitudivinetouch.com/post/exploring-the-differences-between-north-indian-and-south-indian-astrology-charts)). Both encode identical data.
- Kerala convention: label with Malayalam sign/planet abbreviations (option for English). The full document of positions + panchanga + dasha table is what Malayalis call the **jathakam / grahanila**.

### 3.8 Pipeline summary (pseudo-flow) [ENG]

```
(place → lat,lon,tz) → local→UTC → JD
JD → swe_calc_ut × 9 grahas (sidereal, Lahiri) → rashi/degree/retro
JD,lat,lon → swe_houses_ex → lagna, whole-sign bhavas
moon_long → nakshatra, pada → naal (Malayalam name)
longs → vargas (D9 first) → varga positions
sun,moon longs (+sunrise) → tithi, vara, yoga, karana
moon nakshatra + fraction → Vimshottari dasha tree (§4.1)
render: South Indian square chart + panchanga block + dasha table
```

---

## 4. How predictions are made — the interpretive layer

Everything here is **[TRADITION]** (doctrine from the classical texts) except where the computation itself is marked. The AI layer should generate readings *grounded in these rule systems* and always framed as traditional interpretation.

### 4.1 Vimshottari dasha (the primary timing tool)

- **Computation [FACT as a fixed convention, defined in BPHS]:** a 120-year cycle of nine planetary periods: Ketu 7, Venus 20, Sun 6, Moon 10, Mars 7, Rahu 18, Jupiter 16, Saturn 19, Mercury 17 years (sum 120). Each nakshatra has a fixed lord in this sequence starting from Ashwini→Ketu. The **starting mahadasha** is the lord of the Moon's janma nakshatra; the **balance** at birth = (fraction of the nakshatra *not yet* traversed by the Moon) × (that lord's full period). Sub-periods (**antardasha/bhukti**, then pratyantardasha…) subdivide each period in the same 9-lord sequence starting from the period lord, proportionally to each lord's years/120. Source: BPHS dasha chapters ([Santhanam translation on archive.org](https://archive.org/details/BPHSEnglish)).
- **Interpretation [TRADITION]:** results of a dasha follow the period lord's natal condition — house placement, lordships, strength, conjunctions/aspects; antardasha lords modulate. This is the single most consulted feature in Indian consultations ("which dasha am I running?").
- **[ENG]** Precompute the full mahadasha/antardasha (and optionally pratyantar) tree at chart-build time; it's pure arithmetic off the Moon longitude and birth instant. Note the year-length convention (365.25-day "solar year" vs 360-day "savana year") — software differs; Jagannatha Hora/PyJHora expose both; pick 365.25 and document it.

### 4.2 Gochara (transits) and Sade Sati

- Transits are read **from the natal Moon sign** (janma rashi) in mainstream practice. **Sade Sati** = the ~7.5-year window when **Saturn transits the 12th, 1st, and 2nd signs from the natal Moon** (~2.5 years per sign); the tradition holds it to be a testing/restructuring period, most intense while Saturn is on the Moon sign itself. Ashtama Shani (Saturn in the 8th from Moon) and Kantaka Shani are related doctrines. Jupiter transits are read for favourable periods. [TRADITION; computation is just current-longitudes vs natal-Moon-sign — FACT.]
- **[ENG]** Daily transit longitudes come from the same ephemeris call with `JD = now`. Cache per-day.

### 4.3 Yogas, lordships, strength

- **House lordships:** each bhava's ruling planet (owner of the sign on that bhava) links life domains; benefic/malefic functional status depends on lagna. [TRADITION, BPHS.]
- **Yogas:** named combinations — e.g., Raja yogas (kendra-lord + trikona-lord association), Dhana yogas, Gaja-Kesari (Jupiter in kendra from Moon), Pancha-Mahapurusha yogas (Ruchaka/Bhadra/Hamsa/Malavya/Shasha), and afflictions like Kuja/Chovva dosham (Mars in 1/2/4/7/8/12 — **the 2nd house inclusion is a notably South Indian/Kerala rule**) and Kala Sarpa. Sources: BPHS, Brihat Jataka, [Phaladeepika](https://archive.org/details/in.ernet.dli.2015.406251) — see §5.1. [TRADITION]
- **Shadbala (basics only):** six-fold strength (positional, directional, temporal, motional, natural, aspectual) per BPHS; PyJHora and Maitreya implement it — useful as a numeric input to the AI's emphasis weighting, not something to expose raw to users. [TRADITION with a defined algorithm.]

### 4.4 Kerala prashna methodology [TRADITION]

Per Prashna Marga (see §2.2–2.3): judge the chart of the question moment via the lagna of the moment, the **arudha** (sign selected via the querent/cowries), the ashtamangala number, the strength and placement of the Moon and the karyesha (lord of the queried matter's house), plus omens (breathing side of the astrologer, first words heard, objects sighted). Specific classical topics: nashta prashna (lost objects), roga prashna (disease), deva prashna (temple matters), marriage/childbirth/travel queries.

### 4.5 Muhurta and porutham (marriage matching)

- **Muhurta** (electional astrology): choosing auspicious times by panchanga purity (tithi/vara/nakshatra/yoga/karana), lagna strength, and avoidance of rahukalam/gulikakalam etc. Kerala printed panchangams (Mathrubhumi/Manorama tradition) carry ready muhurta listings ([Mathrubhumi Panchangam](https://www.mbibooks.com/product/mathrubhumi-panchangam-2025-2026/)). [TRADITION]
- **Porutham — the South Indian 10-koota system** used in Kerala/Tamil Nadu, computed almost entirely from the couple's **janma nakshatras and Moon signs**: **dina, gana, mahendra, stree-deergha, yoni, rasi, rasyadhipati, vasya, rajju, vedha** ([Prokerala 10-porutham reference](https://www.prokerala.com/astrology/porutham/10-porutham-for-marriage.htm), [AstroVed overview](https://www.astroved.com/articles/10-marriage-matching)). Tradition ranks **rajju and dina** (with gana, rasi, yoni) as the weightiest, and treats **rajju dosha and vedha dosha as hard blockers** regardless of other scores. This contrasts with the **North Indian ashtakoota (36-guna)** aggregate-scoring system ([comparison](https://panchangbodh.com/kundli-matching)). Kerala matching also conventionally checks **chovva dosham (Mars dosha)** compatibility and dasha-sandhi. [TRADITION; the koota lookups are fixed tables — implementable deterministically.]
- **[ENG]** Porutham is a pure table-lookup feature over two nakshatra/rashi pairs — cheap to implement, extremely high demand in the Kerala market (matrimony use case).

---

## 5. Annotated resource list

### 5.1 Classical texts (English translations; primary doctrine sources)

| Text | Edition to use | Link | Notes |
|---|---|---|---|
| **Prashna Marga** (1649, Kerala) | B.V. Raman tr., 2 vols., Motilal Banarsidass (ISBN 9788120810341 / 812081035X for pt. 2) | [MLBD pt.1](https://www.motilalbanarsidass.com/en-us/products/prasna-marga-part-1-english-translation-with-original-text-in-devanagari-and-notes) · [MLBD pt.2](https://www.mlbd.in/products/prasna-marga-part-2-english-translation-with-original-text-in-devanagari-and-notes-b-v-raman-9788120810341-8120810341-9788120810358-812081035x) · [archive scan](https://archive.org/stream/PrasnaMargaBVR/Prasna%20Marga%202_djvu.txt) | The core Kerala text: prashna + ashtamangala + parihara. In-print; archive scans are of uncertain copyright status — license or buy for a commercial KB. |
| **Brihat Parashara Hora Shastra** | R. Santhanam tr., 2 vols. | [archive.org (Santhanam)](https://archive.org/details/brihatparasarahorashastrabyr.santhanam) · [alt scan](https://archive.org/details/BPHSEnglish) · [G.C. Sharma tr. vol.1](https://archive.org/details/brihatparasarahorasastrawithenglishtranslationgirishchandsharmavolume1_547_G) | Foundational natal doctrine: houses, yogas, vargas, Vimshottari, shadbala. Note: text's antiquity/authenticity is debated ([critical essay](https://shyamasundaradasa.com/jyotish/resources/articles/bphs.html)) — treat as the standard compendium, not scripture. |
| **Brihat Jataka** (Varahamihira, 6th c.) | V. Subrahmanya Sastri tr. (uses Bhattotpala); B. Suryanarain Rao tr. (1919, public domain) | [Sastri on archive.org](https://archive.org/details/BrihatJataka2ndEd.ByVSubrahmanyaSastri) · [Rao 1919](https://archive.org/details/in.ernet.dli.2015.406251) · [Wikipedia](https://en.wikipedia.org/wiki/Brihat_Jataka) | The most Kerala-revered classic; its Kerala commentary **Dashadhyayi** ([Wikipedia](https://en.wikipedia.org/wiki/Dasadhyayi)) exists mainly in Malayalam/Sanskrit editions — an English KB will lean on the base text + Bhattotpala. Rao 1919 is safely public domain. |
| **Phaladeepika** (Mantreswara — a South Indian classic) | V. Subrahmanya Sastri tr. | search archive.org / MLBD in-print editions | Compact predictive rules (yogas, dashas, bhava results); widely used in South India. Verify the specific scan's status before ingesting. |
| **Jataka Parijata** (Vaidyanatha Dikshita) | V. Subrahmanya Sastri tr., 3 vols. | archive.org scans exist; verify edition | South Indian compendium; secondary priority. |
| **Krishneeyam** (Krishna Acharya; pre-Prashna Marga Kerala horary text) | N.E. Muthuswami tr., Sagar Publications | [listing](https://jyotishbooks.wordpress.com/2021/12/14/krishneeyam-of-shree-krishna-acharya-by-n-e-muthuswami/) · [Sagar](https://sagarpublications.com/astrology/krishneeyam/) | Short; strong on nashta prashna. In-print, copyrighted — buy/license. |
| **Kerala-school history** | K.V. Sarma, *A History of the Kerala School of Hindu Astronomy*, 1972 | [Wikipedia](https://en.wikipedia.org/wiki/A_History_of_the_Kerala_School_of_Hindu_Astronomy) · [Stanford record](https://searchworks.stanford.edu/view/875819) | Historical grounding; also see David Pingree's *Census of the Exact Sciences in Sanskrit* (Series A, American Philosophical Society) for bibliographic control of Sanskrit jyotisha works (standard academic reference; consult a library copy). |

**Copyright caution [ENG]:** Raman (d. 1998), Santhanam, and Muthuswami translations are 20th-century copyrighted works. Archive.org scans ≠ permission. For a commercial knowledge base: (a) use genuinely public-domain translations (e.g., Suryanarain Rao 1919 Brihat Jataka), (b) buy print/ebook editions and have the AI paraphrase doctrine rather than reproduce text, or (c) license content. Doctrinal *rules* (e.g., dasha lengths, koota tables) are facts/ideas and not copyrightable; verbatim translation text is.

### 5.2 Computation libraries

| Library | Language | License | Link | Notes |
|---|---|---|---|---|
| **Swiss Ephemeris** (Astrodienst) | C (ports everywhere) | **Dual: AGPL-3.0 OR paid professional license** — first license CHF 750, additional CHF 400, unlimited CHF 1550, 99-year term | [official page](https://www.astro.com/swisseph/swephinfo_e.htm) · [LICENSE](https://github.com/aloistr/swisseph/blob/master/LICENSE) · [license contract PDF](http://www.astro.com/swisseph/secont_e.pdf) · [GitHub mirror](https://github.com/aloistr/swisseph) | De-facto standard, JPL-derived, arc-second accuracy, 40+ ayanamshas, houses, rise/set. **AGPL is viral over the network**: an API/web app using it must open-source its whole service, so a closed-source commercial app needs the CHF 750 professional license — cheap; budget for it. |
| **pyswisseph** | Python binding | AGPL-3.0 (binding itself) | [PyPI](https://pypi.org/project/pyswisseph/) · [GitHub](https://github.com/astrorigin/pyswisseph) | The standard Python route. Buying the SE professional license covers the underlying library; the binding's AGPL still applies to the binding code — verify with Astrodienst/author or isolate behind a service you're willing to open-source. |
| **sweph (Node.js)** | Node native binding | AGPL-3.0 | [GitHub timotejroiko/sweph](https://github.com/timotejroiko/sweph) | Best-maintained Node binding if the backend is JS/TS. Same licensing logic. |
| **PyJHora** | Python | Repo references AGPL (and MIT in places) — **treat as AGPL-effective** since it wraps pyswisseph | [GitHub](https://github.com/naturalstupid/PyJHora) · [PyPI](https://pypi.org/project/PyJHora/3.9.3/) | Implements a huge slice of Vedic astrology per PVR Narasimha Rao's book: vargas, shadbala, many dasha systems, yogas, porutham. Excellent as a **reference implementation / test oracle** even if you don't ship it. |
| **VedAstro** | C# (+ [Python wrapper](https://github.com/VedAstro/VedAstro.Python)) | Open source, non-profit; wrapper states MIT — **verify main repo license before shipping** | [site](https://vedastro.org/OpenSource.html) · [GitHub](https://github.com/VedAstro/VedAstro) | Broad Vedic calc + open API; useful for cross-checking outputs. |
| **Maitreya** | C++ desktop | GPL-2.0, free for private & commercial use | [saravali.github.io](https://saravali.github.io/) · [maintained fork](https://github.com/robinrodricks/Maitreya9) | Desktop reference app (South Indian chart rendering, vargas, dashas) — good for manual verification, not embedding (GPL). |
| **Jagannatha Hora (JHora)** | Windows freeware (closed source) | Free, not open source | [vedicastrologer.org/jh](https://www.vedicastrologer.org/jh/) | The practitioner-standard free tool (by P.V.R. Narasimha Rao, Swiss Ephemeris inside). Use as the **ground-truth oracle** for test fixtures: generate charts in JHora, assert your pipeline matches to the arc-minute. |
| **Skyfield + manual ayanamsha** | Python | MIT | [libephemeris (Skyfield-based, SE-compatible API)](https://github.com/g-battaglia/libephemeris) · [PyPI](https://pypi.org/project/libephemeris/) | The **AGPL-free escape hatch**: NASA/JPL kernels via Skyfield (MIT) + your own Lahiri ayanamsha & house math, or the libephemeris drop-in which claims SE-compatible results with 43 ayanamshas, MIT-licensed. Verify accuracy against JHora before trusting. |

### 5.3 APIs (build-vs-buy)

| API | Link | Notes |
|---|---|---|
| **Prokerala Astrology API** | [api.prokerala.com](https://api.prokerala.com/) · [docs](https://api.prokerala.com/docs) · [pricing](https://api.prokerala.com/pricing) | Free tier + credit plans; Vedic endpoints: panchang, birth details, 20+ chart types (rasi/navamsa), dasha, kundli, porutham, mangal dosha — **output available in Malayalam**, and it has an explicit [10-porutham product](https://www.prokerala.com/astrology/porutham/). Prokerala is itself a Kerala-rooted brand; closest fit to this app's domain. Credit costs: panchang 10, birth chart 50, kundli 50–300 credits, etc. |
| **AstrologyAPI (VedicRishi)** | [astrologyapi.com](https://astrologyapi.com/) · [vedicrishi.in](https://vedicrishi.in/web-astro-api) · [RapidAPI listing](https://rapidapi.com/vedicrishi/api/advanced-astrology-and-horoscope/pricing) | REST, free trial; kundli, matching, dasha, PDF reports. North-India-oriented defaults (ashtakoota matching). |
| **VedicAstroAPI** | [vedicastroapi.com](https://vedicastroapi.com/) | Vedic + Western + "AI chat" endpoints, 21 languages; evaluate quality before depending on it. |

**[ENG] Recommendation:** own the computation layer (Swiss Ephemeris professional license + your code, or the Skyfield/MIT route). Astrology APIs are fine for prototyping, but per-call credits at consultation-app volume get expensive, and an AI astrologer needs raw structured chart data (longitudes, dasha trees) more than pre-baked report text. Prokerala is the best prototype API for Kerala specifics (Malayalam output, porutham).

### 5.4 Kerala-specific data & institutions

- **Printed panchangam standard:** [Mathrubhumi Panchangam](https://www.mbibooks.com/product/mathrubhumi-panchangam-2025-2026/) (annual, by Sadanam Narayanan Pothuval); Malayala Manorama and Mathrubhumi calendars are the most-circulated Kerala calendars ([Mathrubhumi calendar app](https://play.google.com/store/apps/details?id=com.mathrubhumi.calendar2019&hl=en)). Use these to **validate** your panchanga output against what Kerala users see at home.
- **Kollavarsham conversion data:** [Malayalam calendars 1900–2049](https://malayalam.usvishakh.net/calendars/150calendars.html); [Prokerala Malayalam calendar](https://www.prokerala.com/general/calendar/); [Nalla Naal pirannal/naal tools](https://nallanaal.in/) as behavioural references. Kollavarsham month boundaries = solar sign transits (sankranti) with Kerala-specific rules — verify against printed panchangam for edge days.
- **Institutions (verified to exist):** the **Department of Jyothisham, Government Sanskrit College, Thiruvananthapuram** — BA in Jyothisha since 1980, MA-level since 2005 ([department page](http://gsctvpm.ac.in/?page_id=1485)); **Kerala Jyothisha Parishath**, a practitioner body ([site](https://www.keralajyothishaparishath.com/)); [Sree Sankaracharya University of Sanskrit, Kalady](https://www.careers360.com/university/sree-sankaracharya-university-of-sanskrit-kalady) for Sanskrit/Indology generally (a dedicated jyotisha degree there was **not** confirmed — do not cite one). These matter for credibility copy and potential advisory partnerships.
- **Academic:** K.V. Sarma (op. cit.); the Indian Journal of History of Science (INSA) regularly publishes Kerala-astronomy papers (e.g., Sarma's editions of *Tantrasangraha*, *Drgganita*); [example modern paper on Kerala-school computation](https://arxiv.org/pdf/2411.08296).

---

## 6. Open questions & risks

1. **Swiss Ephemeris licensing (decide early).** AGPL propagates across the network boundary — any closed-source backend calling it must either open-source or buy the professional license (CHF 750 first / CHF 1550 unlimited, 99 years) ([license terms](https://github.com/aloistr/swisseph/blob/master/LICENSE), [contract](http://www.astro.com/swisseph/secont_e.pdf)). Also confirm whether the *binding* you use (pyswisseph/sweph, both AGPL) is covered by the professional license or needs isolation. Alternative: Skyfield/[libephemeris](https://github.com/g-battaglia/libephemeris) (MIT) — but validate its output against Jagannatha Hora first.
2. **Ayanamsha choice.** Default **Lahiri/Chitrapaksha** (Indian government standard via the Positional Astronomy Centre's Indian Astronomical Ephemeris); expose Raman/KP as settings. Charts differ by ~1.4° between Lahiri and Raman — enough to flip a lagna or nakshatra near boundaries, which users *will* notice against other apps. Document the choice in-app.
3. **Node convention & dasha year-length.** Mean vs true Rahu, and 365.25 vs 360-day dasha years, cause visible discrepancies vs other apps. Pick JHora's defaults (the practitioner standard) and match it in tests.
4. **Kollavarsham/pirannal edge cases.** Sankranti-day month attribution and nakshatra-day boundaries (nakshatra at sunrise vs at the moment) vary between panchangams; validate against Mathrubhumi/Manorama print for a sample year.
5. **Copyright of translations.** Doctrinal rules are free; translation text is not. Prefer public-domain translations (Suryanarain Rao 1919) + purchased editions with paraphrase-only ingestion (§5.1).
6. **Regulatory/ethical exposure in India (concrete):**
   - **No dedicated statute** governs digital astrology; the space is covered indirectly by the IT Act 2000, **Consumer Protection Act 2019** (misleading-advertisement liability, CCPA penalties up to ₹10 lakh first offence / ₹50 lakh repeat), and the DPDP Act for personal data ([legal analysis](https://sudhirrao.com/legal-recourse-against-misleading-astrology-apps-in-india/), [industry overview](https://www.storyboard18.com/how-it-works/biz-of-belief-how-indias-astrology-apps-are-turning-faith-into-fortune-amid-rising-regulatory-concerns-83027.htm)).
   - **ASCI Code** applies to astrology-app advertising: no absolute claims ("100% guarantee"), substantiate any performance claims, visible disclaimers ([coverage](https://bestmediainfo.com/mediainfo/mediainfo-marketing/astrology-apps-on-the-rise-in-india-but-who-guarantees-their-credibility-10511514)).
   - The **Drugs and Magic Remedies Act 1954** has been read as *not* covering astrology per se ([Bombay HC ruling coverage](https://www.livescience.com/12856-astrology-science-indian-court-ruling.html)) — but never let the AI promise cures/remedies for medical conditions; route health questions to disclaimers.
   - **Product implications [ENG]:** persistent "for guidance/entertainment; not a substitute for medical/financial/legal advice" framing; hard guardrails against death predictions, medical diagnosis, and guaranteed outcomes (also note Prashna Marga itself contains longevity/death chapters — exclude from the AI's permissible outputs); DPDP-compliant handling of birth data (it's sensitive personal information); clear AI disclosure (the astrologer is an AI, not a human).
7. **Unverified items deliberately left out:** a jyotisha degree at SSUS Kalady (unconfirmed); specific editions of *Prashnanushtana Paddhati*/*Prashnayanam*; Dashadhyayi English translation (none found). Do not cite these in-app until confirmed.
8. **Cultural authenticity review.** The interpretive KB (especially ashtamangala digitization and deva-prashna adjacency) should be reviewed by a practising Kerala astrologer before launch; temple-ritual territory is culturally sensitive.

---

## 7. Suggested next steps [ENG]

1. Spike the pipeline: pyswisseph + Lahiri → reproduce a JHora chart (lagna, 9 grahas, nakshatra/pada, D9, Vimshottari tree) for 3 test births; assert arc-minute agreement.
2. Decide SE professional license vs Skyfield route; if commercial+closed-source, start the Astrodienst paperwork (it's mail-based and slow).
3. Build the porutham (10-koota) tables and panchanga formulas — pure lookups, no ephemeris licensing issues, immediately demo-able.
4. Acquire: Prashna Marga (Raman, 2 vols), BPHS (Santhanam), Brihat Jataka (Sastri + Rao PD scan), Krishneeyam (Muthuswami) — and structure doctrine extraction as rules (JSON), not prose, to keep copyright clean.
5. Draft the AI-astrologer guardrail spec (no death/medical/guaranteed-outcome outputs; AI disclosure; DPDP data handling) from §6.6.
