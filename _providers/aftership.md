---
access_model:
  confidence: high
  label: Public, self-service with a free tier; API access begins on the Premium tier
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.aftership.com/pricing
  - plans/aftership-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 85
  human_in_the_loop: 0
  name: Aftership Agentic Access
  operation_count: 131
  slug: aftership-agentic-access
  summary_line: 131 operations · 85 acting
api_count: 7
apis:
- baseURL: https://api.aftership.com/address/2024-07/
  baseurl_source: declared
  description: Address validation and correction so packages are delivered to a deliverable, normalized address.
  name: AfterShip Address API
  phrasing_intents:
  - id: post-addresses/validate
    intent: Validate and standardize a shipping address
    question: How do I check that a shipping address is valid before I print a label?
  phrasing_ops: 1
  slug: aftership-address-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Address Validations (Beta) API from AfterShip — 1 operation(s) for address validations (beta).
  name: AfterShip Address Validations (Beta) API
  phrasing_intents:
  - id: post-address-validations
    intent: Create a beta address validation
    question: Can I run an address through the beta address validation check?
  phrasing_ops: 1
  slug: aftership-address-validations-beta-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Cancel Labels API from AfterShip — 2 operation(s) for cancel labels.
  name: AfterShip Cancel Labels API
  phrasing_intents:
  - id: get-cancel-labels
    intent: List cancelled shipping labels
    question: How do I see all the shipping labels I've cancelled?
  - id: post-cancel-labels
    intent: Cancel a shipping label
    question: How do I void a shipping label I no longer need?
  - id: get-cancel-label
    intent: Get one cancelled label's details
    question: What is the status of a specific label cancellation request?
  phrasing_ops: 3
  slug: aftership-cancel-labels-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Cancel Pickups API from AfterShip — 2 operation(s) for cancel pickups.
  name: AfterShip Cancel Pickups API
  phrasing_intents:
  - id: get-cancel-pickups
    intent: List cancelled carrier pickups
    question: How do I see every carrier pickup I've cancelled?
  - id: post-cancel-pickups
    intent: Cancel a scheduled carrier pickup
    question: How do I cancel a courier pickup I scheduled?
  - id: get-cancel-pickup
    intent: Get one cancelled pickup's details
    question: What happened to a specific pickup cancellation request?
  phrasing_ops: 3
  slug: aftership-cancel-pickups-api
- baseURL: https://api.aftership.com/warranty/2026-07
  baseurl_source: declared
  description: Public endpoints for updating item-level claim data.
  name: AfterShip Claim Items API
  phrasing_intents:
  - id: update-claim-item
    intent: Update tags or images on a claim item
    question: How do I add item tags to one item within a claim?
  phrasing_ops: 1
  slug: aftership-claim-items-api
