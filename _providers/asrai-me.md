---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Asrai Me Agentic Access
  operation_count: 43
  slug: asrai-me-agentic-access
  summary_line: 43 operations · 1 acting
api_count: 1
apis:
- baseURL: https://x402.asrai.me/v1
  baseurl_source: declared
  description: The AI API from Asrai — 1 operation(s) for ai.
  name: Asrai AI API
  slug: asrai-me-ai-api
- baseURL: https://x402.asrai.me/v1
  baseurl_source: declared
  description: The Cashflow API from Asrai — 3 operation(s) for cashflow.
  name: Asrai Cashflow API
  slug: asrai-me-cashflow-api
- baseURL: https://x402.asrai.me/v1
  baseurl_source: declared
  description: The Market Data API from Asrai — 12 operation(s) for market data.
  name: Asrai Market Data API
  slug: asrai-me-market-data-api
- baseURL: https://x402.asrai.me/v1
  baseurl_source: declared
  description: The Screeners API from Asrai — 16 operation(s) for screeners.
  name: Asrai Screeners API
  slug: asrai-me-screeners-api
- baseURL: https://x402.asrai.me/v1
  baseurl_source: declared
  description: The Technical API from Asrai — 11 operation(s) for technical.
  name: Asrai Technical API
  slug: asrai-me-technical-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/asrai-me/agentic-access/asrai-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asrai-me-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/asrai-me/plans/asrai-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asrai-me-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asrai-me/rules/asrai-me-rules.yml
  title: ''
  type: Spectral
  url: rules/asrai-me-rules.yml
- group: design
  href: https://artifacts.apis.io/asrai-me/vocabulary/asrai-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asrai-me-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/asrai-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/asrai-me/authentication/asrai-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asrai-me-authentication.yml
- group: design
  href: https://artifacts.apis.io/asrai-me/lifecycle/asrai-me-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/asrai-me-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/asrai-me/conformance/asrai-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asrai-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asrai-me/llms/asrai-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asrai-me-llms.txt
- group: other
  href: https://artifacts.apis.io/asrai-me/hosts/asrai-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asrai-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/asrai-me/vendors/asrai-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asrai-me-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://asrai.me/screener/trust
- group: company
  title: ''
  type: Newsroom
  url: https://asrai.me/news
- group: start
  title: ''
  type: Login
  url: https://asrai.me/login
- group: docs
  title: ''
  type: APIReference
  url: https://asrai.me/agents
- group: auth
  href: https://artifacts.apis.io/asrai-me/security/asrai-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asrai-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asrai.me/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asrai.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asrai.me/privacy
created: '2026-11-01'
description: Asrai is a crypto AI agent platform that scans thousands of coins daily with ALSAT, AlphaTrend and TD, provides AI‑powered trading signals, market analysis, 90‑day outlooks, and a public track record. It offers free starter access and integrates with Telegram.
image: https://asrai.me/icons/og-image.png
layout: provider
modified: '2026-11-01'
name: Asrai
nav: Providers
network: true
overview: 'Asrai publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, Cashflow API, Market Data API, and 2 more. Tagged areas include Cryptocurrency, Artificial Intelligence, Trading, Signals, and Telegram.


  The Asrai catalog on APIs.io includes 1 Spectral governance ruleset.


  Asrai''s developer surface includes authentication, API reference, and 17 more developer resources.'
plans:
- name: Asrai Me Plans Pricing
  plan_count: 3
  slug: asrai-me-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Asrai Me Rate Limits
  slug: asrai-me-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Asrai API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: asrai-me-rules
scopes:
- name: Asrai Me Scopes
  scope_count: 0
  slug: asrai-me-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 46.0
    developer_ergonomics: 21.9
    discoverability: 67.0
    operational_transparency: 0.0
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 34.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asrai Me Authentication
  slug: asrai-me-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Asrai Me Domain Security
  slug: asrai-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: ask-ai
  slug: asrai-me-ask-ai
- name: get-alsat
  slug: asrai-me-get-alsat
- name: get-signal
  slug: asrai-me-get-signal
slug: asrai-me
tags:
- Cryptocurrency
- Artificial Intelligence
- Trading
- Signals
- Telegram
- Analytics
website: https://asrai.me/
---
