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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 170
  human_in_the_loop: 3
  name: Square Agentic Access
  operation_count: 305
  slug: square-agentic-access
  summary_line: 305 operations · 170 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Reporting API (Beta) provides a new way to access all of a business's data to build custom reports and integrations, surfacing sales, payments, and operational metrics across a seller's Square acc
  name: Square Reporting API
  slug: reporting-api
- description: The Channels API lets applications represent and manage the sales channels through which a seller transacts, enabling attribution of orders and payments to specific online or in-person channels.
  name: Square Channels API
  slug: channels-api
- description: The Transfer Orders API lets applications create and manage transfers of inventory stock between a seller's locations, supporting multi-location retail and restaurant operations.
  name: Square Transfer Orders API
  slug: transfer-orders-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The BookingCustomAttributes API from Square — 6 operation(s) for bookingcustomattributes.
  name: Square BookingCustomAttributes API
  phrasing_intents:
  - id: ListBookingCustomAttributeDefinitions
    intent: List booking custom field definitions
    question: What custom fields have been defined for bookings?
  - id: CreateBookingCustomAttributeDefinition
    intent: Define a new custom field for bookings
    question: How do I add a custom field, like a pet's name, to appointments?
  - id: DeleteBookingCustomAttributeDefinition
    intent: Delete a booking custom field definition
    question: How do I remove a custom field definition from bookings entirely?
  - id: RetrieveBookingCustomAttributeDefinition
    intent: Get a booking custom field definition
    question: What is the schema of one booking custom attribute definition?
  - id: UpdateBookingCustomAttributeDefinition
    intent: Update a booking custom field definition
    question: How do I rename or change the description of a booking custom field?
  - id: BulkDeleteBookingCustomAttributes
    intent: Delete custom field values on many bookings
    question: Can I clear a custom field value from many bookings at once?
  - id: BulkUpsertBookingCustomAttributes
    intent: Set custom field values on many bookings
    question: How do I set a custom field value on lots of appointments in one call?
  - id: ListBookingCustomAttributes
    intent: List a booking's custom field values
    question: What custom field values are stored on a specific appointment?
  phrasing_ops: 11
  slug: square-bookingcustomattributes-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Bookings API from Square — 11 operation(s) for bookings.
  name: Square Bookings API
  phrasing_intents:
  - id: ListBookings
    intent: List bookings
    question: How do I see all upcoming appointments for my business?
  - id: CreateBooking
    intent: Book an appointment
    question: How do I schedule a new appointment for a customer in Square?
  - id: SearchAvailability
    intent: Find open appointment slots
    question: What time slots are open for a service next week?
  - id: BulkRetrieveBookings
    intent: Fetch several bookings by ID
    question: Can I get the details of multiple appointments in one request?
  - id: RetrieveBusinessBookingProfile
    intent: Get the seller's booking profile
    question: What are my business's online booking settings?
  - id: ListLocationBookingProfiles
    intent: List location booking profiles
    question: Which of my locations accept bookings?
  - id: RetrieveLocationBookingProfile
    intent: Get one location's booking profile
    question: What are the booking settings for one particular location?
  - id: ListTeamMemberBookingProfiles
    intent: List team member booking profiles
    question: Which staff members can take appointments at a location?
  phrasing_ops: 13
  slug: square-bookings-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Cards API from Square — 3 operation(s) for cards.
  name: Square Cards API
  phrasing_intents:
  - id: ListCards
    intent: List saved cards on file
    question: Which cards on file does a customer have?
  - id: CreateCard
    intent: Save a card on file
    question: How do I store a card for future charges using the Cards API?
  - id: RetrieveCard
    intent: Get a saved card
    question: What brand, last four and expiry does a saved card have?
  - id: DisableCard
    intent: Disable a saved card
    question: How do I stop a saved card from being charged again?
  phrasing_ops: 4
  slug: square-cards-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Catalog API from Square — 13 operation(s) for catalog.
  name: Square Catalog API
  phrasing_intents:
  - id: BatchDeleteCatalogObjects
    intent: Delete several catalog objects at once
    question: How do I delete a bunch of catalog items in one request?
  - id: BatchRetrieveCatalogObjects
    intent: Fetch several catalog objects by ID
    question: Can I fetch many catalog items by their IDs in one call?
  - id: BatchUpsertCatalogObjects
    intent: Create or update catalog objects in bulk
    question: How do I import thousands of products into my Square catalog at once?
  - id: CreateCatalogImage
    intent: Upload a catalog image
    question: How do I add a product photo to an item in my catalog?
  - id: UpdateCatalogImage
    intent: Replace an existing catalog image file
    question: Can I swap out the photo on an existing catalog image?
  - id: CatalogInfo
    intent: Get catalog API batch size limits
    question: What are the batch size limits for catalog upserts?
  - id: ListCatalog
    intent: List catalog objects by type
    question: How do I list all items and categories in my catalog?
  - id: UpsertCatalogObject
    intent: Create or update one catalog object
    question: How do I add a single new item to my Square catalog?
  phrasing_ops: 14
  slug: square-catalog-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Checkout API from Square — 5 operation(s) for checkout.
  name: Square Checkout API
  phrasing_intents:
  - id: CreateCheckout
    intent: Create a legacy hosted checkout for an order
    question: How do I send buyers to a hosted checkout page for an order using the older Checkout endpoint?
  - id: RetrieveLocationSettings
    intent: Get checkout page settings for a location
    question: What tipping and custom field settings does a location's hosted checkout use?
  - id: UpdateLocationSettings
    intent: Update checkout page settings for a location
    question: Can I change the hosted checkout options for just one location?
  - id: RetrieveMerchantSettings
    intent: Get account-wide checkout page settings
    question: Which payment methods are enabled on my hosted checkout pages account-wide?
  - id: UpdateMerchantSettings
    intent: Update account-wide checkout page settings
    question: Can I turn on a payment method for all hosted checkout pages at once?
  - id: ListPaymentLinks
    intent: List payment links
    question: Which payment links have I created so far?
  - id: CreatePaymentLink
    intent: Create a payment link
    question: How do I create a shareable link that lets a buyer pay me?
  - id: DeletePaymentLink
    intent: Delete a payment link
    question: How do I deactivate a payment link so no one can pay it?
  phrasing_ops: 10
  slug: square-checkout-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The CustomerCustomAttributes API from Square — 5 operation(s) for customercustomattributes.
  name: Square CustomerCustomAttributes API
  phrasing_intents:
  - id: ListCustomerCustomAttributeDefinitions
    intent: List customer custom attribute definitions
    question: What custom fields have been defined for customer profiles?
  - id: CreateCustomerCustomAttributeDefinition
    intent: Define a new customer custom attribute
    question: How do I add a custom field like favorite drink to customer profiles?
  - id: DeleteCustomerCustomAttributeDefinition
    intent: Delete a customer custom attribute definition
    question: Will deleting a customer attribute definition wipe its values from all profiles?
  - id: RetrieveCustomerCustomAttributeDefinition
    intent: Get a customer custom attribute definition
    question: What schema does a customer custom attribute definition use?
  - id: UpdateCustomerCustomAttributeDefinition
    intent: Update a customer custom attribute definition
    question: Can I change the name or visibility of a customer attribute definition?
  - id: BulkUpsertCustomerCustomAttributes
    intent: Set custom attributes on many customers
    question: Can I set custom field values on many customer profiles in one request?
  - id: ListCustomerCustomAttributes
    intent: List a customer's custom attributes
    question: Which custom attribute values are stored on a customer profile?
  - id: DeleteCustomerCustomAttribute
    intent: Delete one custom attribute from a customer
    question: Can I clear one custom field value from a customer profile?
  phrasing_ops: 10
  slug: square-customercustomattributes-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Customers API from Square — 10 operation(s) for customers.
  name: Square Customers API
  phrasing_intents:
  - id: ListCustomers
    intent: List customer profiles
    question: How do I page through every customer profile in my Square account?
  - id: CreateCustomer
    intent: Create a customer profile
    question: What is the minimum info needed to add a new customer?
  - id: BulkCreateCustomers
    intent: Create many customer profiles at once
    question: Can I import a batch of new customers in one request?
  - id: BulkDeleteCustomers
    intent: Delete many customer profiles at once
    question: Can I delete a list of customers in a single call?
  - id: BulkRetrieveCustomers
    intent: Fetch several customers by ID
    question: Can I look up multiple customers at once when I already have their IDs?
  - id: BulkUpdateCustomers
    intent: Update many customer profiles at once
    question: Is there a way to update many customer records in one request?
  - id: SearchCustomers
    intent: Search customers by filters
    question: How do I find customers by email, phone or creation date?
  - id: DeleteCustomer
    intent: Delete one customer profile
    question: Can I delete a single customer profile permanently?
  phrasing_ops: 14
  slug: square-customers-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Devices API from Square — 4 operation(s) for devices.
  name: Square Devices API
  phrasing_intents:
  - id: ListDevices
    intent: List Terminal devices
    question: Which Square Terminal devices are connected to my account?
  - id: ListDeviceCodes
    intent: List device pairing codes
    question: What device codes have I created for pairing terminals?
  - id: CreateDeviceCode
    intent: Create a code to pair a Terminal
    question: How do I pair a new Square Terminal with my app?
  - id: GetDeviceCode
    intent: Get a device pairing code
    question: Has a device code been used to pair a Terminal yet?
  - id: GetDevice
    intent: Get a Terminal device
    question: What are the details and status of one Terminal device?
  phrasing_ops: 5
  slug: square-devices-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Disputes API from Square — 8 operation(s) for disputes.
  name: Square Disputes API
  phrasing_intents:
  - id: ListDisputes
    intent: List payment disputes
    question: Which chargebacks are currently open against my account?
  - id: RetrieveDispute
    intent: Get a dispute
    question: What is the reason and due date for a specific chargeback?
  - id: AcceptDispute
    intent: Accept the loss on a dispute
    question: What happens to my balance if I accept a chargeback?
  - id: ListDisputeEvidence
    intent: List evidence on a dispute
    question: What evidence have I already attached to a dispute?
  - id: CreateDisputeEvidenceFile
    intent: Upload an evidence file to a dispute
    question: Which file formats can I upload as dispute evidence?
  - id: CreateDisputeEvidenceText
    intent: Add text evidence to a dispute
    question: Can I submit a written explanation or tracking number as dispute evidence?
  - id: DeleteDisputeEvidence
    intent: Remove evidence from a dispute
    question: How do I take back evidence I uploaded to a dispute by mistake?
  - id: RetrieveDisputeEvidence
    intent: Get one piece of dispute evidence
    question: Can I download evidence after I upload it to a dispute?
  phrasing_ops: 9
  slug: square-disputes-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Employees API from Square — 2 operation(s) for employees.
  name: Square Employees API
  phrasing_intents:
  - id: ListEmployees
    intent: List employees
    question: Who are the employees at one of my locations?
  - id: RetrieveEmployee
    intent: Get an employee
    question: How do I look up one employee's record by ID?
  phrasing_ops: 2
  slug: square-employees-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Events API from Square — 4 operation(s) for events.
  name: Square Events API
  phrasing_intents:
  - id: SearchEvents
    intent: Search recent API events
    question: How do I find Square API events from the last few weeks?
  - id: DisableEvents
    intent: Turn off event searchability
    question: How do I stop events from being searchable?
  - id: EnableEvents
    intent: Turn on event searchability
    question: How do I make events searchable for my application?
  - id: ListEventTypes
    intent: List event types
    question: What event types can I query or subscribe to?
  phrasing_ops: 4
  slug: square-events-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The GiftCardActivities API from Square — 1 operation(s) for giftcardactivities.
  name: Square GiftCardActivities API
  phrasing_intents:
  - id: ListGiftCardActivities
    intent: List gift card activities
    question: What loads, redemptions and adjustments happened on a gift card?
  - id: CreateGiftCardActivity
    intent: Activate, load or redeem a gift card
    question: How do I activate a gift card with a starting balance?
  phrasing_ops: 2
  slug: square-giftcardactivities-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Inventory API from Square — 13 operation(s) for inventory.
  name: Square Inventory API
  phrasing_intents:
  - id: DeprecatedRetrieveInventoryAdjustment
    intent: Get an adjustment (deprecated URL)
    question: Is there an older singular adjustment URL for reading an inventory adjustment?
  - id: RetrieveInventoryAdjustment
    intent: Get an inventory adjustment
    question: How do I view one inventory adjustment, like a sale or waste record?
  - id: DeprecatedBatchChangeInventory
    intent: Apply stock changes (deprecated URL)
    question: Is the old batch-change inventory URL still usable?
  - id: DeprecatedBatchRetrieveInventoryChanges
    intent: Read stock history (deprecated URL)
    question: Is there a legacy batch-retrieve-changes URL for inventory history?
  - id: DeprecatedBatchRetrieveInventoryCounts
    intent: Read stock counts (deprecated URL)
    question: Is the old batch-retrieve-counts URL still around for stock levels?
  - id: BatchChangeInventory
    intent: Adjust or recount stock in bulk
    question: How do I record a stock recount or adjustment for many items at once?
  - id: BatchRetrieveInventoryChanges
    intent: Search inventory change history
    question: Where can I see the history of stock adjustments for my items?
  - id: BatchRetrieveInventoryCounts
    intent: Get current stock counts in bulk
    question: How much stock do I have of several items across my locations?
  phrasing_ops: 13
  slug: square-inventory-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Invoices API from Square — 7 operation(s) for invoices.
  name: Square Invoices API
  phrasing_intents:
  - id: ListInvoices
    intent: List invoices for a location
    question: How do I see all invoices issued from one of my locations?
  - id: CreateInvoice
    intent: Draft an invoice for an order
    question: How do I create an invoice for an order I already made?
  - id: SearchInvoices
    intent: Search invoices by location and customer
    question: Which invoices have I sent to a particular customer?
  - id: DeleteInvoice
    intent: Delete a draft invoice
    question: How do I throw away a draft invoice I no longer need?
  - id: GetInvoice
    intent: Get an invoice
    question: How do I look up one invoice and its payment status?
  - id: UpdateInvoice
    intent: Edit an invoice
    question: How do I change the due date or recipient on an existing invoice?
  - id: CreateInvoiceAttachment
    intent: Attach a file to an invoice
    question: How do I attach a receipt or PDF to an invoice?
  - id: DeleteInvoiceAttachment
    intent: Remove an attachment from an invoice
    question: How do I remove a file I attached to an invoice?
  phrasing_ops: 10
  slug: square-invoices-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Labor API from Square — 11 operation(s) for labor.
  name: Square Labor API
  phrasing_intents:
  - id: ListBreakTypes
    intent: List break types for a business
    question: What kinds of breaks have we set up for staff at each location?
  - id: CreateBreakType
    intent: Create a break type template
    question: How do I set up a new paid or unpaid break template for employees?
  - id: DeleteBreakType
    intent: Delete a break type
    question: Can I remove a break type even if shifts already reference it?
  - id: GetBreakType
    intent: Get a single break type
    question: What are the settings of one specific break type?
  - id: UpdateBreakType
    intent: Update a break type template
    question: Can I change the name or length of an existing break type?
  - id: ListEmployeeWages
    intent: List employee wages (legacy)
    question: Where can I see hourly wages using the older employee wage records?
  - id: GetEmployeeWage
    intent: Get a legacy employee wage record
    question: What does a single legacy EmployeeWage record contain?
  - id: CreateShift
    intent: Record a new shift for a team member
    question: How do I log a workday for a team member at a location?
  phrasing_ops: 16
  slug: square-labor-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The LocationCustomAttributes API from Square — 6 operation(s) for locationcustomattributes.
  name: Square LocationCustomAttributes API
  phrasing_intents:
  - id: ListLocationCustomAttributeDefinitions
    intent: List location custom field definitions
    question: What custom fields exist for my store locations?
  - id: CreateLocationCustomAttributeDefinition
    intent: Define a new custom field for locations
    question: How do I add a custom field, like a store manager, to my locations?
  - id: DeleteLocationCustomAttributeDefinition
    intent: Delete a location custom field definition
    question: How do I remove a custom field definition from all my locations?
  - id: RetrieveLocationCustomAttributeDefinition
    intent: Get a location custom field definition
    question: What does one location custom attribute definition look like?
  - id: UpdateLocationCustomAttributeDefinition
    intent: Update a location custom field definition
    question: How do I rename a custom field defined for locations?
  - id: BulkDeleteLocationCustomAttributes
    intent: Delete custom field values on many locations
    question: Can I clear custom field values from several locations at once?
  - id: BulkUpsertLocationCustomAttributes
    intent: Set custom field values on many locations
    question: How do I set a custom field value on all my stores in one call?
  - id: ListLocationCustomAttributes
    intent: List a location's custom field values
    question: What custom field values are stored on one store location?
  phrasing_ops: 11
  slug: square-locationcustomattributes-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Locations API from Square — 2 operation(s) for locations.
  name: Square Locations API
  phrasing_intents:
  - id: ListLocations
    intent: List all business locations
    question: Which locations does my Square account have, including inactive ones?
  - id: CreateLocation
    intent: Create a business location
    question: Can I add a new store location through the API?
  - id: RetrieveLocation
    intent: Get one location
    question: What address and hours are set for a specific location?
  - id: UpdateLocation
    intent: Update a location
    question: Can I change a location's business hours or address?
  phrasing_ops: 4
  slug: square-locations-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Loyalty API from Square — 16 operation(s) for loyalty.
  name: Square Loyalty API
  phrasing_intents:
  - id: CreateLoyaltyAccount
    intent: Enroll a buyer in the loyalty program
    question: How do I sign a customer up for my Square loyalty program using their phone number?
  - id: SearchLoyaltyAccounts
    intent: Find loyalty accounts by phone or customer
    question: Can I look up a loyalty member by their phone number?
  - id: RetrieveLoyaltyAccount
    intent: Get a loyalty account
    question: How can I see the point balance on one specific loyalty account?
  - id: AccumulateLoyaltyPoints
    intent: Award points earned from a purchase
    question: How do I give a loyalty member the points they earned on an order?
  - id: AdjustLoyaltyPoints
    intent: Manually add or subtract loyalty points
    question: How do I manually correct a buyer's loyalty point balance?
  - id: SearchLoyaltyEvents
    intent: Search the loyalty points ledger
    question: Where can I see the history of points earned and redeemed on loyalty accounts?
  - id: ListLoyaltyPrograms
    intent: List the seller's loyalty programs
    question: What loyalty program does my Square account have set up?
  - id: RetrieveLoyaltyProgram
    intent: Get a loyalty program's rules
    question: How do I read the earning rules and reward tiers of my loyalty program?
  phrasing_ops: 18
  slug: square-loyalty-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The MerchantCustomAttributes API from Square — 6 operation(s) for merchantcustomattributes.
  name: Square MerchantCustomAttributes API
  phrasing_intents:
  - id: ListMerchantCustomAttributeDefinitions
    intent: List merchant custom attribute definitions
    question: What custom fields have been defined for my seller account?
  - id: CreateMerchantCustomAttributeDefinition
    intent: Define a new merchant custom attribute
    question: How do I define a new custom field that can be stored on the merchant?
  - id: DeleteMerchantCustomAttributeDefinition
    intent: Delete a merchant custom attribute definition
    question: Does deleting a merchant attribute definition also remove its stored values?
  - id: RetrieveMerchantCustomAttributeDefinition
    intent: Get a merchant custom attribute definition
    question: What schema and visibility does a merchant custom attribute definition have?
  - id: UpdateMerchantCustomAttributeDefinition
    intent: Update a merchant custom attribute definition
    question: Can I rename or change the visibility of a merchant attribute definition?
  - id: BulkDeleteMerchantCustomAttributes
    intent: Delete many merchant custom attributes
    question: Can I clear several merchant custom attribute values in one call?
  - id: BulkUpsertMerchantCustomAttributes
    intent: Set many merchant custom attributes
    question: Can I set several custom attribute values on merchants at once?
  - id: ListMerchantCustomAttributes
    intent: List a merchant's custom attributes
    question: What custom attribute values are stored on a merchant?
  phrasing_ops: 11
  slug: square-merchantcustomattributes-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Merchants API from Square — 2 operation(s) for merchants.
  name: Square Merchants API
  phrasing_intents:
  - id: ListMerchants
    intent: Get the merchant behind my access token
    question: Which merchant is my access token connected to?
  - id: RetrieveMerchant
    intent: Get a merchant by ID
    question: What business name, country and currency does a merchant have?
  phrasing_ops: 2
  slug: square-merchants-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The MobileAuthorization API from Square — 1 operation(s) for mobileauthorization.
  name: Square MobileAuthorization API
  phrasing_intents:
  - id: CreateMobileAuthorizationCode
    intent: Create a mobile reader authorization code
    question: How does my mobile app get authorized to connect to a Square card reader?
  phrasing_ops: 1
  slug: square-mobileauthorization-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The OrderCustomAttributes API from Square — 6 operation(s) for ordercustomattributes.
  name: Square OrderCustomAttributes API
  phrasing_intents:
  - id: ListOrderCustomAttributeDefinitions
    intent: List order custom field definitions
    question: What custom fields have been defined for orders?
  - id: CreateOrderCustomAttributeDefinition
    intent: Define a new custom field for orders
    question: How do I add a custom field, like a delivery note, to orders?
  - id: DeleteOrderCustomAttributeDefinition
    intent: Delete an order custom field definition
    question: How do I remove a custom field definition from orders entirely?
  - id: RetrieveOrderCustomAttributeDefinition
    intent: Get an order custom field definition
    question: What does one order custom attribute definition contain?
  - id: UpdateOrderCustomAttributeDefinition
    intent: Update an order custom field definition
    question: How do I change the name or description of an order custom field?
  - id: BulkDeleteOrderCustomAttributes
    intent: Delete custom field values on many orders
    question: Can I clear custom field values from several orders at once?
  - id: BulkUpsertOrderCustomAttributes
    intent: Set custom field values on many orders
    question: How do I set a custom field value on lots of orders in one call?
  - id: ListOrderCustomAttributes
    intent: List an order's custom field values
    question: What custom field values are stored on a specific order?
  phrasing_ops: 11
  slug: square-ordercustomattributes-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Orders API from Square — 7 operation(s) for orders.
  name: Square Orders API
  phrasing_intents:
  - id: CreateOrder
    intent: Create an order
    question: How do I create an order with line items in Square?
  - id: BatchRetrieveOrders
    intent: Fetch several orders by ID
    question: Can I pull up many orders at once when I have their IDs?
  - id: CalculateOrder
    intent: Preview order pricing without saving
    question: How can I preview an order's total, taxes and discounts before creating it?
  - id: CloneOrder
    intent: Duplicate an existing order as a draft
    question: How do I copy an existing order to reorder the same items?
  - id: SearchOrders
    intent: Search orders across locations
    question: How do I find all orders from last week across my locations?
  - id: RetrieveOrder
    intent: Get an order
    question: What items and totals are on a specific order?
  - id: UpdateOrder
    intent: Update an open order
    question: How do I add or remove items on an order that's still open?
  - id: PayOrder
    intent: Pay for an order with approved payments
    question: How do I settle an order using payments I already approved?
  phrasing_ops: 8
  slug: square-orders-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Payments API from Square — 5 operation(s) for payments.
  name: Square Payments API
  phrasing_intents:
  - id: ListPayments
    intent: List payments
    question: How do I see all card payments taken in a date range?
  - id: CreatePayment
    intent: Charge a card or record a payment
    question: Can I charge a card or gift card from my own app?
  - id: CancelPaymentByIdempotencyKey
    intent: Void a payment by its idempotency key
    question: What should I do if I never got a response to a create payment request?
  - id: GetPayment
    intent: Get a payment
    question: What is the status and card detail of a specific payment?
  - id: UpdatePayment
    intent: Adjust amount or tip on an approved payment
    question: Can I change the tip on a payment before it's captured?
  - id: CancelPayment
    intent: Void an approved payment
    question: How do I void an authorized payment that hasn't been captured?
  - id: CompletePayment
    intent: Capture an approved payment
    question: How do I capture a delayed payment I authorized earlier?
  phrasing_ops: 7
  slug: square-payments-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Payouts API from Square — 3 operation(s) for payouts.
  name: Square Payouts API
  phrasing_intents:
  - id: ListPayouts
    intent: List payouts to the bank account
    question: When did Square send money to my bank account?
  - id: GetPayout
    intent: Get a payout
    question: How much was in one specific payout and where did it go?
  - id: ListPayoutEntries
    intent: List the entries in a payout
    question: Which charges, refunds and fees make up a payout?
  phrasing_ops: 3
  slug: square-payouts-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Refunds API from Square — 2 operation(s) for refunds.
  name: Square Refunds API
  phrasing_intents:
  - id: ListPaymentRefunds
    intent: List refunds
    question: Which refunds did we issue last month?
  - id: RefundPayment
    intent: Refund a payment
    question: How do I refund a customer's card payment?
  - id: GetPaymentRefund
    intent: Get a refund
    question: What is the status of a refund I issued?
  phrasing_ops: 3
  slug: square-refunds-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Sites API from Square — 1 operation(s) for sites.
  name: Square Sites API
  phrasing_intents:
  - id: ListSites
    intent: List the seller's Square Online sites
    question: What Square Online sites does this seller have?
  phrasing_ops: 1
  slug: square-sites-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Snippets API from Square — 1 operation(s) for snippets.
  name: Square Snippets API
  phrasing_intents:
  - id: DeleteSnippet
    intent: Remove my snippet from a site
    question: How do I remove the code my app added to a Square Online site?
  - id: RetrieveSnippet
    intent: Get my snippet on a Square Online site
    question: What code snippet has my app added to a Square Online site?
  - id: UpsertSnippet
    intent: Add or update a snippet on a site
    question: How do I add a script to the head of every page on a Square Online site?
  phrasing_ops: 3
  slug: square-snippets-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Subscriptions API from Square — 11 operation(s) for subscriptions.
  name: Square Subscriptions API
  phrasing_intents:
  - id: CreateSubscription
    intent: Enroll a customer in a subscription
    question: How do I sign a customer up for a subscription plan?
  - id: BulkSwapPlan
    intent: Move all subscribers to a new plan variation
    question: Can I migrate every active subscriber from one plan variation to another?
  - id: SearchSubscriptions
    intent: Search subscriptions by customer or location
    question: Which subscriptions does a given customer have?
  - id: RetrieveSubscription
    intent: Get one subscription
    question: What is the status and next billing date of a subscription?
  - id: UpdateSubscription
    intent: Update subscription fields
    question: Can I change the tax percentage or price override on an existing subscription?
  - id: DeleteSubscriptionAction
    intent: Delete a scheduled subscription action
    question: Can I undo a scheduled pause or cancellation on a subscription?
  - id: ChangeBillingAnchorDate
    intent: Change a subscription's billing day
    question: Can I move the day of the month a subscriber is billed?
  - id: CancelSubscription
    intent: Cancel a subscription
    question: How do I cancel a customer's subscription at the end of the billing period?
  phrasing_ops: 12
  slug: square-subscriptions-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Team API from Square — 8 operation(s) for team.
  name: Square Team API
  phrasing_intents:
  - id: CreateTeamMember
    intent: Add a team member
    question: How do I add a new employee to my Square team?
  - id: BulkCreateTeamMembers
    intent: Add many team members at once
    question: Can I onboard a whole batch of new staff in one request?
  - id: BulkUpdateTeamMembers
    intent: Update many team members at once
    question: Is there a way to update many existing team members together?
  - id: ListJobs
    intent: List job titles
    question: What job titles exist in my seller account?
  - id: CreateJob
    intent: Create a job title
    question: How do I create a new job title like Barista?
  - id: RetrieveJob
    intent: Get a job
    question: What title and tip setting does a specific job have?
  - id: UpdateJob
    intent: Rename a job or change tip eligibility
    question: If I rename a job, do shifts and wages pick up the new title?
  - id: SearchTeamMembers
    intent: Search team members
    question: Which team members are active at a given location?
  phrasing_ops: 12
  slug: square-team-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Terminal API from Square — 15 operation(s) for terminal.
  name: Square Terminal API
  phrasing_intents:
  - id: CreateTerminalAction
    intent: Send an action request to a Terminal device
    question: How do I push a custom action, like a device pairing check, to a Square Terminal?
  - id: SearchTerminalActions
    intent: Search Terminal action requests
    question: Which Terminal action requests did I send in the last 30 days?
  - id: GetTerminalAction
    intent: Get a Terminal action request
    question: What is the status of an action I sent to a Terminal?
  - id: CancelTerminalAction
    intent: Cancel a Terminal action request
    question: Can I cancel an action request before the device completes it?
  - id: DismissTerminalAction
    intent: Dismiss a Terminal action request
    question: How do I clear a finished action off the Terminal screen?
  - id: CreateTerminalCheckout
    intent: Send a checkout to a Terminal device
    question: How do I make a Square Terminal prompt the customer to pay a set amount?
  - id: SearchTerminalCheckouts
    intent: Search Terminal checkout requests
    question: Which Terminal checkouts did my app create recently?
  - id: GetTerminalCheckout
    intent: Get a Terminal checkout request
    question: Did the customer finish paying on the Terminal checkout I sent?
  phrasing_ops: 15
  slug: square-terminal-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Transactions API from Square — 4 operation(s) for transactions.
  name: Square Transactions API
  phrasing_intents:
  - id: ListTransactions
    intent: List a location's transactions
    question: How do I see sales and refund transactions for one location?
  - id: RetrieveTransaction
    intent: Get a transaction
    question: What are the tenders and refunds on one specific transaction?
  - id: CaptureTransaction
    intent: Capture a delayed-capture transaction
    question: How do I capture a charge I authorized with delayed capture?
  - id: VoidTransaction
    intent: Void a delayed-capture transaction
    question: How do I cancel an authorized charge before it's captured?
  phrasing_ops: 4
  slug: square-transactions-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The V1Transactions API from Square — 2 operation(s) for v1transactions.
  name: Square V1Transactions API
  phrasing_intents:
  - id: V1ListOrders
    intent: List online store orders (V1)
    question: Which online store orders came in at a location under the V1 API?
  - id: V1RetrieveOrder
    intent: Get an online store order with history (V1)
    question: What is the full history of one V1 online store order?
  - id: V1UpdateOrder
    intent: Complete, cancel or refund an online store order (V1)
    question: How do I mark a V1 online store order as shipped with a tracking number?
  phrasing_ops: 3
  slug: square-v1transactions-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Vendors API from Square — 6 operation(s) for vendors.
  name: Square Vendors API
  phrasing_intents:
  - id: BulkCreateVendors
    intent: Add several suppliers at once
    question: How do I add a list of my suppliers as vendors in one call?
  - id: BulkRetrieveVendors
    intent: Fetch several vendors by ID
    question: Can I look up multiple suppliers at once by their vendor IDs?
  - id: BulkUpdateVendors
    intent: Update several suppliers at once
    question: How do I update contact details for many vendors in one request?
  - id: CreateVendor
    intent: Add a supplier
    question: How do I add a single new supplier to my Square account?
  - id: SearchVendors
    intent: Search suppliers
    question: How do I find a supplier by name or status?
  - id: RetrieveVendor
    intent: Get a supplier
    question: What contact details do I have on file for a vendor?
  - id: UpdateVendor
    intent: Update one supplier
    question: How do I edit the details of a single supplier?
  phrasing_ops: 7
  slug: square-vendors-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The OAuth API from Square — 3 operation(s) for oauth.
  name: Square O Auth API
  phrasing_intents:
  - id: RevokeToken
    intent: Revoke a seller's OAuth access
    question: How do I disconnect my app from a seller's Square account?
  - id: ObtainToken
    intent: Get or refresh an OAuth access token
    question: How do I exchange an authorization code for an access token?
  - id: RetrieveTokenStatus
    intent: Check an access token's status
    question: When does my current access token expire?
  phrasing_ops: 3
  slug: square-oauth-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Apple Pay API from Square — 1 operation(s) for apple pay.
  name: Square Apple Pay API
  phrasing_intents:
  - id: RegisterDomain
    intent: Register a domain for Apple Pay on the Web
    question: How do I enable Apple Pay on my website's domain?
  phrasing_ops: 1
  slug: square-apple-pay-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Bank Accounts API from Square — 3 operation(s) for bank accounts.
  name: Square Bank Accounts API
  phrasing_intents:
  - id: ListBankAccounts
    intent: List linked bank accounts
    question: Which bank accounts are linked to my Square account?
  - id: GetBankAccountByV1Id
    intent: Get a bank account by its V1 ID
    question: I only have an old V1 bank account ID; can I still look it up?
  - id: GetBankAccount
    intent: Get a linked bank account
    question: What are the status and details of a specific linked bank account?
  phrasing_ops: 3
  slug: square-bank-accounts-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Cash Drawers API from Square — 3 operation(s) for cash drawers.
  name: Square Cash Drawers API
  phrasing_intents:
  - id: ListCashDrawerShifts
    intent: List cash drawer shifts
    question: How do I see all cash drawer shifts at a location for last month?
  - id: RetrieveCashDrawerShift
    intent: Get a cash drawer shift summary
    question: What were the expected and counted cash amounts for one drawer shift?
  - id: ListCashDrawerShiftEvents
    intent: List events in a cash drawer shift
    question: Which cash payments, paid-ins and paid-outs happened during a drawer shift?
  phrasing_ops: 3
  slug: square-cash-drawers-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Customer Groups API from Square — 2 operation(s) for customer groups.
  name: Square Customer Groups API
  phrasing_intents:
  - id: ListCustomerGroups
    intent: List customer groups
    question: What customer groups exist in my business?
  - id: CreateCustomerGroup
    intent: Create a customer group
    question: How do I create a new group like Wholesale Buyers?
  - id: DeleteCustomerGroup
    intent: Delete a customer group
    question: How do I delete a customer group we no longer need?
  - id: RetrieveCustomerGroup
    intent: Get a customer group
    question: What is the name of a specific customer group?
  - id: UpdateCustomerGroup
    intent: Rename a customer group
    question: Can I rename an existing customer group?
  phrasing_ops: 5
  slug: square-customer-groups-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Customer Segments API from Square — 2 operation(s) for customer segments.
  name: Square Customer Segments API
  phrasing_intents:
  - id: ListCustomerSegments
    intent: List customer segments
    question: What customer segments does my business have?
  - id: RetrieveCustomerSegment
    intent: Get a customer segment
    question: What are the details of one customer segment?
  phrasing_ops: 2
  slug: square-customer-segments-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Gift Cards API from Square — 6 operation(s) for gift cards.
  name: Square Gift Cards API
  phrasing_intents:
  - id: ListGiftCards
    intent: List gift cards
    question: Which gift cards are active in my account?
  - id: CreateGiftCard
    intent: Create or register a gift card
    question: How do I issue a new digital gift card?
  - id: RetrieveGiftCardFromGAN
    intent: Look up a gift card by its number
    question: Can I find a gift card using the number printed on it?
  - id: RetrieveGiftCardFromNonce
    intent: Look up a gift card from a payment token
    question: How do I identify a gift card from the secure token my payment form returned?
  - id: LinkCustomerToGiftCard
    intent: Link a customer to a gift card
    question: Can I save a gift card on file for a customer?
  - id: UnlinkCustomerFromGiftCard
    intent: Unlink a customer from a gift card
    question: How do I remove a gift card from a customer's saved cards?
  - id: RetrieveGiftCard
    intent: Get a gift card by ID
    question: What state and balance does a gift card have when I know its Square ID?
  phrasing_ops: 7
  slug: square-gift-cards-api
