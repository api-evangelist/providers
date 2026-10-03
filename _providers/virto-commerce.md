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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 266
  human_in_the_loop: 9
  name: Virto Commerce Agentic Access
  operation_count: 452
  slug: virto-commerce-agentic-access
  summary_line: 452 operations · 266 acting · 9 human-in-the-loop
api_count: 14
apis:
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Easily manage your products, categories, variations, and properties
  name: Virto Commerce Catalog API
  phrasing_intents:
  - id: AutomaticLinkQuery_Search
    intent: Search automatic category link rules
    question: Which automatic link rules feed products into a virtual category?
  - id: AutomaticLinkQuery_Create
    intent: Create an automatic category link rule
    question: How can a virtual category be filled automatically from a query on another catalog?
  - id: AutomaticLinkQuery_Update
    intent: Update an automatic category link rule
    question: How do I change the source query of an existing automatic link rule?
  - id: AutomaticLinkQuery_Delete
    intent: Delete automatic category link rules
    question: Can I remove automatic link rules I no longer need?
  - id: AutomaticLinkQuery_Get
    intent: Get an automatic category link rule
    question: What source query does a particular automatic link rule run?
  - id: CatalogModuleAssociations_GetProductAssociations
    intent: List one product's associations
    question: Which related, accessory or cross-sell products are linked to this product?
  - id: CatalogModuleAssociations_GetProductsAssociations
    intent: List associations for several products
    question: Can I fetch associations for a whole batch of products at once?
  - id: CatalogModuleAssociations_UpdateAssociations
    intent: Save product associations
    question: How do I link accessories or related items to a product?
  phrasing_ops: 92
  slug: virto-commerce-catalog-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Managing customers contacts and organizations
  name: Virto Commerce Companies and Contacts API
  phrasing_intents:
  - id: CustomerModule_ListOrganizations
    intent: List every organization
    question: Is there a way to pull the full list of organizations without any search filter?
  - id: CustomerModule_SearchMember
    intent: Search members of any type
    question: How do I search across contacts, organizations, employees and vendors in one query?
  - id: CustomerModule_GetMemberById
    intent: Get a member by ID
    question: What does a single member record look like when I fetch it by its ID?
  - id: CustomerModule_PatchMember
    intent: Partially update a member
    question: Can I change just one field on a member without resending the whole record?
  - id: CustomerModule_GetMemberByUserId
    intent: Get the member linked to a user account
    question: Which member record belongs to a given login user account?
  - id: CustomerModule_GetMembersByIds
    intent: Get several members by their IDs
    question: Can I load a batch of members in one request if I already know their IDs?
  - id: CustomerModule_CreateMember
    intent: Create a member of any type
    question: Can I create a new member of any type through one generic endpoint?
  - id: CustomerModule_UpdateMember
    intent: Update a member record
    question: How do I save changes to a member's addresses, phones and emails with a full update?
  phrasing_ops: 45
  slug: virto-commerce-companies-and-contacts-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Simplify inventory management functionality
  name: Virto Commerce Inventory API
  phrasing_intents:
  - id: InventoryModule_SearchInventories
    intent: Search inventory records
    question: How much stock do I have for some products in a given warehouse?
  - id: InventoryModule_SearchProductInventories
    intent: Search a product's inventory by warehouse
    question: Which warehouses actually hold stock of a given product?
  - id: InventoryModule_SearchFulfillmentCenters
    intent: Search fulfillment centers
    question: Which fulfillment centers are registered in Virto Commerce?
  - id: InventoryModule_GetFulfillmentCenter
    intent: Get a fulfillment center by ID
    question: What address and geolocation does a specific fulfillment center have?
  - id: InventoryModule_PatchFulfillmentCenter
    intent: Partially update a fulfillment center
    question: Can I change just one field of a fulfillment center without resending everything?
  - id: InventoryModule_GetFulfillmentCenterByOuterId
    intent: Get a fulfillment center by external ID
    question: How do I find a warehouse using the ID from my ERP system?
  - id: InventoryModule_GetFulfillmentCenters
    intent: Get several fulfillment centers by IDs
    question: Can I fetch a batch of fulfillment centers in one request by their IDs?
  - id: InventoryModule_SaveFulfillmentCenter
    intent: Create or save a fulfillment center
    question: How do I add a new warehouse to Virto Commerce?
  phrasing_ops: 16
  slug: virto-commerce-inventory-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Marketing system with dynamic contents and promotions management
  name: Virto Commerce Marketing API
  phrasing_intents:
  - id: MarketingModuleDynamicContent_DynamicContentPlaceListEntriesSearch
    intent: Browse content place folders and entries
    question: Can I browse content placeholders together with the folders they sit in?
  - id: MarketingModuleDynamicContent_DynamicContentPlacesSearch
    intent: Search dynamic content places
    question: How do I find the placeholders on my storefront where dynamic content can show?
  - id: MarketingModuleDynamicContent_DynamicContentItemsEntriesSearch
    intent: Browse content item folders and entries
    question: Can I browse dynamic content items along with the folders that organize them?
  - id: MarketingModuleDynamicContent_DynamicContentItemsSearch
    intent: Search dynamic content items
    question: How do I find banners or other dynamic content items by keyword?
  - id: MarketingModuleDynamicContent_DynamicContentPublicationsSearch
    intent: Search content publications
    question: Which content publications are currently active for my store?
  - id: MarketingModuleDynamicContent_EvaluateDynamicContent
    intent: Resolve which content to show in a placeholder
    question: What content should display in a storefront placeholder for this shopper right now?
  - id: MarketingModuleDynamicContent_GetDynamicContentById
    intent: Get a dynamic content item
    question: What does a single dynamic content item, like a banner, contain?
  - id: MarketingModuleDynamicContent_CreateDynamicContent
    intent: Create a dynamic content item
    question: How do I add a new banner or content block for the storefront?
  phrasing_ops: 35
  slug: virto-commerce-marketing-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Document based flexible order management system.
  name: Virto Commerce Order Management API
  phrasing_intents:
  - id: OrderModule_SearchCustomerOrder
    intent: Search customer orders
    question: How do I find all orders placed by one customer?
  - id: OrderModule_GetByNumber
    intent: Get an order by its order number
    question: Can I look up an order using the order number the customer gave me?
  - id: OrderModule_GetById
    intent: Get an order by ID
    question: How do I load a customer order with all its shipments and payments by internal ID?
  - id: OrderModule_PatcOrder
    intent: Partially update an order
    question: Can I change a single field on an order without resending the whole document?
  - id: OrderModule_GetByOuterId
    intent: Get an order by external ID
    question: Can I find an order using the ID from my ERP or external system?
  - id: OrderModule_CalculateTotals
    intent: Recalculate order totals
    question: How do I get updated totals after editing items on an order?
  - id: OrderModule_ProcessOrderPayments
    intent: Process an order payment with the gateway
    question: How do I push an order's payment through the external payment system?
  - id: OrderModule_CreateOrderFromCart
    intent: Turn a shopping cart into an order
    question: How do I convert a customer's cart into a placed order?
  phrasing_ops: 35
  slug: virto-commerce-order-management-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Robust pricing management functionality based on price list and dynamic evaluation
  name: Virto Commerce Pricing API
  phrasing_intents:
  - id: PricingModule_EvaluatePrices
    intent: Evaluate product prices for a shopping context
    question: What price would a specific customer pay for these products in my store?
  - id: PricingModule_EvaluatePriceLists
    intent: Evaluate which price lists apply to a context
    question: Which price lists apply to a given store, customer and currency right now?
  - id: PricingModule_GetPricelistAssignmentById
    intent: Get a price list assignment
    question: Which catalog or store is a given price list assignment tied to?
  - id: PricingModule_PatchPriceListAssignment
    intent: Partially update a price list assignment
    question: Can I change only the priority of a price list assignment?
  - id: PricingModule_GetPricelistAssignmentByOuterId
    intent: Get a price list assignment by external id
    question: How can I find a price list assignment using my ERP's key?
  - id: PricingModule_GetNewPricelistAssignments
    intent: Get a blank price list assignment template
    question: What does an empty price list assignment object look like before I save it?
  - id: PricingModule_SearchPricelists
    intent: Search price lists
    question: Which price lists do I have across all catalogs?
  - id: PricingModule_CreatePriceList
    intent: Create a price list
    question: How do I set up a new price list for a currency?
  phrasing_ops: 32
  slug: virto-commerce-pricing-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: 'Quoter enables business users to execute quote requests online. Once initiated, an online conversation takes place with internal users who interact with the business user''s request. The internal user '
  name: Virto Commerce Quotes API
  phrasing_intents:
  - id: QuoteModule_Search
    intent: Search quote requests
    question: Which quote requests has a given B2B customer submitted?
  - id: QuoteModule_GetById
    intent: Get a quote request
    question: What items and prices are on one quote request?
  - id: QuoteModule_Create
    intent: Create a quote request
    question: How does a B2B buyer submit a new request for quote?
  - id: QuoteModule_Update
    intent: Update a quote request
    question: How do I change the expiration date on an existing quote?
  - id: QuoteModule_Delete
    intent: Delete quote requests
    question: How do I delete quote requests that are no longer needed?
  - id: QuoteModule_CalculateTotals
    intent: Recalculate quote totals
    question: What would a quote's totals be after I change its prices or items?
  - id: QuoteModule_GetShipmentMethods
    intent: List shipping methods for a quote
    question: Which shipping methods can be offered on a quote?
  - id: QuoteModule_CreateOrderFromQuote
    intent: Convert a quote into an order
    question: How do I turn an accepted quote into a customer order?
  phrasing_ops: 10
  slug: virto-commerce-quotes-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Shopping cart / checkout functionality
  name: Virto Commerce Shopping Cart API
  phrasing_intents:
  - id: CartModule_GetCart
    intent: Get a shopper's current cart
    question: How do I load the active cart for a customer in a given store, currency and language?
  - id: CartModule_GetCartItemsCount
    intent: Count the items in a cart
    question: How many items are in a shopping cart right now?
  - id: CartModule_AddItemToCart
    intent: Add a product to a cart
    question: How do I add a product to a customer's shopping cart?
  - id: CartModule_ChangeCartItem
    intent: Change a cart line item's quantity
    question: How do I change the quantity of a product already in the cart?
  - id: CartModule_ClearCart
    intent: Empty a cart
    question: How do I remove every item from a cart at once?
  - id: CartModule_RemoveCartItem
    intent: Remove one item from a cart
    question: How do I take a single product out of a cart?
  - id: CartModule_MergeWithCart
    intent: Merge another cart into a cart
    question: How do I combine an anonymous shopper's cart with their account cart after login?
  - id: CartModule_GetCartById
    intent: Get a cart by ID
    question: What does a shopping cart contain when I fetch it by ID?
  phrasing_ops: 24
  slug: virto-commerce-shopping-cart-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Multi store management with individual store settings
  name: Virto Commerce Store API
  phrasing_intents:
  - id: StoreAuthenticationScheme_Get
    intent: Get a store's authentication schemes
    question: Which sign-in schemes are enabled for a particular store?
  - id: StoreAuthenticationScheme_Update
    intent: Update a store's authentication schemes
    question: How do I turn a login scheme on or off for one store?
  - id: StoreModule_SearchStores
    intent: Search stores
    question: Which stores do I have in Virto Commerce and what state are they in?
  - id: StoreModule_GetStoreById
    intent: Get a store by id
    question: What currencies, languages and catalog is a given store set up with?
  - id: StoreModule_PatchStore
    intent: Partially update a store
    question: Can I change just one field on a store without sending the whole record?
  - id: StoreModule_GetStoreByOuterId
    intent: Get a store by its external id
    question: How can I find a store using the integration key from my ERP?
  - id: StoreModule_CreateStore
    intent: Create a store
    question: How do I set up a new storefront with its own catalog and currency?
  - id: StoreModule_UpdateStore
    intent: Update a store
    question: How do I change a store's default currency or time zone?
  phrasing_ops: 13
  slug: virto-commerce-store-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: B2B Innovation Platform
  name: Virto Commerce VirtoCommerce Platform API
  phrasing_intents:
  - id: ExternalSignIn_SignIn
    intent: Start sign-in through an external identity provider
    question: How do I send a user to sign in with an external login provider?
  - id: ExternalSignIn_SignOut
    intent: Sign out of an external identity provider
    question: Can I log a user out of their external identity provider session too?
  - id: ExternalSignIn_SignInCallback
    intent: Complete an external sign-in callback
    question: Which endpoint does the external identity provider call back after login?
  - id: ExternalSignIn_GetExternalLoginProviders
    intent: List external login providers
    question: Which external login providers are configured on the platform?
  - id: AppManifest_GetManifest
    intent: Get an app's plugin manifest
    question: What plugins does a host app's manifest declare?
  - id: AppManifest_InvalidateManifestCache
    intent: Invalidate the app manifest cache
    question: How do I make app manifests pick up newly installed plugins?
  - id: Apps_GetApps
    intent: List available apps
    question: Which apps can the signed-in user open on the platform?
  - id: Authorization_RevokeCurrentUserToken
    intent: Revoke the current user's token
    question: How do I invalidate the access token I'm currently using?
  phrasing_ops: 124
  slug: virto-commerce-virtocommerce-platform-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: Register HTTP webhooks against the platform domain-event catalog, compose the payload from selected entity properties (including previous values), fire test deliveries, and audit every delivery attemp
  name: Virto Commerce Webhooks API
  phrasing_intents:
  - id: WebHooks_GetWebhookById
    intent: Get a webhook by its ID
    question: What URL and events is a specific webhook configured with?
  - id: WebHooks_Search
    intent: Search webhooks
    question: Which webhooks are currently active in my Virto Commerce platform?
  - id: WebHooks_SearchWebhookFeed
    intent: Search webhook delivery logs
    question: Why did a webhook delivery fail, and where are the logs?
  - id: WebHooks_DeleteWebHookFeeds
    intent: Delete webhook log entries
    question: How do I clear old webhook delivery log entries?
  - id: WebHooks_SaveWebhooks
    intent: Create or update webhooks
    question: How do I register a new webhook for platform events?
  - id: WebHooks_DeleteWebHooks
    intent: Delete webhooks
    question: How do I remove a webhook subscription entirely?
  - id: WebHooks_Run
    intent: Send a test request to a webhook
    question: Can I fire a webhook manually to test my receiving endpoint?
  - id: WebHooks_GetAllRegisteredEvents
    intent: List events that can trigger webhooks
    question: What events can I subscribe a webhook to?
  phrasing_ops: 9
  slug: virto-commerce-webhooks-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: 'Return management: search returns, read a return by id, create or update a return against an order, and read the quantities still available to return.'
  name: Virto Commerce Returns API
  phrasing_intents:
  - id: Return_SearchReturns
    intent: Search product returns
    question: Which returns have been opened against a particular order?
  - id: Return_GetReturnById
    intent: Get a return by its ID
    question: What status and resolution does a specific return have?
  - id: Return_UpdateReturn
    intent: Save or update a product return
    question: How do I change the status of an existing return?
  - id: Return_DeleteReturn
    intent: Delete product returns
    question: How do I remove return records I no longer need?
  - id: Return_GetAvailableQuantities
    intent: Check quantities still returnable on an order
    question: How many units of each item on an order can still be returned?
  phrasing_ops: 5
  slug: virto-commerce-returns-api
