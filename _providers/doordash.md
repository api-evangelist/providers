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
  - rate-limits
  - security
  - sandbox
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 90
  human_in_the_loop: 1
  name: Doordash Agentic Access
  operation_count: 151
  slug: doordash-agentic-access
  summary_line: 151 operations · 90 acting · 1 human-in-the-loop
api_count: 14
apis:
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Get address auto-completion suggestions based on partial input.
  name: doordash Addresses API
  phrasing_intents:
  - id: getAddressSuggestions
    intent: Get address suggestions for partial input
    question: Where can I get address autocomplete suggestions from a partial address?
  phrasing_ops: 1
  slug: doordash-addresses-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Manage business entities that represent legal entities or owners.
  name: doordash Businesses API
  phrasing_intents:
  - id: listBusinesses
    intent: List the businesses on my account
    question: Which businesses are on my developer account?
  - id: createBusiness
    intent: Create a business entity
    question: How do I register a new business entity for a merchant?
  - id: getBusiness
    intent: Get one business by external ID
    question: What details are stored for one business?
  - id: updateBusiness
    intent: Update a business's name or description
    question: How do I change a business's name or description?
  phrasing_ops: 4
  slug: doordash-businesses-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Manage the item catalog including adding new items and updating existing item information such as names, descriptions, images, and attributes.
  name: doordash Catalog API
  phrasing_intents:
  - id: validateCatalogProducts
    intent: Check catalog products are eligible for ads
    question: Which of my catalog products are eligible to advertise?
  - id: createItems
    intent: Add new items to the item catalog
    question: How do I add new items to the DoorDash catalog by merchant supplied ID?
  - id: updateItems
    intent: Update existing catalog items
    question: How do I fix details on items already in my catalog?
  phrasing_ops: 3
  slug: doordash-catalog-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Create, retrieve, update, cancel, and estimate deliveries using the classic API endpoints.
  name: doordash Deliveries API
  phrasing_intents:
  - id: createDeliveryEstimate
    intent: Estimate a delivery's fee and time
    question: How much will a delivery cost and how long will it take between two addresses?
  - id: createDelivery
    intent: Create a delivery and dispatch a Dasher
    question: How do I request a Dasher to deliver an order from my store to a customer?
  - id: getDelivery
    intent: Get a delivery's status and details
    question: Where is my delivery right now and what is its status?
  - id: updateDelivery
    intent: Update a delivery's tip or dropoff details
    question: Can I change the tip or dropoff instructions on a delivery in progress?
  - id: cancelDelivery
    intent: Cancel an active delivery
    question: How do I cancel a delivery I no longer need?
  - id: sendCheckoutAuditSignal
    intent: Send a checkout audit signal
    question: What checkout events can I report for tracking a delivery's checkout flow?
  phrasing_ops: 6
  slug: doordash-deliveries-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Manage store-level inventory, pricing, and other in-store attributes for items on the DoorDash platform.
  name: doordash Inventory API
  phrasing_intents:
  - id: createStoreInventory
    intent: Add store pricing and inventory for items
    question: How do I set price and inventory for catalog items at one store?
  - id: updateStoreInventory
    intent: Update store pricing and inventory for items
    question: How quickly do price changes at a store show up?
  phrasing_ops: 2
  slug: doordash-inventory-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Manage item availability and 86ing (marking items as unavailable) in real time.
  name: doordash Items API
  phrasing_intents:
  - id: updateItemStatus
    intent: Mark items in or out of stock at a store
    question: What's the way to 86 an item so customers can't order it?
  phrasing_ops: 1
  slug: doordash-items-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Create, update, and manage menus for stores on the DoorDash marketplace.
  name: doordash Menus API
  phrasing_intents:
  - id: createMenu
    intent: Upload a full menu for a store
    question: How do I upload a full menu for a store?
  - id: updateMenu
    intent: Update an existing store menu
    question: Can I change an existing menu's categories?
  phrasing_ops: 2
  slug: doordash-menus-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Receive, confirm, update, and manage orders placed through the DoorDash marketplace.
  name: doordash Orders API
  phrasing_intents:
  - id: updateOrder
    intent: Update an order's status or items
    question: Can I update the status of an order?
  phrasing_ops: 1
  slug: doordash-orders-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Manage item-level promotions at the store level, including adding and updating promotional pricing.
  name: doordash Promotions API
  phrasing_intents:
  - id: createStorePromotions
    intent: Add item promotions at a store
    question: Where do I set promotional prices for items at a store?
  - id: updateStorePromotions
    intent: Update item promotions at a store
    question: Can I change item promotions already running at a store?
  phrasing_ops: 2
  slug: doordash-promotions-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Validate delivery serviceability and get pricing quotes before creating a delivery.
  name: doordash Quotes API
  phrasing_intents:
  - id: createDeliveryQuote
    intent: Create a delivery quote
    question: How do I check if a delivery is serviceable and what it costs before committing?
  - id: acceptDeliveryQuote
    intent: Accept a delivery quote
    question: What do I call to accept a quote and dispatch a Dasher?
  phrasing_ops: 2
  slug: doordash-quotes-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Create report requests and retrieve report download links for financial, operations, menu, and feedback data.
  name: doordash Reports API
  phrasing_intents:
  - id: createReport
    intent: Request a report for my stores
    question: How do I request a report for my stores?
  - id: getReportLink
    intent: Get a report's status and download link
    question: Has my report finished, and where is its download link?
  phrasing_ops: 2
  slug: doordash-reports-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Manage store locations associated with businesses.
  name: doordash Stores API
  phrasing_intents:
  - id: createStore
    intent: Create a store under a business
    question: How do I add a new store location to a business?
  - id: getStore
    intent: Get a store under a business
    question: What are the details of a store under a business?
  - id: updateStore
    intent: Update a store's name or address
    question: Can I change a store location's name or address?
  - id: getStoreDetails
    intent: Get live store details by merchant ID
    question: What live store-level info does the integration show for my store?
  - id: getMenuDetails
    intent: Get live menu details for a store
    question: What live menu info is set for a store on the integration?
  - id: updateStoreStatus
    intent: Open or close a store for orders
    question: How do I close my store for orders temporarily?
  phrasing_ops: 6
  slug: doordash-stores-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Ad Groups API from Doordash — 2 operation(s) for ad groups.
  name: Doordash Ad Groups API
  phrasing_intents:
  - id: createAdGroup
    intent: Create a new ad group in a campaign
    question: What do I need to set up a new ad group, such as dates and manual targets?
  - id: updateAdGroup
    intent: Update an ad group's bids, dates or status
    question: How do I pause an ad group that is already live?
  - id: getAdGroups
    intent: List ad groups in my campaigns
    question: Which ad groups are running under my sponsored product campaigns?
  - id: getAdGroupById
    intent: Get one ad group by its ID
    question: What are the settings of one specific ad group?
  phrasing_ops: 4
  slug: doordash-ad-groups-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Address API from Doordash — 5 operation(s) for address.
  name: Doordash Address API
  phrasing_intents:
  - id: GetAddressAutoComplete
    intent: Autocomplete a partial address for Drive
    question: How do I suggest full addresses while a Drive user types a dropoff address?
  - id: GetAutocompleteSuggestionsForAddressInput
    intent: Suggest storefront addresses for typed input
    question: What storefront address suggestions match what a shopper has typed so far?
  - id: GetAddressDetailsById
    intent: Get full details for a suggested address
    question: How do I get the full details of an address the shopper picked from the suggestions?
  - id: GetAddressesByGeocode
    intent: Find addresses near a latitude and longitude
    question: Which addresses are closest to a point on the map?
  - id: GetOrCreateAddress
    intent: Get or create an address from a full string
    question: How do I turn a full formatted address string into a saved address record?
  phrasing_ops: 5
  slug: doordash-address-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for mobile app related information
  name: Doordash App API
  phrasing_intents:
  - id: getMinimumApplicationVersion
    intent: Check the minimum mobile app version
    question: What is the minimum app version my iOS or Android storefront app must run?
  - id: getAppMetadata
    intent: Get mobile app metadata for an integration
    question: What metadata does the storefront mobile app need to start up?
  phrasing_ops: 2
  slug: doordash-app-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Assets API from Doordash — 3 operation(s) for assets.
  name: Doordash Assets API
  phrasing_intents:
  - id: postAdsApiV1Assets
    intent: Create an ad asset and get its upload URL
    question: How do I get an upload URL for a new image I want to use in a DoorDash ad?
  - id: getAdsApiV1AssetsByAssetId
    intent: Look up an ad asset by its ID
    question: Where can I see the details of one ad asset I already created?
  - id: postAdsApiV1AssetsByAssetIdRegister
    intent: Register an asset after its upload finishes
    question: What do I do once I've finished uploading the file for an ad asset?
  phrasing_ops: 3
  slug: doordash-assets-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Audit API from Doordash — 1 operation(s) for audit.
  name: Doordash Audit API
  phrasing_intents:
  - id: CheckoutAuditSignal
    intent: Record a checkout audit result for a delivery
    question: Can I report the result of a virtual checkout audit for a delivery?
  phrasing_ops: 1
  slug: doordash-audit-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Business & Store API from Doordash — 9 operation(s) for business & store.
  name: Doordash Business & Store API
  phrasing_intents:
  - id: GetBusiness
    intent: Get a Drive business's details
    question: What details are on file for a business I set up in Drive?
  - id: UpdateBusiness
    intent: Update a Drive business
    question: How do I rename a Drive business?
  - id: CreateBusiness
    intent: Create a Drive business
    question: How do I create a new business in Drive?
  - id: ListBusiness
    intent: List my Drive businesses
    question: Which businesses does my developer account own?
  - id: GetStore
    intent: Get a Drive store's details
    question: What address and phone number are on file for one of my Drive stores?
  - id: UpdateStore
    intent: Update a Drive store's name, phone or address
    question: How do I change a Drive store's phone number?
  - id: CreateStore
    intent: Create a Drive store under a business
    question: How do I add a new pickup store to a Drive business?
  - id: ListStore
    intent: List the Drive stores under a business
    question: Which Drive stores belong to a given business?
  phrasing_ops: 13
  slug: doordash-business-store-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Campaigns API from Doordash — 3 operation(s) for campaigns.
  name: Doordash Campaigns API
  phrasing_intents:
  - id: createCampaign
    intent: Create an ad campaign
    question: How do I launch a new DoorDash ad campaign with a budget?
  - id: updateCampaign
    intent: Update an ad campaign's budget, dates or status
    question: How do I raise the budget on an existing ad campaign?
  - id: getCampaigns
    intent: List ad campaigns
    question: What ad campaigns do I have running?
  - id: getCampaignById
    intent: Get one ad campaign by ID
    question: What are the settings of one particular campaign?
  - id: getBudgetCapoutRecommendations
    intent: Get budget capout recommendations for a campaign
    question: Is my campaign running out of budget early, and what is recommended?
  phrasing_ops: 5
  slug: doordash-campaigns-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for managing checkout and transactions
  name: Doordash Checkout Management Endpoints API
  phrasing_intents:
  - id: authorizeTransaction
    intent: Authorize a DoorDash Direct checkout transaction
    question: How do I authorize a checkout transaction using a DoorDash Direct scan code?
  - id: batchAddTransactions
    intent: Submit a batch of checkout transactions
    question: Can I submit multiple checkout transactions for a store at once?
  phrasing_ops: 2
  slug: doordash-checkoutmanagementendpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: For Sponsored Brand campaigns only.
  name: Doordash Creatives (SB) API
  phrasing_intents:
  - id: postAdsApiV1SbCreatives
    intent: Add new creatives to a campaign ad group
    question: How do I add new creatives to an ad group in a sponsored brand campaign?
  - id: getAdsApiV1SbCreatives
    intent: List the creatives in my campaigns
    question: Which sponsored brand creatives are running in my campaigns?
  phrasing_ops: 2
  slug: doordash-creatives-sb-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The DasherFeedback API from Doordash — 2 operation(s) for dasherfeedback.
  name: Doordash Dasher Feedback API
  phrasing_intents:
  - id: GetAssignments
    intent: See which Dashers were assigned to a delivery
    question: Which Dashers have been assigned to my delivery over time?
  - id: RateDasher
    intent: Rate the Dasher on a delivery
    question: How do I rate the Dasher who handled a delivery?
  phrasing_ops: 2
  slug: doordash-dasherfeedback-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Dataexchange API from Doordash — 2 operation(s) for dataexchange.
  name: Doordash Dataexchange API
  phrasing_intents:
  - id: createReport
    intent: Request a merchant data report
    question: How do I request a report for my stores over a date range?
  - id: getReportLink
    intent: Get the download link for a report
    question: Where do I download a report I requested?
  phrasing_ops: 2
  slug: doordash-dataexchange-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Delivery API from Doordash — 12 operation(s) for delivery.
  name: Doordash Delivery API
  phrasing_intents:
  - id: DeliveryEstimatePost
    intent: Estimate delivery fee and time (Drive v1)
    question: How much would a Drive v1 delivery cost for a given order value?
  - id: DeliveryValidationPost
    intent: Validate v1 delivery details before creating
    question: Can I validate v1 delivery inputs and serviceability before creating the delivery?
  - id: DeliveryListPost
    intent: Create a delivery with the Drive v1 API
    question: How do I create a delivery with the older Drive v1 API?
  - id: DeliveryDetailGet
    intent: Get a v1 delivery by DoorDash delivery ID
    question: What are the details of a delivery by its v1 delivery id?
  - id: DeliveryDetailPatch
    intent: Change the time or address of a v1 delivery
    question: Can I change the delivery time or dropoff address on a v1 delivery?
  - id: DeliveryCancelPut
    intent: Cancel or return a v1 delivery
    question: How do I cancel or start a return for a v1 delivery?
  - id: DeliveryQuote
    intent: Quote a delivery's fee and check coverage
    question: How do I get a quote to confirm a delivery is serviceable and see the fee?
  - id: DeliveryQuoteAccept
    intent: Accept a quote to start the delivery
    question: What do I call to accept a quote and start the delivery?
  phrasing_ops: 14
  slug: doordash-delivery-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The drive-redelivery API from Doordash — 1 operation(s) for drive-redelivery.
  name: Doordash Drive Redelivery API
  phrasing_intents:
  - id: CreateRedelivery
    intent: Redeliver a completed or cancelled order
    question: Can I redeliver an order that was completed or cancelled?
  phrasing_ops: 1
  slug: doordash-drive-redelivery-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: 'The Https: API from Doordash — 2 operation(s) for https:.'
  name: 'Doordash Https: API'
  phrasing_intents:
  - id: CreateCheckoutPost
    intent: Create a checkout order session
    question: How do I start a hosted checkout by creating an order session?
  - id: GetCheckoutPage
    intent: Load the checkout page for an order session
    question: Which URL renders the checkout HTML for an order session?
  phrasing_ops: 2
  slug: doordash-https-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints to manage inventory/pricing and other item attributes specific to this store
  name: Doordash Inventory Management Endpoints API
  phrasing_intents:
  - id: batchAddStoreItem
    intent: Put a new item on sale at a store
    question: How do I make a new item available for sale at a store with a base price?
  - id: batchUpdateStoreItem
    intent: Update an item a store already sells
    question: What's the way to update price or stock of an item a store already sells?
  - id: updateItemsInBusiness
    intent: Update item prices across all business stores
    question: Can I update an item's price across every store in a business at once?
  phrasing_ops: 3
  slug: doordash-inventorymanagementendpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for item management
  name: Doordash Item Management Endpoints API
  phrasing_intents:
  - id: batchAddItems
    intent: Add new items managed by a business
    question: How do I add new items that a business sells across its stores?
  - id: batchUpdateItems
    intent: Update existing items managed by a business
    question: Can I edit details of existing business items in bulk?
  phrasing_ops: 2
  slug: doordash-itemmanagementendpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints to create jobs to support pull request flows.
  name: Doordash Job Management Endpoints API
  phrasing_intents:
  - id: createJobs
    intent: Trigger a job to pull store items
    question: Can I ask for all of a store's items to be pulled from my system?
  phrasing_ops: 1
  slug: doordash-jobmanagementendpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for JWT resources
  name: Doordash JWT API
  phrasing_intents:
  - id: CreateJWTForIntegrationId
    intent: Create a JWT for an integration
    question: Where do I get a JWT for my business, business group or store integration?
  phrasing_ops: 1
  slug: doordash-jwt-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: For Sponsored Products campaigns only.
  name: Doordash Keywords (SP) API
  phrasing_intents:
  - id: getRecommendedKeywordsForProducts
    intent: Get keyword recommendations for products
    question: Which keywords should I bid on for these products?
  - id: getRecommendedKeywordsAdGroupStatus
    intent: Get recommended keywords with ad group status
    question: Which recommended keywords are new to my ad group?
  phrasing_ops: 2
  slug: doordash-keywords-sp-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for loyalty related resources
  name: Doordash Loyalty API
  phrasing_intents:
  - id: getAccountBalance
    intent: Get a user's loyalty balance
    question: How many loyalty points does a user have?
  - id: getMemberProfile
    intent: Get a user's loyalty member profile
    question: What's in a user's loyalty member profile?
  - id: revokeUserSession
    intent: Revoke a user's loyalty session
    question: How do I log a user out of the loyalty provider?
  - id: deleteUserAccount
    intent: Delete a user's account
    question: How do I delete a user's loyalty account?
  - id: getUserSession
    intent: Get a user's loyalty session info
    question: What session info does the loyalty provider hold for a user?
  - id: GenerateStorefrontUserQrCode
    intent: Get a user's loyalty QR code
    question: Where do I get a user's loyalty QR code to show at a store?
  - id: LoyaltyRetrieveRewards
    intent: List a user's loyalty rewards at a store
    question: Which loyalty rewards can a user redeem at a store?
  - id: LoyaltyCheckIn
    intent: Check a user in at a store for points
    question: How does a user check in at a store to earn loyalty points?
  phrasing_ops: 9
  slug: doordash-loyalty-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Menu API from Doordash — 1 operation(s) for menu.
  name: Doordash Menu API
  phrasing_intents:
  - id: getAdsApiV1MenuLabels
    intent: List dish labels for interest targeting
    question: Which dish labels can I target by interest in a DoorDash ad campaign?
  phrasing_ops: 1
  slug: doordash-menu-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for updating and creating menus
  name: Doordash Menu Endpoints API
  phrasing_intents:
  - id: menuCreate
    intent: Create a menu with store hours
    question: What does it take to push a new menu with store hours?
  - id: menuUpdate
    intent: Update an existing menu and its hours
    question: Can I update an existing menu and its hours?
  phrasing_ops: 2
  slug: doordash-menu-endpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Menu Item API from Doordash — 1 operation(s) for menu item.
  name: Doordash Menu Item API
  phrasing_intents:
  - id: GetStoreMenuItem
    intent: Get one item from a store's menu
    question: What options and details does a menu item have?
  phrasing_ops: 1
  slug: doordash-menu-item-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Menu V2 API from Doordash — 1 operation(s) for menu v2.
  name: Doordash Menu V2 API
  phrasing_intents:
  - id: GetStoreMenuV2
    intent: Get a store's full menu (v2)
    question: Which call loads a store's full menu for my storefront?
  phrasing_ops: 1
  slug: doordash-menu-v2-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: To retrieve business IDs available for merchant targeting.
  name: Doordash Merchants (Retailers) API
  phrasing_intents:
  - id: getAdsApiV1Merchants
    intent: List merchant business IDs for ad targeting
    question: Which merchant business IDs can I target in a DoorDash ad campaign?
  phrasing_ops: 1
  slug: doordash-merchants-retailers-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for new verticals self-serve integration onboarding
  name: Doordash New Verticals Self Serve Integration Endpoints API
  phrasing_intents:
  - id: createManagedMerchantConnectUrl
    intent: Generate an onboarding URL for one merchant
    question: How do I generate an onboarding link for a merchant location?
  - id: submitMultiLocationOnboardingIntent
    intent: Submit onboarding for many locations at once
    question: Can I submit onboarding for many store locations in one batch?
  phrasing_ops: 2
  slug: doordash-newverticalsselfserveintegrationendpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for order resources
  name: Doordash Order API
  phrasing_intents:
  - id: CreateStorefrontOrderSessionFromExternalCartId
    intent: Create an order session from an external cart
    question: How do I create an order session from an external cart?
  - id: CreateCartFromOrderSession
    intent: Turn an order session into a cart
    question: What's the way to turn an order session into a cart for a consumer?
  - id: getOrderHistory
    intent: Get a consumer's order history
    question: What orders has a consumer placed before?
  - id: getOrderStatus
    intent: Get the status of a storefront order
    question: What's the status of a storefront order?
  phrasing_ops: 4
  slug: doordash-order-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for retrieving and confirming success of orders
  name: Doordash Order Endpoints API
  phrasing_intents:
  - id: confirmOrder
    intent: Confirm or fail an incoming order
    question: How does a merchant confirm or fail an incoming order?
  - id: adjustOrderItems
    intent: Cancel, adjust or substitute order items
    question: How do I substitute or remove items from an order?
  - id: cancelOrder
    intent: Cancel an entire order as the merchant
    question: How does a merchant cancel an entire order?
  - id: storeConfirmOrderReadyForPickup
    intent: Send an order event such as ready for pickup
    question: How do I tell DoorDash an order is ready for pickup?
  - id: returnOrder
    intent: Mark a retail order as returned
    question: How do I mark a retail order as returned?
  phrasing_ops: 5
  slug: doordash-order-endpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Product Ads API from Doordash — 1 operation(s) for product ads.
  name: Doordash Product Ads API
  phrasing_intents:
  - id: createProductAd
    intent: Add a product to an ad group as an ad
    question: How do I add a product to an ad group as a product ad?
  - id: getProductAds
    intent: List product ads
    question: Which product ads are in my campaigns?
  - id: deleteProductAd
    intent: Remove a product ad from an ad group
    question: How do I remove a product from an ad group?
  phrasing_ops: 3
  slug: doordash-product-ads-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for promotion management
  name: Doordash Promotion Management Endpoints API
  phrasing_intents:
  - id: createPromotion
    intent: Create a new promotion for a store
    question: What do I send to create a new promotion for a store?
  - id: updatePromotions
    intent: Update promotions at a store
    question: Can I change an existing store promotion's end time?
  phrasing_ops: 2
  slug: doordash-promotionmanagementendpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Refunds API from Doordash — 1 operation(s) for refunds.
  name: Doordash Refunds API
  phrasing_intents:
  - id: ProcessRefund
    intent: Request a refund for a delivery
    question: Can I request a refund for a delivery order?
  phrasing_ops: 1
  slug: doordash-refunds-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Report API from Doordash — 3 operation(s) for report.
  name: Doordash Report API
  phrasing_intents:
  - id: createReport
    intent: Create an ads performance report
    question: How do I create an ads performance report for a date range?
  - id: downloadReportRequest
    intent: Download an ads report
    question: Where do I download an ads report once it is ready?
  - id: listReports
    intent: List my ads reports
    question: Which ads reports have I created recently?
  phrasing_ops: 3
  slug: doordash-report-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: To retrieve brands and categories available for behavioral targeting.
  name: Doordash Resources API
  phrasing_intents:
  - id: searchResources
    intent: Search ad categories or brands
    question: Which categories or brands can I target in ads?
  phrasing_ops: 1
  slug: doordash-resources-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for store searches
  name: Doordash Search API
  phrasing_intents:
  - id: NearbyStoresByBusinessId
    intent: Find a business's stores near a location
    question: Which of a business's stores are near a customer's location?
  - id: NearbyStoresByBusinessGroupId
    intent: Find a business group's stores near a location
    question: Which stores in a business group are near a location?
  phrasing_ops: 2
  slug: doordash-search-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for store based operations
  name: Doordash Store Endpoints API
  phrasing_intents:
  - id: getStoreInfo
    intent: Get store summary (base store path)
    question: What summary info is held for my store location on the base store endpoint?
  - id: updateStoreStatus
    intent: Activate or deactivate a store (activation-status)
    question: How do I deactivate a store with a reason using the activation-status endpoint?
  - id: itemActivation
    intent: Stock items in or out (item activation-status)
    question: Can I mark items in or out of stock through the item activation-status webhook?
  - id: itemOptionActivation
    intent: Stock item options in or out (activation-status)
    question: Can I stock item options in or out through the item_option activation-status webhook?
  - id: getStoreMenuInfo
    intent: Get a store's menu details
    question: What menu details are held for my store?
  - id: getStoreMenu
    intent: Get a store's raw menu JSON
    question: Can I pull the raw menu JSON for a store?
  - id: getApiV1StoresByLocationIdStoreDetails
    intent: Get store summary (store_details path)
    question: Can I get my store's summary from the store_details endpoint?
  - id: putApiV1StoresByLocationIdStatus
    intent: Deactivate a store for a set duration
    question: Can I deactivate a store for a set number of hours?
  phrasing_ops: 12
  slug: doordash-store-endpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: Endpoints for managing stores
  name: Doordash Store Management Endpoints API
  phrasing_intents:
  - id: updateStore
    intent: Update a store's open and special hours
    question: Can I update a store's regular open hours?
  phrasing_ops: 1
  slug: doordash-storemanagementendpoints-api