- baseURL: https://connect.squareup.com
  baseurl_source: spec
  description: The Webhook Subscriptions API from Square — 5 operation(s) for webhook subscriptions.
  name: Square Webhook Subscriptions API
  phrasing_intents:
  - id: ListWebhookEventTypes
    intent: List subscribable webhook event types
    question: Which webhook events can my app subscribe to?
  - id: ListWebhookSubscriptions
    intent: List my webhook subscriptions
    question: What webhook subscriptions does my application have?
  - id: CreateWebhookSubscription
    intent: Subscribe to webhook events
    question: How do I start receiving Square webhook notifications at my URL?
  - id: DeleteWebhookSubscription
    intent: Delete a webhook subscription
    question: How do I stop a webhook subscription for good?
  - id: RetrieveWebhookSubscription
    intent: Get a webhook subscription
    question: What events and URL does a given webhook subscription use?
  - id: UpdateWebhookSubscription
    intent: Update a webhook subscription
    question: How do I change the notification URL or events of a webhook subscription?
  - id: UpdateWebhookSubscriptionSignatureKey
    intent: Rotate a webhook signature key
    question: How do I rotate the signing key used to verify my webhooks?
  - id: TestWebhookSubscription
    intent: Send a test webhook event
    question: How can I check that my webhook endpoint is receiving events?
  phrasing_ops: 8
  slug: square-webhook-subscriptions-api
