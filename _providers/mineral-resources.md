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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/mineral-resources/llms/mineral-resources-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mineral-resources-llms.txt
- group: other
  href: https://artifacts.apis.io/mineral-resources/hosts/mineral-resources-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mineral-resources-hosts.yml
- group: other
  href: https://artifacts.apis.io/mineral-resources/vendors/mineral-resources-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mineral-resources-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mineral-resources/security/mineral-resources-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mineral-resources-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mineralresources.com.au/
- group: company
  title: ''
  type: About
  url: https://www.mineralresources.com.au/about-us/who-we-are/
- group: other
  title: ''
  type: Leadership
  url: https://www.mineralresources.com.au/about-us/leadership/
- group: company
  title: ''
  type: Newsroom
  url: https://www.mineralresources.com.au/news/
- group: operate
  title: ''
  type: Support
  url: https://www.mineralresources.com.au/get-in-touch/
- group: company
  title: ''
  type: Careers
  url: https://www.mineralresources.com.au/careers/
- group: company
  title: ''
  type: Investors
  url: https://www.mineralresources.com.au/investor-centre/
- group: other
  title: ''
  type: Sustainability
  url: https://www.mineralresources.com.au/sustainability/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mineralresources.com.au/privacy-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://www.mineralresources.com.au/disclaimer/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mineral-resources-limited
- group: other
  title: ''
  type: X
  url: https://twitter.com/mrlminres
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/mineralresourceslimited
coverage:
  checked: '2026-10-22'
  detail: MinRes is an ASX-listed mining services, iron ore and lithium company; its site, sitemap and llms.txt name no API, developer portal or spec, and /openapi.json returns 404.
  evidence:
  - status: 200
    url: https://www.mineralresources.com.au/
  - status: 200
    url: https://www.mineralresources.com.au/llms.txt
  - status: 404
    url: https://www.mineralresources.com.au/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-21'
description: 'Mineral Resources Limited (MinRes, ASX: MIN) is an Australian mining services and diversified resources company with operations in iron ore and lithium, spanning mining services (mining and processing, transport and logistics, innovation, manufacturing), engineering and construction, iron ore (Onslow Iron, Pilbara Hub), lithium (Wodgina, Mt Marion, Bald Hill) and energy (exploration, gas production, power). Its website publishes no public API, developer portal or API documentation; this profile records the company''s published web presence.'
image: https://www.mineralresources.com.au/_next/static/media/open-graph.3jjb6q4v1_7bp.png
layout: provider
modified: '2026-10-22'
name: Mineral Resources
nav: Providers
network: true
overview: 'Mineral Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mining, Mining Services, Iron Ore, and Lithium.


  Mineral Resources'' developer surface includes support, YouTube channel, and 15 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 7.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mineral Resources Domain Security
  slug: mineral-resources-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mineral-resources
tags:
- Company
- Mining
- Mining Services
- Iron Ore
- Lithium
- Energy
- Australia
website: https://www.mineralresources.com.au/
---