- baseURL: https://openapi.doordash.com/drive/v2
  baseurl_source: declared
  description: The Targeting API from Doordash — 1 operation(s) for targeting.
  name: Doordash Targeting API
  phrasing_intents:
  - id: postAdsApiV1TargetingAudienceEstimate
    intent: Estimate the audience size for campaign targeting
    question: How many people would my campaign targeting reach before I launch it?
  phrasing_ops: 1
  slug: doordash-targeting-api
artifact_total: 276
asyncapis:
- description: 'DoorDash Drive sends webhook notifications for delivery status updates, enabling near-real-time information flow from DoorDash and Dashers to partner applications. Webhooks support scenarios like map '
  name: DoorDash Drive Delivery Webhooks
  slug: doordash-drive-webhooks-asyncapi
- description: DoorDash Marketplace sends webhook notifications for order events, menu processing status, delivery status updates, and store onboarding events. Each environment (Sandbox and Production) supports only
  name: DoorDash Marketplace Webhooks
  slug: doordash-marketplace-webhooks-asyncapi
- description: DoorDash Reporting API sends webhook notifications when report generation is complete and the report is ready for download. Partners configure a webhook endpoint to receive these notifications instead
  name: DoorDash Reporting Webhooks
  slug: doordash-reporting-webhooks-asyncapi
