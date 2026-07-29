---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bird Rides Agentic Access
  operation_count: 10
  slug: bird-rides-agentic-access
  summary_line: 10 operations
api_count: 10
apis:
- description: Credentialed city / municipal data portal at https://city-data.bird.co providing partner cities with access to fleet, trip, and operational data feeds beyond the public GBFS surface. Access is granted
  name: Bird City Data Portal
  slug: bird-city-data-portal
- description: Bird Platform is the white-label fleet operator program that lets independent local operators run a Bird-branded e-scooter service in their own market using Bird vehicles, the Bird consumer app, and a
  name: Bird Platform (Fleet Operator)
  slug: bird-platform-operator
- description: 'The undocumented mobile-app backend that powers the Bird iOS and Android consumer apps. Hosts include api.birdapp.com, api-auth.prod.birdapp.com, and api-bird.prod.birdapp.com. The surface is email + '
  name: Bird Mobile App Backend (Unofficial)
  slug: bird-mobile-app-api
- description: GBFS auto-discovery and version metadata
  name: Bird Discovery API
  slug: bird-rides-discovery-api
- description: No-ride / no-parking polygon zones
  name: Bird Geofencing API
  slug: bird-rides-geofencing-api
- description: Rider-facing pricing plans
  name: Bird Pricing API
  slug: bird-rides-pricing-api
- description: Real-time feeds with 60-second TTL
  name: Bird Realtime API
  slug: bird-rides-realtime-api
- description: Docking-station information (mostly empty for free-floating Bird markets)
  name: Bird Stations API
  slug: bird-rides-stations-api
- description: System-level information and regions
  name: Bird System API
  slug: bird-rides-system-api
- description: Vehicle inventory and real-time availability
  name: Bird Vehicles API
  slug: bird-rides-vehicles-api
artifact_total: 38
collections:
- collection_type: open
  name: Bird GBFS Feed
  slug: open-bird-gbfs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bird-rides-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bird-rides-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bird.co
- group: other
  title: ''
  type: Product
  url: https://three.bird.co
- group: other
  title: ''
  type: Product
  url: https://bikeshare.bird.co
- group: docs
  title: ''
  type: Documentation
  url: https://www.bird.co/how
- group: other
  title: ''
  type: Map
  url: https://www.bird.co/map
- group: other
  title: ''
  type: Safety
  url: https://www.bird.co/safety
- group: other
  title: ''
  type: Sustainability
  url: https://www.bird.co/sustainability
- group: operate
  title: ''
  type: Support
  url: https://help.bird.co
- group: other
  title: ''
  type: Cities
  url: https://www.bird.co/cities
- group: other
  title: ''
  type: Platform
  url: https://www.bird.co/platform
- group: other
  title: ''
  type: FleetManager
  url: https://www.bird.co/us-fm
- group: company
  title: ''
  type: OperatorPartner
  url: https://www.bird.co/us-op
- group: company
  title: ''
  type: About
  url: https://www.bird.co/about
- group: company
  title: ''
  type: Careers
  url: https://www.bird.co/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.bird.co/contact-us
- group: company
  title: ''
  type: Press
  url: https://www.bird.co/press
- group: company
  title: ''
  type: Blog
  url: https://www.bird.co/blog
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.bird.co
- group: commercial
  title: ''
  type: Terms
  url: https://www.bird.co/terms
- group: commercial
  title: ''
  type: Privacy
  url: https://www.bird.co/privacy
- group: commercial
  title: ''
  type: License
  url: https://www.bird.co/wp-content/uploads/2019/03/GBFS-Data-License-Agreement-2018-09-25.pdf
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/us/app/bird-be-free-enjoy-the-ride/id1260842311
- group: other
  title: ''
  type: PlayStore
  url: https://play.google.com/store/apps/details?id=co.bird.android
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/birdrides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thirdlanemobility
- group: other
  title: ''
  type: ParentCompany
  url: https://www.thirdlanemobility.com
- group: other
  title: ''
  type: SisterBrand
  url: https://www.spin.app
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/birdride
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/bird
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bird-rides
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Bird_Global
- group: commercial
  title: ''
  type: Plans
  url: plans/bird-rides-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bird-rides-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bird-rides-finops.yml
