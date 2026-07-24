---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tier Mobility Agentic Access
  operation_count: 9
  slug: tier-mobility-agentic-access
  summary_line: 9 operations
api_count: 5
apis:
- description: GBFS discovery and versioning
  name: TIER Discovery API
  slug: tier-mobility-discovery-api
- description: Station information and availability
  name: TIER Stations API
  slug: tier-mobility-stations-api
- description: System-level metadata and pricing
  name: TIER System API
  slug: tier-mobility-system-api
- description: Vehicle inventory, types, and real-time status
  name: TIER Vehicles API
  slug: tier-mobility-vehicles-api
- description: Geofencing rules and operational zones
  name: TIER Zones API
  slug: tier-mobility-zones-api
artifact_total: 31
collections:
- collection_type: open
  name: TIER / Dott GBFS API
  slug: open-tier-mobility-gbfs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tier-mobility-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tier-mobility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ridedott.com/
- group: other
  title: ''
  type: Company
  url: https://ridedott.com/about
- group: company
  title: ''
  type: Newsroom
  url: https://ridedott.com/press
- group: company
  title: ''
  type: Careers
  url: https://ridedott.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridedott.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridedott.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.ridedott.com/
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/app/id1440301673
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.ridedott.rider
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ridedott
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ridedott
- group: other
  title: ''
  type: Standards
  url: https://github.com/MobilityData/gbfs
- group: company
  title: ''
  type: Blog
  url: https://ridedott.com/feed
- group: other
  title: ''
  type: GBFS
  url: https://gbfs.api.ridedott.com/public/v2/gbfs_versions.json
- group: start
  title: ''
  type: SystemsRegistry
  url: https://github.com/MobilityData/gbfs/blob/master/systems.csv
created: '2026-05-25'
description: TIER Mobility was a Berlin-headquartered shared electric micromobility operator founded in 2018 by Lawrence Leuschner, Julian Blessin, and Matthias Laug, providing e-scooter, e-bike, and e-moped sharing across European and Middle Eastern cities. In March 2024, TIER merged with Amsterdam-based Dott to form the combined European micromobility champion that now trades under the Dott brand on ridedott.com, operating in 400+ cities across roughly 22 countries including Germany, France, the United Kingdom, Italy, Spain, the Netherlands, Belgium, Sweden, Norway, Finland, Denmark, Austria, Switzerland, Poland, Greece, Hungary, Israel, Saudi Arabia, Qatar, and the UAE. All public real-time data — fleet positions, battery levels, vehicle types, pricing plans, stations, and geofencing zones — is published via GBFS 2.3 (General Bikeshare Feed Specification) endpoints at https://gbfs.api.ridedott.com/public/v2/{system_id}/, with one `system_id` per city. There is no consumer authentication
  or paid API tier; feeds are open data consumed by city regulators, MaaS aggregators, and trip-planning apps.
examples:
- key_count: 4
  name: Tier Mobility Free Bike Status Example
  slug: tier-mobility-free-bike-status-example
- key_count: 4
  name: Tier Mobility Gbfs Discovery Example
  slug: tier-mobility-gbfs-discovery-example
- key_count: 4
  name: Tier Mobility Pricing Plans Example
  slug: tier-mobility-pricing-plans-example
- key_count: 4
  name: Tier Mobility Vehicle Types Example
  slug: tier-mobility-vehicle-types-example
features:
- GBFS 2.3 feeds for 340+ Dott (formerly TIER) systems across Europe, the Middle East, and the Gulf
- Real-time free-floating e-scooter and e-bike fleet positions
- Battery level and remaining range per vehicle
- Per-city, per-vehicle-type pricing plans (unlock + per-minute)
- Geofencing zones with ride / park / speed rules
- Station information and status (in dock-based markets)
- Vehicle type catalogue (`dott_scooter`, `dott_bicycle`)
- Rental deep-link URIs (Android, iOS) for unlock flows
- Multilingual rider apps (16+ languages)
- Open, unauthenticated public data — no API key required
- Merger note: TIER + Dott (2024) — all feeds unified under ridedott.com
finops:
- name: Tier Mobility Finops
  service_category: ''
  slug: tier-mobility-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tier-mobility.png
json_schemas:
- name: TIER/Dott Pricing Plan
  property_count: 7
  slug: tier-mobility-pricing-plan
- name: TIER/Dott Vehicle
  property_count: 11
  slug: tier-mobility-vehicle
jsonld:
- class_count: 16
  name: Tier Mobility Context
  property_count: 6
  slug: tier-mobility-context
layout: provider
modified: '2026-05-25'
name: TIER
nav: Providers
network: true
overview: 'TIER publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Stations API, System API, and 2 more. Tagged areas include Mobility, Micromobility, Shared Mobility, E-Scooter, and E-Bike.


  The TIER catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TIER''s developer surface includes support, engineering blog, and 15 more developer resources.'
plans:
- name: Tier Mobility Plans Pricing
  plan_count: 2
  slug: tier-mobility-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Tier Mobility Rate Limits
  slug: tier-mobility-rate-limits
rules:
- name: TIER API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tier-mobility-jsonschema-spectral-rules
- name: TIER API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: tier-mobility-rules
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.3
    developer_ergonomics: 6.5
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 41.7
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 41.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tier-mobility/refs/heads/main/screenshots/tier-mobility-2026-06-20T195343.png
security:
- kind: domain-security
  name: Tier Mobility Domain Security
  slug: tier-mobility-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tier-mobility
tags:
- Mobility
- Micromobility
- Shared Mobility
- E-Scooter
- E-Bike
- Transportation
- Smart Cities
- MaaS
- GBFS
- Open Data
- Europe
- Real-Time
website: https://ridedott.com/
---
