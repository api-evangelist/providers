---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Sendcloud Agentic Access
  operation_count: 94
  slug: sendcloud-agentic-access
  summary_line: 94 operations · 42 acting
api_count: 20
apis:
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Address API from Sendcloud — 1 operation(s) for address.
  name: Sendcloud Address API
  phrasing_intents:
  - id: sc-public-v3-scp-post-validate_address
    intent: Validate a shipping address
    question: Can I check that a shipping address is valid before I create a label?
  phrasing_ops: 1
  slug: sendcloud-address-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Analytics API from Sendcloud — 2 operation(s) for analytics.
  name: Sendcloud Analytics API
  phrasing_intents:
  - id: sc-public-v3-analytics-get-carrier_transit_times
    intent: Get transit-time statistics for a carrier
    question: How long does a carrier typically take to deliver my parcels?
  - id: sc-public-v3-analytics-get-shipping_option_transit_times
    intent: Get transit-time statistics for a shipping option
    question: How fast is a specific shipping option delivering compared to what I expected?
  phrasing_ops: 2
  slug: sendcloud-analytics-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Broadcast API from Sendcloud — 1 operation(s) for broadcast.
  name: Sendcloud Broadcast API
  phrasing_intents:
  - id: sc-public-v3-scp-post-test_broadcast
    intent: Send a test event to a subscription
    question: Is there a way to check that my event subscription endpoint is receiving events?
  phrasing_ops: 1
  slug: sendcloud-broadcast-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Connections API from Sendcloud — 2 operation(s) for connections.
  name: Sendcloud Connections API
  phrasing_intents:
  - id: sc-public-v3-scp-post-create_connection
    intent: Create an event notification connection
    question: How do I add a new endpoint where shipping events get delivered?
  - id: sc-public-v3-scp-get-list_connections
    intent: List event notification connections
    question: Which external endpoints are set up to receive my Sendcloud event notifications?
  - id: sc-public-v3-scp-get-connection
    intent: Get one event connection
    question: How do I look up the details of a single event connection?
  - id: sc-public-v3-scp-patch-connection
    intent: Update an event connection
    question: Can I change the endpoint configuration of an existing connection?
  - id: sc-public-v3-scp-delete-connection
    intent: Delete an event connection
    question: What happens to my subscriptions if I delete a connection?
  phrasing_ops: 5
  slug: sendcloud-connections-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Customs Documents Download API from Sendcloud — 2 operation(s) for customs documents download.
  name: Sendcloud Customs Documents Download API
  phrasing_intents:
  - id: sc-public-v2-scp-get-customs_document_normal_printer
    intent: Download a parcel's customs declaration PDF
    question: How do I get the customs declaration for one parcel as a PDF?
  - id: sc-public-v2-scp-get-customs_document_multiple_normal_printer
    intent: Download customs declarations for many parcels
    question: Can I download customs declarations for several parcels in one PDF?
  phrasing_ops: 2
  slug: sendcloud-customs-documents-download-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Integration exception logs API
  name: Sendcloud Exception logs API
  phrasing_intents:
  - id: sc-public-v3-integrations-get-retrieve_integrations_logs
    intent: List exception logs across all integrations
    question: Why are my shop integrations failing to talk to my webshop?
  - id: sc-public-v3-integrations-get-retrieve_integration_logs
    intent: List exception logs for one integration
    question: What errors has one specific shop integration hit recently?
  - id: sc-public-v3-integrations-post-create_integration_logs
    intent: Record an exception log for an integration
    question: How can my integration report a failed shop request so the merchant sees it?
  phrasing_ops: 3
  slug: sendcloud-exception-logs-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Integrations API from Sendcloud — 6 operation(s) for integrations.
  name: Sendcloud Integrations API
  phrasing_intents:
  - id: sc-public-v2-orders-get-retrieve_a_list_of_integrations
    intent: List connected shop integrations
    question: Which webshops are connected to my Sendcloud account?
  - id: sc-public-v2-orders-get-retrieve_an_integration
    intent: Get one shop integration
    question: How do I see the settings of a single shop integration?
  - id: sc-public-v2-orders-put-update_an_integration
    intent: Replace a shop integration's settings
    question: How do I overwrite all of a shop integration's settings in one go?
  - id: sc-public-v2-orders-patch-partial_update_an_integration
    intent: Change selected shop integration settings
    question: Can I turn on the webhook for a shop without resending all its settings?
  - id: sc-public-v2-orders-delete-delete_an_integration
    intent: Delete a shop integration
    question: How do I disconnect a webshop from Sendcloud?
  - id: sc-public-v2-orders-get-retrieve_integrations_logs
    intent: List all integration exception logs (v2)
    question: Where can I see every error my shop integrations have logged?
  - id: sc-public-v2-orders-get-retrieve_integration_logs
    intent: List exception logs for one integration (v2)
    question: What went wrong with one particular shop integration?
  - id: sc-public-v2-orders-post-create_integration_logs
    intent: Record an integration exception log (v2)
    question: How does my integration add an entry to the merchant's connection issue log?
  phrasing_ops: 12
  slug: sendcloud-integrations-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Label Download API from Sendcloud — 4 operation(s) for label download.
  name: Sendcloud Label Download API
  phrasing_intents:
  - id: sc-public-v2-scp-get-label_document_normal_printer
    intent: Download a parcel's label for a normal printer
    question: How do I print one parcel's shipping label on a regular A4 printer?
  - id: sc-public-v2-scp-get-label_document_multiple_normal_printer
    intent: Download labels for many parcels for a normal printer
    question: Can I get labels for several parcels in one PDF for an office printer?
  - id: sc-public-v2-scp-get-label_document_label_printer
    intent: Download a parcel's label for a label printer
    question: How do I get one parcel's label formatted for a thermal label printer?
  - id: sc-public-v2-scp-get-label_document_multiple_label_printer
    intent: Download labels for many parcels for a label printer
    question: Can I bulk download labels for several parcels sized for a label printer?
  phrasing_ops: 4
  slug: sendcloud-label-download-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Labels API from Sendcloud — 2 operation(s) for labels.
  name: Sendcloud Labels API
  phrasing_intents:
  - id: sc-public-v2-scp-get-label_by_parcel_id
    intent: Get label download links for a parcel
    question: Where do I get the label download URLs for a parcel I created?
  - id: sc-public-v2-scp-post-label_by_parcel_ids
    intent: Request labels for multiple parcels
    question: How do I request shipping labels for a batch of parcels at once?
  phrasing_ops: 2
  slug: sendcloud-labels-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: OrderAPI
  name: Sendcloud Orders API
  phrasing_intents:
  - id: sc-public-v3-orders-post-create_orders
    intent: Create or update orders in batch
    question: How do I import orders from my own system into a Sendcloud API integration?
  - id: sc-public-v3-orders-get-list_orders
    intent: List orders
    question: Which orders came in from a specific shop integration this week?
  - id: sc-public-v3-orders-get-retrieve_order
    intent: Get an order
    question: What are all the details of one particular order?
  - id: sc-public-v3-orders-delete-delete_order
    intent: Delete an order
    question: Can I remove an order that was cancelled in my shop?
  - id: sc-public-v3-orders-patch-partial_update_order
    intent: Update an order
    question: Can I fix the shipping address on an order after import?
  phrasing_ops: 5
  slug: sendcloud-orders-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Parcel Documents API from Sendcloud — 2 operation(s) for parcel documents.
  name: Sendcloud Parcel Documents API
  phrasing_intents:
  - id: sc-public-v3-scp-get-retrieve_parcel_documents
    intent: Download a parcel document
    question: How do I download a specific document, like a label, for one parcel?
  - id: sc-public-v3-scp-get-retrieve_parcel_documents_bulk
    intent: Download a document type for many parcels
    question: Can I download the same document type for several parcels together?
  phrasing_ops: 2
  slug: sendcloud-parcel-documents-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Parcel Tracking API from Sendcloud — 2 operation(s) for parcel tracking.
  name: Sendcloud Parcel Tracking API
  phrasing_intents:
  - id: sc-public-v3-shipping_intelligence_engine-get-get_parcel_by_tracking_number
    intent: Track a parcel by tracking number
    question: Where is my parcel right now?
  - id: sc-public-v3-shipping_intelligence_engine-post-register_parcel_for_tracking
    intent: Register an external parcel for tracking
    question: Can Sendcloud track a parcel I shipped outside of Sendcloud?
  phrasing_ops: 2
  slug: sendcloud-parcel-tracking-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Get insights about parcels
  name: Sendcloud Parcels API
  phrasing_intents:
  - id: sc-public-v2-analytics-get-parcels_series
    intent: Chart parcel volume over time
    question: How many parcels did I ship per day last month?
  - id: sc-public-v2-analytics-get-parcels_buckets
    intent: Group parcel counts by a category
    question: Which destination countries receive the most of my parcels?
  - id: sc-public-v2-analytics-get-parcels_summary
    intent: Count parcels for the last N days
    question: How many parcels have I sent in the last 30 days?
  - id: sc-public-v2-scp-get-all_parcels
    intent: List parcels
    question: Which parcels have I created or imported into my account?
  - id: sc-public-v2-scp-post-create_parcel
    intent: Create one or more parcels
    question: How do I create a new parcel and announce it to the carrier right away?
  - id: sc-public-v2-scp-put-update_a_parcel
    intent: Update an unannounced parcel
    question: Can I change a parcel's data before it's announced to the carrier?
  - id: sc-public-v2-scp-get-parcel_by_id
    intent: Get a parcel
    question: How do I look up a single parcel by its ID?
  - id: sc-public-v2-scp-post-cancel_specific
    intent: Cancel or delete a parcel
    question: Can I cancel a parcel after it has been announced?
  phrasing_ops: 9
  slug: sendcloud-parcels-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Get insights about products
  name: Sendcloud Products API
  phrasing_intents:
  - id: sc-public-v2-analytics-get-products_series
    intent: Chart shipped product volume over time
    question: How many products did I ship per week this quarter?
  - id: sc-public-v2-analytics-get-products_buckets
    intent: Group shipped products by a category
    question: Which products do I ship most to each country?
  phrasing_ops: 2
  slug: sendcloud-products-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Generate data exports and reports.
  name: Sendcloud Reporting API
  phrasing_intents:
  - id: sc-public-v2-reporting_analytics-post-parcels_report
    intent: Generate a parcels CSV report
    question: How do I export my outgoing parcels to a CSV file?
  - id: sc-public-v2-reporting_analytics-get-parcels_report
    intent: Download a parcels report
    question: Is my parcels report ready to download yet?
  phrasing_ops: 2
  slug: sendcloud-reporting-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Returns API from Sendcloud — 6 operation(s) for returns.
  name: Sendcloud Returns API
  phrasing_intents:
  - id: sc-public-v3-scp-post-validate_address
    intent: Validate a shipping address
    question: Can I check that a shipping address is valid before I create a label?
  - id: sc-public-v3-scp-post-returns_create_new_return
    intent: Create a return
    question: How do I create a standalone return for a customer?
  - id: sc-public-v3-scp-get-returns_get_returns
    intent: List returns
    question: Which returns were created in the last two weeks?
  - id: sc-public-v3-scp-get-returns_get_details
    intent: Get a return
    question: How do I check the details of a specific return?
  - id: sc-public-v3-scp-patch-returns_cancel
    intent: Request cancellation of a return
    question: Can I cancel a return a customer no longer needs?
  - id: sc-public-v3-scp-post-returns_validate
    intent: Check a return can be announced
    question: Can I test whether a return would be accepted without creating it?
  - id: sc-public-v3-scp-post-returns_create_new_return_synchronously
    intent: Create a return and wait for the carrier
    question: How do I create a return and get the carrier's response immediately?
  phrasing_ops: 7
  slug: sendcloud-returns-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Service Points API
  name: Sendcloud Service Points API
  phrasing_intents:
  - id: sc-public-v3-servicepoints-get-list_service_points
    intent: Find service points near a location
    question: Where are the nearest pickup points in a postal code?
  - id: sc-public-v3-servicepoints-get-service_point
    intent: Get a service point
    question: How do I get the address and opening hours of one service point?
  - id: sc-public-v3-servicepoints-post-check_availability
    intent: Check if a service point is available
    question: Is a given service point open and accepting parcels right now?
  phrasing_ops: 3
  slug: sendcloud-service-points-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: OrderLabelAPI
  name: Sendcloud Ship an Order API
  phrasing_intents:
  - id: sc-public-v3-orders_labels-post-create_labels_async
    intent: Create labels for orders asynchronously
    question: Can I create shipping labels for many orders in one go?
  - id: sc-public-v3-orders_labels-post-create_labels_sync
    intent: Create a label for one order and wait
    question: Can I get the label for a single order back in the same response?
  phrasing_ops: 2
  slug: sendcloud-ship-an-order-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Shipments API
  name: Sendcloud Shipments API
  phrasing_intents:
  - id: sc-public-v3-scp-post-announce_shipment
    intent: Create and announce a shipment synchronously
    question: How do I create a shipment and get the label in the same response?
  - id: sc-public-v3-scp-get-all_shipments
    intent: List shipments
    question: Which shipments have I created or imported recently?
  - id: sc-public-v3-scp-post-create_shipment
    intent: Create and announce a shipment asynchronously
    question: Can I submit a shipment and have it announced in the background?
  - id: sc-public-v3-scp-post-announce_shipment_with_rules
    intent: Announce a shipment with shipping rules, synchronously
    question: Can my shipping rules pick the method when I announce a shipment and wait for it?
  - id: sc-public-v3-scp-post-create_shipment_with_rules
    intent: Announce a shipment with shipping rules, asynchronously
    question: Can shipping rules and defaults be applied to a shipment announced in the background?
  - id: sc-public-v3-scp-post-validate_address
    intent: Validate a shipping address
    question: Can I check that a shipping address is valid before I create a label?
  - id: sc-public-v3-scp-get-shipment_by_id
    intent: Get a shipment
    question: How do I look up one shipment by its ID?
  - id: sc-public-v3-scp-post-cancel_shipment
    intent: Cancel an announced shipment
    question: Can I cancel a shipment that's already been announced to the carrier?
  phrasing_ops: 12
  slug: sendcloud-shipments-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Subscriptions API from Sendcloud — 2 operation(s) for subscriptions.
  name: Sendcloud Subscriptions API
  phrasing_intents:
  - id: sc-public-v3-scp-post-create_subscription
    intent: Subscribe a connection to an event type
    question: How do I start receiving a specific event at one of my connections?
  - id: sc-public-v3-scp-get-list_subscriptions
    intent: List event subscriptions
    question: Which shipping events am I subscribed to?
  - id: sc-public-v3-scp-get-subscription
    intent: Get an event subscription
    question: Which connection and event does a given subscription route?
  - id: sc-public-v3-scp-patch-subscription
    intent: Update an event subscription
    question: Can I pause a subscription without deleting it?
  - id: sc-public-v3-scp-delete-subscription
    intent: Delete an event subscription
    question: What's the way to stop receiving an event type for good?
  phrasing_ops: 5
  slug: sendcloud-subscriptions-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Tracking API from Sendcloud — 1 operation(s) for tracking.
  name: Sendcloud Tracking API
  phrasing_intents:
  - id: sc-public-v2-tracking-get-detailed_tracking_information
    intent: Get a parcel's tracking history
    question: Where is my parcel and what has happened to it so far?
  phrasing_ops: 1
  slug: sendcloud-tracking-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Get insights about average transit times per carriers and shipping methods
  name: Sendcloud Transit times API
  phrasing_intents:
  - id: sc-public-v2-analytics-get-carrier_transit_times
    intent: Get a carrier's average transit time
    question: How many days on average does a carrier take to deliver?
  - id: sc-public-v2-analytics-get-shipping_method_transit_times
    intent: Get a shipping method's average transit time
    question: How long does a particular shipping method usually take?
  phrasing_ops: 2
  slug: sendcloud-transit-times-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: Get list of carriers and shipping methods a user ever used
  name: Sendcloud User Carriers and Shipping Methods API
  phrasing_intents:
  - id: sc-public-v2-analytics-get-user_shipping_methods
    intent: List shipping methods I have used
    question: Which shipping methods have I ever used?
  - id: sc-public-v2-analytics-get-user_carriers
    intent: List carriers I have used
    question: Which carriers have I shipped with?
  phrasing_ops: 2
  slug: sendcloud-user-carriers-and-shipping-methods-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Events API from Sendcloud — 0 operation(s) for events.
  name: Sendcloud Events API
  slug: sendcloud-events-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The Webhooks API from Sendcloud — 0 operation(s) for webhooks.
  name: Sendcloud Webhooks API
  slug: sendcloud-webhooks-api
