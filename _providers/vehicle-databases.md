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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Vehicle Databases Agentic Access
  operation_count: 6
  slug: vehicle-databases-agentic-access
  summary_line: 6 operations
api_count: 5
apis:
- description: OEM maintenance schedules and service intervals
  name: Vehicle Databases Maintenance API
  slug: vehicle-databases-maintenance-api
- description: NHTSA safety recall data
  name: Vehicle Databases Recalls API
  slug: vehicle-databases-recalls-api
- description: Service items, fluids, and parts
  name: Vehicle Databases Services API
  slug: vehicle-databases-services-api
- description: Technical service bulletins
  name: Vehicle Databases TSBs API
  slug: vehicle-databases-tsbs-api
- description: Vehicle lookup and VIN decoding
  name: Vehicle Databases Vehicles API
  slug: vehicle-databases-vehicles-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vehicle Databases Maintenance API
  slug: open-vehicle-databases-maintenance-api
- collection_type: open
  name: Vehicle Databases Maintenance Recalls API
  slug: open-vehicle-databases-recalls-api
- collection_type: open
  name: Vehicle Databases Maintenance Services API
  slug: open-vehicle-databases-services-api
- collection_type: open
  name: Vehicle Databases Maintenance TSBs API
  slug: open-vehicle-databases-tsbs-api
- collection_type: open
  name: Vehicle Databases Maintenance Vehicles API
  slug: open-vehicle-databases-vehicles-api
- collection_type: open
  name: Vehicle Databases Maintenance API
  slug: open-vehicle-databases
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vehicle-databases-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vehicle-databases-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vehicle-databases-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vehicledatabases.com/
- group: start
  title: ''
  type: Portal
  url: https://vehicledatabases.com/
- group: docs
  title: ''
  type: Documentation
  url: https://vehicledatabases.com/vehicle-maintenance-api
- group: commercial
  title: ''
  type: Pricing
  url: https://vehicledatabases.com/pricing
- group: design
  title: ''
  type: SpectralRules
  url: rules/vehicle-databases-spectral-rules.yml
- group: company
  title: Vehicle Databases Spectral Rules
  type: Blog
  url: https://vehicledatabases.com/feed/
- group: design
  title: Vehicle Databases Vocabulary
  type: Vocabulary
  url: vocabulary/vehicle-databases-vocabulary.yml
created: '2025-02-12'
description: Vehicle Databases provides automotive maintenance schedule APIs with OEM-compliant service schedules for vehicles up to 200,000 miles. Delivers maintenance intervals, service items, fluids, and recall data for automotive service platforms, fleet management systems, and consumer maintenance reminder applications.
examples:
- key_count: 4
  name: Vehicle Databases Maintenance Interval Example
  slug: vehicle-databases-maintenance-interval-example
- key_count: 5
  name: Vehicle Databases Maintenance Schedule Example
  slug: vehicle-databases-maintenance-schedule-example
- key_count: 7
  name: Vehicle Databases Recall Example
  slug: vehicle-databases-recall-example
- key_count: 9
  name: Vehicle Databases Service Item Example
  slug: vehicle-databases-service-item-example
- key_count: 6
  name: Vehicle Databases Tsb Example
  slug: vehicle-databases-tsb-example
- key_count: 10
  name: Vehicle Databases Vehicle Detail Example
  slug: vehicle-databases-vehicle-detail-example
features:
- description: Factory maintenance schedules matching OEM specifications for vehicles up to 200,000 miles with mileage and time-based service intervals.
  name: OEM-Compliant Maintenance Schedules
- description: Detailed service item data including fluid specifications, part numbers, labor time estimates, and OEM-required procedures for each service.
  name: Service Item Details
- description: Decode 17-character VINs to extract make, model, year, engine, trim, and manufacturing details for vehicle identification.
  name: VIN Decoder
- description: NHTSA recall information linked to specific vehicles including recall dates, component affected, risk description, and remedy status.
  name: Recall Data
- description: OEM technical service bulletins (TSBs) for specific vehicle issues including symptom description, diagnosis, and corrective action.
  name: Technical Service Bulletins
finops:
- name: Vehicle Databases Finops
  service_category: API
  slug: vehicle-databases-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vehicle-databases.png
json_schemas:
- name: MaintenanceInterval
  property_count: 4
  slug: vehicle-databases-maintenance-interval
- name: MaintenanceSchedule
  property_count: 5
  slug: vehicle-databases-maintenance-schedule
- name: Recall
  property_count: 7
  slug: vehicle-databases-recall
- name: ServiceItem
  property_count: 9
  slug: vehicle-databases-service-item
- name: TSB
  property_count: 6
  slug: vehicle-databases-tsb
- name: VehicleDetail
  property_count: 12
  slug: vehicle-databases-vehicle-detail
json_structures:
- name: Vehicle Databases Maintenance Interval Structure
  property_count: 4
  slug: vehicle-databases-maintenance-interval-structure
- name: Vehicle Databases Maintenance Schedule Structure
  property_count: 5
  slug: vehicle-databases-maintenance-schedule-structure
- name: Vehicle Databases Recall Structure
  property_count: 7
  slug: vehicle-databases-recall-structure
- name: Vehicle Databases Service Item Structure
  property_count: 9
  slug: vehicle-databases-service-item-structure
- name: Vehicle Databases Tsb Structure
  property_count: 6
  slug: vehicle-databases-tsb-structure
- name: Vehicle Databases Vehicle Detail Structure
  property_count: 12
  slug: vehicle-databases-vehicle-detail-structure
layout: provider
modified: '2026-05-19'
name: Vehicle Databases
nav: Providers
network: true
overview: 'Vehicle Databases publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Maintenance API, Recalls API, Services API, and 2 more. Tagged areas include Automotive, Fleet Management, Maintenance, Recalls, and Vehicles.


  The Vehicle Databases catalog on APIs.io includes 2 Spectral governance rulesets.


  Vehicle Databases'' developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Vehicle Databases Plans Pricing
  plan_count: 3
  slug: vehicle-databases-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 5
  name: Vehicle Databases Rate Limits
  slug: vehicle-databases-rate-limits
rules:
- name: Vehicle Databases API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vehicle-databases-jsonschema-spectral-rules
- name: Vehicle Databases API Rules
  rule_count: 27
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 15
  slug: vehicle-databases-spectral-rules
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 23.9
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 7.9
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vehicle-databases/refs/heads/main/screenshots/vehicle-databases-2026-06-20T200859.png
security:
- kind: authentication
  name: Vehicle Databases Authentication
  slug: vehicle-databases-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vehicle Databases Domain Security
  slug: vehicle-databases-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vehicle-databases
tags:
- Automotive
- Fleet Management
- Maintenance
- Recalls
- Vehicles
use_cases:
- description: Automate maintenance scheduling for commercial and enterprise fleets using OEM-compliant service intervals and mileage-based triggers.
  name: Fleet Maintenance Management
- description: Integrate maintenance schedules and TSBs into shop management systems to provide accurate service recommendations and labor estimates.
  name: Auto Repair Shop Management
- description: Power maintenance reminder apps and connected car services with personalized OEM service schedules based on vehicle and mileage.
  name: Consumer Maintenance Reminders
- description: Combine telematics mileage data with maintenance schedules to provide proactive service alerts in usage-based insurance applications.
  name: Insurance Telematics
website: https://vehicledatabases.com/
---
