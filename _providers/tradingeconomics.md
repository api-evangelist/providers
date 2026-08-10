---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tradingeconomics Agentic Access
  operation_count: 30
  slug: tradingeconomics-agentic-access
  summary_line: 30 operations
api_count: 7
apis:
- description: Persistent WebSocket connection at wss://stream.tradingeconomics.com delivering live market quote ticks by symbol and push notifications for economic calendar releases, news, and earnings via subscrib
  name: Trading Economics Streaming API
  slug: tradingeconomics-streaming-api
- description: The Economic Calendar API from Trading Economics — 5 operation(s) for economic calendar.
  name: Trading Economics Economic Calendar API
  slug: tradingeconomics-economic-calendar-api
- description: The Financials API from Trading Economics — 2 operation(s) for financials.
  name: Trading Economics Financials API
  slug: tradingeconomics-financials-api
- description: The Forecasts API from Trading Economics — 4 operation(s) for forecasts.
  name: Trading Economics Forecasts API
  slug: tradingeconomics-forecasts-api
- description: The Historical API from Trading Economics — 5 operation(s) for historical.
  name: Trading Economics Historical API
  slug: tradingeconomics-historical-api
- description: The Indicators API from Trading Economics — 5 operation(s) for indicators.
  name: Trading Economics Indicators API
  slug: tradingeconomics-indicators-api
- description: The Markets API from Trading Economics — 9 operation(s) for markets.
  name: Trading Economics Markets API
  slug: tradingeconomics-markets-api
artifact_total: 17
asyncapis:
- description: 'AsyncAPI 2.6 description of the Trading Economics **WebSocket streaming surface** at `wss://stream.tradingeconomics.com/`. Unlike many data providers whose "streaming" is HTTP polling or SSE, Trading '
  name: Trading Economics Streaming API (WebSocket)
  slug: tradingeconomics-asyncapi
collections:
- collection_type: open
  name: Trading Economics API
  slug: open-tradingeconomics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tradingeconomics-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tradingeconomics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradingeconomics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tradingeconomics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tradingeconomics.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tradingeconomics.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradingeconomics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tradingeconomics
- group: commercial
  title: ''
  type: Pricing
  url: https://tradingeconomics.com/api/pricing.aspx
- group: commercial
  title: ''
  type: Plans
  url: plans/tradingeconomics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tradingeconomics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tradingeconomics-finops.yml
created: '2026-07-11'
description: Trading Economics provides economic data for 196 countries - more than 20 million time series covering economic indicators like interest rates, inflation, GDP, and unemployment - alongside an economic calendar, proprietary macro forecasts, historical data, and live market quotes, all delivered through a single REST API and a WebSocket streaming service.
finops:
- name: Tradingeconomics Finops
  service_category: Analytics
  slug: tradingeconomics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tradingeconomics.png
layout: provider
modified: '2026-07-11'
name: Trading Economics
nav: Providers
network: true
overview: 'Trading Economics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Streaming API, Economic Calendar API, Financials API, and 4 more. Tagged areas include Economic Indicators, Interest Rates, Macroeconomics, Financial Data, and Economic Calendar.


  The Trading Economics catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Trading Economics'' developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Tradingeconomics Plans Pricing
  plan_count: 4
  slug: tradingeconomics-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 5
  name: Tradingeconomics Rate Limits
  slug: tradingeconomics-rate-limits
rules:
- name: Trading Economics API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: tradingeconomics-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Tradingeconomics Authentication
  slug: tradingeconomics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Tradingeconomics Domain Security
  slug: tradingeconomics-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tradingeconomics Vulnerability Disclosure
  slug: tradingeconomics-vulnerability-disclosure
  summary_line: disclosure policy published
slug: tradingeconomics
tags:
- Economic Indicators
- Interest Rates
- Macroeconomics
- Financial Data
- Economic Calendar
- Forecasts
- Markets
website: https://tradingeconomics.com
---
