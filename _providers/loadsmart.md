---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 160
  human_in_the_loop: 122
  name: Loadsmart Agentic Access
  operation_count: 284
  slug: loadsmart-agentic-access
  summary_line: 284 operations · 160 acting · 122 human-in-the-loop
api_count: 48
apis:
- description: The Appointments API from Loadsmart — 10 operation(s) for appointments.
  name: Loadsmart Appointments API
  slug: loadsmart-appointments-api
- description: The Asset Container API from Loadsmart — 5 operation(s) for asset container.
  name: Loadsmart Asset Container API
  slug: loadsmart-asset-container-api
- description: The Asset Visit API from Loadsmart — 10 operation(s) for asset visit.
  name: Loadsmart Asset Visit API
  slug: loadsmart-asset-visit-api
- description: The Audit Log API from Loadsmart — 1 operation(s) for audit log.
  name: Loadsmart Audit Log API
  slug: loadsmart-audit-log-api
- description: The Authentication API from Loadsmart — 4 operation(s) for authentication.
  name: Loadsmart Authentication API
  slug: loadsmart-authentication-api
- description: This API allows third parties to create, list, retrieve and accept bids.
  name: Loadsmart Bids API
  slug: loadsmart-bids-api
- description: The BOL API from Loadsmart — 3 operation(s) for bol.
  name: Loadsmart BOL API
  slug: loadsmart-bol-api
- description: Manages new capacity. A capacity is a truck that is empty and it's location.
  name: Loadsmart Capacity API
  slug: loadsmart-capacity-api
- description: This API allows partners to request integration for Carriers and also manage Carrier's information. The usage of this API is detailed at https://developer.loadsmart.com/carrier-integrations/how-tos/ho
  name: Loadsmart Carrier API
  slug: loadsmart-carrier-api
- description: The Carrier Companies API from Loadsmart — 2 operation(s) for carrier companies.
  name: Loadsmart Carrier Companies API
  slug: loadsmart-carrier-companies-api
- description: The Carrier Users API from Loadsmart — 8 operation(s) for carrier users.
  name: Loadsmart Carrier Users API
  slug: loadsmart-carrier-users-api
- description: Data entities store the actual values submitted through Forms. Each form submission creates multiple Data records - one for each Form Field with a value. These records maintain the relationship betwee
  name: Loadsmart Custom Forms - Data API
  slug: loadsmart-custom-forms-data-api
- description: 'Fields are global definitions that specify fundamental attributes like data type (text, number, dropdown, etc.), validation rules, and base properties. Fields are organization-wide resources that can '
  name: Loadsmart Custom Forms - Fields API
  slug: loadsmart-custom-forms-fields-api
- description: Flows define the sequence and logic of form presentation. Each Flow must have a primary "fromForm" and may optionally include a secondary "formTo" that appears after the first form is completed. Flows
  name: Loadsmart Custom Forms - Flows API
  slug: loadsmart-custom-forms-flows-api
- description: Form Fields are instances of global Field definitions within a specific Form. While Fields define the data type and general properties, Form Fields customize these instances with form-specific attribu
  name: Loadsmart Custom Forms - Form Fields API
  slug: loadsmart-custom-forms-form-fields-api
- description: 'Forms are collections of form fields that represent a complete data entry interface. Each Form belongs to a Flow and captures related data points in a structured way. Forms provide the user interface '
  name: Loadsmart Custom Forms - Forms API
  slug: loadsmart-custom-forms-forms-api
- description: Triggers are event listeners that activate on specific API or UI events. Each Trigger is associated with exactly one Flow. When a Trigger fires, it initiates its associated Flow, which in turn present
  name: Loadsmart Custom Forms - Triggers API
  slug: loadsmart-custom-forms-triggers-api
- description: The Docks API from Loadsmart — 8 operation(s) for docks.
  name: Loadsmart Docks API
  slug: loadsmart-docks-api
- description: The Documents API from Loadsmart — 2 operation(s) for documents.
  name: Loadsmart Documents API
  slug: loadsmart-documents-api
- description: The Gates API from Loadsmart — 1 operation(s) for gates.
  name: Loadsmart Gates API
  slug: loadsmart-gates-api
- description: The General API from Loadsmart — 3 operation(s) for general.
  name: Loadsmart General API
  slug: loadsmart-general-api
- description: 'This API allows third parties to search and accept available Offers. ## Webhook events There are few webhook events that can be triggered related to Load Offers API. The following example refers to th'
  name: Loadsmart Load Offers API
  slug: loadsmart-load-offers-api
- description: The Load Type Groups API from Loadsmart — 2 operation(s) for load type groups.
  name: Loadsmart Load Type Groups API
  slug: loadsmart-load-type-groups-api
- description: The Load Types API from Loadsmart — 4 operation(s) for load types.
  name: Loadsmart Load Types API
  slug: loadsmart-load-types-api
- description: This endpoint will be the entrypoint for our integrations. It will receive loads.
  name: Loadsmart Loads API
  slug: loadsmart-loads-api
- description: The Metrics API from Loadsmart — 23 operation(s) for metrics.
  name: Loadsmart Metrics API
  slug: loadsmart-metrics-api
