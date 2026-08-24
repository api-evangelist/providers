---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 100
  human_in_the_loop: 0
  name: Bringg Agentic Access
  operation_count: 136
  slug: bringg-agentic-access
  summary_line: 136 operations · 100 acting
api_count: 30
apis:
- description: The Administration API from Bringg — 1 operation(s) for administration.
  name: Bringg Administration API
  slug: bringg-administration-api
- description: The Analytics API from Bringg — 2 operation(s) for analytics.
  name: Bringg Analytics API
  slug: bringg-analytics-api
- description: The Authentication API from Bringg — 2 operation(s) for authentication.
  name: Bringg Authentication API
  slug: bringg-authentication-api
- description: The Blackouts API from Bringg — 4 operation(s) for blackouts.
  name: Bringg Blackouts API
  slug: bringg-blackouts-api
- description: The Bulk API from Bringg — 3 operation(s) for bulk.
  name: Bringg Bulk API
  slug: bringg-bulk-api
- description: The Customers API from Bringg — 5 operation(s) for customers.
  name: Bringg Customers API
  slug: bringg-customers-api
- description: The Delivery Blocks API from Bringg — 8 operation(s) for delivery blocks.
  name: Bringg Delivery Blocks API
  slug: bringg-delivery-blocks-api
- description: The Delivery Slots API from Bringg — 2 operation(s) for delivery slots.
  name: Bringg Delivery Slots API
  slug: bringg-delivery-slots-api
- description: The Drivers API from Bringg — 15 operation(s) for drivers.
  name: Bringg Drivers API
  slug: bringg-drivers-api
- description: The Floating Inventory API from Bringg — 4 operation(s) for floating inventory.
  name: Bringg Floating Inventory API
  slug: bringg-floating-inventory-api
- description: The Inventory API from Bringg — 2 operation(s) for inventory.
  name: Bringg Inventory API
  slug: bringg-inventory-api
- description: The Notes API from Bringg — 3 operation(s) for notes.
  name: Bringg Notes API
  slug: bringg-notes-api
- description: The Operations API from Bringg — 1 operation(s) for operations.
  name: Bringg Operations API
  slug: bringg-operations-api
- description: The Order Configurations API from Bringg — 2 operation(s) for order configurations.
  name: Bringg Order Configurations API
  slug: bringg-order-configurations-api
- description: The Orders API from Bringg — 22 operation(s) for orders.
  name: Bringg Orders API
  slug: bringg-orders-api
- description: The Packages API from Bringg — 6 operation(s) for packages.
  name: Bringg Packages API
  slug: bringg-packages-api
- description: The Parking Spots API from Bringg — 5 operation(s) for parking spots.
  name: Bringg Parking Spots API
  slug: bringg-parking-spots-api
- description: The Planned Routes API from Bringg — 2 operation(s) for planned routes.
  name: Bringg Planned Routes API
  slug: bringg-planned-routes-api
- description: The Quotes API from Bringg — 1 operation(s) for quotes.
  name: Bringg Quotes API
  slug: bringg-quotes-api
- description: The Recurring Orders API from Bringg — 3 operation(s) for recurring orders.
  name: Bringg Recurring Orders API
  slug: bringg-recurring-orders-api
- description: The Routes API from Bringg — 4 operation(s) for routes.
  name: Bringg Routes API
  slug: bringg-routes-api
- description: The Service Areas API from Bringg — 8 operation(s) for service areas.
  name: Bringg Service Areas API
  slug: bringg-service-areas-api
- description: The Service Plans API from Bringg — 4 operation(s) for service plans.
  name: Bringg Service Plans API
  slug: bringg-service-plans-api
- description: The Shifts API from Bringg — 2 operation(s) for shifts.
  name: Bringg Shifts API
  slug: bringg-shifts-api
- description: The Teams API from Bringg — 8 operation(s) for teams.
  name: Bringg Teams API
  slug: bringg-teams-api
- description: The Users API from Bringg — 6 operation(s) for users.
  name: Bringg Users API
  slug: bringg-users-api
- description: The Vehicle Profiles API from Bringg — 5 operation(s) for vehicle profiles.
  name: Bringg Vehicle Profiles API
  slug: bringg-vehicle-profiles-api
- description: The Vehicles API from Bringg — 8 operation(s) for vehicles.
  name: Bringg Vehicles API
  slug: bringg-vehicles-api
- description: The Waypoints API from Bringg — 6 operation(s) for waypoints.
  name: Bringg Waypoints API
  slug: bringg-waypoints-api
- description: The Webhooks API from Bringg — 7 operation(s) for webhooks.
  name: Bringg Webhooks API
  slug: bringg-webhooks-api
