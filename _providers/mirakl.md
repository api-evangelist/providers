---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 126
  human_in_the_loop: 0
  name: Mirakl Agentic Access
  operation_count: 352
  slug: mirakl-agentic-access
  summary_line: 352 operations · 126 acting
api_count: 14
apis:
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Carriers API from Mirakl — 1 operation(s) for carriers.
  name: Mirakl Carriers API
  phrasing_intents:
  - id: upsertCarriers
    intent: Sync a channel's allowed carriers
    question: How do I share my channel's allowed carrier list with Mirakl Connect?
  phrasing_ops: 1
  slug: mirakl-carriers-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Catalog Configuration API from Mirakl — 1 operation(s) for catalog configuration.
  name: Mirakl Catalog Configuration API
  phrasing_intents:
  - id: configureChannelCatalog
    intent: Configure catalog capabilities for a channel
    question: How do I configure which catalog capabilities a sales channel uses?
  phrasing_ops: 1
  slug: mirakl-catalog-configuration-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Incidents API from Mirakl — 1 operation(s) for incidents.
  name: Mirakl Incidents API
  phrasing_intents:
  - id: OR64
    intent: Resolve an incident on an order line
    question: How do I mark an incident on an order line as resolved?
  phrasing_ops: 1
  slug: mirakl-incidents-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Invoicing and Accounting API from Mirakl — 11 operation(s) for invoicing and accounting.
  name: Mirakl Invoicing and Accounting API
  phrasing_intents:
  - id: DR73
    intent: Download accounting documents
    question: How do I download invoices or credit notes from a document request?
  - id: IV01
    intent: List invoices and credit notes
    question: Which invoices and credit notes were issued in a date range?
  - id: SBC11
    intent: List seller billing cycles
    question: What billing cycles have been run for sellers, and were they paid out?
  - id: DR11
    intent: List accounting document requests
    question: Which accounting document requests are pending issuance?
  - id: DR12
    intent: List a document request's lines
    question: What lines make up a specific accounting document request?
  - id: DR74
    intent: Upload accounting documents
    question: How do I upload the invoices I issued for document requests?
  - id: IV02
    intent: Download one invoice or credit note
    question: How do I get the PDF of a specific marketplace invoice?
  - id: TL02
    intent: List seller transaction lines
    question: What transactions make up a seller's payout?
  phrasing_ops: 11
  slug: mirakl-invoicing-and-accounting-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Messages API from Mirakl — 9 operation(s) for messages.
  name: Mirakl Messages API
  phrasing_intents:
  - id: M01
    intent: List order and offer messages (deprecated)
    question: Can I still list messages on orders and offers with the old messages endpoint?
  - id: M10
    intent: Get an inbox thread
    question: How do I read every message in a conversation thread?
  - id: M11
    intent: List inbox threads
    question: Which message threads have been updated since yesterday?
  - id: M14
    intent: Start a thread with the operator
    question: How can a seller open a conversation with the marketplace operator?
  - id: M12
    intent: Reply to a thread
    question: How do I reply in an existing message thread?
  - id: M13
    intent: Download a thread attachment
    question: How do I download a file someone attached in a message thread?
  - id: OR42
    intent: Post a message on an order (deprecated)
    question: Can I still post a message on an order with the old order-messages endpoint?
  - id: OR43
    intent: Start a thread on a product order
    question: How do I open a conversation about a product order?
  phrasing_ops: 10
  slug: mirakl-messages-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Multiple shipments API from Mirakl — 7 operation(s) for multiple shipments.
  name: Mirakl Multiple shipments API
  phrasing_intents:
  - id: ST01
    intent: Create shipments
    question: How do I split an order into several shipments?
  - id: ST11
    intent: List shipments
    question: How do I list the shipments for an order?
  - id: ST07
    intent: Update the ship-from origin of shipments
    question: How do I change the shipping origin on existing shipments?
  - id: ST06
    intent: Delete shipments
    question: Can I delete shipments I created by mistake?
  - id: ST12
    intent: List items still to ship
    question: Which order items still need to be shipped?
  - id: ST23
    intent: Set carrier tracking on shipments
    question: How do I add tracking numbers to multiple shipments at once?
  - id: ST24
    intent: Mark shipments as shipped
    question: How do I confirm that several shipments have left the warehouse?
  - id: ST26
    intent: Mark shipments ready for pickup
    question: How do I tell the customer their shipment is ready to collect?
  phrasing_ops: 9
  slug: mirakl-multiple-shipments-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Offers API from Mirakl — 16 operation(s) for offers.
  name: Mirakl Offers API
  phrasing_intents:
  - id: OF22
    intent: Get an offer's details
    question: How do I look up the details of a single offer?
  - id: OF26
    intent: Get available stock for an offer
    question: How much stock is left on a given offer?
  - id: OF51
    intent: Download changed offers as CSV (deprecated)
    question: Can I still pull a synchronous CSV of offers changed since my last request?
  - id: OF52
    intent: Start an asynchronous offer export
    question: What's the recommended way to export a large offer catalogue as CSV or JSON?
  - id: OF53
    intent: Check an offer export's status
    question: Is my asynchronous offer export finished yet?
  - id: OF54
    intent: Download an offer export file chunk
    question: How do I fetch each chunk of a completed offer export?
  - id: P11
    intent: List offers for given products
    question: Which sellers have offers on a given product and at what price?
  - id: OF01
    intent: Import an offer file
    question: How do I bulk create, update or delete offers by uploading a file?
  phrasing_ops: 19
  slug: mirakl-offers-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Orders API from Mirakl — 34 operation(s) for orders.
  name: Mirakl Orders API
  phrasing_intents:
  - id: deleteOrderDocument
    intent: Delete a channel order document from Connect
    question: Can I remove a document I previously pushed to Mirakl Connect for a channel order?
  - id: updateActionStatus
    intent: Report the final outcome of an async order action
    question: How do I tell Mirakl Connect that an asynchronous command event action succeeded or failed?
  - id: updateAnonymizeAfterDate
    intent: Set when Connect should anonymize orders
    question: How do I tell Mirakl Connect after which date my orders should be anonymized?
  - id: uploadOrderDocument
    intent: Upload a document to a channel order in Connect
    question: How do I attach a document to a channel order using its channel order ID in Mirakl Connect?
  - id: upsertOrders
    intent: Push channel orders into Mirakl Connect
    question: How do I synchronize orders from my sales channel into Mirakl Connect?
  - id: acceptOrderLines
    intent: Accept or refuse Connect order lines (original)
    question: Which endpoint do I use to accept or refuse Connect order lines synchronously, the original non-v2 one?
  - id: listOrders
    intent: List Mirakl Connect orders (original version)
    question: How do I pull Connect orders updated since my last sync using the original orders list?
  - id: v2-acceptOrderLines
    intent: Accept or refuse Connect order lines (v2)
    question: How do I accept or refuse Connect order lines with the v2 asynchronous accept endpoint?
  phrasing_ops: 47
  slug: mirakl-orders-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Picklists API from Mirakl — 1 operation(s) for picklists.
  name: Mirakl Picklists API
  phrasing_intents:
  - id: PL11
    intent: List picklists
    question: Which picklists do I have for today's pickups?
  phrasing_ops: 1
  slug: mirakl-picklists-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Platform Settings API from Mirakl — 19 operation(s) for platform settings.
  name: Mirakl Platform Settings API
  phrasing_intents:
  - id: AF01
    intent: List the platform's custom fields
    question: Which custom fields has the operator defined on the marketplace?
  - id: CH11
    intent: List enabled sales channels
    question: Which sales channels are enabled on my Mirakl marketplace?
  - id: CUR01
    intent: List activated currencies
    question: Which currencies are activated on the marketplace platform?
  - id: DO01
    intent: List document types
    question: What kinds of documents can be attached to orders or shops on the marketplace?
  - id: L01
    intent: List platform locales
    question: Which locales and languages does the marketplace support?
  - id: PC01
    intent: Get platform modules and features
    question: Which modules and major features were activated when the platform was set up?
  - id: V01
    intent: Check the platform is up
    question: Is the Mirakl platform up right now?
  - id: OF61
    intent: List offer conditions
    question: What offer conditions like new or refurbished can sellers choose from?
  phrasing_ops: 20
  slug: mirakl-platform-settings-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Product Feedback API from Mirakl — 1 operation(s) for product feedback.
  name: Mirakl Product Feedback API
  phrasing_intents:
  - id: updateStoreCatalogItems
    intent: Update a store's catalog items on a channel
    question: How do I tell Mirakl Connect which products a store sells on a channel?
  phrasing_ops: 1
  slug: mirakl-product-feedback-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Products API from Mirakl — 11 operation(s) for products.
  name: Mirakl Products API
  phrasing_intents:
  - id: CM11
    intent: Export source product data sheet statuses
    question: How do I get a delta of product data sheet statuses changed since my last sync?
  - id: H11
    intent: List catalog categories in a hierarchy
    question: What are the child categories under a given catalog category?
  - id: P41
    intent: Import a product file
    question: How do I upload a product catalog file to the marketplace?
  - id: P51
    intent: List product import statuses
    question: How do I see the status of all my product imports?
  - id: P42
    intent: Get the status of one product import
    question: Has my product import finished processing?
  - id: P44
    intent: Download the non-integrated products report
    question: Which products from my import were not integrated, and why?
  - id: P45
    intent: Download the added products report
    question: Which products were successfully added by my import?
  - id: P46
    intent: Download a product import in operator format
    question: Can I see my product file after it was converted into the operator format?
  phrasing_ops: 12
  slug: mirakl-products-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Promotions API from Mirakl — 2 operation(s) for promotions.
  name: Mirakl Promotions API
  phrasing_intents:
  - id: PR01
    intent: List promotions
    question: Which promotions are running on the marketplace right now?
  - id: PR03
    intent: Create a promotion
    question: How do I set up a new promotion for my shop?
  - id: PR04
    intent: Update a promotion
    question: How do I change the dates or reward of an existing promotion?
  phrasing_ops: 3
  slug: mirakl-promotions-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Returns API from Mirakl — 8 operation(s) for returns.
  name: Mirakl Returns API
  phrasing_intents:
  - id: upsertReturns
    intent: Sync returns into Mirakl Connect
    question: How do I push returns from my sales channel into Mirakl Connect?
  - id: v2-acceptReturn
    intent: Accept or refuse a Connect return
    question: Can I approve a return request that's still waiting in REQUEST_INITIATED from Connect?
  - id: v2-acknowledgeReturnReception
    intent: Mark a Connect return as received
    question: How do I confirm I physically got the item back for a Connect return?
  - id: v2-closeReturn
    intent: Close a Connect return
    question: When the refund and checks are done, how do I close a return in Connect?
  - id: v2-listReturns
    intent: List Mirakl Connect returns
    question: Which Connect returns changed since my last sync?
  - id: v2-updateReturnTrackingInformation
    intent: Update a Connect return's tracking
    question: How do I add a return shipping tracking number to a Connect return?
  - id: RT01
    intent: Create marketplace returns
    question: How do I open new returns for order lines on the marketplace?
  - id: RT11
    intent: List marketplace returns
    question: Which returns are open on the marketplace right now?
  phrasing_ops: 17
  slug: mirakl-returns-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Services API from Mirakl — 5 operation(s) for services.
  name: Mirakl Services API
  phrasing_intents:
  - id: SL01
    intent: Create a service location
    question: How do I add a new place where customers can book my services?
  - id: SL12
    intent: List service locations
    question: Where are the locations my shop offers services from?
  - id: SL06
    intent: Delete a service location
    question: How do I remove a location my shop no longer uses?
  - id: SM11
    intent: List service models
    question: What service models can I base a new service on?
  - id: SOF11
    intent: List services
    question: What services is my shop currently offering?
  - id: SOF25
    intent: Create a service
    question: How do I publish a new service offering on the marketplace?
  - id: SOF26
    intent: Update a service
    question: How do I change the price or description of an existing service?
  - id: SOF27
    intent: Delete a service
    question: How do I remove a service from my shop?
  phrasing_ops: 8
  slug: mirakl-services-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Store API from Mirakl — 1 operation(s) for store.
  name: Mirakl Store API
  phrasing_intents:
  - id: SELLER_ACCOUNT_STORE_CREATE
    intent: Create stores for a user
    question: How does a connector create stores and link them to a seller user?
  - id: SELLER_ACCOUNT_STORE_UPDATE
    intent: Update a channel store
    question: How do I rename or suspend a store on a channel?
  phrasing_ops: 2
  slug: mirakl-store-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Stores API from Mirakl — 5 operation(s) for stores.
  name: Mirakl Stores API
  phrasing_intents:
  - id: A01
    intent: Get shop account information
    question: How do I see my shop's account details on the marketplace?
  - id: A02
    intent: Update shop account information
    question: How do I change my shop name, email or return policy?
  - id: A21
    intent: Get shop statistics
    question: How is my shop performing over recent periods?
  - id: S30
    intent: List a shop's business documents
    question: Which business documents has my shop uploaded?
  - id: S32
    intent: Upload business documents for a shop
    question: How do I upload business documents like ID or registration papers for my shop?
  - id: S31
    intent: Download shop business documents
    question: How do I download the business documents for one or more shops?
  - id: S33
    intent: Delete a shop business document
    question: Can I remove a business document from my shop?
  phrasing_ops: 7
  slug: mirakl-stores-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Taxonomy API from Mirakl — 2 operation(s) for taxonomy.
  name: Mirakl Taxonomy API
  phrasing_intents:
  - id: createTaxonomyRule
    intent: Create taxonomy rules for a channel
    question: How do I define taxonomy rules for a sales channel in Mirakl Connect?
  - id: upsertProductType
    intent: Create or replace a channel product type
    question: How do I create a product type with its attributes for a channel?
  phrasing_ops: 2
  slug: mirakl-taxonomy-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Users API from Mirakl — 1 operation(s) for users.
  name: Mirakl Users API
  phrasing_intents:
  - id: RO02
    intent: List shop roles
    question: What user roles are available for a shop?
  phrasing_ops: 1
  slug: mirakl-users-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Catalog API from Mirakl — 1 operation(s) for catalog.
  name: Mirakl Catalog API
  phrasing_intents:
  - id: deleteProducts
    intent: Delete products from the Connect catalog
    question: How do I remove products from my Mirakl Connect catalog in bulk?
  - id: listProducts
    intent: List products in the Connect catalog
    question: How do I see all products imported into my Mirakl Connect catalog?
  - id: upsertProducts
    intent: Create or update Connect catalog products
    question: How do I add or update products in my Mirakl Connect catalog?
  phrasing_ops: 3
  slug: mirakl-catalog-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Channel API from Mirakl — 1 operation(s) for channel.
  name: Mirakl Channel API
  phrasing_intents:
  - id: SELLER_ACCOUNT_CHANNEL_UPSERT
    intent: Create or update channels
    question: How do I register sales channels for seller accounts?
  phrasing_ops: 1
  slug: mirakl-channel-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Checkout API from Mirakl — 1 operation(s) for checkout.
  name: Mirakl Checkout API
  phrasing_intents:
  - id: GetCustomCarrierRates
    intent: Get Mirakl carrier rates for checkout
    question: How do I show the Mirakl shipping method as a custom carrier rate at checkout?
  phrasing_ops: 1
  slug: mirakl-checkout-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Connection API from Mirakl — 2 operation(s) for connection.
  name: Mirakl Connection API
  phrasing_intents:
  - id: GetConnection
    intent: Get the Shopify-Mirakl connection
    question: Is my Shopify store connected to a Mirakl instance?
  - id: HardDeleteConnectionDev
    intent: Hard delete a dev/test connection
    question: How do I wipe a test connection environment to start over?
  phrasing_ops: 2
  slug: mirakl-connection-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Conversations API from Mirakl — 5 operation(s) for conversations.
  name: Mirakl Conversations API
  phrasing_intents:
  - id: createConversation
    intent: Start a conversation with a customer
    question: How do I start a new conversation with a marketplace customer?
  - id: listConversations
    intent: List order conversations
    question: Which customer conversations have changed since my last sync?
  - id: createMessage
    intent: Send a message in a conversation
    question: How do I reply to a customer inside an existing conversation?
  - id: downloadConversationAttachments
    intent: Download conversation attachments
    question: How do I get all the files shared in a conversation?
  - id: getConversationActionStatus
    intent: Check a conversation action's status
    question: Did my asynchronous conversation request succeed?
  - id: getConversationMessages
    intent: Get a conversation's messages
    question: What messages have been exchanged in a conversation?
  phrasing_ops: 6
  slug: mirakl-conversations-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Mapping API from Mirakl — 2 operation(s) for mapping.
  name: Mirakl Mapping API
  phrasing_intents:
  - id: ListOrderReturnMappings
    intent: List Mirakl returns for a Shopify order
    question: Which marketplace returns are linked to a Shopify order?
  - id: ListOrderTransactionMappings
    intent: List Mirakl transactions for a Shopify order
    question: What debits, refunds and cancellations has Mirakl recorded for a Shopify order?
  phrasing_ops: 2
  slug: mirakl-mapping-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Mirakl Connect Channel Platform Webhooks API from Mirakl — 0 operation(s) for mirakl connect channel platform webhooks.
  name: Mirakl Connect Channel Platform Webhooks API
  slug: mirakl-mirakl-connect-channel-platform-webhooks-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Product Bindings API from Mirakl — 2 operation(s) for product bindings.
  name: Mirakl Product Bindings API
  phrasing_intents:
  - id: DeleteProductBindings
    intent: Delete product bindings
    question: How do I unlink a Shopify product from its Mirakl product?
  - id: ImportProductBindings
    intent: Create product bindings
    question: How do I link existing Shopify products to Mirakl products?
  - id: ListProductBindings
    intent: List product bindings
    question: Which Mirakl product is a Shopify product linked to?
  - id: UpdateProductBindings
    intent: Update product bindings
    question: Can I change an existing product binding instead of recreating it?
  phrasing_ops: 4
  slug: mirakl-product-bindings-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Public API from Mirakl — 2 operation(s) for public.
  name: Mirakl Public API
  phrasing_intents:
  - id: GetCheckoutData
    intent: Get marketplace data for checkout
    question: What marketplace information should I show at checkout for a cart?
  - id: GetShippingFees
    intent: Get shipping fees per seller at checkout
    question: Which shipping methods and fees does each seller offer for my cart?
  phrasing_ops: 2
  slug: mirakl-public-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Settings API from Mirakl — 1 operation(s) for settings.
  name: Mirakl Settings API
  phrasing_intents:
  - id: ListSettings
    intent: List connector settings
    question: What settings is my Mirakl connector currently using?
  - id: UpdateSettings
    intent: Update connector settings
    question: How do I change a single connector setting without resetting the others?
  phrasing_ops: 2
  slug: mirakl-settings-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Setup API from Mirakl — 3 operation(s) for setup.
  name: Mirakl Setup API
  phrasing_intents:
  - id: SetupCheckConsistency
    intent: Check whether installed app data is current
    question: Is the data set up when I installed the app still up to date?
  - id: SetupCheckPermissions
    intent: Check the Shopify app permissions
    question: Does the Shopify app have all the permissions it needs?
  - id: SetupUpdate
    intent: Refresh the app's initialized data
    question: How do I update the data created during the app installation?
  phrasing_ops: 3
  slug: mirakl-setup-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Shipments API from Mirakl — 2 operation(s) for shipments.
  name: Mirakl Shipments API
  phrasing_intents:
  - id: createShipment
    intent: Ship items of a Connect order (original)
    question: How do I ship items of a Connect order in one package with the original shipment call?
  - id: v2-createShipment
    intent: Ship items of a Connect order (v2)
    question: How do I ship Connect order items from a specific warehouse?
  phrasing_ops: 2
  slug: mirakl-shipments-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Storefront API from Mirakl — 13 operation(s) for storefront.
  name: Mirakl Storefront API
  phrasing_intents:
  - id: CreateReturn
    intent: Create a return from the storefront
    question: How can a shopper start a return for an order from my storefront?
  - id: GetEvaluationsAssessments
    intent: Get seller evaluation criteria
    question: What criteria do customers rate sellers on in the storefront?
  - id: GetItemsToReturn
    intent: Get returnable items for orders
    question: Which items can a shopper still return from their orders?
  - id: GetPromotions
    intent: Get promotions for offers
    question: Which promotions apply when a shopper buys a given offer?
  - id: GetReturns
    intent: List a shopper's returns
    question: Where can a customer see the status of returns they've started?
  - id: GetShipment
    intent: Get shipment by Shopify fulfillment
    question: How do I get Mirakl shipment details from a Shopify fulfillment ID?
  - id: ListAccountingOrdersDocuments
    intent: List accounting documents for orders
    question: Where can a shopper download invoices for their marketplace orders?
  - id: ListOrdersDocuments
    intent: List general documents for orders
    question: What non-accounting documents are attached to my marketplace orders?
  phrasing_ops: 13
  slug: mirakl-storefront-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Synchronization API from Mirakl — 11 operation(s) for synchronization.
  name: Mirakl Synchronization API
  phrasing_intents:
  - id: SyncCatalogStructure
    intent: Sync Shopify categories and attributes to Mirakl
    question: How do I push my Shopify category structure and attributes into Mirakl?
  - id: SyncDeletedMiraklProducts
    intent: Remove products deleted in Mirakl from Shopify
    question: How do I remove third-party products from Shopify that were deleted in Mirakl?
  - id: SyncFirstPartyProducts
    intent: Sync first-party products from Shopify to Mirakl
    question: How do I send my own Shopify products to Mirakl?
  - id: SyncOfferConditions
    intent: Sync offer conditions from Mirakl to Shopify
    question: How do I bring Mirakl offer conditions into Shopify?
  - id: SyncOffers
    intent: Import Mirakl offers into Shopify
    question: How do I import seller offers from Mirakl into Shopify?
  - id: SyncOrders
    intent: Sync orders between Mirakl and Shopify
    question: How do I force an order sync between Mirakl and Shopify?
  - id: SyncPromotions
    intent: Sync Mirakl promotions into Shopify discounts
    question: How do Mirakl promotions become Shopify code discounts?
  - id: SyncReturns
    intent: Sync returns from Mirakl to Shopify
    question: How do I bring Mirakl returns into Shopify?
  phrasing_ops: 11
  slug: mirakl-synchronization-api
