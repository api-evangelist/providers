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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Themeparks Wiki Agentic Access
  operation_count: 6
  slug: themeparks-wiki-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: Theme park resort destinations
  name: ThemeParks.wiki Destinations API
  slug: themeparks-wiki-destinations-api
- description: Park entities including rides, shows, restaurants, and parks
  name: ThemeParks.wiki Entities API
  slug: themeparks-wiki-entities-api
artifact_total: 57
collections:
- collection_type: open
  name: ThemeParks.wiki API
  slug: open-themeparks-wiki
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/themeparks-wiki-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/themeparks-wiki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://themeparks.wiki/
- group: docs
  title: ''
  type: Documentation
  url: https://api.themeparks.wiki/docs/v1/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThemeParks
- group: design
  title: ThemeParks.wiki Spectral Rules
  type: SpectralRules
  url: rules/themeparks-wiki-spectral-rules.yml
- group: design
  title: ThemeParks.wiki Vocabulary
  type: Vocabulary
  url: vocabulary/themeparks-wiki-vocabulary.yml
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: agent
  title: ''
  type: LlmsText
  url: https://themeparks.wiki/llms.txt
created: '2025-02-24'
description: An ever-growing database of real-time data for the world's best theme parks, including wait times, schedules, and park information.
examples:
- key_count: 4
  name: Themeparks Wiki Children Response Example
  slug: themeparks-wiki-children-response-example
- key_count: 5
  name: Themeparks Wiki Destination Example
  slug: themeparks-wiki-destination-example
- key_count: 1
  name: Themeparks Wiki Destinations Response Example
  slug: themeparks-wiki-destinations-response-example
- key_count: 6
  name: Themeparks Wiki Entity Example
  slug: themeparks-wiki-entity-example
- key_count: 4
  name: Themeparks Wiki Live Data Response Example
  slug: themeparks-wiki-live-data-response-example
- key_count: 7
  name: Themeparks Wiki Live Entity Data Example
  slug: themeparks-wiki-live-entity-data-example
- key_count: 2
  name: Themeparks Wiki Location Example
  slug: themeparks-wiki-location-example
- key_count: 2
  name: Themeparks Wiki Park Example
  slug: themeparks-wiki-park-example
- key_count: 1
  name: Themeparks Wiki Queue Data Example
  slug: themeparks-wiki-queue-data-example
- key_count: 5
  name: Themeparks Wiki Schedule Entry Example
  slug: themeparks-wiki-schedule-entry-example
- key_count: 4
  name: Themeparks Wiki Schedule Response Example
  slug: themeparks-wiki-schedule-response-example
features:
- description: Live queue wait times and operational status for attractions at 75+ destinations
  name: Real-Time Wait Times
- description: Operating hours, special event schedules, and monthly calendar views for parks
  name: Park Schedules
- description: Complete listing of all supported theme park resort destinations worldwide
  name: Destination Catalog
- description: Detailed information for parks, attractions, shows, and restaurants
  name: Entity Metadata
- description: Real-time OPERATING, DOWN, CLOSED, and REFURBISHMENT status for all entities
  name: Live Operational Status
- description: Historical and future operating schedules by specific month and year
  name: Monthly Schedule Lookup
finops:
- name: Themeparks Wiki Finops
  service_category: API
  slug: themeparks-wiki-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/themeparks-wiki.png
integrations:
- description: Community integrations for theme park data displays
  name: EmulationStation/RetroPie
- description: Smart home integrations for displaying live park data on dashboards
  name: Home Assistant
- description: Media center plugin integrations for theme park information
  name: Kodi
json_schemas:
- name: ChildrenResponse
  property_count: 4
  slug: themeparks-wiki-children-response
- name: Destination
  property_count: 5
  slug: themeparks-wiki-destination
- name: DestinationsResponse
  property_count: 1
  slug: themeparks-wiki-destinations-response
- name: Entity
  property_count: 7
  slug: themeparks-wiki-entity
- name: LiveDataResponse
  property_count: 4
  slug: themeparks-wiki-live-data-response
- name: LiveEntityData
  property_count: 7
  slug: themeparks-wiki-live-entity-data
- name: Location
  property_count: 2
  slug: themeparks-wiki-location
- name: Park
  property_count: 2
  slug: themeparks-wiki-park
- name: QueueData
  property_count: 1
  slug: themeparks-wiki-queue-data
- name: ScheduleEntry
  property_count: 5
  slug: themeparks-wiki-schedule-entry
- name: ScheduleResponse
  property_count: 4
  slug: themeparks-wiki-schedule-response
json_structures:
- name: Themeparks Wiki Children Response Structure
  property_count: 4
  slug: themeparks-wiki-children-response-structure
- name: Themeparks Wiki Destination Structure
  property_count: 5
  slug: themeparks-wiki-destination-structure
- name: Themeparks Wiki Destinations Response Structure
  property_count: 1
  slug: themeparks-wiki-destinations-response-structure
- name: Themeparks Wiki Entity Structure
  property_count: 7
  slug: themeparks-wiki-entity-structure
- name: Themeparks Wiki Live Data Response Structure
  property_count: 4
  slug: themeparks-wiki-live-data-response-structure
- name: Themeparks Wiki Live Entity Data Structure
  property_count: 7
  slug: themeparks-wiki-live-entity-data-structure
- name: Themeparks Wiki Location Structure
  property_count: 2
  slug: themeparks-wiki-location-structure
- name: Themeparks Wiki Park Structure
  property_count: 2
  slug: themeparks-wiki-park-structure
- name: Themeparks Wiki Queue Data Structure
  property_count: 1
  slug: themeparks-wiki-queue-data-structure
- name: Themeparks Wiki Schedule Entry Structure
  property_count: 5
  slug: themeparks-wiki-schedule-entry-structure
- name: Themeparks Wiki Schedule Response Structure
  property_count: 4
  slug: themeparks-wiki-schedule-response-structure
jsonld:
- class_count: 12
  name: Themeparks Wiki Context
  property_count: 32
  slug: themeparks-wiki-context
layout: provider
modified: '2026-05-19'
name: ThemeParks.wiki
nav: Providers
network: true
overview: 'ThemeParks.wiki publishes 2 APIs on the [APIs.io](https://apis.io/) network: Destinations API and Entities API. Tagged areas include Entertainment, Real-Time, Theme Parks, Wait Times, and Travel.


  The ThemeParks.wiki catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ThemeParks.wiki''s developer surface includes documentation, authentication, and 6 more developer resources.'
plans:
- name: Themeparks Wiki Plans Pricing
  plan_count: 3
  slug: themeparks-wiki-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Themeparks Wiki Rate Limits
  slug: themeparks-wiki-rate-limits
rules:
- name: ThemeParks.wiki API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: themeparks-wiki-jsonschema-spectral-rules
- name: ThemeParks.wiki API Rules
  rule_count: 27
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 15
  slug: themeparks-wiki-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: -7.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.6
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/themeparks-wiki/refs/heads/main/screenshots/themeparks-wiki-2026-06-20T195346.png
security:
- kind: domain-security
  name: Themeparks Wiki Domain Security
  slug: themeparks-wiki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: themeparks-wiki
tags:
- Entertainment
- Real-Time
- Theme Parks
- Wait Times
- Travel
use_cases:
- description: Research park schedules and wait time patterns before visiting
  name: Trip Planning
- description: Monitor live wait times and attraction availability during a park visit
  name: Real-Time Monitoring
- description: Power home media center displays with live park data and wait times
  name: Media Centers
- description: Power AI agents that help users plan and navigate theme park visits
  name: AI Park Assistant
website: https://themeparks.wiki/
---
