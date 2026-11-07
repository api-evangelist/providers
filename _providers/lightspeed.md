---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 171
  human_in_the_loop: 0
  name: Lightspeed Agentic Access
  operation_count: 383
  slug: lightspeed-agentic-access
  summary_line: 383 operations · 171 acting
api_count: 3
apis:
- description: REST API for Lightspeed Retail R-Series (formerly Vend) providing access to sales, inventory, customers, products, and reporting data for retail point-of-sale systems.
  name: Lightspeed Retail R-Series API
  slug: retail-r-series
- description: REST API for Lightspeed eCom (C-Series) e-commerce platform providing endpoints for products, orders, customers, shipments, payments, and inventory management. Requires Advanced or Professional subscr
  name: Lightspeed eCom API
  slug: ecom-c-series
- description: REST API for Lightspeed eCom E-Series, the Ecwid storefront platform Lightspeed acquired in 2021 and now sells as eCom E-Series. Provides store profile, product catalog, categories, orders, customers,
  name: Lightspeed eCom E-Series (Ecwid) API
  slug: ecom-e-series
- description: REST API for Lightspeed Restaurant O-Series, the Kounta hospitality point-of-sale platform Lightspeed acquired in 2019 and sells as O-Series. Exposes sites, registers, products, categories, orders, cu
  name: Lightspeed Restaurant O-Series (Kounta) API
  slug: restaurant-o-series