artifact_total: 403
asyncapis:
- description: 'AsyncAPI 2.6 description of the Square webhook event surface. Square delivers HTTPS POST notifications to a subscriber-provided `notification_url` whenever an event occurs on a seller''s account. Each '
  name: Square Webhooks
  slug: square-webhooks-asyncapi
collections:
- collection_type: postman
  name: Square ApplePay API
  slug: postman-square-applepay-api
- collection_type: postman
  name: Square ApplePay BankAccounts API
  slug: postman-square-bankaccounts-api
- collection_type: postman
  name: Square ApplePay BookingCustomAttributes API
  slug: postman-square-bookingcustomattributes-api
- collection_type: postman
  name: Square ApplePay Bookings API
  slug: postman-square-bookings-api
- collection_type: postman
  name: Square ApplePay Cards API
  slug: postman-square-cards-api
- collection_type: postman
  name: Square ApplePay CashDrawers API
  slug: postman-square-cashdrawers-api
- collection_type: postman
  name: Square ApplePay Catalog API
  slug: postman-square-catalog-api
- collection_type: postman
  name: Square ApplePay Checkout API
  slug: postman-square-checkout-api
- collection_type: postman
  name: Square ApplePay CustomerCustomAttributes API
  slug: postman-square-customercustomattributes-api
