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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-08-19'
api_count: 9
apis:
- description: The Assets API from Mesh — 2 operation(s) for assets.
  name: Mesh Assets API
  slug: mesh-assets-api
- description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Bi'
  name: Mesh Balance API
  slug: mesh-balance-api
- description: The BrokerAccountDetail API from Mesh — 1 operation(s) for brokeraccountdetail.
  name: Mesh BrokerAccountDetail API
  slug: mesh-brokeraccountdetail-api
- description: The recommended approach for account authentication. Front manages multiple authentication flows and handles all authentication steps such as MFA codes and OAuth redirect through our web and mobile SD
  name: Mesh Managed Account Authentication API
  slug: mesh-managed-account-authentication-api
- description: The Managed Transfers API from Mesh — 10 operation(s) for managed transfers.
  name: Mesh Managed Transfers API
  slug: mesh-managed-transfers-api
- description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Op'
  name: Mesh Portfolio API
  slug: mesh-portfolio-api
- description: Not recommended approach. Using this approach, the API client is responsible for handling multiple authentication flows and supporting future updates and changes.
  name: Mesh Self Managed Account Authentication API
  slug: mesh-self-managed-account-authentication-api
- description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Bi'
  name: Mesh Transactions API
  slug: mesh-transactions-api
- description: '### Supported integrations: ```Robinhood``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Binance``` ```Gemini``` ```OkCoin``` ```KuCoin``` ```BinanceInternational``` ```Bitstamp```'
  name: Mesh Transfers API
  slug: mesh-transfers-api
artifact_total: 24
asyncapis:
- description: ''
  name: Mesh Transfers Webhooks
  slug: mesh-transfers-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mesh Connect Integration Assets API
  slug: open-mesh-assets-api
- collection_type: open
  name: Mesh Connect Integration Assets Balance API
  slug: open-mesh-balance-api
- collection_type: open
  name: Mesh Connect Integration Assets BrokerAccountDetail API
  slug: open-mesh-brokeraccountdetail-api
- collection_type: open
  name: Mesh Connect Integration Assets Managed Account Authentication API
  slug: open-mesh-managed-account-authentication-api
- collection_type: open
  name: Mesh Connect Integration Assets Managed Transfers API
  slug: open-mesh-managed-transfers-api
- collection_type: open
  name: Mesh Connect Integration Assets Portfolio API
  slug: open-mesh-portfolio-api
- collection_type: open
  name: Mesh Connect Integration Assets Self Managed Account Authentication API
  slug: open-mesh-self-managed-account-authentication-api
- collection_type: open
  name: Mesh Connect Integration Assets Transactions API
  slug: open-mesh-transactions-api
- collection_type: open
  name: Mesh Connect Integration Assets Transfers API
  slug: open-mesh-transfers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mesh-integration-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.meshconnect.com/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meshconnect.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.meshconnect.com/build/15min-quickstart
- group: start
  title: ''
  type: Login
  url: https://dashboard.meshconnect.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.meshpay.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FrontFin
- group: operate
  title: ''
  type: StatusPage
  url: https://status.meshconnect.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meshpay.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meshpay.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.meshpay.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.meshpay.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/mesh-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mesh-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mesh-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mesh-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mesh-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mesh-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mesh-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mesh-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mesh-transfers-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mesh-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/mesh-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mesh-packages.yml
- group: design
  title: ''
  type: Components
  url: components/mesh-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mesh-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mesh-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mesh-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mesh is the first global crypto payments network, connecting hundreds of exchanges, wallets, and financial platforms into a single, unified infrastructure layer so businesses can let users pay, get paid, deposit, and transfer digital assets from any wallet on any chain. The Mesh Connect Integration API lets developers programmatically generate Link tokens for Mesh's hosted connection UX, initiate managed crypto transfers (deposit, payment, onramp, withdrawal), read holdings, balances, and transaction history across connected exchange and self-custody accounts, verify wallet ownership, and receive HMAC-signed transfer-status webhooks. Mesh handles credential validation, MFA, OAuth, and per-integration error handling on the developer's behalf. Formerly Front Finance. SOC 2 Type II certified. Backed by Anthemis and General Catalyst.
image: https://cdn.prod.website-files.com/656cc624086b77872a31a084/68d8116f8f0a10f661523cea_Favicon_new.png
layout: provider
mcp_servers:
- description: ''
  name: mesh-mcp.yml
  slug: mesh-mcpyml
modified: '2026-07-20'
name: Mesh
nav: Providers
network: true
overview: 'Mesh publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Balance API, BrokerAccountDetail API, and 6 more. Tagged areas include Company, Crypto, Cryptocurrency, Payments, and Digital Assets.


  The Mesh catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mesh''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, sandbox, and 23 more developer resources.'
random_paper: 131
score:
  band: strong
  composite: 57.9
  delta: 3.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 64.6
    developer_ergonomics: 68.5
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 54.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mesh/refs/heads/main/screenshots/mesh-2026-08-07T172618.png
security:
- kind: authentication
  name: Mesh Authentication
  slug: mesh-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mesh Domain Security
  slug: mesh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mesh Trust Center
  slug: mesh-trust-center
  summary_line: SOC 2 Type II
slug: mesh
tags:
- Company
- Crypto
- Cryptocurrency
- Payments
- Digital Assets
- Financial Services
- Wallets
- Exchanges
- Transfers
- Stablecoins
- Embedded Finance
- Fintech
- On-Ramp
- Blockchain
website: https://docs.meshconnect.com/overview
---
