---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Regrow Ag Agentic Access
  operation_count: 40
  slug: regrow-ag-agentic-access
  summary_line: 40 operations · 19 acting
api_count: 2
apis:
- baseURL: https://api.regrow.ag/monitor-api/
  baseurl_source: declared
  description: The OGC API - General API from Regrow — 1 operation(s) for ogc api - general.
  name: Regrow OGC API - General API
  slug: regrow-ag-ogc-api-general-api
- baseURL: https://api.regrow.ag/monitor-api/
  baseurl_source: declared
  description: The OGC API - Processes API from Regrow — 4 operation(s) for ogc api - processes.
  name: Regrow OGC API - Processes API
  slug: regrow-ag-ogc-api-processes-api
- baseURL: https://api.regrow.ag/monitor-api/
  baseurl_source: declared
  description: 'Explore API allows users to predict or forecast the emissions impact of adopting a regenerative agricultural practice, or *intervention*, for a specific field. Explore uses the DNDC model to simulate '
  name: Regrow V0 Explore API - Intervention API
  slug: regrow-ag-v0-explore-api-intervention-api
- baseURL: https://api.regrow.ag/monitor-api/
  baseurl_source: declared
  description: Measure API is composed of modules. This module is called `Intervention`, and to learn more about the API consult the documentation at https://help.regrow.ag/intervention-module-integration-guide.
  name: Regrow V0 Measure API - Intervention API
  slug: regrow-ag-v0-measure-api-intervention-api
- baseURL: https://api.regrow.ag/monitor-api/
  baseurl_source: declared
  description: Measure API is composed of modules. This module is called `Inventory`, and to learn more about the API consult the documentation at https://help.regrow.ag/inventory-module-integration-overview.
  name: Regrow V0 Measure API - Inventory API
  slug: regrow-ag-v0-measure-api-inventory-api
- baseURL: https://api.regrow.ag/monitor-api/
  baseurl_source: declared
  description: Measure API is composed of modules. This module is called `Enteric`, and to learn more about the API consult the documentation at https://help.regrow.ag/.
  name: Regrow V1 Measure API - Enteric API
  slug: regrow-ag-v1-measure-api-enteric-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/regrow-ag/agentic-access/regrow-ag-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/regrow-ag-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/regrow-ag/rate-limits/regrow-ag-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/regrow-ag-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/regrow-ag/rules/regrow-ag-rules.yml
  title: ''
  type: Spectral
  url: rules/regrow-ag-rules.yml
- group: design
  href: https://artifacts.apis.io/regrow-ag/json-ld/regrow-ag-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/regrow-ag-context.jsonld
- group: design
  href: https://artifacts.apis.io/regrow-ag/vocabulary/regrow-ag-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/regrow-ag-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/regrow-ag/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/regrow-ag/data-model/regrow-ag-data-model.yml
  title: ''
  type: DataModel
  url: data-model/regrow-ag-data-model.yml
- group: operate
  href: https://artifacts.apis.io/regrow-ag/changelog/regrow-ag-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/regrow-ag-changelog.yml
- group: design
  href: https://artifacts.apis.io/regrow-ag/conventions/regrow-ag-conventions.yml
  title: ''
  type: Conventions
  url: conventions/regrow-ag-conventions.yml
- group: auth
  href: https://artifacts.apis.io/regrow-ag/authentication/regrow-ag-authentication.yml
  title: ''
  type: Authentication
  url: authentication/regrow-ag-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.regrow.ag/versioning-of-measure-api-and-explore-api
- group: design
  href: https://artifacts.apis.io/regrow-ag/lifecycle/regrow-ag-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/regrow-ag-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/regrow-ag/errors/regrow-ag-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/regrow-ag-problem-types.yml
- group: design
  href: https://artifacts.apis.io/regrow-ag/conformance/regrow-ag-conformance.yml
  title: ''
  type: Conformance
  url: conformance/regrow-ag-conformance.yml
- group: other
  href: https://artifacts.apis.io/regrow-ag/overlays/regrow-ag-measure-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/regrow-ag-measure-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/regrow-ag/hosts/regrow-ag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/regrow-ag-hosts.yml
- group: other
  href: https://artifacts.apis.io/regrow-ag/vendors/regrow-ag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/regrow-ag-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.regrow.ag/new-client-onboarding-to-measure-api
- group: company
  title: ''
  type: Website
  url: https://www.regrow.ag
- group: auth
  href: https://artifacts.apis.io/regrow-ag/security/regrow-ag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/regrow-ag-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.regrow.ag/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.regrow.ag/apis
- group: start
  title: ''
  type: Login
  url: https://app.regrow.ag
- group: company
  title: ''
  type: Blog
  url: https://www.regrow.ag/resources/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.regrow.ag/resources/news