- baseURL: https://your-instance.mirakl.net
  baseurl_source: declared
  description: The Synchronization Errors API from Mirakl — 14 operation(s) for synchronization errors.
  name: Mirakl Synchronization Errors API
  phrasing_intents:
  - id: GetOfferRecoverableError
    intent: Get one offer sync error
    question: What went wrong with a specific offer that failed to sync into Shopify?
  - id: GetOrderRecoverableError
    intent: Get one order sync error
    question: Why did a particular order fail to sync between Mirakl and Shopify?
  - id: GetProductRecoverableError
    intent: Get one product sync error
    question: What caused a specific product to fail during catalog synchronization?
  - id: GetPromotionRecoverableError
    intent: Get one promotion sync error
    question: Why did one Mirakl promotion fail to become a Shopify discount?
  - id: GetReturnRecoverableError
    intent: Get one return sync error
    question: What went wrong when a specific return synced from Mirakl to Shopify?
  - id: GetShipmentRecoverableError
    intent: Get one shipment sync error
    question: Why did a particular shipment fail to sync into Shopify?
  - id: GetShopRecoverableError
    intent: Get one shop sync error
    question: What stopped a specific Mirakl shop from syncing into Shopify?
  - id: ListOfferRecoverableErrors
    intent: List offer sync errors
    question: Which offers failed to sync from Mirakl into Shopify?
  phrasing_ops: 14
  slug: mirakl-synchronization-errors-api
