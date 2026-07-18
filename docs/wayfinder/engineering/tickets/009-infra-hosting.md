---
id: 009
title: Infrastructure & hosting
label: wayfinder:grilling
status: open
assignee:
blocked-by: [004, 008]
---

## Question

Where does the concierge MVP run? To decide: hosting for the Python engine service, the TS frontend, and Postgres; whether India-region hosting matters at concierge scale (DPDP posture from ticket 008; latency to Kerala vs Gulf/US/UK diaspora users); managed platform (Supabase/Vercel/Fly-class) vs single VPS vs Indian cloud region; background-job story (daily panchanga/transit precompute); cost envelope at 20–50 users; secrets & environment management for a solo founder + agents workflow (agents need deploy access without owning production secrets). Blocked by engine architecture (what's being deployed) and the data model (residency/encryption needs).