- group: other
  title: ''
  type: Leadership
  url: https://www.regrow.ag/tags/team
- group: operate
  title: ''
  type: Support
  url: https://help.regrow.ag/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.regrow.ag/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.regrow.ag/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.regrow.ag/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regrowag
- group: company
  title: ''
  type: Twitter
  url: https://www.twitter.com/regrowag
created: '2026-10-18'
description: Regrow (regrow.ag) runs an Agriculture Resilience Platform that helps food and agriculture companies measure, report, and reduce on-farm greenhouse gas emissions, cut scope 3 emissions and work toward net zero goals. Its developer portal at developers.regrow.ag lists the Explore API (baseline GHG emissions and the modeled impact of regenerative practices), the Measure API Enteric, Intervention and Inventory modules, and the Monitor API (remote-sensing based field crop and management practice verification). The API documentation requires signing in to the portal.
image: https://cdn.prod.website-files.com/6886e3608592c9b2ccef36f2/6a34a2ce44d27a821ee6e49c_9ee0b697532cf0b5851d72e412be4d7a_home-og.jpg
json_schemas:
- name: ExecuteProcessRequestBody[MonitorFieldBoundaryIdInputs]
  property_count: 5
  slug: regrow-ag-execute-process-request-body-monitor-field-boundary-id-inputs
- name: ExecuteProcessRequestBody[MonitorFieldGeojsonInputs]
  property_count: 5
  slug: regrow-ag-execute-process-request-body-monitor-field-geojson-inputs
- name: HealthCheck
  property_count: 3
  slug: regrow-ag-health-check
- name: InterventionInput
  property_count: 4
  slug: regrow-ag-intervention-input
- name: JobResultResponse
  property_count: 0
  slug: regrow-ag-job-result-response
- name: JobStatusResponse
  property_count: 12
  slug: regrow-ag-job-status-response
- name: MonitorFieldBoundaryIdOutputs
  property_count: 1
  slug: regrow-ag-monitor-field-boundary-id-outputs
- name: ProjectInventoryResponse
  property_count: 3
  slug: regrow-ag-project-inventory-response
- name: ProjectScope1CreditShareResponse
  property_count: 2
  slug: regrow-ag-project-scope1-credit-share-response
- name: ProjectScope1Response
  property_count: 2
  slug: regrow-ag-project-scope1-response
- name: ProjectScope3CreditShareResponse
  property_count: 2
  slug: regrow-ag-project-scope3-credit-share-response
- name: ProjectScope3Response
  property_count: 2
  slug: regrow-ag-project-scope3-response
jsonld:
- class_count: 120
  name: Regrow Ag Context
  property_count: 191
  slug: regrow-ag-context
layout: provider
modified: '2026-10-18'
name: Regrow
nav: Providers
network: true
overview: 'Regrow publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including OGC API - General API, OGC API - Processes API, V0 Explore API - Intervention API, and 3 more. Tagged areas include Company, Agriculture, Sustainability, Greenhouse Gas Emissions, and Carbon.


  The Regrow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Regrow''s developer surface includes changelog, authentication, getting-started guide, API reference, engineering blog, support, and 26 more developer resources.'
plans:
- name: Regrow Ag Plans Pricing
  plan_count: 0
  slug: regrow-ag-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Regrow Ag Rate Limits
  slug: regrow-ag-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Regrow API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 4
  slug: regrow-ag-rules
scopes:
- name: Regrow Ag Scopes
  scope_count: 0
  slug: regrow-ag-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 58.9
    discoverability: 69.6
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Regrow Ag Authentication
  slug: regrow-ag-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Regrow Ag Domain Security
  slug: regrow-ag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 8
skills:
- name: regrow-ag-create-and-manage-project-with-fields
  slug: regrow-ag-create-and-manage-project-with-fields
- name: regrow-ag-enteric-project-management
  slug: regrow-ag-enteric-project-management
- name: regrow-ag-explore-field-estimates
  slug: regrow-ag-explore-field-estimates
- name: regrow-ag-intervention-project
  slug: regrow-ag-intervention-project
- name: regrow-ag-measure-inventory-project
  slug: regrow-ag-measure-inventory-project
- name: regrow-ag-monitor-field-and-retrieve-results
  slug: regrow-ag-monitor-field-and-retrieve-results
- name: regrow-ag-monitor-field
  slug: regrow-ag-monitor-field
- name: regrow-ag-upload-field-and-retrieve-estimates
  slug: regrow-ag-upload-field-and-retrieve-estimates
slug: regrow-ag
tags:
- Company
- Agriculture
- Sustainability
- Greenhouse Gas Emissions
- Carbon
- Regenerative Agriculture
- Remote Sensing
- Climate
website: https://www.regrow.ag
---
