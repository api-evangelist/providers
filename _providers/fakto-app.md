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
  href: https://artifacts.apis.io/fakto-app/well-known/fakto-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fakto-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/fakto-app/hosts/fakto-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fakto-app-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://fakto.app/mcp/pricing
- group: start
  title: ''
  type: Login
  url: https://fakto.app/mcp/login
- group: auth
  href: https://artifacts.apis.io/fakto-app/security/fakto-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fakto-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fakto.app/
- group: docs
  title: ''
  type: Documentation
  url: https://fakto.app/mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fakto.app/mcp/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fakto.app/mcp/privacy-policy
created: '2026-10-30'
description: Fakto.app provides an AI-driven integration platform that connects Polish accounting software wFirma and Fakturownia with large language models like ChatGPT and Claude. It automates invoicing, client management, and payment tracking through natural language commands, offering a no‑code assistant for businesses to streamline bookkeeping tasks.
image: https://fakto.app/mcp/og-image.png
layout: provider
modified: '2026-10-30'
name: fakto-app
nav: Providers
network: true
overview: 'fakto-app is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Accounting, Integration, Poland, and Automation.


  fakto-app''s developer surface includes pricing, documentation, and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fakto-app/fakto-app-2026-11-03T131815.png
security:
- kind: domain-security
  name: Fakto App Domain Security
  slug: fakto-app-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: fakto-app
tags:
- Artificial Intelligence
- Accounting
- Integration
- Poland
- Automation
website: https://fakto.app/
---
