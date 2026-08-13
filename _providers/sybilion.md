---
access_model:
  confidence: medium
  label: Self-serve signup, prices unpublished
  onboarding: self-serve
  pricing: unknown
  public: true
  source:
  - https://sybilion.dev/docs/tiers
  - https://sybilion.dev/signup
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 73.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sybilion Agentic Access
  operation_count: 11
  slug: sybilion-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 2
apis:
- description: REST API exposing asynchronous forecasts with quantile bands and driver attribution, ranked external drivers, alerts, the region/category catalog, account balance and tier, and paginated billing histo
  name: Sybilion Operational API
  slug: sybilion-operational-api
- description: Hosted Streamable-HTTP MCP server providing agent-native tools for forecasts (submit_forecast, get_forecast, get_forecast_chart, get_forecast_artifact), alerts (get_alerts) and catalog discovery (list
  name: Sybilion MCP Server
  slug: sybilion-mcp-server
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sybilion.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://sybilion.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sybilion.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://sybilion.dev/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://sybilion.dev/docs/community
- group: operate
  title: ''
  type: Community
  url: https://join.slack.com/t/sybilioncommunity/shared_invite/zt-3y6vx56nk-WJu35eLxkyFQr~Yfko6RjQ
- group: company
  title: ''
  type: Blog
  url: https://www.sybilion.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sybilion-AI
- group: start
  title: ''
  type: SignUp
  url: https://sybilion.dev/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sybilion.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.sybilion.com/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.sybilion.com/case-studies
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sybilion-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sybilion-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sybilion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sybilion-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sybilion-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sybilion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sybilion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sybilion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sybilion-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sybilion-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sybilion-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/sybilion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sybilion-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sybilion-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sybilion-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sybilion-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sybilion-operational-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/sybilion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sybilion-rate-limits.yml
created: '2026-07-05'
description: 'Sybilion is a decision layer for industrial companies, providing economic and causal forecasting that connects external market dynamics to internal exposure for procurement, trading and risk teams. It forecasts monthly business time series up to twelve months ahead with 80% and 90% quantile bands, ranks the external macroeconomic drivers that move a series with Granger lag relationships and feature-importance scores, backtests against the last twelve months, and raises alerts on the market movements turning relevant to a customer''s exposure right now. The same causal model is reachable two ways: an anonymously-specified OpenAPI 3.0.3 REST API at api.sybilion.dev using Bearer API keys, and a hosted OAuth MCP server at mcp.sybilion.dev that ChatGPT, Claude and the TradingView Remix extension connect to directly. Billing is a prepaid EUR-cent balance with expiring credit tranches and pre-flight holds. Official Python, Go, TypeScript and R SDKs are published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sybilion.png
layout: provider
mcp_servers:
- description: ''
  name: sybilion-mcp.yml
  slug: sybilion-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-11'
name: Sybilion
nav: Providers
network: true
overview: 'Sybilion publishes 1 API on the [APIs.io](https://apis.io/) network: Operational API. Tagged areas include Industrial market intelligence, Commodity price forecasting, Economic forecasting, Time-series forecasting, and Procurement.


  Sybilion''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Sybilion Plans Pricing
  plan_count: 5
  slug: sybilion-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 3
  name: Sybilion Rate Limits
  slug: sybilion-rate-limits
scopes:
- name: Sybilion Scopes
  scope_count: 4
  slug: sybilion-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 54.5
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 50.7
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 54.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Sybilion Authentication
  slug: sybilion-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Sybilion Domain Security
  slug: sybilion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sybilion
tags:
- Industrial market intelligence
- Commodity price forecasting
- Economic forecasting
- Time-series forecasting
- Procurement
- Supply-chain risk
- Trading analytics
- AI decision support
- MCP
- Agent-native
- Causal inference
- Anomaly detection
website: https://www.sybilion.com/
---