- description: Partner REST API for Lightspeed Golf, the Chronogolf tee-sheet and golf course management platform Lightspeed acquired in 2019. Covers organizations, courses, tee times, green fees, reservations and c
  name: Lightspeed Golf (Chronogolf) Partner API
  slug: golf-g-series
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Audit and security operations
  name: Lightspeed Commerce Audit API
  phrasing_intents:
  - id: GetAuditLogEvents
    intent: List audit log events
    question: Who changed customers, registers or outlets in my store and when?
  - id: get-security_events
    intent: List my security events
    question: What sign-ins and security events are recorded for my own account?
  phrasing_ops: 2
  slug: lightspeed-audit-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Brand operations
  name: Lightspeed Commerce Brands API
  phrasing_intents:
  - id: ListBrands
    intent: List brands
    question: What product brands are set up in my store?
  - id: CreateBrand
    intent: Create a brand
    question: How do I add a new brand to assign products to?
  - id: DeleteBrandByID
    intent: Delete a brand
    question: What happens to products when their brand is deleted?
  - id: GetBrandByID
    intent: Get a brand
    question: What are the details of one brand?
  - id: UpdateBrandById
    intent: Update a brand
    question: Can I rename an existing brand?
  phrasing_ops: 5
  slug: lightspeed-brands-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: A log of requests and responses between Lightspeed and an integration channel.
  name: Lightspeed Commerce Channel Request Log API
  phrasing_intents:
  - id: listRequests
    intent: List channel request log records
    question: Which requests to my sales channel failed with an error status?
  - id: getSingleRequest
    intent: Get a single channel request log
    question: How do I inspect one channel request log entry in detail?
  - id: getSingleRequestText
    intent: Get a channel request log as plain text
    question: Can I download a request log entry as plain text?
  - id: listChannels
    intent: List configured sales channels
    question: Which sales channels are configured on my store?
  phrasing_ops: 4
  slug: lightspeed-channel-request-log-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Consignment Product operations
  name: Lightspeed Commerce Consignment Products API
  phrasing_intents:
  - id: CreateOrUpdateConsignmentProducts
    intent: Bulk add or update consignment products
    question: How do I add or update many products on a stock order at once?
  - id: ListProductsByConsignmentID
    intent: List products on a consignment
    question: Which products are on a particular stock order or transfer?
  - id: CreateConsignmentProduct
    intent: Add a product to a consignment
    question: How do I add a single product to a supplier order?
  - id: DeleteProductFromConsignment
    intent: Remove a product from a consignment
    question: How do I take a product off a stock order?
  - id: UpdateProductInConsignment
    intent: Update a product's quantity on a consignment
    question: How do I change the ordered count for one product on a stock order?
  phrasing_ops: 5
  slug: lightspeed-consignment-products-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Stock control operations
  name: Lightspeed Commerce Consignments API
  phrasing_intents:
  - id: GetConsignments
    intent: List consignments
    question: What stock orders, transfers and stocktakes are in progress?
  - id: CreateConsignment
    intent: Create a stock order, transfer or stocktake
    question: How do I raise a supplier stock order or an outlet transfer?
  - id: DeleteConsignmentByID
    intent: Delete a consignment
    question: Can I delete a stock order that was created by mistake?
  - id: GetConsignmentByID
    intent: Get a consignment
    question: What is the status of a specific stock order?
  - id: UpdateConsignmentByID
    intent: Update a consignment or advance its status
    question: How do I mark a supplier order as sent or received?
  - id: ListConsignmentTotals
    intent: Get a consignment's item count and cost
    question: How many items and what total cost are on a stock order?
  phrasing_ops: 6
  slug: lightspeed-consignments-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Customer Address operations
  name: Lightspeed Commerce Customer Addresses API
  phrasing_intents:
  - id: ListCustomerAddresses
    intent: List a customer's addresses
    question: What shipping and billing addresses does a customer have on file?
  - id: CreateCustomerAddress
    intent: Add an address to a customer
    question: How do I save a new delivery address for a customer?
  - id: DeleteCustomerAddress
    intent: Delete a customer address
    question: Can I remove an old address from a customer's profile?
  - id: GetCustomerAddress
    intent: Get one customer address
    question: Can I fetch a single address for a customer?
  - id: UpdateCustomerAddress
    intent: Update a customer address
    question: How do I correct a customer's saved address?
  phrasing_ops: 5
  slug: lightspeed-customer-addresses-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Customer Group operations
  name: Lightspeed Commerce Customer Groups API
  phrasing_intents:
  - id: ListCustomerGroups
    intent: List customer groups
    question: What customer groups like VIP or wholesale do we have?
  - id: CreateCustomerGroup
    intent: Create a customer group
    question: How do I create a new customer group for wholesale buyers?
  - id: GetCustomerGroupById
    intent: Get a customer group
    question: How do I look up one customer group by its ID?
  - id: UpdateCustomerGroup
    intent: Rename a customer group
    question: How do I rename an existing customer group?
  - id: DeleteCustomersFromCustomerGroup
    intent: Remove customers from a customer group
    question: How do I take customers out of a group without deleting them?
  - id: GetCustomerGroupCustomers
    intent: List customers in a customer group
    question: Which customers belong to a particular customer group?
  - id: AddCustomersToCustomerGroup
    intent: Add customers to a customer group
    question: How do I add several customers to a group at once?
  phrasing_ops: 7
  slug: lightspeed-customer-groups-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Customer operations
  name: Lightspeed Commerce Customers API
  phrasing_intents:
  - id: ListCustomers
    intent: List customers
    question: How do I list all the customers in my store?
  - id: CreateCustomer
    intent: Create a new customer
    question: How do I add a new customer record with their email and phone?
  - id: DeleteCustomerByID
    intent: Delete a customer
    question: How do I delete a customer record?
  - id: GetCustomerByID
    intent: Get a single customer
    question: How do I look up a customer's full record by ID?
  - id: UpdateCustomerByID
    intent: Update a customer's details
    question: How do I change an existing customer's email or phone number?
  phrasing_ops: 5
  slug: lightspeed-customers-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: 'V1 endpoints (`/f/finance/...`) for retrieving sales and financial data. For the newer V2 versions of these endpoints see FinancialV2 ### V1 behaviour - **Sorting**: No guaranteed sorting order; inter'
  name: Lightspeed Commerce Financial API
  phrasing_intents:
  - id: financial-apiGetBusinesses
    intent: List businesses and their locations
    question: Which businesses and restaurant locations can my API token see?
  - id: financial-apiGetTaxRates
    intent: Get tax rates for a location
    question: What tax rates are configured for my restaurant?
  - id: financial-apiGetPaymentMethods
    intent: List payment methods for a location
    question: Which payment methods, like card or cash, are set up at a venue?
  - id: financial-apiGetAccountingGroups
    intent: List accounting groups for a location
    question: What accounting groups are items assigned to at my restaurant?
  - id: financial-apiGetFinancials
    intent: Get financial data for a date range
    question: How do I export every receipt and payment for a location over a period?
  - id: financial-apiGetDailyFinancials
    intent: Get financial data for one business day
    question: What did my restaurant take today so far?
  - id: financial-apiGetReceiptByExternalReference
    intent: Find a receipt by external reference
    question: Can I look up a receipt using the reference my ordering system attached to it?
  - id: financial-apiGetAggregatedSales
    intent: Get sales totals grouped by a dimension
    question: How much did each staff member or device sell today?
  phrasing_ops: 8
  slug: lightspeed-financial-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: 'V2 endpoints (`/f/v2/...`) for retrieving sales and financial data. ### Endpoint Mapping | V1 Endpoint | V2 Endpoint | |-------------|-------------| | `getFinancials` (`/f/finance/{id}/financials/{fro'
  name: Lightspeed Commerce Financial V2 API
  phrasing_intents:
  - id: financial-apiGetBusinessLocationSales
    intent: Get sales for a location over a date range
    question: How do I pull all closed sales for a restaurant over a date range?
  - id: financial-apiGetBusinessLocationSalesOfABusinessDay
    intent: Get sales for a single business day
    question: What were a location's sales for one business day?
  - id: financial-apiGetLightspeedPayments
    intent: Get Lightspeed Payments fees and surcharges
    question: How much did I pay in Lightspeed Payments fees over a period?
  - id: financial-apiGetBusinessLocationAbortedOrdersOfABusinessDay
    intent: List aborted orders for a business day
    question: Which orders had all items removed before being committed on a given day?
  phrasing_ops: 4
  slug: lightspeed-financialv2-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Fulfillment operations
  name: Lightspeed Commerce Fulfillments API
  phrasing_intents:
  - id: getFulfillmentSummary
    intent: List fulfillments
    question: Which orders are waiting to be picked, packed or shipped?
  - id: postFulfillSale
    intent: Fulfill an entire sale
    question: How do I mark every item in an order as fulfilled at once?
  - id: postFulfillLineItems
    intent: Fulfill specific line items
    question: Can I fulfill only some line items of an order?
  - id: getFulfillmentHistory
    intent: Get a fulfillment's history
    question: When was each item in an order picked, packed or returned?
  - id: postPackLineItems
    intent: Set packed quantities for line items
    question: How do I record that some items have been packed?
  - id: postPickLineItems
    intent: Set picked quantities for line items
    question: How do I record items picked from the shelf for an order?
  phrasing_ops: 6
  slug: lightspeed-fulfillments-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Gift Card operations
  name: Lightspeed Commerce Gift Cards API
  phrasing_intents:
  - id: ListGiftCards
    intent: List gift cards
    question: Which gift cards have been issued by my store?
  - id: CreateGiftCard
    intent: Issue and activate a new gift card
    question: How do I sell a new gift card with a starting balance?
  - id: VoidGiftCardById
    intent: Void a gift card by its internal ID
    question: Can I cancel a gift card using its internal ID so its balance goes to zero?
  - id: FindGiftCardById
    intent: Look up a gift card by its internal ID
    question: Can I fetch a gift card and its transaction history using its internal ID rather than the card number?
  - id: VoidGiftCardByNumber
    intent: Void a gift card by card number
    question: How do I void a lost gift card using the number printed on it?
  - id: FindGiftCardByNumber
    intent: Look up a gift card by card number
    question: What's the remaining balance on the gift card a customer just handed me?
  - id: ReverseGiftCardTransaction
    intent: Reverse a gift card redemption
    question: Can I undo a gift card redemption that was charged by mistake?
  - id: FindGiftCardByTransactionId
    intent: Find the gift card behind a transaction
    question: Which gift card was used in a given gift card transaction?
  phrasing_ops: 11
  slug: lightspeed-gift-cards-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The ID Cards API from Lightspeed Commerce — 2 operation(s) for id cards.
  name: Lightspeed Commerce ID Cards API
  phrasing_intents:
  - id: id-cards-apiCreateIdCardBatch
    intent: Create a batch of ID cards
    question: How do I start a new batch of ID cards for a location?
  - id: id-cards-apiCreateIdCards
    intent: Generate ID cards in an existing batch
    question: How do I generate a number of ID cards inside a batch?
  phrasing_ops: 2
  slug: lightspeed-id-cards-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Inventory operations
  name: Lightspeed Commerce Inventory API
  phrasing_intents:
  - id: ListCustomInventoryAdjustmentReasons
    intent: List custom inventory adjustment reasons
    question: What custom reasons have we set up for adjusting stock?
  - id: CreateCustomInventoryAdjustmentReason
    intent: Create a custom inventory adjustment reason
    question: How do I add a new reason like 'water damage' for stock adjustments?
  - id: UpdateCustomInventoryAdjustmentReason
    intent: Rename or toggle an adjustment reason
    question: How do I disable a custom stock adjustment reason we no longer use?
  - id: ListInventoryRecords
    intent: List inventory records across products
    question: How do I pull inventory records for all products and outlets?
  - id: SetReorderPoints
    intent: Set reorder points for products at outlets
    question: How do I set the reorder point for products at specific outlets?
  - id: ListProductInventoryRecords
    intent: Get inventory records for one product
    question: How much of a specific product do we have at each outlet?
  - id: ListInventoryLevels
    intent: List inventory levels with filters
    question: Which products need to be procured based on current inventory levels?
  - id: ListProductInventoryLevels
    intent: Get inventory levels for one product
    question: What are the current stock levels for a single product?
  phrasing_ops: 10
  slug: lightspeed-inventory-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Items API from Lightspeed Commerce — 2 operation(s) for items.
  name: Lightspeed Commerce Items API
  phrasing_intents:
  - id: items-apiGetItemById
    intent: Get a menu item
    question: What price and SKU does a particular menu item have?
  - id: items-apiPut
    intent: Update a menu item
    question: Can I change the price of an existing item on the menu?
  - id: items-apiGetItems
    intent: List or search menu items
    question: What items are on the menu at a restaurant location?
  - id: items-apiCreateItem
    intent: Create a menu item
    question: How do I add a new dish or drink to a location's menu?
  phrasing_ops: 4
  slug: lightspeed-items-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Loyalty Adjustments [BETA] API from Lightspeed Commerce — 1 operation(s) for loyalty adjustments [beta].
  name: Lightspeed Commerce Loyalty Adjustments [BETA] API
  phrasing_intents:
  - id: postLoyaltyAdjustmentsBulk
    intent: Adjust loyalty balances for many customers at once
    question: Can I change the loyalty balance of a whole batch of customers in one request?
  phrasing_ops: 1
  slug: lightspeed-loyalty-adjustments-beta-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Order and Pay API from Lightspeed Commerce — 19 operation(s) for order and pay.
  name: Lightspeed Commerce Order and Pay API
  phrasing_intents:
  - id: apeLookupBusinesses
    intent: List businesses and locations for my token
    question: Which businesses and business locations can my access token reach?
  - id: apeLookupFloorPlans
    intent: List a location's floorplans
    question: What floorplans are set up for my restaurant location?
  - id: apeGetTables
    intent: List the tables on one floorplan
    question: Which tables are on a particular floorplan in my venue?
  - id: apeAccountProfiles
    intent: List active order profiles for a location
    question: What order profiles are active at my business location?
  - id: apeGetAccountProfile
    intent: Get one order profile by its code
    question: How do I look up the details of a single order profile by its code?
  - id: apeLoadMenus
    intent: List the menus at a business location
    question: Which menus exist for my business location?
  - id: apeGetMenuById
    intent: Load a single menu (deprecated V1)
    question: How do I load a menu with the older deprecated V1 menu endpoint?
  - id: apeGetMenuByIdV2
    intent: Load a single menu with modifiers (V2)
    question: How do I load a full menu including product modifier groups and modifiers?
  phrasing_ops: 20
  slug: lightspeed-order-and-pay-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: 'The Order and Pay: Webhook API from Lightspeed Commerce — 4 operation(s) for order and pay: webhook.'
  name: 'Lightspeed Commerce Order and Pay: Webhook API'
  phrasing_intents:
  - id: apeCreateWebhookOo
    intent: Create an order status webhook
    question: How do I set up a webhook to get order status updates?
  - id: apeUpdateWebhookOo
    intent: Update an existing webhook
    question: How do I change the URL of a webhook I already configured?
  - id: apeGetWebhookOo
    intent: Retrieve a webhook
    question: How do I see how a webhook endpoint is configured?
  - id: apeDeleteWebhookEndpoint
    intent: Delete a webhook
    question: How do I stop receiving order webhooks entirely?
  - id: apeGetWebhookBusinessLocations
    intent: List locations enabled on a webhook
    question: Which business locations are attached to my webhook?
  - id: apeAddWebhookBusinessLocation
    intent: Enable a webhook for a business location
    question: How do I get item availability notifications for a location?
  - id: apeRemoveWebhookBusinessLocation
    intent: Remove a business location from a webhook
    question: How do I stop one location from sending events to my webhook?
  phrasing_ops: 7
  slug: lightspeed-order-and-pay-webhook-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Outlet Product Tax operations
  name: Lightspeed Commerce Outlet Product Taxes API
  phrasing_intents:
  - id: listOutletProductTaxes
    intent: List product tax assignments per outlet
    question: Which tax applies to each product at a given outlet?
  phrasing_ops: 1
  slug: lightspeed-outlet-product-taxes-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Outlet operations
  name: Lightspeed Commerce Outlets API
  phrasing_intents:
  - id: ListOutlets
    intent: List outlets
    question: Which store locations do I have?
  - id: GetOutletByID
    intent: Get an outlet
    question: What address and settings does one store location have?
  phrasing_ops: 2
  slug: lightspeed-outlets-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Packing slip rendering operations
  name: Lightspeed Commerce Packing Slips API
  phrasing_intents:
  - id: getPackingSlip
    intent: Render a full packing slip for a fulfillment
    question: How do I print a packing slip for an order fulfillment?
  - id: getPartialPackingSlip
    intent: Render a partial packing slip for packed items
    question: Can I print a packing slip for only the items packed so far?
  phrasing_ops: 2
  slug: lightspeed-packing-slips-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Partner Billing operations
  name: Lightspeed Commerce Partner Billing API
  phrasing_intents:
  - id: PartnerSubscriptions
    intent: List a retailer's partner subscriptions
    question: Which of my app subscriptions does this retailer currently have?
  - id: PartnerSubscription
    intent: Get a partner subscription
    question: What plan and status does a specific partner subscription have?
  - id: PartnerToken
    intent: Start a new partner subscription checkout
    question: How do I send a retailer to subscribe to my app's paid plan?
  - id: PartnerTokenGet
    intent: Look up a subscription token
    question: What subscription does a partner subscription token point to?
  - id: PartnerUpdateSubscriptionToken
    intent: Start a subscription change checkout
    question: How do I let a retailer upgrade or change their existing app subscription?
  phrasing_ops: 5
  slug: lightspeed-partner-billing-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Payment Type operations
  name: Lightspeed Commerce Payment Types API
  phrasing_intents:
  - id: ListPaymentTypes
    intent: List payment types
    question: What payment types like cash or card are set up in my store?
  phrasing_ops: 1
  slug: lightspeed-payment-types-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The PMS API from Lightspeed Commerce — 3 operation(s) for pms.
  name: Lightspeed Commerce PMS API
  phrasing_intents:
  - id: pms-apiGetRevenueCenters
    intent: List POS configurations for PMS revenue centers
    question: Which POS configurations can I map to hotel PMS revenue centers?
  - id: pms-apiGetProvider
    intent: Get a PMS provider
    question: How do I see the settings of a PMS provider I created?
  - id: pms-apiUpdateProvider
    intent: Update a PMS provider
    question: How do I change the endpoint or API key for my PMS provider?
  - id: pms-apiDeleteProvider
    intent: Delete a PMS provider
    question: How do I permanently remove a PMS integration from a location?
  - id: pms-apiGetProviders
    intent: List PMS providers
    question: Which PMS providers have I configured for my locations?
  - id: pms-apiCreateProvider
    intent: Create a PMS provider
    question: How do I connect a property management system to a restaurant location?
  phrasing_ops: 6
  slug: lightspeed-pms-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The PMS Integration API from Lightspeed Commerce — 0 operation(s) for pms integration.
  name: Lightspeed Commerce PMS Integration API
  slug: lightspeed-pms-integration-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Price Book operations
  name: Lightspeed Commerce Price Books API
  phrasing_intents:
  - id: ListPriceBookProducts
    intent: List price book products across all books
    question: Which products have special prices across all my price books?
  - id: ListPriceBooksV3
    intent: List price books
    question: What price books do I have set up for customer groups and outlets?
  - id: CreatePriceBookV3
    intent: Create a price book
    question: How do I create special pricing for a customer group at certain outlets?
  - id: GetPriceBookByIDV3
    intent: Get a single price book
    question: Which outlets and customer groups does a specific price book cover?
  - id: UpdatePriceBookV3
    intent: Update a price book's settings
    question: Can I rename a price book or change which outlets it applies to?
  - id: DeletePriceBookProducts
    intent: Remove products from a price book
    question: Can I remove some products from a price book without deleting the book?
  - id: GetPriceBookProductsForPriceBook
    intent: List products in one price book
    question: What prices does a particular price book set for its products?
  - id: UpdatePriceBookProducts
    intent: Patch price book products
    question: Can I PATCH the prices of products already in a price book?
  phrasing_ops: 10
  slug: lightspeed-price-books-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Product Categories operations
  name: Lightspeed Commerce Product Categories API
  phrasing_intents:
  - id: ListProductCategories
    intent: List product categories
    question: How are my product categories arranged into a hierarchy?
  - id: DeleteProductCategories
    intent: Delete product categories
    question: What happens to products and child categories when I delete a category?
  - id: CreateUpdateProductCategories
    intent: Create or update a category hierarchy
    question: How do I build a nested category tree for my products in one go?
  phrasing_ops: 3
  slug: lightspeed-product-categories-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Product Image operations
  name: Lightspeed Commerce Product Images API
  phrasing_intents:
  - id: DeleteProductImageByID
    intent: Delete a product image
    question: Can I remove an image from a product?
  - id: GetProductImageDataByID
    intent: Check a product image
    question: Has a product image finished processing after I uploaded it?
  - id: SetImagePosition
    intent: Reorder a product image
    question: How do I make a different image the first one shown for a product?
  phrasing_ops: 3
  slug: lightspeed-product-images-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Product Type operations
  name: Lightspeed Commerce Product Types API
  phrasing_intents:
  - id: ListProductTypes
    intent: List product types (deprecated)
    question: What product types exist in my catalog under the older classification?
  - id: GetProductTypeByID
    intent: Get a product type
    question: What is the name of a particular legacy product type?
  phrasing_ops: 2
  slug: lightspeed-product-types-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Product operations
  name: Lightspeed Commerce Products API
  phrasing_intents:
  - id: ListProducts
    intent: List products in the catalog
    question: How do I list all products in my retail catalog?
  - id: CreateProduct
    intent: Create a new product
    question: How do I add a new product with a price and SKU?
  - id: DeleteProduct
    intent: Delete a product or single variant
    question: How do I delete one product or just one of its variants?
  - id: GetProductByID
    intent: Get a single product
    question: How do I fetch the full details of one product by ID?
  - id: UpdateProduct
    intent: Update an existing product
    question: How do I change the details of a product I already created?
  - id: UploadImage
    intent: Upload an image for a product
    question: How do I upload a product photo as a file?
  - id: DeleteProductFamily
    intent: Delete an entire product variant family
    question: How do I delete a product along with all of its variants?
  - id: GetPriceBooksForProduct
    intent: List price books a product belongs to
    question: Which price books include this product?
  phrasing_ops: 8
  slug: lightspeed-products-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Promo Code API from Lightspeed Commerce — 2 operation(s) for promo code.
  name: Lightspeed Commerce Promo Code API
  phrasing_intents:
  - id: DeletePromoCodesBulk
    intent: Delete promo codes in bulk
    question: How do I delete a batch of promo codes by their IDs?
  - id: GetActivePromoCodesBulk
    intent: Check whether promo codes are active
    question: Are these promo codes still active?
  phrasing_ops: 2
  slug: lightspeed-promo-code-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Promotion operations
  name: Lightspeed Commerce Promotions API
  phrasing_intents:
  - id: ApplyDiscount
    intent: Preview the best promotion for a sale
    question: Which promotion gives the best discount for this basket?
  - id: ListPromotions
    intent: List promotions by end date
    question: What promotions are set up for my retail store?
  - id: CreatePromotion
    intent: Create a promotion
    question: How do I set up a buy-one-get-one or percentage-off deal?
  - id: SearchPromotions
    intent: Search promotions by name, outlet or dates
    question: Which promotions have 'summer' in their name?
  - id: GetPromotionByID
    intent: Get a promotion
    question: What are the conditions and discount of one specific promotion?
  - id: UpdatePromotion
    intent: Update a promotion
    question: Can I change the end date of a running promotion?
  - id: GetPromotionProducts
    intent: List products a promotion applies to
    question: Which products are discounted by a promotion and at what price?
  - id: GetPromotionPromoCodes
    intent: List a promotion's promo codes
    question: What promo codes belong to a promotion?
  phrasing_ops: 8
  slug: lightspeed-promotions-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Purchase order operations
  name: Lightspeed Commerce Purchase Orders API
  phrasing_intents:
  - id: ListPurchaseOrders
    intent: List purchase orders
    question: What purchase orders do we have with our suppliers?
  - id: GetPurchaseOrderByID
    intent: Get a purchase order
    question: How do I look up one purchase order by its ID?
  - id: ListPurchaseOrderDeliveries
    intent: List deliveries on a purchase order
    question: Which deliveries have arrived against a purchase order?
  - id: ListPurchaseOrderDeliveryLineItems
    intent: List line items in a purchase order delivery
    question: What items came in on a particular delivery for a purchase order?
  - id: ListPurchaseOrderLineItems
    intent: List line items on a purchase order
    question: Which products and quantities were ordered on a purchase order?
  phrasing_ops: 5
  slug: lightspeed-purchase-orders-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Quotes operations
  name: Lightspeed Commerce Quotes API
  phrasing_intents:
  - id: get-quotes
    intent: List quotes
    question: What price quotes have we given customers?
  - id: get-quote-quote_id
    intent: Get a quote
    question: What items and prices are on a specific quote?
  phrasing_ops: 2
  slug: lightspeed-quotes-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Register operations
  name: Lightspeed Commerce Registers API
  phrasing_intents:
  - id: ListButtonLayouts
    intent: List register button layouts
    question: What quick key button layouts are set up for my registers?
  - id: GetButtonLayoutById
    intent: Get a register button layout
    question: How are the quick key buttons arranged in one layout?
  - id: ListRegisters
    intent: List registers
    question: Which registers are set up across my outlets?
  - id: GetRegisterByID
    intent: Get a register
    question: Is a particular register currently open or closed?
  - id: CloseRegister
    intent: Close a register
    question: How do I close a till at the end of the day?
  - id: OpenRegister
    intent: Open a register
    question: How do I open a till before trading starts?
  - id: RegisterPaymentsSummary
    intent: Get a register's payment totals
    question: How much cash and card has one register taken?
  phrasing_ops: 7
  slug: lightspeed-registers-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Reservations for Platforms API from Lightspeed Commerce — 11 operation(s) for reservations for platforms.
  name: Lightspeed Commerce Reservations for Platforms API
  phrasing_intents:
  - id: reservation-serviceOnboardingCallback
    intent: Complete restaurant onboarding for a platform
    question: After I receive the onboarding webhook, how do I finish connecting the restaurant?
  - id: reservation-serviceGetByPlatformCode
    intent: Get a reservation platform's profile
    question: What webhook URLs and settings are saved on my reservation platform profile?
  - id: reservation-serviceSetByPlatformCode
    intent: Create or update a reservation platform profile
    question: How do I register my booking platform with its display name and webhook URLs?
  - id: reservation-servicePlatformCourseSettings
    intent: Configure a platform's course settings
    question: Can my reservation platform be allowed to update course numbers?
  - id: reservation-servicePushPlatformReservation
    intent: Create or update a reservation
    question: How do I push a new booking into the restaurant's POS?
  - id: reservation-serviceActivateApiKeysAuth
    intent: Secure platform webhooks with an API key
    question: Can Lightspeed send an X-Api-Key header when calling my reservation webhooks?
  - id: reservation-serviceActivateBasicAuth
    intent: Secure platform webhooks with basic auth
    question: Can reservation webhooks be sent with a username and password?
  - id: reservation-serviceActivateBearerAuthAuth
    intent: Secure platform webhooks with a bearer token
    question: Can webhook calls to my platform carry a bearer token?
  phrasing_ops: 12
  slug: lightspeed-reservations-for-platforms-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Retailer operations
  name: Lightspeed Commerce Retailers API
  phrasing_intents:
  - id: GetRetailer
    intent: Get the retailer's account information
    question: What account settings and details does this retailer have?
  phrasing_ops: 1
  slug: lightspeed-retailers-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Rich Item API from Lightspeed Commerce — 6 operation(s) for rich item.
  name: Lightspeed Commerce Rich Item API
  phrasing_intents:
  - id: teckelGetAllergens
    intent: List allergens available for rich items
    question: Which allergens can I tag on a menu item?
  - id: teckelGetLocales
    intent: Get a business's item languages
    question: Which languages are my item descriptions set up in?
  - id: teckelUpdateLocales
    intent: Set a business's item languages
    question: How do I add French as an item language for my business?
  - id: teckelGetRichItems
    intent: List all rich items for a business
    question: How do I get all rich item descriptions and allergens for my business?
  - id: teckelGetRichItem
    intent: Get one rich item by SKU
    question: How do I fetch the rich content for a single SKU?
  - id: teckelUpdateRichItemPicture
    intent: Set the picture on a rich item
    question: How do I upload a photo for a menu item?
  - id: teckelCreateOrUpdateRichItem
    intent: Create or update a rich item's details
    question: How do I add allergens and descriptions to a menu item?
  - id: teckelDeleteRichItem
    intent: Delete a rich item
    question: How do I remove the rich content for an item?
  phrasing_ops: 10
  slug: lightspeed-rich-item-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Sale operations
  name: Lightspeed Commerce Sales API
  phrasing_intents:
  - id: ListSales
    intent: List sales
    question: What sales has my store made recently?
  - id: CreateSale
    intent: Record a new sale
    question: How do I push an order from my own system into the POS as a sale?
  - id: GetSaleByID
    intent: Get a sale
    question: What was sold and paid on a specific sale?
  - id: UpdateSale
    intent: Update an existing sale
    question: Can I add a payment or change the customer on a sale that's already recorded?
  - id: initReturnSale
    intent: Start a return for a sale
    question: How do I process a customer return against a closed sale?
  phrasing_ops: 5
  slug: lightspeed-sales-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Search related operations
  name: Lightspeed Commerce Search API
  phrasing_intents:
  - id: Search
    intent: Search sales, products or customers
    question: How do I find all sales made by a customer between two dates?
  phrasing_ops: 1
  slug: lightspeed-search-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Serial number related operations
  name: Lightspeed Commerce Serial Numbers API
  phrasing_intents:
  - id: get-serialnumbers
    intent: List serial numbers
    question: Which serial numbers are recorded for a product?
  - id: create-serialnumber
    intent: Record a serial number for a product
    question: How do I register a serial number for an item at an outlet?
  - id: delete-serialnumber
    intent: Delete a serial number
    question: How do I remove a serial number that was entered by mistake?
  - id: get-serialnumber
    intent: Get a single serial number
    question: How do I look up one serial number record by ID?
  phrasing_ops: 4
  slug: lightspeed-serial-numbers-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Service orders and Job management
  name: Lightspeed Commerce Service Orders API
  phrasing_intents:
  - id: ListServiceItems
    intent: List a customer's service items
    question: Which items has a customer brought in for repair or service?
  - id: ListServiceStatuses
    intent: List service order statuses
    question: What statuses can a service order move through in my store?
  - id: CreateServiceStatus
    intent: Create a custom service status
    question: How do I add a custom stage like 'Waiting for parts' to service orders?
  - id: DeleteServiceStatus
    intent: Delete a custom service status
    question: Can I delete a custom service status that is no longer used?
  - id: GetServiceStatus
    intent: Get a service status
    question: What are the details of one service status?
  - id: UpdateServiceStatus
    intent: Rename or reorder a service status
    question: Can I rename a custom service status?
  - id: ListServices
    intent: List service orders
    question: What service orders are open across my store?
  - id: CreateService
    intent: Create a service order
    question: How do I book a repair job for a customer at the register?
  phrasing_ops: 10
  slug: lightspeed-service-orders-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Shifts API from Lightspeed Commerce — 1 operation(s) for shifts.
  name: Lightspeed Commerce Shifts API
  phrasing_intents:
  - id: ListShifts
    intent: List shifts
    question: What shifts have been recorded in my retail store?
  phrasing_ops: 1
  slug: lightspeed-shifts-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Staff API. Authorisation Code grant type is required for this API with permission ROLE_CONFIG_USERS.
  name: Lightspeed Commerce Staff API
  phrasing_intents:
  - id: staff-apiGetShift
    intent: List staff shifts at a business location
    question: Which staff members clocked shifts at my restaurant last week?
  - id: staff-apiGetPOSStaff
    intent: List POS users at a business location
    question: Who has a login on the point-of-sale devices at this venue?
  - id: staff-apiCreatePOSStaff
    intent: Create a POS user
    question: How do I add a new server or cashier who logs in on the POS terminal?
  - id: staff-apiUpdatePOSStaff
    intent: Update an existing POS user
    question: Can I change the PIN code or roles of a POS user who already exists?
  - id: staff-apiGetBackOfficeStaff
    intent: List back office users at a location
    question: Which managers have back office access to this restaurant's dashboard?
  - id: staff-apiGetSingleStaff
    intent: Get one staff member's details
    question: What details are stored for a specific employee at a business location?
  - id: staff-apiGetPosUserGroups
    intent: List POS user groups
    question: What user groups exist for grouping POS staff at my venue?
  - id: staff-apiGetPosUserGroupById
    intent: Get a single POS user group
    question: Which roles and settings does a particular user group carry?
  phrasing_ops: 17
  slug: lightspeed-staff-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Store Credit operations
  name: Lightspeed Commerce Store Credits API
  phrasing_intents:
  - id: ListStoreCredit
    intent: List store credit customers and recent activity
    question: Which customers have store credit and what have they done with it lately?
  - id: BulkBalancesStoreCreditList
    intent: Get store credit balances in bulk
    question: How do I get just the balances of all store credit customers in one call?
  - id: BulkStoreCreditList
    intent: Get store credit customers and history in bulk
    question: Can I bulk-fetch store credit customers with their recent transaction lists?
  - id: StoreCreditReport
    intent: Get the store credit report
    question: Where can I see a report of all store credit in my store?
  - id: ListStoreCreditForCustomer
    intent: Get a customer's store credit history
    question: What store credit operations has a particular customer had?
  - id: StoreCreditBalanceForCustomer
    intent: Get a customer's store credit balance
    question: How much store credit does this customer have left?
  - id: CreateStoreCreditHold
    intent: Place a temporary hold on store credit
    question: How do I temporarily reserve part of a customer's store credit before checkout?
  - id: ReverseStoreCreditHold
    intent: Release a store credit hold
    question: How do I release a store credit hold if the customer abandons checkout?
  phrasing_ops: 9
  slug: lightspeed-store-credits-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Supplier operations
  name: Lightspeed Commerce Suppliers API
  phrasing_intents:
  - id: ListSuppliers
    intent: List suppliers
    question: Which suppliers do we buy stock from?
  - id: CreateSupplier
    intent: Add a new supplier
    question: How do I add a new supplier with their contact details?
  - id: DeleteSupplierById
    intent: Delete a supplier
    question: What happens to products linked to a supplier when I delete it?
  - id: GetSupplierByID
    intent: Get a single supplier
    question: What contact details do we hold for a particular supplier?
  - id: UpdateSupplierByID
    intent: Update a supplier
    question: How do I change an existing supplier's contact or markup?
  phrasing_ops: 5
  slug: lightspeed-suppliers-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Tag operations
  name: Lightspeed Commerce Tags API
  phrasing_intents:
  - id: ListTags
    intent: List product tags
    question: What tags am I using to group products?
  - id: CreateTag
    intent: Create a product tag
    question: How do I create a new tag to label products?
  - id: DeleteTagByID
    intent: Delete a product tag
    question: What happens to products when I delete their tag?
  - id: GetTagByID
    intent: Get a product tag
    question: What is the name of a tag with a given ID?
  - id: UpdateTagByID
    intent: Rename a product tag
    question: Can I rename a tag without retagging all its products?
  phrasing_ops: 5
  slug: lightspeed-tags-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Tax Breakdown API from Lightspeed Commerce — 1 operation(s) for tax breakdown.
  name: Lightspeed Commerce Tax Breakdown API
  phrasing_intents:
  - id: tax-preview-apiTaxBreakdown
    intent: Preview the tax breakdown of an order
    question: How much tax will a proposed order carry before I submit it?
  phrasing_ops: 1
  slug: lightspeed-tax-breakdown-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Tax operations
  name: Lightspeed Commerce Taxes API
  phrasing_intents:
  - id: ListTaxes
    intent: List sales taxes
    question: What sales tax rates are set up in my store?
  - id: CreateTax
    intent: Create a sales tax
    question: How do I add a new sales tax rate?
  - id: GetTaxByID
    intent: Get a single tax
    question: What rate does a particular tax apply?
  phrasing_ops: 3
  slug: lightspeed-taxes-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: User operations
  name: Lightspeed Commerce Users API
  phrasing_intents:
  - id: GetUser
    intent: Get the currently signed-in user
    question: Which user is my API token acting as?
  - id: ListUsers
    intent: List staff users
    question: What staff user accounts exist in my store?
  - id: GetUsersById
    intent: Get several users by their IDs
    question: Can I fetch multiple specific users in one request?
  - id: DeleteUserByID
    intent: Delete a user
    question: How do I delete a staff member who has left?
  - id: GetUserByID
    intent: Get a single user
    question: How do I look up one staff member's user record?
  - id: GetSalesTotalsForUserByID
    intent: Get a user's sales totals
    question: How much has a particular staff member sold?
  - id: DeleteSessionsByUserID
    intent: Sign a user out of all sessions
    question: How do I force a user to log out everywhere?
  phrasing_ops: 7
  slug: lightspeed-users-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: The Variant Attributes API from Lightspeed Commerce — 2 operation(s) for variant attributes.
  name: Lightspeed Commerce Variant Attributes API
  phrasing_intents:
  - id: ListVariantAttributes
    intent: List variant attributes
    question: Which variant attributes like Size or Color are defined in my store?
  - id: CreateVariantAttribute
    intent: Create a variant attribute
    question: How do I add a new attribute like Size before creating variants?
  - id: DeleteVariantAttribute
    intent: Delete a variant attribute
    question: Why can't I delete a variant attribute that's used by a product family?
  - id: GetVariantAttributes
    intent: Get a single variant attribute
    question: How do I fetch one variant attribute by ID?
  - id: UpdateVariantAttribute
    intent: Rename a variant attribute
    question: How do I rename an existing variant attribute?
  phrasing_ops: 5
  slug: lightspeed-variant-attributes-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Webhook operations
  name: Lightspeed Commerce Webhooks API
  phrasing_intents:
  - id: get-webhooks
    intent: List retail webhooks
    question: Which webhooks are registered on my retail account?
  - id: post-webhooks
    intent: Create a retail webhook
    question: How do I get notified when a sale or product changes?
  - id: delete-webhooks-webhookId
    intent: Delete a retail webhook
    question: Can I permanently remove a webhook subscription?
  - id: get-webhooks-id
    intent: Get a retail webhook
    question: Is a particular webhook active and which URL does it call?
  - id: put-webhooks-id
    intent: Update a retail webhook
    question: Can I disable a webhook without deleting it?
  phrasing_ops: 5
  slug: lightspeed-webhooks-api