artifact_total: 141
asyncapis:
- description: Bringg sends server-to-server webhook callbacks to subscriber URLs when events occur on orders, drivers, runs, customers, and waypoints. Bringg retries failed deliveries three times before recording t
  name: Bringg Webhooks
  slug: bringg-webhooks-asyncapi
collections:
- collection_type: postman
  name: Bringg Delivery Hub Administration API
  slug: postman-bringg-administration-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Analytics API
  slug: postman-bringg-analytics-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Authentication API
  slug: postman-bringg-authentication-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Blackouts API
  slug: postman-bringg-blackouts-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Bulk API
  slug: postman-bringg-bulk-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Customers API
  slug: postman-bringg-customers-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Delivery Blocks API
  slug: postman-bringg-delivery-blocks-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Delivery Slots API
  slug: postman-bringg-delivery-slots-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Drivers API
  slug: postman-bringg-drivers-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Floating Inventory API
  slug: postman-bringg-floating-inventory-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Inventory API
  slug: postman-bringg-inventory-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Notes API
  slug: postman-bringg-notes-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Operations API
  slug: postman-bringg-operations-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Order Configurations API
  slug: postman-bringg-order-configurations-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Orders API
  slug: postman-bringg-orders-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Packages API
  slug: postman-bringg-packages-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Parking Spots API
  slug: postman-bringg-parking-spots-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Planned Routes API
  slug: postman-bringg-planned-routes-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Quotes API
  slug: postman-bringg-quotes-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Recurring Orders API
  slug: postman-bringg-recurring-orders-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Routes API
  slug: postman-bringg-routes-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Service Areas API
  slug: postman-bringg-service-areas-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Service Plans API
  slug: postman-bringg-service-plans-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Shifts API
  slug: postman-bringg-shifts-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Teams API
  slug: postman-bringg-teams-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Users API
  slug: postman-bringg-users-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Vehicle Profiles API
  slug: postman-bringg-vehicle-profiles-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Vehicles API
  slug: postman-bringg-vehicles-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Waypoints API
  slug: postman-bringg-waypoints-api
- collection_type: postman
  name: Bringg Delivery Hub Administration Webhooks API
  slug: postman-bringg-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bringg Delivery Hub Administration API
  slug: open-bringg-administration-api
- collection_type: open
  name: Bringg Delivery Hub Administration Analytics API
  slug: open-bringg-analytics-api
- collection_type: open
  name: Bringg Delivery Hub Administration Authentication API
  slug: open-bringg-authentication-api
- collection_type: open
  name: Bringg Delivery Hub Administration Blackouts API
  slug: open-bringg-blackouts-api
- collection_type: open
  name: Bringg Delivery Hub Administration Bulk API
  slug: open-bringg-bulk-api
- collection_type: open
  name: Bringg Delivery Hub Administration Customers API
  slug: open-bringg-customers-api
- collection_type: open
  name: Bringg Delivery Hub Administration Delivery Blocks API
  slug: open-bringg-delivery-blocks-api
- collection_type: open
  name: Bringg Delivery Hub API
  slug: open-bringg-delivery-hub-api
- collection_type: open
  name: Bringg Delivery Hub Administration Delivery Slots API
  slug: open-bringg-delivery-slots-api
- collection_type: open
  name: Bringg Delivery Hub Administration Drivers API
  slug: open-bringg-drivers-api
- collection_type: open
  name: Bringg Drivers and Shifts API
  slug: open-bringg-drivers-shifts-api
- collection_type: open
  name: Bringg Fleet Partners (Self-Integrated Fleets) API
  slug: open-bringg-fleet-partners-api
- collection_type: open
  name: Bringg Delivery Hub Administration Floating Inventory API
  slug: open-bringg-floating-inventory-api
- collection_type: open
  name: Bringg Delivery Hub Administration Inventory API
  slug: open-bringg-inventory-api
- collection_type: open
  name: Bringg Delivery Hub Administration Notes API
  slug: open-bringg-notes-api
- collection_type: open
  name: Bringg Delivery Hub Administration Operations API
  slug: open-bringg-operations-api
- collection_type: open
  name: Bringg Delivery Hub Administration Order Configurations API
  slug: open-bringg-order-configurations-api
- collection_type: open
  name: Bringg Delivery Hub Administration Orders API
  slug: open-bringg-orders-api
- collection_type: open
  name: Bringg Delivery Hub Administration Packages API
  slug: open-bringg-packages-api
- collection_type: open
  name: Bringg Delivery Hub Administration Parking Spots API
  slug: open-bringg-parking-spots-api
- collection_type: open
  name: Bringg Delivery Hub Administration Planned Routes API
  slug: open-bringg-planned-routes-api
- collection_type: open
  name: Bringg Delivery Hub Administration Quotes API
  slug: open-bringg-quotes-api
- collection_type: open
  name: Bringg Delivery Hub Administration Recurring Orders API
  slug: open-bringg-recurring-orders-api