- baseURL: https://api.aftership.com/warranty/2026-07
  baseurl_source: declared
  description: Public endpoints for creating and polling claim shipment resources.
  name: AfterShip Claim Shipments API
  phrasing_intents:
  - id: create-claim-shipment
    intent: Create a shipment for a claim
    question: How do I send a replacement shipment for an approved claim?
  - id: get-claim-shipment
    intent: Check a claim shipment and its label status
    question: Has the label for my claim shipment finished generating yet?
  phrasing_ops: 2
  slug: aftership-claim-shipments-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Claims API from AfterShip — 10 operation(s) for claims.
  name: AfterShip Claims API
  phrasing_intents:
  - id: get-claims
    intent: List shipping protection claims
    question: How do I see all claims filed against my shipping protection?
  - id: get-claim-id
    intent: Get a claim by its ID
    question: Can I look up a claim using its ID from the claims list?
  - id: get-claim
    intent: Retrieve the full Claim resource
    question: What does the full Claim resource show for a single claim?
  - id: patch-claim
    intent: Update a claim's note, email or address
    question: Can I change the contact email on a claim?
  - id: approve-claim
    intent: Approve a claim under review
    question: How do I approve a claim that's still under review?
  - id: reject-claim
    intent: Reject a claim under review
    question: Can I decline a claim and give the customer a reason?
  - id: cancel-claim
    intent: Cancel an approved or in-process claim
    question: How do I cancel a claim that was already approved?
  - id: resolve-claim
    intent: Mark an in-process claim as resolved
    question: How do I close out a claim once it has been fully handled?
  phrasing_ops: 11
  slug: aftership-claims-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: The Courier API from AfterShip — 2 operation(s) for courier.
  name: AfterShip Courier API
  phrasing_intents:
  - id: detect-courier
    intent: Detect the courier for a tracking number
    question: Which courier does this tracking number belong to?
  phrasing_ops: 1
  slug: aftership-courier-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: The Courier connection API from AfterShip — 2 operation(s) for courier connection.
  name: AfterShip Courier connection API
  phrasing_intents:
  - id: get-courier-connections
    intent: List courier connections
    question: How do I see all the carrier accounts I've connected for tracking?
  - id: post-courier-connections
    intent: Connect a courier account with credentials
    question: How do I connect my own carrier account so tracking uses its credentials?
  - id: get-courier-connections-by-id
    intent: Get one courier connection
    question: What are the details of a single courier connection?
  - id: put-courier-connections-by-id
    intent: Update a courier connection's credentials
    question: How do I update the credentials on an existing courier connection?
  - id: delete-courier-connections-by-id
    intent: Delete a courier connection
    question: How do I disconnect a carrier account I no longer use?
  phrasing_ops: 5
  slug: aftership-courier-connection-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Couriers API from AfterShip — 1 operation(s) for couriers.
  name: AfterShip Couriers API
  phrasing_intents:
  - id: get-couriers
    intent: List all supported couriers
    question: Which couriers does AfterShip support for tracking?
  phrasing_ops: 1
  slug: aftership-couriers-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Coverages API from AfterShip — 5 operation(s) for coverages.
  name: AfterShip Coverages API
  phrasing_intents:
  - id: get-coverages
    intent: List shipping protection coverages
    question: How do I see all the shipping protection coverages I've issued?
  - id: post-coverage
    intent: Create shipping protection coverage for an order
    question: How do I add shipping protection to a new order?
  - id: get-coverage-id
    intent: Get a coverage by ID
    question: What's the status of a specific shipping protection coverage?
  - id: post-coverage-id-update-tracking
    intent: Add tracking info to a coverage
    question: How do I attach tracking information to a coverage so it becomes active?
  - id: post-coverage-void
    intent: Void an inactive coverage
    question: How do I void a coverage so it won't be charged?
  - id: post-coverage-calculate
    intent: Calculate a shipping protection premium
    question: How much would shipping protection cost for an order of a given value?
  phrasing_ops: 6
  slug: aftership-coverages-api