- baseURL: https://virtostart-demo-admin.govirto.com/api
  baseurl_source: declared
  description: The module enables you to be notified of new messages or changes via a Message Queue of your choice
  name: Virto Commerce Event Bus module API
  phrasing_intents:
  - id: Connections_SearchConnections
    intent: Search event bus provider connections
    question: Which event bus connections are set up in my Virto Commerce platform?
  - id: Connections_GetConnectionByName
    intent: Get an event bus connection by name
    question: What options is a specific event bus connection configured with?
  - id: Connections_DeleteConnection
    intent: Delete an event bus connection
    question: Can I remove an event bus connection that was registered in the database?
  - id: Connections_CreateConnection
    intent: Create an event bus provider connection
    question: How can I connect the event bus to a new message provider?
  - id: Connections_UpdateConnection
    intent: Update an event bus connection
    question: How do I change the provider options on an existing event bus connection?
  - id: ConnectionsLog_SearchProviderConnectionLog
    intent: Search provider connection failure logs
    question: Why are events failing to reach my event bus provider?
  - id: Subscriptions_Get
    intent: List available domain events
    question: What domain events can the event bus subscribe to?
  - id: Subscriptions_SearchSubscriptions
    intent: Search event bus subscriptions
    question: Which event subscriptions are sending events through a given connection?
  phrasing_ops: 12
  slug: virto-commerce-event-bus-module-api
