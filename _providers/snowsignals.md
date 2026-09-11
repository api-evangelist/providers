---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-09-10'
api_count: 2
apis:
- baseURL: https://snowsignals.io/v1
  baseurl_source: declared
  description: TrendVane daas API — metered, prepaid market-phase reads per currency and timeframe (boundary = settled last closed bar, updates = intra-bar), plus free unmetered metadata (phases, pricing model, serv
  name: SnowSignals API
  slug: snowsignals-api
- baseURL: https://pay.snowsignals.io
  baseurl_source: declared
  description: 'Pay-per-call retail gateway for the same TrendVane phase reads over the x402 payment protocol (v2) — no account, API key, or OAuth anywhere: a metered GET answers 402 with a signed quote (exact amount'
  name: SnowSignals x402 Gateway
  slug: snowsignals-x402-gateway
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://snowsignals.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snowsignals.io/terms
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/snowkidind/snowsignals-mcp
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snowsignals-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/snowsignals-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/snowsignals-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/snowsignals-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snowsignals-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/snowsignals-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/snowsignals-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/snowsignals-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/snowsignals-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/snowsignals-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/snowsignals-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/snowsignals-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/snowsignals-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snowsignals-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/snowsignals-packages.yml
created: '2026-09-10'
description: 'SnowSignals is a crypto market-data platform (data-as-a-service) whose TrendVane product serves multi-timeframe market-phase (regime) classifications — market state, not trade signals — for BTC, ETH, GRAM, SOL and TRX over a metered REST API and a hosted, OAuth-gated MCP server. Pricing is prepaid in stablecoin and served in-band by a free, no-auth discovery call, so an agent can compute the exact cost of a read before spending; a free phase-resolution model (successor-transition probabilities, continuation rates, MFE/MAE) supports interpreting each reading. The platform is deliberately agent-native: first-party llms.txt, self-hosted APIs.json, RFC 8414/9728 OAuth discovery, and an official MCP registry listing. A first-party x402 gateway (pay.snowsignals.io, live 2026-09-10) additionally sells the same phase reads pay-per-call in USDC on Base with no account at all.'
image: https://snowsignals.io/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: SnowSignals
  slug: snowsignals
- description: ''
  name: SnowSignals MCP Server
  slug: snowsignals-mcp-server
modified: '2026-09-10'
name: SnowSignals
nav: Providers
network: true
overview: 'SnowSignals publishes 2 APIs on the [APIs.io](https://apis.io/) network, including x402 Gateway, and 1 more. Tagged areas include crypto, market-data, bitcoin, analytics, and market-phase.


  SnowSignals'' developer surface includes authentication and 18 more developer resources.'
plans:
- name: Snowsignals Plans Pricing
  plan_count: 2
  slug: snowsignals-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Snowsignals Rate Limits
  slug: snowsignals-rate-limits
scopes:
- name: Snowsignals Scopes
  scope_count: 1
  slug: snowsignals-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.0
    catalog_earned_first_party: 8.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 47.6
    developer_ergonomics: 23.2
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
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
    score: 55.0
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Snowsignals Authentication
  slug: snowsignals-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Snowsignals Domain Security
  slug: snowsignals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snowsignals
tags:
- crypto
- market-data
- bitcoin
- analytics
- market-phase
- regime
- trendvane
- daas
- mcp
- agent-native
- financial-data
- x402
website: https://snowsignals.io
---
