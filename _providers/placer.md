---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Placer Agentic Access
  operation_count: 33
  slug: placer-agentic-access
  summary_line: 33 operations · 28 acting
api_count: 8
apis:
- description: The Account Info API from Placer — 1 operation(s) for account info.
  name: Placer Account Info API
  slug: placer-account-info-api
- description: The Loyalty Reports API from Placer — 1 operation(s) for loyalty reports.
  name: Placer Loyalty Reports API
  slug: placer-loyalty-reports-api
- description: The Manage POIs API from Placer — 6 operation(s) for manage pois.
  name: Placer Manage POIs API
  slug: placer-manage-pois-api
- description: The Ranking Reports API from Placer — 4 operation(s) for ranking reports.
  name: Placer Ranking Reports API
  slug: placer-ranking-reports-api
- description: The Retail Sales Reports API from Placer — 5 operation(s) for retail sales reports.
  name: Placer Retail Sales Reports API
  slug: placer-retail-sales-reports-api
- description: The Trade Area Reports API from Placer — 3 operation(s) for trade area reports.
  name: Placer Trade Area Reports API
  slug: placer-trade-area-reports-api
- description: The Visitor Journey Reports API from Placer — 2 operation(s) for visitor journey reports.
  name: Placer Visitor Journey Reports API
  slug: placer-visitor-journey-reports-api
- description: The Visits Reports API from Placer — 7 operation(s) for visits reports.
  name: Placer Visits Reports API
  slug: placer-visits-reports-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://placer.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.placer.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.placer.ai/docs/welcome-to-placers-feeds
- group: docs
  title: ''
  type: APIReference
  url: https://docs.placer.ai/reference/welcome-to-papi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.placer.ai/reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/placer-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/placer-papi-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/placer-papi-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/placer-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/placer-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/placer-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/placer-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.placer.ai/reference/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.placer.ai/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/placer-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/placer-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/placer-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/placer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/placer-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/placer-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://analytics.placer.ai/my-zone/my-requests/support-requests
- group: start
  title: ''
  type: Login
  url: https://analytics.placer.ai
- group: company
  title: ''
  type: Blog
  url: https://www.placer.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.placer.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.placer.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.placer.ai/privacy-policy
created: '2026-07-17'
description: Placer.ai is a location analytics and foot-traffic intelligence platform that measures visits, trade areas, demographics, and consumer behavior for physical points of interest across retail, CPG, commercial real estate, hospitality, and the public sector. Its public developer surface, the Placer API (PAPI, base https://papi.placer.ai), lets developers and data analysts extract Placer's location analytics programmatically to enrich, filter, or combine it with other data sources for custom dashboards, internal reporting, and competitive analysis. The v1 REST API covers entity/POI search, custom POI and tag management, and a suite of report endpoints spanning visit metrics and trends, trade area (true trade area, drive-time, demographics), ranking, loyalty, and retail sales. Authentication is a static API key sent in the x-api-key header.
image: https://files.readme.io/338fd63-small-Placer_logo_ai_308px2x.png
layout: provider
mcp_servers:
- description: ''
  name: placer-mcp.yml
  slug: placer-mcpyml
modified: '2026-07-20'
name: Placer
nav: Providers
network: true
overview: 'Placer publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account Info API, Loyalty Reports API, Manage POIs API, and 5 more. Tagged areas include Company, Location Analytics, Foot Traffic, Geospatial, and Retail Analytics.


  Placer''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 20 more developer resources.'
random_paper: 51
rate_limits:
- limit_count: 7
  name: Placer Rate Limits
  slug: placer-rate-limits
score:
  band: developing
  composite: 50.7
  delta: -1.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 55.4
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Placer Authentication
  slug: placer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Placer Domain Security
  slug: placer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: placer
tags:
- Company
- Location Analytics
- Foot Traffic
- Geospatial
- Retail Analytics
- Real Estate
- Consumer Insights
- Data
website: https://placer.ai
---