artifact_total: 35
asyncapis:
- description: ''
  name: Virto Commerce Webhooks
  slug: virto-commerce-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VirtoCommerce.Cart Catalog API
  slug: open-virto-commerce-catalog-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Companies and Contacts API
  slug: open-virto-commerce-companies-and-contacts-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Inventory API
  slug: open-virto-commerce-inventory-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Marketing API
  slug: open-virto-commerce-marketing-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Order Management API
  slug: open-virto-commerce-order-management-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Pricing API
  slug: open-virto-commerce-pricing-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Quotes API
  slug: open-virto-commerce-quotes-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Shopping Cart API
  slug: open-virto-commerce-shopping-cart-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog Store API
  slug: open-virto-commerce-store-api
- collection_type: open
  name: VirtoCommerce.Cart Catalog VirtoCommerce Platform API
  slug: open-virto-commerce-virtocommerce-platform-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/capabilities/virto-commerce-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/virto-commerce-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/VirtoCommerce/vc-module-catalog/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/VirtoCommerce/vc-module-catalog/releases
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/overlays/virto-commerce-event-bus-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/virto-commerce-event-bus-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/agentic-access/virto-commerce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/virto-commerce-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/security/virto-commerce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virto-commerce-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/authentication/virto-commerce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/virto-commerce-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/scopes/virto-commerce-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/virto-commerce-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://virtocommerce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.virtocommerce.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VirtoCommerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virto-commerce/
- group: company
  title: ''
  type: Blog
  url: https://virtocommerce.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://virtocommerce.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/VirtoCommerce
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/plans/virto-commerce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/virto-commerce-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/rate-limits/virto-commerce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/virto-commerce-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/finops/virto-commerce-finops.yml
  title: ''
  type: FinOps
  url: finops/virto-commerce-finops.yml