- collection_type: postman
  name: Square ApplePay CustomerGroups API
  slug: postman-square-customergroups-api
- collection_type: postman
  name: Square ApplePay Customers API
  slug: postman-square-customers-api
- collection_type: postman
  name: Square ApplePay CustomerSegments API
  slug: postman-square-customersegments-api
- collection_type: postman
  name: Square ApplePay Devices API
  slug: postman-square-devices-api
- collection_type: postman
  name: Square ApplePay Disputes API
  slug: postman-square-disputes-api
- collection_type: postman
  name: Square ApplePay Employees API
  slug: postman-square-employees-api
- collection_type: postman
  name: Square ApplePay Events API
  slug: postman-square-events-api
- collection_type: postman
  name: Square ApplePay GiftCardActivities API
  slug: postman-square-giftcardactivities-api
- collection_type: postman
  name: Square ApplePay GiftCards API
  slug: postman-square-giftcards-api
- collection_type: postman
  name: Square ApplePay Inventory API
  slug: postman-square-inventory-api
- collection_type: postman
  name: Square ApplePay Invoices API
  slug: postman-square-invoices-api
- collection_type: postman
  name: Square ApplePay Labor API
  slug: postman-square-labor-api
- collection_type: postman
  name: Square ApplePay LocationCustomAttributes API
  slug: postman-square-locationcustomattributes-api
- collection_type: postman
  name: Square ApplePay Locations API
  slug: postman-square-locations-api
- collection_type: postman
  name: Square ApplePay Loyalty API
  slug: postman-square-loyalty-api
- collection_type: postman
  name: Square ApplePay MerchantCustomAttributes API
  slug: postman-square-merchantcustomattributes-api
- collection_type: postman
  name: Square ApplePay Merchants API
  slug: postman-square-merchants-api
- collection_type: postman
  name: Square ApplePay MobileAuthorization API
  slug: postman-square-mobileauthorization-api
- collection_type: postman
  name: Square ApplePay OAuth API
  slug: postman-square-oauth-api
- collection_type: postman
  name: Square ApplePay OrderCustomAttributes API
  slug: postman-square-ordercustomattributes-api
- collection_type: postman
  name: Square ApplePay Orders API
  slug: postman-square-orders-api
- collection_type: postman
  name: Square ApplePay Payments API
  slug: postman-square-payments-api
