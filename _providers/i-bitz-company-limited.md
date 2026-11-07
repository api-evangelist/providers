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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/i-bitz-company-limited/hosts/i-bitz-company-limited-hosts.yml
  title: ''
  type: Hosts
  url: hosts/i-bitz-company-limited-hosts.yml
- group: other
  href: https://artifacts.apis.io/i-bitz-company-limited/vendors/i-bitz-company-limited-vendors.yml
  title: ''
  type: Vendors
  url: vendors/i-bitz-company-limited-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/i-bitz
- group: auth
  href: https://artifacts.apis.io/i-bitz-company-limited/security/i-bitz-company-limited-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/i-bitz-company-limited-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.i-bitz.co.th
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.co.th/mcp
  - status: 200
    url: https://www.i-bitz.co.th
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: i-bitz company limited provides geospatial and Internet of Things technology solutions, primarily through its SaaS products Vallaris, a web‑mapping and GIS tool, and JetStream, a data storage platform for streaming data such as IoT devices. The company serves government agencies and some private sector clients in Thailand, offering GIS web mapping, spatial analysis, and data visualization services.
layout: provider
modified: '2026-10-23'
name: i-bitz company limited
nav: Providers
network: true
overview: i-bitz company limited is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, GIS, Mapping, IoT, and Data Streaming.
random_paper: 0
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/i-bitz-company-limited/i-bitz-company-limited-2026-11-03T133600.png
security:
- kind: domain-security
  name: I Bitz Company Limited Domain Security
  slug: i-bitz-company-limited-domain-security
  summary_line: TLSv1.3
slug: i-bitz-company-limited
tags:
- Geospatial
- GIS
- Mapping
- IoT
- Data Streaming
- Government
website: https://www.i-bitz.co.th
---