- group: docs
  title: ''
  type: SwaggerUI
  url: https://virtostart-demo-admin.govirto.com/docs/index.html
- group: operate
  title: ''
  type: Support
  url: https://help.virtocommerce.com/support/home
- group: operate
  title: ''
  type: Community
  url: https://www.virtocommerce.org/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.virtocommerce.org/c/news-digest/14
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/packages/virto-commerce-packages.yml
  title: ''
  type: Packages
  url: packages/virto-commerce-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/packages/virto-commerce-packages.yml
  title: ''
  type: SDKs
  url: packages/virto-commerce-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/well-known/virto-commerce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/virto-commerce-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/mcp/virto-commerce-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/virto-commerce-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/mcp/virto-commerce-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/virto-commerce-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/llms/virto-commerce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/virto-commerce-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/conformance/virto-commerce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/virto-commerce-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/conformance/virto-commerce-conformance.yml
  title: ''
  type: Compliance
  url: conformance/virto-commerce-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/errors/virto-commerce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/virto-commerce-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/lifecycle/virto-commerce-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/virto-commerce-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/conventions/virto-commerce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/virto-commerce-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/changelog/virto-commerce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/virto-commerce-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/cli/virto-commerce-cli.yml
  title: ''
  type: CLI
  url: cli/virto-commerce-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/components/virto-commerce-components.yml
  title: ''
  type: Components
  url: components/virto-commerce-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/data-model/virto-commerce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/virto-commerce-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/sandbox/virto-commerce-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/virto-commerce-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/asyncapi/virto-commerce-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/virto-commerce-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/graphql/virto-commerce-schema.graphql
  title: ''
  type: GraphQL
  url: graphql/virto-commerce-schema.graphql
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.virtocommerce.org/platform/developer-guide/
- group: docs
  title: ''
  type: APIReference
  url: https://virtostart-demo-admin.govirto.com/docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/VirtoCommerce/start-local
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtocommerce.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtocommerce.com/privacy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Virtocommerce/videos
created: '2026-06-13'
description: Virto Commerce is an open-source, API-first B2B e-commerce platform built on .NET Core. It provides REST and GraphQL APIs for catalog management, pricing, inventory, order management, customer organizations, marketing, payments, shipping, subscriptions, and complex B2B purchasing workflows including quotes, contracts, and approval routing. The modular architecture offers 100+ independently deployable modules covering the full commerce stack for enterprise deployments.
finops:
- name: Virto Commerce Finops
  service_category: ''
  slug: virto-commerce-finops
