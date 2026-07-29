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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Arcbest Agentic Access
  operation_count: 5
  slug: arcbest-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
apis:
- description: Pickup scheduling and management
  name: ArcBest Pickups API
  slug: arcbest-pickups-api
- description: Freight rate quote services
  name: ArcBest Rates API
  slug: arcbest-rates-api
- description: Shipment booking and management
  name: ArcBest Shipments API
  slug: arcbest-shipments-api
- description: Shipment tracking and visibility
  name: ArcBest Tracking API
  slug: arcbest-tracking-api
artifact_total: 64
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arcbest-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arcbest-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arcbest-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arcbest
- group: start
  title: ''
  type: Portal
  url: https://www.arcbest.com/
- group: start
  title: ''
  type: Signup
  url: https://www.arcbest.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/rules/arcbest-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/vocabulary/arcbest-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/json-ld/arcbest-api-context.jsonld
created: '2026-03-23'
description: ArcBest is a logistics company offering less-than-truckload (LTL) freight, truckload, moving, and supply chain management services. The ArcBest API platform provides integration capabilities for freight rating, booking, tracking, and supply chain visibility.
examples:
- key_count: 6
  name: Arcbest Api Address Example
  slug: arcbest-api-address-example
- key_count: 2
  name: Arcbest Api Error Response Example
  slug: arcbest-api-error-response-example
- key_count: 7
  name: Arcbest Api Freight Item Example
  slug: arcbest-api-freight-item-example
- key_count: 3
  name: Arcbest Api Pickup Confirmation Example
  slug: arcbest-api-pickup-confirmation-example
- key_count: 4
  name: Arcbest Api Pickup Request Example
  slug: arcbest-api-pickup-request-example
- key_count: 4
  name: Arcbest Api Rate Request Example
  slug: arcbest-api-rate-request-example
- key_count: 5
  name: Arcbest Api Rate Response Example
  slug: arcbest-api-rate-response-example
- key_count: 4
  name: Arcbest Api Shipment Example
  slug: arcbest-api-shipment-example
- key_count: 2
  name: Arcbest Api Shipment List Example
  slug: arcbest-api-shipment-list-example
- key_count: 5
  name: Arcbest Api Shipment Request Example
  slug: arcbest-api-shipment-request-example
- key_count: 3
  name: Arcbest Api Tracking Event Example
  slug: arcbest-api-tracking-event-example
- key_count: 5
  name: Arcbest Api Tracking Status Example
  slug: arcbest-api-tracking-status-example
features:
- description: Real-time less-than-truckload freight rate quotes with transit time estimates.
  name: LTL Rate Quotes
- description: API-based shipment booking and scheduling for LTL and truckload freight.
  name: Shipment Booking
- description: Real-time tracking of freight shipments with status updates and delivery notifications.
  name: Shipment Tracking
- description: Electronic Bill of Lading generation and management through API integration.
  name: BOL Generation
- description: Automated pickup scheduling and confirmation for outbound freight.
  name: Pickup Scheduling
- description: End-to-end supply chain visibility across ArcBest freight and logistics services.
  name: Supply Chain Visibility
finops:
- name: Arcbest Finops
  service_category: API
  slug: arcbest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arcbest.png
integrations:
- description: Integration with SAP ERP for freight cost allocation and logistics management.
  name: SAP
- description: Connect to Oracle ERP and WMS systems for automated freight operations.
  name: Oracle
- description: Integrate shipment tracking and freight data with Salesforce CRM.
  name: Salesforce
- description: Multi-carrier shipping management platform integration.
  name: ShipStation
- description: E-commerce platform integration for LTL freight rate display and booking.
  name: Shopify
json_schemas:
- name: Address
  property_count: 6
  slug: arcbest-api-address
- name: ErrorResponse
  property_count: 2
  slug: arcbest-api-error-response
- name: FreightItem
  property_count: 7
  slug: arcbest-api-freight-item
- name: PickupConfirmation
  property_count: 3
  slug: arcbest-api-pickup-confirmation
- name: PickupRequest
  property_count: 4
  slug: arcbest-api-pickup-request
- name: RateRequest
  property_count: 4
  slug: arcbest-api-rate-request
- name: RateResponse
  property_count: 5
  slug: arcbest-api-rate-response
- name: ShipmentList
  property_count: 2
  slug: arcbest-api-shipment-list
- name: ShipmentRequest
  property_count: 5
  slug: arcbest-api-shipment-request
- name: Shipment
  property_count: 4
  slug: arcbest-api-shipment
- name: TrackingEvent
  property_count: 3
  slug: arcbest-api-tracking-event