collections:
- collection_type: postman
  name: DoorDash Drive Classic Addresses API
  slug: postman-doordash-addresses-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Businesses API
  slug: postman-doordash-businesses-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Catalog API
  slug: postman-doordash-catalog-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Deliveries API
  slug: postman-doordash-deliveries-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Inventory API
  slug: postman-doordash-inventory-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Items API
  slug: postman-doordash-items-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Menus API
  slug: postman-doordash-menus-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Orders API
  slug: postman-doordash-orders-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Promotions API
  slug: postman-doordash-promotions-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Quotes API
  slug: postman-doordash-quotes-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Reports API
  slug: postman-doordash-reports-api
- collection_type: postman
  name: DoorDash Drive Classic Addresses Stores API
  slug: postman-doordash-stores-api
- collection_type: open
  name: DoorDash Drive Classic Addresses API
  slug: open-doordash-addresses-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Businesses API
  slug: open-doordash-businesses-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Catalog API
  slug: open-doordash-catalog-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Deliveries API
  slug: open-doordash-deliveries-api
- collection_type: open
  name: DoorDash Drive Classic API
  slug: open-doordash-drive-classic
- collection_type: open
  name: DoorDash Drive API
  slug: open-doordash-drive
- collection_type: open
  name: DoorDash Drive Classic Addresses Inventory API
  slug: open-doordash-inventory-api