artifact_total: 63
asyncapis:
- description: ''
  name: Mirakl Webhooks
  slug: mirakl-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers API
  slug: open-mirakl-carriers-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Catalog Configuration API
  slug: open-mirakl-catalog-configuration-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Incidents API
  slug: open-mirakl-incidents-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Invoicing and Accounting API
  slug: open-mirakl-invoicing-and-accounting-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Messages API
  slug: open-mirakl-messages-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Multiple shipments API
  slug: open-mirakl-multiple-shipments-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Offers API
  slug: open-mirakl-offers-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Orders API
  slug: open-mirakl-orders-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Picklists API
  slug: open-mirakl-picklists-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Platform Settings API
  slug: open-mirakl-platform-settings-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Product Feedback API
  slug: open-mirakl-product-feedback-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Products API
  slug: open-mirakl-products-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Promotions API
  slug: open-mirakl-promotions-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Returns API
  slug: open-mirakl-returns-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Services API
  slug: open-mirakl-services-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Store API
  slug: open-mirakl-store-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Stores API
  slug: open-mirakl-stores-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Taxonomy API
  slug: open-mirakl-taxonomy-api
- collection_type: open
  name: Mirakl Connect Channel Platform APIs Carriers Users API
  slug: open-mirakl-users-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/capabilities/mirakl-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mirakl-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-connect-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-connect-channel-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-connect-channel-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-account-channel-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-account-channel-platform-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-mmp-front-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-mmp-front-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-mcm-front-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-mcm-front-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-mms-front-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-mms-front-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-shopify-operator-connector-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-shopify-operator-connector-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mirakl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mirakl.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mirakl.com/content/product/mmp/rest/seller/openapi3
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mirakl.com/content/product/connect-channel-platform/getting-started/api-overview
- group: operate
  title: ''
  type: Support
  url: https://help.mirakl.net
