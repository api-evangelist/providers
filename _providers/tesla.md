---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 54
  human_in_the_loop: 14
  name: Tesla Agentic Access
  operation_count: 65
  slug: tesla-agentic-access
  summary_line: 65 operations · 54 acting · 14 human-in-the-loop
api_count: 1
apis:
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: The Authentication API from Tesla — 1 operation(s) for authentication.
  name: Tesla Authentication API
  slug: tesla-authentication-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: The Media Control API from Tesla — 8 operation(s) for media control.
  name: Tesla Media Control API
  slug: tesla-media-control-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: The Vehicle Commands API from Tesla — 45 operation(s) for vehicle commands.
  name: Tesla Vehicle Commands API
  slug: tesla-vehicle-commands-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: The Vehicles API from Tesla — 11 operation(s) for vehicles.
  name: Tesla Vehicles API
  slug: tesla-vehicles-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tesla Authentication API
  slug: open-tesla-authentication-api
- collection_type: open
  name: Tesla Authentication Media Control API
  slug: open-tesla-media-control-api
- collection_type: open
  name: Tesla Authentication Vehicle Commands API
  slug: open-tesla-vehicle-commands-api
- collection_type: open
  name: Tesla Authentication Vehicles API
  slug: open-tesla-vehicles-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tesla-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/timdorr/tesla-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/timdorr/tesla-api/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/timdorr/tesla-api/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tesla-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tesla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tesla-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tesla-motors
- group: start
  title: ''
  type: Portal
  url: https://developer.tesla.com/
- group: other
  title: ''
  type: Announcements
  url: https://developer.tesla.com/docs/fleet-api/announcements
- group: operate
  title: ''
  type: FAQ
  url: https://developer.tesla.com/docs/fleet-api/support/faq
- group: operate
  title: ''
  type: Contact
  url: https://developer.tesla.com/docs/fleet-api/support/contact
- group: other
  title: ''
  type: Repository
  url: https://github.com/teslamotors
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tdorssers/TeslaPy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/timdorr/tesla-api
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/781424/2s9YRCWB4f
- group: agent
  title: ''
  type: LlmsText
  url: https://tesla-api.timdorr.com/llms.txt
created: '2025-02-25'
description: Tesla, Inc. is an American electric vehicle and clean energy company founded in 2003. Tesla offers the Fleet API for partners to access Tesla vehicles and energy devices with owner-granted permissions, covering vehicle telemetry, remote commands, charging management, energy site management, and fleet management capabilities.
examples:
- key_count: 2
  name: Tesla List Vehicles Example
  slug: tesla-list-vehicles-example
finops:
- name: Tesla Finops
  service_category: API
  slug: tesla-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Tesla Fleet API and Owner API. Tesla does not publish an official GraphQL endpoint, but this schema models the domain objects and operations
  name: Tesla GraphQL Schema
  slug: tesla-graphql
json_schemas:
- name: Tesla Vehicle
  property_count: 10
  slug: tesla-vehicle
json_structures:
- name: Tesla Vehicle State Structure
  property_count: 0
  slug: tesla-vehicle-state-structure
jsonld:
- class_count: 30
  name: Tesla Context
  property_count: 0
  slug: tesla-context
layout: provider
modified: '2026-05-19'
name: Tesla
nav: Providers
network: true
overview: 'Tesla publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Media Control API, Vehicle Commands API, and 1 more. Tagged areas include Automobiles, Cars, Vehicles, Electric Vehicles, and Energy.


  The Tesla catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tesla''s developer surface includes developer portal, FAQ, and 16 more developer resources.'
plans:
- name: Tesla Plans Pricing
  plan_count: 3
  slug: tesla-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Tesla Rate Limits
  slug: tesla-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tesla API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tesla-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Tesla API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 5
  slug: tesla-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 55.2
    developer_ergonomics: 42.9
    discoverability: 79.6
    governance: 13.6
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 31.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Tesla Domain Security
  slug: tesla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tesla Vulnerability Disclosure
  slug: tesla-vulnerability-disclosure
  summary_line: disclosure policy published
slug: tesla
tags:
- Automobiles
- Cars
- Vehicles
- Electric Vehicles
- Energy
- Clean Energy
- IoT
website: https://www.tesla.com
---
