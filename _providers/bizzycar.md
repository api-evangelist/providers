---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: api.bizzycar.com is live but is BizzyCar's own application backend, not a product — every contract path (/openapi.json, /swagger.json, /api-docs, /graphql) returns the app's Rails JSON 404 envelope, none of the 238 URLs in the sitemap is a developer, docs or API page, and there is no bizzycar GitHub org or package on any registry; BizzyCar sells the DMS connectors it consumes, not an API it exposes.
  evidence:
  - status: 404
    url: https://api.bizzycar.com/openapi.json
  - status: 404
    url: https://api.bizzycar.com/graphql
  - status: 200
    url: https://www.bizzycar.com/sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/bizzycar
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'BizzyCar is a B2B SaaS platform for automotive dealerships that automates service recall management, customer outreach and mobile service. Founded in 2018 and headquartered in Saint Peters, Missouri, the company ingests VIN-level open-recall data from OEM partners, matches it against a dealer''s market area and DMS records, then uses AI-driven outreach (SMS, email, voice) to book service appointments and dispatch mobile service vans. Products include Recall Outreach, Recall Scout, Recall Radar, Service Engine, Mobile Service and Fleet IQ. BizzyCar is primarily an API *consumer* rather than an API producer: it ships pre-built connectors into dealer management systems (Dealertrack, DMS Plus, Open/Mate, Asbury, PBS, Tekion, Fortellis, Reynolds & Reynolds) and service schedulers (Xtime, TCC, DealerFX, Affinitiv, Update Promise), but publishes no public developer program, API reference or machine-readable contract of its own.'
image: https://www.bizzycar.com/hubfs/1.%201200x630.png
layout: provider
modified: '2026-08-07'
name: BizzyCar
nav: Providers
network: true
random_paper: 87
slug: bizzycar
tags:
- Company
- Automotive
- Recall Management
- Dealerships
- Mobile Service
- Vehicle Service
- Fleet Management
- Scheduling
- SaaS
---