- baseURL: https://{domain_prefix}.retail.lightspeed.app
  baseurl_source: declared
  description: Workflow operations
  name: Lightspeed Commerce Workflows API
  phrasing_intents:
  - id: GetCustomFields
    intent: List custom field definitions for an entity
    question: What custom fields are defined on sales or products in my store?
  - id: CreateCustomField
    intent: Define a new custom field
    question: How do I add a new custom field to products or customers?
  - id: GetCustomFieldValues
    intent: Get custom field values on a record
    question: What custom field values are stored on a specific sale or customer?
  - id: SetCustomFieldValues
    intent: Set custom field values on a record
    question: How do I save custom field values onto a particular customer or sale?
  - id: delete-custom-field
    intent: Delete a custom field and its values
    question: What happens to stored values when I delete a custom field?
  - id: update-custom-field
    intent: Update a custom field definition
    question: Can I rename the title of an existing custom field?
  - id: get-remote-rules
    intent: List registered remote rules
    question: Which remote rule URLs are registered on my retailer account?
  - id: create-remote-rule
    intent: Register a remote rule URL
    question: How do I register my own service URL as a remote business rule?
  phrasing_ops: 12
  slug: lightspeed-workflows-api
artifact_total: 259
asyncapis:
- description: ''
  name: Lightspeed Webhooks
  slug: lightspeed-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/lightspeed/agentic-access/lightspeed-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lightspeed-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/rules/lightspeed-rules.yml
  title: ''
  type: Spectral
  url: rules/lightspeed-rules.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/json-ld/lightspeed-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lightspeed-context.jsonld
