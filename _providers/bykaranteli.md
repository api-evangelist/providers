---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bykaranteli Agentic Access
  operation_count: 14
  slug: bykaranteli-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- description: The X402 API from ByKaranteli — 14 operation(s) for x402.
  name: ByKaranteli X402 API
  slug: bykaranteli-x402-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bykaranteli-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bykaranteli-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bykaranteli.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://bykaranteli.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://bykaranteli.com/guide
- group: operate
  title: ''
  type: Support
  url: https://t.me/bykaranteli_com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bykarantelicom
- group: commercial
  title: ''
  type: Pricing
  url: https://bykaranteli.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://bykaranteli.com/register
- group: start
  title: ''
  type: Login
  url: https://bykaranteli.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://bykaranteli.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bykaranteli-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bykaranteli-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bykaranteli-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bykaranteli-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bykaranteli-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bykaranteli-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bykaranteli-plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bykaranteli-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/bykaranteli-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bykaranteli-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bykaranteli-vocabulary.yml
- group: design
  title: ''
  type: Components
  url: components/bykaranteli-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: A crypto-derivatives market-structure data service built on a deterministic crypto-futures signal engine. Its free, no-key public REST API surfaces funding rates/arbitrage, open interest, liquidation maps, options (Deribit), ETF flows, order-flow toxicity (VPIN), Coinbase premium, CFTC COT positioning, and Fear & Greed / BTC-dominance indices, plus live signal performance and per-symbol/strategy leaderboards. It also offers a hosted MCP server, x402 agent-payment endpoints, and CC0 datasets.
examples:
- key_count: 6
  name: Bykaranteli Public Indices
  slug: bykaranteli-public-indices
- key_count: 3
  name: Bykaranteli Public Pressure
  slug: bykaranteli-public-pressure
- key_count: 8
  name: Bykaranteli Public Recent
  slug: bykaranteli-public-recent
- key_count: 4
  name: Bykaranteli V1 Health
  slug: bykaranteli-v1-health
- key_count: 10
  name: Bykaranteli V1 Leaderboard
  slug: bykaranteli-v1-leaderboard
- key_count: 5
  name: Bykaranteli X402 Payment Required
  slug: bykaranteli-x402-payment-required
finops:
- name: Bykaranteli Finops
  service_category: ''
  slug: bykaranteli-finops
image: https://bykaranteli.com/brand/icon-192.png
layout: provider
modified: '2026-08-09'
name: ByKaranteli
nav: Providers
network: true
overview: 'ByKaranteli publishes 1 API on the [APIs.io](https://apis.io/) network: X402 API. Tagged areas include Cryptocurrency, Crypto Derivatives, Market Data, Funding Rates, and Open Interest.


  ByKaranteli''s developer surface includes API reference, getting-started guide, support, pricing, signup flow, changelog, authentication, and 17 more developer resources.'
plans:
- name: Bykaranteli Plans
  plan_count: 5
  slug: bykaranteli-plans
random_paper: 14
rate_limits:
- limit_count: 2
  name: Bykaranteli Rate Limits
  slug: bykaranteli-rate-limits
score:
  band: developing
  composite: 51.7
  facets:
    commercial_clarity: 63.2
    contract_quality: 47.3
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 31.3
    operational_transparency: 57.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: authentication
  name: Bykaranteli Authentication
  slug: bykaranteli-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Bykaranteli Domain Security
  slug: bykaranteli-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bykaranteli
tags:
- Cryptocurrency
- Crypto Derivatives
- Market Data
- Funding Rates
- Open Interest
- Liquidations
- Options
- ETF Flows
- Financial Data
- MCP
- x402
- Agents
website: https://bykaranteli.com/developers
---
