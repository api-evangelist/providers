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
- group: agent
  href: https://artifacts.apis.io/atticstandard-com/llms/atticstandard-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atticstandard-com-llms.txt
- group: other
  href: https://artifacts.apis.io/atticstandard-com/hosts/atticstandard-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atticstandard-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atticstandard-com/vendors/atticstandard-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atticstandard-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.atticstandard.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AtticStandard
- group: auth
  href: https://artifacts.apis.io/atticstandard-com/security/atticstandard-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atticstandard-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atticstandard.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atticstandard.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atticstandard.com/privacy-policy
coverage:
  checked: '2026-11-02'
  detail: Attic Standard provides a price benchmark service but offers no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.atticstandard.com/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Attic Standard provides the independent global price benchmark for AI inference. It aggregates published vendor rates, normalizes them into comparable units, and builds weekly indexes that buyers and sellers can use to price contracts, audit pricing fairness, and stabilize budgets. The service offers transparent methodology, data coverage across major AI inference providers, and a neutral reference point for procurement, finance, analysts, and investors.
image: https://cdn.prod.website-files.com/69908f8912eaccb119313c6e/6ab554cd9b77ea5bf8576c1e_b32ff927912fe6cbf27cf072f859e5cf_og-home.png
layout: provider
modified: '2026-11-02'
name: Attic Standard
nav: Providers
network: true
overview: Attic Standard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Inference, Benchmarks, Pricing, and Data.
random_paper: 18
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 12.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atticstandard Com Domain Security
  slug: atticstandard-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atticstandard-com
tags:
- Artificial Intelligence
- Inference
- Benchmarks
- Pricing
- Data
website: https://atticstandard.com/
---