- group: design
  href: https://artifacts.apis.io/lightspeed/vocabulary/lightspeed-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lightspeed-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/lightspeed/hosts/lightspeed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lightspeed-hosts.yml
- group: build
  href: https://artifacts.apis.io/lightspeed/integrations/lightspeed-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/lightspeed-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/lightspeed/vendors/lightspeed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lightspeed-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.lightspeedhq.com/news/
- group: other
  href: https://artifacts.apis.io/lightspeed/capabilities/lightspeed-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lightspeed-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/lightspeed/scopes/lightspeed-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lightspeed-scopes.yml
- group: auth
  href: https://artifacts.apis.io/lightspeed/authentication/lightspeed-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lightspeed-authentication.yml
- group: auth
  href: https://artifacts.apis.io/lightspeed/security/lightspeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lightspeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lightspeedhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lightspeedhq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LightspeedHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightspeedcommerce
- group: company
  title: ''
  type: Blog
  url: https://www.lightspeedhq.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lightspeedhq.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightspeedhq.com/
- group: other
  title: ''
  type: X
  url: https://x.com/LightspeedHQ
- group: commercial
  href: https://artifacts.apis.io/lightspeed/plans/lightspeed-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lightspeed-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lightspeed/rate-limits/lightspeed-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lightspeed-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lightspeed/finops/lightspeed-finops.yml
  title: ''
  type: FinOps
  url: finops/lightspeed-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lightspeedhq.com/
