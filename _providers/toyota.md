---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
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
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Climate control management
  name: Toyota Climate API
  slug: toyota-climate-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Electric and hybrid vehicle battery data
  name: Toyota Electric API
  slug: toyota-electric-api
- baseURL: https://api.eig.toyota.com/telematics/v1
  baseurl_source: spec
  description: Fleet vehicle management operations
  name: Toyota Fleet API
  slug: toyota-fleet-api
- baseURL: https://api.eig.toyota.com/telematics/v1
  baseurl_source: spec
  description: Vehicle health and diagnostics
  name: Toyota Health API
  slug: toyota-health-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Service history
  name: Toyota History API
  slug: toyota-history-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Vehicle location services
  name: Toyota Location API
  slug: toyota-location-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Vehicle notification management
  name: Toyota Notifications API
  slug: toyota-notifications-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Remote vehicle commands
  name: Toyota Remote API
  slug: toyota-remote-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Vehicle status and diagnostics
  name: Toyota Status API
  slug: toyota-status-api
- baseURL: https://api.eig.toyota.com/telematics/v1
  baseurl_source: spec
  description: Connected service and satellite radio subscriptions
  name: Toyota Subscriptions API
  slug: toyota-subscriptions-api
- baseURL: https://api.eig.toyota.com/telematics/v1
  baseurl_source: spec
  description: Real-time vehicle telemetry data
  name: Toyota Telemetry API
  slug: toyota-telemetry-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Trip history and driving data
  name: Toyota Trips API
  slug: toyota-trips-api
- baseURL: https://api.toyota.com/connected/v1
  baseurl_source: spec
  description: Vehicle registration and management
  name: Toyota Vehicles API
  slug: toyota-vehicles-api
artifact_total: 44
collections:
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
- group: commercial
  href: https://artifacts.apis.io/toyota/plans/toyota-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/toyota-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/toyota/rate-limits/toyota-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/toyota-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/toyota/finops/toyota-finops.yml
  title: ''
  type: FinOps
  url: finops/toyota-finops.yml
- group: other
  href: https://artifacts.apis.io/toyota/capabilities/toyota-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/toyota-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/toyota/agentic-access/toyota-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/toyota-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/toyota/security/toyota-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/toyota-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/toyota/security/toyota-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toyota-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/toyota/authentication/toyota-authentication.yml
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
  href: https://artifacts.apis.io/toyota/rules/toyota-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/toyota-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/toyota/vocabulary/toyota-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/toyota-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/toyota/json-ld/toyota-context.jsonld
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
- has_sources: true
  method: generated
  name: Toyota Finops
  primary_unit: ''
  service_category: Connected Vehicle / Telematics
  slug: toyota-finops
  template: false
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
overview: 'Toyota publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Climate API, Electric API, Fleet API, and 11 more. Tagged areas include Automobiles, Cars, Vehicles, Connected Vehicles, and Telematics.


  The Toyota catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Toyota''s developer surface includes authentication, documentation, engineering blog, and 14 more developer resources.'
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
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Toyota — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: toyota-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 59
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
  composite: 31.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 53.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 27.3
    contract_quality: 54.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 69.2
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/toyota/toyota-2026-10-11T131125.png
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
- Connected Vehicles
- Telematics
- Fleet Management
- Electric Vehicles
website: https://developer.eig.toyota.com/
---
