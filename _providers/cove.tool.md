---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cove.Tool Agentic Access
  operation_count: 14
  slug: cove.tool-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 2
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
artifact_total: 40
collections:
- collection_type: open
  name: cove.tool API
  slug: open-cove
- collection_type: open
  name: cove.tool REST API v2
  slug: open-cove
common:
- group: design
  href: https://artifacts.apis.io/cove.tool/conventions/cove.tool-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cove.tool-conventions.yml
- group: agent
  href: https://artifacts.apis.io/cove.tool/agentic-access/cove.tool-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cove.tool-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cove.tool/rules/cove.tool-rules.yml
  title: ''
  type: Spectral
  url: rules/cove.tool-rules.yml
- group: design
  href: https://artifacts.apis.io/cove.tool/json-ld/cove.tool-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cove.tool-context.jsonld
- group: design
  href: https://artifacts.apis.io/cove.tool/vocabulary/cove.tool-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cove.tool-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/cove.tool/hosts/cove.tool-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cove.tool-hosts.yml
- group: other
  href: https://artifacts.apis.io/cove.tool/vendors/cove.tool-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cove.tool-vendors.yml
- group: other
  href: https://artifacts.apis.io/cove.tool/overlays/cove.tool-rest-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cove.tool-rest-api-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cove.tool/overlays/cove.tool-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cove.tool-api-v1-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/cove.tool/security/cove.tool-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cove.tool-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cove.tool/authentication/cove.tool-authentication.yml
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
  href: https://artifacts.apis.io/cove.tool/errors/cove.tool-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cove.tool-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cove.tool/lifecycle/cove.tool-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cove.tool-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cove.tool/conformance/cove.tool-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cove.tool-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/cove.tool/plans/cove.tool-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cove.tool-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cove.tool/rate-limits/cove.tool-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cove.tool-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cove.tool/data-model/cove.tool-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cove.tool-data-model.yml
- group: agent
  href: https://artifacts.apis.io/cove.tool/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-11'
description: 'cove.tool (rebranded to "cove" in 2025) is an Atlanta, Georgia building-performance analysis platform for architects, engineers and contractors, founded in 2017 by Sandeep Ahuja, Patrick Chopson and Daniel Chopson. Its analysis.tool engine runs energy, daylight, glare, embodied carbon, water, radiation, shadow and cost-versus-performance optimization on early-stage building designs. The company publishes a public REST API — marketed as api.tool — that lets software vendors and design firms create projects, upload building geometry, select an energy code, kick off daylight and energy simulation, poll job status and retrieve EUI, sDA and ASE results without using the web application. Two OpenAPI 3.0 definitions are served from the developer portal: a three-operation v1 and a thirteen-operation v2.'
image: https://developers.covetool.com/covetool_logo.png
json_schemas:
- name: AllProjectsRequestsA
  property_count: 0
  slug: cove.tool-all-projects-requests-a
- name: AllProjectsRequestsB
  property_count: 0
  slug: cove.tool-all-projects-requests-b
- name: AuthTokenRequests
  property_count: 2
  slug: cove.tool-auth-token-requests
- name: AuthTokenResponses
  property_count: 2
  slug: cove.tool-auth-token-responses
- name: CreateProjectRequestBody
  property_count: 4
  slug: cove.tool-create-project-request-body
- name: CreateProjectResponse
  property_count: 1
  slug: cove.tool-create-project-response
- name: DaylightAnalysisResultsResponse
  property_count: 1
  slug: cove.tool-daylight-analysis-results-response
- name: DaylightAnalysisStatusResponse
  property_count: 1
  slug: cove.tool-daylight-analysis-status-response
- name: EnergyCodeForProjectsResponses
  property_count: 1
  slug: cove.tool-energy-code-for-projects-responses
- name: EnergyCodeResponses
  property_count: 1
  slug: cove.tool-energy-code-responses
- name: GetProjectInfoResponse
  property_count: 1
  slug: cove.tool-get-project-info-response
- name: RunDaylightAnalysisRequestBody
  property_count: 2
  slug: cove.tool-run-daylight-analysis-request-body
- name: RunDaylightAnalysisResponse
  property_count: 0
  slug: cove.tool-run-daylight-analysis-response
- name: StopDaylightAnalysisResponse
  property_count: 0
  slug: cove.tool-stop-daylight-analysis-response
- name: UpdateGeometryAreasResponses_2
  property_count: 1
  slug: cove.tool-update-geometry-areas-responses-2
- name: UpdateGeometryAreasResponses
  property_count: 2
  slug: cove.tool-update-geometry-areas-responses
- name: Update2DGeometryAreasRequests
  property_count: 22
  slug: cove.tool-update2-dgeometry-areas-requests
- name: Update3DGeometryAreasRequests
  property_count: 17
  slug: cove.tool-update3-dgeometry-areas-requests
- name: Update3DGeometryRequestBody
  property_count: 41
  slug: cove.tool-update3-dgeometry-request-body
- name: UserProfileResponse
  property_count: 1
  slug: cove.tool-user-profile-response
- name: UserSignupOKResponses
  property_count: 1
  slug: cove.tool-user-signup-okresponses
- name: UserSignupRequests
  property_count: 4
  slug: cove.tool-user-signup-requests
jsonld:
- class_count: 29
  name: Cove.Tool Context
  property_count: 86
  slug: cove.tool-context
layout: provider
modified: '2026-08-11'
name: Cove.Tool
nav: Providers
network: true
overview: 'Cove.Tool publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication Token API, Daylight Analysis API, Energy Codes API, and 4 more. Tagged areas include Company, Building Performance, Energy Modeling, Daylight Analysis, and Sustainability.


  The Cove.Tool catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cove.Tool''s developer surface includes authentication, API reference, documentation, getting-started guide, support, signup flow, and 22 more developer resources.'
plans:
- name: Cove.Tool Plans Pricing
  plan_count: 0
  slug: cove.tool-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Cove.Tool Rate Limits
  slug: cove.tool-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Cove.Tool API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: cove.tool-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 41.9
  provenance:
    agentic_access: derived
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
    score: 17.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cove.tool/cove.tool-2026-09-02T145157.png
security:
- kind: authentication
  name: Cove.Tool Authentication
  slug: cove.tool-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Cove.Tool Domain Security
  slug: cove.tool-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: cove-tool-provision-team-access
  slug: cove.tool-provision-team-access
- name: cove-tool-run-daylight-analysis
  slug: cove.tool-run-daylight-analysis
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
