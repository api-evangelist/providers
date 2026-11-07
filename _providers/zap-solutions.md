---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
artifact_total: 0
common:
- group: other
  href: https://artifacts.apis.io/zap-solutions/hosts/zap-solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zap-solutions-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://zap.solutions
coverage:
  checked: '2026-10-14'
  detail: zap.solutions serves a Namecheap 'Domain registration has expired' parking page over HTTP (HTTPS and api.zap.solutions do not connect), so the company publishes no developer program, docs or contract.
  evidence:
  - status: 200
    url: http://zap.solutions
  - status: 0
    url: https://api.zap.solutions
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Zap Solutions, Inc. is a money transmitter / virtual-currency business surfaced in the NYDFS crypto-exchange market-gap harvest; Indiana DFI lists Zap Solutions, Inc. with a Money Transmitter license (No. 64521, issued 2023-08-17). Its website domain zap.solutions currently serves a Namecheap 'Domain registration has expired' parking page over HTTP and does not answer HTTPS, and no public API, developer portal or documentation was found.
layout: provider
modified: '2026-10-14'
name: Zap Solutions
nav: Providers
network: true
overview: Zap Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Money Transmission, Virtual Currency, and Cryptocurrency.
random_paper: 16
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: zap-solutions
tags:
- Company
- Payments
- Money Transmission
- Virtual Currency
- Cryptocurrency
- Fintech
website: https://zap.solutions
---
