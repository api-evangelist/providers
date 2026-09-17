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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-09-16'
api_count: 2
apis:
- baseURL: https://snowsignals.io/v1
  baseurl_source: declared
  description: The Notifications API from SnowSignals — 1 operation(s) for notifications.
  name: SnowSignals Notifications API
  slug: snowsignals-notifications-api
- baseURL: https://snowsignals.io/v1
  baseurl_source: declared
  description: The Phase API from SnowSignals — 6 operation(s) for phase.
  name: SnowSignals Phase API
  slug: snowsignals-phase-api
- baseURL: https://snowsignals.io/v1
  baseurl_source: declared
  description: The Phases API from SnowSignals — 2 operation(s) for phases.
  name: SnowSignals Phases API
  slug: snowsignals-phases-api
- baseURL: https://snowsignals.io/v1
  baseurl_source: declared
  description: The Time API from SnowSignals — 1 operation(s) for time.
  name: SnowSignals Time API
  slug: snowsignals-time-api
- baseURL: https://snowsignals.io/v1
  baseurl_source: declared
  description: The User API from SnowSignals — 3 operation(s) for user.
  name: SnowSignals User API
  slug: snowsignals-user-api
artifact_total: 12
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/overlays/snowsignals-daas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snowsignals-daas-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://snowsignals.io/mcp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/overlays/snowsignals-x402-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snowsignals-x402-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/llms/snowsignals-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snowsignals-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/well-known/snowsignals-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snowsignals-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/mcp/snowsignals-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snowsignals-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/mcp/snowsignals-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/snowsignals-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/authentication/snowsignals-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snowsignals-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/scopes/snowsignals-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/snowsignals-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/conventions/snowsignals-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snowsignals-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/errors/snowsignals-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snowsignals-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/conformance/snowsignals-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snowsignals-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/lifecycle/snowsignals-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snowsignals-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/plans/snowsignals-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snowsignals-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/rate-limits/snowsignals-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snowsignals-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/data-model/snowsignals-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snowsignals-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/security/snowsignals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snowsignals-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/snowsignals/refs/heads/main/packages/snowsignals-packages.yml
  title: ''
  type: Packages
  url: packages/snowsignals-packages.yml
created: '2026-09-10'
description: 'SnowSignals is a crypto market-data platform (data-as-a-service) whose TrendVane product serves multi-timeframe market-phase (regime) classifications — market state, not trade signals — for BTC, ETH, GRAM, SOL and TRX over a metered REST API and a hosted, OAuth-gated MCP server. Pricing is prepaid in stablecoin and served in-band by a free, no-auth discovery call, so an agent can compute the exact cost of a read before spending; a free phase-resolution model (successor-transition probabilities, continuation rates, MFE/MAE) supports interpreting each reading. The platform is deliberately agent-native: first-party llms.txt, self-hosted APIs.json, RFC 8414/9728 OAuth discovery, and an official MCP registry listing. A first-party x402 gateway (pay.snowsignals.io, live 2026-09-10) additionally sells the same phase reads pay-per-call in USDC on Base with no account at all.'
image: https://snowsignals.io/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: SnowSignals MCP Server
  slug: snowsignals-mcp-server
- description: ''
  name: SnowSignals
  slug: snowsignals
modified: '2026-09-10'
name: SnowSignals
nav: Providers
network: true
overview: 'SnowSignals publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Notifications API, Phase API, Phases API, and 2 more. Tagged areas include Crypto, Market Data, Bitcoin, Analytics, and market-phase.


  SnowSignals'' developer surface includes authentication and 21 more developer resources.'
plans:
- name: Snowsignals Plans Pricing
  plan_count: 2
  slug: snowsignals-plans-pricing
random_paper: 20
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
  composite: 33.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.0
    catalog_earned_first_party: 8.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 50.9
    developer_ergonomics: 23.2
    discoverability: 70.4
    operational_transparency: 5.3
  previous_composite: 32.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
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
- Crypto
- Market Data
- Bitcoin
- Analytics
- market-phase
- regime
- trendvane
- DaaS
- MCP
- agent-native
- Financial Data
- x402
website: https://snowsignals.io
---
