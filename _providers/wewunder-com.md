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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/wewunder-com/well-known/wewunder-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wewunder-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/wewunder-com/hosts/wewunder-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wewunder-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wewunder-com/vendors/wewunder-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wewunder-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wunderpower.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.wunderpower.com/press
- group: start
  title: ''
  type: Login
  url: https://app.wunderpower.com/login
- group: auth
  href: https://artifacts.apis.io/wewunder-com/security/wewunder-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wewunder-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wewunder.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://wewunder.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: 'Wunder is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by techstars) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.sanity.io/images/wxj9gge9/production/334b68c51b4ea650f360994a443747af9d6de626-3072x2304.png?w=600&auto=format
layout: provider
modified: '2026-10-24'
name: Wunder
nav: Providers
network: true
overview: Wunder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Solar, Battery Storage, EV Charging, ESG Reporting, and Portfolio Management.
random_paper: 21
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wewunder-com/wewunder-com-2026-11-03T150137.png
security:
- kind: domain-security
  name: Wewunder Com Domain Security
  slug: wewunder-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wewunder-com
tags:
- Solar
- Battery Storage
- EV Charging
- ESG Reporting
- Portfolio Management
- Real Estate Energy Solutions
website: https://wewunder.com/
---
