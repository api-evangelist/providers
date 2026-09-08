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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.act-ion.com/
- group: company
  title: ''
  type: About
  url: https://www.act-ion.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.act-ion.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.act-ion.com/news?format=rss
- group: company
  title: ''
  type: Careers
  url: https://www.act-ion.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.act-ion.com/#contact
- group: auth
  title: ''
  type: DomainSecurity
  url: security/act-ion-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/act-ion-llms.txt
coverage:
  checked: '2026-09-06'
  detail: ACT-ion Battery Technologies manufactures single-crystal cathode active material powder for lithium-ion cells at a pilot plant in Carrollton, Texas — the product is a physical material, not software — and act-ion.com is a six-page Squarespace marketing site (Home, About, Technology, News, Careers, plus a mailto contact anchor) with no /developers, no /api, no machine-readable contract, and no api., docs., developer., app. or portal. subdomain in DNS.
  evidence:
  - status: 200
    url: https://www.act-ion.com/
  - status: 200
    url: https://www.act-ion.com/sitemap.xml
  - status: 404
    url: https://www.act-ion.com/openapi.json
  - status: 404
    url: https://www.act-ion.com/llms.txt
  - status: 404
    url: https://www.act-ion.com/apis.json
  - status: 404
    url: https://www.act-ion.com/.well-known/agent-card.json
  - status: 404
    url: https://www.act-ion.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'ACT-ion Battery Technologies, Inc. is an advanced battery materials company founded in Dallas, Texas and spun out of Hunt Energy Enterprises, now running an advanced cathode pilot plant in Carrollton, Texas. It manufactures surface-engineered single-crystal cathode active materials (CAM) for lithium-ion batteries across LFP, LMFP, NMC and lithium-manganese-rich chemistries, marketed as ACT-ion LXP+, using a chemistry-agnostic high-throughput continuous synthesis process that deposits a protective, conductive shell during particle growth to cut CAM cost and plant footprint. It raised a $7.5M pre-Series A led by BASF Venture Capital, extended to $11.5M, won a 2024 R&D 100 Award, and named Mark McGough CEO in August 2026. ACT-ion is a materials manufacturer, not a software vendor: it publishes no API, developer portal, SDK or machine-readable contract.'
image: https://static1.squarespace.com/static/671165060b55f84558c51ab9/t/6791005a8039e671e2bda9ad/1737556058427/action+logo+-+color+-+cut+1.png?format=1500w
layout: provider
modified: '2026-09-06'
name: ACT-ion
nav: Providers
network: true
overview: 'ACT-ion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Battery Materials, Cathode Active Materials, and Lithium-Ion Batteries.


  ACT-ion''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Act Ion Domain Security
  slug: act-ion-domain-security
  summary_line: TLSv1.3 · HSTS
slug: act-ion
tags:
- Company
- Energy
- Battery Materials
- Cathode Active Materials
- Lithium-Ion Batteries
- Energy Storage
- Advanced Manufacturing
- Clean Energy
- Electric Vehicles
- Materials Science
- Deep Tech
- Texas
website: https://www.act-ion.com/
---
