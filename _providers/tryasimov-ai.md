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
  href: https://artifacts.apis.io/tryasimov-ai/hosts/tryasimov-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tryasimov-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/tryasimov-ai/vendors/tryasimov-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tryasimov-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tryasimov-ai/security/tryasimov-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tryasimov-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryasimov.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://tryasimov.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryasimov.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryasimov.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://tryasimov.ai/support
coverage:
  checked: '2026-10-24'
  detail: The provider's website is a JavaScript‑rendered single‑page app with no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://tryasimov.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Asimov builds large‑scale human activity datasets to train next‑generation robots. By collecting real‑world egocentric video, 3‑D pose, depth and annotations across kitchens, offices, hotels and warehouses on three continents, they provide clean, annotated data that bridges the robotics data gap. Backed by Y Combinator, Asimov enables robotics teams to accelerate perception and manipulation models with diverse, organic human motion data.
layout: provider
modified: '2026-10-24'
name: Asimov
nav: Providers
network: true
overview: 'Asimov is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Data, Artificial Intelligence, and Human Intelligence.


  Asimov''s developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.2
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
screenshot: https://apis.io/screenshots/tryasimov-ai/tryasimov-ai-2026-11-03T145128.png
security:
- kind: domain-security
  name: Tryasimov Ai Domain Security
  slug: tryasimov-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tryasimov-ai
tags:
- Company
- Robotics
- Data
- Artificial Intelligence
- Human Intelligence
website: https://tryasimov.ai/
---
