---
access_model:
  confidence: high
  label: Credentials issued on request
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://api-docs.groundtruth.com/welcome-824669m0
  - https://help.groundtruth.com/hc/en-us/articles/4402393255315-Can-I-set-up-external-reporting-API
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Groundtruth Agentic Access
  operation_count: 318
  slug: groundtruth-agentic-access
  summary_line: 318 operations · 63 acting
api_count: 3
apis:
- description: 'REST API for the GroundTruth Ads Manager platform: create and manage accounts, organizations, tenants, users, campaigns, ad groups, creatives and creative assets; run audience, location and static ref'
  name: GroundTruth Ads Manager Public API
  slug: groundtruth-ads-manager-public-api
- description: 'Read-only external reporting API (the "demand" API) for pulling GroundTruth campaign performance out of the platform and into a partner or agency reporting stack: account, organization, campaign, ad g'
  name: Groundtruth Reporting API
  slug: groundtruth-reporting-api
- description: Model Context Protocol endpoint served on the GroundTruth developer documentation host. It answers MCP JSON-RPC on /mcp but returns error -32001 "Authorization required" to anonymous initialize and to
  name: GroundTruth Documentation MCP Server
  slug: groundtruth-documentation-mcp-server
artifact_total: 12
collections:
- collection_type: open
  name: Ads Manager API
  slug: open-groundtruth-ads-manager
- collection_type: open
  name: Groundtruth Reporting API
  slug: open-groundtruth-reporting
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groundtruth-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/groundtruth-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.groundtruth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.groundtruth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.groundtruth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.groundtruth.com/
- group: start
  title: ''
  type: SignUp
  url: https://ads.groundtruth.com/login?sign_up=1
- group: start
  title: ''
  type: Login
  url: https://ads.groundtruth.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.groundtruth.com/insight/category/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.groundtruth.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.groundtruth.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.groundtruth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.groundtruth.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.groundtruth.com/get-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/groundtruth-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/groundtruth-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/groundtruth-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/groundtruth-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/groundtruth-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/groundtruth-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/groundtruth-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/groundtruth-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/groundtruth-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/groundtruth-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/groundtruth-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/groundtruth-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/groundtruth-ads-manager-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/groundtruth-reporting-overlay.yaml
created: '2026-07-17'
description: 'GroundTruth is a location-intelligence performance advertising platform (formerly xAd) that helps brands and agencies plan, launch, and measure omnichannel ad campaigns tied to real-world behavior. Its Ads Manager, proprietary Blueprints location-mapping technology, and Dynamic Intent Prediction AI turn visitation, behavioral, and demographic signals into targeting and store-visit and sales attribution across verticals including QSR/restaurants, CPG, auto, retail, healthcare, education, travel, and political. GroundTruth is backed by Emergence Capital and IVP and became part of ZeroToOne.AI in 2026. GroundTruth publishes two public REST API surfaces: the Ads Manager Public API at api-public.groundtruth.com (259 operations across accounts, organizations, tenants, campaigns, ad groups, creatives, audiences, jobs, uploads, search and reporting, with a live OpenAPI 3.1 document and Swagger UI at /docs), and the Groundtruth Reporting API at reporting.groundtruth.com (59 read-only
  demand-reporting operations described by an OpenAPI 3.0.1 document). Both authenticate with the paired X-GT-USER-ID and X-GT-API-KEY headers; credentials are issued on request rather than self-serve.'
image: https://www.groundtruth.com/wp-content/uploads/2026/06/GroundTruth-Featured-Image.webp
layout: provider
mcp_servers:
- description: ''
  name: groundtruth-mcp.yml
  slug: groundtruth-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-12'
name: GroundTruth
nav: Providers
network: true
overview: 'GroundTruth publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ads Manager Public API and Reporting API. Tagged areas include Company, Martech, Advertising, Location Intelligence, and Marketing.


  GroundTruth''s developer surface includes documentation, API reference, signup flow, engineering blog, support, getting-started guide, authentication, and 22 more developer resources.'
plans:
- name: Groundtruth Plans Pricing
  plan_count: 0
  slug: groundtruth-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Groundtruth Rate Limits
  slug: groundtruth-rate-limits
score:
  band: developing
  composite: 40.7
  delta: -3.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 51.6
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groundtruth/refs/heads/main/screenshots/groundtruth-2026-07-25T220343.png
security:
- kind: authentication
  name: Groundtruth Authentication
  slug: groundtruth-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Groundtruth Domain Security
  slug: groundtruth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groundtruth
tags:
- Company
- Martech
- Advertising
- Location Intelligence
- Marketing
- Adtech
- Location-Based Marketing
- Advertising API
- Campaign Management
- Ad Reporting
- Attribution
- Geofencing
- Digital Out Of Home
- CTV
website: https://www.groundtruth.com
---
