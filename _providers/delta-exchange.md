---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Delta Exchange Agentic Access
  operation_count: 50
  slug: delta-exchange-agentic-access
  summary_line: 50 operations · 20 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'Official Delta Exchange MCP server (Python, published on PyPI as delta-exchange-mcp and run locally with uvx) exposing market data, account and trading tools over the Delta Exchange India API; market '
  name: Delta Exchange MCP Server
  slug: delta-exchange-mcp
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Account level settings
  name: Delta Exchange Account API
  slug: delta-exchange-account-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get Asset List
  name: Delta Exchange Assets API
  slug: delta-exchange-assets-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: The Heartbeat Management API from Delta Exchange — 2 operation(s) for heartbeat management.
  name: Delta Exchange Heartbeat Management API
  slug: delta-exchange-heartbeat-management-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: The Historical OHLC Candles/Sparklines API from Delta Exchange — 2 operation(s) for historical ohlc candles/sparklines.
  name: Delta Exchange Historical OHLC Candles/Sparklines API
  slug: delta-exchange-historical-ohlc-candles-sparklines-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get Indices List
  name: Delta Exchange Indices API
  slug: delta-exchange-indices-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Market maker protection
  name: Delta Exchange MMP API
  slug: delta-exchange-mmp-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: L2Orderbook
  name: Delta Exchange Orderbook API
  slug: delta-exchange-orderbook-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Placing Orders, Cancelling Orders, Placing batch orders, Cancelling batch orders, Get Open orders, Change Orders Leverage. Rate limits have been introduced recently that allows only set number of oper
  name: Delta Exchange Orders API
  slug: delta-exchange-orders-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get Open positions, Change Position Margin, Close Position, Close All Position
  name: Delta Exchange Positions API
  slug: delta-exchange-positions-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get Product List
  name: Delta Exchange Products API
  slug: delta-exchange-products-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: The Settlement Prices API from Delta Exchange — 1 operation(s) for settlement prices.
  name: Delta Exchange Settlement Prices API
  slug: delta-exchange-settlement-prices-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get Volume Stats
  name: Delta Exchange Stats API
  slug: delta-exchange-stats-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get Orders History, Get Fill History
  name: Delta Exchange Trade History API
  slug: delta-exchange-tradehistory-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get Trades of a contract
  name: Delta Exchange Trades API
  slug: delta-exchange-trades-api
- baseURL: https://api.india.delta.exchange/v2
  baseurl_source: declared
  description: Get balances, Get transaction history
  name: Delta Exchange Wallet API
  slug: delta-exchange-wallet-api
artifact_total: 23
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/well-known/delta-exchange-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delta-exchange-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/agentic-access/delta-exchange-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/delta-exchange-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/rate-limits/delta-exchange-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delta-exchange-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/rules/delta-exchange-rules.yml
  title: ''
  type: Spectral
  url: rules/delta-exchange-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/vocabulary/delta-exchange-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/delta-exchange-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/data-model/delta-exchange-data-model.yml
  title: ''
  type: DataModel
  url: data-model/delta-exchange-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/conventions/delta-exchange-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delta-exchange-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/sandbox/delta-exchange-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/delta-exchange-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/security/delta-exchange-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/delta-exchange-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/security/delta-exchange-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/delta-exchange-vulnerability-disclosure.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/lifecycle/delta-exchange-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/delta-exchange-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.delta.exchange/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/lifecycle/delta-exchange-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/delta-exchange-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/errors/delta-exchange-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/delta-exchange-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/conformance/delta-exchange-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delta-exchange-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/llms/delta-exchange-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delta-exchange-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/mcp/delta-exchange-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/delta-exchange-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/mcp/delta-exchange-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/delta-exchange-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/well-known/delta-exchange-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/delta-exchange-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/hosts/delta-exchange-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delta-exchange-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/integrations/delta-exchange-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/delta-exchange-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/vendors/delta-exchange-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delta-exchange-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/packages/delta-exchange-packages.yml
  title: ''
  type: SDKs
  url: packages/delta-exchange-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/packages/delta-exchange-packages.yml
  title: ''
  type: Packages
  url: packages/delta-exchange-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/authentication/delta-exchange-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delta-exchange-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/delta-exchange/refs/heads/main/security/delta-exchange-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delta-exchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.delta.exchange
- group: docs
  title: ''
  type: Documentation
  url: https://docs.delta.exchange/
- group: company
  title: ''
  type: Blog
  url: https://www.delta.exchange/blog
- group: start
  title: ''
  type: Login
  url: https://www.delta.exchange/app/login
- group: company
  title: ''
  type: Newsroom
  url: https://www.delta.exchange/press
- group: operate
  title: ''
  type: Support
  url: https://www.delta.exchange/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.delta.exchange/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.delta.exchange/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/delta-exchange
- group: commercial
  title: ''
  type: Pricing
  url: https://www.delta.exchange/fees
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.delta.exchange/algo/delta-exchange-apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/delta-exchange/
- group: other
  title: ''
  type: X
  url: https://x.com/Delta_Exchange
created: '2026-10-13'
description: Delta Exchange is a derivatives-focused crypto exchange; Delta Exchange India (operated by Excelium Technologies Private Limited, FIU-registered) offers INR-settled perpetual futures, BTC and ETH call and put options and spot markets. It publishes a Swagger 2.0 REST API v2 (api.india.delta.exchange), WebSocket market and account feeds, a demo/testnet environment, official Python and Node REST clients, and an official local MCP server (delta-exchange-mcp on PyPI).
image: https://static.delta.exchange/seo/india/delta_twitter_og_img.jpg
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 41 tools listed.
  name: Delta Exchange MCP Server
  slug: delta-exchange-mcp
modified: '2026-10-13'
name: Delta Exchange
nav: Providers
network: true
overview: 'Delta Exchange publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Assets API, Heartbeat Management API, and 13 more. Tagged areas include Company, Cryptocurrency, Crypto Exchanges, Derivatives, and Trading.


  The Delta Exchange catalog on APIs.io includes 1 Spectral governance ruleset.


  Delta Exchange''s developer surface includes sandbox, authentication, documentation, engineering blog, support, pricing, and 34 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 4
  name: Delta Exchange Rate Limits
  slug: delta-exchange-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Delta Exchange API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: delta-exchange-rules
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 45.3
    developer_ergonomics: 54.2
    discoverability: 73.3
    operational_transparency: 71.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Delta Exchange Authentication
  slug: delta-exchange-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Delta Exchange Domain Security
  slug: delta-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Delta Exchange Vulnerability Disclosure
  slug: delta-exchange-vulnerability-disclosure
  summary_line: no policy recorded
slug: delta-exchange
tags:
- Company
- Cryptocurrency
- Crypto Exchanges
- Derivatives
- Trading
- Options
- Futures
- Market Data
website: https://www.delta.exchange
---