- collection_type: open
  name: DoorDash Item Management API
  slug: open-doordash-item-management
- collection_type: open
  name: DoorDash Drive Classic Addresses Items API
  slug: open-doordash-items-api
- collection_type: open
  name: DoorDash Marketplace API
  slug: open-doordash-marketplace
- collection_type: open
  name: DoorDash Drive Classic Addresses Menus API
  slug: open-doordash-menus-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Orders API
  slug: open-doordash-orders-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Promotions API
  slug: open-doordash-promotions-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Quotes API
  slug: open-doordash-quotes-api
- collection_type: open
  name: DoorDash Reporting API
  slug: open-doordash-reporting
- collection_type: open
  name: DoorDash Drive Classic Addresses Reports API
  slug: open-doordash-reports-api
- collection_type: open
  name: DoorDash Drive Classic Addresses Stores API
  slug: open-doordash-stores-api
common:
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-ads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-ads-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-storefront-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-storefront-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-parcel-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-parcel-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-drive-refunds-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-drive-refunds-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-drive-redelivery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-drive-redelivery-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-drive-dasher-feedback-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-drive-dasher-feedback-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-external-checkout-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-external-checkout-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-marketplace-legacy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-marketplace-legacy-overlay.yaml
- group: other
  href: https://artifacts.apis.io/doordash/capabilities/doordash-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/doordash-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/doordash/overview
