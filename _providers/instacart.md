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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Instacart Agentic Access
  operation_count: 23
  slug: instacart-agentic-access
  summary_line: 23 operations · 19 acting
api_count: 10
apis:
- description: Instacart Shopping Widgets are front-end web components that retailers can embed into their websites to add e-commerce functionalities powered by Instacart without interacting with any API directly. T
  name: Instacart Shopping Widgets
  slug: shopping-widgets
- description: Endpoints for obtaining and managing OAuth 2.0 access tokens used to authenticate API requests.
  name: instacart Authentication API
  slug: instacart-authentication-api
- description: Endpoints for shopper-customer communication including sending and retrieving chat messages.
  name: instacart Chat API
  slug: instacart-chat-api
- description: Endpoints for finding delivery stores, previewing time slots, reserving time slots, and creating delivery orders.
  name: instacart Delivery API
  slug: instacart-delivery-api
- description: Endpoints for updating item-level attributes such as pricing and availability at specific store locations. Items contain information that can vary from one store to another.
  name: instacart Items API
  slug: instacart-items-api
- description: Endpoints for last mile delivery where items are pre-packed and only require delivery from the store to the customer.
  name: instacart Last Mile Delivery API
  slug: instacart-last-mile-delivery-api
- description: Endpoints for retrieving order status, handling details, and item information after checkout.
  name: instacart Orders API
  slug: instacart-orders-api
- description: Endpoints for finding pickup stores, previewing time slots, reserving time slots, and creating pickup orders.
  name: instacart Pickup API
  slug: instacart-pickup-api
- description: Endpoints for creating and updating products in the retailer's catalog on Instacart. Products are the same across all of a retailer's stores.
  name: instacart Products API
  slug: instacart-products-api
- description: Endpoints for managing item replacements suggested by shoppers during order fulfillment.
  name: instacart Replacements API
  slug: instacart-replacements-api
artifact_total: 72
asyncapis:
- description: Instacart Connect notifies retailers of order status changes and fulfillment events through webhook callbacks. Retailers configure callback endpoints to receive real-time notifications about order lif
  name: Instacart Connect Event Callbacks
  slug: instacart-connect-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Instacart Catalog Authentication API
  slug: open-instacart-authentication-api
- collection_type: open
  name: Instacart Catalog API
  slug: open-instacart-catalog-api
- collection_type: open
  name: Instacart Catalog Authentication Chat API
  slug: open-instacart-chat-api
- collection_type: open
  name: Instacart Connect Fulfillment API
  slug: open-instacart-connect-fulfillment-api
- collection_type: open
  name: Instacart Connect Post-Checkout API
  slug: open-instacart-connect-post-checkout-api
- collection_type: open
  name: Instacart Catalog Authentication Delivery API
  slug: open-instacart-delivery-api
- collection_type: open
  name: Instacart Developer Platform API
  slug: open-instacart-developer-platform-api
- collection_type: open
  name: Instacart Catalog Authentication Items API
  slug: open-instacart-items-api
- collection_type: open
  name: Instacart Catalog Authentication Last Mile Delivery API
  slug: open-instacart-last-mile-delivery-api
- collection_type: open
  name: Instacart Catalog Authentication Orders API
  slug: open-instacart-orders-api
- collection_type: open
  name: Instacart Catalog Authentication Pickup API
  slug: open-instacart-pickup-api
- collection_type: open
  name: Instacart Catalog Authentication Products API
  slug: open-instacart-products-api
- collection_type: open
  name: Instacart Catalog Authentication Replacements API
  slug: open-instacart-replacements-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instacart-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/instacart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instacart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/instacart-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instacart
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instacart
- group: design
  title: ''
  type: JSONLD
  url: json-ld/instacart-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instacart-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/instacart-product-schema.json
description: Use the public Instacart APIs to add Instacart shopping capabilities to your applications, such as product shopping lists and recipe ingredients.
finops:
- name: Instacart Finops
  service_category: Marketplace + Logistics
  slug: instacart-finops
graphqls:
- description: This conceptual GraphQL schema models the Instacart grocery delivery and retail platform. Instacart provides APIs for retailers, brands, and developers to integrate grocery shopping, delivery, fulfill
  name: Instacart GraphQL Schema
  slug: instacart-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instacart.png