- collection_type: postman
  name: Square ApplePay Payouts API
  slug: postman-square-payouts-api
- collection_type: postman
  name: Square ApplePay Refunds API
  slug: postman-square-refunds-api
- collection_type: postman
  name: Square ApplePay Sites API
  slug: postman-square-sites-api
- collection_type: postman
  name: Square ApplePay Snippets API
  slug: postman-square-snippets-api
- collection_type: postman
  name: Square ApplePay Subscriptions API
  slug: postman-square-subscriptions-api
- collection_type: postman
  name: Square ApplePay Team API
  slug: postman-square-team-api
- collection_type: postman
  name: Square ApplePay Terminal API
  slug: postman-square-terminal-api
- collection_type: postman
  name: Square ApplePay Transactions API
  slug: postman-square-transactions-api
- collection_type: postman
  name: Square ApplePay V1Transactions API
  slug: postman-square-v1transactions-api
- collection_type: postman
  name: Square ApplePay Vendors API
  slug: postman-square-vendors-api
- collection_type: postman
  name: Square ApplePay WebhookSubscriptions API
  slug: postman-square-webhooksubscriptions-api
- collection_type: open
  name: Square ApplePay API
  slug: open-square-applepay-api
- collection_type: open
  name: Square ApplePay BankAccounts API
  slug: open-square-bankaccounts-api
- collection_type: open
  name: Square ApplePay BookingCustomAttributes API
  slug: open-square-bookingcustomattributes-api
- collection_type: open
  name: Square ApplePay Bookings API
  slug: open-square-bookings-api
- collection_type: open
  name: Square ApplePay Cards API
  slug: open-square-cards-api
- collection_type: open
  name: Square ApplePay CashDrawers API
  slug: open-square-cashdrawers-api
- collection_type: open
  name: Square ApplePay Catalog API
  slug: open-square-catalog-api
- collection_type: open
  name: Square ApplePay Checkout API
  slug: open-square-checkout-api
- collection_type: open
  name: Square ApplePay CustomerCustomAttributes API
  slug: open-square-customercustomattributes-api
- collection_type: open
  name: Square ApplePay CustomerGroups API
  slug: open-square-customergroups-api
- collection_type: open
  name: Square ApplePay Customers API
  slug: open-square-customers-api
- collection_type: open
  name: Square ApplePay CustomerSegments API
  slug: open-square-customersegments-api
- collection_type: open
  name: Square ApplePay Devices API
  slug: open-square-devices-api
- collection_type: open
  name: Square ApplePay Disputes API
  slug: open-square-disputes-api
- collection_type: open
  name: Square ApplePay Employees API
  slug: open-square-employees-api
- collection_type: open
  name: Square ApplePay Events API
  slug: open-square-events-api
- collection_type: open
  name: Square ApplePay GiftCardActivities API
  slug: open-square-giftcardactivities-api
- collection_type: open
  name: Square ApplePay GiftCards API
  slug: open-square-giftcards-api
- collection_type: open
  name: Square ApplePay Inventory API
  slug: open-square-inventory-api
- collection_type: open
  name: Square ApplePay Invoices API
  slug: open-square-invoices-api
- collection_type: open
  name: Square ApplePay Labor API
  slug: open-square-labor-api
- collection_type: open
  name: Square ApplePay LocationCustomAttributes API
  slug: open-square-locationcustomattributes-api
- collection_type: open
  name: Square ApplePay Locations API
  slug: open-square-locations-api
- collection_type: open
  name: Square ApplePay Loyalty API
  slug: open-square-loyalty-api
- collection_type: open
  name: Square ApplePay MerchantCustomAttributes API
  slug: open-square-merchantcustomattributes-api
- collection_type: open
  name: Square ApplePay Merchants API
  slug: open-square-merchants-api
- collection_type: open
  name: Square ApplePay MobileAuthorization API
  slug: open-square-mobileauthorization-api
- collection_type: open
  name: Square ApplePay OAuth API
  slug: open-square-oauth-api
- collection_type: open
  name: Square ApplePay OrderCustomAttributes API
  slug: open-square-ordercustomattributes-api
- collection_type: open
  name: Square ApplePay Orders API
  slug: open-square-orders-api
- collection_type: open
  name: Square ApplePay Payments API
  slug: open-square-payments-api
- collection_type: open
  name: Square ApplePay Payouts API
  slug: open-square-payouts-api
- collection_type: open
  name: Square ApplePay Refunds API
  slug: open-square-refunds-api
- collection_type: open
  name: Square ApplePay Sites API
  slug: open-square-sites-api
- collection_type: open
  name: Square ApplePay Snippets API
  slug: open-square-snippets-api
- collection_type: open
  name: Square ApplePay Subscriptions API
  slug: open-square-subscriptions-api
- collection_type: open
  name: Square ApplePay Team API
  slug: open-square-team-api
- collection_type: open
  name: Square ApplePay Terminal API
  slug: open-square-terminal-api
- collection_type: open
  name: Square ApplePay Transactions API
  slug: open-square-transactions-api
- collection_type: open
  name: Square ApplePay V1Transactions API
  slug: open-square-v1transactions-api
- collection_type: open
  name: Square ApplePay Vendors API
  slug: open-square-vendors-api
- collection_type: open
  name: Square ApplePay WebhookSubscriptions API
  slug: open-square-webhooksubscriptions-api
- collection_type: open
  name: Square
  slug: open-square
common:
- group: design
  href: https://artifacts.apis.io/square/lifecycle/square-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/square-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/square/rules/square-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/square-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/square/rules/square-rules.yml
  title: ''
  type: Spectral
  url: rules/square-rules.yml
- group: design
  href: https://artifacts.apis.io/square/rules/square-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/square-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/square/rules/square-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/square-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/square/vocabulary/square-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/square-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/square/asyncapi/square-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/square-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/square/conventions/square-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/square-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://squareup.com/us/en/payments/secure
- group: design
  href: https://artifacts.apis.io/square/conformance/square-conformance.yml
  title: ''
  type: Conformance
  url: conformance/square-conformance.yml
- group: other
  href: https://artifacts.apis.io/square/overlays/square-apple-pay-api-phrasing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/square-apple-pay-api-phrasing-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/square/llms/square-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/square-llms.txt
- group: agent
  href: https://artifacts.apis.io/square/well-known/square-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/square-well-known.yml
- group: other
  href: https://artifacts.apis.io/square/hosts/square-hosts.yml
  title: ''
  type: Hosts
  url: hosts/square-hosts.yml
- group: build
  href: https://artifacts.apis.io/square/integrations/square-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/square-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/square/vendors/square-vendors.yml
  title: ''
  type: Vendors
  url: vendors/square-vendors.yml
- group: build
  href: https://artifacts.apis.io/square/packages/square-packages.yml
  title: ''
  type: Packages
  url: packages/square-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://squareup.com/signup
- group: company
  title: ''
  type: Newsroom
  url: https://community.squareup.com/t5/News/ct-p/news
- group: commercial
  title: ''
  type: Pricing
  url: https://squareup.com/us/en/pricing
- group: company
  title: ''
  type: Website
  url: https://www.squareup.com/
- group: other
  href: https://artifacts.apis.io/square/capabilities/square-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/square-capability-edges.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://developer.squareup.com/reference/square/deprecated
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/square/overview
- group: agent
  href: https://artifacts.apis.io/square/agentic-access/square-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/square-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/square/security/square-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/square-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/square/authentication/square-authentication.yml
  title: ''
  type: Authentication
  url: authentication/square-authentication.yml
- group: auth
  href: https://artifacts.apis.io/square/scopes/square-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/square-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/joinsquare
- group: start
  title: ''
  type: Portal
  url: https://developer.squareup.com/us/en
- group: docs
  title: ''
  type: Documentation
  url: https://developer.squareup.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.squareup.com/reference/square
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.squareup.com/docs/square-get-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.squareup.com/docs/oauth-api/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.squareup.com/docs/changelog/connect
- group: build
  title: ''
  type: SDKs
  url: https://developer.squareup.com/docs/sdks
- group: build
  title: ''
  type: SDKs
  url: https://developer.squareup.com/docs/devtools/postman
- group: design
  title: ''
  type: Webhooks
  url: https://developer.squareup.com/docs/webhooks/webhook-subscriptions-api
- group: docs
  href: https://artifacts.apis.io/square/asyncapi/square-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/square-webhooks-asyncapi.yml
- group: start
  title: ''
  type: Sandbox
  url: https://developer.squareup.com/docs/devtools/sandbox/overview
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.squareup.com/docs/build-basics/api-rate-limits
- group: docs
  title: ''
  type: Documentation
  url: https://developer.squareup.com/docs/build-basics/api-lifecycle
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.squareup.com/docs/buildbasics
- group: docs
  title: ''
  type: Documentation
  url: https://developer.squareup.com/docs/development-essentials
- group: start
  title: ''
  type: Console
  url: https://developer.squareup.com/explorer/square
- group: start
  title: ''
  type: Console
  url: https://developer.squareup.com/docs/devtools/developer-dashboard
- group: start
  title: ''
  type: Signup
  url: https://developer.squareup.com/apps
- group: company
  title: ''
  type: Blog
  url: https://developer.squareup.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://developer.squareup.com/forums/
- group: commercial
  title: ''
  type: Pricing
  url: https://squareup.com/us/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://squareup.com/us/en/legal/general/ua
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://squareup.com/us/en/legal/general/privacy
- group: operate
  title: ''
  type: Support
  url: https://squareup.com/help/us/en
- group: company
  title: ''
  type: Partners
  url: https://squareup.com/us/en/partnerships
- group: operate
  title: ''
  type: StatusPage
  url: https://www.issquareup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/square
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/square/connect-api-specification
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/square-connect
- group: other
  title: ''
  type: X
  url: https://x.com/SquareDev
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/squaredev
- group: docs
  href: https://artifacts.apis.io/square/json-schema/payment.json
  title: ''
  type: JSONSchema
  url: json-schema/payment.json
- group: docs
  href: https://artifacts.apis.io/square/json-schema/money.json
  title: ''
  type: JSONSchema
  url: json-schema/money.json
- group: docs
  href: https://artifacts.apis.io/square/json-schema/order.json
  title: ''
  type: JSONSchema
  url: json-schema/order.json
