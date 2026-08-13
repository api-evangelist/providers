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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Mesh Connect Agentic Access
  operation_count: 50
  slug: mesh-connect-agentic-access
  summary_line: 50 operations · 33 acting
api_count: 12
apis:
- description: The Assets API from Mesh Connect — 2 operation(s) for assets.
  name: Mesh Connect Assets API
  slug: mesh-connect-assets-api
- description: The Auth token API from Mesh Connect — 1 operation(s) for auth token.
  name: Mesh Connect Auth token API
  slug: mesh-connect-auth-token-api
- description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Bi'
  name: Mesh Connect Balance API
  slug: mesh-connect-balance-api
- description: The BrokerAccountDetail API from Mesh Connect — 1 operation(s) for brokeraccountdetail.
  name: Mesh Connect BrokerAccountDetail API
  slug: mesh-connect-brokeraccountdetail-api
- description: The Main Clients API from Mesh Connect — 1 operation(s) for main clients.
  name: Mesh Connect Main Clients API
  slug: mesh-connect-main-clients-api
- description: The recommended approach for account authentication. Front manages multiple authentication flows and handles all authentication steps such as MFA codes and OAuth redirect through our web and mobile SD
  name: Mesh Connect Managed Account Authentication API
  slug: mesh-connect-managed-account-authentication-api
- description: The Managed Transfers API from Mesh Connect — 10 operation(s) for managed transfers.
  name: Mesh Connect Managed Transfers API
  slug: mesh-connect-managed-transfers-api
- description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Op'
  name: Mesh Connect Portfolio API
  slug: mesh-connect-portfolio-api
- description: The Registered Clients API from Mesh Connect — 3 operation(s) for registered clients.
  name: Mesh Connect Registered Clients API
  slug: mesh-connect-registered-clients-api
- description: Not recommended approach. Using this approach, the API client is responsible for handling multiple authentication flows and supporting future updates and changes.
  name: Mesh Connect Self Managed Account Authentication API
  slug: mesh-connect-self-managed-account-authentication-api
- description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Bi'
  name: Mesh Connect Transactions API
  slug: mesh-connect-transactions-api
- description: '### Supported integrations: ```Robinhood``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Binance``` ```Gemini``` ```OkCoin``` ```KuCoin``` ```BinanceInternational``` ```Bitstamp```'
  name: Mesh Connect Transfers API
  slug: mesh-connect-transfers-api
artifact_total: 18
asyncapis:
- description: ''
  name: Mesh Connect Transfers Webhooks
  slug: mesh-connect-transfers-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mesh-connect-admin-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mesh-connect-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.meshpay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.meshconnect.com/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meshconnect.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meshconnect.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.meshconnect.com/build/15min-quickstart
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
- group: start
  title: ''
  type: Login
  url: https://dashboard.meshconnect.com/login
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
  url: security/mesh-connect-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mesh-connect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mesh-connect-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/mesh-connect-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mesh-connect-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mesh-connect-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mesh-connect-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mesh-connect-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mesh-connect-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mesh-connect-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mesh-connect-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mesh-connect-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mesh-connect-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mesh-connect-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/mesh-connect-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mesh-connect-transfers-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mesh (formerly Mesh Connect) is a global crypto payments network that lets businesses accept crypto payments from 300+ wallets and exchanges and settle in stablecoins or local currency through a single integration. The Mesh Integration API and embeddable Link SDK handle account connection, credential validation, MFA, portfolio and balance aggregation, and managed crypto transfers across exchanges and self-custody wallets. Mesh is backed by Paradigm and operates in the crypto-infrastructure sector.
image: https://cdn.prod.website-files.com/656cc624086b77872a31a084/68d80ffccc987492d4bd2e0a_Untitled%20design%20(81).png
layout: provider
mcp_servers:
- description: ''
  name: mesh-connect-mcp.yml
  slug: mesh-connect-mcpyml
modified: '2026-07-20'
name: Mesh Connect
nav: Providers
network: true
overview: 'Mesh Connect publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Auth token API, Balance API, and 9 more. Tagged areas include Company, Crypto Infrastructure, Crypto Payments, Digital Assets, and Wallets.


  The Mesh Connect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mesh Connect''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, sandbox, changelog, and 24 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 53.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.8
    developer_ergonomics: 64.7
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mesh-connect/refs/heads/main/screenshots/mesh-connect-2026-08-07T172619.png
security:
- kind: authentication
  name: Mesh Connect Authentication
  slug: mesh-connect-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Mesh Connect Domain Security
  slug: mesh-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mesh Connect Trust Center
  slug: mesh-connect-trust-center
  summary_line: SOC 2
slug: mesh-connect
tags:
- Company
- Crypto Infrastructure
- Crypto Payments
- Digital Assets
- Wallets
- Exchanges
- Embedded Finance
- Stablecoins
- Payments
website: https://www.meshpay.com
---
