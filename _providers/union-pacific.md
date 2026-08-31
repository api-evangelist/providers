---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Union Pacific Agentic Access
  operation_count: 14
  slug: union-pacific-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 8
apis:
- description: Access company account information
  name: Union Pacific Account API
  slug: union-pacific-account-api
- description: Manage exception cases for shipments that are off course
  name: Union Pacific Cases API
  slug: union-pacific-cases-api
- description: Search and identify rail equipment by specifications
  name: Union Pacific Equipment API
  slug: union-pacific-equipment-api
- description: Manage intermodal planning, reservations, and driver services
  name: Union Pacific Intermodal API
  slug: union-pacific-intermodal-api
- description: View Union Pacific network facility and location details
  name: Union Pacific Location API
  slug: union-pacific-location-api
- description: Perform actions on shipments — order equipment, release, or cancel
  name: Union Pacific Shipment Actions API
  slug: union-pacific-shipment-actions-api
- description: Track and manage rail shipments with location and ETA data
  name: Union Pacific Shipment API
  slug: union-pacific-shipment-api
- description: Look up waybill details for shipments
  name: Union Pacific Waybill API
  slug: union-pacific-waybill-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Union Pacific Account API
  slug: open-union-pacific-account-api
- collection_type: open
  name: Union Pacific Account Cases API
  slug: open-union-pacific-cases-api
- collection_type: open
  name: Union Pacific Account Equipment API
  slug: open-union-pacific-equipment-api
- collection_type: open
  name: Union Pacific Account Intermodal API
  slug: open-union-pacific-intermodal-api
- collection_type: open
  name: Union Pacific Account Location API
  slug: open-union-pacific-location-api
- collection_type: open
  name: Union Pacific Account Shipment Actions API
  slug: open-union-pacific-shipment-actions-api
- collection_type: open
  name: Union Pacific Account Shipment API
  slug: open-union-pacific-shipment-api
- collection_type: open
  name: Union Pacific Account Waybill API
  slug: open-union-pacific-waybill-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/union-pacific-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/union-pacific-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unionpacific
created: '2025-02-06'
description: Union Pacific is one of the largest freight railroad networks in the United States, operating across 23 states in the western two-thirds of the country. The company transports a diverse range of commodities including agricultural products, automotive goods, chemicals, energy resources, and industrial materials. Union Pacific's API platform gives businesses programmatic access to real-time shipment tracking, equipment management, intermodal planning, and supply chain exception handling, enabling seamless integration with logistics and supply chain management systems.
examples:
- key_count: 2
  name: Union Pacific Create Intermodal Reservation Example
  slug: union-pacific-create-intermodal-reservation-example
- key_count: 2
  name: Union Pacific List Shipments Example
  slug: union-pacific-list-shipments-example
finops:
- name: Union Pacific Finops
  service_category: Freight Rail
  slug: union-pacific-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/union-pacific.png
json_schemas:
- name: Account
  property_count: 4
  slug: union-pacific-account
- name: ActionResponse
  property_count: 4
  slug: union-pacific-action-response
- name: CancelRequest
  property_count: 2
  slug: union-pacific-cancel-request
- name: Case
  property_count: 8
  slug: union-pacific-case
- name: Equipment
  property_count: 5
  slug: union-pacific-equipment
- name: IntermodalDeparture
  property_count: 6
  slug: union-pacific-intermodal-departure
- name: IntermodalLane
  property_count: 6
  slug: union-pacific-intermodal-lane
- name: IntermodalReservationRequest
  property_count: 6
  slug: union-pacific-intermodal-reservation-request
- name: IntermodalReservation
  property_count: 7
  slug: union-pacific-intermodal-reservation
- name: Location
  property_count: 7
  slug: union-pacific-location
- name: OrderEquipmentRequest
  property_count: 6
  slug: union-pacific-order-equipment-request
- name: ReleaseShipmentRequest
  property_count: 3
  slug: union-pacific-release-shipment-request
- name: Shipment
  property_count: 11
  slug: union-pacific-shipment
- name: Waybill
  property_count: 8
  slug: union-pacific-waybill
json_structures:
- name: Union Pacific Case Structure
  property_count: 0
  slug: union-pacific-case-structure
- name: Union Pacific Equipment Structure
  property_count: 0
  slug: union-pacific-equipment-structure
- name: Union Pacific Intermodal Reservation Structure
  property_count: 0
  slug: union-pacific-intermodal-reservation-structure
- name: Union Pacific Location Structure
  property_count: 0
  slug: union-pacific-location-structure
- name: Union Pacific Shipment Structure
  property_count: 0
  slug: union-pacific-shipment-structure
- name: Union Pacific Waybill Structure
  property_count: 0
  slug: union-pacific-waybill-structure
jsonld:
- class_count: 0
  name: Union Pacific Context
  property_count: 18
  slug: union-pacific-context
layout: provider
modified: '2026-05-19'
name: Union Pacific
nav: Providers
network: true
overview: 'Union Pacific publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Cases API, Equipment API, and 5 more. Tagged areas include Fortune 500, Freight, Railroads, Shipping, and Trains.


  The Union Pacific catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Union Pacific Plans Pricing
  plan_count: 1
  slug: union-pacific-plans-pricing
press:
- date: '2026-05-25'
  title: UNP Union Pacific Corporation Latest Press Releases
  url: https://seekingalpha.com/symbol/UNP/press-releases
- date: '2026-05-25'
  title: 'Union Pacific''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/union-pacific-ai-strategy-analysis-of-dominance-in-railroad/
- date: '2026-05-25'
  title: QScreen AI Appoints Former Union Pacific Vice President ...
  url: https://www.newsfilecorp.com/release/294734/QScreen-AI-Appoints-Former-Union-Pacific-Vice-President-as-Strategic-Advisor-to-Drive-Expansion-into-North-American-Rail-and-Transportation-Markets
- date: '2026-05-25'
  title: Our track inspectors are getting a high-tech assist. With AI ...
  url: https://www.facebook.com/unionpacific/posts/our-track-inspectors-are-getting-a-high-tech-assistwith-ai-powered-machine-visio/1400107518819198/
- date: '2026-05-25'
  title: Union Pacific's AI Chat Gives Employees Tool to Save ...
  url: https://www.up.com/news/service/ai-chatgpt-tool-it-240205
- date: '2026-05-22'
  title: AI is Enhancing How Union Pacific Inspects Track
  url: https://www.up.com/news/safety/ai-powered-vision-inspects-track-260522
random_paper: 15
rate_limits:
- limit_count: 1
  name: Union Pacific Rate Limits
  slug: union-pacific-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Union Pacific API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: union-pacific-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Union Pacific API Rules
  rule_count: 36
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 18
  slug: union-pacific-spectral-rules
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 27.9
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 22.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Union Pacific Domain Security
  slug: union-pacific-domain-security
  summary_line: TLSv1.3 · DMARC
slug: union-pacific
tags:
- Fortune 500
- Freight
- Railroads
- Shipping
- Trains
- Supply Chain
- Logistics
---
