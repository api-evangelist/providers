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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/source-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/source-llms.txt
- group: company
  title: ''
  type: Website
  url: https://source.co/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sourceglobal
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/source-3902
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/source_stock/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/source-stock
coverage:
  checked: '2026-08-05'
  detail: SOURCE Global appears to have wound down — every path on source.co, including the homepage and all /.well-known/* probes, returns HTTP 402 with Shopify's "Store unavailable" page, source.co/llms.txt answers 200 with only "This store is currently unavailable. Agent interaction is not possible at this time.", and the legacy zeromasswater.com domain is now a parked GoDaddy builder page.
  evidence:
  - status: 402
    url: https://source.co/
  - status: 200
    url: https://source.co/llms.txt
  - status: 402
    url: https://source.co/.well-known/agent-card.json
  - status: 402
    url: https://source.co/openapi.json
  - status: 200
    url: https://source.co/robots.txt
  - status: 200
    url: https://zeromasswater.com/
  - status: 404
    url: https://api.github.com/orgs/sourceglobal
  reason: defunct
  state: none
created: '2026-08-05'
description: 'SOURCE Global, PBC (founded as Zero Mass Water) is a Scottsdale, Arizona public benefit corporation started in 2014 by Arizona State University materials scientist Cody Friesen to make drinking water out of sunlight and air. Its SOURCE Hydropanel is an off-grid solar-thermal device that pulls water vapor from the atmosphere, condenses and mineralizes it, and delivers roughly five liters of drinking water a day; the panels were deployed in residential, commercial, community and humanitarian projects across more than 50 countries, and the company later moved into bottled water, acquiring Proud Source Water in 2023. It raised approximately USD 270 million in total, including a USD 50 million Series C led by BlackRock in 2020 and a USD 130 million Series D in 2022 co-led by Breakthrough Energy Ventures and the Drawdown Fund with Microsoft Climate Innovation Fund and Fifth Wall participating. SOURCE was a hardware and consumer-products business rather than a software vendor: it
  never published a developer portal, API reference, SDK or any machine-readable API contract, and the only machine-readable surface its site ever exposed was the Shopify platform behind its direct-to-consumer storefront. The company went quiet during 2025 — an April 2025 SEC filing showed a USD 75 million raise that closed at USD 19.3 million, and founder Cody Friesen announced his departure in June 2025 — and as of August 2026 source.co answers HTTP 402 "Store unavailable" on every path while the legacy zeromasswater.com domain resolves to a parked GoDaddy builder page.'
layout: provider
modified: '2026-08-05'
name: SOURCE Global
nav: Providers
network: true
overview: SOURCE Global is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Water, Drinking Water, Cleantech, and Climate Tech.
random_paper: 6
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 2
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
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Source Domain Security
  slug: source-domain-security
  summary_line: TLSv1.3 · DMARC
slug: source
tags:
- Company
- Water
- Drinking Water
- Cleantech
- Climate Tech
- Atmospheric Water Generation
- Hardware
- Consumer Products
- Renewable Energy
- Public Benefit Corporation
website: https://source.co/
---