- baseURL: https://panel.sendcloud.sc/api/v3
  baseurl_source: declared
  description: The OAuth2 API from Sendcloud — 1 operation(s) for oauth2.
  name: Sendcloud O Auth2 API
  phrasing_intents:
  - id: sc-public-v3-scp-post-start_authorization
    intent: Start OAuth2 authorization for a connection
    question: What's needed to authorize a connection that uses OAuth2, like Klaviyo?
  phrasing_ops: 1
  slug: sendcloud-oauth2-api
arazzos:
- description: Announce a shipment synchronously, then retrieve the return portal URL customers use to create a return.
  name: Sendcloud Announce a Shipment and Get its Return Portal URL
  slug: sendcloud-announce-shipment-return-portal-workflow
- description: Announce a shipment synchronously, then verify it and read its label document link.
  name: Sendcloud Announce a Shipment with Label
  slug: sendcloud-announce-shipment-with-label-workflow
- description: List parcels filtered by status, then request a single bulk PDF of their labels.
  name: Sendcloud Bulk Print Labels for Recent Parcels
  slug: sendcloud-bulk-print-labels-workflow
- description: Look up a shipment by id, then cancel it and branch on whether cancellation was immediate or queued.
  name: Sendcloud Cancel a Shipment with Confirmation
  slug: sendcloud-cancel-shipment-workflow
