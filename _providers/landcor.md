---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Landcor Agentic Access
  operation_count: 12
  slug: landcor-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- description: The Landcor Property API is a live REST service on api.landcor.com that publishes a valid OpenAPI 3.1.0 contract titled "Landcor Property API" version 0.1.0, served anonymously at https://api.landcor.
  name: Landcor Property API
  slug: landcor-property-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Resolve a BC street address to a Landcor PID, then pull property detail, the AVM valuation range and the valuation history.
  name: Landcor — address to valuation
  slug: landcor-address-to-valuation
- description: Run a proposed mortgage amount against Landcor's AVM value for a BC property and retrieve the password-protected PDF valuation report for the file.
  name: Landcor — loan-to-value check and valuation report
  slug: landcor-ltv-check-and-report
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/landcor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landcor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/landcor-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.landcor.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.landcor.com/redoc
- group: design
  title: ''
  type: Conventions
  url: conventions/landcor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/landcor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/landcor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/landcor-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/landcor-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/landcor-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/landcor-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/landcor-address-to-valuation.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/landcor-ltv-check-and-report.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/landcor-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/landcor-property-api-overlay.yaml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/landcor-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.landcor.com/
- group: other
  title: ''
  type: Products
  url: https://www.landcor.com/online-property-tools/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.landcor.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://store.landcor.com/user/user_add.aspx
- group: start
  title: ''
  type: Login
  url: https://store.landcor.com/user/login.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.landcor.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.landcor.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.landcor.com/about-us/landcor-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.landcor.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.landcor.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.landcor.com/acceptable-use/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.landcor.com/security-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Landcor
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/landcor-data-corporation
created: '2026-07-26'
description: 'Landcor Data Corporation is a New Westminster, British Columbia property data and automated valuation company, founded in 2000, that sells residential valuations, assessment detail and land title documents across the roughly 1.9 million residential properties in BC. It sits in the valuation and public-record layer of the Canadian value chain rather than the listings layer: its inputs are BC Assessment detail, Land Title and Survey Authority (LTSA) title and document search, BC Registry Services, municipal tax certificates and materials licensed from the Integrated Cadastral Information Society (ICIS), and its outputs are the Valuator AVM report, the Adjusted Value Profiler, the Property Profiler, Title Search Plus and historic valuation reports sold to lenders, appraisers, notaries, insurers and brokerages. Its API posture is the unusual case in this study: a real, live, anonymously readable machine-readable contract exists with no developer programme around it. The host api.landcor.com
  runs a FastAPI service on Azure App Service in Canada Central that serves a valid OpenAPI 3.1.0 document titled "Landcor Property API" version 0.1.0 at /openapi.json, with Swagger UI at /docs and ReDoc at /redoc, all returning HTTP 200 without credentials. Twelve operations cover property search, property detail, PDF report retrieval, valuation range, valuation history, loan-to-value checks, neighbourhood sales series, comparables, address autocomplete and an AVM narrative summary. Every operation except /health requires an HTTP Bearer token and returns 401 "Missing token" without one, and no route to obtain that token is published anywhere: landcor.com carries no developer, API, partner or data-licensing page, does not link api.landcor.com at all, and the store.landcor.com self-serve account is for buying individual reports through the web store, not for API credentials. RESO is absent, which is the expected Canadian answer. Landcor is not among the nineteen Canadian organizations RESO
  lists as members, holds no Web API or Data Dictionary certification, exposes no OData $metadata document, and uses its own PID identifier rather than the RESO Universal Property Identifier. No open, unlicensed dataset is published: the underlying assessment, title and cadastral data is licensed to Landcor from provincial bodies and resold, so the public record itself is a commercial product here.'
image: https://www.landcor.com/wp-content/uploads/2026/01/favicon-152.png
layout: provider
mcp_servers:
- description: ''
  name: landcor-mcp.yml
  slug: landcor-mcpyml
modified: '2026-07-26'
name: Landcor Data
nav: Providers
network: true
overview: 'Landcor Data publishes 1 API on the [APIs.io](https://apis.io/) network: Landcor Property API. Tagged areas include Real Estate, Canada, Valuation, AVM, and Property Records.


  Landcor Data''s developer surface includes authentication, documentation, API reference, pricing, signup flow, support, engineering blog, and 25 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 36.4
  delta: -2.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 32.3
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Landcor Authentication
  slug: landcor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Landcor Domain Security
  slug: landcor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: landcor
tags:
- Real Estate
- Canada
- Valuation
- AVM
- Property Records
- Title
- Land Registry
- Mortgage
- PropTech
- Property Data
website: https://www.landcor.com/
---
