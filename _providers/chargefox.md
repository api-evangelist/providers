---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'Chargefox is Australia''s largest public electric-vehicle charging network and, since 2023, a charging software platform rather than a hardware owner. Founded in 2017 and headquartered in Melbourne, it was acquired outright in 2022 by Australian Motoring Services, the joint vehicle of six state motoring clubs — NRMA, RACV, RACQ, RAA, RAC and RACT — which makes it one of the very few member-owned pieces of national energy infrastructure in the country. Its own company page claims 2,200+ public charging plugs, 5,000+ charging sessions a day and 170,000+ app downloads. In the Australian energy value chain it sits downstream of the retailer and the meter: it does not generate, transmit or sell electricity as a licensed retailer, it operates the charge points other businesses, councils and governments own, authorises drivers, meters the session, prices it and settles it. That position is exactly why the Consumer Data Right does not touch it. Chargefox does NOT appear among the 84
  energy data-holder brands on the ACCC CDR Register checked on 2026-07-27 — even though Arcline by RACV, an energy retailer owned by one of Chargefox''s own shareholder clubs, does — so the statutory mandate that produced Australia''s identical fifty-bank banking contract stops at the retail electricity licence and never reaches the charge point. What Chargefox has instead is an entirely voluntary, entirely commercial API posture built on a genuine industry standard. It publishes a real, anonymously readable developer documentation site at https://app.chargefox.com/developers/docs carrying a Redoc-rendered OpenAPI 3.0.1 contract for a four-endpoint Fleets API, and its own rate-limit documentation enumerates a full Open Charge Point Interface CPO implementation across OCPI 2.1.1, 2.2 and 2.2.1 covering locations, sessions, CDRs, tariffs, tokens and commands. Every one of those endpoints is closed. Anonymous probes returned 401 with `WWW-Authenticate: Token realm="Application"` on the OCPI
  paths and 401 on the Fleets paths, and no anonymous locations, tariff or network-status feed of any kind could be found, so Chargefox publishes zero open market data and zero consumer data — a documented standard, fully implemented, entirely behind a commercial gate.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargefox.png
layout: provider
modified: '2026-07-27'
name: Chargefox
nav: Providers
network: true
random_paper: 67
slug: chargefox
tags:
- Energy
- Australia
- EV Charging
- Electricity
- Utilities
- OCPI
- Charge Point Operator
- Roaming
- Fleets
- Mobility
- Charging Sessions
- Electrification
---
