---
api_count: 2
artifact_total: 0
created: '2026-07-27'
description: 'char.gy is a British public electric-vehicle charge point operator that specialises in on-street charging for the roughly forty percent of UK households with no off-street parking, and it is best known for putting the charger inside the lamp post. Founded by Richard Stobart out of the digital agency Unboxed, it installed its first public charger in Marlow, Buckinghamshire in 2018, is now led by CEO John Lewis from Floor 5, 55 King William St, London EC4R 9AD, and is backed with £100m by Zouk Capital through the UK Government-backed Charging Infrastructure Investment Fund. Its own about page claims over 5,000 charge points and 28.3 million kg of CO2 saved, and its live open data feed returned an x-total-count of 5,409 locations on 2026-07-27. In the UK energy value chain it sits at the very end of the wire: it is not a licensed supplier, not a network operator and not a metering agent, it operates charge points on street furniture owned by local authorities — Haringey, Southwark,
  Brent, Barnet, Harrow, Coventry, Brighton and Hove, Richmond and Wandsworth, Enfield and others — authorising drivers, metering the session and pricing it. Britain has no consumer data-portability mandate for energy equivalent to Australia''s Consumer Data Right, so nothing compels char.gy to expose an individual driver''s usage or billing data through an API, and it does not: there is no consumer API, no OAuth server, no OpenID Connect discovery document and no accredited-recipient scheme anywhere on the domain. What Britain DID mandate here is open infrastructure data. The Public Charge Point Regulations 2023 (SI 2023/1168), Part 4 regulation 10(5), require every charge point operator to make reference data and availability data available to the public free of charge, in a machine readable format, and — the crucial clause — "without any requirement to agree to terms and conditions regarding the use of that data". char.gy complies, and the compliance is real rather than claimed: it publishes
  an OCPI-shaped Locations feed and an OCPI-shaped Tariffs feed at https://char.gy/open-ocpi/locations and https://char.gy/open-ocpi/tariffs, both of which returned HTTP 200 with application/json to a completely anonymous GET on 2026-07-27, paginated with x-total-count, x-limit and RFC 5988 Link rel="next" headers, carrying real GB*CGY*E*NNNNN EVSE identifiers, IEC 62196 Type 2 connectors, per-connector tariff_ids and time-of-day restricted pence-per-kWh price components. The posture is therefore the clean split this sector keeps producing, but rotated: market and infrastructure data wide open and genuinely ungated because a regulation forbids gating it, consumer data entirely absent because no regulation asks for it, and the commercial OCPI CPO roaming interface at /ocpi/cpo/ closed behind OCPI Token authorization for partner e-mobility service providers. There is no developer portal — the entire public documentation for the open API is a single Freshdesk help-centre article.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargy.png
layout: provider
modified: '2026-07-27'
name: char.gy
nav: Providers
network: true
random_paper: 26
slug: chargy
tags:
- Energy
- United Kingdom
- EV Charging
- Electricity
- Utilities
- OCPI
- Charge Point Operator
- Open Data
- Roaming
- Tariffs
- Mobility
- Electrification
---
