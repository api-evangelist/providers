---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.replicahq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.replicahq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.replicahq.com/en/collections/1232529-introduction-to-replica
- group: operate
  title: ''
  type: Support
  url: https://help.replicahq.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.replicahq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replicahq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/replicahq
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.replicahq.com/en/articles/4374395-replica-product-release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.replicahq.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.replicahq.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://studio.replicahq.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/replica-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replica-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/replica-data-dictionary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/replica-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replica-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/replica-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/replica-packages.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-active-transportation.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-annual-average-daily-traffic-aadt.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-auto-tnc-trips.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-commercial-freight.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-consumer-spending-by-county-to-county-flows.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-consumer-spending-by-home-merchant-location.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-crash-data.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-daily-network-link-volumes.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-daily-o-d-data.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-daily-vmt.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-demographics-employment.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-disaggregate-trip-tables.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-free-flow-speed-per-network-link.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-hourly-auto-volume-profile.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-network-links.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-quarter-hourly-speed-profile-per-network-link-annual.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-transit.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-turning-movement-counts-tmcs.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/replica-weekly-spend-by-merchant-location.json
created: '2026-08-02'
description: Replica is a San Francisco-based data platform for the built environment, spun out of Alphabet's Sidewalk Labs in 2019, that operates a nationwide activity-based travel model. Its analytical engine combines public data (US Census/ACS, GTFS transit feeds, OpenStreetMap road networks, land-use records, state traffic counts) with licensed private data (de-identified aggregate mobile location, credit transaction and driving-behavior data) to synthesize a privacy-preserving simulated population and a complete trip table for the United States. Products include Places (seasonal, high-fidelity activity-based travel model), Trends (weekly near-real-time mobility and land-use data), Safety Hub, Safe Streets Planner, and a suite of workflow applications used by state DOTs, MPOs, transit agencies, cities and counties. Data is consumed through the Replica Studio web platform, CSV export and direct database access; Replica publishes documented dataset schemas at documentation.replicahq.com
  but no public developer REST API, SDK or developer portal.
image: https://replicahq.com/og-image.jpg
json_schemas:
- name: Active Transportation Trips
  property_count: 33
  slug: replica-active-transportation
- name: Annual Average Daily Traffic (AADT)
  property_count: 13
  slug: replica-annual-average-daily-traffic-aadt
- name: Auto and TNC Trips
  property_count: 33
  slug: replica-auto-tnc-trips
- name: Commercial Freight Trips
  property_count: 33
  slug: replica-commercial-freight
- name: '[Discontinued] Spend County-to-County Flows'
  property_count: 6
  slug: replica-consumer-spending-by-county-to-county-flows
- name: '[Discontinued] Weekly Spend (by home location)'
  property_count: 5
  slug: replica-consumer-spending-by-home-merchant-location
- name: Crash Data
  property_count: 16
  slug: replica-crash-data
- name: Daily Network Link Volumes
  property_count: 5
  slug: replica-daily-network-link-volumes
- name: Daily O-D Pairs
  property_count: 6
  slug: replica-daily-o-d-data
- name: Daily VMT
  property_count: 4
  slug: replica-daily-vmt
- name: Demographics and Employment
  property_count: 39
  slug: replica-demographics-employment
- name: Seasonal Trip Table
  property_count: 33
  slug: replica-disaggregate-trip-tables
- name: Annual Speeds per Network Link
  property_count: 15
  slug: replica-free-flow-speed-per-network-link
- name: Hourly Auto Volume Profile
  property_count: 12
  slug: replica-hourly-auto-volume-profile
- name: Network Links
  property_count: 13
  slug: replica-network-links
- name: Annual Quarter-Hourly Speed Profiles
  property_count: 12
  slug: replica-quarter-hourly-speed-profile-per-network-link-annual
- name: Transit Trips
  property_count: 40
  slug: replica-transit
- name: Turning Movement Counts
  property_count: 15
  slug: replica-turning-movement-counts-tmcs
- name: '[Discontinued] Weekly Spend (by merchant location)'
  property_count: 5
  slug: replica-weekly-spend-by-merchant-location
layout: provider
modified: '2026-08-02'
name: Replica
nav: Providers
network: true
overview: 'Replica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Mobility, Transportation, and Geospatial.


  Replica''s developer surface includes documentation, getting-started guide, support, engineering blog, changelog, and 33 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 33.3
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 18.4
  previous_composite: 18.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Replica Domain Security
  slug: replica-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: replica
tags:
- Company
- Data
- Mobility
- Transportation
- Geospatial
- Urban Planning
- Travel Demand Modeling
- Government
- Analytics
- Data Platform
website: https://www.replicahq.com/
---