created: '2026-05-25'
description: Bird is a shared electric scooter and bike micromobility operator headquartered in Miami, Florida and operating as the global anchor brand of Third Lane Mobility, Inc. Founded in 2017 by Travis VanderZanden, Bird pioneered the dockless electric scooter category in Santa Monica, California and rapidly expanded to hundreds of cities across North America, Europe, and the Middle East. After overstating revenue, delisting from the NYSE in September 2023 (ticker BRDS), and filing Chapter 11 bankruptcy in December 2023, Bird emerged in April 2024 under the new private parent company Third Lane Mobility, Inc., which also owns the Spin brand acquired from TIER in September 2023. Bird operates the Bird Three e-scooter and a Bird Bikeshare service, plus the Bird Platform white-label program for independent fleet operators and a Cities partner program that ships "in-depth APIs" and operator dashboards to municipal partners. Bird publishes public General Bikeshare Feed Specification (GBFS)
  auto-discovery feeds at mds.bird.co for 88+ cities across 12 countries (AT, BE, CA, CH, DE, ES, FI, FR, IL, IT, PT, US), and operates a private city-data portal at city-data.bird.co for credentialed municipal API access. There is no public consumer / 3rd-party developer API or SDK — the consumer surface is the iOS and Android Bird apps, the Bird Three product site, and the Bikeshare site. The undocumented mobile backend at api.birdapp.com / api-auth.prod.birdapp.com is well-documented in the community WoBike project but is not officially sanctioned for third-party use.
examples:
- key_count: 4
  name: Bird System Information Example
  slug: bird-system-information-example
- key_count: 4
  name: Bird Vehicle Types Example
  slug: bird-vehicle-types-example
features:
- Bird Three — flagship dockless electric scooter with swappable batteries, GPS, anti-theft and government-technology features
- Bird Bikeshare — electric-assist pedal bike service with 60 km nominal range
- Public GBFS v2.3 auto-discovery feeds for 88 cities across 12 countries (AT BE CA CH DE ES FI FR IL IT PT US)
- GBFS sub-feeds — system_information, vehicle_types, free_bike_status, station_information, station_status, geofencing_zones, system_pricing_plans, system_regions, gbfs_versions
- 60-second TTL on real-time GBFS data with both v1.1 and v2.3 advertised in MobilityData systems.csv
- City data portal at city-data.bird.co for credentialed municipal access to operational and trip data
- Bird Platform — white-label fleet operator program with hosted dashboard, historical analytics, geospatial tools, and GovTech compliance features
- Bird Cities partner program with custom dashboards and "in-depth APIs" for municipal trend analysis
- Bird Community Pricing — 50% discount for qualifying low-income riders
- Community Mode for resident issue reporting (improperly parked vehicles, hazards)
- SMS unlock and cash payment options for unbanked / no-smartphone riders
- In-app no-ride and no-parking geofencing enforced via GBFS geofencing_zones feed
- iOS and Android consumer apps with magic-link email authentication
- 200,000+ vehicle fleet under Third Lane Mobility (Bird + Spin)
- 350+ city footprint across North America, Europe, Middle East, and Asia
finops:
- name: Bird Rides Finops
  service_category: ''
  slug: bird-rides-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bird-rides.png
json_schemas:
- name: Bird Geofencing Zone
  property_count: 3
  slug: bird-geofencing-zone
- name: Bird System Information
  property_count: 7
  slug: bird-system-information
- name: Bird Vehicle
  property_count: 8
  slug: bird-vehicle
jsonld:
- class_count: 20
  name: Bird Rides Context
  property_count: 8
  slug: bird-rides-context
layout: provider
modified: '2026-05-25'
name: Bird
nav: Providers
network: true
overview: 'Bird publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Geofencing API, Pricing API, and 4 more. Tagged areas include Micromobility, Shared Mobility, Electric Scooters, E-Scooters, and E-Bikes.


  The Bird catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bird''s developer surface includes documentation, support, engineering blog, terms of service, privacy policy, and 31 more developer resources.'
plans:
- name: Bird Rides Plans Pricing
  plan_count: 4
  slug: bird-rides-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 0
  name: Bird Rides Rate Limits
  slug: bird-rides-rate-limits
rules:
- name: Bird API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bird-rides-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.2
  delta: -3.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bird-rides/refs/heads/main/screenshots/bird-rides-2026-06-20T173255.png
security:
- kind: domain-security
  name: Bird Rides Domain Security
  slug: bird-rides-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bird-rides
tags:
- Micromobility
- Shared Mobility
- Electric Scooters
- E-Scooters
- E-Bikes
- Bikeshare
- Transportation
- Urban Mobility
- GBFS
- General Bikeshare Feed Specification
- Mobility Data Specification
- MDS
- Geofencing
- Cities
- Smart Cities
- Fleet Management
- Third Lane Mobility
website: https://www.bird.co
---