- baseURL: https://api.aftership.com/personalization/2025-01
  baseurl_source: declared
  description: The Discoveries API from AfterShip — 4 operation(s) for discoveries.
  name: AfterShip Discoveries API
  phrasing_intents:
  - id: post-discoveries-recommend
    intent: Recommend products to a shopper
    question: How do I show 'you may also like' product recommendations in my store?
  - id: post-discoveries-suggest
    intent: Suggest search queries as a shopper types
    question: Can I show autocomplete suggestions while a shopper types in my store search box?
  - id: post-discoveries-search
    intent: Search a store's products by text or image
    question: How do I search my store catalog by keyword?
  - id: post-discoveries-tagging
    intent: Predict a product's category and tags
    question: Can AI suggest a category and tags for a product I'm listing?
  phrasing_ops: 4
  slug: aftership-discoveries-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Email Parses API from AfterShip — 2 operation(s) for email parses.
  name: AfterShip Email Parses API
  phrasing_intents:
  - id: email-parses-v2
    intent: Parse order and tracking details from an email (V2)
    question: Can I extract tracking numbers from a raw shipping confirmation email's headers and body?
  - id: email-parses
    intent: Parse order details from an email subject and sender
    question: How do I pull tracking info out of an email using just its subject and sender?
  phrasing_ops: 2
  slug: aftership-email-parses-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: The Estimated delivery date API from AfterShip — 2 operation(s) for estimated delivery date.
  name: AfterShip Estimated delivery date API
  phrasing_intents:
  - id: predict
    intent: Predict delivery date for one shipment
    question: When will a package shipped with a given carrier likely arrive?
  - id: predict-batch
    intent: Predict delivery dates for many shipments
    question: Can I get estimated delivery dates for several shipments in one request?
  phrasing_ops: 2
  slug: aftership-estimated-delivery-date-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Fulfillments API from AfterShip — 3 operation(s) for fulfillments.
  name: AfterShip Fulfillments API
  phrasing_intents:
  - id: create-fulfillment
    intent: Create a fulfillment for an order
    question: How do I record that part of an order has shipped?
  - id: get-fulfillments
    intent: List fulfillments for an order
    question: How do I see all fulfillments for an order?
  - id: get-fulfillment-by-id
    intent: Get a fulfillment by ID
    question: What are the details of one specific fulfillment?
  - id: update-fulfillment-by-id
    intent: Update a fulfillment's tracking or pickup info
    question: How do I add tracking numbers to an existing fulfillment?
  - id: update-fulfillment-status
    intent: Move a fulfillment to its next status
    question: What order do fulfillment statuses have to be updated in?
  phrasing_ops: 5
  slug: aftership-fulfillments-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Item tags API from AfterShip — 1 operation(s) for item tags.
  name: AfterShip Item tags API
  phrasing_intents:
  - id: list-item-tags
    intent: List tags available for claim items
    question: Which item tags can I apply to claim items?
  phrasing_ops: 1
  slug: aftership-item-tags-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Labels API from AfterShip — 2 operation(s) for labels.
  name: AfterShip Labels API
  phrasing_intents:
  - id: get-labels
    intent: List shipping labels
    question: How do I see all the shipping labels I've created?
  - id: post-labels
    intent: Create a shipping label
    question: How do I print a shipping label for a package?
  - id: get-label
    intent: Get a shipping label by ID
    question: Can I retrieve a label I already created, including its file?
  phrasing_ops: 3
  slug: aftership-labels-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Locations API from AfterShip — 2 operation(s) for locations.
  name: AfterShip Locations API
  phrasing_intents:
  - id: create-location
    intent: Create a manual location
    question: How do I add a new warehouse or pickup location?
  - id: get-locations
    intent: List store and warehouse locations
    question: How do I see all my warehouse and store locations?
  - id: get-location-by-id
    intent: Get a location by ID
    question: What are the details of one of my locations?
  - id: update-location-by-id
    intent: Update a location's details
    question: How do I change the opening hours of an existing location?
  phrasing_ops: 4
  slug: aftership-locations-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Manifests API from AfterShip — 2 operation(s) for manifests.
  name: AfterShip Manifests API
  phrasing_intents:
  - id: get-manifests
    intent: List shipping manifests
    question: How do I see the end-of-day manifests I've created?
  - id: post-manifests
    intent: Create a manifest for labels
    question: How do I create an end-of-day manifest for my labels?
  - id: get-manifest
    intent: Get a manifest by ID
    question: What's in a specific manifest?
  phrasing_ops: 3
  slug: aftership-manifests-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Memberships API from AfterShip — 2 operation(s) for memberships.
  name: AfterShip Memberships API
  phrasing_intents:
  - id: get-memberships
    intent: List organization memberships
    question: Who are the members of my AfterShip organization?
  - id: post-memberships
    intent: Add a member with a role
    question: How do I invite a teammate into my organization?
  - id: get-memberships-id
    intent: Get a membership by ID
    question: What role does a particular member have?
  - id: patch-memberships-:id
    intent: Change a member's role
    question: How do I change what role a teammate has?
  - id: delete-memberships-:id
    intent: Remove a member from the organization
    question: How do I remove someone from my organization?
  phrasing_ops: 5
  slug: aftership-memberships-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Orders API from AfterShip — 4 operation(s) for orders.
  name: AfterShip Orders API
  phrasing_intents:
  - id: create-order
    intent: Create an order
    question: How do I push a new order into AfterShip for tracking and returns?
  - id: get-orders
    intent: List orders in a store
    question: How do I pull a list of orders from my store?
  - id: get-order-by-id
    intent: Get an order by ID
    question: What are the details of a specific order?
  - id: update-order-by-id
    intent: Update an order's details or status
    question: Can I change the shipping address on an order I already created?
  - id: create-order-item
    intent: Add a line item to an order
    question: How do I add another product line to an existing order?
  - id: get-order-item
    intent: Get one line item from an order
    question: What are the details of a single item within an order?
  - id: update-order-item
    intent: Update an order line item
    question: Can I change the quantity of an item on an order?
  - id: delete-order-item
    intent: Delete a line item from an order
    question: How do I remove a product line from an order?
  phrasing_ops: 8
  slug: aftership-orders-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Pickups API from AfterShip — 2 operation(s) for pickups.
  name: AfterShip Pickups API
  phrasing_intents:
  - id: get-pickups
    intent: List carrier pickups
    question: How do I see all the carrier pickups I've scheduled?
  - id: post-pickups
    intent: Schedule a carrier pickup
    question: How do I book a courier to collect my parcels?
  - id: get-pickup
    intent: Get a pickup by ID
    question: Is my scheduled pickup confirmed?
  phrasing_ops: 3
  slug: aftership-pickups-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Products API from AfterShip — 4 operation(s) for products.
  name: AfterShip Products API
  phrasing_intents:
  - id: create-product
    intent: Create a product with variants
    question: How do I add a new product to my store catalog?
  - id: get-products
    intent: List or search products in a store
    question: How do I list the products in my store?
  - id: get-product-by-id
    intent: Get a product by ID
    question: What are the details of a specific product?
  - id: update-product-by-id
    intent: Update a product's details
    question: Can I change a product's title or description?
  - id: create-product-variant
    intent: Add a variant to a product
    question: How do I add a new size or color variant to a product?
  - id: get-product-variant
    intent: Get a product variant
    question: What are the details of one variant of a product?
  - id: update-product-variant
    intent: Update a product variant
    question: How do I change a variant's price or stock level?
  - id: delete-product-variant
    intent: Delete a product variant
    question: How do I remove a variant I no longer sell?
  phrasing_ops: 8
  slug: aftership-products-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Rates API from AfterShip — 2 operation(s) for rates.
  name: AfterShip Rates API
  phrasing_intents:
  - id: get-rates
    intent: List past rate calculations
    question: Can I see the shipping rate quotes I've requested before?
  - id: post-rates
    intent: Calculate shipping rates
    question: How much will it cost to ship this package with each of my carriers?
  - id: get-rate
    intent: Get a rate calculation by ID
    question: Can I retrieve the result of a rate calculation later?
  phrasing_ops: 3
  slug: aftership-rates-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Return Dropoffs API from AfterShip — 1 operation(s) for return dropoffs.
  name: AfterShip Return Dropoffs API
  phrasing_intents:
  - id: post-returns-rma-rma_number-dropoffs-dropoff_id-drops
    intent: Record return items dropped off in store
    question: How do I log that a shopper dropped off return items after scanning their QR code?
  phrasing_ops: 1
  slug: aftership-return-dropoffs-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Return items API from AfterShip — 2 operation(s) for return items.
  name: AfterShip Return items API
  phrasing_intents:
  - id: patch-returns-return_id-items-item_id
    intent: Update a return item by return ID
    question: How do I update an item on a return when I have the return ID?
  - id: patch-returns-rma-rma_number-items-item_id
    intent: Update a return item by RMA number
    question: Can I update a return item using the customer-facing RMA number?
  phrasing_ops: 2
  slug: aftership-return-items-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: Create, approve, reject, resolve and receive returns by return ID or RMA number, manage return items, item tags and returns-page deep links.
  name: AfterShip Returns API
  phrasing_intents:
  - id: get-returns-return_id
    intent: Get a return by return ID
    question: How do I look up a return using its internal return ID?
  - id: get-returns-rma-rma_number
    intent: Get a return by RMA number
    question: Can I find a return using the RMA number the customer gave me?
  - id: get-returns
    intent: List and filter returns
    question: How do I list returns awaiting approval?
  - id: post-returns
    intent: Create a refund return for an order
    question: How do I open a return on behalf of a customer?
  - id: post-returns-rma-rma_number-approve
    intent: Approve a return by RMA number
    question: Can I approve a return using its RMA number and generate a label?
  - id: post-returns-return_id-approve
    intent: Approve a return by return ID
    question: How do I approve a return when I have its return ID?
  - id: post-returns-rma-rma_number-resolve
    intent: Resolve a return by RMA number
    question: Can I resolve a return using the RMA number once it's handled?
  - id: post-returns-return_id-resolve
    intent: Resolve a return by return ID
    question: How do I move a return to resolved status using its return ID?
  phrasing_ops: 16
  slug: aftership-returns-api
