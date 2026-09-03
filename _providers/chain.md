---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Chain's unified REST API for stablecoin payments (funding, payouts, payees), card issuing, wallets, and a double-entry ledger. Bearer API-key auth with sandbox and live key prefixes (sk_sandbox_ / sk_
  name: Chain API
  slug: chain-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chain.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chain.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://chain.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://chain.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://chain.com/documentation
- group: auth
  title: ''
  type: Authentication
  url: authentication/chain-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: https://chain.com/documentation/webhooks
- group: build
  title: ''
  type: SDKs
  url: https://chain.com/documentation/sdks
- group: build
  title: ''
  type: Packages
  url: packages/chain-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chain-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/chain-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chain-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/chain-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chain-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://chain.com/blog
- group: operate
  title: ''
  type: Support
  url: https://chain.com/support
- group: operate
  title: ''
  type: ChangeLog
  url: https://chain.com/developers/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://chain.com/developers/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chain
- group: start
  title: ''
  type: SignUp
  url: https://app.chain.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chain.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chain.com/privacy-policy
created: '2026-07-17'
description: Chain is a stablecoin payments infrastructure platform that lets enterprises move money globally across both traditional banking rails and digital-currency networks. Its unified REST API covers funding, payouts and payees; virtual and physical card issuing; wallet registration with compliance screening; and a double-entry ledger for reconciliation. Chain connects ACH, Fedwire, FedNow, SEPA, Faster Payments, Visa and Mastercard with multi-stablecoin support (USDC, USDT, USDP, RLUSD) for real-time settlement and payouts to 200+ countries. The platform exposes API-key (Bearer) authentication, an idempotency-key header, webhooks with signature verification, and separate sandbox and live environments for developers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chain.png
layout: provider
modified: '2026-07-18'
name: Chain
nav: Providers
network: true
overview: 'Chain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Stablecoins, Cryptocurrency, and Blockchain.


  Chain''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 16 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 32.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chain/refs/heads/main/screenshots/chain-2026-07-25T205022.png
security:
- kind: authentication
  name: Chain Authentication
  slug: chain-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chain Domain Security
  slug: chain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chain
tags:
- Company
- Payments
- Stablecoins
- Cryptocurrency
- Blockchain
- Financial-Services
- Wallets
- Cards
- Cross-Border Payments
website: https://chain.com
---
