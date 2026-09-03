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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Current and historical market data across Hyperliquid core, Spot, HIP-3, HIP-4, and Lighter. Direct market-data requests use X-API-Key.
  name: 0xArchive REST API
  slug: 0xarchive-rest-api
- description: Real-time subscriptions for supported Hyperliquid channels and historical replay for Hyperliquid and Lighter. Clients authenticate during the handshake with a bearer API key.
  name: 0xArchive WebSocket API
  slug: 0xarchive-websocket-api
- description: Read-only market-data discovery and retrieval for MCP clients. Hosted MCP uses client-managed OAuth and requires no 0xArchive API key.
  name: 0xArchive Hosted MCP
  slug: 0xarchive-hosted-mcp
artifact_total: 12
asyncapis:
- description: ''
  name: 0Xarchive Websocket Channels
  slug: 0xarchive-websocket-channels
common:
- group: company
  title: ''
  type: Website
  url: https://0xarchive.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.0xarchive.io/
- group: other
  title: ''
  type: APICatalog
  url: https://0xarchive.io/.well-known/api-catalog
- group: start
  title: ''
  type: APIOnboarding
  url: https://0xarchive.io/.well-known/api-onboarding
- group: design
  title: ''
  type: SpectralRules
  url: https://0xarchive.io/.well-known/spectral-ruleset.yaml
- group: other
  title: ''
  type: AICatalog
  url: https://0xarchive.io/.well-known/ai-catalog.json
- group: agent
  title: ''
  type: LLMSTxt
  url: https://0xarchive.io/llms.txt
- group: other
  title: ''
  type: x402Facilitator
  url: https://0xarchive.io/facilitator
- group: commercial
  title: ''
  type: Pricing
  url: https://0xarchive.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://0xarchive.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://0xarchive.io/privacy
- group: commercial
  title: ''
  type: DataLicense
  url: https://docs.0xarchive.io/data-rights
- group: auth
  title: ''
  type: Security
  url: https://0xarchive.io/.well-known/security.txt
- group: operate
  title: ''
  type: Status
  url: https://0xarchive.io/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://0xarchive.io/changelog
- group: operate
  title: ''
  type: Support
  url: mailto:support@0xarchive.io
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/0xarchive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/0xarchive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/0xarchive-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/0xarchive-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/0xarchive-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/0xarchive-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/0xarchive-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/0xarchive-security.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/0xarchive-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/0xarchive-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/0xarchive-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/0xarchive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/0xarchive-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/0xarchive-cli.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/0xarchive-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/0xarchive-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/0xarchive-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://0xarchive.io/status
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/0xarchive-scopes.yml
- group: auth
  title: ''
  type: Security
  url: security/0xarchive-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/0xarchive-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/0xarchive-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/0xarchive-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/0xarchive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/0xarchive-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/0xarchive-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.0xarchive.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.0xarchive.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.0xarchive.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.0xarchive.io/quickstart
- group: operate
  title: ''
  type: Support
  url: https://0xarchive.io/contact
- group: company
  title: ''
  type: Blog
  url: https://0xarchive.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xArchiveIO
- group: start
  title: ''
  type: SignUp
  url: https://0xarchive.io/signup
- group: start
  title: ''
  type: Login
  url: https://0xarchive.io/login
- group: build
  title: ''
  type: Examples
  url: https://github.com/0xArchiveIO/examples
created: '2026-08-30'
description: '0xArchive is a replayable market-data archive for two decentralised perpetuals venues, Hyperliquid and Lighter, delivered as one REST API, one WebSocket API that carries both live subscriptions and historical replay on a single connection, bulk Parquet export, and a hosted MCP server. Hyperliquid coverage is split into four route families - core perpetuals, Spot, HIP-3 builder perps and HIP-4 binary outcome markets - each with its own symbol format and its own set of available data types. Beyond order books, trades, candles, funding, open interest and liquidations, the archive reconstructs order-level depth that the venues do not serve directly: L4 for the Hyperliquid families and L3 for Lighter. Access is unusually flat - every plan including Free reaches every route family, schema and served depth, and plans gate capacity and Free''s rolling 30-day history window rather than route access. An agent can buy its own 30-day Build or Pro access with an x402 USDC payment on Base
  and receive an API key on settlement, with no human signup step.'
image: https://0xarchive.io/logo-mark.svg
layout: provider
mcp_servers:
- description: 'Live MCP, gated: initialize returns 401 "Missing Authorization". Present and auth-required, not absent. Found via their own .well-known/mcp.json descriptor. Verified 2026-09-01.'
  name: 0xArchive MCP Server
  slug: 0xarchive-mcp-server
- description: Read-only market-data discovery and retrieval for MCP clients across Hyperliquid (core perps, HIP-3 builder perps, HIP-4 outcome markets, Spot) and Lighter.
  name: 0xArchive MCP
  slug: 0xarchive-mcp
modified: '2026-09-01'
name: 0xArchive
nav: Providers
network: true
overview: '0xArchive publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include market data, historical data, crypto, DeFi, and perpetuals.


  The 0xArchive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  0xArchive''s developer surface includes developer portal, pricing, status page, changelog, support, authentication, CLI, and 46 more developer resources.'
plans:
- name: 0Xarchive Plans Pricing
  plan_count: 5
  slug: 0xarchive-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: 0Xarchive Rate Limits
  slug: 0xarchive-rate-limits
scopes:
- name: 0Xarchive Scopes
  scope_count: 0
  slug: 0xarchive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 54.5
    developer_ergonomics: 85.7
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 78.9
  previous_composite: 73.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/0xarchive/refs/heads/main/screenshots/0xarchive-2026-09-02T144104.png
security:
- kind: authentication
  name: 0Xarchive Authentication
  slug: 0xarchive-authentication
  summary_line: apiKey/oauth2/siwe · 4 schemes
- kind: domain-security
  name: 0Xarchive Domain Security
  slug: 0xarchive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 0Xarchive Vulnerability Disclosure
  slug: 0xarchive-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: 0xarchive
tags:
- market data
- historical data
- crypto
- DeFi
- perpetuals
- derivatives
- order book
- Hyperliquid
- Lighter
- HIP-3
- HIP-4
- prediction markets
- WebSocket
- streaming
- historical replay
- Parquet
- bulk data
- MCP
- agent-native
- x402
- OpenAPI
- REST
website: https://0xarchive.io/
---