- description: Create a parcel with a label request, then retrieve its PDF label download URLs.
  name: Sendcloud Create a Parcel and Fetch its Label
  slug: sendcloud-create-parcel-fetch-label-workflow
- description: Create a labelled parcel, then retrieve the return portal URL a customer can use to start a return.
  name: Sendcloud Create a Parcel and Get its Return Portal URL
  slug: sendcloud-create-parcel-return-portal-workflow
- description: Create a labelled parcel, then poll its tracking until it is en route.
  name: Sendcloud Create a Parcel and Track its Shipment
  slug: sendcloud-create-parcel-track-shipment-workflow
- description: Create a standalone return, inspect it, and request cancellation only when it is still cancellable.
  name: Sendcloud Create a Return and Cancel It If Cancellable
  slug: sendcloud-create-return-cancel-if-cancellable-workflow
- description: Register a parcel labelled outside Sendcloud for tracking, then retrieve its tracking record.
  name: Sendcloud Register an External Parcel and Track It
  slug: sendcloud-register-external-parcel-track-workflow
- description: Request a label for an order asynchronously, then poll the created parcel until it has a label.
  name: Sendcloud Ship an Order Asynchronously and Poll the Parcel
  slug: sendcloud-ship-order-async-poll-parcel-workflow
- description: Request a label for an order synchronously, then pull its v3 tracking detail.
  name: Sendcloud Ship an Order Synchronously and Track It
  slug: sendcloud-ship-order-sync-track-workflow