- group: agent
  href: https://artifacts.apis.io/doordash/agentic-access/doordash-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doordash-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/doordash/security/doordash-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/doordash-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/doordash/security/doordash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doordash-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/doordash/authentication/doordash-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doordash-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.doordash.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.doordash.com/en-US/
- group: company
  title: ''
  type: Website
  url: https://www.doordash.com/
- group: company
  title: ''
  type: Blog
  url: https://doordash.engineering/
- group: start
  title: Developer Portal sign-up and login
  type: SignUp
  url: https://developer.doordash.com/portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doordash.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doordash.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://help.doordash.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doordash
- group: build
  title: DoorDash Open Source
  type: GitHubOrganization
  url: https://github.com/doordash-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/doordash
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/@doordash/sdk
- group: build
  title: OpenAPI Go Codegen (oapi-codegen-dd)
  type: Tools
  url: https://github.com/doordash-oss/oapi-codegen-dd
- group: design
  href: https://artifacts.apis.io/doordash/json-ld/doordash-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/doordash-context.jsonld
- group: docs
  href: https://artifacts.apis.io/doordash/json-schema/doordash-delivery-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/doordash-delivery-schema.json
- group: docs
  href: https://artifacts.apis.io/doordash/json-schema/doordash-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/doordash-order-schema.json
- group: docs
  href: https://artifacts.apis.io/doordash/json-schema/doordash-menu-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/doordash-menu-schema.json
- group: docs
  href: https://artifacts.apis.io/doordash/json-schema/doordash-report-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/doordash-report-schema.json
- group: design
  href: https://artifacts.apis.io/doordash/vocabulary/doordash-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/doordash-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/doordash/rules/doordash-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/doordash-spectral-rules.yml
- group: commercial
  href: https://artifacts.apis.io/doordash/plans/doordash-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doordash-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/doordash/rate-limits/doordash-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/doordash-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/doordash/finops/doordash-finops.yml
  title: ''
  type: FinOps
  url: finops/doordash-finops.yml
- group: docs
  href: https://artifacts.apis.io/doordash/openapi/_original/doordash-drive-openapi.yml
  title: DoorDash Drive API 2.1.59 (provider-published, harvested verbatim)
  type: OpenAPI
  url: openapi/_original/doordash-drive-openapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.doordash.com/en-US/api/drive
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.doordash.com/en-US/docs/drive/tutorials/get_started/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.doordash.com/en-US/docs/drive/overview/pricing_payment
- group: operate
  title: ''
  type: StatusPage
  url: https://www.doordashstatus.com
- group: design
  href: https://artifacts.apis.io/doordash/lifecycle/doordash-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/doordash-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/doordash/changelog/doordash-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/doordash-changelog.yml
- group: operate
  title: Reporting API release notes
  type: ChangeLog
  url: https://developer.doordash.com/en-US/docs/reporting/overview/release_notes
- group: design
  href: https://artifacts.apis.io/doordash/conventions/doordash-conventions.yml
  title: ''
  type: Conventions
  url: conventions/doordash-conventions.yml
- group: design
  href: https://artifacts.apis.io/doordash/conventions/doordash-conventions.yml
  title: Idempotency and reversibility rules (external_delivery_id, cancel-before-assignment)
  type: Idempotency
  url: conventions/doordash-conventions.yml
- group: design
  href: https://artifacts.apis.io/doordash/errors/doordash-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doordash-problem-types.yml
- group: design
  href: https://artifacts.apis.io/doordash/conformance/doordash-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doordash-conformance.yml
- group: auth
  title: DoorDash Trust Center (SOC 2, PCI DSS)
  type: Compliance
  url: https://trust.doordash.com/
- group: auth
  title: DoorDash Bug Bounty Program
  type: Security
  url: https://hackerone.com/doordash
- group: auth
  href: https://artifacts.apis.io/doordash/security/doordash-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doordash-vulnerability-disclosure.yml
- group: build
  href: https://artifacts.apis.io/doordash/packages/doordash-packages.yml
  title: ''
  type: Packages
  url: packages/doordash-packages.yml
- group: start
  href: https://artifacts.apis.io/doordash/sandbox/doordash-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/doordash-sandbox.yml
- group: design
  href: https://artifacts.apis.io/doordash/components/doordash-components.yml
  title: ''
  type: Components
  url: components/doordash-components.yml
- group: design
  href: https://artifacts.apis.io/doordash/data-model/doordash-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doordash-data-model.yml
- group: agent
  href: https://artifacts.apis.io/doordash/mcp/doordash-mcp.yml
  title: MCP candidate - DoorDash publishes no MCP server
  type: MCPServer
  url: mcp/doordash-mcp.yml
- group: agent
  href: https://artifacts.apis.io/doordash/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/doordash/llms/doordash-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doordash-llms.txt
- group: other
  href: https://artifacts.apis.io/doordash/overlays/doordash-drive-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doordash-drive-overlay.yaml
- group: design
  title: Drive webhook event reference
  type: Webhooks
  url: https://developer.doordash.com/en-US/docs/drive/reference/webhooks
- group: docs
  href: https://artifacts.apis.io/doordash/asyncapi/doordash-drive-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/doordash-drive-webhooks-asyncapi.yml
