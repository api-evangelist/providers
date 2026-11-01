---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://cfenv.com/api/graphql
  baseurl_source: declared
  description: GraphQL API for Chengfengtechnology data platform
  name: Chengfengtechnology GraphQL API
  slug: chengfengtechnology-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/chengfengtechnology/llms/chengfengtechnology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chengfengtechnology-llms.txt
- group: agent
  href: https://artifacts.apis.io/chengfengtechnology/well-known/chengfengtechnology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chengfengtechnology-well-known.yml
- group: other
  href: https://artifacts.apis.io/chengfengtechnology/hosts/chengfengtechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chengfengtechnology-hosts.yml
- group: other
  href: https://artifacts.apis.io/chengfengtechnology/vendors/chengfengtechnology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chengfengtechnology-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cfenv.com/blogs/news
- group: auth
  href: https://artifacts.apis.io/chengfengtechnology/security/chengfengtechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chengfengtechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cfenv.com/pages/about-us
- group: operate
  title: ''
  type: Contact
  url: https://cfenv.com/pages/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cfenv.com/pages/privacy-policy
coverage:
  checked: '2026-10-08'
  detail: No owned OpenAPI/GraphQL contract could be verified for Chengfengtechnology; the GraphQL endpoint appears unrelated.
  evidence:
  - status: 200
    url: https://cfenv.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Shanghai Chengfeng Technology Co., Ltd. provides water monitoring and testing solutions, including unmanned vessels, buoy stations, and data platforms. Established in 2008, the company offers ISO‑certified products and services worldwide, focusing on environmental monitoring, water quality analysis, and integrated hardware‑software systems.
layout: provider
modified: '2026-10-08'
name: Chengfengtechnology
nav: Providers
network: true
overview: 'Chengfengtechnology is listed with 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Company, Water Monitoring, Environmental Tech, IoT, and China.'
random_paper: 1
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 13.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chengfengtechnology Domain Security
  slug: chengfengtechnology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: chengfengtechnology
tags:
- Company
- Water Monitoring
- Environmental Tech
- IoT
- China
website: https://cfenv.com/pages/about-us
---
