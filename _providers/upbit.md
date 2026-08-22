---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Upbit Agentic Access
  operation_count: 44
  slug: upbit-agentic-access
  summary_line: 44 operations · 13 acting
api_count: 8
apis:
- description: The Upbit WebSocket API delivers real-time streaming data for market and account events. Public streams include live tickers, full orderbook updates, OHLCV candles, and trade feeds for any trading pai
  name: Upbit WebSocket API
  slug: websocket-api
- description: Account balance and portfolio endpoints — JWT required
  name: Upbit Exchange - Account API
  slug: upbit-exchange-account-api
- description: Deposit management endpoints — JWT required
  name: Upbit Exchange - Deposits API
  slug: upbit-exchange-deposits-api
- description: Order management endpoints — JWT required
  name: Upbit Exchange - Orders API
  slug: upbit-exchange-orders-api
- description: Service status and API key endpoints — JWT required
  name: Upbit Exchange - Service API
  slug: upbit-exchange-service-api
- description: Travel Rule compliance endpoints — JWT required
  name: Upbit Exchange - Travel Rule API
  slug: upbit-exchange-travel-rule-api
- description: Withdrawal management endpoints — JWT required
  name: Upbit Exchange - Withdrawals API
  slug: upbit-exchange-withdrawals-api
- description: Public market data endpoints — no authentication required
  name: Upbit Quotation API
  slug: upbit-quotation-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Upbit REST Exchange - Account API
  slug: open-upbit-exchange-account-api
- collection_type: open
  name: Upbit REST Exchange - Account Exchange - Deposits API
  slug: open-upbit-exchange-deposits-api
- collection_type: open
  name: Upbit REST Exchange - Account Exchange - Orders API
  slug: open-upbit-exchange-orders-api
- collection_type: open
  name: Upbit REST Exchange - Account Exchange - Service API
  slug: open-upbit-exchange-service-api
- collection_type: open
  name: Upbit REST Exchange - Account Exchange - Travel Rule API
  slug: open-upbit-exchange-travel-rule-api
- collection_type: open
  name: Upbit REST Exchange - Account Exchange - Withdrawals API
  slug: open-upbit-exchange-withdrawals-api
- collection_type: open
  name: Upbit REST Exchange - Account Quotation API
  slug: open-upbit-quotation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upbit-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/upbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upbit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://upbit.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://global-docs.upbit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://global-docs.upbit.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://global-docs.upbit.com/docs/first-exchange-api-call
- group: auth
  title: ''
  type: Authentication
  url: https://global-docs.upbit.com/reference/auth
- group: operate
  title: ''
  type: RateLimits
  url: https://global-docs.upbit.com/reference/rate-limits
- group: build
  title: ''
  type: GitHub
  url: https://github.com/upbit-exchange
- group: build
  title: ''
  type: SDKs
  url: https://global-docs.upbit.com/docs/sdk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upbit.com/service_center/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upbit.com/service_center/privacy_policy
- group: operate
  title: ''
  type: Support
  url: https://global-docs.upbit.com/docs/support
- group: agent
  title: ''
  type: LlmsText
  url: https://global-docs.upbit.com/llms.txt
- group: other
  title: ''
  type: Announcements
  url: https://global-docs.upbit.com/docs/announcements
created: '2026-06-13'
description: Upbit is a leading South Korean cryptocurrency exchange operated by Dunamu Inc., offering REST and WebSocket APIs for market data retrieval, order management, account balances, and transaction history. Developers must register an Upbit account with security level 2 or higher to issue API keys. Authenticated requests use JWT bearer tokens (HS512) generated from an Access Key and Secret Key pair, while public quotation endpoints (market data, tickers, orderbooks, candles) require no authentication. Upbit supports KRW, BTC, and USDT trading markets and complies with travel-rule regulations for digital asset transfers. Regional API endpoints are available for Korea, Singapore, Indonesia, and Thailand.
finops:
- name: Upbit Finops
  service_category: Financial Services
  slug: upbit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upbit.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: Upbit
nav: Providers
network: true
overview: 'Upbit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Exchange - Account API, Exchange - Deposits API, Exchange - Orders API, and 4 more. Tagged areas include Cryptocurrency, Exchange, Market Data, Orders, and Trading.


  The Upbit catalog on APIs.io includes 1 JSON-LD context.


  Upbit''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, support, and 12 more developer resources.'
plans:
- name: Upbit Plans Pricing
  plan_count: 2
  slug: upbit-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Upbit Rate Limits
  slug: upbit-rate-limits
score:
  band: developing
  composite: 42.0
  delta: -9.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 60.5
    developer_ergonomics: 31.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 48.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/upbit/refs/heads/main/screenshots/upbit-2026-06-20T200501.png
security:
- kind: authentication
  name: Upbit Authentication
  slug: upbit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Upbit Domain Security
  slug: upbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Upbit Vulnerability Disclosure
  slug: upbit-vulnerability-disclosure
  summary_line: disclosure policy published
slug: upbit
tags:
- Cryptocurrency
- Exchange
- Market Data
- Orders
- Trading
- WebSocket
website: https://upbit.com
---