- baseURL: https://api.aftership.com/returns/2026-07
  baseurl_source: declared
  description: The Returns Page API from AfterShip — 1 operation(s) for returns page.
  name: AfterShip Returns Page API
  phrasing_intents:
  - id: post-create-return-deep-link
    intent: Create a pre-filled returns page link
    question: How do I send a customer a link that opens the returns page with their order filled in?
  phrasing_ops: 1
  slug: aftership-returns-page-api
- baseURL: https://api.aftership.com/admin/2022-01
  baseurl_source: declared
  description: The Roles API from AfterShip — 1 operation(s) for roles.
  name: AfterShip Roles API
  phrasing_intents:
  - id: get-roles
    intent: List available member roles
    question: Which roles can I assign to members of my organization?
  phrasing_ops: 1
  slug: aftership-roles-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Shipper Accounts API from AfterShip — 5 operation(s) for shipper accounts.
  name: AfterShip Shipper Accounts API
  phrasing_intents:
  - id: get-shipper-accounts
    intent: List shipper accounts
    question: Which carrier shipper accounts do I have set up?
  - id: post-shipper-accounts
    intent: Add a carrier shipper account
    question: How do I connect a new carrier account for shipping labels?
  - id: get-shipper-accounts-id
    intent: Get a shipper account by ID
    question: What are the details of a specific shipper account?
  - id: delete-shipper-accounts-id
    intent: Delete a shipper account
    question: How do I remove a carrier account I no longer ship with?
  - id: put-shipper-accounts-id-info
    intent: Update a shipper account's address or description
    question: How do I change the address on a shipper account?
  - id: patch-shipper-accounts-id-credentials
    intent: Update a shipper account's credentials
    question: How do I update the carrier password on a shipper account?
  - id: patch-shipper-accounts-id-settings
    intent: Update a FedEx shipper account's settings
    question: Can I turn on electronic trade documents for my FedEx shipper account?
  phrasing_ops: 7
  slug: aftership-shipper-accounts-api
