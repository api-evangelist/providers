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
api_count: 1
apis:
- description: API documentation for WON's services
  name: WON API
  slug: won-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/won/llms/won-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/won-llms.txt
- group: other
  href: https://artifacts.apis.io/won/hosts/won-hosts.yml
  title: ''
  type: Hosts
  url: hosts/won-hosts.yml
- group: other
  href: https://artifacts.apis.io/won/vendors/won-vendors.yml
  title: ''
  type: Vendors
  url: vendors/won-vendors.yml
- group: auth
  href: https://artifacts.apis.io/won/security/won-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/won-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://won.ai
created: '2026-10-25'
description: WON is an independent business design and strategic advisory firm serving retail, travel, hospitality, and financial services brands. It provides experience intelligence and operational intelligence to drive profit and growth for its clients, leveraging deep industry expertise and data-driven insights.
image: https://won.ai/logo.png
layout: provider
modified: '2026-10-25'
name: WON
nav: Providers
network: true
overview: WON is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advisory, Business-Design, Retail, and Travel.
random_paper: 4
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/won/won-2026-11-03T150230.png
security:
- kind: domain-security
  name: Won Domain Security
  slug: won-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: won
tags:
- Company
- Advisory
- Business-Design
- Retail
- Travel
- Hospitality
- Financial Services
website: https://won.ai
---
