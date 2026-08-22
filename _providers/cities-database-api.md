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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cities Database Api Agentic Access
  operation_count: 1
  slug: cities-database-api-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The Cities API from Cities Database API — 1 operation(s) for cities.
  name: Cities Database API Cities API
  slug: cities-database-api-cities-api
artifact_total: 15
collections:
- collection_type: postman
  name: AirLabs Database Cities API
  slug: postman-cities-database-api-cities-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AirLabs Database Cities API
  slug: open-cities-database-api-cities-api
- collection_type: open
  name: AirLabs Cities Database API
  slug: open-cities-database-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cities-database-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cities-database-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cities-database-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cities-database-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://airlabs.co/
- group: docs
  title: ''
  type: Documentation
  url: https://airlabs.co/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://airlabs.co/pricing
- group: start
  title: ''
  type: Signup
  url: https://airlabs.co/signup
- group: start
  title: ''
  type: Login
  url: https://airlabs.co/login
- group: other
  title: ''
  type: Account
  url: https://airlabs.co/account
- group: auth
  title: ''
  type: Authentication
  url: https://airlabs.co/account/api-key
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airlabs.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airlabs.co/terms
- group: operate
  title: ''
  type: Support
  url: https://airlabs.co/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://airlabs.co/status
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cities-database-api-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cities-database-api-city-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/cities-database-api-rules.yml
created: '2024-03-30'
description: The Cities Database API by AirLabs provides a global reference dataset of cities keyed to IATA metropolitan area codes, ISO country codes, and geographic coordinates. The API is consumed alongside the AirLabs Airports, Airlines, and Flights APIs to power travel search, mapping, geocoding, and clustering experiences. Authentication uses an api_key query parameter obtained from the AirLabs account dashboard. All responses are JSON arrays of city objects.
finops:
- name: Cities Database Api Finops
  service_category: API
  slug: cities-database-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cities-database-api.png
json_schemas:
- name: AirLabs City
  property_count: 12
  slug: cities-database-api-city
jsonld:
- class_count: 13
  name: Cities Database Api Context
  property_count: 0
  slug: cities-database-api-context
layout: provider
modified: '2026-05-19'
name: Cities Database API
nav: Providers
network: true
overview: 'Cities Database API publishes 1 API on the [APIs.io](https://apis.io/) network: Cities API. Tagged areas include Cities, Data, Geography, Locations, and Reference Data.


  The Cities Database API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cities Database API''s developer surface includes authentication, documentation, pricing, signup flow, support, and 13 more developer resources.'
plans:
- name: Cities Database Api Plans Pricing
  plan_count: 3
  slug: cities-database-api-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Cities Database Api Rate Limits
  slug: cities-database-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cities Database API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cities-database-api-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Cities Database API API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: cities-database-api-rules
score:
  band: thin
  composite: 31.9
  delta: -19.4
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 9.8
    contract_quality: 62.2
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cities-database-api/refs/heads/main/screenshots/cities-database-api-2026-06-20T174409.png
security:
- kind: authentication
  name: Cities Database Api Authentication
  slug: cities-database-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cities Database Api Domain Security
  slug: cities-database-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cities-database-api
tags:
- Cities
- Data
- Geography
- Locations
- Reference Data
- Travel
website: https://airlabs.co/
---
