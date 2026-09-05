---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST API for TRON Energy and Bandwidth rental, energy subscriptions, and AML crypto checks. Endpoints include Get Services, Check Balance, Estimate Energy, Address Info, Calculate Resource Cost, Creat
  name: TronZap REST API
  slug: tronzap-rest-api
- description: Fully public, unauthenticated Orders API for non-custodial wallet integrations. Four operations — POST /v1/orders/calculate (a true dry run whose total is guaranteed to equal the order amount), POST /
  name: TronZap Wallet Orders API
  slug: tronzap-wallet-orders-api
artifact_total: 7
collections:
- collection_type: postman
  name: Tron Energy API by TronZap.com
  slug: postman-tronzap
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tronzap-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tronzap.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tronzap.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tronzap.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-wallets.tronzap.com/getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://tronzap.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tron-energy-market
- group: commercial
  title: ''
  type: Pricing
  url: https://tronzap.com/b2b
- group: start
  title: ''
  type: SignUp
  url: https://dash.tronzap.com/register
- group: start
  title: ''
  type: Login
  url: https://dash.tronzap.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tronzap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tronzap.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://tronzap.com/learn
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tron-energy/tronzap-com/overview
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tronzap-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tronzap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tronzap-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tronzap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tronzap-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tronzap-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tronzap-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tronzap-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tronzap-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tronzap-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tronzap-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tronzap-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: API-first TRON-network infrastructure provider offering automated TRON Energy and Bandwidth rental, energy subscriptions, and AML crypto checks to reduce USDT (TRC-20) transfer costs via delegation to non-custodial wallets.
image: https://tronzap.com/images/logo-1200x630.png
layout: provider
modified: '2026-08-30'
name: TronZap
nav: Providers
network: true
overview: 'TronZap publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Blockchain, Cryptocurrency, TRON, DeFi infrastructure, and Stablecoins.


  TronZap''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 20 more developer resources.'
plans:
- name: Tronzap Plans Pricing
  plan_count: 2
  slug: tronzap-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Tronzap Rate Limits
  slug: tronzap-rate-limits
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 42.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tronzap/refs/heads/main/screenshots/tronzap-2026-09-02T164311.png
security:
- kind: authentication
  name: Tronzap Authentication
  slug: tronzap-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Tronzap Domain Security
  slug: tronzap-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tronzap
tags:
- Blockchain
- Cryptocurrency
- TRON
- DeFi infrastructure
- Stablecoins
- USDT
- TRC-20
- Resource marketplace
- Payments
- Fees optimization
- Web3
- DeFi
- Payouts
- Compliance
- AML
- Developer Tools
- SDK
website: https://tronzap.com/developers
---
