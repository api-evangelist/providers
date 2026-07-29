---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Climate Fieldview Agentic Access
  operation_count: 11
  slug: climate-fieldview-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 5
apis:
- description: As-applied agrochemical data
  name: Climate FieldView Application API
  slug: climate-fieldview-application-api
- description: Agricultural field boundaries and metadata
  name: Climate FieldView Fields API
  slug: climate-fieldview-fields-api
- description: As-harvested yield data and maps
  name: Climate FieldView Harvest API
  slug: climate-fieldview-harvest-api
- description: As-planted activity data and maps
  name: Climate FieldView Planting API
  slug: climate-fieldview-planting-api
- description: Soil sample results and layers
  name: Climate FieldView Soil Sampling API
  slug: climate-fieldview-soil-sampling-api
artifact_total: 22
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
  name: Climate FieldView Platform API
  slug: open-climate-fieldview-platform
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/climate-fieldview/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/climate-fieldview-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/climate-fieldview-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/climate-fieldview-authentication.yml
- group: auth
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
  title: ''
  type: OpenAPI
  url: openapi/climate-fieldview-platform-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/climate-fieldview-field-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/climate-fieldview-context.jsonld
- group: design
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
- name: Climate Fieldview Finops
  service_category: API
  slug: climate-fieldview-finops
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
overview: 'Climate FieldView publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Application API, Fields API, Harvest API, and 2 more. Tagged areas include Agriculture, Bayer, Crop Data, Field Boundaries, and Harvest.


  The Climate FieldView catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Climate FieldView''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Climate Fieldview Plans Pricing
  plan_count: 3
  slug: climate-fieldview-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Climate Fieldview Rate Limits
  slug: climate-fieldview-rate-limits
rules:
- name: Climate FieldView API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: climate-fieldview-jsonschema-spectral-rules
- name: Climate FieldView API Rules
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
  band: strong
  composite: 56.9
  delta: -3.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.9
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/climate-fieldview/refs/heads/main/screenshots/climate-fieldview-2026-06-20T174520.png
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
- OAuth2
- Planting
- Precision Ag
website: https://climate.com/
---
