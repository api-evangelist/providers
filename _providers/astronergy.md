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
  url: security/astronergy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astronergy.com/
- group: company
  title: ''
  type: About
  url: https://www.astronergy.com/about-astronergy/
- group: company
  title: ''
  type: Blog
  url: https://www.astronergy.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.astronergy.com/news/
- group: other
  title: ''
  type: Products
  url: https://www.astronergy.com/product-series/
- group: other
  title: ''
  type: Downloads
  url: https://www.astronergy.com/download-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.astronergy.com/compliance/
- group: other
  title: ''
  type: Sustainability
  url: https://www.astronergy.com/sustainability/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astronergy.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astronergy.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.astronergy.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/astronergy-solar/
- group: other
  title: ''
  type: Parent
  url: https://www.chint.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astronergy-llms.txt
- group: other
  title: ''
  type: Profile
  url: https://www.hiive.com/securities/astronergy-stock
coverage:
  checked: '2026-08-06'
  detail: Astronergy manufactures PV cells and modules, and its whole 37-page astronergy.com sitemap is marketing, PDF datasheets and two web-form tools (module-authenticity, PV Planner) with no developer section — the WordPress REST API answers 401 rest_forbidden and the live api.astronergy.com backend returns a Spring Boot JSON 404 at every spec, well-known and MCP path probed.
  evidence:
  - status: 200
    url: https://www.astronergy.com/sitemap.xml
  - status: 401
    url: https://www.astronergy.com/wp-json/
  - status: 404
    url: https://api.astronergy.com/openapi.json
  - status: 404
    url: https://api.astronergy.com/.well-known/agent-card.json
  - status: 404
    url: https://www.astronergy.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Astronergy (Chint New Energy Technology Co., Ltd.) is the photovoltaic cell and module manufacturing arm of China''s CHINT Group. Founded in 2006, it is one of the earliest private Chinese enterprises in the PV sector and is ranked among the world''s largest module suppliers. It designs, manufactures and sells high-efficiency crystalline-silicon PV cells and modules — notably the n-type TOPCon ASTRO N series in bifacial and monofacial form — for utility-scale power stations, commercial and industrial rooftops, and residential systems. Astronergy sells into more than 140 countries and regions and operates manufacturing bases and sales centers in markets including Germany, Spain, the USA, Brazil and Turkey. Its public web surface is a marketing and product-download site: datasheets, installation manuals, warranty and certification PDFs, a module-authenticity checker and a PV Planner yield calculator. It publishes no developer program, API documentation or machine-readable API
  contract.'
image: https://www.astronergy.com/wp-content/uploads/2023/05/logo_w.png
layout: provider
modified: '2026-08-06'
name: Astronergy
nav: Providers
network: true
overview: 'Astronergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar, Photovoltaic, Renewable Energy, and Energy.


  Astronergy''s developer surface includes engineering blog, product news, and 14 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astronergy/refs/heads/main/screenshots/astronergy-2026-08-07T161819.png
security:
- kind: domain-security
  name: Astronergy Domain Security
  slug: astronergy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: astronergy
tags:
- Company
- Solar
- Photovoltaic
- Renewable Energy
- Energy
- Manufacturing
- Hardware
- Sustainability
- Climate
website: https://www.astronergy.com/
---
