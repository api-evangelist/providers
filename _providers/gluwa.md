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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: REST API for the Gluwa borderless financial platform — balances, fees, transactions, payment QR codes, wrap/unwrap, and the Exchange API (quotes, orders, order books). Secured with API keys and addres
  name: Gluwa API
  slug: gluwa-api
artifact_total: 4
asyncapis:
- description: ''
  name: Gluwa Webhooks
  slug: gluwa-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://gluwa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.gluwa.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gluwa.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gluwa.com/api/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gluwa.com/get-started/dashboard.md
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.gluwa.com
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@gluwa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gluwa
- group: auth
  title: ''
  type: Authentication
  url: authentication/gluwa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gluwa-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gluwa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gluwa-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gluwa-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gluwa-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/gluwa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gluwa-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gluwa-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gluwa-domain-security.yml
created: '2026-07-17'
description: Gluwa is a borderless financial platform and blockchain infrastructure company that connects emerging markets to the global economy. Its consumer surface is the Gluwa Wallet, Dashboard, Invest (Investor DAO / fixed-term interest accounts) and Exchange, backed by the Gluwacoin interoperable stablecoin standard (USDG, KRWG, NGNG). Gluwa exposes a REST API (balances, fees, transactions, payment QR codes, wrap/unwrap, and an Exchange API for quotes, orders and order books) secured with API keys and address signatures, with webhooks and idempotent transaction requests. Gluwa also builds and operates Creditcoin, an EVM-compatible layer-1 blockchain, and the Universal Smart Contract (USC) multichain framework, shipping TypeScript, Solidity, PHP, .NET and Java SDKs. Originally surfaced as a 500 Global portfolio company.
image: https://gluwa.com/resources/meta-image.png
layout: provider
modified: '2026-07-19'
name: Gluwa
nav: Providers
network: true
overview: 'Gluwa publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Cryptocurrency, Stablecoin, and Payments.


  The Gluwa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gluwa''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, changelog, and 11 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gluwa/refs/heads/main/screenshots/gluwa-2026-07-25T215947.png
security:
- kind: authentication
  name: Gluwa Authentication
  slug: gluwa-authentication
  summary_line: apiKey/http-signature · 2 schemes
- kind: domain-security
  name: Gluwa Domain Security
  slug: gluwa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gluwa
tags:
- Company
- Blockchain
- Cryptocurrency
- Stablecoin
- Payments
- Fintech
- Wallets
- Creditcoin
- Smart Contracts
- Emerging Markets
website: https://gluwa.com
---