- collection_type: open
  name: Bringg Delivery Hub Administration Routes API
  slug: open-bringg-routes-api
- collection_type: open
  name: Bringg Delivery Hub Administration Service Areas API
  slug: open-bringg-service-areas-api
- collection_type: open
  name: Bringg Delivery Hub Administration Service Plans API
  slug: open-bringg-service-plans-api
- collection_type: open
  name: Bringg Delivery Hub Administration Shifts API
  slug: open-bringg-shifts-api
- collection_type: open
  name: Bringg Delivery Hub Administration Teams API
  slug: open-bringg-teams-api
- collection_type: open
  name: Bringg Delivery Hub Administration Users API
  slug: open-bringg-users-api
- collection_type: open
  name: Bringg Delivery Hub Administration Vehicle Profiles API
  slug: open-bringg-vehicle-profiles-api
- collection_type: open
  name: Bringg Delivery Hub Administration Vehicles API
  slug: open-bringg-vehicles-api
- collection_type: open
  name: Bringg Delivery Hub Administration Waypoints API
  slug: open-bringg-waypoints-api
- collection_type: open
  name: Bringg Delivery Hub Administration Webhooks API
  slug: open-bringg-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bringg/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bringg-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bringg-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bringg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bringg-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bringg-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bringg.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bringg.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bringg.com/reference/welcome-to-bringgs-api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bringg.com/v2.0/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bringg.com/docs/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.bringg.com/docs/bringg-api-access-management
- group: auth
  title: ''
  type: Authentication
  url: https://developers.bringg.com/docs/oauth-20-urls
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.bringg.com/docs/errors
- group: design
  title: ''
  type: Webhooks
  url: https://developers.bringg.com/docs/bringg-webhooks
- group: design
  title: ''
  type: Webhooks
  url: https://developers.bringg.com/reference/webhooks-index
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bringg.com/docs/webhook-authentication-methods
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bringg.com/docs/data-formatting
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bringg.com/docs/bringg-system-requirements
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.bringg.com/reference/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bringg.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.bringg.com/reference/terms-of-service
- group: other
  title: ''
  type: KnowledgeBase
  url: https://help.bringg.com
- group: company
  title: ''
  type: Blog
  url: https://www.bringg.com/resources/blog
- group: start
  title: ''
  type: Portal
  url: https://www.bringg.com/platform/
- group: start
  title: ''
  type: Portal
  url: https://www.bringg.com/carrier-network/
- group: start
  title: ''
  type: Portal
  url: https://www.bringg.com/about/
- group: build
  title: ''
  type: SDKs
  url: https://developers.bringg.com/docs/dashboard-sdk-resources
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bringg/Bringg-iOS-DriverSDK
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bringg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bringg
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/bringg
- group: start
  title: ''
  type: Signup
  url: https://www.bringg.com/contact-us/
- group: commercial
  title: ''
  type: Plans
  url: plans/bringg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bringg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bringg-finops.yml
- group: other
  title: ''
  type: Modules
  url: ''
created: '2026-05-25T00:00:00.000Z'
description: Bringg is a last-mile delivery and fulfillment orchestration platform headquartered in Tel Aviv (founded 2013, CEO Guy Bloch). The Bringg platform combines modular software (Shopping Experience, Plan, Dispatch, Drive, Delivery Experience, Automation Center, Intelligence, Connect) with the Bringg Carrier Network — 250+ pre-integrated third-party, crowdsourced, and autonomous carriers across 70+ countries — to give enterprise retailers and logistics providers a single integration point for orchestrating own-fleet and partner-fleet deliveries. Bringg's developer surface exposes a REST Delivery Hub API for orders/runs/customers/teams/service areas/service plans/delivery slots/blackouts/inventory/packages, a Drivers & Shifts API for users/shifts/delivery-blocks/vehicles, a Fleet Partners API for self-integrated carriers, 50+ outbound webhook event types, and JavaScript/iOS/Android SDKs powering the Dispatcher and Driver apps. All HTTP APIs use OAuth 2.0 Client Credentials Grant against
  region-specific GCP base URLs (US2/US3/US4, EU2/EU3) — visible on status.bringg.com. Bringg counts 800+ customers including Best Buy, AutoZone, ASDA, Wegmans, FedEx Office, Metro, uBreakiFix, and B&Q, and processes 200 million annual deliveries.
examples:
- key_count: 2
  name: Bringg Create Task Example
  slug: bringg-create-task-example