- name: TrackingStatus
  property_count: 5
  slug: arcbest-api-tracking-status
json_structures:
- name: Arcbest Api Address Structure
  property_count: 6
  slug: arcbest-api-address-structure
- name: Arcbest Api Error Response Structure
  property_count: 2
  slug: arcbest-api-error-response-structure
- name: Arcbest Api Freight Item Structure
  property_count: 7
  slug: arcbest-api-freight-item-structure
- name: Arcbest Api Pickup Confirmation Structure
  property_count: 3
  slug: arcbest-api-pickup-confirmation-structure
- name: Arcbest Api Pickup Request Structure
  property_count: 4
  slug: arcbest-api-pickup-request-structure
- name: Arcbest Api Rate Request Structure
  property_count: 4
  slug: arcbest-api-rate-request-structure
- name: Arcbest Api Rate Response Structure
  property_count: 5
  slug: arcbest-api-rate-response-structure
- name: Arcbest Api Shipment List Structure
  property_count: 2
  slug: arcbest-api-shipment-list-structure
- name: Arcbest Api Shipment Request Structure
  property_count: 5
  slug: arcbest-api-shipment-request-structure
- name: Arcbest Api Shipment Structure
  property_count: 4
  slug: arcbest-api-shipment-structure
- name: Arcbest Api Tracking Event Structure
  property_count: 3
  slug: arcbest-api-tracking-event-structure
- name: Arcbest Api Tracking Status Structure
  property_count: 5
  slug: arcbest-api-tracking-status-structure
jsonld:
- class_count: 12
  name: Arcbest Api Context
  property_count: 41
  slug: arcbest-api-context
layout: provider
modified: '2026-04-19'
name: ArcBest
nav: Providers
network: true
overview: 'ArcBest publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Pickups API, Rates API, Shipments API, and 1 more. Tagged areas include Logistics, Freight, LTL, Supply Chain, and Shipping.


  The ArcBest catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ArcBest''s developer surface includes authentication, developer portal, signup flow, and 6 more developer resources.'
plans:
- name: Arcbest Plans Pricing
  plan_count: 3
  slug: arcbest-plans-pricing
press:
- date: '2026-05-25'
  title: ArcBest Continues its Revolutionary Line of Technology ...
  url: https://armoneyandpolitics.com/arcbest-technology/
- date: '2026-05-25'
  title: ArcBest sees gains in operations through AI
  url: https://www.truckingdive.com/news/arcbests-optimization-efforts-improve-truckload-ltl-operations/756526/
- date: '2026-05-25'
  title: ArcBest Highlights Strategic Pillars and Long-Term ...
  url: https://www.businesswire.com/news/home/20250929578216/en/ArcBest-Highlights-Strategic-Pillars-and-Long-Term-Financial-Targets-at-2025-Investor-Day
- date: '2026-05-25'
  title: 'Press Release: ArcBest Introduces Latest Vaux Vision ...'
  url: https://www.facebook.com/ArcBestCorp/posts/press-release-arcbest-introduces-latest-vaux-vision-advancements-and-key-leaders/1241212648014110/
- date: '2026-05-25'
  title: ArcBest Helps Bridge the Gap Between Robotics and ...
  url: https://investors.arcb.com/news-events/news/News-Details/2024/ArcBest-Helps-Bridge-the-Gap-Between-Robotics-and-Logistics-Using-NVIDIA-Technology/
random_paper: 47
rate_limits:
- limit_count: 5
  name: Arcbest Rate Limits
  slug: arcbest-rate-limits
rules:
- name: ArcBest API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: arcbest-jsonschema-spectral-rules
- name: ArcBest API Rules
  rule_count: 24
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 11
  slug: arcbest-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: -7.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/screenshots/arcbest-2026-06-20T172358.png
security:
- kind: authentication
  name: Arcbest Authentication
  slug: arcbest-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arcbest Domain Security
  slug: arcbest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arcbest
tags:
- Logistics
- Freight
- LTL
- Supply Chain
- Shipping
- Transportation
use_cases:
- description: Integrate ArcBest freight rates and booking into e-commerce platforms for automated shipping.
  name: E-Commerce Shipping
- description: Connect ArcBest freight services to ERP systems for automated freight procurement and accounting.
  name: ERP Integration
- description: Integrate with Transportation Management Systems for multi-carrier freight optimization.
  name: TMS Integration
- description: Connect ArcBest pickup scheduling with warehouse management systems for outbound logistics automation.
  name: Warehouse Management
website: https://www.arcbest.com/
---
