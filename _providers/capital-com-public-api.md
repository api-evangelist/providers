---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Capital Com Public Api Agentic Access
  operation_count: 27
  slug: capital-com-public-api-agentic-access
  summary_line: 27 operations · 11 acting
api_count: 8
apis:
- description: The Capital.com WebSocket API streams real-time market data, supporting up to 40 concurrent instruments and OHLC candlestick subscriptions for low-latency trading applications.
  name: Capital.com WebSocket API
  slug: capital-com-websocket-api
- description: Account information, preferences, and demo top-up.
  name: Capital.com Public API Accounts API
  slug: capital-com-public-api-accounts-api
- description: Server time, ping, and encryption-key utility endpoints.
  name: Capital.com Public API General API
  slug: capital-com-public-api-general-api
- description: Account activity and transaction history.
  name: Capital.com Public API History API
  slug: capital-com-public-api-history-api
- description: Market navigation and instrument lookup.
  name: Capital.com Public API Markets API
  slug: capital-com-public-api-markets-api
- description: Operations for opening, updating, and closing trading positions.
  name: Capital.com Public API Positions API
  slug: capital-com-public-api-positions-api
- description: Operations for creating, switching, and ending API sessions.
  name: Capital.com Public API Session API
  slug: capital-com-public-api-session-api
- description: Operations for managing limit and stop working orders.
  name: Capital.com Public API Working Orders API
  slug: capital-com-public-api-working-orders-api
artifact_total: 18
asyncapis:
- description: Real-time streaming API from Capital.com for market data and OHLC candlestick updates. Clients connect over WebSocket using session tokens (CST and X-SECURITY-TOKEN) obtained from the Capital.com REST
  name: Capital.com WebSocket Streaming API
  slug: capital-com-public-api-asyncapi
collections:
- collection_type: open
  name: Capital.com REST API
  slug: open-capital-com-public-api-capital-com-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capital-com-public-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/capital-com-public-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capital-com-public-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capital-com-public-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capital-com-sv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capitalcom
- group: company
  title: ''
  type: Website
  url: https://capital.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open-api.capital.com
- group: start
  title: ''
  type: Sandbox
  url: https://demo-api-capital.backend-capital.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capital.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capital.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://capital.com/help
- group: company
  title: ''
  type: Blog
  url: https://capital.com/news-and-analysis
created: '2024-12-03'
description: Capital.com is a European trading platform offering CFDs across shares, indices, commodities, forex, and cryptocurrencies. The Capital.com Public API provides direct access to the trading engine for automated strategies, giving programmatic control of positions, working orders, account preferences, and historical and streaming market data. A companion WebSocket API streams real-time prices and OHLC candles for up to 40 concurrent instruments.
finops:
- name: Capital Com Public Api Finops
  service_category: API
  slug: capital-com-public-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capital-com-public-api.png
layout: provider
modified: '2026-05-29'
name: Capital.com Public API
nav: Providers
network: true
overview: 'Capital.com Public API publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Capital.com WebSocket API, Accounts API, General API, and 5 more. Tagged areas include CFD, Commodities, Cryptocurrency, Financial, and Forex.


  The Capital.com Public API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Capital.com Public API''s developer surface includes authentication, documentation, sandbox, support, engineering blog, and 8 more developer resources.'
plans:
- name: Capital Com Public Api Plans Pricing
  plan_count: 3
  slug: capital-com-public-api-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Capital Com Public Api Rate Limits
  slug: capital-com-public-api-rate-limits
rules:
- name: Capital.com Public API API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: capital-com-public-api-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: -7.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 66.0
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 13.2
  previous_composite: 52.8
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
    score: 53.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/capital-com-public-api/refs/heads/main/screenshots/capital-com-public-api-2026-06-20T173937.png
security:
- kind: authentication
  name: Capital Com Public Api Authentication
  slug: capital-com-public-api-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Capital Com Public Api Domain Security
  slug: capital-com-public-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Capital Com Public Api Vulnerability Disclosure
  slug: capital-com-public-api-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: capital-com-public-api
tags:
- CFD
- Commodities
- Cryptocurrency
- Financial
- Forex
- Indices
- Market Data
- Shares
- Streaming
- Trading
- WebSocket
website: https://capital.com/
---