- description: Validate a return payload, create the return, then retrieve its full detail.
  name: Sendcloud Validate and Create a Return
  slug: sendcloud-validate-create-return-workflow
artifact_total: 156
collections:
- collection_type: postman
  name: Shipments
  slug: postman-sendcloud-shipments
- collection_type: postman
  name: Analytics
  slug: postman-sendcloud-v2-analytics
- collection_type: postman
  name: Integrations
  slug: postman-sendcloud-v2-integrations
- collection_type: postman
  name: Labels
  slug: postman-sendcloud-v2-labels
- collection_type: postman
  name: Parcel Documents
  slug: postman-sendcloud-v2-parcel-documents
- collection_type: postman
  name: Parcels
  slug: postman-sendcloud-v2-parcels
- collection_type: postman
  name: Reporting
  slug: postman-sendcloud-v2-reporting
- collection_type: postman
  name: Tracking parcels
  slug: postman-sendcloud-v2-tracking
- collection_type: postman
  name: Webhooks
  slug: postman-sendcloud-v2-webhooks
- collection_type: postman
  name: Analytics
  slug: postman-sendcloud-v3-analytics
- collection_type: postman
  name: Event Subscriptions API
  slug: postman-sendcloud-v3-event-subscriptions
- collection_type: postman
  name: Integrations
  slug: postman-sendcloud-v3-integrations