- group: docs
  href: https://artifacts.apis.io/square/json-schema/catalog-item.json
  title: ''
  type: JSONSchema
  url: json-schema/catalog-item.json
- group: docs
  href: https://artifacts.apis.io/square/json-schema/customer.json
  title: ''
  type: JSONSchema
  url: json-schema/customer.json
- group: docs
  href: https://artifacts.apis.io/square/json-schema/location.json
  title: ''
  type: JSONSchema
  url: json-schema/location.json
- group: docs
  href: https://artifacts.apis.io/square/json-schema/subscription.json
  title: ''
  type: JSONSchema
  url: json-schema/subscription.json
- group: design
  href: https://artifacts.apis.io/square/json-ld/square-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/square-context.jsonld
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/square-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/square-nodejs-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/square-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/square-dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/square-ruby-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/square-php-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/square-go-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/web-sdk
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/square/web-payments-quickstart
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/mobile-payments-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/mobile-payments-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/mobile-payments-sdk-flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/mobile-payments-sdk-react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/square/in-app-payments-react-native-plugin
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/square/in-app-payments-ios-quickstart
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/square/in-app-payments-android-quickstart
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/square/connect-api-specification
- group: design
  href: https://artifacts.apis.io/square/rules/square-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/square-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/square/vocabulary/square-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/square-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/square/square-mcp-server
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/square/square-mcp-server
- group: build
  title: Remote MCP Server (Hosted)
  type: Tools
  url: https://mcp.squareup.com/sse
- group: docs
  title: MCP Server Documentation
  type: Documentation
  url: https://developer.squareup.com/docs/mcp
- group: build
  title: MCP Server (npm)
  type: SDKs
  url: https://www.npmjs.com/package/square-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.squareup.com/llms.txt
- group: design
  href: https://artifacts.apis.io/square/json-structure/catalog-item-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/catalog-item-structure.json
- group: design
  href: https://artifacts.apis.io/square/json-structure/customer-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/customer-structure.json
- group: design
  href: https://artifacts.apis.io/square/json-structure/location-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/location-structure.json
- group: design
  href: https://artifacts.apis.io/square/json-structure/money-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/money-structure.json
- group: design
  href: https://artifacts.apis.io/square/json-structure/order-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/order-structure.json
- group: design
  href: https://artifacts.apis.io/square/json-structure/payment-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/payment-structure.json
- group: design
  href: https://artifacts.apis.io/square/json-structure/subscription-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/subscription-structure.json
- group: build
  href: https://artifacts.apis.io/square/examples/catalog-item-example.json
  title: ''
  type: Examples
  url: examples/catalog-item-example.json
- group: build
  href: https://artifacts.apis.io/square/examples/customer-example.json
  title: ''
  type: Examples
  url: examples/customer-example.json
- group: build
  href: https://artifacts.apis.io/square/examples/location-example.json
  title: ''
  type: Examples
  url: examples/location-example.json
- group: build
  href: https://artifacts.apis.io/square/examples/money-example.json
  title: ''
  type: Examples
  url: examples/money-example.json
- group: build
  href: https://artifacts.apis.io/square/examples/order-example.json
  title: ''
  type: Examples
  url: examples/order-example.json
- group: build
  href: https://artifacts.apis.io/square/examples/payment-example.json
  title: ''
  type: Examples
  url: examples/payment-example.json
- group: build
  href: https://artifacts.apis.io/square/examples/subscription-example.json
  title: ''
  type: Examples
  url: examples/subscription-example.json
- group: commercial
  href: https://artifacts.apis.io/square/plans/square-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/square-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/square/rate-limits/square-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/square-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/square/finops/square-finops.yml
  title: ''
  type: FinOps
  url: finops/square-finops.yml
- group: start
  href: https://artifacts.apis.io/square/sandbox/square-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/square-sandbox.yml
- group: design
  href: https://artifacts.apis.io/square/conventions/square-conventions.yml
  title: ''
  type: Conventions
  url: conventions/square-conventions.yml
- group: operate
  href: https://artifacts.apis.io/square/changelog/square-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/square-changelog.yml
- group: design
  href: https://artifacts.apis.io/square/components/square-components.yml
  title: ''
  type: Components
  url: components/square-components.yml
- group: design
  href: https://artifacts.apis.io/square/data-model/square-data-model.yml
  title: ''
  type: DataModel
  url: data-model/square-data-model.yml
- group: build
  href: https://artifacts.apis.io/square/errors/square-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/square-decline-codes.yml
- group: auth
  href: https://artifacts.apis.io/square/security/square-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/square-trust-center.yml
created: '2025-02-08'
description: Square provides APIs for payment processing, point of sale, and business management solutions enabling developers to build custom commerce applications.
examples:
- key_count: 19
  name: Catalog Item Example
  slug: catalog-item-example
- key_count: 19
  name: Customer Example
  slug: customer-example
- key_count: 27
  name: Location Example
  slug: location-example
- key_count: 2
  name: Money Example
  slug: money-example
- key_count: 29
  name: Order Example
  slug: order-example
- key_count: 38
  name: Payment Example
  slug: payment-example
- key_count: 19
  name: Subscription Example
  slug: subscription-example
features:
- 'Tap/dip/swipe: 2.6%+15¢ Free, 2.5%+15¢ Plus, 2.4%+15¢ Premium'
- 'Online (Square site): 3.3%+30¢ Free, 2.9%+30¢ Plus/Premium'
- 'Online API: 2.9%+30¢ all plans'
- 'Manual entry/card on file: 3.5%+15¢ all plans'
- 'ACH (invoice): 1% $1 min ($10 cap on Plus/Premium)'
- 'ACH (API): 1% $1 min, $5 cap'
- 'Afterpay BNPL: 6%+30¢'
- 'Cash/check: free'
- 'Bitcoin: 0% until 2027'
- 'International cards: +1.50% on top'
- Square Payments, POS, Online, Invoices, Subscriptions APIs
- Square Reader/Stand/Terminal/Register hardware
- Webhooks for transactions, customers, orders
- OAuth 2.0 + Personal access tokens
- Catalog API for items, categories, taxes, modifiers
- Customer Directory API
finops:
- has_sources: true
  method: derived
  name: Square Finops
  primary_unit: location
  service_category: ''
  slug: square-finops
  template: false
image: https://images.squarespace-cdn.com/content/v1/5e3b09f5e4e7d30f0b8c8e8f/square-logo.png
integrations:
- name: Apple Pay
- name: Google Pay
- name: Cash App Pay
- name: Afterpay
- name: QuickBooks
- name: WooCommerce
- name: Wix
- name: BigCommerce
json_schemas:
- name: Square Catalog Item
  property_count: 19
  slug: catalog-item
- name: Square Customer
  property_count: 19
  slug: customer
- name: Square Location
  property_count: 27
  slug: location
- name: Square Money
  property_count: 2
  slug: money
- name: Square Order
  property_count: 29
  slug: order
- name: Square Payment
  property_count: 38
  slug: payment
- name: AcceptDisputeResponse
  property_count: 2
  slug: square-accept-dispute-response
- name: BatchChangeInventoryRequest
  property_count: 3
  slug: square-batch-change-inventory-request
- name: BatchRetrieveCatalogObjectsResponse
  property_count: 3
  slug: square-batch-retrieve-catalog-objects-response
- name: BatchRetrieveInventoryChangesRequest
  property_count: 8
  slug: square-batch-retrieve-inventory-changes-request
- name: BatchRetrieveInventoryChangesResponse
  property_count: 3
  slug: square-batch-retrieve-inventory-changes-response
- name: BatchRetrieveInventoryCountsRequest
  property_count: 6
  slug: square-batch-retrieve-inventory-counts-request
- name: BatchUpsertCatalogObjectsRequest
  property_count: 2
  slug: square-batch-upsert-catalog-objects-request
- name: BatchUpsertCatalogObjectsResponse
  property_count: 4
  slug: square-batch-upsert-catalog-objects-response
- name: BulkCreateVendorsRequest
  property_count: 1
  slug: square-bulk-create-vendors-request
- name: BulkCreateVendorsResponse
  property_count: 2
  slug: square-bulk-create-vendors-response
- name: BulkRetrieveBookingsResponse
  property_count: 2
  slug: square-bulk-retrieve-bookings-response
- name: BulkRetrieveTeamMemberBookingProfilesResponse
  property_count: 2
  slug: square-bulk-retrieve-team-member-booking-profiles-response
- name: BulkRetrieveVendorsResponse
  property_count: 2
  slug: square-bulk-retrieve-vendors-response
- name: BulkUpdateTeamMembersRequest
  property_count: 1
  slug: square-bulk-update-team-members-request
- name: BulkUpdateTeamMembersResponse
  property_count: 2
  slug: square-bulk-update-team-members-response
- name: BulkUpdateVendorsResponse
  property_count: 2
  slug: square-bulk-update-vendors-response
- name: BulkUpsertBookingCustomAttributesResponse
  property_count: 2
  slug: square-bulk-upsert-booking-custom-attributes-response
- name: BulkUpsertCustomerCustomAttributesRequest
  property_count: 1
  slug: square-bulk-upsert-customer-custom-attributes-request
- name: BulkUpsertCustomerCustomAttributesResponse
  property_count: 2
  slug: square-bulk-upsert-customer-custom-attributes-response
- name: BulkUpsertLocationCustomAttributesResponse
  property_count: 2
  slug: square-bulk-upsert-location-custom-attributes-response
- name: BulkUpsertMerchantCustomAttributesResponse
  property_count: 2
  slug: square-bulk-upsert-merchant-custom-attributes-response
- name: BulkUpsertOrderCustomAttributesResponse
  property_count: 2
  slug: square-bulk-upsert-order-custom-attributes-response
- name: CalculateLoyaltyPointsRequest
  property_count: 3
  slug: square-calculate-loyalty-points-request
- name: CalculateOrderResponse
  property_count: 2
  slug: square-calculate-order-response
- name: CancelInvoiceResponse
  property_count: 2
  slug: square-cancel-invoice-response
- name: CaptureTransactionResponse
  property_count: 1
  slug: square-capture-transaction-response
- name: ChangeBillingAnchorDateResponse
  property_count: 3
  slug: square-change-billing-anchor-date-response