created: '2026-05-04'
description: DoorDash is an on-demand local commerce platform whose developer program exposes its logistics and marketplace network through thirteen publicly documented REST APIs. Drive, Drive (classic) and Parcel let businesses request deliveries fulfilled by DoorDash's Dasher fleet, with Refunds, Redelivery and Dasher Feedback attached to that surface. Marketplace, Marketplace (legacy) and Item Management let merchants and retailers receive orders and synchronize menus, catalogs, inventory and promotions, while Storefront powers white-label online ordering, Reporting delivers financial and operational data exchange, and the Ads API sells sponsored placement on the marketplace. Every API authenticates with a short-lived HS256 JSON Web Token the caller signs itself, and DoorDash serves each OpenAPI definition as plain YAML from developer.doordash.com.
examples:
- key_count: 1
  name: Doordash Accept Quote Request Example
  slug: doordash-accept-quote-request-example
- key_count: 6
  name: Doordash Address Suggestion Example
  slug: doordash-address-suggestion-example
- key_count: 3
  name: Doordash Business Example
  slug: doordash-business-example
- key_count: 3
  name: Doordash Business Request Example
  slug: doordash-business-request-example
- key_count: 2
  name: Doordash Cancelled Item Example
  slug: doordash-cancelled-item-example
- key_count: 11
  name: Doordash Catalog Item Example
  slug: doordash-catalog-item-example
- key_count: 1
  name: Doordash Catalog Items Request Example
  slug: doordash-catalog-items-request-example
- key_count: 3
  name: Doordash Catalog Items Response Example
  slug: doordash-catalog-items-response-example
- key_count: 2
  name: Doordash Checkout Audit Signal Example
  slug: doordash-checkout-audit-signal-example
- key_count: 16
  name: Doordash Classic Delivery Example
  slug: doordash-classic-delivery-example
- key_count: 18
  name: Doordash Classic Delivery Request Example
  slug: doordash-classic-delivery-request-example
- key_count: 3
  name: Doordash Classic Delivery Update Request Example
  slug: doordash-classic-delivery-update-request-example
- key_count: 3
  name: Doordash Customer Example
  slug: doordash-customer-example
- key_count: 29
  name: Doordash Delivery Example
  slug: doordash-delivery-example
- key_count: 5
  name: Doordash Delivery Item Example
  slug: doordash-delivery-item-example
- key_count: 21
  name: Doordash Delivery Request Example
  slug: doordash-delivery-request-example
- key_count: 3
  name: Doordash Delivery Update Request Example
  slug: doordash-delivery-update-request-example
- key_count: 27
  name: Doordash Delivery Webhook Payload Example
  slug: doordash-delivery-webhook-payload-example
- key_count: 5
  name: Doordash Estimate Example
  slug: doordash-estimate-example
- key_count: 4
  name: Doordash Estimate Request Example
  slug: doordash-estimate-request-example
- key_count: 4
  name: Doordash Item Option Example
  slug: doordash-item-option-example
- key_count: 1
  name: Doordash Item Status Update Example
  slug: doordash-item-status-update-example
- key_count: 2
  name: Doordash Location Example
  slug: doordash-location-example
- key_count: 8
  name: Doordash Marketplace Delivery Webhook Payload Example
  slug: doordash-marketplace-delivery-webhook-payload-example
- key_count: 5
  name: Doordash Menu Category Example
  slug: doordash-menu-category-example
- key_count: 3
  name: Doordash Menu Details Example
  slug: doordash-menu-details-example
- key_count: 8
  name: Doordash Menu Item Example
  slug: doordash-menu-item-example
- key_count: 4
  name: Doordash Menu Option Example
  slug: doordash-menu-option-example
- key_count: 2
  name: Doordash Menu Request Example
  slug: doordash-menu-request-example
- key_count: 2
  name: Doordash Menu Response Example
  slug: doordash-menu-response-example
- key_count: 6
  name: Doordash Menu Webhook Payload Example
  slug: doordash-menu-webhook-payload-example
- key_count: 5
  name: Doordash Onboarding Webhook Payload Example
  slug: doordash-onboarding-webhook-payload-example
- key_count: 5
  name: Doordash Option Group Example
  slug: doordash-option-group-example
- key_count: 14
  name: Doordash Order Example
  slug: doordash-order-example
- key_count: 6
  name: Doordash Order Item Example
  slug: doordash-order-item-example
- key_count: 4
  name: Doordash Order Item Option Example
  slug: doordash-order-item-option-example
- key_count: 3
  name: Doordash Order Update Example
  slug: doordash-order-update-example
- key_count: 13
  name: Doordash Order Webhook Payload Example
  slug: doordash-order-webhook-payload-example
- key_count: 5
  name: Doordash Promotion Example
  slug: doordash-promotion-example
- key_count: 1
  name: Doordash Promotions Request Example
  slug: doordash-promotions-request-example
- key_count: 3
  name: Doordash Promotions Response Example
  slug: doordash-promotions-response-example
- key_count: 6
  name: Doordash Quote Example
  slug: doordash-quote-example
- key_count: 10
  name: Doordash Quote Request Example
  slug: doordash-quote-request-example
- key_count: 6
  name: Doordash Report Link Response Example
  slug: doordash-report-link-response-example
- key_count: 7
  name: Doordash Report Ready Payload Example
  slug: doordash-report-ready-payload-example
- key_count: 4
  name: Doordash Report Request Example
  slug: doordash-report-request-example
- key_count: 2
  name: Doordash Report Request Response Example
  slug: doordash-report-request-response-example
- key_count: 6
  name: Doordash Store Details Example
  slug: doordash-store-details-example
- key_count: 5
  name: Doordash Store Example
  slug: doordash-store-example
- key_count: 6
  name: Doordash Store Item Example
  slug: doordash-store-item-example
- key_count: 1
  name: Doordash Store Items Request Example
  slug: doordash-store-items-request-example
- key_count: 3
  name: Doordash Store Items Response Example
  slug: doordash-store-items-response-example
- key_count: 4
  name: Doordash Store Request Example
  slug: doordash-store-request-example
- key_count: 2
  name: Doordash Store Status Update Example
  slug: doordash-store-status-update-example
- key_count: 4
  name: Doordash Substitution Example
  slug: doordash-substitution-example
finops:
- has_sources: true
  method: derived
  name: Doordash Finops
  primary_unit: delivery
  service_category: ''
  slug: doordash-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doordash.png
json_schemas:
- name: AcceptQuoteRequest
  property_count: 1
  slug: doordash-accept-quote-request
- name: AddressSuggestion
  property_count: 6
  slug: doordash-address-suggestion
- name: BusinessRequest
  property_count: 3
  slug: doordash-business-request
- name: Business
  property_count: 3
  slug: doordash-business
- name: CancelledItem
  property_count: 2
  slug: doordash-cancelled-item
- name: CatalogItem
  property_count: 11
  slug: doordash-catalog-item
- name: CatalogItemsRequest
  property_count: 1
  slug: doordash-catalog-items-request
