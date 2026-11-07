---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Imbawallet Com Agentic Access
  operation_count: 24
  slug: imbawallet-com-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 2
apis:
- baseURL: https://imbawallet.com
  baseurl_source: declared
  description: Register, assertion JWT, webhook, HMAC
  name: imbawallet-com Auth API
  slug: imbawallet-com-auth-api
- baseURL: https://imbawallet.com
  baseurl_source: declared
  description: Partner settlement balance
  name: imbawallet-com Balance API
  slug: imbawallet-com-balance-api
- baseURL: https://imbawallet.com
  baseurl_source: declared
  description: Card catalog, issue, list, secrets, topup, freeze
  name: imbawallet-com Cards API
  slug: imbawallet-com-cards-api
- baseURL: https://imbawallet.com
  baseurl_source: declared
  description: Cards, eSIM, gifts, and catalog reads
  name: imbawallet-com Catalog API
  slug: imbawallet-com-catalog-api
- baseURL: https://imbawallet.com
  baseurl_source: declared
  description: USDT TRC-20 deposit address
  name: imbawallet-com Deposit API
  slug: imbawallet-com-deposit-api
- baseURL: https://imbawallet.com
  baseurl_source: declared
  description: USDT withdrawals from partner balance
  name: imbawallet-com Withdrawals API
  slug: imbawallet-com-withdrawals-api
artifact_total: 25
common:
- group: design
  href: https://artifacts.apis.io/imbawallet-com/data-model/imbawallet-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/imbawallet-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/imbawallet-com/agentic-access/imbawallet-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/imbawallet-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/imbawallet-com/rate-limits/imbawallet-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/imbawallet-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/imbawallet-com/rules/imbawallet-com-rules.yml
  title: ''
  type: Spectral
  url: rules/imbawallet-com-rules.yml
- group: design
  href: https://artifacts.apis.io/imbawallet-com/vocabulary/imbawallet-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/imbawallet-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/imbawallet-com/conventions/imbawallet-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/imbawallet-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/imbawallet-com/conventions/imbawallet-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/imbawallet-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/imbawallet-com/authentication/imbawallet-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/imbawallet-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/imbawallet-com/scopes/imbawallet-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/imbawallet-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/imbawallet-com/errors/imbawallet-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/imbawallet-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/imbawallet-com/llms/imbawallet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/imbawallet-com-llms.txt
- group: other
  href: https://artifacts.apis.io/imbawallet-com/a2a/imbawallet-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/imbawallet-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/imbawallet-com/well-known/imbawallet-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/imbawallet-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/imbawallet-com/hosts/imbawallet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/imbawallet-com-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.imbawallet.com/
- group: auth
  href: https://artifacts.apis.io/imbawallet-com/security/imbawallet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imbawallet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://imbawallet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://imbawallet.com/agent_api_about_rus.html
- group: docs
  title: ''
  type: APIReference
  url: https://imbawallet.com/openapi/agent.json
- group: start
  title: ''
  type: GettingStarted
  url: https://imbawallet.com/landing.html
- group: operate
  title: ''
  type: Support
  url: https://imbawallet.com/faq_rus.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imbawallet.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imbawallet.com/privacy
created: '2026-10-30'
description: IMBA Wallet is a fintech service offering virtual Visa and MasterCard cards backed by USDT cryptocurrency, supporting payments via Google Pay, Apple Pay, and the Russian SBP system. Users can register via Telegram, a web browser, or Android app, and manage cards, top‑up with USDT (TRC‑20 and TON) or rubles, access travel eSIM for over 150 countries, and purchase digital gift cards using USDT balances. The platform also provides a prepaid Agent API for agents to deposit USDT and access a catalog, though conversion and withdrawals are currently closed. Documentation is available in Russian, with OpenAPI specifications and well‑known configuration files.
image: https://imbawallet.com/assets/imba_wallet_logo.png
json_schemas:
- name: BalanceResponse
  property_count: 0
  slug: imbawallet-com-balance-response
- name: CardBalanceResponse
  property_count: 0
  slug: imbawallet-com-card-balance-response
- name: CardGetResponse
  property_count: 0
  slug: imbawallet-com-card-get-response
- name: CardIssueRequest
  property_count: 0
  slug: imbawallet-com-card-issue-request
- name: CardIssueResponse
  property_count: 0
  slug: imbawallet-com-card-issue-response
- name: CardListResponse
  property_count: 0
  slug: imbawallet-com-card-list-response
- name: CreateCardRequest
  property_count: 0
  slug: imbawallet-com-create-card-request
- name: DepositAddressResponse
  property_count: 0
  slug: imbawallet-com-deposit-address-response
- name: RegisterRequest
  property_count: 0
  slug: imbawallet-com-register-request
- name: RegisterResponse
  property_count: 0
  slug: imbawallet-com-register-response
- name: TokenResponse
  property_count: 0
  slug: imbawallet-com-token-response
- name: TopupCardRequest
  property_count: 0
  slug: imbawallet-com-topup-card-request
layout: provider
modified: '2026-10-30'
name: imbawallet-com
nav: Providers
network: true
overview: 'imbawallet-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Balance API, Cards API, and 3 more. Tagged areas include Fintech, Payments, Cryptocurrency, Virtual Cards, and Wallets.


  The imbawallet-com catalog on APIs.io includes 1 Spectral governance ruleset.


  imbawallet-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 18 more developer resources.'
plans:
- name: Imbawallet Com Plans Pricing
  plan_count: 0
  slug: imbawallet-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Imbawallet Com Rate Limits
  slug: imbawallet-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: imbawallet-com API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: imbawallet-com-rules
scopes:
- name: Imbawallet Com Scopes
  scope_count: 16
  slug: imbawallet-com-scopes
  summary_line: 16 scopes
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 17.4
    contract_quality: 51.7
    developer_ergonomics: 33.3
    discoverability: 73.2
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/imbawallet-com/imbawallet-com-2026-11-03T133659.png
security:
- kind: authentication
  name: Imbawallet Com Authentication
  slug: imbawallet-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Imbawallet Com Domain Security
  slug: imbawallet-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: imbawallet-com
tags:
- Fintech
- Payments
- Cryptocurrency
- Virtual Cards
- Wallets
website: https://imbawallet.com/
---
