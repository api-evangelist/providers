---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: half
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Instacart Agentic Access
  operation_count: 24
  slug: instacart-agentic-access
  summary_line: 24 operations · 17 acting
api_count: 5
apis:
- description: Instacart Shopping Widgets are front-end web components that retailers can embed into their websites to add e-commerce functionalities powered by Instacart without interacting with any API directly. T
  name: Instacart Shopping Widgets
  slug: shopping-widgets
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for obtaining and managing OAuth 2.0 access tokens used to authenticate API requests.
  name: instacart Authentication API
  phrasing_intents:
  - id: generateAccessToken
    intent: Get an OAuth access token for the API
    question: How do I get a bearer token to call the Instacart Connect APIs?
  phrasing_ops: 1
  slug: instacart-authentication-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for shopper-customer communication including sending and retrieving chat messages.
  name: instacart Chat API
  phrasing_intents:
  - id: getChatMessages
    intent: Read the shopper chat for an order
    question: How can I see what the customer and shopper have said to each other about an order?
  - id: sendChatMessage
    intent: Send a message to the order's shopper
    question: How do I message the shopper who is picking my order?
  phrasing_ops: 2
  slug: instacart-chat-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for finding delivery stores, previewing time slots, reserving time slots, and creating delivery orders.
  name: instacart Delivery API
  phrasing_intents:
  - id: findDeliveryStores
    intent: Find stores that deliver to a location
    question: Which stores can deliver groceries to a given address?
  - id: previewDeliveryTimeSlots
    intent: Preview available delivery time slots
    question: What delivery windows can I show a customer before checkout?
  - id: reserveDeliveryTimeSlot
    intent: Hold a delivery time slot
    question: How do I hold a delivery window for a customer before placing the order?
  - id: createDeliveryOrder
    intent: Place a delivery order
    question: How do I place a grocery delivery order after reserving a time slot?
  - id: getOrder
    intent: Look up an order's status and details
    question: What is the current status of a customer's grocery order?
  - id: cancelOrder
    intent: Cancel an order before a shopper takes it
    question: How do I cancel a delivery or pickup order?
  phrasing_ops: 6
  slug: instacart-delivery-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for updating item-level attributes such as pricing and availability at specific store locations. Items contain information that can vary from one store to another.
  name: instacart Items API
  phrasing_intents:
  - id: submitItems
    intent: Update store-level item prices and stock
    question: How do I update pricing and availability for products at a specific store?
  phrasing_ops: 1
  slug: instacart-items-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for last mile delivery where items are pre-packed and only require delivery from the store to the customer.
  name: instacart Last Mile Delivery API
  phrasing_intents:
  - id: findLastMileStores
    intent: Find stores offering last mile delivery
    question: Which stores can handle last mile delivery of pre-packed orders to an address?
  - id: previewLastMileServiceOptions
    intent: Reserve a last mile delivery window
    question: How do I secure a delivery window for a pre-packed last mile order?
  - id: createLastMileOrder
    intent: Place a last mile delivery order
    question: How do I create an order for pre-packed items that only need transport to the customer?
  - id: stageLastMileOrder
    intent: Mark a last mile order packed and ready
    question: How do I tell the driver a last mile order is packed and ready at the store?
  phrasing_ops: 4
  slug: instacart-last-mile-delivery-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for retrieving order status, handling details, and item information after checkout.
  name: instacart Orders API
  phrasing_intents:
  - id: getOrderHandling
    intent: Get an order's address, shopper and notes
    question: Who is the shopper on an order and what address is it going to?
  - id: getOrderItems
    intent: Track item status and replacements in an order
    question: How can I see which items in an order have been picked or replaced?
  phrasing_ops: 2
  slug: instacart-orders-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for finding pickup stores, previewing time slots, reserving time slots, and creating pickup orders.
  name: instacart Pickup API
  phrasing_intents:
  - id: findPickupStores
    intent: Find stores offering pickup
    question: Which nearby stores let a customer pick up their order?
  - id: previewPickupTimeSlots
    intent: Preview available pickup time slots
    question: What pickup times can I offer a customer before checkout?
  - id: createPickupOrder
    intent: Place a pickup order
    question: How do I place an order the customer will collect in store?
  phrasing_ops: 3
  slug: instacart-pickup-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for creating and updating products in the retailer's catalog on Instacart. Products are the same across all of a retailer's stores.
  name: instacart Products API
  phrasing_intents:
  - id: submitProducts
    intent: Add or update catalog products
    question: How do I add new products to my retailer catalog?
  - id: createShoppingListPage
    intent: Create a shareable shopping list page
    question: How do I generate a link to a shopping list that people can add to their cart?
  - id: createRecipePage
    intent: Create a shoppable recipe page
    question: How do I publish a recipe page where readers can buy the ingredients?
  phrasing_ops: 3
  slug: instacart-products-api