features:
- Last-mile delivery orchestration across own fleet and third-party fleets in a single platform
- Modular product suite — Shopping Experience, Plan, Dispatch, Drive, Delivery Experience
- Bringg Connect carrier network with 250+ third-party, crowdsourced, and autonomous carriers across 70+ countries
- Automation Center for no-code workflow automation
- Intelligence module for dashboards, reporting, and cost/profit/driver-performance insights
- REST APIs for orders, runs, drivers, vehicles, service areas, service plans, planned delivery windows, blackouts, packages, inventory, floating inventory
- 50+ outbound webhook event types covering order, driver, run, customer, waypoint, and inventory lifecycle
- OAuth 2.0 Client Credentials Grant authentication with configurable token TTLs (default 30 min write, 4 hr read)
- Regional deployments on Google Cloud Platform (US2, US3, US4, EU2, EU3) with per-region status and billing
- JSONL bulk upload pipeline (prepare/upload/process/results) for large data loads
- Bringg Driver App (iOS, Android) with offline support, geofence-powered visibility, and configurable workflows
- Bringg Dispatcher web app and JavaScript SDK for embedded dispatch UX
- Bringg Services — tokenless, GUID-based URLs for limited merchant operations without auth
- Quotes and Availability API for multi-carrier quoting before order placement
- Recurring orders, delivery blocks, vehicle profiles, parking spots, and service-area polygons
- Statuspage at status.bringg.com with per-region component status across 13 components (Auth, API, Customer Experience, Delivery Partners, Dispatch, Driver App, Geolocation, Infrastructure, Inventory, Notifications, Planning, Reporting, Billing)
- Used by enterprise retailers including Best Buy, AutoZone, ASDA, Wegmans, FedEx Office, Metro, uBreakiFix, and B&Q
- 800+ customers and 200 million annual deliveries
finops:
- name: Bringg Finops
  service_category: ''
  slug: bringg-finops
graphqls:
- description: 'Conceptual GraphQL schema for the [Bringg Delivery Hub API](https://developers.bringg.com/reference/welcome-to-bringgs-api-reference), derived from Bringg''s REST API surface: the Delivery Hub API, Dri'
  name: Bringg GraphQL Schema
  slug: bringg-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bringg.png
integrations:
- category: Carriers and crowdsourced fleets
  examples:
  - DoorDash
  - Postmates
  - Uber
  - Lyft
  - Glovo
  - Bringg Carrier Network 250+
- category: OMS / ERP
  description: REST APIs and webhooks for OMS/ERP synchronization.
- category: eCommerce
  description: Order intake and shopping-experience integration.
- category: WMS / TMS
  description: Warehouse and transportation system integration.
json_schemas:
- name: Bringg Customer
  property_count: 16
  slug: bringg-customer
- name: Bringg Driver (User)
  property_count: 12
  slug: bringg-driver
- name: Bringg Order (Task)
  property_count: 20
  slug: bringg-order
- name: Bringg Run (Route)
  property_count: 11
  slug: bringg-run
- name: Bringg Waypoint
  property_count: 14
  slug: bringg-waypoint
json_structures:
- name: Bringg Order Structure
  property_count: 8
  slug: bringg-order-structure
jsonld:
- class_count: 24
  name: Bringg Context
  property_count: 0
  slug: bringg-context
layout: provider
modified: '2026-05-25'
name: Bringg
nav: Providers
network: true
overview: 'Bringg publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Analytics API, Authentication API, and 27 more. Tagged areas include Last Mile Delivery, Delivery Orchestration, Fulfillment, Logistics, and Retail.


  The Bringg catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Bringg''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, signup flow, and 29 more developer resources.'
plans:
- name: Bringg Plans Pricing
  plan_count: 1
  slug: bringg-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Bringg Rate Limits
  slug: bringg-rate-limits
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: Bringg API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: bringg-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Bringg API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bringg-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Bringg API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: bringg-rules
scopes:
- name: Bringg Scopes
  scope_count: 25
  slug: bringg-scopes
  summary_line: 25 scopes · clientCredentials
score:
  band: strong
  composite: 58.7
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 13.6
    contract_quality: 75.8
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 61.8
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bringg/refs/heads/main/screenshots/bringg-2026-06-20T173708.png
security:
- kind: authentication
  name: Bringg Authentication
  slug: bringg-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bringg Domain Security
  slug: bringg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bringg Trust Center
  slug: bringg-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: bringg
solutions:
- description: Enable same-day, scheduled, and curbside fulfillment for enterprise retailers.
  name: Retail Same-Day Delivery
- description: Orchestrate return pickups and reverse logistics.
  name: Returns
- description: Plug into 250+ pre-integrated third-party fleets through a single integration.
  name: Carrier Network Access
- description: Equip drivers with the Bringg Driver App, optimized routes, and geofence-aware workflows.
  name: Driver Productivity
tags:
- Last Mile Delivery
- Delivery Orchestration
- Fulfillment
- Logistics
- Retail
- Dispatch
- Routing
- Driver App
- Carrier Network
- Fleet Management
- Supply Chain
- E-Commerce
- Same-Day Delivery
- Curbside Pickup
- Returns
website: https://www.bringg.com
---
