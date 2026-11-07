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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sybilion Agentic Access
  operation_count: 11
  slug: sybilion-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 1
apis:
- description: Hosted Streamable-HTTP MCP server providing agent-native tools for forecasts (submit_forecast, get_forecast, get_forecast_chart, get_forecast_artifact), alerts (get_alerts) and catalog discovery (list
  name: Sybilion MCP Server
  slug: sybilion-mcp-server
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Alerts API from Sybilion — 1 operation(s) for alerts.
  name: Sybilion Alerts API
  slug: sybilion-alerts-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Categories API from Sybilion — 1 operation(s) for categories.
  name: Sybilion Categories API
  slug: sybilion-categories-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Drivers API from Sybilion — 1 operation(s) for drivers.
  name: Sybilion Drivers API
  slug: sybilion-drivers-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Forecasts API from Sybilion — 3 operation(s) for forecasts.
  name: Sybilion Forecasts API
  slug: sybilion-forecasts-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Health API from Sybilion — 1 operation(s) for health.
  name: Sybilion Health API
  slug: sybilion-health-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Jobs API from Sybilion — 1 operation(s) for jobs.
  name: Sybilion Jobs API
  slug: sybilion-jobs-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Me API from Sybilion — 1 operation(s) for me.
  name: Sybilion Me API
  slug: sybilion-me-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Regions API from Sybilion — 1 operation(s) for regions.
  name: Sybilion Regions API
  slug: sybilion-regions-api
- baseURL: https://api.sybilion.dev
  baseurl_source: declared
  description: The Usage API from Sybilion — 1 operation(s) for usage.
  name: Sybilion Usage API
  slug: sybilion-usage-api
artifact_total: 23
collections:
- collection_type: open
  name: Sybilion API
  slug: open-sybilion-operational-api
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://sybilion.dev/docs/tiers
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
  href: https://artifacts.apis.io/sybilion/llms/sybilion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sybilion-llms.txt
- group: agent
  href: https://artifacts.apis.io/sybilion/well-known/sybilion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sybilion-well-known.yml
- group: auth
  href: https://artifacts.apis.io/sybilion/authentication/sybilion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sybilion-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sybilion/scopes/sybilion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sybilion-scopes.yml
- group: design
  href: https://artifacts.apis.io/sybilion/conventions/sybilion-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sybilion-conventions.yml
- group: design
  href: https://artifacts.apis.io/sybilion/conventions/sybilion-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sybilion-conventions.yml
- group: design
  href: https://artifacts.apis.io/sybilion/errors/sybilion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sybilion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sybilion/lifecycle/sybilion-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sybilion-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sybilion/conformance/sybilion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sybilion-conformance.yml
- group: auth
  href: https://artifacts.apis.io/sybilion/security/sybilion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sybilion-domain-security.yml
- group: design
  href: https://artifacts.apis.io/sybilion/data-model/sybilion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sybilion-data-model.yml
- group: build
  href: https://artifacts.apis.io/sybilion/packages/sybilion-packages.yml
  title: ''
  type: Packages
  url: packages/sybilion-packages.yml
- group: build
  href: https://artifacts.apis.io/sybilion/packages/sybilion-packages.yml
  title: ''
  type: SDKs
  url: packages/sybilion-packages.yml
- group: agent
  href: https://artifacts.apis.io/sybilion/mcp/sybilion-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sybilion-mcp.yml
- group: build
  href: https://artifacts.apis.io/sybilion/mcp/sybilion-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sybilion-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/sybilion/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sybilion/agentic-access/sybilion-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sybilion-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/sybilion/overlays/sybilion-operational-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sybilion-operational-api-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/sybilion/plans/sybilion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sybilion-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sybilion/rate-limits/sybilion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sybilion-rate-limits.yml
created: '2026-07-05'
description: 'Sybilion is a decision layer for industrial companies, providing economic and causal forecasting that connects external market dynamics to internal exposure for procurement, trading and risk teams. It forecasts monthly business time series up to twelve months ahead with 80% and 90% quantile bands, ranks the external macroeconomic drivers that move a series with Granger lag relationships and feature-importance scores, backtests against the last twelve months, and raises alerts on the market movements turning relevant to a customer''s exposure right now. The same causal model is reachable two ways: an anonymously-specified OpenAPI 3.0.3 REST API at api.sybilion.dev using Bearer API keys, and a hosted OAuth MCP server at mcp.sybilion.dev that ChatGPT, Claude and the TradingView Remix extension connect to directly. Billing is a prepaid EUR-cent balance with expiring credit tranches and pre-flight holds. Official Python, Go, TypeScript and R SDKs are published.'
finops:
- has_sources: true
  method: derived
  name: Sybilion Finops
  primary_unit: ''
  service_category: ''
  slug: sybilion-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sybilion.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.sybilion.dev over HTTP; 7 tools listed.
  name: Sybilion MCP Server
  slug: sybilion
modified: '2026-08-11'
name: Sybilion
nav: Providers
network: true
overview: 'Sybilion publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Categories API, Drivers API, and 7 more. Tagged areas include Industrial market intelligence, Commodity price forecasting, Economic Forecasting, Time-series forecasting, and Procurement.


  The Sybilion catalog on APIs.io includes 1 Spectral governance ruleset.


  Sybilion''s developer surface includes pricing, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 26 more developer resources.'
plans:
- name: Sybilion Plans Pricing
  plan_count: 5
  slug: sybilion-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Sybilion Rate Limits
  slug: sybilion-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Sybilion API Rules
  rule_count: 55
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 5
  slug: sybilion-rules
scopes:
- name: Sybilion Scopes
  scope_count: 4
  slug: sybilion-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 53.2
    developer_ergonomics: 56.5
    discoverability: 68.3
    operational_transparency: 34.2
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sybilion/sybilion-2026-08-17T082216.png
security:
- kind: authentication
  name: Sybilion Authentication
  slug: sybilion-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Sybilion Domain Security
  slug: sybilion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Use the Sybilion MCP connector from an agent
  slug: sybilion-connect-mcp-agent
- name: Forecast a monthly series and explain what drove it
  slug: sybilion-forecast-and-explain
- name: Rank external drivers for a series without double-billing
  slug: sybilion-rank-drivers-safely
slug: sybilion
tags:
- Industrial market intelligence
- Commodity price forecasting
- Economic Forecasting
- Time-series forecasting
- Procurement
- Supply Chain Risk
- Trading analytics
- AI decision support
- MCP
- Agent-Native
- Causal Inference
- Anomaly Detection
website: https://www.sybilion.com/
---