- group: company
  title: ''
  type: Blog
  url: https://www.mirakl.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mirakl
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mirakl.com/products/connect/pricing/
- group: start
  title: ''
  type: Login
  url: https://miraklconnect.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mirakl.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mirakl.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mirakl.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/authentication/mirakl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mirakl-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/scopes/mirakl-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mirakl-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/conventions/mirakl-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mirakl-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/errors/mirakl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mirakl-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/data-model/mirakl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mirakl-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/lifecycle/mirakl-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mirakl-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/packages/mirakl-packages.yml
  title: ''
  type: Packages
  url: packages/mirakl-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/packages/mirakl-packages.yml
  title: ''
  type: SDKs
  url: packages/mirakl-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/mcp/mirakl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mirakl-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/well-known/mirakl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mirakl-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/llms/mirakl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mirakl-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/overlays/mirakl-mmp-seller-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mirakl-mmp-seller-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/conformance/mirakl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mirakl-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mirakl.com/why-mirakl/technology
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/security/mirakl-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mirakl-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/security/mirakl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mirakl-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/agentic-access/mirakl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mirakl-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/asyncapi/mirakl-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mirakl-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.mirakl.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/rate-limits/mirakl-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mirakl-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/plans/mirakl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mirakl-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/changelog/mirakl-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mirakl-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/sandbox/mirakl-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mirakl-sandbox.yml
- group: build
  title: ''
  type: Postman
  url: https://developer.mirakl.com/specs/content/product/mmp/rest/seller/postman-mmp-seller.json?download