- group: operate
  title: ''
  type: Support
  url: https://www.lightspeedhq.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lightspeedhq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lightspeedhq.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.lightspeedhq.com/login/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lightspeedhq.com/
- group: build
  href: https://artifacts.apis.io/lightspeed/packages/lightspeed-packages.yml
  title: ''
  type: Packages
  url: packages/lightspeed-packages.yml
- group: build
  href: https://artifacts.apis.io/lightspeed/packages/lightspeed-packages.yml
  title: ''
  type: SDKs
  url: packages/lightspeed-packages.yml
- group: agent
  href: https://artifacts.apis.io/lightspeed/mcp/lightspeed-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lightspeed-mcp.yml
- group: build
  href: https://artifacts.apis.io/lightspeed/mcp/lightspeed-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lightspeed-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lightspeed/llms/lightspeed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lightspeed-llms.txt
- group: other
  href: https://artifacts.apis.io/lightspeed/overlays/lightspeed-x-series-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lightspeed-x-series-overlay.yaml
- group: other
  href: https://artifacts.apis.io/lightspeed/overlays/lightspeed-k-series-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lightspeed-k-series-overlay.yaml
- group: design
  href: https://artifacts.apis.io/lightspeed/conformance/lightspeed-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lightspeed-conformance.yml
- group: auth
  href: https://artifacts.apis.io/lightspeed/security/lightspeed-trust-center.yml
  title: ''
  type: Compliance
  url: security/lightspeed-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lightspeed/security/lightspeed-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lightspeed-trust-center.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/errors/lightspeed-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lightspeed-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/lifecycle/lightspeed-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lightspeed-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/lightspeed/lifecycle/lightspeed-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/lightspeed-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/lightspeed/security/lightspeed-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lightspeed-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/lightspeed/security/lightspeed-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lightspeed-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/lightspeed/sandbox/lightspeed-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lightspeed-sandbox.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/conventions/lightspeed-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lightspeed-conventions.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/conventions/lightspeed-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/lightspeed-conventions.yml
