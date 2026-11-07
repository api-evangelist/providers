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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/exnaton/hosts/exnaton-hosts.yml
  title: ''
  type: Hosts
  url: hosts/exnaton-hosts.yml
- group: other
  href: https://artifacts.apis.io/exnaton/vendors/exnaton-vendors.yml
  title: ''
  type: Vendors
  url: vendors/exnaton-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exnaton.ai/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.exnaton.ai/en/press
- group: other
  title: ''
  type: Leadership
  url: https://www.exnaton.ai/team
- group: company
  title: ''
  type: Blog
  url: https://www.exnaton.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.exnaton.com/
- group: auth
  href: https://artifacts.apis.io/exnaton/security/exnaton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/exnaton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://exnaton.com
coverage:
  checked: '2026-10-24'
  detail: The main website renders content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.exnaton.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: 'Exnaton is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by true-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.prod.website-files.com/66dddcf8e9ac180eef47cdcf/69fdb29e43a6cb4ab8349068_026d017cab63c3090ef48a74277b051c_Open%20graph.png
layout: provider
modified: '2026-10-24'
name: Exnaton
nav: Providers
network: true
overview: 'Exnaton is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy Utilities, Energy Sharing, Power Purchase Agreements, EV Charging, and API Integration.


  Exnaton''s developer surface includes pricing, engineering blog, documentation, and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 41.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/exnaton/exnaton-2026-11-03T131734.png
security:
- kind: domain-security
  name: Exnaton Domain Security
  slug: exnaton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: exnaton
tags:
- Energy Utilities
- Energy Sharing
- Power Purchase Agreements
- EV Charging
- API Integration
website: https://exnaton.com
---