- name: CloneOrderResponse
  property_count: 2
  slug: square-clone-order-response
- name: CompletePaymentResponse
  property_count: 2
  slug: square-complete-payment-response
- name: CreateBookingCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-create-booking-custom-attribute-definition-request
- name: CreateCardRequest
  property_count: 4
  slug: square-create-card-request
- name: CreateCardResponse
  property_count: 2
  slug: square-create-card-response
- name: CreateCheckoutRequest
  property_count: 9
  slug: square-create-checkout-request
- name: CreateCheckoutResponse
  property_count: 2
  slug: square-create-checkout-response
- name: CreateCustomerCardRequest
  property_count: 4
  slug: square-create-customer-card-request
- name: CreateCustomerCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-create-customer-custom-attribute-definition-request
- name: CreateCustomerGroupRequest
  property_count: 2
  slug: square-create-customer-group-request
- name: CreateCustomerGroupResponse
  property_count: 2
  slug: square-create-customer-group-response
- name: CreateCustomerRequest
  property_count: 12
  slug: square-create-customer-request
- name: CreateDeviceCodeRequest
  property_count: 2
  slug: square-create-device-code-request
- name: CreateDeviceCodeResponse
  property_count: 2
  slug: square-create-device-code-response
- name: CreateDisputeEvidenceTextRequest
  property_count: 3
  slug: square-create-dispute-evidence-text-request
- name: CreateGiftCardActivityRequest
  property_count: 2
  slug: square-create-gift-card-activity-request
- name: CreateGiftCardActivityResponse
  property_count: 2
  slug: square-create-gift-card-activity-response
- name: CreateGiftCardRequest
  property_count: 3
  slug: square-create-gift-card-request
- name: CreateInvoiceResponse
  property_count: 2
  slug: square-create-invoice-response
- name: CreateLocationCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-create-location-custom-attribute-definition-request
- name: CreateLocationRequest
  property_count: 1
  slug: square-create-location-request
- name: CreateLocationResponse
  property_count: 2
  slug: square-create-location-response
- name: CreateMerchantCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-create-merchant-custom-attribute-definition-request
- name: CreateMobileAuthorizationCodeRequest
  property_count: 1
  slug: square-create-mobile-authorization-code-request
- name: CreateMobileAuthorizationCodeResponse
  property_count: 3
  slug: square-create-mobile-authorization-code-response
- name: CreateOrderCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-create-order-custom-attribute-definition-request
- name: CreateOrderResponse
  property_count: 2
  slug: square-create-order-response
- name: CreatePaymentLinkRequest
  property_count: 7
  slug: square-create-payment-link-request
- name: CreatePaymentLinkResponse
  property_count: 3
  slug: square-create-payment-link-response
- name: CreatePaymentRequest
  property_count: 25
  slug: square-create-payment-request
- name: CreatePaymentResponse
  property_count: 2
  slug: square-create-payment-response
- name: CreateShiftResponse
  property_count: 2
  slug: square-create-shift-response
- name: CreateSubscriptionRequest
  property_count: 13
  slug: square-create-subscription-request
- name: CreateTeamMemberRequest
  property_count: 2
  slug: square-create-team-member-request
- name: CreateTeamMemberResponse
  property_count: 2
  slug: square-create-team-member-response
- name: CreateVendorRequest
  property_count: 2
  slug: square-create-vendor-request
- name: CreateWebhookSubscriptionResponse
  property_count: 2
  slug: square-create-webhook-subscription-response
- name: DeleteSnippetResponse
  property_count: 1
  slug: square-delete-snippet-response
- name: DisableCardResponse
  property_count: 2
  slug: square-disable-card-response
- name: DisableEventsResponse
  property_count: 1
  slug: square-disable-events-response
- name: DismissTerminalCheckoutResponse
  property_count: 2
  slug: square-dismiss-terminal-checkout-response
- name: DismissTerminalRefundResponse
  property_count: 2
  slug: square-dismiss-terminal-refund-response
- name: EnableEventsResponse
  property_count: 1
  slug: square-enable-events-response
- name: GetBankAccountByV1IdResponse
  property_count: 2
  slug: square-get-bank-account-by-v1-id-response
- name: GetBankAccountResponse
  property_count: 2
  slug: square-get-bank-account-response
- name: GetDeviceCodeResponse
  property_count: 2
  slug: square-get-device-code-response
- name: GetDeviceResponse
  property_count: 2
  slug: square-get-device-response
- name: GetInvoiceResponse
  property_count: 2
  slug: square-get-invoice-response
- name: GetPaymentRefundResponse
  property_count: 2
  slug: square-get-payment-refund-response
- name: GetPaymentResponse
  property_count: 2
  slug: square-get-payment-response
- name: GetPayoutResponse
  property_count: 2
  slug: square-get-payout-response
- name: GetShiftResponse
  property_count: 2
  slug: square-get-shift-response
- name: GetTerminalRefundResponse
  property_count: 2
  slug: square-get-terminal-refund-response
- name: LinkCustomerToGiftCardResponse
  property_count: 2
  slug: square-link-customer-to-gift-card-response
- name: ListBankAccountsResponse
  property_count: 3
  slug: square-list-bank-accounts-response
- name: ListBookingCustomAttributeDefinitionsResponse
  property_count: 3
  slug: square-list-booking-custom-attribute-definitions-response
- name: ListBookingCustomAttributesResponse
  property_count: 3
  slug: square-list-booking-custom-attributes-response
- name: ListBookingsResponse
  property_count: 3
  slug: square-list-bookings-response
- name: ListCardsResponse
  property_count: 3
  slug: square-list-cards-response
- name: ListCashDrawerShiftEventsResponse
  property_count: 3
  slug: square-list-cash-drawer-shift-events-response
- name: ListCustomerCustomAttributeDefinitionsResponse
  property_count: 3
  slug: square-list-customer-custom-attribute-definitions-response
- name: ListCustomerCustomAttributesResponse
  property_count: 3
  slug: square-list-customer-custom-attributes-response
- name: ListCustomerGroupsResponse
  property_count: 3
  slug: square-list-customer-groups-response
- name: ListCustomerSegmentsResponse
  property_count: 3
  slug: square-list-customer-segments-response
- name: ListCustomersResponse
  property_count: 4
  slug: square-list-customers-response
- name: ListDeviceCodesResponse
  property_count: 3
  slug: square-list-device-codes-response
- name: ListDevicesResponse
  property_count: 3
  slug: square-list-devices-response
- name: ListDisputeEvidenceResponse
  property_count: 3
  slug: square-list-dispute-evidence-response
- name: ListDisputesResponse
  property_count: 3
  slug: square-list-disputes-response
- name: ListEmployeeWagesResponse
  property_count: 3
  slug: square-list-employee-wages-response
- name: ListEmployeesResponse
  property_count: 3
  slug: square-list-employees-response
- name: ListEventTypesResponse
  property_count: 3
  slug: square-list-event-types-response
- name: ListGiftCardActivitiesResponse
  property_count: 3
  slug: square-list-gift-card-activities-response
- name: ListGiftCardsResponse
  property_count: 3
  slug: square-list-gift-cards-response
- name: ListInvoicesResponse
  property_count: 3
  slug: square-list-invoices-response
- name: ListLocationCustomAttributeDefinitionsResponse
  property_count: 3
  slug: square-list-location-custom-attribute-definitions-response
- name: ListLocationCustomAttributesResponse
  property_count: 3
  slug: square-list-location-custom-attributes-response
- name: ListLocationsResponse
  property_count: 2
  slug: square-list-locations-response
- name: ListLoyaltyProgramsResponse
  property_count: 2
  slug: square-list-loyalty-programs-response
- name: ListLoyaltyPromotionsResponse
  property_count: 3
  slug: square-list-loyalty-promotions-response
- name: ListMerchantCustomAttributeDefinitionsResponse
  property_count: 3
  slug: square-list-merchant-custom-attribute-definitions-response
- name: ListMerchantCustomAttributesResponse
  property_count: 3
  slug: square-list-merchant-custom-attributes-response
- name: ListMerchantsResponse
  property_count: 3
  slug: square-list-merchants-response
- name: ListOrderCustomAttributeDefinitionsResponse
  property_count: 3
  slug: square-list-order-custom-attribute-definitions-response
- name: ListOrderCustomAttributesResponse
  property_count: 3
  slug: square-list-order-custom-attributes-response
- name: ListPaymentLinksResponse
  property_count: 3
  slug: square-list-payment-links-response
- name: ListPaymentRefundsResponse
  property_count: 3
  slug: square-list-payment-refunds-response
- name: ListPaymentsResponse
  property_count: 3
  slug: square-list-payments-response
- name: ListPayoutEntriesResponse
  property_count: 3
  slug: square-list-payout-entries-response
- name: ListPayoutsResponse
  property_count: 3
  slug: square-list-payouts-response
- name: ListSitesResponse
  property_count: 2
  slug: square-list-sites-response
- name: ListSubscriptionEventsResponse
  property_count: 3
  slug: square-list-subscription-events-response
- name: ListTeamMemberBookingProfilesResponse
  property_count: 3
  slug: square-list-team-member-booking-profiles-response
- name: ListTeamMemberWagesResponse
  property_count: 3
  slug: square-list-team-member-wages-response
- name: ListTransactionsResponse
  property_count: 3
  slug: square-list-transactions-response
- name: ListWebhookEventTypesResponse
  property_count: 3
  slug: square-list-webhook-event-types-response
- name: ListWebhookSubscriptionsResponse
  property_count: 3
  slug: square-list-webhook-subscriptions-response
- name: ObtainTokenRequest
  property_count: 10
  slug: square-obtain-token-request
- name: ObtainTokenResponse
  property_count: 11
  slug: square-obtain-token-response
- name: PauseSubscriptionRequest
  property_count: 5
  slug: square-pause-subscription-request
- name: PayOrderResponse
  property_count: 2
  slug: square-pay-order-response
- name: PublishInvoiceResponse
  property_count: 2
  slug: square-publish-invoice-response
- name: RefundPaymentRequest
  property_count: 13
  slug: square-refund-payment-request
- name: RefundPaymentResponse
  property_count: 2
  slug: square-refund-payment-response
- name: RegisterDomainRequest
  property_count: 1
  slug: square-register-domain-request