- group: operate
  href: https://artifacts.apis.io/lightspeed/changelog/lightspeed-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lightspeed-changelog.yml
- group: build
  href: https://artifacts.apis.io/lightspeed/cli/lightspeed-cli.yml
  title: ''
  type: CLI
  url: cli/lightspeed-cli.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/components/lightspeed-components.yml
  title: ''
  type: Components
  url: components/lightspeed-components.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/data-model/lightspeed-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lightspeed-data-model.yml
- group: design
  href: https://artifacts.apis.io/lightspeed/asyncapi/lightspeed-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lightspeed-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/lightspeed/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/lightspeed/openapi/_original/lightspeed-x-series-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/lightspeed-x-series-openapi.json
- group: docs
  href: https://artifacts.apis.io/lightspeed/openapi/_original/lightspeed-k-series-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/lightspeed-k-series-openapi.json
- group: design
  href: https://artifacts.apis.io/lightspeed/json-ld/lightspeed.json
  title: ''
  type: JSONLD
  url: json-ld/lightspeed.json
- group: docs
  title: ''
  type: APIReference
  url: https://x-series-api.lightspeedhq.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://x-series-api.lightspeedhq.com/docs/quick_start
- group: build
  title: ''
  type: Postman
  url: https://developers.lightspeedhq.com/ecom/introduction/images/Lightspeed_eCom.postman_collection.json
created: '2026-06-13'
description: Omnichannel commerce platform with REST APIs for retail and restaurant POS, inventory management, loyalty programs, and e-commerce integrations. Lightspeed serves retailers and restaurateurs with cloud-based point-of-sale systems, enabling custom integrations through APIs for sales, inventory, customers, orders, payments, and loyalty programs across multiple product lines including Retail X-Series, Retail R-Series, Restaurant K-Series, and eCom.
finops:
- has_sources: true
  method: derived
  name: Lightspeed Finops
  primary_unit: subscription
  service_category: ''
  slug: lightspeed-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightspeed.png
json_schemas:
- name: apeAccountSnapshot
  property_count: 19
  slug: lightspeed-ape-account-snapshot
- name: apeCustomerInfo
  property_count: 9
  slug: lightspeed-ape-customer-info
- name: apeLocalOrderItemLine
  property_count: 10
  slug: lightspeed-ape-local-order-item-line
- name: apeMenuV2
  property_count: 5
  slug: lightspeed-ape-menu-v2
- name: apeStandalonePayment
  property_count: 12
  slug: lightspeed-ape-standalone-payment
- name: apeToGoOrderItemLine
  property_count: 9
  slug: lightspeed-ape-to-go-order-item-line
- name: apeWebhookEndpointBusinessLocationDto
  property_count: 4
  slug: lightspeed-ape-webhook-endpoint-business-location-dto
- name: apeWebhookEndpoint
  property_count: 9
  slug: lightspeed-ape-webhook-endpoint
- name: Audit Log Event
  property_count: 11
  slug: lightspeed-audit-log-event
- name: Brand
  property_count: 2
  slug: lightspeed-brand-base
- name: Brand Collection
  property_count: 2
  slug: lightspeed-brand-collection
- name: Brand Response
  property_count: 1
  slug: lightspeed-brand-response
- name: Business Rule
  property_count: 4
  slug: lightspeed-business-rule
- name: ButtonLayoutCollection
  property_count: 3
  slug: lightspeed-button-layout-collection
- name: ButtonLayout
  property_count: 5
  slug: lightspeed-button-layout
- name: Channels response
  property_count: 1
  slug: lightspeed-channel-collection-response
- name: Consignment Collection
  property_count: 2
  slug: lightspeed-consignment-collection
- name: Consignment Product Collection
  property_count: 1
  slug: lightspeed-consignment-product-collection
- name: Consignment Product Request
  property_count: 1
  slug: lightspeed-consignment-product-request
- name: Consignment Product Response
  property_count: 1
  slug: lightspeed-consignment-product-response
- name: Consignment Product
  property_count: 11
  slug: lightspeed-consignment-product
- name: Consignment Request
  property_count: 1
  slug: lightspeed-consignment-request
- name: Consignment Response
  property_count: 1
  slug: lightspeed-consignment-response
- name: ConsignmentTotalsResponse
  property_count: 1
  slug: lightspeed-consignment-totals-response
- name: Create Custom Inventory Adjustment Reason Request
  property_count: 3
  slug: lightspeed-create-custom-inventory-adjustment-reason-request
- name: CreateSupplierRequest
  property_count: 4
  slug: lightspeed-create-supplier-request
- name: CreateTagRequest
  property_count: 1
  slug: lightspeed-create-tag-request
- name: CreateTaxRequest
  property_count: 5
  slug: lightspeed-create-tax-request
- name: Custom Field Definition Parameters
  property_count: 7
  slug: lightspeed-custom-field-definition-params
- name: Custom Field Definition
  property_count: 8
  slug: lightspeed-custom-field-definition
- name: Custom Field Value Parameters
  property_count: 3
  slug: lightspeed-custom-field-values-params
- name: Customer Address Base
  property_count: 9
  slug: lightspeed-customer-address-base
- name: Customer Address Collection
  property_count: 1
  slug: lightspeed-customer-address-collection
- name: Customer Address Create Response
  property_count: 1
  slug: lightspeed-customer-address-create-response
- name: Customer Address Response
  property_count: 1
  slug: lightspeed-customer-address-response
- name: Customer Base
  property_count: 37
  slug: lightspeed-customer-base
- name: Customer Collection
  property_count: 2
  slug: lightspeed-customer-collection
- name: Customer Group Collection
  property_count: 2
  slug: lightspeed-customer-group-collection
- name: Customer Group Response
  property_count: 1
  slug: lightspeed-customer-group-response
- name: Customer Group
  property_count: 8
  slug: lightspeed-customer-group
- name: Customer Response
  property_count: 1
  slug: lightspeed-customer-response
- name: DailyAgenda
  property_count: 2
  slug: lightspeed-daily-agenda
- name: DetailedService
  property_count: 3
  slug: lightspeed-detailed-service
