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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/maxworth-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/maxworth-app/llms/maxworth-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maxworth-app-llms.txt
- group: other
  href: https://artifacts.apis.io/maxworth-app/hosts/maxworth-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maxworth-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/maxworth-app/vendors/maxworth-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maxworth-app-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://maxworth.app/news/
- group: auth
  href: https://artifacts.apis.io/maxworth-app/security/maxworth-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maxworth-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maxworth.app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maxworth.app/privacy/
- group: company
  title: ''
  type: About
  url: https://maxworth.app/about/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://maxworth.app/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: MaxWorth is a privacy‑first credit card benefits tracker that aggregates recurring credits, annual‑fee ROI, card‑linked offers and cashback portal rates without requiring users to connect a bank account. The service provides an iOS app, browser extensions, and a web portal to track card benefits, redemption progress, reset dates, and offer recommendations across US, Canada and Australia credit cards.
image: https://maxworth.app/assets/logo/og-default.png
layout: provider
modified: '2026-10-30'
name: maxworth-app
nav: Providers
network: true
overview: maxworth-app is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Credit Cards, Privacy, and Tracker.
random_paper: 8
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.3
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 7.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/maxworth-app/maxworth-app-2026-11-03T135354.png
security:
- kind: domain-security
  name: Maxworth App Domain Security
  slug: maxworth-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maxworth-app
tags:
- Company
- Finance
- Credit Cards
- Privacy
- Tracker
website: https://maxworth.app/
---