graphqls:
- description: Virto Commerce exposes a unified GraphQL API (the "Experience API" or xAPI) as the primary interface for headless storefronts. Built on top of the GraphQL.NET library, the xAPI aggregates catalog, car
  name: Virto Commerce GraphQL API
  slug: virto-commerce-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/virto-commerce.png
jsonld:
- class_count: 15
  name: Virto Commerce Context
  property_count: 0
  slug: virto-commerce-context
layout: provider
mcp_servers:
- description: Virto Commerce ships a real, published MCP surface, and it is a LOCAL STDIO one. The supported path is the Commerce Operations Foundation (COF) MCP server run over stdio with Virto's own adapter (@vir
  name: Virto Commerce MCP
  slug: virto-commerce-mcp
modified: '2026-08-13'
name: Virto Commerce
nav: Providers
network: true
overview: 'Virto Commerce publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Companies and Contacts API, Inventory API, and 10 more. Tagged areas include B2B eCommerce, Catalog Management, Order Management, Pricing, and Inventory.


  The Virto Commerce catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Virto Commerce''s developer surface includes authentication, documentation, engineering blog, pricing, support, changelog, CLI, and 40 more developer resources.'
plans:
- name: Virto Commerce Plans Pricing
  plan_count: 3
  slug: virto-commerce-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Virto Commerce Rate Limits
  slug: virto-commerce-rate-limits
scopes:
- name: Virto Commerce Scopes
  scope_count: 84
  slug: virto-commerce-scopes
  summary_line: 84 scopes · password/clientCredentials
score:
  band: exemplar
  composite: 71.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 75.0
    catalog_earned_first_party: 24.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 50.8
    developer_ergonomics: 80.4
    discoverability: 76.7
    operational_transparency: 57.9
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 8.3
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 72.2
screenshot: https://raw.githubusercontent.com/api-evangelist/virto-commerce/refs/heads/main/screenshots/virto-commerce-2026-06-20T201036.png
security:
- kind: authentication
  name: Virto Commerce Authentication
  slug: virto-commerce-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Virto Commerce Domain Security
  slug: virto-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virto-commerce
tags:
- B2B eCommerce
- Catalog Management
- Order Management
- Pricing
- Inventory
- Shopping Cart
- Customer Management
- Marketing
- Payments
- Shipping
- Subscription
- Headless Commerce
- Open Source
- .NET
- Webhook
- Event-Driven
- CloudEvents
- GraphQL
- Returns
- MCP
- B2B Quotes
website: https://virtocommerce.com/
---