- name: DiscountParam consists of a Sale, and related information to check if a promotion applies, and to calculate the discount
  property_count: 6
  slug: lightspeed-discount-param
- name: DiscountParam consists of a Sale, and related information to check if a promotion applies, and to calculate the discount
  property_count: 1
  slug: lightspeed-discount-response
- name: financial-apiAbortedOrderDto
  property_count: 4
  slug: lightspeed-financial-api-aborted-order-dto
- name: financial-apiFinancialDto
  property_count: 6
  slug: lightspeed-financial-api-financial-dto
- name: financial-apiLSPaymentsDto
  property_count: 4
  slug: lightspeed-financial-api-lspayments-dto
- name: financial-apiResourcesTaxRate
  property_count: 2
  slug: lightspeed-financial-api-resources-tax-rate
- name: financial-apiSaleDto
  property_count: 22
  slug: lightspeed-financial-api-sale-dto
- name: financial-apiSalesDailyExportDto
  property_count: 3
  slug: lightspeed-financial-api-sales-daily-export-dto
- name: financial-apiSalesExportDto
  property_count: 2
  slug: lightspeed-financial-api-sales-export-dto
- name: FulfillLineItemsRequest
  property_count: 2
  slug: lightspeed-fulfill-line-items-request
- name: FulfillLineItemsResponse
  property_count: 1
  slug: lightspeed-fulfill-line-items-response
- name: FulfillmentHistoryResponse
  property_count: 2
  slug: lightspeed-fulfillment-history-response
- name: GetUsersByIdsRequest
  property_count: 0
  slug: lightspeed-get-users-by-ids-request
- name: Gift Card Activation Parameters
  property_count: 5
  slug: lightspeed-gift-card-activation-params
- name: Gift Card Collection
  property_count: 1
  slug: lightspeed-gift-card-collection
- name: Gift Card
  property_count: 11
  slug: lightspeed-gift-card
- name: Gift Card Response
  property_count: 1
  slug: lightspeed-gift-card-singleton
- name: Gift Card Transaction Parameters
  property_count: 6
  slug: lightspeed-gift-card-transaction-params
- name: Gift Card Transaction Response
  property_count: 1
  slug: lightspeed-gift-card-transaction-singleton
- name: id-cards-apiCreateIdCardBatchRequest
  property_count: 1
  slug: lightspeed-id-cards-api-create-id-card-batch-request
- name: id-cards-apiCreateIdCardsRequest
  property_count: 1
  slug: lightspeed-id-cards-api-create-id-cards-request
- name: id-cards-apiCreateIdCardsResponse
  property_count: 2
  slug: lightspeed-id-cards-api-create-id-cards-response
- name: id-cards-apiIdCardBatch
  property_count: 3
  slug: lightspeed-id-cards-api-id-card-batch
- name: Image Position
  property_count: 1
  slug: lightspeed-image-position
- name: Image Response
  property_count: 1
  slug: lightspeed-image-response
- name: Inventory Count Item Response
  property_count: 1
  slug: lightspeed-inventory-count-item-response
- name: InventoryLevel
  property_count: 15
  slug: lightspeed-inventory-level
- name: InventoryLevelsRequest
  property_count: 12
  slug: lightspeed-inventory-levels-request
- name: InventoryRequest
  property_count: 7
  slug: lightspeed-inventory-request
- name: Inventory
  property_count: 12
  slug: lightspeed-inventory
- name: items-apiCreateItemDTO
  property_count: 11
  slug: lightspeed-items-api-create-item-dto
- name: items-apiItemDTO
  property_count: 19
  slug: lightspeed-items-api-item-dto
- name: items-apiUpdateItemDTO
  property_count: 11
  slug: lightspeed-items-api-update-item-dto
- name: LoyaltyAdjustmentCreateBody
  property_count: 2
  slug: lightspeed-loyalty-adjustment-create-body
- name: LoyaltyAdjustmentResponse
  property_count: 2
  slug: lightspeed-loyalty-adjustment-response
- name: Outlet Collection
  property_count: 2
  slug: lightspeed-outlet-collection
- name: Outlet Response
  property_count: 1
  slug: lightspeed-outlet-response
- name: OutletTaxCollection
  property_count: 2
  slug: lightspeed-outlet-tax-collection
- name: PackLineItemsRequest
  property_count: 2
  slug: lightspeed-pack-line-items-request
- name: PackLineItemsResponse
  property_count: 1
  slug: lightspeed-pack-line-items-response
- name: Partial Packing Slip Request
  property_count: 2
  slug: lightspeed-partial-packing-slip-request
- name: PartnerSubscription
  property_count: 3
  slug: lightspeed-partner-subscription
- name: PartnerSubscriptionTokenRequest
  property_count: 5
  slug: lightspeed-partner-subscription-token-request
- name: PartnerSubscriptionTokenResponse
  property_count: 3
  slug: lightspeed-partner-subscription-token-response
- name: PartnerSubscriptionToken
  property_count: 11
  slug: lightspeed-partner-subscription-token
- name: PartnerSubscriptions
  property_count: 0
  slug: lightspeed-partner-subscriptions
- name: PartnerUpdateSubscriptionTokenRequest
  property_count: 4
  slug: lightspeed-partner-update-subscription-token-request
- name: PaymentTypeCollection
  property_count: 2
  slug: lightspeed-payment-type-collection
- name: PickLineItemsRequest
  property_count: 2
  slug: lightspeed-pick-line-items-request
- name: pms-apiBusinessLocationId
  property_count: 0
  slug: lightspeed-pms-api-business-location-id
- name: pms-apiGetProvider
  property_count: 6
  slug: lightspeed-pms-api-get-provider
- name: pms-apiProviderApiKey
  property_count: 0
  slug: lightspeed-pms-api-provider-api-key
- name: pms-apiProviderEndpoint
  property_count: 0
  slug: lightspeed-pms-api-provider-endpoint
- name: pms-apiProviderFeatures
  property_count: 0
  slug: lightspeed-pms-api-provider-features
- name: pms-apiProviderName
  property_count: 0
  slug: lightspeed-pms-api-provider-name
- name: Price Book Collection
  property_count: 1
  slug: lightspeed-price-book-collection
- name: Price Book Create Request
  property_count: 6
  slug: lightspeed-price-book-create-request
- name: Price Book Product Collection
  property_count: 1
  slug: lightspeed-price-book-product-collection
- name: Price Book Product ID Collection
  property_count: 1
  slug: lightspeed-price-book-product-id-collection
- name: Price Book Products Update Response
  property_count: 1
  slug: lightspeed-price-book-products-update-response
- name: Price Book Update Request
  property_count: 6
  slug: lightspeed-price-book-update-request
- name: ProductCategory
  property_count: 6
  slug: lightspeed-product-category
- name: Product Collection
  property_count: 2
  slug: lightspeed-product-collection
- name: Product
  property_count: 35
  slug: lightspeed-product-create-body
- name: Product Response
  property_count: 1
  slug: lightspeed-product-response
- name: Product Type Collection
  property_count: 2
  slug: lightspeed-product-type-collection
- name: Product Type Response
  property_count: 1
  slug: lightspeed-product-type-response
- name: Product Update 2.1 Request
  property_count: 2
  slug: lightspeed-product-update21-request
- name: Map of Promo Codes to booleans
  property_count: 0
  slug: lightspeed-promo-codes-map
- name: Promotion Promo Codes response
  property_count: 0
  slug: lightspeed-promotion-delete-promo-codes-response
- name: Promotion Products response
  property_count: 1
  slug: lightspeed-promotion-products-response
- name: Promotion Promo Codes response
  property_count: 1
  slug: lightspeed-promotion-promo-codes-response
- name: Promotion response
  property_count: 19
  slug: lightspeed-promotion-response
- name: Promotion
  property_count: 15
  slug: lightspeed-promotion
- name: Purchase Order Collection Response
  property_count: 2
  slug: lightspeed-purchase-order-collection-response
- name: Purchase Order Delivery Collection Response
  property_count: 2
  slug: lightspeed-purchase-order-delivery-collection-response
- name: Purchase Order Delivery Line Item Collection Response
  property_count: 2
  slug: lightspeed-purchase-order-delivery-line-item-collection-response
- name: Purchase Order Line Item Collection Response
  property_count: 2
  slug: lightspeed-purchase-order-line-item-collection-response
- name: Purchase Order Response
  property_count: 1
  slug: lightspeed-purchase-order-response
- name: Quote
  property_count: 19
  slug: lightspeed-quote
- name: QuotesCollection
  property_count: 3
  slug: lightspeed-quotes-collection
- name: Register Close Request
  property_count: 1
  slug: lightspeed-register-close-request
