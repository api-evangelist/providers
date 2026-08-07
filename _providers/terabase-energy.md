---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.5
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: The REST API behind PlantPredict, Terabase Energy's utility-scale solar performance-modeling platform. It exposes the full modeling engine — projects, predictions, power plant designs (blocks/arrays/i
  name: PlantPredict Performance API
  slug: plantpredict-performance-api
- description: Hosted Model Context Protocol server that lets Claude, ChatGPT and Cursor act on a user's own PlantPredict account — creating and running predictions, importing weather and shade scenes, browsing proj
  name: PlantPredict MCP Connector
  slug: plantpredict-mcp-connector
- description: Terabase Energy's terrain analysis and solar site-planning API, used by the Terrain Pro application for elevation data extraction, layout generation, grading/earthwork solutions, pile binning and reve
  name: Terrain Pro API
  slug: terrain-pro-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.terabase.energy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.plantpredict.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plantpredict.com/api-docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://docs.plantpredict.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.plantpredict.com/api-docs/api_quick_start_guide
- group: operate
  title: ''
  type: Support
  url: https://www.plantpredict.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.terabase.energy/resources-library?cat=insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plantpredict
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plantpredict.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.plantpredict.com/signup
- group: start
  title: ''
  type: Login
  url: https://ui.plantpredict.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.terabase.energy/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.terabase.energy/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/3855302/UVsHUoHa
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.plantpredict.com/release-notes/Current-Version
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/terabase-energy-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.plantpredict.com/user-guide/resources/security-compliance
- group: agent
  title: ''
  type: MCPServer
  url: mcp/terabase-energy-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/terabase-energy-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terabase-energy-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/terabase-energy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/terabase-energy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/terabase-energy-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terabase-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/terabase-energy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/terabase-energy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/terabase-energy-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/terabase-energy-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terabase-energy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/terabase-energy-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terabase-energy-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/terabase-energy-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/terabase-energy-plantpredict-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/terabase-energy-a2a.yml
created: '2026-08-05'
description: Terabase Energy builds digital and automation technology for the full lifecycle of utility-scale solar power plants — engineering and energy modeling, robotic field construction, and plant operations. Its software portfolio includes PlantPredict, an industry-standard bankable performance-modeling platform for utility-scale PV that predicts energy yield from early-stage prospecting through operational monitoring; Terrain Pro, a terrain analysis, grading and pile-layout engine for site design; Construct, a construction management platform; and Terafab, an automated field-factory system for solar module installation. PlantPredict exposes its entire modeling engine as a documented REST API (OpenAPI 3.1, OAuth 2.0 client-credentials via AWS Cognito), an official Python SDK, a Postman collection, and a hosted, OAuth-protected Model Context Protocol (MCP) connector for Claude, ChatGPT and Cursor.
image: https://www.terabase.energy/wp-content/uploads/cropped-favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: terabase-energy-mcp.yml
  slug: terabase-energy-mcpyml
modified: '2026-08-05'
name: Terabase Energy
nav: Providers
network: true
overview: 'Terabase Energy publishes 1 API on the [APIs.io](https://apis.io/) network: PlantPredict Performance API. Tagged areas include solar, renewable-energy, energy-modeling, utility-scale-solar, and simulation.


  Terabase Energy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 65
rate_limits:
- limit_count: 0
  name: Terabase Energy Rate Limits
  slug: terabase-energy-rate-limits
scopes:
- name: Terabase Energy Scopes
  scope_count: 2
  slug: terabase-energy-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 56.3
  facets:
    commercial_clarity: 52.6
    contract_quality: 62.5
    developer_ergonomics: 78.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Terabase Energy Authentication
  slug: terabase-energy-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Terabase Energy Domain Security
  slug: terabase-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: terabase-energy
tags:
- solar
- renewable-energy
- energy-modeling
- utility-scale-solar
- simulation
- photovoltaics
- construction-technology
- geospatial
- terrain-analysis
- climate-tech
- mcp
- energy-storage
website: https://www.terabase.energy/
---
