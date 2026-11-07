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
  href: https://artifacts.apis.io/betable-com/llms/betable-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betable-com-llms.txt
- group: other
  href: https://artifacts.apis.io/betable-com/hosts/betable-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betable-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/betable-com/vendors/betable-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betable-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betable.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.betable.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betable.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://betable.com/news/
- group: auth
  href: https://artifacts.apis.io/betable-com/security/betable-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betable-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corp.betable.com
- group: company
  title: ''
  type: Website
  url: https://betable.com
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract was found on any probed host.
  evidence:
  - status: 522
    url: https://api.betable.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Betable provides a modern platform infrastructure combined with iGaming expertise, enabling operators to launch, manage, and grow casino, sportsbook, player accounts, payments, CRM, and compliance solutions from a single platform, wallet, and contract. The company focuses on delivering flexible, controllable gaming services for operators worldwide.
image: https://betable.com/wp-content/themes/betable/assets/favicons/og-image.png
layout: provider
modified: '2026-10-29'
name: corp
nav: Providers
network: true
overview: corp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, iGaming, Platform, Casinos, and Company.
random_paper: 3
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/betable-com/betable-com-2026-11-03T121702.png
security:
- kind: domain-security
  name: Betable Com Domain Security
  slug: betable-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: betable-com
tags:
- Gaming
- iGaming
- Platform
- Casinos
- Company
website: https://corp.betable.com
---