json_schemas:
- name: CartItem
  property_count: 3
  slug: instacart-cartitem
- name: ChatMessage
  property_count: 4
  slug: instacart-chatmessage
- name: ChatMessagesResponse
  property_count: 1
  slug: instacart-chatmessagesresponse
- name: CreateOrderRequest
  property_count: 4
  slug: instacart-createorderrequest
- name: Error
  property_count: 2
  slug: instacart-error
- name: FindStoresRequest
  property_count: 7
  slug: instacart-findstoresrequest
- name: Ingredient
  property_count: 6
  slug: instacart-ingredient
- name: Item
  property_count: 10
  slug: instacart-item
- name: ItemSubmissionRequest
  property_count: 1
  slug: instacart-itemsubmissionrequest
- name: LineItem
  property_count: 8
  slug: instacart-lineitem
- name: Instacart Order
  property_count: 12
  slug: instacart-order
- name: OrderHandlingResponse
  property_count: 6
  slug: instacart-orderhandlingresponse
- name: OrderItem
  property_count: 5
  slug: instacart-orderitem
- name: OrderItemsResponse
  property_count: 1
  slug: instacart-orderitemsresponse
- name: OrderResponse
  property_count: 7
  slug: instacart-orderresponse
- name: PostCheckoutOrderItem
  property_count: 6
  slug: instacart-postcheckoutorderitem
- name: PreviewServiceOptionsRequest
  property_count: 2
  slug: instacart-previewserviceoptionsrequest
- name: Instacart Product
  property_count: 12
  slug: instacart-product
- name: ProductsLinkResponse
  property_count: 1
  slug: instacart-productslinkresponse
- name: ProductSubmissionRequest
  property_count: 1
  slug: instacart-productsubmissionrequest
- name: RecipeRequest
  property_count: 10
  slug: instacart-reciperequest
- name: Replacement
  property_count: 3
  slug: instacart-replacement
- name: ReplacementDecisionRequest
  property_count: 1
  slug: instacart-replacementdecisionrequest
- name: ReplacementResponse
  property_count: 2
  slug: instacart-replacementresponse
- name: ReserveTimeSlotRequest
  property_count: 2
  slug: instacart-reservetimeslotrequest
- name: SendMessageRequest
  property_count: 1
  slug: instacart-sendmessagerequest
- name: ServiceOption
  property_count: 5
  slug: instacart-serviceoption
- name: ServiceOptionHoldResponse
  property_count: 3
  slug: instacart-serviceoptionholdresponse
- name: ServiceOptionsResponse
  property_count: 1
  slug: instacart-serviceoptionsresponse
- name: ShoppingListRequest
  property_count: 7
  slug: instacart-shoppinglistrequest
- name: Store
  property_count: 4
  slug: instacart-store
- name: StoresResponse
  property_count: 1
  slug: instacart-storesresponse
- name: SubmissionResponse
  property_count: 4
  slug: instacart-submissionresponse
- name: TokenRequest
  property_count: 4
  slug: instacart-tokenrequest
- name: TokenResponse
  property_count: 5
  slug: instacart-tokenresponse
json_structures:
- name: Instacart Structure
  property_count: 0
  slug: instacart-structure
jsonld:
- class_count: 0
  name: Instacart Context
  property_count: 8
  slug: instacart-context
layout: provider
modified: '2026-05-19'
name: instacart
nav: Providers
network: true
overview: 'instacart publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Chat API, Delivery API, and 6 more.


  The instacart catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  instacart''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Instacart Plans Pricing
  plan_count: 2
  slug: instacart-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 1
  name: Instacart Rate Limits
  slug: instacart-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: instacart API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: instacart-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: instacart API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: instacart-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.2
  delta: -4.6
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 11.4
    contract_quality: 75.1
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 11.4
    operational_transparency: 7.9
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instacart/refs/heads/main/screenshots/instacart-2026-06-20T183414.png
security:
- kind: authentication
  name: Instacart Authentication
  slug: instacart-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Instacart Domain Security
  slug: instacart-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Instacart Vulnerability Disclosure
  slug: instacart-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: instacart
---
