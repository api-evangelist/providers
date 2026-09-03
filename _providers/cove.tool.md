---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 4
apis:
- baseURL: https://app.covetool.com/api/v2
  baseurl_source: declared
  description: Attempting to make API requests without authentication will fail. API requests must be made over HTTPS. Authentication tokens are used to help identify the user attempting to make the HTTP requests. <
  name: Cove.Tool Authentication Token API
  slug: cove.tool-authentication-token-api
- baseURL: https://app.covetool.com/api/v2
  baseurl_source: declared
  description: The Daylight Analysis API from Cove.Tool — 4 operation(s) for daylight analysis.
  name: Cove.Tool Daylight Analysis API
  slug: cove.tool-daylight-analysis-api
- baseURL: https://app.covetool.com/api/v2
  baseurl_source: declared
  description: The Energy Codes API from Cove.Tool — 1 operation(s) for energy codes.
  name: Cove.Tool Energy Codes API
  slug: cove.tool-energy-codes-api
- baseURL: https://app.covetool.com/api/v2
  baseurl_source: declared
  description: The Profiles API from Cove.Tool — 1 operation(s) for profiles.
  name: Cove.Tool Profiles API
  slug: cove.tool-profiles-api
- baseURL: https://app.covetool.com/api/v2
  baseurl_source: declared
  description: Update project geometry and obtain an Energy Use Intensity (EUI) breakdown of a given model.
  name: Cove.Tool Project Geometry API
  slug: cove.tool-project-geometry-api
- baseURL: https://app.covetool.com/api/v2
  baseurl_source: declared
  description: Lists all the projects of current user and returns a list of objects with project name, runs, and its url.
  name: Cove.Tool Projects API
  slug: cove.tool-projects-api
- baseURL: https://app.covetool.com/api/v2
  baseurl_source: declared
  description: The User API from Cove.Tool — 1 operation(s) for user.
  name: Cove.Tool User API
  slug: cove.tool-user-api
artifact_total: 13
collections:
- collection_type: open
  name: cove.tool API
  slug: open-cove
- collection_type: open
  name: cove.tool REST API v2
  slug: open-cove
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cove.tool-rest-api-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cove.tool-api-v1-overlay.yaml
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
overview: 'Cove.Tool publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication Token API, Daylight Analysis API, Energy Codes API, and 4 more. Tagged areas include Company, Building Performance, Energy Modeling, Daylight Analysis, and Sustainability.


  Cove.Tool''s developer surface includes authentication, API reference, documentation, getting-started guide, support, signup flow, and 17 more developer resources.'
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
  composite: 35.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 50.5
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 35.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cove.tool/refs/heads/main/screenshots/cove.tool-2026-09-02T145157.png
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
