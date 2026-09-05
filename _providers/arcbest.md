---
access_model:
  confidence: high
  label: Enterprise · Sales-gated, credentials issued by ArcBest
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - sandbox
  - lifecycle
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Arcbest Agentic Access
  operation_count: 5
  slug: arcbest-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 6
apis:
- baseURL: https://api.arcb.com
  baseurl_source: declared
  description: Pickup scheduling and management
  name: ArcBest Pickups API
  slug: arcbest-pickups-api
- baseURL: https://api.arcb.com
  baseurl_source: declared
  description: Freight rate quote services
  name: ArcBest Rates API
  slug: arcbest-rates-api
- baseURL: https://api.arcb.com
  baseurl_source: declared
  description: Shipment booking and management
  name: ArcBest Shipments API
  slug: arcbest-shipments-api
- baseURL: https://api.arcb.com
  baseurl_source: declared
  description: Shipment tracking and visibility
  name: ArcBest Tracking API
  slug: arcbest-tracking-api
- baseURL: https://api.arcb.com/expedite/customer
  baseurl_source: declared
  description: 'Quote, book and track ArcBest Expedite (Panther Premium Logistics) time-critical freight directly from a shipper''s own application. Client-credential authorize call returns a bearer token; quotes are '
  name: ArcBest Expedite Customer API
  slug: arcbest-expedite-customer-api
- baseURL: https://api.arcb.com/expedite/digital
  baseurl_source: declared
  description: The integration surface ArcBest publishes for transportation management systems and freight-visibility platforms. HTTP Basic authenticated; quote, book, poll booking status, retrieve the Bill of Ladin
  name: ArcBest Expedite Third Party TMS API
  slug: arcbest-expedite-tms-api
artifact_total: 75
asyncapis:
- description: ''
  name: Arcbest Track And Trace Webhooks
  slug: arcbest-track-and-trace-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ArcBest Pickups API
  slug: open-arcbest-pickups-api
- collection_type: open
  name: ArcBest Pickups Rates API
  slug: open-arcbest-rates-api
- collection_type: open
  name: ArcBest Pickups Shipments API
  slug: open-arcbest-shipments-api
- collection_type: open
  name: ArcBest Pickups Tracking API
  slug: open-arcbest-tracking-api
common:
- group: company
  title: ''
  type: Website
  url: https://arcb.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/arcbest-expedite-customer-api-openapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arcbest-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arcbest-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arcbest-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arcbest-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arcbest-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/arcbest-track-and-trace-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/arcbest-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/arcbest-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arcbest-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arcbest-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/arcbest-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arcbest-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://arcb.com/technology/shippers/API
- group: docs
  title: ''
  type: APIReference
  url: https://arcb.com/technology/shippers/API/expedite-setup-documentation-download
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arcb.com/technology/shippers
- group: start
  title: ''
  type: GettingStarted
  url: https://arcb.com/technology/shippers/API/expedite-setup-documentation-download
- group: operate
  title: ''
  type: Support
  url: https://support.arcb.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.arcb.com/en/collections/900749-quote-tools
- group: company
  title: ''
  type: Blog
  url: https://arcb.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://arcb.com/registration/customer
- group: start
  title: ''
  type: Login
  url: https://arcb.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcb.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcb.com/privacy-policy
- group: other
  title: ''
  type: Standard
  url: https://arcb.com/technology/shippers/EDI
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArcBest-Technologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arcbest
- group: start
  title: ''
  type: Portal
  url: https://arcb.com/
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
description: 'ArcBest is a multibillion-dollar freight and logistics provider operating ABF Freight (LTL), Panther Premium Logistics (expedite), MoLo (truckload brokerage) and U-Pack (moving), with managed transportation, warehousing and international forwarding alongside. Its integration surface is published on arcb.com in two forms: REST APIs covering rate quote, volume quote, tracking, document retrieval, transit times, pickup request and Bill of Lading, whose documentation sits behind a customer login; and ANSI X12 EDI, where ArcBest publishes downloadable 204, 210 and 214 mapping specifications openly. The one API surface documented publicly is ArcBest Expedite - a Customer API and a third-party TMS API, each shipped as a downloadable Swagger-Codegen reference with worked JSON examples, live at api.arcb.com with a test environment at test.api.arcb.com.'
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
- name: Arcbest Expedite Quote Request Model
  property_count: 0
  slug: arcbest-expedite-quote-request-model
- name: Arcbest Expedite Quote Response Model
  property_count: 0
  slug: arcbest-expedite-quote-response-model
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
mcp_servers:
- description: ''
  name: ArcBest MCP Server
  slug: arcbest-mcp-server
modified: '2026-09-04'
name: ArcBest
nav: Providers
network: true
overview: 'ArcBest publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Pickups API, Rates API, Shipments API, and 3 more. Tagged areas include Logistics, Freight, LTL, Supply Chain, and Shipping.


  The ArcBest catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  ArcBest''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 29 more developer resources.'
plans:
- name: Arcbest Plans Pricing
  plan_count: 0
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
random_paper: 5
rate_limits:
- limit_count: 0
  name: Arcbest Rate Limits
  slug: arcbest-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ArcBest API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: arcbest-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: ArcBest API Rules
  rule_count: 24
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 11
  slug: arcbest-spectral-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.3
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 47.0
    contract_quality: 29.3
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 47.0
    operational_transparency: 13.2
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 28.6
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/screenshots/arcbest-2026-06-20T172358.png
security:
- kind: authentication
  name: Arcbest Authentication
  slug: arcbest-authentication
  summary_line: http · 2 schemes
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
- Expedite
- Truckload
- EDI
- Bill of Lading
- Rate Quote
- Shipment Tracking
use_cases:
- description: Integrate ArcBest freight rates and booking into e-commerce platforms for automated shipping.
  name: E-Commerce Shipping
- description: Connect ArcBest freight services to ERP systems for automated freight procurement and accounting.
  name: ERP Integration
- description: Integrate with Transportation Management Systems for multi-carrier freight optimization.
  name: TMS Integration
- description: Connect ArcBest pickup scheduling with warehouse management systems for outbound logistics automation.
  name: Warehouse Management
website: https://arcb.com/
---