- baseURL: https://api.aftership.com/postmen/v3
  baseurl_source: declared
  description: The Specific Shipper Accounts API from AfterShip — 2 operation(s) for specific shipper accounts.
  name: AfterShip Specific Shipper Accounts API
  phrasing_intents:
  - id: post-v3-couriers-fedex-shipper-accounts
    intent: Create a FedEx shipper account
    question: How do I connect my FedEx account for label creation?
  - id: post-v3-couriers-fedex-shipper-accounts-id-update
    intent: Update a legacy FedEx shipper account
    question: How do I update a legacy FedEx shipper account?
  phrasing_ops: 2
  slug: aftership-specific-shipper-accounts-api
- baseURL: https://api.aftership.com/commerce/2026-07
  baseurl_source: declared
  description: The Stores API from AfterShip — 2 operation(s) for stores.
  name: AfterShip Stores API
  phrasing_intents:
  - id: create-store
    intent: Create a store
    question: How do I create a new store before pushing orders and products?
  - id: get-stores
    intent: List stores
    question: How do I see all the stores in my Commerce account?
  - id: get-store-by-id
    intent: Get a store by ID
    question: What are the settings of a specific store?
  - id: update-store-by-id
    intent: Update a store's details
    question: Can I change a store's support email or phone?
  phrasing_ops: 4
  slug: aftership-stores-api