- name: RegisterDomainResponse
  property_count: 2
  slug: square-register-domain-response
- name: RetrieveCardResponse
  property_count: 2
  slug: square-retrieve-card-response
- name: RetrieveCashDrawerShiftResponse
  property_count: 2
  slug: square-retrieve-cash-drawer-shift-response
- name: RetrieveCustomerGroupResponse
  property_count: 2
  slug: square-retrieve-customer-group-response
- name: RetrieveCustomerSegmentResponse
  property_count: 2
  slug: square-retrieve-customer-segment-response
- name: RetrieveDisputeResponse
  property_count: 2
  slug: square-retrieve-dispute-response
- name: RetrieveEmployeeResponse
  property_count: 2
  slug: square-retrieve-employee-response
- name: RetrieveGiftCardFromGANResponse
  property_count: 2
  slug: square-retrieve-gift-card-from-ganresponse
- name: RetrieveGiftCardFromNonceResponse
  property_count: 2
  slug: square-retrieve-gift-card-from-nonce-response
- name: RetrieveInventoryAdjustmentResponse
  property_count: 2
  slug: square-retrieve-inventory-adjustment-response
- name: RetrieveInventoryChangesResponse
  property_count: 3
  slug: square-retrieve-inventory-changes-response
- name: RetrieveLocationResponse
  property_count: 2
  slug: square-retrieve-location-response
- name: RetrieveLoyaltyProgramResponse
  property_count: 2
  slug: square-retrieve-loyalty-program-response
- name: RetrieveMerchantResponse
  property_count: 2
  slug: square-retrieve-merchant-response
- name: RetrieveOrderResponse
  property_count: 2
  slug: square-retrieve-order-response
- name: RetrieveSnippetResponse
  property_count: 2
  slug: square-retrieve-snippet-response
- name: RetrieveTokenStatusResponse
  property_count: 5
  slug: square-retrieve-token-status-response
- name: RetrieveTransactionResponse
  property_count: 2
  slug: square-retrieve-transaction-response
- name: RetrieveWebhookSubscriptionResponse
  property_count: 2
  slug: square-retrieve-webhook-subscription-response
- name: RevokeTokenRequest
  property_count: 4
  slug: square-revoke-token-request
- name: RevokeTokenResponse
  property_count: 2
  slug: square-revoke-token-response
- name: SearchAvailabilityResponse
  property_count: 2
  slug: square-search-availability-response
- name: SearchCatalogItemsRequest
  property_count: 10
  slug: square-search-catalog-items-request
- name: SearchCatalogObjectsRequest
  property_count: 8
  slug: square-search-catalog-objects-request
- name: SearchCatalogObjectsResponse
  property_count: 5
  slug: square-search-catalog-objects-response
- name: SearchCustomersRequest
  property_count: 4
  slug: square-search-customers-request
- name: SearchCustomersResponse
  property_count: 4
  slug: square-search-customers-response
- name: SearchEventsRequest
  property_count: 3
  slug: square-search-events-request
- name: SearchEventsResponse
  property_count: 4
  slug: square-search-events-response
- name: SearchInvoicesResponse
  property_count: 3
  slug: square-search-invoices-response
- name: SearchLoyaltyEventsResponse
  property_count: 3
  slug: square-search-loyalty-events-response
- name: SearchLoyaltyRewardsResponse
  property_count: 3
  slug: square-search-loyalty-rewards-response
- name: SearchShiftsResponse
  property_count: 3
  slug: square-search-shifts-response
- name: SearchSubscriptionsRequest
  property_count: 4
  slug: square-search-subscriptions-request
- name: SearchSubscriptionsResponse
  property_count: 3
  slug: square-search-subscriptions-response
- name: SearchTeamMembersResponse
  property_count: 3
  slug: square-search-team-members-response
- name: SearchTerminalActionsResponse
  property_count: 3
  slug: square-search-terminal-actions-response
- name: SearchTerminalCheckoutsResponse
  property_count: 3
  slug: square-search-terminal-checkouts-response
- name: SearchTerminalRefundsResponse
  property_count: 3
  slug: square-search-terminal-refunds-response
- name: SearchVendorsResponse
  property_count: 3
  slug: square-search-vendors-response
- name: SubmitEvidenceResponse
  property_count: 2
  slug: square-submit-evidence-response
- name: TestWebhookSubscriptionResponse
  property_count: 2
  slug: square-test-webhook-subscription-response
- name: UnlinkCustomerFromGiftCardResponse
  property_count: 2
  slug: square-unlink-customer-from-gift-card-response
- name: UpdateBookingCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-update-booking-custom-attribute-definition-request
- name: UpdateBookingResponse
  property_count: 2
  slug: square-update-booking-response
- name: UpdateCustomerCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-update-customer-custom-attribute-definition-request
- name: UpdateCustomerGroupRequest
  property_count: 1
  slug: square-update-customer-group-request
- name: UpdateCustomerGroupResponse
  property_count: 2
  slug: square-update-customer-group-response
- name: UpdateCustomerRequest
  property_count: 12
  slug: square-update-customer-request
- name: UpdateLocationCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-update-location-custom-attribute-definition-request
- name: UpdateLocationRequest
  property_count: 1
  slug: square-update-location-request
- name: UpdateLocationResponse
  property_count: 2
  slug: square-update-location-response
- name: UpdateLocationSettingsResponse
  property_count: 2
  slug: square-update-location-settings-response
- name: UpdateMerchantCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-update-merchant-custom-attribute-definition-request
- name: UpdateOrderCustomAttributeDefinitionRequest
  property_count: 2
  slug: square-update-order-custom-attribute-definition-request
- name: UpdatePaymentResponse
  property_count: 2
  slug: square-update-payment-response
- name: UpdateShiftResponse
  property_count: 2
  slug: square-update-shift-response
- name: UpdateTeamMemberResponse
  property_count: 2
  slug: square-update-team-member-response
- name: UpdateWebhookSubscriptionResponse
  property_count: 2
  slug: square-update-webhook-subscription-response
- name: UpsertBookingCustomAttributeRequest
  property_count: 2
  slug: square-upsert-booking-custom-attribute-request
- name: UpsertLocationCustomAttributeRequest
  property_count: 2
  slug: square-upsert-location-custom-attribute-request
- name: UpsertMerchantCustomAttributeRequest
  property_count: 2
  slug: square-upsert-merchant-custom-attribute-request
- name: UpsertOrderCustomAttributeRequest
  property_count: 2
  slug: square-upsert-order-custom-attribute-request
- name: UpsertSnippetRequest
  property_count: 1
  slug: square-upsert-snippet-request
- name: UpsertSnippetResponse
  property_count: 2
  slug: square-upsert-snippet-response
- name: V1Order
  property_count: 25
  slug: square-v1-order
- name: V1UpdateOrderRequest
  property_count: 5
  slug: square-v1-update-order-request
- name: VoidTransactionResponse
  property_count: 1
  slug: square-void-transaction-response
- name: Square Subscription
  property_count: 19
  slug: subscription
json_structures:
- name: Catalog Item Structure
  property_count: 19
  slug: catalog-item-structure
- name: Customer Structure
  property_count: 19
  slug: customer-structure
- name: Location Structure
  property_count: 27
  slug: location-structure
- name: Money Structure
  property_count: 2
  slug: money-structure
- name: Order Structure
  property_count: 29
  slug: order-structure
- name: Payment Structure
  property_count: 38
  slug: payment-structure
- name: Subscription Structure
  property_count: 19
  slug: subscription-structure
jsonld:
- class_count: 0
  name: Square Context
  property_count: 10
  slug: square-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Remote MCP server at mcp.squareup.com over HTTP.
  name: Square MCP Server
  slug: square
modified: '2026-06-03'
name: Square
nav: Providers
network: true
overview: 'Square publishes 45 API contracts indexed on the [APIs.io](https://apis.io/) network, including BookingCustomAttributes API, Bookings API, Cards API, and 42 more. Tagged areas include Booking, Location, Square, Restaurant, and Catalog.


  The Square catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 4 Spectral governance rulesets.


  Square''s developer surface includes signup flow, pricing, authentication, developer portal, documentation, API reference, getting-started guide, and 110 more developer resources.'
plans:
- name: Square Plans Pricing
  plan_count: 4
  slug: square-plans-pricing
- name: Square Price Estimates
  plan_count: 0
  slug: square-price-estimates
random_paper: 9
rate_limits:
- limit_count: 0
  name: Square Rate Limits
  slug: square-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Square — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: square-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Square — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: square-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Square API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 2
  slug: square-rules
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Square API Rules
  rule_count: 36
  severity_counts:
    error: 8
    hint: 0
    info: 9
    warn: 19
  slug: square-spectral-rules
scopes:
- name: Square Scopes
  scope_count: 58
  slug: square-scopes
  summary_line: 58 scopes · authorizationCode
score:
  band: exemplar
  composite: 76.1
  coverage:
    artifact_dirs: 40
    catalog_earned: 68.0
    catalog_earned_first_party: 12.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 72.9
    developer_ergonomics: 82.1
    discoverability: 59.2
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 79.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/square/square-2026-06-20T194428.png
security:
- kind: authentication
  name: Square Authentication
  slug: square-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Square Domain Security
  slug: square-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Square Trust Center
  slug: square-trust-center
  summary_line: PCI DSS, PCI SAQ A, ISO 27001, EMVCo
slug: square
tags:
- Booking
- Location
- Square
- Restaurant
- Catalog
- Checkout
- Customers
- Disputes
- E-Commerce
- Financial Technology
- Gift Cards
- Inventory
- Invoicing
- Labor
- Loyalty
- Merchants
- Order
- Payments
- Point-of-Sale
- Refunds
- Retail
- Subscription
- Team
- Webhook
- Payment Processing
- Payment Terminals
use_cases:
- name: Accept Payments Online
- name: Build Custom POS Systems
- name: Manage Product Catalogs
- name: Track Inventory Across Locations
- name: Create Loyalty and Rewards Programs
- name: Send and Manage Invoices
- name: Schedule Appointments and Bookings
- name: Manage Team Members and Labor
- name: Process Refunds and Disputes
- name: Sell Gift Cards
- name: Set Up Recurring Subscriptions
website: https://www.squareup.com/
---