- baseURL: https://connect.instacart.com
  baseurl_source: declared
  description: Endpoints for managing item replacements suggested by shoppers during order fulfillment.
  name: instacart Replacements API
  phrasing_intents:
  - id: updateItemReplacement
    intent: Approve or reject a shopper's replacement
    question: How does a customer accept a substitute the shopper picked?
  phrasing_ops: 1
  slug: instacart-replacements-api
- description: Instacart's first-party remote Model Context Protocol server. Production endpoint https://mcp.instacart.com/mcp over Streamable HTTP, authenticated with a Developer Platform API key as an Authorizatio
  name: Instacart Developer Platform MCP Server
  slug: instacart-mcp-server
- baseURL: https://dboktu48tbzl9.cloudfront.net/{retailer-name}/evergreen
  baseurl_source: declared
  description: The Rest API from instacart — 1 operation(s) for rest.
  name: instacart Rest API
  phrasing_intents:
  - id: create
    intent: Turn recipe ingredients into a shopping link
    question: How can a chat assistant turn a recipe into a link to buy the ingredients?
  phrasing_ops: 1
  slug: instacart-rest-api
artifact_total: 79
asyncapis:
- description: Instacart Connect notifies retailers of order status changes and fulfillment events through webhook callbacks. Retailers configure callback endpoints to receive real-time notifications about order lif
  name: Instacart Connect Event Callbacks
  slug: instacart-connect-events-asyncapi
collections:
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
- group: company
  title: ''
  type: Blog
  url: https://company.instacart.com/blog
- group: company
  title: ''
  type: Website
  url: https://www.instacart.com/
- group: other
  href: https://artifacts.apis.io/instacart/capabilities/instacart-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/instacart-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/instacart/overlays/instacart-llm-integration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/instacart-llm-integration-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/instacart/agentic-access/instacart-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/instacart-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/instacart/security/instacart-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/instacart-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/instacart/security/instacart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instacart-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/instacart/authentication/instacart-authentication.yml
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
  href: https://artifacts.apis.io/instacart/json-ld/instacart-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/instacart-context.jsonld
- group: docs
  href: https://artifacts.apis.io/instacart/json-schema/instacart-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/instacart-order-schema.json
- group: docs
  href: https://artifacts.apis.io/instacart/json-schema/instacart-product-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/instacart-product-schema.json
- group: agent
  href: https://artifacts.apis.io/instacart/well-known/instacart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/instacart-well-known.yml
- group: auth
  href: https://artifacts.apis.io/instacart/well-known/instacart-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/instacart-security.txt
- group: agent
  href: https://artifacts.apis.io/instacart/mcp/instacart-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/instacart-mcp.yml
- group: build
  href: https://artifacts.apis.io/instacart/mcp/instacart-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/instacart-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/instacart/llms/instacart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instacart-llms.txt
- group: agent
  href: https://artifacts.apis.io/instacart/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/instacart/conformance/instacart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instacart-conformance.yml
- group: design
  href: https://artifacts.apis.io/instacart/errors/instacart-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instacart-problem-types.yml
- group: design
  href: https://artifacts.apis.io/instacart/lifecycle/instacart-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/instacart-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/instacart/scopes/instacart-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/instacart-scopes.yml
- group: design
  href: https://artifacts.apis.io/instacart/conventions/instacart-conventions.yml
  title: ''
  type: Conventions
  url: conventions/instacart-conventions.yml
- group: start
  href: https://artifacts.apis.io/instacart/sandbox/instacart-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/instacart-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/instacart/changelog/instacart-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/instacart-changelog.yml
- group: design
  href: https://artifacts.apis.io/instacart/components/instacart-components.yml
  title: ''
  type: Components
  url: components/instacart-components.yml
- group: design
  href: https://artifacts.apis.io/instacart/data-model/instacart-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instacart-data-model.yml
- group: build
  href: https://artifacts.apis.io/instacart/packages/instacart-packages.yml
  title: ''
  type: Packages
  url: packages/instacart-packages.yml
- group: commercial
  href: https://artifacts.apis.io/instacart/plans/instacart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/instacart-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/instacart/rate-limits/instacart-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/instacart-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/instacart/finops/instacart-finops.yml
  title: ''
  type: FinOps
  url: finops/instacart-finops.yml
- group: design
  href: https://artifacts.apis.io/instacart/vocabulary/instacart-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/instacart-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/instacart/json-structure/instacart-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/instacart-structure.json