- name: CatalogItemsResponse
  property_count: 3
  slug: doordash-catalog-items-response
- name: CheckoutAuditSignal
  property_count: 2
  slug: doordash-checkout-audit-signal
- name: ClassicDeliveryRequest
  property_count: 18
  slug: doordash-classic-delivery-request
- name: ClassicDelivery
  property_count: 16
  slug: doordash-classic-delivery
- name: ClassicDeliveryUpdateRequest
  property_count: 3
  slug: doordash-classic-delivery-update-request
- name: Customer
  property_count: 3
  slug: doordash-customer
- name: DeliveryItem
  property_count: 5
  slug: doordash-delivery-item
- name: DeliveryRequest
  property_count: 21
  slug: doordash-delivery-request
- name: Delivery
  property_count: 29
  slug: doordash-delivery
- name: DeliveryUpdateRequest
  property_count: 3
  slug: doordash-delivery-update-request
- name: DeliveryWebhookPayload
  property_count: 27
  slug: doordash-delivery-webhook-payload
- name: Error
  property_count: 3
  slug: doordash-error
- name: EstimateRequest
  property_count: 4
  slug: doordash-estimate-request
- name: Estimate
  property_count: 5
  slug: doordash-estimate
- name: ItemOption
  property_count: 4
  slug: doordash-item-option
- name: ItemStatusUpdate
  property_count: 1
  slug: doordash-item-status-update
- name: ItemError
  property_count: 3
  slug: doordash-itemerror
- name: Location
  property_count: 2
  slug: doordash-location
- name: MarketplaceDeliveryWebhookPayload
  property_count: 8
  slug: doordash-marketplace-delivery-webhook-payload
- name: MenuCategory
  property_count: 5
  slug: doordash-menu-category
- name: MenuDetails
  property_count: 3
  slug: doordash-menu-details
- name: MenuItem
  property_count: 8
  slug: doordash-menu-item
- name: MenuOption
  property_count: 4
  slug: doordash-menu-option
- name: MenuRequest
  property_count: 2
  slug: doordash-menu-request
- name: MenuResponse
  property_count: 2
  slug: doordash-menu-response
- name: DoorDash Menu
  property_count: 4
  slug: doordash-menu
- name: MenuWebhookPayload
  property_count: 6
  slug: doordash-menu-webhook-payload
- name: OnboardingWebhookPayload
  property_count: 5
  slug: doordash-onboarding-webhook-payload
- name: OptionGroup
  property_count: 5
  slug: doordash-option-group
- name: OrderItemOption
  property_count: 4
  slug: doordash-order-item-option
- name: OrderItem
  property_count: 6
  slug: doordash-order-item
- name: Order
  property_count: 14
  slug: doordash-order
- name: OrderUpdate
  property_count: 3
  slug: doordash-order-update
- name: OrderWebhookPayload
  property_count: 13
  slug: doordash-order-webhook-payload
- name: Promotion
  property_count: 5
  slug: doordash-promotion
- name: PromotionsRequest
  property_count: 1
  slug: doordash-promotions-request
- name: PromotionsResponse
  property_count: 3
  slug: doordash-promotions-response
- name: QuoteRequest
  property_count: 10
  slug: doordash-quote-request
- name: Quote
  property_count: 6
  slug: doordash-quote
- name: ReportLinkResponse
  property_count: 6
  slug: doordash-report-link-response
- name: ReportReadyPayload
  property_count: 7
  slug: doordash-report-ready-payload
- name: ReportRequestResponse
  property_count: 2
  slug: doordash-report-request-response
- name: ReportRequest
  property_count: 4
  slug: doordash-report-request
- name: DoorDash Report
  property_count: 9
  slug: doordash-report
- name: StoreDetails
  property_count: 6
  slug: doordash-store-details
- name: StoreItem
  property_count: 6
  slug: doordash-store-item
- name: StoreItemsRequest
  property_count: 1
  slug: doordash-store-items-request
- name: StoreItemsResponse
  property_count: 3
  slug: doordash-store-items-response
- name: StoreRequest
  property_count: 4
  slug: doordash-store-request
- name: Store
  property_count: 5
  slug: doordash-store
- name: StoreStatusUpdate
  property_count: 2
  slug: doordash-store-status-update
- name: Substitution
  property_count: 4
  slug: doordash-substitution
json_structures:
- name: Doordash Accept Quote Request Structure
  property_count: 1
  slug: doordash-accept-quote-request-structure
- name: Doordash Address Suggestion Structure
  property_count: 6
  slug: doordash-address-suggestion-structure
- name: Doordash Business Request Structure
  property_count: 3
  slug: doordash-business-request-structure
- name: Doordash Business Structure
  property_count: 3
  slug: doordash-business-structure
- name: Doordash Cancelled Item Structure
  property_count: 2
  slug: doordash-cancelled-item-structure
- name: Doordash Catalog Item Structure
  property_count: 11
  slug: doordash-catalog-item-structure
- name: Doordash Catalog Items Request Structure
  property_count: 1
  slug: doordash-catalog-items-request-structure
- name: Doordash Catalog Items Response Structure
  property_count: 3
  slug: doordash-catalog-items-response-structure
- name: Doordash Checkout Audit Signal Structure
  property_count: 2
  slug: doordash-checkout-audit-signal-structure
- name: Doordash Classic Delivery Request Structure
  property_count: 18
  slug: doordash-classic-delivery-request-structure
- name: Doordash Classic Delivery Structure
  property_count: 16
  slug: doordash-classic-delivery-structure
- name: Doordash Classic Delivery Update Request Structure
  property_count: 3
  slug: doordash-classic-delivery-update-request-structure
- name: Doordash Customer Structure
  property_count: 3
  slug: doordash-customer-structure
- name: Doordash Delivery Item Structure
  property_count: 5
  slug: doordash-delivery-item-structure
- name: Doordash Delivery Request Structure
  property_count: 21
  slug: doordash-delivery-request-structure
- name: Doordash Delivery Structure
  property_count: 29
  slug: doordash-delivery-structure
- name: Doordash Delivery Update Request Structure
  property_count: 3
  slug: doordash-delivery-update-request-structure
- name: Doordash Delivery Webhook Payload Structure
  property_count: 27
  slug: doordash-delivery-webhook-payload-structure
- name: Doordash Estimate Request Structure
  property_count: 4
  slug: doordash-estimate-request-structure
- name: Doordash Estimate Structure
  property_count: 5
  slug: doordash-estimate-structure
- name: Doordash Item Option Structure
  property_count: 4
  slug: doordash-item-option-structure
- name: Doordash Item Status Update Structure
  property_count: 1
  slug: doordash-item-status-update-structure
- name: Doordash Location Structure
  property_count: 2
  slug: doordash-location-structure
- name: Doordash Marketplace Delivery Webhook Payload Structure
  property_count: 8
  slug: doordash-marketplace-delivery-webhook-payload-structure
- name: Doordash Menu Category Structure
  property_count: 5
  slug: doordash-menu-category-structure