- baseURL: https://api.aftership.com/tracking/2026-07
  baseurl_source: declared
  description: 'Shipment tracking across 1,400+ carriers: create and query trackings, detect couriers, manage courier connections, and predict estimated delivery dates.'
  name: AfterShip Tracking API
  phrasing_intents:
  - id: get-trackings
    intent: List and filter shipment trackings
    question: How do I list all the shipments I'm tracking?
  - id: create-tracking
    intent: Start tracking a shipment
    question: How do I start tracking a package with AfterShip?
  - id: get-tracking-by-id
    intent: Get a tracking's latest status
    question: Where is my package right now?
  - id: update-tracking-by-id
    intent: Update a tracking's details
    question: Can I change the courier or order number on an existing tracking?
  - id: delete-tracking-by-id
    intent: Delete a tracking
    question: How do I stop tracking and remove a shipment?
  - id: retrack-tracking-by-id
    intent: Retrack an expired tracking
    question: Can I resume tracking a shipment after it expired?
  - id: mark-tracking-completed-by-id
    intent: Mark a tracking as completed
    question: How do I manually mark a shipment as delivered or lost?
  phrasing_ops: 7
  slug: aftership-tracking-api
- baseURL: https://api.aftership.com/warranty/2026-07
  baseurl_source: declared
  description: Public endpoints for querying and correcting warranty registration data.
  name: AfterShip Warranty Registrations API
  phrasing_intents:
  - id: get-order-warranty-registrations
    intent: Look up warranty registrations for an order
    question: Which items in a customer's order have registered warranties?
  - id: patch-warranty-registration
    intent: Update a warranty registration
    question: How do I extend the expiry of a warranty registration?
  - id: invalidate-warranty-registration
    intent: Invalidate a warranty registration
    question: How do I void a customer's warranty registration?
  phrasing_ops: 3
  slug: aftership-warranty-registrations-api
