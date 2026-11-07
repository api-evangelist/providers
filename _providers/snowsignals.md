---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.9
  scored_at: '2026-11-06'
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
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/snowsignals/capabilities/snowsignals-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/snowsignals-capability-edges.yml
- group: company
  title: ''
  type: Blog
  url: https://snowsignals.io/blog/
- group: other
  href: https://artifacts.apis.io/snowsignals/overlays/snowsignals-daas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snowsignals-daas-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://snowsignals.io/mcp
- group: other
  href: https://artifacts.apis.io/snowsignals/overlays/snowsignals-x402-overlay.yaml
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
  href: https://artifacts.apis.io/snowsignals/llms/snowsignals-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snowsignals-llms.txt
- group: agent
  href: https://artifacts.apis.io/snowsignals/well-known/snowsignals-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snowsignals-well-known.yml
- group: agent
  href: https://artifacts.apis.io/snowsignals/mcp/snowsignals-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snowsignals-mcp.yml
- group: build
  href: https://artifacts.apis.io/snowsignals/mcp/snowsignals-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/snowsignals-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/snowsignals/authentication/snowsignals-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snowsignals-authentication.yml
- group: auth
  href: https://artifacts.apis.io/snowsignals/scopes/snowsignals-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/snowsignals-scopes.yml
- group: design
  href: https://artifacts.apis.io/snowsignals/conventions/snowsignals-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snowsignals-conventions.yml
- group: design
  href: https://artifacts.apis.io/snowsignals/errors/snowsignals-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snowsignals-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snowsignals/conformance/snowsignals-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snowsignals-conformance.yml
- group: design
  href: https://artifacts.apis.io/snowsignals/lifecycle/snowsignals-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snowsignals-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/snowsignals/plans/snowsignals-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snowsignals-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/snowsignals/rate-limits/snowsignals-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snowsignals-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/snowsignals/data-model/snowsignals-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snowsignals-data-model.yml
- group: agent
  href: https://artifacts.apis.io/snowsignals/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/snowsignals/security/snowsignals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snowsignals-domain-security.yml
- group: build
  href: https://artifacts.apis.io/snowsignals/packages/snowsignals-packages.yml
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
  slug: mcp
modified: '2026-10-06'
name: SnowSignals
nav: Providers
network: true
overview: 'SnowSignals publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Notifications API, Phase API, Phases API, and 2 more. Tagged areas include Cryptocurrency, Market Data, Bitcoin, Analytics, and market-phase.


  The SnowSignals catalog on APIs.io includes 1 Spectral governance ruleset.


  SnowSignals'' developer surface includes engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Snowsignals Plans Pricing
  plan_count: 2
  slug: snowsignals-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Snowsignals Rate Limits
  slug: snowsignals-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: SnowSignals API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: snowsignals-rules
scopes:
- name: Snowsignals Scopes
  scope_count: 1
  slug: snowsignals-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 46.5
    catalog_earned_first_party: 8.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 48.8
    developer_ergonomics: 25.6
    discoverability: 70.0
    operational_transparency: 5.3
  previous_composite: 33.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 60.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/snowsignals/snowsignals-2026-10-11T130027.png
security:
- kind: authentication
  name: Snowsignals Authentication
  slug: snowsignals-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Snowsignals Domain Security
  slug: snowsignals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: snowsignals-manage-prepaid-balance
  slug: snowsignals-manage-prepaid-balance
- name: snowsignals-read-market-phase
  slug: snowsignals-read-market-phase
slug: snowsignals
tags:
- Cryptocurrency
- Market Data
- Bitcoin
- Analytics
- market-phase
- regime
- trendvane
- DaaS
- MCP
- Agent-Native
- Financial Data
- x402
website: https://snowsignals.io
---