- group: start
  title: ''
  type: SignUp
  url: https://www.mirakl.com/products/connect/pricing/
created: '2026-07-17'
description: Mirakl is the global leader in platform business innovation, providing an operating system for commerce that lets retailers, brands, and B2B distributors launch and scale online marketplaces and dropship programs without holding inventory. The platform spans the Mirakl Marketplace Platform (MMP), Mirakl Platform for Services (MPS), the Mirakl Catalog Platform, Mirakl Connect for multichannel selling, Mirakl Ads retail media, and Mirakl Payout. Mirakl exposes extensive REST APIs (OpenAPI 3.1) for sellers/shops and operators covering orders, offers, products, catalog, invoicing, messaging, returns, and shipments, plus a Connect Channel Platform with push webhooks for offer, price/stock, product, order-action, and store events.
image: https://developer.mirakl.com/assets/favicon.4ab028206801f00ee2105fefa49d337d0d59395bb42860e0a6ab464c1729fe2d.930eac86.ico
layout: provider
mcp_servers:
- description: Remote MCP server at developer.mirakl.com over streamable HTTP.
  name: Mirakl MCP Server
  slug: mirakl-developer-docs
modified: '2026-09-16'
name: Mirakl
nav: Providers
network: true
overview: 'Mirakl publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Carriers API, Catalog Configuration API, Incidents API, and 31 more. Tagged areas include Company, Commerce, E-Commerce, Marketplace, and Dropship.


  The Mirakl catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mirakl''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 39 more developer resources.'
plans:
- name: Mirakl Plans Pricing
  plan_count: 3
  slug: mirakl-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 478
  name: Mirakl Rate Limits
  slug: mirakl-rate-limits
scopes:
- name: Mirakl Scopes
  scope_count: 0
  slug: mirakl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 55.9
    developer_ergonomics: 73.2
    discoverability: 78.6
    operational_transparency: 50.0
  previous_composite: 72.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 95.7
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/mirakl/refs/heads/main/screenshots/mirakl-2026-08-07T183712.png
security:
- kind: authentication
  name: Mirakl Authentication
  slug: mirakl-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Mirakl Domain Security
  slug: mirakl-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Mirakl Trust Center
  slug: mirakl-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27018, ISO 22301
slug: mirakl
tags:
- Company
- Commerce
- E-Commerce
- Marketplace
- Dropship
- Retail
- Catalog
- Order
- Retail Media
- B2B
website: https://www.mirakl.com/
---