- description: The Observations API from Loadsmart — 3 operation(s) for observations.
  name: Loadsmart Observations API
  slug: loadsmart-observations-api
- description: The Orgs API from Loadsmart — 5 operation(s) for orgs.
  name: Loadsmart Orgs API
  slug: loadsmart-orgs-api
- description: Quotes provide the price and conditions for a future shipment. To create a shipment, you need first to request a valid quote.
  name: Loadsmart Quotes API
  slug: loadsmart-quotes-api
- description: Provides information about routing
  name: Loadsmart Routes API
  slug: loadsmart-routes-api
- description: The SAML API from Loadsmart — 5 operation(s) for saml.
  name: Loadsmart SAML API
  slug: loadsmart-saml-api
- description: The Settings Metadata API from Loadsmart — 3 operation(s) for settings metadata.
  name: Loadsmart Settings Metadata API
  slug: loadsmart-settings-metadata-api
- description: 'Our API supports fetch and change of a variety of shipments status, the main ones are responsible to move the shipment from booked to in transit and delivered, They must obey the following order: * **'
  name: Loadsmart Shipment Events API
  slug: loadsmart-shipment-events-api
- description: Stops of a shipment
  name: Loadsmart Shipment Stops API
  slug: loadsmart-shipment-stops-api
- description: Manage shipments
  name: Loadsmart Shipments API
  slug: loadsmart-shipments-api
- description: The Shipper Accounting Info API from Loadsmart — 1 operation(s) for shipper accounting info.
  name: Loadsmart Shipper Accounting Info API
  slug: loadsmart-shipper-accounting-info-api
- description: Manage the accounts associated with shippers. An account represents an user.
  name: Loadsmart Shipper Accounts API
  slug: loadsmart-shipper-accounts-api
- description: Manage shippers. A shipper is a company that creates and manages loads on Loadsmart platform.
  name: Loadsmart Shippers API
  slug: loadsmart-shippers-api
- description: The Storage API from Loadsmart — 2 operation(s) for storage.
  name: Loadsmart Storage API
  slug: loadsmart-storage-api
- description: The Unit Limiter API from Loadsmart — 5 operation(s) for unit limiter.
  name: Loadsmart Unit Limiter API
  slug: loadsmart-unit-limiter-api
- description: The Users API from Loadsmart — 6 operation(s) for users.
  name: Loadsmart Users API
  slug: loadsmart-users-api
- description: The Warehouse Groups API from Loadsmart — 2 operation(s) for warehouse groups.
  name: Loadsmart Warehouse Groups API
  slug: loadsmart-warehouse-groups-api
- description: The Warehouses API from Loadsmart — 4 operation(s) for warehouses.
  name: Loadsmart Warehouses API
  slug: loadsmart-warehouses-api
- description: Webhooks allow you to receive certain events from Loadsmart. When one of those events is triggered, we'll send an HTTP POST request to the webhook's configured URL(s). This URL(s) should be sent to Lo
  name: Loadsmart Webhooks API
  slug: loadsmart-webhooks-api
- description: The YMS - Spot API from Loadsmart — 8 operation(s) for yms - spot.
  name: Loadsmart YMS - Spot API
  slug: loadsmart-yms-spot-api
- description: The YMS - Spot Area API from Loadsmart — 2 operation(s) for yms - spot area.
  name: Loadsmart YMS - Spot Area API
  slug: loadsmart-yms-spot-area-api
- description: The YMS - Spot Assignment API from Loadsmart — 4 operation(s) for yms - spot assignment.
  name: Loadsmart YMS - Spot Assignment API
  slug: loadsmart-yms-spot-assignment-api
- description: The YMS - Yard View API from Loadsmart — 4 operation(s) for yms - yard view.
  name: Loadsmart YMS - Yard View API
  slug: loadsmart-yms-yard-view-api
artifact_total: 73
collections:
- collection_type: open
  name: Opendock Nova API Documentation
  slug: open-loadsmart-opendock
- collection_type: open
  name: Loadsmart API
  slug: open-loadsmart-shipperguide
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loadsmart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loadsmart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loadsmart-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://loadsmart.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.loadsmart.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.loadsmart.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.loadsmart.com/docs/shipperguide/api-reference
- group: docs
  title: ''
  type: OpenAPI
  url: https://developer.loadsmart.com/api/openapi.yaml
- group: company
  title: ''
  type: About
  url: https://loadsmart.com/about/
- group: company
  title: ''
  type: Careers
  url: https://loadsmart.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://loadsmart.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://blog.loadsmart.com/
- group: operate
  title: ''
  type: Community
  url: https://community.loadsmart.com/
- group: docs
  title: ''
  type: ShipperGuide
  url: https://loadsmart.com/shippers/shipperguide-tms/
- group: other
  title: ''
  type: ManagedTransportation
  url: https://loadsmart.com/shippers/managed-transportation/
- group: other
  title: ''
  type: FreightIntelAI
  url: https://loadsmart.com/freightintel-ai/
- group: other
  title: ''
  type: PrivateFleetOptimizer
  url: https://loadsmart.com/shippers/private-fleet-optimizer/
