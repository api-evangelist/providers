---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The current cove.tool REST API. Thirteen operations across six tags — User, Profiles, Energy Codes, Projects, Project Geometry and Daylight Analysis — covering account creation, project create/read/up
  name: cove.tool REST API v2
  slug: rest-api-v2
- description: 'The original cove.tool API, still served from the developer portal alongside v2. Three operations: obtain an API token, list projects and their associated information, and update run values (geometry)'
  name: cove.tool API v1
  slug: api-v1
artifact_total: 8
collections:
- collection_type: open
  name: cove.tool API
  slug: open-cove
- collection_type: open
  name: cove.tool REST API v2
  slug: open-cove
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cove.tool-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cove.tool-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cove.inc/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.covetool.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.covetool.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.covetool.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.covetool.com/en/articles/6022777-what-is-the-cove-tool-api
- group: operate
  title: ''
  type: Support
  url: https://help.covetool.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.covetool.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.covetool.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/covetool
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cove.tools/terms-of-use
- group: design
  title: ''
  type: Conventions
  url: conventions/cove.tool-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cove.tool-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cove.tool-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cove.tool-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cove.tool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cove.tool-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cove.tool-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cove.tool-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-11'
description: 'cove.tool (rebranded to "cove" in 2025) is an Atlanta, Georgia building-performance analysis platform for architects, engineers and contractors, founded in 2017 by Sandeep Ahuja, Patrick Chopson and Daniel Chopson. Its analysis.tool engine runs energy, daylight, glare, embodied carbon, water, radiation, shadow and cost-versus-performance optimization on early-stage building designs. The company publishes a public REST API — marketed as api.tool — that lets software vendors and design firms create projects, upload building geometry, select an energy code, kick off daylight and energy simulation, poll job status and retrieve EUI, sDA and ASE results without using the web application. Two OpenAPI 3.0 definitions are served from the developer portal: a three-operation v1 and a thirteen-operation v2.'
image: https://developers.covetool.com/covetool_logo.png
layout: provider
modified: '2026-08-11'
name: Cove.Tool
nav: Providers
network: true
overview: 'Cove.Tool publishes 2 APIs on the [APIs.io](https://apis.io/) network: REST API v2 and API v1. Tagged areas include Company, Building Performance, Energy Modeling, Daylight Analysis, and Sustainability.


  Cove.Tool''s developer surface includes authentication, API reference, documentation, getting-started guide, support, signup flow, and 15 more developer resources.'
plans:
- name: Cove.Tool Plans Pricing
  plan_count: 0
  slug: cove.tool-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Cove.Tool Rate Limits
  slug: cove.tool-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 49.8
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 36.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Cove.Tool Authentication
  slug: cove.tool-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cove.Tool Domain Security
  slug: cove.tool-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cove.tool
tags:
- Company
- Building Performance
- Energy Modeling
- Daylight Analysis
- Sustainability
- Architecture
- AEC
- Simulation
- Embodied Carbon
- Building Design
website: https://cove.inc/
---
