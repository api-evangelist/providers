---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-29'
  detail: Stay Alfred Inc. permanently closed on 20 May 2020 and the stayalfred.com host is no longer controlled by the company — every path, including /openapi.json and every /.well-known/ path, returns a Cloudflare 301 into a rotating set of unrelated third-party domains, while api./developer./docs./app.stayalfred.com are all NXDOMAIN and no GitHub organization or package-registry namespace ever existed.
  evidence:
  - status: 301
    url: https://www.stayalfred.com/
  - status: 301
    url: https://www.stayalfred.com/openapi.json
  - status: 301
    url: https://www.stayalfred.com/.well-known/agent-card.json
  - status: 301
    url: https://www.stayalfred.com/.well-known/security.txt
  - status: 200
    url: https://www.stayalfred.com/robots.txt
  - status: 404
    url: https://api.github.com/orgs/stayalfred
  - status: 404
    url: https://registry.npmjs.org/stayalfred
  - status: 403
    url: https://forgeglobal.com/stay-alfred_stock/
  reason: defunct
  state: none
created: '2026-08-29'
description: 'Stay Alfred Inc. was a Spokane, Washington short-term-rental and hospitality operator that pioneered the "travel apartment" — full apartments in walkable downtown cores, leased in bulk from multifamily building owners and operated with hotel-style consistency, cleaning and guest support. Founded in 2011 by Jordan Allen, who was named EY Entrepreneur Of The Year for the Pacific Northwest in 2019, the company grew to roughly 2,000-2,500 units across 28 to 33 U.S. markets including Denver, San Diego, Miami, New Orleans and Nashville, hosted around half a million guests, and employed more than 230 people. It raised approximately $62M in total venture funding, headlined by a $47M Series B in October 2018 led by Chicago real-estate technology fund Nine Four Ventures. Distribution ran through its own consumer booking site and the major online travel agencies, so Stay Alfred was an API CONSUMER rather than an API publisher; it never operated a developer program, public API, SDK, webhook
  catalog or machine-readable specification. COVID-19 ended it: the company closed every property nationwide from 1 April 2020, a rescue funding round was withdrawn at the last minute, and on 20 May 2020 Stay Alfred announced it would close permanently, winding down through mid-2020 while it had been on track for roughly $100M in revenue that year. The stayalfred.com domain is still on its original 2013 registration but is no longer controlled by the company: it is privacy-shielded, Cloudflare-hosted, and every path now 301-redirects into a rotating chain of unrelated third-party sites. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-29'
name: Stay Alfred
nav: Providers
network: true
overview: Stay Alfred is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Travel, Hospitality, and Lodging.
random_paper: 3
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: stay-alfred
tags:
- Company
- Defunct
- Travel
- Hospitality
- Lodging
- Short-Term Rental
- Vacation Rental
- Corporate Housing
- Accommodations
- Real-Estate
- Consumer
---
