---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Climate Fieldview Agentic Access
  operation_count: 11
  slug: climate-fieldview-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: Agricultural field boundaries and metadata
  name: Climate FieldView Fields API
  slug: climate-fieldview-fields-api
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: Field Boundary data endpoints.
  name: Climate FieldView Boundaries API
  slug: climate-fieldview-boundaries-api
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: General data export endpoints.
  name: Climate FieldView Exports API
  slug: climate-fieldview-exports-api
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: Farm organization data endpoints.
  name: Climate FieldView Farm Organizations API
  slug: climate-fieldview-farmorganizations-api
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: General data retrieval endpoints.
  name: Climate FieldView Layers API
  slug: climate-fieldview-layers-api
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: Operation data endpoints.
  name: Climate FieldView Operations API
  slug: climate-fieldview-operations-api
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: Resource Owner data endpoints.
  name: Climate FieldView Resource Owners API
  slug: climate-fieldview-resourceowners-api
- baseURL: https://api.climate.com
  baseurl_source: declared
  description: General data upload endpoints.
  name: Climate FieldView Uploads API
  slug: climate-fieldview-uploads-api
artifact_total: 30
collections:
- collection_type: postman
  name: Climate FieldView Platform Application API
  slug: postman-climate-fieldview-application-api
- collection_type: postman
  name: Climate FieldView Platform Application Fields API
  slug: postman-climate-fieldview-fields-api
- collection_type: postman
  name: Climate FieldView Platform Application Harvest API
  slug: postman-climate-fieldview-harvest-api
- collection_type: postman
  name: Climate FieldView Platform Application Planting API
  slug: postman-climate-fieldview-planting-api
- collection_type: postman
  name: Climate FieldView Platform Application Soil Sampling API
  slug: postman-climate-fieldview-soil-sampling-api
- collection_type: open
  name: Climate FieldView Platform Application API
  slug: open-climate-fieldview-application-api
- collection_type: open
  name: Climate FieldView Platform Application Fields API
  slug: open-climate-fieldview-fields-api
- collection_type: open
  name: Climate FieldView Platform Application Harvest API
  slug: open-climate-fieldview-harvest-api
- collection_type: open
  name: Climate FieldView Platform Application Planting API
  slug: open-climate-fieldview-planting-api
- collection_type: open
  name: Climate FieldView Platform API
  slug: open-climate-fieldview-platform
- collection_type: open
  name: Climate FieldView Platform Application Soil Sampling API
  slug: open-climate-fieldview-soil-sampling-api
common:
- group: commercial
  href: https://artifacts.apis.io/climate-fieldview/plans/climate-fieldview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/climate-fieldview-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/climate-fieldview/rate-limits/climate-fieldview-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/climate-fieldview-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/climate-fieldview/finops/climate-fieldview-finops.yml
  title: ''
  type: FinOps
  url: finops/climate-fieldview-finops.yml
- group: other
  href: https://artifacts.apis.io/climate-fieldview/capabilities/climate-fieldview-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/climate-fieldview-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/climate-fieldview/overview
- group: agent
  href: https://artifacts.apis.io/climate-fieldview/agentic-access/climate-fieldview-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/climate-fieldview-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/climate-fieldview/security/climate-fieldview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/climate-fieldview-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/climate-fieldview/authentication/climate-fieldview-authentication.yml
  title: ''
  type: Authentication
  url: authentication/climate-fieldview-authentication.yml
- group: auth
  href: https://artifacts.apis.io/climate-fieldview/scopes/climate-fieldview-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/climate-fieldview-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/climate-llc
- group: company
  title: ''
  type: Website
  url: https://climate.com/
- group: start
  title: ''
  type: Portal
  url: https://dev.fieldview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fieldview.com/technical-documentation/
- group: auth
  title: ''
  type: Authentication
  url: https://dev.fieldview.com/api-details/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.fieldview.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://climate.com/en-us/legal/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://climate.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/TheClimateCorporation/api-example
- group: company
  title: ''
  type: Partners
  url: https://climate.com/partners
- group: docs
  href: https://artifacts.apis.io/climate-fieldview/openapi/_original/climate-fieldview-platform-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/climate-fieldview-platform-openapi.yml
- group: docs
  href: https://artifacts.apis.io/climate-fieldview/json-schema/climate-fieldview-field-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/climate-fieldview-field-schema.json
- group: design
  href: https://artifacts.apis.io/climate-fieldview/json-ld/climate-fieldview-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/climate-fieldview-context.jsonld
- group: design
  href: https://artifacts.apis.io/climate-fieldview/rules/climate-fieldview-rules.yml
  title: ''
  type: Spectral
  url: rules/climate-fieldview-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://climate.com/en-us/resources/blog.html
created: '2025-03-05'
description: Climate FieldView is a digital agriculture platform from Bayer (originally developed by The Climate Corporation) that gives growers, agronomists, and agribusiness partners a single view of field-level operations. The platform ingests as-planted, as-applied, and as-harvested data from field equipment, combines it with imagery, weather, and soil layers, and exposes those agronomic datasets through a REST API at api.climate.com. Authentication is via OAuth 2.0 authorization-code grant, and resources include fields, planting and harvest activities, application records, and soil samples.
finops:
- has_sources: false
  method: generated
  name: Climate Fieldview Finops
  primary_unit: request
  service_category: API
  slug: climate-fieldview-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/climate-fieldview.png
json_schemas:
- name: Climate FieldView Field
  property_count: 11
  slug: climate-fieldview-field
jsonld:
- class_count: 2
  name: Climate Fieldview Context
  property_count: 23
  slug: climate-fieldview-context
layout: provider
modified: '2026-05-19'
name: Climate FieldView
nav: Providers
network: true
overview: 'Climate FieldView publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Fields API, Boundaries API, Exports API, and 5 more. Tagged areas include Agriculture, Bayer, Crop Data, Field Boundaries, and Harvest.


  The Climate FieldView catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Climate FieldView''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 19 more developer resources.'
plans:
- name: Climate Fieldview Plans Pricing
  plan_count: 3
  slug: climate-fieldview-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Climate Fieldview Rate Limits
  slug: climate-fieldview-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Climate FieldView — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: climate-fieldview-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Climate FieldView API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: climate-fieldview-rules
scopes:
- name: Climate Fieldview Scopes
  scope_count: 5
  slug: climate-fieldview-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.5
    catalog_earned_first_party: 0.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 60.1
    developer_ergonomics: 53.6
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 57.1
      total: 14
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/climate-fieldview/climate-fieldview-2026-06-20T174520.png
security:
- kind: authentication
  name: Climate Fieldview Authentication
  slug: climate-fieldview-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Climate Fieldview Domain Security
  slug: climate-fieldview-domain-security
  summary_line: TLSv1.3 · DMARC
slug: climate-fieldview
tags:
- Agriculture
- Bayer
- Crop Data
- Field Boundaries
- Harvest
- OAuth
- Planting
- Precision Agriculture
- AgTech
- Authentication
website: https://climate.com/
---