- group: design
  href: https://artifacts.apis.io/instacart/asyncapi/instacart-connect-events-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/instacart-connect-events-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/instacart/asyncapi/instacart-connect-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/instacart-connect-events-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/instacart/rules/instacart-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/instacart-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/instacart/rules/instacart-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/instacart-jsonschema-spectral-rules.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/instacart
- group: operate
  title: ''
  type: StatusPage
  url: https://enterprise-status.instacart.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.instacart.com/connect/api/fulfillment/deprecated
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.instacart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instacart.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.instacart.com/developer_platform_api/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.instacart.com/developer_platform_api/get_started/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.instacart.com/developer_platform_api/api/changelog
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.instacart.com/developer_platform_api/api/error_and_status_codes
- group: auth
  title: ''
  type: Authentication
  url: https://docs.instacart.com/connect/api/authentication
- group: operate
  title: ''
  type: Support
  url: https://instacart.atlassian.net/servicedesk/customer/portal/1
- group: operate
  title: ''
  type: FAQ
  url: https://docs.instacart.com/developer_platform_api/faq
- group: company
  title: ''
  type: Blog
  url: https://tech.instacart.com/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.instacart.com/
- group: start
  title: ''
  type: Portal
  url: https://dashboard.instacart.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instacart.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instacart.com/privacy
- group: commercial
  title: ''
  type: DeveloperTerms
  url: https://docs.instacart.com/developer_platform_api/guide/terms_and_policies/developer_terms
created: '2026-05-04'
description: 'Instacart (Maplebear Inc.) is a North American grocery technology company that operates the Instacart Marketplace and sells its underlying commerce, fulfillment, catalog, advertising and storefront technology to retailers and brands. Its published API surface splits cleanly in two. The Instacart Developer Platform API is open to app and website developers, costs nothing, and exposes two shoppable-page operations plus a nearby-retailers lookup at connect.instacart.com/idp/v1 -- and, unusually, Instacart pays the developer, commissioning attributed orders through an Impact affiliate programme. Instacart Connect is the enterprise half: OAuth 2.0, partner-gated Fulfillment, Post-checkout, Transaction and Sandbox APIs, the Catalog API, Carrot Ads and Shopping Widgets, all bundled into a retailer or brand partner agreement. Instacart also runs a first-party remote Model Context Protocol server at https://mcp.instacart.com/mcp whose tools/list is served anonymously, making it one
  of the few grocery-sector providers with a directly reachable agent surface.'
finops:
- has_sources: true
  method: derived
  name: Instacart Finops
  primary_unit: ''
  service_category: ''
  slug: instacart-finops
  template: true
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
mcp_servers:
- description: Instacart publishes a first-party, remote Model Context Protocol server that exposes the Instacart Developer Platform's two shoppable-page operations as MCP tools. The production endpoint is https://m
  name: Instacart Developer Platform MCP Server
  slug: instacart-developer-platform-mcp-server
modified: '2026-10-06'
name: Instacart
nav: Providers
network: true
overview: 'Instacart publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Chat API, Delivery API, and 9 more. Tagged areas include Grocery, E-Commerce, Marketplace, Retail, and Logistics.


  The Instacart catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Instacart''s developer surface includes engineering blog, authentication, sandbox, changelog, documentation, API reference, getting-started guide, and 49 more developer resources.'
plans:
- name: Instacart Plans Pricing
  plan_count: 3
  slug: instacart-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Instacart Rate Limits
  slug: instacart-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Instacart — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: instacart-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Instacart — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: instacart-jsonschema-spectral-rules
scopes:
- name: Instacart Scopes
  scope_count: 6
  slug: instacart-scopes
  summary_line: 6 scopes
score:
  band: exemplar
  composite: 70.0
  coverage:
    artifact_dirs: 37
    catalog_earned: 74.0
    catalog_earned_first_party: 20.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 63.6
    developer_ergonomics: 66.1
    discoverability: 80.0
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/instacart/instacart-2026-06-20T183414.png
security:
- kind: authentication
  name: Instacart Authentication
  slug: instacart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Instacart Domain Security
  slug: instacart-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Instacart Vulnerability Disclosure
  slug: instacart-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 5
skills:
- name: instacart-create-shoppable-recipe
  slug: instacart-create-shoppable-recipe
- name: instacart-create-shopping-list
  slug: instacart-create-shopping-list
- name: instacart-place-delivery-order
  slug: instacart-place-delivery-order
- name: instacart-submit-catalog-data
  slug: instacart-submit-catalog-data
- name: instacart-track-order-post-checkout
  slug: instacart-track-order-post-checkout
slug: instacart
tags:
- Grocery
- E-Commerce
- Marketplace
- Retail
- Logistics
- Last Mile Delivery
- Fulfillment
- Catalog
- Advertising
- Agents
- MCP
- Agentic Commerce
website: https://www.instacart.com/
---
