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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Manhattan Associates Agentic Access
  operation_count: 17
  slug: manhattan-associates-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 9
apis:
- description: Manhattan Active Platform APIs provide core platform capabilities for authentication, tenant configuration, and integration with Manhattan Active solutions. REST APIs follow OAuth client credentials f
  name: Manhattan Active Platform API
  slug: manhattan-active-platform-api
- description: Manhattan Active Supply Chain Planning APIs provide demand forecasting, inventory optimization, and replenishment planning capabilities to optimize stock levels and reduce carrying costs across supply
  name: Manhattan Active Supply Chain Planning API
  slug: manhattan-active-supply-chain-planning-api
- description: Manhattan Associates provides warehouse management (WMS) and transportation management (TMS) APIs for supply chain execution. APIs enable order management, inventory tracking, shipment planning, labor
  name: Manhattan Associates TMS/WMS API
  slug: manhattan-associates-api
- description: ASN and receipt management
  name: manhattan-associates Inbound API
  slug: manhattan-associates-inbound-api
- description: Real-time inventory positions and ATP
  name: manhattan-associates Inventory API
  slug: manhattan-associates-inventory-api
- description: Order lifecycle and management
  name: manhattan-associates Orders API
  slug: manhattan-associates-orders-api
- description: Outbound order fulfillment and shipment
  name: manhattan-associates Outbound API
  slug: manhattan-associates-outbound-api
- description: Order promising and delivery date estimation
  name: manhattan-associates Promising API
  slug: manhattan-associates-promising-api
- description: Return and exchange processing
  name: manhattan-associates Returns API
  slug: manhattan-associates-returns-api
artifact_total: 54
collections:
- collection_type: open
  name: Manhattan Active Omni Order Management API
  slug: open-manhattan-associates-omni
- collection_type: open
  name: Manhattan Active Supply Chain (WMS) API
  slug: open-manhattan-associates-wms
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/manhattan-associates-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manhattan-associates-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/manhattan-associates-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/manhattan-associates-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manhattan-associates
- group: start
  title: ''
  type: Portal
  url: https://developer.manh.com/
- group: company
  title: ''
  type: Website
  url: https://www.manh.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.manh.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.manh.com/docs/how-to/rest-api/
- group: docs
  title: ''
  type: Documentation
  url: https://api.developer.manh.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.manh.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.manh.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.manh.com/our-insights/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.manh.com/trust-center
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/openapi/manhattan-associates-omni-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/openapi/manhattan-associates-wms-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/json-schema/manhattan-associates-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/json-ld/manhattan-associates-context.jsonld
description: Manhattan Associates is a leading provider of supply chain commerce solutions, enabling unified commerce across stores, warehouses, and inventory across the supply chain.
finops:
- name: Manhattan Associates Finops
  service_category: Supply Chain Software
  slug: manhattan-associates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manhattan-associates.png
json_schemas:
- name: Address
  property_count: 9
  slug: manhattan-associates-address
- name: AvailabilityRequest
  property_count: 3
  slug: manhattan-associates-availabilityrequest
- name: AvailabilityResponse
  property_count: 1
  slug: manhattan-associates-availabilityresponse
- name: ErrorResponse
  property_count: 3
  slug: manhattan-associates-errorresponse
- name: Fulfillment
  property_count: 9
  slug: manhattan-associates-fulfillment
- name: InventoryPosition
  property_count: 8
  slug: manhattan-associates-inventoryposition
- name: InventoryPositionListResponse
  property_count: 2
  slug: manhattan-associates-inventorypositionlistresponse
- name: Manhattan Active Order
  property_count: 13
  slug: manhattan-associates-order
- name: OrderCreateRequest
  property_count: 8
  slug: manhattan-associates-ordercreaterequest
- name: OrderLine
  property_count: 9
  slug: manhattan-associates-orderline
- name: OrderLineRequest
  property_count: 5
  slug: manhattan-associates-orderlinerequest
- name: OrderListResponse
  property_count: 4
  slug: manhattan-associates-orderlistresponse
- name: OrderTotals
  property_count: 6
  slug: manhattan-associates-ordertotals
- name: OrderUpdateRequest
  property_count: 4
  slug: manhattan-associates-orderupdaterequest
- name: OutboundLine
  property_count: 7
  slug: manhattan-associates-outboundline
- name: OutboundOrder
  property_count: 10
  slug: manhattan-associates-outboundorder
- name: OutboundOrderCreateRequest
  property_count: 6
  slug: manhattan-associates-outboundordercreaterequest
- name: OutboundOrderListResponse
  property_count: 2
  slug: manhattan-associates-outboundorderlistresponse
- name: PromiseRequest
  property_count: 4
  slug: manhattan-associates-promiserequest
- name: PromiseResponse
  property_count: 1
  slug: manhattan-associates-promiseresponse
- name: Receipt
  property_count: 8
  slug: manhattan-associates-receipt
- name: ReceiptCreateRequest
  property_count: 5
  slug: manhattan-associates-receiptcreaterequest
- name: ReceiptLine
  property_count: 7
  slug: manhattan-associates-receiptline
- name: ReceiptLineRequest
  property_count: 4
  slug: manhattan-associates-receiptlinerequest
- name: ReceiptListResponse
  property_count: 2
  slug: manhattan-associates-receiptlistresponse
- name: Return
  property_count: 6
  slug: manhattan-associates-return
- name: ReturnRequest
  property_count: 3
  slug: manhattan-associates-returnrequest
- name: ShipAddress
  property_count: 8
  slug: manhattan-associates-shipaddress
- name: ShipmentConfirmRequest
  property_count: 5
  slug: manhattan-associates-shipmentconfirmrequest
- name: Transfer
  property_count: 7
  slug: manhattan-associates-transfer
- name: TransferRequest
  property_count: 4
  slug: manhattan-associates-transferrequest
- name: WarehouseInventoryRecord
  property_count: 11
  slug: manhattan-associates-warehouseinventoryrecord
- name: WarehouseInventoryResponse
  property_count: 2
  slug: manhattan-associates-warehouseinventoryresponse
json_structures:
- name: Manhattan Associates Structure
  property_count: 0
  slug: manhattan-associates-structure
jsonld:
- class_count: 22
  name: Manhattan Associates Context
  property_count: 13
  slug: manhattan-associates-context
layout: provider
modified: '2026-05-19'
name: manhattan-associates
nav: Providers
network: true
overview: 'manhattan-associates publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Inbound API, Inventory API, Orders API, and 3 more.


  The manhattan-associates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  manhattan-associates'' developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, support, and 12 more developer resources.'
plans:
- name: Manhattan Associates Plans Pricing
  plan_count: 2
  slug: manhattan-associates-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 2
  name: Manhattan Associates Rate Limits
  slug: manhattan-associates-rate-limits
rules:
- name: manhattan-associates API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: manhattan-associates-jsonschema-spectral-rules
scopes:
- name: Manhattan Associates Scopes
  scope_count: 5
  slug: manhattan-associates-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 52.2
  delta: -3.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 73.4
    developer_ergonomics: 45.7
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/screenshots/manhattan-associates-2026-06-20T184920.png
security:
- kind: authentication
  name: Manhattan Associates Authentication
  slug: manhattan-associates-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Manhattan Associates Domain Security
  slug: manhattan-associates-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: manhattan-associates
website: https://www.manh.com/
---
