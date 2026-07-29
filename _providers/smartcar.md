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
- acting_count: 7
  human_in_the_loop: 2
  name: Smartcar Agentic Access
  operation_count: 21
  slug: smartcar-agentic-access
  summary_line: 21 operations · 7 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: EV charging management and status
  name: Smartcar Charging API
  slug: smartcar-charging-api
- description: Manage vehicle connections and user authorizations
  name: Smartcar Connections API
  slug: smartcar-connections-api
- description: Vehicle navigation and destination setting
  name: Smartcar Navigation API
  slug: smartcar-navigation-api
- description: Vehicle security, locking and unlocking
  name: Smartcar Security API
  slug: smartcar-security-api
- description: Read vehicle signals and status data
  name: Smartcar Vehicle Data API
  slug: smartcar-vehicle-data-api
artifact_total: 22
collections:
- collection_type: open
  name: Smartcar Vehicles API
  slug: open-smartcar-vehicles
common:
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
  url: openapi/smartcar-vehicles-openapi.yml
- group: design
  title: ''
  type: Spectral
  url: rules/smartcar-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/connected-vehicle-management.yaml
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
random_paper: 14
rate_limits:
- limit_count: 5
  name: Smartcar Rate Limits
  slug: smartcar-rate-limits
rules:
- name: Smartcar API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: smartcar-jsonschema-spectral-rules
- name: Smartcar API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 4
  slug: smartcar-rules
score:
  band: developing
  composite: 53.5
  delta: -4.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.8
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 57.5
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
