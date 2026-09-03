---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.terawatt-technology.com/
- group: operate
  title: ''
  type: Support
  url: https://www.terawatt-technology.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/terawatt-technology-inc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terawatt-technology-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terawatt-technology-llms.txt
coverage:
  checked: '2026-08-30'
  detail: TeraWatt Technology manufactures lithium-ion battery cells for EV, eVTOL and grid-storage OEMs; its entire public surface is a four-anchor Webflow marketing site (Vision, News, Careers, Contact) with no developer section, and api./developer./docs.terawatt-technology.com do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://www.terawatt-technology.com/
  - status: 404
    url: https://www.terawatt-technology.com/openapi.json
  - status: 404
    url: https://www.terawatt-technology.com/.well-known/api-catalog
  - status: 404
    url: https://www.terawatt-technology.com/.well-known/agent-card.json
  - status: 404
    url: https://www.terawatt-technology.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: 'TeraWatt Technology Inc. is a next-generation lithium-ion battery company founded in 2020 by Ken Ogata (CEO) and Yifan Tang, headquartered in California with an R&D center in Santa Clara and operations in Japan, including its first mass-production facility in Shizuoka. The company develops, manufactures and commercializes lithium-ion cells engineered for ultra-high energy density, high power output, improved safety and competitive cost, aimed at electric vehicles, drones, eVTOL aircraft and grid-scale energy-storage systems. It closed a Series C round with investors including Khosla Ventures, Temasek, JIC Venture Growth Investments, JBIC, JERA and ITOCHU Technology Ventures. TeraWatt Technology is a hardware manufacturer: it publishes no public API, developer portal, machine-readable contract or SDK, which was verified by probing its only public host rather than assumed.'
image: https://cdn.prod.website-files.com/62c28e77ff36a9cee41c7444/62c928f69749a0f46b7f2eb7_web-tab-thumbnail.png
layout: provider
modified: '2026-08-30'
name: TeraWatt Technology
nav: Providers
network: true
overview: 'TeraWatt Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Batteries, Energy Storage, Lithium-Ion, and Electric Vehicles.


  TeraWatt Technology''s developer surface includes support and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/terawatt-technology/refs/heads/main/screenshots/terawatt-technology-2026-09-02T163128.png
security:
- kind: domain-security
  name: Terawatt Technology Domain Security
  slug: terawatt-technology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: terawatt-technology
tags:
- Company
- Batteries
- Energy Storage
- Lithium-Ion
- Electric Vehicles
- Manufacturing
- Clean Energy
- Hardware
website: https://www.terawatt-technology.com/
---
