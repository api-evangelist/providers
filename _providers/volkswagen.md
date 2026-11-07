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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Volkswagen Agentic Access
  operation_count: 12
  slug: volkswagen-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 1
apis:
- baseURL: https://productdata.volkswagenag.com/v3
  baseurl_source: declared
  description: Browse vehicle catalog — countries, brands, models, types, and options.
  name: Volkswagen Catalog API
  slug: volkswagen-catalog-api
- baseURL: https://productdata.volkswagenag.com/v3
  baseurl_source: declared
  description: Configure vehicles — check buildability, recover, and resolve configurations.
  name: Volkswagen Configuration API
  slug: volkswagen-configuration-api
- baseURL: https://productdata.volkswagenag.com/v3
  baseurl_source: declared
  description: Retrieve vehicle information — WLTP emissions, images, and order data.
  name: Volkswagen Information API
  slug: volkswagen-information-api
artifact_total: 23
collections:
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/volkswagen/overview
- group: commercial
  href: https://artifacts.apis.io/volkswagen/plans/volkswagen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/volkswagen-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/volkswagen/rate-limits/volkswagen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/volkswagen-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/volkswagen/finops/volkswagen-finops.yml
  title: ''
  type: FinOps
  url: finops/volkswagen-finops.yml
- group: company
  title: ''
  type: Website
  url: https://volkswagenag.com
- group: other
  href: https://artifacts.apis.io/volkswagen/capabilities/volkswagen-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/volkswagen-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/volkswagen/agentic-access/volkswagen-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/volkswagen-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/volkswagen/security/volkswagen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/volkswagen-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/volkswagen/security/volkswagen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/volkswagen-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/volkswagen/authentication/volkswagen-authentication.yml
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
  href: https://artifacts.apis.io/volkswagen/openapi/_original/volkswagen-okapi-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/volkswagen-okapi-openapi.yml
- group: docs
  href: https://artifacts.apis.io/volkswagen/json-schema/volkswagen-vehicle-config-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/volkswagen-vehicle-config-schema.json
- group: design
  href: https://artifacts.apis.io/volkswagen/json-structure/volkswagen-vehicle-config-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/volkswagen-vehicle-config-structure.json
- group: design
  href: https://artifacts.apis.io/volkswagen/json-ld/volkswagen-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/volkswagen-context.jsonld
- group: design
  href: https://artifacts.apis.io/volkswagen/vocabulary/volkswagen-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/volkswagen-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/volkswagen/rules/volkswagen-rules.yml
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
- has_sources: false
  method: generated
  name: Volkswagen Finops
  primary_unit: request
  service_category: API
  slug: volkswagen-finops
  template: true
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
modified: '2026-09-16'
name: Volkswagen
nav: Providers
network: true
overview: 'Volkswagen publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Catalog API, Configuration API, and Information API. Tagged areas include Automobiles, Cars, Vehicles, Automotive, and Vehicle Configuration.


  The Volkswagen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Volkswagen''s developer surface includes authentication, support, developer portal, engineering blog, and 20 more developer resources.'
plans:
- name: Volkswagen Plans Pricing
  plan_count: 3
  slug: volkswagen-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Volkswagen Rate Limits
  slug: volkswagen-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Volkswagen — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: volkswagen-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 49
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
  composite: 43.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.4
    catalog_earned_first_party: 0.0
    catalog_gap: 49.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 27.3
    contract_quality: 61.8
    developer_ergonomics: 51.2
    discoverability: 73.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/volkswagen/volkswagen-2026-06-20T201131.png
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
website: https://volkswagenag.com
---
