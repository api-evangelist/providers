---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/domio_stock/
coverage:
  checked: '2026-08-12'
  detail: Domio Inc. shut down in November 2020 and its former host staydomio.com was re-registered in September 2021 by an unrelated party, so every path now returns the same 114-byte GoDaddy parking-lander stub with HTTP 200 — including /openapi.json and every /.well-known/ path — and none of them is a document.
  evidence:
  - status: 200
    url: https://www.staydomio.com/
  - status: 200
    url: https://www.staydomio.com/openapi.json
  - status: 200
    url: https://www.staydomio.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/domio
  - status: 403
    url: https://forgeglobal.com/domio_stock/
  reason: defunct
  state: none
created: '2026-08-12'
description: Domio was a New York City hospitality and real-estate technology company that designed, leased, and operated branded "apart-hotels" — spacious, design-forward apartment-style accommodations aimed at group and extended-stay travelers. Founded in June 2016 by former Bank of America Merrill Lynch real-estate bankers Jay Roberts and Adrian Lam, the company used data analysis and machine learning to select buildings for its portfolio and distributed inventory through its own site and app alongside third-party channels such as Airbnb. It raised roughly $117M across five rounds, including a $12M Series A in 2018 from Tribeca Venture Partners and SoftBank Capital, a $50M joint-venture facility from Upper90, and a $100M Series B in December 2019 (half equity, half debt) led by GGV Capital with Eldridge Industries, 3L Capital, Cain International and Tenaya Capital. Airbnb suspended all of Domio's host accounts in August 2020, the co-founders resigned that September, and the company ceased
  operations in November 2020, selling its assets through an assignment for the benefit of creditors overseen by Sherwood Partners. Domio never published a developer program, public API, SDK, or machine-readable specification. Its former host staydomio.com was re-registered on 2021-09-19 by an unrelated party and now serves a GoDaddy parking lander, so it is deliberately not wired as a Website pointer. This profile is retained as a historical record; there is no API surface to enrich.
layout: provider
modified: '2026-08-12'
name: Domio
nav: Providers
network: true
overview: Domio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Travel, Hospitality, and Lodging.
random_paper: 89
score:
  band: minimal
  composite: 4.6
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  previous_composite: 4.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
slug: domio
tags:
- Company
- Defunct
- Travel
- Hospitality
- Lodging
- Short-Term Rental
- Accommodations
- Real Estate
- Consumer
website: https://forgeglobal.com/domio_stock/
---
