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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Us Army Corps Of Engineers Agentic Access
  operation_count: 9
  slug: us-army-corps-of-engineers-agentic-access
  summary_line: 9 operations
api_count: 9
apis:
- description: The National Inventory of Dams (NID) API provides access to the comprehensive database of US dams maintained by the US Army Corps of Engineers. The database contains information on over 70 data fields
  name: USACE National Inventory of Dams API
  slug: usace-national-inventory-of-dams
- description: 'The USACE Open Data program provides public access to geospatial data, regulatory permit information, and other datasets maintained by the US Army Corps of Engineers. Data is available through ArcGIS '
  name: USACE Open Data
  slug: usace-open-data
- description: The Catalog API from US Army Corps of Engineers — 1 operation(s) for catalog.
  name: US Army Corps of Engineers Catalog API
  slug: us-army-corps-of-engineers-catalog-api
- description: The Levels API from US Army Corps of Engineers — 1 operation(s) for levels.
  name: US Army Corps of Engineers Levels API
  slug: us-army-corps-of-engineers-levels-api
- description: The Locations API from US Army Corps of Engineers — 2 operation(s) for locations.
  name: US Army Corps of Engineers Locations API
  slug: us-army-corps-of-engineers-locations-api
- description: The Offices API from US Army Corps of Engineers — 1 operation(s) for offices.
  name: US Army Corps of Engineers Offices API
  slug: us-army-corps-of-engineers-offices-api
- description: The Ratings API from US Army Corps of Engineers — 1 operation(s) for ratings.
  name: US Army Corps of Engineers Ratings API
  slug: us-army-corps-of-engineers-ratings-api
- description: The Reservoirs API from US Army Corps of Engineers — 1 operation(s) for reservoirs.
  name: US Army Corps of Engineers Reservoirs API
  slug: us-army-corps-of-engineers-reservoirs-api
- description: The Timeseries API from US Army Corps of Engineers — 2 operation(s) for timeseries.
  name: US Army Corps of Engineers Timeseries API
  slug: us-army-corps-of-engineers-timeseries-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USACE CWMS Data Catalog API
  slug: open-us-army-corps-of-engineers-catalog-api
- collection_type: open
  name: USACE CWMS Data Catalog Levels API
  slug: open-us-army-corps-of-engineers-levels-api
- collection_type: open
  name: USACE CWMS Data Catalog Locations API
  slug: open-us-army-corps-of-engineers-locations-api
- collection_type: open
  name: USACE CWMS Data Catalog Offices API
  slug: open-us-army-corps-of-engineers-offices-api
- collection_type: open
  name: USACE CWMS Data Catalog Ratings API
  slug: open-us-army-corps-of-engineers-ratings-api
- collection_type: open
  name: USACE CWMS Data Catalog Reservoirs API
  slug: open-us-army-corps-of-engineers-reservoirs-api
- collection_type: open
  name: USACE CWMS Data Catalog Timeseries API
  slug: open-us-army-corps-of-engineers-timeseries-api
- collection_type: open
  name: USACE CWMS Data API
  slug: open-usace-cwms-data
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/USACE/cwms-data-api/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-army-corps-of-engineers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-army-corps-of-engineers-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-army-corps-of-engineers
created: '2024-11-21'
description: The US Army Corps of Engineers is a federal agency that plays a critical role in managing the nation's water resources and infrastructure. They are responsible for building and maintaining dams, levees, and flood control systems, overseeing construction of ports, harbors, and waterways, and providing engineering support to military operations. USACE publishes open APIs including the CWMS Data API for water management timeseries data, the National Inventory of Dams API, and open geospatial datasets.
examples:
- key_count: 2
  name: Usace Cwms Data Get Locations Example
  slug: usace-cwms-data-get-locations-example
- key_count: 2
  name: Usace Cwms Data Get Timeseries Example
  slug: usace-cwms-data-get-timeseries-example
finops:
- name: Us Army Corps Of Engineers Finops
  service_category: API
  slug: us-army-corps-of-engineers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-army-corps-of-engineers.png
json_schemas:
- name: USACE CWMS Location
  property_count: 16
  slug: usace-location
- name: USACE CWMS Timeseries
  property_count: 8
  slug: usace-timeseries
json_structures:
- name: Usace Timeseries Structure
  property_count: 0
  slug: usace-timeseries-structure
jsonld:
- class_count: 30
  name: Us Army Corps Of Engineers Context
  property_count: 3
  slug: us-army-corps-of-engineers-context
layout: provider
modified: '2026-05-19'
name: US Army Corps of Engineers
nav: Providers
network: true
overview: 'US Army Corps of Engineers publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Levels API, Locations API, and 4 more. Tagged areas include Water Resources, Federal Government, Military Engineering, Infrastructure, and Open Data.


  The US Army Corps of Engineers catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Us Army Corps Of Engineers Plans Pricing
  plan_count: 3
  slug: us-army-corps-of-engineers-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Us Army Corps Of Engineers Rate Limits
  slug: us-army-corps-of-engineers-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Army Corps of Engineers API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-army-corps-of-engineers-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: US Army Corps of Engineers API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: usace-cwms-data-rules
score:
  band: emerging
  composite: 23.5
  delta: -8.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 60.2
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/us-army-corps-of-engineers/refs/heads/main/screenshots/us-army-corps-of-engineers-2026-06-20T200546.png
security:
- kind: domain-security
  name: Us Army Corps Of Engineers Domain Security
  slug: us-army-corps-of-engineers-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-army-corps-of-engineers
tags:
- Water Resources
- Federal Government
- Military Engineering
- Infrastructure
- Open Data
- Geospatial Data
---
