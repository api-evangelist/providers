---
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The MAX Exchange V3 RESTful API — 54 operations across public market data, spot and margin (m-wallet) order management, trade history, wallet balances, deposits, withdrawals, internal transfers, rewar
  name: MAX Exchange REST API v3
  slug: maicoin-max-rest-v3
- description: Real-time streaming service for MAX Exchange. Public channels cover order book (book), trade, ticker, kline, market_status and m-wallet pool_quota; private channels stream order snapshots/updates, tra
  name: MAX Exchange WebSocket API
  slug: maicoin-max-websocket
- description: Unauthenticated system status endpoint reporting whether the MAX API is online or in maintenance, with an ISO 8601 last_changed_at timestamp. Documented in the MAX V3 API reference; status updates may
  name: MAX System Status API
  slug: maicoin-max-status
artifact_total: 8
asyncapis:
- description: 'Real-time streaming for MAX Exchange (MaiCoin). One WebSocket endpoint carries both public market-data channels and, after authentication, private account channels. Field names are abbreviated on the '
  name: MAX Exchange WebSocket API
  slug: maicoin-max-websocket-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maicoin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://max.maicoin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://campaign.maicoin.com/en/api
- group: docs
  title: ''
  type: Documentation
  url: https://campaign.maicoin.com/en/api-document
- group: docs
  title: ''
  type: APIReference
  url: https://max-api.maicoin.com/doc/v3.html
- group: start
  title: ''
  type: GettingStarted
  url: https://campaign.maicoin.com/en/api
- group: operate
  title: ''
  type: Support
  url: https://support.maicoin.com
- group: company
  title: ''
  type: Blog
  url: https://blog.maicoin.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maicoin
- group: operate
  title: ''
  type: StatusPage
  url: https://status-max.maicoin.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://campaign.maicoin.com/en/vip
- group: start
  title: ''
  type: SignUp
  url: https://max.maicoin.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.maicoin.com/max/MAX-Terms-of-Use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assets.maicoin.com/max/max-privacy-policy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maicoin-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/maicoin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/maicoin-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maicoin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/maicoin-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/maicoin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/maicoin-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/maicoin-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/maicoin-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/maicoin-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maicoin-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/maicoin-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/maicoin-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/maicoin-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/maicoin-max-websocket-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/maicoin-max-v3-overlay.yaml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/maicoin-mcp.yml
created: '2026-08-25'
description: MaiCoin is a Taiwan-based digital asset group that operates MAX (MaiCoin Assets eXchange), a regulated cryptocurrency exchange offering spot trading, margin borrowing (m-wallet), staking, and fiat TWD on/off-ramps. MAX publishes a public V3 RESTful trading API with 54 operations spanning public market data (markets, tickers, order book depth, k-line, public trades), order management, trade history, wallet and account balances, deposits and withdrawals, internal transfers, currency conversion, and margin loan/repayment/liquidation. A companion WebSocket streaming service delivers real-time order book, ticker, k-line, trade, market status and private order/trade/account events. Authentication uses HMAC-SHA256 request signing over a base64 payload with X-MAX-ACCESSKEY, X-MAX-PAYLOAD and X-MAX-SIGNATURE headers.
image: https://cdn.prod.website-files.com/61c42c1d462b6844a0915d9b/6a7160b6139bc8cdd5e3cf27_logo_MAX.png
layout: provider
modified: '2026-08-25'
name: MaiCoin
nav: Providers
network: true
overview: 'MaiCoin publishes 1 API on the [APIs.io](https://apis.io/) network: MAX Exchange REST API v3. Tagged areas include Company, Cryptocurrency, Digital Assets, Exchange, and Trading.


  The MaiCoin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MaiCoin''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Maicoin Plans Pricing
  plan_count: 10
  slug: maicoin-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Maicoin Rate Limits
  slug: maicoin-rate-limits
score:
  band: strong
  composite: 60.3
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 42.7
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 65.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Maicoin Authentication
  slug: maicoin-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Maicoin Domain Security
  slug: maicoin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: maicoin
tags:
- Company
- Cryptocurrency
- Digital Assets
- Exchange
- Trading
- Financial Services
- Market Data
- Blockchain
- Taiwan
- WebSocket
website: https://max.maicoin.com
---
