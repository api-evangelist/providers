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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: National Highway Traffic Safety Administration Agentic Access
  operation_count: 24
  slug: national-highway-traffic-safety-administration-agentic-access
  summary_line: 24 operations · 1 acting
api_count: 6
apis:
- description: Equipment, parts, and Canadian vehicle specifications
  name: National Highway Traffic Safety Administration Equipment API
  slug: national-highway-traffic-safety-administration-equipment-api
- description: Endpoints for vehicle make and model information
  name: National Highway Traffic Safety Administration Makes and Models API
  slug: national-highway-traffic-safety-administration-makes-and-models-api
- description: Endpoints for manufacturer and World Manufacturer Identifier (WMI) data
  name: National Highway Traffic Safety Administration Manufacturers API
  slug: national-highway-traffic-safety-administration-manufacturers-api
- description: Reference variables and value lists
  name: National Highway Traffic Safety Administration Reference API
  slug: national-highway-traffic-safety-administration-reference-api
- description: Endpoints related to vehicle types
  name: National Highway Traffic Safety Administration Vehicle Types API
  slug: national-highway-traffic-safety-administration-vehicle-types-api
- description: Endpoints for decoding Vehicle Identification Numbers
  name: National Highway Traffic Safety Administration VIN Decoding API
  slug: national-highway-traffic-safety-administration-vin-decoding-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NHTSA vPIC Vehicle Equipment API
  slug: open-national-highway-traffic-safety-administration-equipment-api
- collection_type: open
  name: NHTSA vPIC Vehicle Equipment Makes and Models API
  slug: open-national-highway-traffic-safety-administration-makes-and-models-api
- collection_type: open
  name: NHTSA vPIC Vehicle Equipment Manufacturers API
  slug: open-national-highway-traffic-safety-administration-manufacturers-api
- collection_type: open
  name: NHTSA vPIC Vehicle Equipment Reference API
  slug: open-national-highway-traffic-safety-administration-reference-api
- collection_type: open
  name: NHTSA vPIC Vehicle Equipment Vehicle Types API
  slug: open-national-highway-traffic-safety-administration-vehicle-types-api
- collection_type: open
  name: NHTSA vPIC Vehicle Equipment VIN Decoding API
  slug: open-national-highway-traffic-safety-administration-vin-decoding-api
- collection_type: open
  name: NHTSA vPIC Vehicle API
  slug: open-national-highway-traffic-safety-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-highway-traffic-safety-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-highway-traffic-safety-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-highway-traffic-safety-administration-nhtsa
- group: company
  title: ''
  type: Website
  url: https://www.nhtsa.gov/
- group: start
  title: ''
  type: Portal
  url: https://vpic.nhtsa.dot.gov/api/
created: '2024-03-30'
description: The National Highway Traffic Safety Administration (NHTSA) provides APIs for vehicle safety information including vehicle recall data and the Product Information Catalog Vehicle Listing (vPIC) for decoding Vehicle Identification Numbers (VINs) and accessing vehicle specifications submitted by manufacturers.
finops:
- name: National Highway Traffic Safety Administration Finops
  service_category: API
  slug: national-highway-traffic-safety-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-highway-traffic-safety-administration.png
layout: provider
modified: '2026-05-19'
name: National Highway Traffic Safety Administration
nav: Providers
network: true
overview: 'National Highway Traffic Safety Administration publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Equipment API, Makes and Models API, Manufacturers API, and 3 more. Tagged areas include Federal Government, Safety, Transportation, and Vehicles.


  National Highway Traffic Safety Administration''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: National Highway Traffic Safety Administration Plans Pricing
  plan_count: 3
  slug: national-highway-traffic-safety-administration-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: National Highway Traffic Safety Administration Rate Limits
  slug: national-highway-traffic-safety-administration-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: -0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 42.8
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-highway-traffic-safety-administration/refs/heads/main/screenshots/national-highway-traffic-safety-administration-2026-06-20T190021.png
security:
- kind: domain-security
  name: National Highway Traffic Safety Administration Domain Security
  slug: national-highway-traffic-safety-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-highway-traffic-safety-administration
tags:
- Federal Government
- Safety
- Transportation
- Vehicles
website: https://www.nhtsa.gov/
---
