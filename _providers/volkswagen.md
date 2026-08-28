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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Volkswagen Agentic Access
  operation_count: 12
  slug: volkswagen-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 3
apis:
- description: Browse vehicle catalog — countries, brands, models, types, and options.
  name: Volkswagen Catalog API
  slug: volkswagen-catalog-api
- description: Configure vehicles — check buildability, recover, and resolve configurations.
  name: Volkswagen Configuration API
  slug: volkswagen-configuration-api
- description: Retrieve vehicle information — WLTP emissions, images, and order data.
  name: Volkswagen Information API
  slug: volkswagen-information-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Volkswagen OKAPI - Open Konfigurator Catalog API
  slug: open-volkswagen-catalog-api
- collection_type: open
  name: Volkswagen OKAPI - Open Konfigurator Catalog Configuration API
  slug: open-volkswagen-configuration-api
- collection_type: open
  name: Volkswagen OKAPI - Open Konfigurator Catalog Information API
  slug: open-volkswagen-information-api
- collection_type: open
  name: Volkswagen OKAPI - Open Konfigurator API
  slug: open-volkswagen-okapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/volkswagen-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/volkswagen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volkswagen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/volkswagen-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volkswagen
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/volkswagen
- group: other
  title: ''
  type: WhatsNew
  url: https://productdata.volkswagenag.com/whats-new.html
- group: docs
  title: ''
  type: Guide
  url: https://productdata.volkswagenag.com/introduction.html
- group: operate
  title: ''
  type: Support
  url: https://productdata.volkswagenag.com/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://productdata.volkswagenag.com/condition-of-use.html
- group: start
  title: ''
  type: Portal
  url: https://okapi-ddp.productdata.volkswagenag.com/dev-portal/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/volkswagen-okapi-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/volkswagen-vehicle-config-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/volkswagen-vehicle-config-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/volkswagen-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/volkswagen-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/volkswagen-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.volkswagen-newsroom.com/en/feeds/press-releases
created: '2025-02-25'
description: Volkswagen is a German automotive company and the parent of the VW Group, manufacturing vehicles under brands including Volkswagen, Audi, SEAT, Skoda, CUPRA, Porsche, Lamborghini, and Bentley. The OKAPI (Open Konfigurator API) provides programmatic access to VW AG product data for vehicle catalog browsing, interactive configuration, buildability validation, WLTP emissions data, configuration images, and order/pricing information across global markets.
examples:
- key_count: 2
  name: Volkswagen Checkbuildability Example
  slug: volkswagen-checkBuildability-example
- key_count: 2
  name: Volkswagen Getorderinformation Example
  slug: volkswagen-getOrderInformation-example
- key_count: 2
  name: Volkswagen Getwltpdata Example
  slug: volkswagen-getWltpData-example
- key_count: 2
  name: Volkswagen Listcountries Example
  slug: volkswagen-listCountries-example
finops:
- name: Volkswagen Finops
  service_category: API
  slug: volkswagen-finops
graphqls:
- description: Volkswagen provides connected vehicle APIs through the We Connect platform. The API covers vehicle status, remote operations (lock, ventilation, charging), electric range and charging data, trip histo
  name: Volkswagen GraphQL API
  slug: volkswagen-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/volkswagen.png
json_schemas:
- name: Volkswagen Vehicle Configuration
  property_count: 6
  slug: volkswagen-vehicle-config
json_structures:
- name: Volkswagen Vehicle Config Structure
  property_count: 0
  slug: volkswagen-vehicle-config-structure
jsonld:
- class_count: 25
  name: Volkswagen Context
  property_count: 0
  slug: volkswagen-context
layout: provider
modified: '2026-05-19'
name: Volkswagen
nav: Providers
network: true
overview: 'Volkswagen publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Configuration API, and Information API. Tagged areas include Automobiles, Cars, Vehicles, Automotive, and Vehicle Configuration.


  The Volkswagen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Volkswagen''s developer surface includes authentication, support, developer portal, engineering blog, and 14 more developer resources.'
plans:
- name: Volkswagen Plans Pricing
  plan_count: 3
  slug: volkswagen-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Volkswagen Rate Limits
  slug: volkswagen-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Volkswagen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: volkswagen-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Volkswagen API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: volkswagen-rules
score:
  band: developing
  composite: 46.2
  delta: 4.3
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 71.7
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/volkswagen/refs/heads/main/screenshots/volkswagen-2026-06-20T201131.png
security:
- kind: authentication
  name: Volkswagen Authentication
  slug: volkswagen-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Volkswagen Domain Security
  slug: volkswagen-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Volkswagen Vulnerability Disclosure
  slug: volkswagen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: volkswagen
tags:
- Automobiles
- Cars
- Vehicles
- Automotive
- Vehicle Configuration
website: https://okapi-ddp.productdata.volkswagenag.com/dev-portal/
---
