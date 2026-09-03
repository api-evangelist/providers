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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sage-geosystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sagegeosystems.com/
- group: company
  title: ''
  type: About
  url: https://www.sagegeosystems.com/company
- group: company
  title: ''
  type: Blog
  url: https://www.sagegeosystems.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.sagegeosystems.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sagegeosystems.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sagegeosystems.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sage-geosystems
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@sagegeosystems
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sage-geosystems-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Sage Geosystems builds geothermal power generation and energy storage plants; its entire web presence is a seven-page Webflow marketing site (home, technology, projects, company, newsroom, contact, careers) with no developer, docs, or API path — /developers, /api, /docs, /openapi.json and every /.well-known/* probe returned 404, and no GitHub organization exists under the name.
  evidence:
  - status: 200
    url: https://www.sagegeosystems.com/
  - status: 404
    url: https://www.sagegeosystems.com/developers
  - status: 404
    url: https://www.sagegeosystems.com/api
  - status: 404
    url: https://www.sagegeosystems.com/openapi.json
  - status: 404
    url: https://www.sagegeosystems.com/.well-known/agent-card.json
  - status: 404
    url: https://www.sagegeosystems.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Sage Geosystems is a Houston, Texas energy company developing "Pressure Geothermal" — an evolution of traditional geothermal that applies subsurface breakthroughs from the oil and gas industry to hot dry rock. Its two-well Power Generation system circulates water through engineered "lung" fractures and extracts heat at surface through a heat exchanger driving an sCO2 turbine, while its single-well EarthStore energy storage system charges and discharges over 8-hour to multi-day timescales for long-duration storage. The company markets to utilities, data centers and government partners rather than to developers: as of this profile it operates a seven-page marketing site with no developer portal, public API, SDK, or machine-readable specification of any kind.'
image: https://cdn.prod.website-files.com/67c84ff5859691041733b20c/67e6ff023d9f135d5a3f4b12_Sage-OG.png
layout: provider
modified: '2026-08-26'
name: Sage Geosystems
nav: Providers
network: true
overview: 'Sage Geosystems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Geothermal, Energy Storage, and Power Generation.


  Sage Geosystems'' developer surface includes engineering blog, support, YouTube channel, and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sage-geosystems/refs/heads/main/screenshots/sage-geosystems-2026-09-02T154256.png
security:
- kind: domain-security
  name: Sage Geosystems Domain Security
  slug: sage-geosystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sage-geosystems
tags:
- Company
- Energy
- Geothermal
- Energy Storage
- Power Generation
- Renewable Energy
- Cleantech
website: https://www.sagegeosystems.com/
---