- name: Register Collection
  property_count: 2
  slug: lightspeed-register-collection
- name: Register Open Request
  property_count: 1
  slug: lightspeed-register-open-request
- name: Register Payments Summary Response
  property_count: 1
  slug: lightspeed-register-payments-summary-response
- name: Remote Business Rules
  property_count: 4
  slug: lightspeed-remote-business-rule
- name: Request Logs response
  property_count: 1
  slug: lightspeed-request-collection-response
- name: Request Log response
  property_count: 1
  slug: lightspeed-request-single-response
- name: reservation-servicePlatformBearerTokenWebhook
  property_count: 2
  slug: lightspeed-reservation-service-platform-bearer-token-webhook
- name: reservation-servicePlatformBusinessLocation
  property_count: 8
  slug: lightspeed-reservation-service-platform-business-location
- name: reservation-servicePlatformOAuth2Webhook
  property_count: 8
  slug: lightspeed-reservation-service-platform-oauth2-webhook
- name: reservation-servicePlatformProfileResponse
  property_count: 14
  slug: lightspeed-reservation-service-platform-profile-response
- name: reservation-servicePlatformProfile
  property_count: 15
  slug: lightspeed-reservation-service-platform-profile
- name: reservation-servicePlatformReservation
  property_count: 13
  slug: lightspeed-reservation-service-platform-reservation
- name: Retailer response
  property_count: 1
  slug: lightspeed-retailer-response
- name: Sale Collection
  property_count: 2
  slug: lightspeed-sale-collection
- name: Sale Create Response
  property_count: 1
  slug: lightspeed-sale-create-response
- name: Sale Request
  property_count: 16
  slug: lightspeed-sale-request
- name: Sale Response
  property_count: 1
  slug: lightspeed-sale-response
- name: Sale Update Request
  property_count: 15
  slug: lightspeed-sale-update-request
- name: Search Response
  property_count: 1
  slug: lightspeed-search-response
- name: Serial Number Collection
  property_count: 2
  slug: lightspeed-serial-number-collection
- name: Request to create a sale
  property_count: 3
  slug: lightspeed-serial-number-request
- name: Serial Number Response
  property_count: 1
  slug: lightspeed-serial-number-response
- name: ServiceOrderRequest
  property_count: 10
  slug: lightspeed-service-order-request
- name: ServiceOrder
  property_count: 13
  slug: lightspeed-service-order
- name: ServiceStatusDetails
  property_count: 8
  slug: lightspeed-service-status-details
- name: Set Reorder Points Request
  property_count: 0
  slug: lightspeed-set-reorder-points-request
- name: Shift Collection
  property_count: 2
  slug: lightspeed-shift-collection
- name: staff-apiBOStaff
  property_count: 13
  slug: lightspeed-staff-api-bostaff
- name: staff-apiPOSStaff
  property_count: 15
  slug: lightspeed-staff-api-posstaff
- name: staff-apiResponseSchema
  property_count: 3
  slug: lightspeed-staff-api-response-schema
- name: staff-apiShift
  property_count: 8
  slug: lightspeed-staff-api-shift
- name: staff-apiStaff
  property_count: 16
  slug: lightspeed-staff-api-staff
- name: staff-apiUpdatePosStaffDto
  property_count: 9
  slug: lightspeed-staff-api-update-pos-staff-dto
- name: Store Credit Bulk Response
  property_count: 1
  slug: lightspeed-store-credit-bulk-response
- name: Store Credit Customer Balance
  property_count: 4
  slug: lightspeed-store-credit-customer-balance
- name: Store Credit Customer
  property_count: 7
  slug: lightspeed-store-credit-customer
- name: Store Credit Report
  property_count: 3
  slug: lightspeed-store-credit-report
- name: Store Credit Transaction Parameters for Customer
  property_count: 5
  slug: lightspeed-store-credit-transaction-params
- name: Store Credit Transaction for Customer
  property_count: 8
  slug: lightspeed-store-credit-transaction
- name: Supplier Collection
  property_count: 2
  slug: lightspeed-supplier-collection
- name: Supplier Response
  property_count: 1
  slug: lightspeed-supplier-response
- name: Tag Collection
  property_count: 2
  slug: lightspeed-tag-collection
- name: Tag Response
  property_count: 1
  slug: lightspeed-tag-response
- name: Tax Collection
  property_count: 1
  slug: lightspeed-tax-collection
- name: Tax Response
  property_count: 1
  slug: lightspeed-tax-response
- name: teckelLinkSelfPage
  property_count: 1
  slug: lightspeed-teckel-link-self-page
- name: teckelPictureSpecDto
  property_count: 4
  slug: lightspeed-teckel-picture-spec-dto
- name: teckelRichItemDescriptionDto
  property_count: 3
  slug: lightspeed-teckel-rich-item-description-dto
- name: teckelRichItemDtoDates
  property_count: 2
  slug: lightspeed-teckel-rich-item-dto-dates
- name: teckelRichItemDtoPictures
  property_count: 3
  slug: lightspeed-teckel-rich-item-dto-pictures
- name: teckelRichItemDto
  property_count: 4
  slug: lightspeed-teckel-rich-item-dto
- name: Parameters for updating a custom field
  property_count: 4
  slug: lightspeed-update-custom-field-params
- name: User Collection
  property_count: 2
  slug: lightspeed-user-collection
- name: User Response
  property_count: 1
  slug: lightspeed-user-response
- name: User Sale Total Response
  property_count: 1
  slug: lightspeed-user-sale-total-response
- name: VariantAttributeResponse
  property_count: 3
  slug: lightspeed-variant-attribute-response
- name: WebhookRequest
  property_count: 3
  slug: lightspeed-webhook-request
- name: Webhook
  property_count: 5
  slug: lightspeed-webhook
jsonld:
- class_count: 120
  name: Lightspeed Context
  property_count: 311
  slug: lightspeed-context
layout: provider
mcp_servers:
- description: 'Lightspeed runs two hosted, anonymous MCP servers — one per documentation platform. Both are documentation-plane servers: they let an agent read and search the API contract. Only the X-Series server c'
  name: Lightspeed Commerce MCP Servers
  slug: lightspeed-commerce-mcp-servers
modified: '2026-09-16'
name: Lightspeed Commerce
nav: Providers
network: true
overview: 'Lightspeed Commerce publishes 58 API contracts indexed on the [APIs.io](https://apis.io/) network, including Lightspeed eCom API, Audit API, Brands API, and 55 more. Tagged areas include Commerce, Point-of-Sale, Retail, Restaurant, and Inventory.


  The Lightspeed Commerce catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Lightspeed Commerce''s developer surface includes authentication, documentation, engineering blog, pricing, support, signup flow, sandbox, and 52 more developer resources.'
plans:
- name: Lightspeed Plans Pricing
  plan_count: 6
  slug: lightspeed-plans-pricing
- name: Lightspeed Price Estimates
  plan_count: 0
  slug: lightspeed-price-estimates
random_paper: 9
rate_limits:
- limit_count: 6
  name: Lightspeed Rate Limits
  slug: lightspeed-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Lightspeed Commerce API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: lightspeed-rules
scopes:
- name: Lightspeed Scopes
  scope_count: 90
  slug: lightspeed-scopes
  summary_line: 90 scopes · authorizationCode
score:
  band: exemplar
  composite: 86.5
  coverage:
    artifact_dirs: 38
    catalog_earned: 92.8
    catalog_earned_first_party: 24.0
    catalog_gap: 22.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 100.0
    contract_governance: 22.0
    contract_quality: 79.4
    developer_ergonomics: 85.1
    discoverability: 80.8
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 85.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 77.4
      total: 53
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/lightspeed/lightspeed-2026-06-20T184527.png
security:
- kind: authentication
  name: Lightspeed Authentication
  slug: lightspeed-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lightspeed Domain Security
  slug: lightspeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lightspeed Vulnerability Disclosure
  slug: lightspeed-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lightspeed Trust Center
  slug: lightspeed-trust-center
  summary_line: PCI DSS, SOC 2, SOC 3, GDPR
skill_count: 4
skills:
- name: lightspeed-gift-card-transaction
  slug: lightspeed-gift-card-transaction
- name: lightspeed-restaurant-online-order
  slug: lightspeed-restaurant-online-order
- name: lightspeed-sync-external-sale
  slug: lightspeed-sync-external-sale
- name: lightspeed-webhook-subscription
  slug: lightspeed-webhook-subscription
slug: lightspeed
tags:
- Commerce
- Point-of-Sale
- Retail
- Restaurant
- Inventory
- Loyalty
- Payments
- E-Commerce
- Omnichannel
- Canada
website: https://www.lightspeedhq.com/
---