- collection_type: postman
  name: Orders
  slug: postman-sendcloud-v3-orders
- collection_type: postman
  name: Parcel documents API
  slug: postman-sendcloud-v3-parcel-documents
- collection_type: postman
  name: Parcel Tracking API
  slug: postman-sendcloud-v3-parcel-tracking
- collection_type: postman
  name: Reporting
  slug: postman-sendcloud-v3-reporting
- collection_type: postman
  name: Returns
  slug: postman-sendcloud-v3-returns
- collection_type: postman
  name: Service Points API [BETA]
  slug: postman-sendcloud-v3-service-points
- collection_type: postman
  name: Ship an Order
  slug: postman-sendcloud-v3-ship-an-order
- collection_type: postman
  name: Webhooks
  slug: postman-sendcloud-v3-webhooks
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shipments Address API
  slug: open-sendcloud-address-api
- collection_type: open
  name: Shipments Address Analytics API
  slug: open-sendcloud-analytics-api
- collection_type: open
  name: Shipments Address Broadcast API
  slug: open-sendcloud-broadcast-api
- collection_type: open
  name: Shipments Address Connections API
  slug: open-sendcloud-connections-api
- collection_type: open
  name: Shipments Address Customs Documents Download API
  slug: open-sendcloud-customs-documents-download-api
- collection_type: open
  name: Shipments Address Exception logs API
  slug: open-sendcloud-exception-logs-api
- collection_type: open
  name: Shipments Address Integrations API
  slug: open-sendcloud-integrations-api
- collection_type: open
  name: Shipments Address Label Download API
  slug: open-sendcloud-label-download-api
- collection_type: open
  name: Shipments Address Labels API
  slug: open-sendcloud-labels-api
- collection_type: open
  name: Shipments Address OAuth2 API
  slug: open-sendcloud-oauth2-api
