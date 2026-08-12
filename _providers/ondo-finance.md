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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 59
  human_in_the_loop: 3
  name: Ondo Finance Agentic Access
  operation_count: 130
  slug: ondo-finance-agentic-access
  summary_line: 130 operations · 59 acting · 3 human-in-the-loop
api_count: 26
apis:
- description: The Account API from Ondo Finance — 3 operation(s) for account.
  name: Ondo Finance Account API
  slug: ondo-finance-account-api
- description: The API Keys API from Ondo Finance — 3 operation(s) for api keys.
  name: Ondo Finance API Keys API
  slug: ondo-finance-api-keys-api
- description: Get Asset Price Information
  name: Ondo Finance Assets API
  slug: ondo-finance-assets-api
- description: Get Mint and Redeem Attestations
  name: Ondo Finance Attestations API
  slug: ondo-finance-attestations-api
- description: The Auth API from Ondo Finance — 12 operation(s) for auth.
  name: Ondo Finance Auth API
  slug: ondo-finance-auth-api
- description: Get On Chain Data
  name: Ondo Finance Chains API
  slug: ondo-finance-chains-api
- description: The Chat API from Ondo Finance — 1 operation(s) for chat.
  name: Ondo Finance Chat API
  slug: ondo-finance-chat-api
- description: The Connection API from Ondo Finance — 2 operation(s) for connection.
  name: Ondo Finance Connection API
  slug: ondo-finance-connection-api
- description: The Fills API from Ondo Finance — 3 operation(s) for fills.
  name: Ondo Finance Fills API
  slug: ondo-finance-fills-api
- description: The Funding Rate API from Ondo Finance — 4 operation(s) for funding rate.
  name: Ondo Finance Funding Rate API
  slug: ondo-finance-funding-rate-api
- description: Get Trading Limits
  name: Ondo Finance Limits API
  slug: ondo-finance-limits-api
- description: The Margin Account API from Ondo Finance — 5 operation(s) for margin account.
  name: Ondo Finance Margin Account API
  slug: ondo-finance-margin-account-api
- description: The Market Data API from Ondo Finance — 9 operation(s) for market data.
  name: Ondo Finance Market Data API
  slug: ondo-finance-market-data-api
- description: The Markets API from Ondo Finance — 1 operation(s) for markets.
  name: Ondo Finance Markets API
  slug: ondo-finance-markets-api
- description: The Orders API from Ondo Finance — 6 operation(s) for orders.
  name: Ondo Finance Orders API
  slug: ondo-finance-orders-api
- description: The Portfolio API from Ondo Finance — 2 operation(s) for portfolio.
  name: Ondo Finance Portfolio API
  slug: ondo-finance-portfolio-api
- description: The Positions API from Ondo Finance — 2 operation(s) for positions.
  name: Ondo Finance Positions API
  slug: ondo-finance-positions-api
- description: The Private Channels API from Ondo Finance — 11 operation(s) for private channels.
  name: Ondo Finance Private Channels API
  slug: ondo-finance-private-channels-api
- description: The Public Channels API from Ondo Finance — 7 operation(s) for public channels.
  name: Ondo Finance Public Channels API
  slug: ondo-finance-public-channels-api
- description: The Sandbox API from Ondo Finance — 2 operation(s) for sandbox.
  name: Ondo Finance Sandbox API
  slug: ondo-finance-sandbox-api
- description: Get Market and Trading Statuses
  name: Ondo Finance Status API
  slug: ondo-finance-status-api
- description: The Stop Orders API from Ondo Finance — 1 operation(s) for stop orders.
  name: Ondo Finance Stop Orders API
  slug: ondo-finance-stop-orders-api
- description: Get Ticker Information
  name: Ondo Finance Tickers API
  slug: ondo-finance-tickers-api
- description: The Tool API from Ondo Finance — 4 operation(s) for tool.
  name: Ondo Finance Tool API
  slug: ondo-finance-tool-api
- description: The TWAP Orders API from Ondo Finance — 5 operation(s) for twap orders.
  name: Ondo Finance TWAP Orders API
  slug: ondo-finance-twap-orders-api
- description: The Wallet API from Ondo Finance — 12 operation(s) for wallet.
  name: Ondo Finance Wallet API
  slug: ondo-finance-wallet-api
artifact_total: 32
common:
- group: company
  title: ''
  type: Website
  url: https://ondo.finance/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ondo.finance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ondo.finance/api-reference/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ondo.finance/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ondo.finance/api-reference/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ondoprotocol
- group: company
  title: ''
  type: Blog
  url: https://www.ondo.finance/insights
- group: operate
  title: ''
  type: Support
  url: https://ondo.finance/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.ondo.finance
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.ondo.finance/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.ondo.finance/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/ondo-finance-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ondo-finance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ondo-finance-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ondo-finance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://immunefi.com/bug-bounty/ondofinance/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ondo-finance-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ondo-finance-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ondo-finance-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ondo-finance-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ondo-finance-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ondo-finance-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ondo.finance/api-reference/upcoming-changes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ondo-finance-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ondo-finance-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ondo-finance-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ondo-finance-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/ondo-finance-gm-backend.proto
- group: other
  title: ''
  type: Overlay
  url: overlays/ondo-finance-gm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ondo-finance-perps-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ondo-finance-perps-ws-overlay.yaml
created: '2026-07-17'
description: 'Ondo Finance builds institutional-grade platforms and infrastructure to bring financial markets onchain, tokenizing real-world assets and equities. Its developer surface spans three APIs: the GM Backend API (Ondo Stocks / Global Markets) for tokenized-stock prices, market data, dividends, trading limits and mint/redeem attestations, exposed over REST plus a gRPC real-time streaming service; and the Ondo Perps REST and WebSocket APIs for perpetual-futures trading with SIWE (EIP-4361) and Web2 authentication, order management, positions, funding and live market data. Products include Ondo Stocks, USDY (yieldcoin) and OUSG (tokenized US Treasuries).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ondo-finance.png
layout: provider
mcp_servers:
- description: ''
  name: ondo-finance-mcp.yml
  slug: ondo-finance-mcpyml
modified: '2026-07-20'
name: Ondo Finance
nav: Providers
network: true
overview: 'Ondo Finance publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Assets API, and 23 more. Tagged areas include Company, Crypto, Tokenization, Real World Assets, and DeFi.


  Ondo Finance''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 25 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 2
  name: Ondo Finance Rate Limits
  slug: ondo-finance-rate-limits
score:
  band: developing
  composite: 51.7
  delta: -0.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 59.8
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 60.5
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ondo-finance/refs/heads/main/screenshots/ondo-finance-2026-08-07T190231.png
security:
- kind: authentication
  name: Ondo Finance Authentication
  slug: ondo-finance-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Ondo Finance Domain Security
  slug: ondo-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ondo Finance Vulnerability Disclosure
  slug: ondo-finance-vulnerability-disclosure
  summary_line: contact published
slug: ondo-finance
tags:
- Company
- Crypto
- Tokenization
- Real World Assets
- DeFi
- Stocks
- Trading
- Perpetual Futures
- Market Data
- Blockchain
- Financial Services
website: https://ondo.finance/
---
