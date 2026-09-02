---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Toyota Agentic Access
  operation_count: 25
  slug: toyota-agentic-access
  summary_line: 25 operations · 7 acting
api_count: 2
apis:
- description: Toyota Dealers API enables searching and retrieving dealer information including location, hours, services offered, and inventory. Supports dealer locator applications and service scheduling integrati
  name: Toyota Dealers API
  slug: toyota-dealers
- description: Climate control management
  name: Toyota Climate API
  slug: toyota-climate-api
- description: Electric and hybrid vehicle battery data
  name: Toyota Electric API
  slug: toyota-electric-api
- description: Fleet vehicle management operations
  name: Toyota Fleet API
  slug: toyota-fleet-api
- description: Vehicle health and diagnostics
  name: Toyota Health API
  slug: toyota-health-api
- description: Service history
  name: Toyota History API
  slug: toyota-history-api
- description: Vehicle location services
  name: Toyota Location API
  slug: toyota-location-api
- description: Vehicle notification management
  name: Toyota Notifications API
  slug: toyota-notifications-api
- description: Remote vehicle commands
  name: Toyota Remote API
  slug: toyota-remote-api
- description: Vehicle status and diagnostics
  name: Toyota Status API
  slug: toyota-status-api
- description: Connected service and satellite radio subscriptions
  name: Toyota Subscriptions API
  slug: toyota-subscriptions-api
- description: Real-time vehicle telemetry data
  name: Toyota Telemetry API
  slug: toyota-telemetry-api
- description: Trip history and driving data
  name: Toyota Trips API
  slug: toyota-trips-api
- description: Vehicle registration and management
  name: Toyota Vehicles API
  slug: toyota-vehicles-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Toyota Connected Services Climate API
  slug: open-toyota-climate-api
- collection_type: open
  name: Toyota Connected Services API
  slug: open-toyota-connected-services
- collection_type: open
  name: Toyota Connected Services Climate Electric API
  slug: open-toyota-electric-api
- collection_type: open
  name: Toyota Connected Services Climate Fleet API
  slug: open-toyota-fleet-api
- collection_type: open
  name: Toyota Connected Services Climate Health API
  slug: open-toyota-health-api
- collection_type: open
  name: Toyota Connected Services Climate History API
  slug: open-toyota-history-api
- collection_type: open
  name: Toyota Connected Services Climate Location API
  slug: open-toyota-location-api
- collection_type: open
  name: Toyota Connected Services Climate Notifications API
  slug: open-toyota-notifications-api
- collection_type: open
  name: Toyota Connected Services Climate Remote API
  slug: open-toyota-remote-api
- collection_type: open
  name: Toyota Connected Services Climate Status API
  slug: open-toyota-status-api
- collection_type: open
  name: Toyota Connected Services Climate Subscriptions API
  slug: open-toyota-subscriptions-api
- collection_type: open
  name: Toyota Telematics API
  slug: open-toyota-telematics
- collection_type: open
  name: Toyota Connected Services Climate Telemetry API
  slug: open-toyota-telemetry-api
- collection_type: open
  name: Toyota Connected Services Climate Trips API
  slug: open-toyota-trips-api
- collection_type: open
  name: Toyota Connected Services Climate Vehicles API
  slug: open-toyota-vehicles-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/toyota-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toyota-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/toyota-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toyota-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toyota-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TOYOTA
- group: company
  title: ''
  type: Website
  url: https://developer.eig.toyota.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.eig.toyota.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eig.toyota.com/apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toyota-motor-corporation
- group: design
  title: ''
  type: Rules
  url: rules/toyota-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/toyota-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/toyota-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://pressroom.toyota.com/feed/
created: '2025-02-25'
description: Toyota Motor Corporation is a Japanese multinational automotive manufacturer that designs, manufactures, and sells vehicles, including cars, trucks, and buses. Founded in 1937, Toyota has become one of the largest automakers in the world, known for its reliability, innovation, and commitment to sustainability. Toyota's developer platform (developer.eig.toyota.com) provides APIs for vehicle lifecycle management, telematics and connected services, dealer data, and fleet management for business partners, dealers, fleet operators, and developers building mobility applications. Toyota's product lineup includes hybrids like the Prius, trucks like the Tacoma, and EVs including the bZ4X.
examples:
- key_count: 2
  name: Toyota Get Electric Status Example
  slug: toyota-get-electric-status-example
- key_count: 2
  name: Toyota Send Remote Command Example
  slug: toyota-send-remote-command-example
finops:
- name: Toyota Finops
  service_category: Connected Vehicle / Telematics
  slug: toyota-finops
graphqls:
- description: This conceptual GraphQL schema represents the Toyota Motor connected vehicle and telematics API surface, covering the Toyota Developer Portal (developer.eig.toyota.com). It unifies the Vehicle, Telema
  name: Toyota Motor GraphQL Schema
  slug: toyota-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toyota.png
json_schemas:
- name: Toyota Electric Status
  property_count: 10
  slug: toyota-electric-status
- name: Toyota Vehicle
  property_count: 10
  slug: toyota-vehicle
json_structures:
- name: Toyota Vehicle Structure
  property_count: 0
  slug: toyota-vehicle-structure
jsonld:
- class_count: 58
  name: Toyota Context
  property_count: 0
  slug: toyota-context
layout: provider
modified: '2026-05-19'
name: Toyota
nav: Providers
network: true
overview: 'Toyota publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Climate API, Electric API, Fleet API, and 10 more. Tagged areas include Automobiles, Cars, Vehicles, Connected Car, and Telematics.


  The Toyota catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Toyota''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Toyota Plans Pricing
  plan_count: 1
  slug: toyota-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Toyota Rate Limits
  slug: toyota-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Toyota API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: toyota-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Toyota API Rules
  rule_count: 18
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 12
  slug: toyota-spectral-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 65.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Toyota Authentication
  slug: toyota-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Toyota Domain Security
  slug: toyota-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Toyota Vulnerability Disclosure
  slug: toyota-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: toyota
tags:
- Automobiles
- Cars
- Vehicles
- Connected Car
- Telematics
- Fleet Management
- Electric Vehicles
website: https://developer.eig.toyota.com/
---
