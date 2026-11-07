---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Oddiwire provides a real-time esports odds API covering major titles. The API offers REST endpoints under the base URL https://oddiwire.com, e.g., /v1/health, /v1/fixtures, and SSE streams.
  name: Oddiwire API
  slug: oddiwire-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/oddiwire-com/plans/oddiwire-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oddiwire-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/oddiwire-com/llms/oddiwire-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oddiwire-com-llms.txt
- group: other
  href: https://artifacts.apis.io/oddiwire-com/hosts/oddiwire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oddiwire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/oddiwire-com/vendors/oddiwire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oddiwire-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oddiwire.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oddiwire.com/privacy.html
- group: auth
  href: https://artifacts.apis.io/oddiwire-com/security/oddiwire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oddiwire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oddiwire.com/
created: '2026-10-30'
description: Oddiwire provides a real-time esports odds API covering major titles like League of Legends, CS2, Dota 2, Valorant, and more. The service offers REST and SSE endpoints delivering raw no‑vig probabilities, market names, and totals. It includes documentation, pricing, a dashboard, and status page, and is not affiliated with ODDIN.GG. The platform aims to give developers easy access to live esports betting data.
image: https://oddiwire.com/og-cover.png?v=2
layout: provider
modified: '2026-10-30'
name: oddiwire-com
nav: Providers
network: true
overview: oddiwire-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Esports, Odds, Real-Time, and Betting.
plans:
- name: Oddiwire Com Plans Pricing
  plan_count: 4
  slug: oddiwire-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 16.9
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/oddiwire-com/oddiwire-com-2026-11-03T140444.png
security:
- kind: domain-security
  name: Oddiwire Com Domain Security
  slug: oddiwire-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oddiwire-com
tags:
- Company
- Esports
- Odds
- Real-Time
- Betting
website: https://oddiwire.com/
---
