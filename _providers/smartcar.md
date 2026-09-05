---
access_model:
  confidence: medium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Smartcar Agentic Access
  operation_count: 21
  slug: smartcar-agentic-access
  summary_line: 21 operations · 7 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://vehicle.api.smartcar.com/v2.0
  baseurl_source: spec
  description: EV charging management and status
  name: Smartcar Charging API
  slug: smartcar-charging-api
- baseURL: https://vehicle.api.smartcar.com/v2.0
  baseurl_source: spec
  description: Manage vehicle connections and user authorizations
  name: Smartcar Connections API
  slug: smartcar-connections-api
- baseURL: https://vehicle.api.smartcar.com/v2.0
  baseurl_source: spec
  description: Vehicle navigation and destination setting
  name: Smartcar Navigation API
  slug: smartcar-navigation-api
- baseURL: https://vehicle.api.smartcar.com/v2.0
  baseurl_source: spec
  description: Vehicle security, locking and unlocking
  name: Smartcar Security API
  slug: smartcar-security-api
- baseURL: https://vehicle.api.smartcar.com/v2.0
  baseurl_source: spec
  description: Read vehicle signals and status data
  name: Smartcar Vehicle Data API
  slug: smartcar-vehicle-data-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smartcar Vehicles Charging API
  slug: open-smartcar-charging-api
- collection_type: open
  name: Smartcar Vehicles Charging Connections API
  slug: open-smartcar-connections-api
- collection_type: open
  name: Smartcar Vehicles Charging Navigation API
  slug: open-smartcar-navigation-api
- collection_type: open
  name: Smartcar Vehicles Charging Security API
  slug: open-smartcar-security-api
- collection_type: open
  name: Smartcar Vehicles Charging Vehicle Data API
  slug: open-smartcar-vehicle-data-api
- collection_type: open
  name: Smartcar Vehicles API
  slug: open-smartcar-vehicles
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/smartcar-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartcar-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smartcar-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartcar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartcar-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartcar
- group: start
  title: ''
  type: Portal
  url: https://smartcar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://smartcar.com/docs/api/
- group: company
  title: ''
  type: Website
  url: https://smartcar.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartcar
- group: commercial
  title: ''
  type: Pricing
  url: https://smartcar.com/pricing/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/smartcar-vehicles-openapi.yml
- group: design
  title: ''
  type: Spectral
  url: rules/smartcar-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/smartcar-vehicle-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/smartcar-battery-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/smartcar-vehicles-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/smartcar-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/smartcar-vocabulary.yml
created: '2026-03-16'
description: Smartcar is a connected vehicle platform that provides a standardized REST API for accessing vehicle data and sending commands to connected cars. The API enables developers to retrieve battery levels, odometer readings, location, lock/unlock doors, start/stop charging, and access vehicle attributes across multiple vehicle brands through a single integration. Smartcar supports OAuth 2.0 authorization and covers EVs and ICE vehicles from dozens of OEMs including Tesla, Ford, BMW, Honda, and more.
examples:
- key_count: 2
  name: Smartcar Get Battery Level Example
  slug: smartcar-get-battery-level-example
- key_count: 2
  name: Smartcar Get Vehicle Example
  slug: smartcar-get-vehicle-example
- key_count: 2
  name: Smartcar Lock Vehicle Example
  slug: smartcar-lock-vehicle-example
finops:
- name: Smartcar Finops
  service_category: API
  slug: smartcar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartcar.png
json_schemas:
- name: Smartcar Battery
  property_count: 2
  slug: smartcar-battery
- name: Smartcar Vehicle
  property_count: 5
  slug: smartcar-vehicle
json_structures:
- name: Smartcar Vehicles Structure
  property_count: 0
  slug: smartcar-vehicles-structure
jsonld:
- class_count: 13
  name: Smartcar Context
  property_count: 11
  slug: smartcar-context
layout: provider
modified: '2026-05-19'
name: Smartcar
nav: Providers
network: true
overview: 'Smartcar publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Charging API, Connections API, Navigation API, and 2 more. Tagged areas include Automotive, Connected Vehicles, IoT, Mobility, and Fleet Management.


  The Smartcar catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Smartcar''s developer surface includes authentication, developer portal, documentation, pricing, and 14 more developer resources.'
plans:
- name: Smartcar Plans Pricing
  plan_count: 3
  slug: smartcar-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Smartcar Rate Limits
  slug: smartcar-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Smartcar API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: smartcar-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Smartcar API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 4
  slug: smartcar-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 28.8
    contract_quality: 61.5
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartcar/refs/heads/main/screenshots/smartcar-2026-06-20T194039.png
security:
- kind: authentication
  name: Smartcar Authentication
  slug: smartcar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smartcar Domain Security
  slug: smartcar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Smartcar Trust Center
  slug: smartcar-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: smartcar
tags:
- Automotive
- Connected Vehicles
- IoT
- Mobility
- Fleet Management
- EV Management
- Telematics
website: https://smartcar.com/
---