- collection_type: open
  name: Shipments Address Orders API
  slug: open-sendcloud-orders-api
- collection_type: open
  name: Shipments Address Parcel Documents API
  slug: open-sendcloud-parcel-documents-api
- collection_type: open
  name: Shipments Address Parcel Tracking API
  slug: open-sendcloud-parcel-tracking-api
- collection_type: open
  name: Shipments Address Parcels API
  slug: open-sendcloud-parcels-api
- collection_type: open
  name: Shipments Address Products API
  slug: open-sendcloud-products-api
- collection_type: open
  name: Shipments Address Reporting API
  slug: open-sendcloud-reporting-api
- collection_type: open
  name: Shipments Address Returns API
  slug: open-sendcloud-returns-api
- collection_type: open
  name: Shipments Address Service Points API
  slug: open-sendcloud-service-points-api
- collection_type: open
  name: Shipments Address Ship an Order API
  slug: open-sendcloud-ship-an-order-api
- collection_type: open
  name: Address Shipments API
  slug: open-sendcloud-shipments-api
- collection_type: open
  name: Shipments
  slug: open-sendcloud-shipments
- collection_type: open
  name: Shipments Address Subscriptions API
  slug: open-sendcloud-subscriptions-api
- collection_type: open
  name: Shipments Address Tracking API
  slug: open-sendcloud-tracking-api
- collection_type: open
  name: Shipments Address Transit times API
  slug: open-sendcloud-transit-times-api
- collection_type: open
  name: Shipments Address User Carriers and Shipping Methods API
  slug: open-sendcloud-user-carriers-and-shipping-methods-api
- collection_type: open
  name: Analytics
  slug: open-sendcloud-v2-analytics
- collection_type: open
  name: Integrations
  slug: open-sendcloud-v2-integrations
- collection_type: open
  name: Labels
  slug: open-sendcloud-v2-labels
- collection_type: open
  name: Parcel Documents
  slug: open-sendcloud-v2-parcel-documents
- collection_type: open
  name: Parcels
  slug: open-sendcloud-v2-parcels
- collection_type: open
  name: Reporting
  slug: open-sendcloud-v2-reporting
- collection_type: open
  name: Tracking parcels
  slug: open-sendcloud-v2-tracking
- collection_type: open
  name: Webhooks
  slug: open-sendcloud-v2-webhooks
- collection_type: open
  name: Analytics
  slug: open-sendcloud-v3-analytics
- collection_type: open
  name: Event Subscriptions API
  slug: open-sendcloud-v3-event-subscriptions
- collection_type: open
  name: Integrations
  slug: open-sendcloud-v3-integrations
- collection_type: open
  name: Orders
  slug: open-sendcloud-v3-orders
- collection_type: open
  name: Parcel documents API
  slug: open-sendcloud-v3-parcel-documents
- collection_type: open
  name: Parcel Tracking API
  slug: open-sendcloud-v3-parcel-tracking
- collection_type: open
  name: Reporting
  slug: open-sendcloud-v3-reporting
- collection_type: open
  name: Returns
  slug: open-sendcloud-v3-returns
- collection_type: open
  name: Service Points API [BETA]
  slug: open-sendcloud-v3-service-points
- collection_type: open
  name: Ship an Order
  slug: open-sendcloud-v3-ship-an-order
- collection_type: open
  name: Webhooks
  slug: open-sendcloud-v3-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/capabilities/sendcloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sendcloud-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/a2a/sendcloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sendcloud-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/agentic-access/sendcloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendcloud-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/security/sendcloud-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sendcloud-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/security/sendcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendcloud-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/authentication/sendcloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendcloud-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/scopes/sendcloud-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sendcloud-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sendcloud/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-announce-shipment-return-portal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-announce-shipment-return-portal-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-announce-shipment-with-label-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-announce-shipment-with-label-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-bulk-print-labels-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-bulk-print-labels-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-cancel-shipment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-cancel-shipment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-create-parcel-fetch-label-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-parcel-fetch-label-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-create-parcel-return-portal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-parcel-return-portal-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-create-parcel-track-shipment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-parcel-track-shipment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-create-return-cancel-if-cancellable-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-create-return-cancel-if-cancellable-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-register-external-parcel-track-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-register-external-parcel-track-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-ship-order-async-poll-parcel-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-ship-order-async-poll-parcel-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-ship-order-sync-track-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-ship-order-sync-track-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/arazzo/sendcloud-validate-create-return-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/sendcloud-validate-create-return-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.sendcloud.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sendcloud.dev
