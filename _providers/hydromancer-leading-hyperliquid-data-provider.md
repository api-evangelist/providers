---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-09-21'
api_count: 2
apis:
- description: Hyperliquid data REST API using a single POST /info operation dispatcher (type field selects the operation). Bearer-token authentication. Provides user state, positions, asset data, order data, histor
  name: Hydromancer REST API
  slug: hydromancer-rest-api
- description: Real-time WebSocket streams for Hypercore events, orderbooks (L2/L4), trades, and account updates. API key passed as a query parameter.
  name: Hydromancer WebSocket API
  slug: hydromancer-websocket-api
artifact_total: 8
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/rate-limits/hydromancer-leading-hyperliquid-data-provider-websocket-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hydromancer-leading-hyperliquid-data-provider-websocket-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/mcp/hydromancer-leading-hyperliquid-data-provider-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hydromancer-leading-hyperliquid-data-provider-mcp.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/rate-limits/hydromancer-leading-hyperliquid-data-provider-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hydromancer-leading-hyperliquid-data-provider-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/plans/hydromancer-leading-hyperliquid-data-provider-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hydromancer-leading-hyperliquid-data-provider-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/changelog/hydromancer-leading-hyperliquid-data-provider-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hydromancer-leading-hyperliquid-data-provider-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/conventions/hydromancer-leading-hyperliquid-data-provider-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hydromancer-leading-hyperliquid-data-provider-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/sandbox/hydromancer-leading-hyperliquid-data-provider-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hydromancer-leading-hyperliquid-data-provider-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/authentication/hydromancer-leading-hyperliquid-data-provider-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hydromancer-leading-hyperliquid-data-provider-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/lifecycle/hydromancer-leading-hyperliquid-data-provider-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hydromancer-leading-hyperliquid-data-provider-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/lifecycle/hydromancer-leading-hyperliquid-data-provider-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hydromancer-leading-hyperliquid-data-provider-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/errors/hydromancer-leading-hyperliquid-data-provider-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hydromancer-leading-hyperliquid-data-provider-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/llms/hydromancer-leading-hyperliquid-data-provider-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hydromancer-leading-hyperliquid-data-provider-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/well-known/hydromancer-leading-hyperliquid-data-provider-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hydromancer-leading-hyperliquid-data-provider-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hydromancer-leading-hyperliquid-data-provider/refs/heads/main/security/hydromancer-leading-hyperliquid-data-provider-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hydromancer-leading-hyperliquid-data-provider-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hydromancer.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hydromancer.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hydromancer.xyz/readme/rest-api
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.hydromancer.xyz/readme/pricing
- group: company
  title: ''
  type: Blog
  url: https://hydromancer.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://hydromancer.xyz/contact
created: '2026-09-21'
description: Hydromancer is data infrastructure for the Hyperliquid ecosystem, offering real-time REST and WebSocket APIs, L2/L4 orderbook streaming, liquidations feeds, oracle and perp/spot price data, HIP-3/HIP-4 market events, and granular historical datasets (via its Reservoir exports). The REST API is a single POST /info dispatcher with Bearer-token authentication and token-metered subscription pricing; the WebSocket API delivers low-latency streams with tiered connection and subscription limits. Documentation is agent-native (llms.txt plus Markdown twins of every page). Onboarding is manual, with a discretionary free tier for public-goods and early-stage teams.
layout: provider
mcp_servers:
- description: ''
  name: Hydromancer MCP Server
  slug: hydromancer-mcp-server
modified: '2026-09-21'
name: Hydromancer
nav: Providers
network: true
overview: 'Hydromancer publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hyperliquid, Blockchain, Web3, DeFi, and Crypto trading data.


  Hydromancer''s developer surface includes changelog, sandbox, authentication, documentation, API reference, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Hydromancer Leading Hyperliquid Data Provider Plans Pricing
  plan_count: 4
  slug: hydromancer-leading-hyperliquid-data-provider-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Hydromancer Leading Hyperliquid Data Provider Rate Limits
  slug: hydromancer-leading-hyperliquid-data-provider-rate-limits
- limit_count: 5
  name: Hydromancer Leading Hyperliquid Data Provider Websocket Rate Limits
  slug: hydromancer-leading-hyperliquid-data-provider-websocket-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 72.2
    operational_transparency: 55.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hydromancer Leading Hyperliquid Data Provider Authentication
  slug: hydromancer-leading-hyperliquid-data-provider-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Hydromancer Leading Hyperliquid Data Provider Domain Security
  slug: hydromancer-leading-hyperliquid-data-provider-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hydromancer-leading-hyperliquid-data-provider
tags:
- Hyperliquid
- Blockchain
- Web3
- DeFi
- Crypto trading data
- Market Data
- Real-Time
- WebSocket streaming
- Historical Data
- Orderbook data
website: https://hydromancer.xyz
---