artifact_total: 45
asyncapis:
- description: ''
  name: Aftership Webhooks
  slug: aftership-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/capabilities/aftership-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aftership-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/agentic-access/aftership-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aftership-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/authentication/aftership-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aftership-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/security/aftership-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aftership-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/security/aftership-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aftership-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/security/aftership-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aftership-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AfterShip
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aftership
- group: company
  title: ''
  type: Website
  url: https://www.aftership.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/plans/aftership-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aftership-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/rate-limits/aftership-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aftership-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/finops/aftership-finops.yml
  title: ''
  type: FinOps
  url: finops/aftership-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/packages/aftership-packages.yml
  title: ''
  type: Packages
  url: packages/aftership-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/packages/aftership-packages.yml
  title: ''
  type: SDKs
  url: packages/aftership-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/well-known/aftership-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aftership-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/mcp/aftership-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aftership-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/mcp/aftership-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aftership-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/llms/aftership-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aftership-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/conformance/aftership-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aftership-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/conformance/aftership-conformance.yml
  title: ''
  type: Compliance
  url: conformance/aftership-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/errors/aftership-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aftership-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/lifecycle/aftership-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aftership-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.aftershipstatus.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/lifecycle/aftership-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aftership-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/scopes/aftership-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aftership-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/security/aftership-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aftership-vulnerability-disclosure.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/sandbox/aftership-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aftership-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/conventions/aftership-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aftership-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/changelog/aftership-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aftership-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/components/aftership-components.yml
  title: ''
  type: Components
  url: components/aftership-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/data-model/aftership-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aftership-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/asyncapi/aftership-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aftership-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/overlays/aftership-tracking-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aftership-tracking-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aftership.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.aftership.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.aftership.com/docs/tracking/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aftership.com/docs/tracking/quickstart/api-quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.aftership.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.aftership.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.aftership.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aftership.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.aftership.com/sso/authorize?continue=register&pd=tracking
- group: start
  title: ''
  type: Login
  url: https://accounts.aftership.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aftership.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aftership.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/aftership/workspace/api-aftership-com
created: '2026-05-08'
description: AfterShip is a post-purchase experience platform for ecommerce brands, retailers, marketplaces and 3PLs, founded in 2012 and headquartered in Hong Kong. Its products cover shipment tracking across 1,400+ carriers, branded tracking pages, AI-predicted estimated delivery dates, automated returns and exchanges, warranty and claims management, shipping-label generation and rate shopping (Postmen), shipment protection, address validation, AI email parsing, product personalization and discovery, and marketplace feed management. AfterShip publishes ten versioned, date-based REST APIs on api.aftership.com, each with a downloadable OpenAPI 3.1 description, seven first-party SDKs, webhooks, an OAuth 2.0 authorization server, and public and OAuth-gated MCP servers for AI agents.
finops:
- name: Aftership Finops
  service_category: Shipping
  slug: aftership-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aftership.png
layout: provider
mcp_servers:
- description: AfterShip publishes an anonymous, no-auth remote MCP server for real-time package tracking and a Returns Center demo, plus two OAuth-gated remote MCP servers (Post-purchase and Channels) documented on
  name: AfterShip Tracking & Returns MCP Server
  slug: aftership-tracking-returns-mcp-server
modified: '2026-08-27'
name: AfterShip
nav: Providers
network: true
overview: 'AfterShip publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Address API, Address Validations (Beta) API, Cancel Labels API, and 31 more. Tagged areas include Shipping, Tracking, E-Commerce, Post-Purchase, and Notification.


  The AfterShip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AfterShip''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 40 more developer resources.'
plans:
- name: Aftership Plans Pricing
  plan_count: 4
  slug: aftership-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 20
  name: Aftership Rate Limits
  slug: aftership-rate-limits
scopes:
- name: Aftership Scopes
  scope_count: 7
  slug: aftership-scopes
  summary_line: 7 scopes
score:
  band: exemplar
  composite: 78.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 58.2
    developer_ergonomics: 81.0
    discoverability: 80.0
    operational_transparency: 92.1
  previous_composite: 78.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/aftership/refs/heads/main/screenshots/aftership-2026-06-20T165736.png
security:
- kind: authentication
  name: Aftership Authentication
  slug: aftership-authentication
  summary_line: apiKey/hmac-signature/oauth2 · 3 schemes
- kind: domain-security
  name: Aftership Domain Security
  slug: aftership-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aftership Vulnerability Disclosure
  slug: aftership-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Aftership Trust Center
  slug: aftership-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: aftership
tags:
- Shipping
- Tracking
- E-Commerce
- Post-Purchase
- Notification
- Logistics
- Returns
- Warranty
- Address Validation
- Fulfillment
- Carrier
- Webhook
- MCP
- Retail
website: https://www.aftership.com/
---