- group: docs
  title: ''
  type: Documentation
  url: https://sendcloud.dev/docs/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://sendcloud.dev/api/v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://sendcloud.dev/docs/getting-started/
- group: start
  title: ''
  type: GettingStarted
  url: https://sendcloud.dev/docs/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://sendcloud.dev/docs/getting-started/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://sendcloud.dev/docs/getting-started/rate-limits/
- group: design
  title: ''
  type: Pagination
  url: https://sendcloud.dev/api/v3/pagination/
- group: docs
  title: ''
  type: APIVersionGuide
  url: https://sendcloud.dev/docs/getting-started/api-version-guide/
- group: docs
  title: ''
  type: MigrationGuide
  url: https://sendcloud.dev/docs/getting-started/migration-guidelines-for-api-v3/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sendcloud.dev/api/v3/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sendcloud.dev/api/v2/changelog/
- group: other
  title: ''
  type: Glossary
  url: https://sendcloud.dev/docs/getting-started/glossary/
- group: build
  title: ''
  type: Postman
  url: https://sendcloud.dev/docs/getting-started/postman/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendcloud.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.sendcloud.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.sendcloud.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://releaselog.sendcloud.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sendcloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendcloud/
- group: agent
  title: ''
  type: LlmsText
  url: https://sendcloud.dev/llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/rules/sendcloud-rules.yml
  title: ''
  type: SpectralRules
  url: rules/sendcloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/vocabulary/sendcloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sendcloud-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/json-ld/sendcloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sendcloud-context.jsonld
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/plans/sendcloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendcloud-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/rate-limits/sendcloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sendcloud-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/finops/sendcloud-finops.yml
  title: ''
  type: FinOps
  url: finops/sendcloud-finops.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Sendcloud/SendCloud-API-PHP-Wrapper
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Sendcloud/api-integration-example
created: '2026-05-25'
description: Sendcloud is Europe's leading shipping platform for e-commerce, headquartered in Eindhoven, Netherlands. The platform connects 30,000+ merchants to 160+ carriers (DHL, DPD, UPS, GLS, FedEx, PostNL, bpost, La Poste, Royal Mail, Hermes, and many more) and 100+ commerce / WMS / marketplace integrations across the UK, Netherlands, Belgium, France, Germany, Austria, Italy, and Spain. The Sendcloud APIs cover the full fulfillment lifecycle — Orders, Ship an Order, Shipments, Service Points, Parcel Tracking, Parcel Documents, Returns, Event Subscriptions, Webhooks, Integrations, Analytics, and Reporting — over a versioned v2 / v3 REST surface on https://panel.sendcloud.sc, authenticated with HTTP Basic (public + private key) or OAuth 2.0 client credentials.
examples:
- key_count: 6
  name: Sendcloud Announce Shipment Example
  slug: sendcloud-announce-shipment-example
- key_count: 7
  name: Sendcloud Create Return Example
  slug: sendcloud-create-return-example
- key_count: 2
  name: Sendcloud List Service Points Example
  slug: sendcloud-list-service-points-example
features:
- description: DHL, DPD, UPS, GLS, FedEx, PostNL, bpost, La Poste, Royal Mail, Hermes, Colissimo, Chronopost, Mondial Relay, and many more.
  name: 160+ European carriers
- description: Shopify, WooCommerce, Magento, PrestaShop, BigCommerce, Amazon, eBay, Etsy, Bol.com, Lightspeed.
  name: 100+ commerce / WMS / marketplace integrations
- description: Aggregated parcel-shop, locker, and post-office network exposed through one Service Points API.
  name: Service points across Europe
- description: Merchant-branded tracking pages, email / SMS / WhatsApp delivery notifications.
  name: Branded tracking
- description: Self-service consumer return portal with drop-off, pickup, postbox, and in-store options.
  name: Returns portal
- description: Multiple physical parcels announced under a single shipment.
  name: Multicollo (multi-parcel) shipments
- description: Warehouse-floor pick-and-pack workflow.
  name: Pack & Go
- description: Versioned v2 and v3 REST surface.
  name: REST API at panel.sendcloud.sc
- description: Public/private key Basic auth or token exchange at https://account.sendcloud.com/oauth2/token (scope api).
  name: HTTP Basic + OAuth 2.0 client credentials
- description: v3 list endpoints return next/previous cursors.
  name: Cursor-based pagination
- description: parcel-status-changed, return-created and other typed events delivered to merchant endpoints.
  name: Typed event subscriptions and webhooks
- description: 1,000 GET / minute and 100 unsafe / minute (15 burst / second) per integration.
  name: Rate limits by HTTP safety class
- description: Subscription priced in EUR; carrier postage in local currency.
  name: Multi-currency billing
