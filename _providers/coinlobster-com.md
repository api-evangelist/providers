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
api_count: 1
apis:
- description: Real-time crypto whale tracker API providing live trades, alerts, and market data.
  name: CoinLobster Crypto Data API
  slug: coinlobster-crypto-data-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/coinlobster-com/plans/coinlobster-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coinlobster-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coinlobster-com/conformance/coinlobster-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinlobster-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinlobster-com/llms/coinlobster-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinlobster-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinlobster-com/well-known/coinlobster-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinlobster-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coinlobster-com/hosts/coinlobster-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinlobster-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinlobster-com/vendors/coinlobster-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinlobster-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://coinlobster.com/login
- group: company
  title: ''
  type: Blog
  url: https://coinlobster.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoinLobster
- group: auth
  href: https://artifacts.apis.io/coinlobster-com/security/coinlobster-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinlobster-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinlobster.com/
- group: docs
  title: ''
  type: Documentation
  url: https://coinlobster.com/docs
- group: other
  title: ''
  type: Developers
  url: https://coinlobster.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://coinlobster.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinlobster.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinlobster.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://coinlobster.com/faq
created: '2026-11-04'
description: CoinLobster provides live crypto market data, tracking whale trades, order books, funding, and smart‑money positions across 18 exchanges and 3 blockchains. The platform offers a terminal, radar, and AI‑driven insights, with free sign‑up and API access for developers and traders.
image: https://coinlobster.com/images/og-home.png
layout: provider
modified: '2026-11-04'
name: CoinLobster
nav: Providers
network: true
overview: 'CoinLobster is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Data, WhaleTracking, and Artificial Intelligence.


  CoinLobster''s developer surface includes engineering blog, documentation, pricing, support, and 13 more developer resources.'
plans:
- name: Coinlobster Com Plans Pricing
  plan_count: 2
  slug: coinlobster-com-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinlobster Com Domain Security
  slug: coinlobster-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinlobster-com
tags:
- Cryptocurrency
- Data
- WhaleTracking
- Artificial Intelligence
website: https://coinlobster.com/
---