- name: Doordash Menu Details Structure
  property_count: 3
  slug: doordash-menu-details-structure
- name: Doordash Menu Item Structure
  property_count: 8
  slug: doordash-menu-item-structure
- name: Doordash Menu Option Structure
  property_count: 4
  slug: doordash-menu-option-structure
- name: Doordash Menu Request Structure
  property_count: 2
  slug: doordash-menu-request-structure
- name: Doordash Menu Response Structure
  property_count: 2
  slug: doordash-menu-response-structure
- name: Doordash Menu Webhook Payload Structure
  property_count: 6
  slug: doordash-menu-webhook-payload-structure
- name: Doordash Onboarding Webhook Payload Structure
  property_count: 5
  slug: doordash-onboarding-webhook-payload-structure
- name: Doordash Option Group Structure
  property_count: 5
  slug: doordash-option-group-structure
- name: Doordash Order Item Option Structure
  property_count: 4
  slug: doordash-order-item-option-structure
- name: Doordash Order Item Structure
  property_count: 6
  slug: doordash-order-item-structure
- name: Doordash Order Structure
  property_count: 14
  slug: doordash-order-structure
- name: Doordash Order Update Structure
  property_count: 3
  slug: doordash-order-update-structure
- name: Doordash Order Webhook Payload Structure
  property_count: 13
  slug: doordash-order-webhook-payload-structure
- name: Doordash Promotion Structure
  property_count: 5
  slug: doordash-promotion-structure
- name: Doordash Promotions Request Structure
  property_count: 1
  slug: doordash-promotions-request-structure
- name: Doordash Promotions Response Structure
  property_count: 3
  slug: doordash-promotions-response-structure
- name: Doordash Quote Request Structure
  property_count: 10
  slug: doordash-quote-request-structure
- name: Doordash Quote Structure
  property_count: 6
  slug: doordash-quote-structure
- name: Doordash Report Link Response Structure
  property_count: 6
  slug: doordash-report-link-response-structure
- name: Doordash Report Ready Payload Structure
  property_count: 7
  slug: doordash-report-ready-payload-structure
- name: Doordash Report Request Response Structure
  property_count: 2
  slug: doordash-report-request-response-structure
- name: Doordash Report Request Structure
  property_count: 4
  slug: doordash-report-request-structure
- name: Doordash Store Details Structure
  property_count: 6
  slug: doordash-store-details-structure
- name: Doordash Store Item Structure
  property_count: 6
  slug: doordash-store-item-structure
- name: Doordash Store Items Request Structure
  property_count: 1
  slug: doordash-store-items-request-structure
- name: Doordash Store Items Response Structure
  property_count: 3
  slug: doordash-store-items-response-structure
- name: Doordash Store Request Structure
  property_count: 4
  slug: doordash-store-request-structure
- name: Doordash Store Status Update Structure
  property_count: 2
  slug: doordash-store-status-update-structure
- name: Doordash Store Structure
  property_count: 5
  slug: doordash-store-structure
- name: Doordash Substitution Structure
  property_count: 4
  slug: doordash-substitution-structure
jsonld:
- class_count: 0
  name: Doordash Context
  property_count: 7
  slug: doordash-context
- class_count: 13
  name: Doordash Drive Classic Context
  property_count: 31
  slug: doordash-drive-classic-context
- class_count: 14
  name: Doordash Drive Context
  property_count: 47
  slug: doordash-drive-context
- class_count: 3
  name: Doordash Drive Webhooks Context
  property_count: 25
  slug: doordash-drive-webhooks-context
- class_count: 11
  name: Doordash Item Management Context
  property_count: 23
  slug: doordash-item-management-context
- class_count: 20
  name: Doordash Marketplace Context
  property_count: 38
  slug: doordash-marketplace-context
- class_count: 7
  name: Doordash Marketplace Webhooks Context
  property_count: 26
  slug: doordash-marketplace-webhooks-context
- class_count: 4
  name: Doordash Reporting Context
  property_count: 8
  slug: doordash-reporting-context
- class_count: 2
  name: Doordash Reporting Webhooks Context
  property_count: 6
  slug: doordash-reporting-webhooks-context
layout: provider
mcp_servers:
- description: DoorDash publishes NO Model Context Protocol server. Nothing on developer.doordash.com mentions MCP (415 sitemap URLs checked, zero matches), no /mcp endpoint exists on openapi.doordash.com, and every
  name: MCP candidate - DoorDash publishes no MCP server
  slug: mcp-candidate---doordash-publishes-no-mcp-server
modified: '2026-09-17'
name: Doordash
nav: Providers
network: true
overview: 'Doordash publishes 49 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Businesses API, Catalog API, and 46 more. Tagged areas include Delivery, Logistics, Last Mile Delivery, On-Demand, and Food Delivery.


  The Doordash catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 9 JSON-LD contexts, and 3 Spectral governance rulesets.


  Doordash''s developer surface includes authentication, documentation, engineering blog, signup flow, support, tooling, API reference, and 55 more developer resources.'
plans:
- name: Doordash Plans Pricing
  plan_count: 3
  slug: doordash-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Doordash Rate Limits
  slug: doordash-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Doordash — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: doordash-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Doordash — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: doordash-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Doordash API Rules
  rule_count: 42
  severity_counts:
    error: 7
    hint: 0
    info: 8
    warn: 27
  slug: doordash-spectral-rules
score:
  band: exemplar
  composite: 77.8
  coverage:
    artifact_dirs: 37
    catalog_earned: 83.0
    catalog_earned_first_party: 20.0
    catalog_gap: 32.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 69.1
    developer_ergonomics: 74.4
    discoverability: 71.4
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 77.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 98.0
      derived: 0
      marker_coverage: 0.0
      total: 49
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/doordash/doordash-2026-06-20T180204.png
security:
- kind: authentication
  name: Doordash Authentication
  slug: doordash-authentication
  summary_line: http/apiKey · 5 schemes
- kind: domain-security
  name: Doordash Domain Security
  slug: doordash-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doordash Vulnerability Disclosure
  slug: doordash-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Doordash Trust Center
  slug: doordash-trust-center
  summary_line: SOC 2, PCI DSS
skill_count: 5
skills:
- name: doordash-accept-and-fulfil-a-marketplace-order
  slug: doordash-accept-and-fulfil-a-marketplace-order
- name: doordash-create-and-track-a-delivery
  slug: doordash-create-and-track-a-delivery
- name: doordash-onboard-a-business-and-store
  slug: doordash-onboard-a-business-and-store
- name: doordash-request-and-download-a-report
  slug: doordash-request-and-download-a-report
- name: doordash-sync-a-catalog-and-availability
  slug: doordash-sync-a-catalog-and-availability
slug: doordash
tags:
- Delivery
- Logistics
- Last Mile Delivery
- On-Demand
- Food Delivery
- Local Commerce
- Marketplace
- Restaurant
- Grocery
- Retail
- Fulfillment
- Webhook
website: https://www.doordash.com/
---