- description: Official Postman and downloadable OpenAPI for v3 surfaces.
  name: Postman collection + OpenAPI v3
- description: Sendcloud-Partner-Id header for third-party platforms calling on behalf of merchants.
  name: Marketplace integration guidelines
finops:
- name: Sendcloud Finops
  service_category: Shipping API
  slug: sendcloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: DeliveryOption
  property_count: 0
  slug: sendcloud-deliveryoption
- name: Sendcloud Order
  property_count: 0
  slug: sendcloud-order
- name: Sendcloud ParcelTrackingCreateRequest
  property_count: 0
  slug: sendcloud-parceltrackingcreaterequest
- name: Sendcloud ParcelTrackingResponse
  property_count: 0
  slug: sendcloud-parceltrackingresponse
- name: Price Object
  property_count: 2
  slug: sendcloud-price
- name: Return Object
  property_count: 33
  slug: sendcloud-return
- name: Service Point Search Result
  property_count: 0
  slug: sendcloud-servicepoint
- name: Service Point Address
  property_count: 5
  slug: sendcloud-servicepointaddress
- name: Service Point
  property_count: 13
  slug: sendcloud-servicepointdetail
json_structures:
- name: Sendcloud Return Structure
  property_count: 7
  slug: sendcloud-return-structure
- name: Sendcloud Shipment Structure
  property_count: 9
  slug: sendcloud-shipment-structure
jsonld:
- class_count: 40
  name: Sendcloud Context
  property_count: 17
  slug: sendcloud-context
layout: provider
mcp_servers:
- description: Remote MCP server at sendcloud.dev over HTTP; 3 tools listed.
  name: Sendcloud MCP Server
  slug: sendcloud
modified: '2026-05-25'
name: Sendcloud
nav: Providers
network: true
overview: 'Sendcloud publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Address API, Analytics API, Broadcast API, and 23 more. Tagged areas include Shipping, Logistics, E-Commerce, Carrier, and Labels.


  The Sendcloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sendcloud''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, engineering blog, and 43 more developer resources.'
plans:
- name: Sendcloud Plans Pricing
  plan_count: 6
  slug: sendcloud-plans-pricing
- name: Sendcloud Price Estimates
  plan_count: 0
  slug: sendcloud-price-estimates
random_paper: 15
rate_limits:
- limit_count: 3
  name: Sendcloud Rate Limits
  slug: sendcloud-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sendcloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sendcloud-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Sendcloud API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 8
  slug: sendcloud-rules
scopes:
- name: Sendcloud Scopes
  scope_count: 1
  slug: sendcloud-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 96.0
    catalog_earned_first_party: 24.0
    catalog_gap: 19.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 57.9
    contract_governance: 27.3
    contract_quality: 70.4
    developer_ergonomics: 69.0
    discoverability: 80.0
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 96.2
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 32.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/sendcloud/refs/heads/main/screenshots/sendcloud-2026-06-20T193651.png
security:
- kind: authentication
  name: Sendcloud Authentication
  slug: sendcloud-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Sendcloud Domain Security
  slug: sendcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sendcloud Trust Center
  slug: sendcloud-trust-center
  summary_line: ISO 27001, GDPR
slug: sendcloud
solutions:
- description: EUR 33/month - 400 labels/month, 3 integrations, branded tracking.
  name: Lite
- description: EUR 99/month - 1,000 labels/month, Pack & Go, WhatsApp notifications.
  name: Growth
- description: EUR 195/month - 10,000 labels/month, return management module, analytics.
  name: Premium
- description: EUR 799/month - 30,000 labels/month, dedicated CSM, marketplace solutions.
  name: Pro
- description: Custom volumes, SLAs, custom development.
  name: Enterprise
tags:
- Shipping
- Logistics
- E-Commerce
- Carrier
- Labels
- Returns
- Tracking
- Europe
- A2A
use_cases:
- description: Direct-to-consumer brands shipping across the EU from a central warehouse.
  name: European D2C fulfillment
- description: UK / EU cross-border shipping with customs documents and carrier routing.
  name: Cross-border ecommerce
- description: Brands selling on Amazon, eBay, Etsy, and Bol.com aggregating fulfillment in one platform.
  name: Marketplace shipping
- description: Warehouse providers calling Sendcloud on behalf of multiple merchants via the Integrations API and Sendcloud-Partner-Id header.
  name: 3PL / WMS integration
- description: Merchant-branded tracking, return portal, and notifications.
  name: Branded post-purchase experience
- description: Self-service returns with multi-method drop-off / pickup.
  name: Returns automation
website: https://www.sendcloud.com
---
