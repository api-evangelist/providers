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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bykaranteli Agentic Access
  operation_count: 14
  slug: bykaranteli-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://bykaranteli.com
  baseurl_source: declared
  description: Per-call priced history and depth endpoints, settled in USDC over the x402 protocol on Solana and Base mainnet through the Coinbase CDP facilitator. 13 priced endpoints plus the free catalog at /api/x
  name: ByKaranteli X402 API
  slug: bykaranteli-x402-api
- description: 'The free, no-key public REST surface — 10 endpoints under /api/v1/public/ described by the provider''s own self-describing manifest, plus the /api/public/ index endpoints. Verified 2026-08-11: unauthen'
  name: ByKaranteli Public API
  slug: bykaranteli-public-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ByKaranteli crypto derivatives data X402 API
  slug: open-bykaranteli-x402-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bykaranteli-mcp.yml
- group: docs
  title: ''
  type: Documentation
  url: https://bykaranteli.com/developers
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
mcp_servers:
- description: ''
  name: ByKaranteli MCP Server
  slug: bykaranteli-mcp-server
modified: '2026-08-09'
name: ByKaranteli
nav: Providers
network: true
overview: 'ByKaranteli publishes 1 API on the [APIs.io](https://apis.io/) network: X402 API. Tagged areas include Cryptocurrency, Crypto Derivatives, Market Data, Funding Rates, and Open Interest.


  ByKaranteli''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 19 more developer resources.'
plans:
- name: Bykaranteli Plans
  plan_count: 5
  slug: bykaranteli-plans
random_paper: 19
rate_limits:
- limit_count: 2
  name: Bykaranteli Rate Limits
  slug: bykaranteli-rate-limits
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 24
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 51.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 55.3
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bykaranteli/refs/heads/main/screenshots/bykaranteli-2026-08-17T080800.png
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
