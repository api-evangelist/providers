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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Travelcenters Of America Agentic Access
  operation_count: 10
  slug: travelcenters-of-america-agentic-access
  summary_line: 10 operations
api_count: 6
apis:
- description: Fuel code management for fleet operators
  name: TravelCenters of America Fuel Codes API
  slug: travelcenters-of-america-fuel-codes-api
- description: Travel center location search and amenity data
  name: TravelCenters of America Locations API
  slug: travelcenters-of-america-locations-api
- description: Parking availability at travel centers
  name: TravelCenters of America Parking API
  slug: travelcenters-of-america-parking-api
- description: Fuel and service pricing data
  name: TravelCenters of America Pricing API
  slug: travelcenters-of-america-pricing-api
- description: Shower facility availability
  name: TravelCenters of America Showers API
  slug: travelcenters-of-america-showers-api
- description: Work order management for TA Truck Service
  name: TravelCenters of America Truck Service API
  slug: travelcenters-of-america-truck-service-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TravelCenters of America Fuel Codes API
  slug: open-travelcenters-of-america-fuel-codes-api
- collection_type: open
  name: TravelCenters of America Fuel Codes Locations API
  slug: open-travelcenters-of-america-locations-api
- collection_type: open
  name: TravelCenters of America Fuel Codes Parking API
  slug: open-travelcenters-of-america-parking-api
- collection_type: open
  name: TravelCenters of America Fuel Codes Pricing API
  slug: open-travelcenters-of-america-pricing-api
- collection_type: open
  name: TravelCenters of America Fuel Codes Showers API
  slug: open-travelcenters-of-america-showers-api
- collection_type: open
  name: TravelCenters of America Fuel Codes Truck Service API
  slug: open-travelcenters-of-america-truck-service-api
- collection_type: open
  name: TravelCenters of America API
  slug: open-travelcenters-of-america
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/travelcenters-of-america-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travelcenters-of-america-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/travelcenters-of-america-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/travelcenters-of-america
- group: company
  title: ''
  type: Website
  url: https://www.ta-petro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accessta.com/
- group: other
  title: ''
  type: Developers
  url: https://www.ta-petro.com/developers/
- group: start
  title: ''
  type: Signup
  url: https://services.accessta.com/APIRequest/DevApiRequest
created: '2026-03-24'
description: TravelCenters of America is the largest publicly traded full-service travel center network in the United States, operating under the TA, Petro Stopping Centers, and TA Express brands. The company provides REST APIs for truck service work order management, retail location data, fuel codes, pricing, parking availability, and shower availability.
examples:
- key_count: 2
  name: Travelcenters Of America Get Parking Availability Example
  slug: travelcenters-of-america-get-parking-availability-example
- key_count: 2
  name: Travelcenters Of America List Locations Example
  slug: travelcenters-of-america-list-locations-example
finops:
- name: Travelcenters Of America Finops
  service_category: API
  slug: travelcenters-of-america-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/travelcenters-of-america.png
json_schemas:
- name: Travel Center Location
  property_count: 14
  slug: travelcenters-of-america-location
json_structures:
- name: Travelcenters Of America Location Structure
  property_count: 0
  slug: travelcenters-of-america-location-structure
jsonld:
- class_count: 42
  name: Travelcenters Of America Context
  property_count: 0
  slug: travelcenters-of-america-context
layout: provider
modified: '2026-05-19'
name: TravelCenters of America
nav: Providers
network: true
overview: 'TravelCenters of America publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Fuel Codes API, Locations API, Parking API, and 3 more. Tagged areas include Travel Centers, Truck Service, Retail, Fuel, and Locations.


  The TravelCenters of America catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TravelCenters of America''s developer surface includes authentication, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Travelcenters Of America Plans Pricing
  plan_count: 3
  slug: travelcenters-of-america-plans-pricing
press:
- date: '2026-05-25'
  title: TravelCenters of America (TA) Q2 2022 Earnings Call ...
  url: https://www.fool.com/earnings/call-transcripts/2022/08/02/travelcenters-of-america-ta-q2-2022-earnings-call/
- date: '2026-05-25'
  title: TravelCenters of America Celebrates 300th Travel Center ...
  url: https://www.prnewswire.com/news-releases/travelcenters-of-america-celebrates-300th-travel-center-milestone-302070078.html
- date: '2026-05-25'
  title: TravelCenters of America Outlines Plans Heading into 50th ...
  url: https://www.ta-petro.com/blog/travelcenters-of-america-outlines-plans-heading-into-50th-anniversary-year/
- date: '2026-05-25'
  title: BP to buy TravelCenters for $1.3 bln in U.S. fuel retail drive
  url: https://www.reuters.com/markets/deals/bp-buy-travelcenters-america-13-billion-2023-02-16/
- date: '2026-05-25'
  title: TravelCenters of America and NATSO Foundation Work to ...
  url: https://www.prnewswire.com/news-releases/travelcenters-of-america-and-natso-foundation-work-to-enhance-safety-for-roadside-service-technicians-302112405.html
random_paper: 20
rate_limits:
- limit_count: 5
  name: Travelcenters Of America Rate Limits
  slug: travelcenters-of-america-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TravelCenters of America API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: travelcenters-of-america-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: TravelCenters of America API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 3
    info: 0
    warn: 4
  slug: travelcenters-of-america-rules
score:
  band: thin
  composite: 36.6
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 66.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/travelcenters-of-america/refs/heads/main/screenshots/travelcenters-of-america-2026-06-20T195634.png
security:
- kind: authentication
  name: Travelcenters Of America Authentication
  slug: travelcenters-of-america-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Travelcenters Of America Domain Security
  slug: travelcenters-of-america-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: travelcenters-of-america
tags:
- Travel Centers
- Truck Service
- Retail
- Fuel
- Locations
- Trucking
- Fleet Management
- Fortune 500
website: https://www.ta-petro.com/
---