- group: other
  title: ''
  type: FlatbedMessenger
  url: https://loadsmart.com/flatbed-messenger/
- group: other
  title: ''
  type: CarrierLoadboard
  url: https://loadsmart.com/carriers/loadboard/
- group: docs
  title: ''
  type: CarrierGuide
  url: https://loadsmart.com/carriers/carrierguide-tms/
- group: other
  title: ''
  type: Factoring
  url: https://loadsmart.com/carriers/factoring/
- group: other
  title: ''
  type: Opendock
  url: https://opendock.com/
- group: other
  title: ''
  type: NavTrac
  url: https://loadsmart.com/warehouse/navtrac/
- group: build
  title: ''
  type: OracleIntegration
  url: https://loadsmart.com/integrations/oracle/
- group: build
  title: ''
  type: MercuryGateIntegration
  url: https://loadsmart.com/integrations/mercury-gate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loadsmart
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LoadSmartUS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loadsmart
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCN-pkKcoMargmyL0Br3-H5w
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/loadsmart
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/loadsmartUS
- group: commercial
  title: ''
  type: Plans
  url: plans/loadsmart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loadsmart-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loadsmart-finops.yml
created: '2026-05-25'
description: Loadsmart is a digital freight technology company and 4PL that connects shippers, carriers, warehouses, and dock operations on a single platform. Founded in 2014 by Felipe Capella and Ricardo Salgado and headquartered in Chicago (with significant New York presence), Loadsmart raised more than $346M from investors including BlackRock, SoftBank Latin America Fund, Maersk Growth, TFI International, CSX, Ports America, and Connor Capital, reaching a reported $1.3B valuation. The platform spans full and partial truckload, less-than-truckload, drayage, expedited, flatbed (via Flatbed Messenger), and multimodal freight, plus the ShipperGuide TMS for procurement, planning, and execution; CarrierGuide TMS and a carrier loadboard with factoring; Opendock for dock appointment scheduling and the Nova warehouse API; and NavTrac for yard management and computer-vision gate/yard visibility. FreightIntel AI provides machine-learning powered freight recommendations across the suite. Loadsmart
  exposes a public Developer Portal with two production OpenAPI surfaces — the ShipperGuide API (api.loadsmart.com, JWT/RS256 authentication, with quote, book, tender, track, and webhook lanes) and the Opendock Nova / Neutron API (neutron.opendock.com, JWT bearer authentication) — and ships a Postman collection plus partner integrations with Oracle Transportation Management, MercuryGate, Blue Yonder, SAP, NetSuite, and other TMS/ERP platforms.
features:
- ShipperGuide TMS for freight procurement, planning, and execution across modes
- Managed Transportation (4PL) services for enterprise shippers
- FreightIntel AI machine-learning recommendations for rate, mode, and lane decisions
- Private Fleet Optimizer for fleet-running shippers
- Flatbed Messenger marketplace for flatbed freight
- CarrierGuide TMS, Carrier Loadboard, and Factoring services for motor carriers
- Opendock Nova for dock appointment scheduling, hours of operation, gates, and yards
- Subspace real-time WebSocket API streaming dock appointment events
- Appointment Validation API for verifying PO numbers before scheduling
- NavTrac yard management and computer-vision asset tracking
- Public ShipperGuide REST API (50 paths) for quote, book, tender, track, and webhooks
- Public Opendock Nova/Neutron REST API (151 paths) for warehouse, dock, and appointment ops
- JWT/RS256 authentication for ShipperGuide; JWT bearer for Opendock Nova
- Sandbox environments for both API surfaces
- Webhook surface for quote, shipment, load, bid, and carrier lifecycle events
- Integrations with Oracle Transportation Management, MercuryGate, and other TMS/ERPs
- Postman collections for both ShipperGuide and Opendock Nova
finops:
- name: Loadsmart Finops
  service_category: Logistics and Supply Chain
  slug: loadsmart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loadsmart.png
layout: provider
modified: '2026-05-25'
name: Loadsmart
nav: Providers
network: true
overview: 'Loadsmart publishes 48 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Asset Container API, Asset Visit API, and 45 more. Tagged areas include Freight, Logistics, Transportation, Supply Chain, and Digital Freight.


  Loadsmart''s developer surface includes authentication, documentation, API reference, engineering blog, YouTube channel, and 29 more developer resources.'
plans:
- name: Loadsmart Plans Pricing
  plan_count: 6
  slug: loadsmart-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Loadsmart Rate Limits
  slug: loadsmart-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.9
    developer_ergonomics: 41.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loadsmart/refs/heads/main/screenshots/loadsmart-2026-06-20T184627.png
security:
- kind: authentication
  name: Loadsmart Authentication
  slug: loadsmart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Loadsmart Domain Security
  slug: loadsmart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: loadsmart
tags:
- Freight
- Logistics
- Transportation
- Supply Chain
- Digital Freight
- Freight Brokerage
- Truckload
- LTL
- Drayage
- Flatbed
- Multimodal
- TMS
- Dock Scheduling
- Yard Management
- Warehouse
- 4PL
- FreightTech
website: https://loadsmart.com
---
