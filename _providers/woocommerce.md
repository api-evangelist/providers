---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Woocommerce Agentic Access
  operation_count: 81
  slug: woocommerce-agentic-access
  summary_line: 81 operations · 39 acting
api_count: 2
apis:
- description: WooCommerce delivers real-time event notifications via HTTP POST webhooks for orders, products, customers, coupons, and subscriptions lifecycle changes. Webhooks are configured in the WooCommerce admi
  name: WooCommerce Webhook Events
  slug: webhook-events
- description: 'WooCommerce GraphQL support is provided by the WPGraphQL WooCommerce extension (WooGraphQL), an open-source WordPress plugin that exposes the full WooCommerce data model through a GraphQL endpoint at '
  name: WooCommerce GraphQL API
  slug: graphql-api
- description: Manage the current shopper's cart session including items, coupons, and shipping
  name: WooCommerce Cart API
  slug: woocommerce-cart-api
- description: Submit and manage the checkout process for the current shopper
  name: WooCommerce Checkout API
  slug: woocommerce-checkout-api
- description: Create, retrieve, update, and delete discount coupons
  name: WooCommerce Coupons API
  slug: woocommerce-coupons-api
- description: Create, retrieve, update, and delete customer accounts
  name: WooCommerce Customers API
  slug: woocommerce-customers-api
- description: Manage private and customer-facing notes on orders
  name: WooCommerce Order Notes API
  slug: woocommerce-order-notes-api
- description: Create and retrieve refunds associated with orders
  name: WooCommerce Order Refunds API
  slug: woocommerce-order-refunds-api
- description: Create, retrieve, update, and delete customer orders
  name: WooCommerce Orders API
  slug: woocommerce-orders-api
- description: Retrieve and configure available payment gateways
  name: WooCommerce Payment Gateways API
  slug: woocommerce-payment-gateways-api
- description: Retrieve global product attributes and their terms for filtering
  name: WooCommerce Product Attributes API
  slug: woocommerce-product-attributes-api
- description: Manage product categories used to organize the store catalog
  name: WooCommerce Product Categories API
  slug: woocommerce-product-categories-api
- description: Retrieve customer reviews on products
  name: WooCommerce Product Reviews API
  slug: woocommerce-product-reviews-api
- description: Retrieve product tags for filtering
  name: WooCommerce Product Tags API
  slug: woocommerce-product-tags-api
- description: Manage variations of variable products including price, stock, and attributes
  name: WooCommerce Product Variations API
  slug: woocommerce-product-variations-api
- description: Create, retrieve, update, and delete store products and their variations
  name: WooCommerce Products API
  slug: woocommerce-products-api
- description: Retrieve aggregated sales, product, and customer report data
  name: WooCommerce Reports API
  slug: woocommerce-reports-api
- description: Manage shipping zones, their locations, and shipping methods
  name: WooCommerce Shipping Zones API
  slug: woocommerce-shipping-zones-api
- description: Retrieve system environment, active plugins, and store configuration status
  name: WooCommerce System Status API
  slug: woocommerce-system-status-api
- description: Manage tax rates and tax classes applied at checkout
  name: WooCommerce Tax Rates API
  slug: woocommerce-tax-rates-api
- description: Create and manage webhooks that deliver event notifications to URLs
  name: WooCommerce Webhooks API
  slug: woocommerce-webhooks-api
arazzos:
- description: Create a category, a variable product in it, a variation, and confirm the variation.
  name: WooCommerce Category, Variable Product, and Variation
  slug: woocommerce-category-variable-product-variation-workflow
- description: Create a product category, create a product assigned to it, then read the product back.
  name: WooCommerce Create Category and Product
  slug: woocommerce-create-category-and-product-workflow
- description: Create a customer account and place an order on their behalf, then read the order back.
  name: WooCommerce Create Customer and Order
  slug: woocommerce-create-customer-and-order-workflow
- description: Create a customer with a full billing address, then place an order reusing that address.
  name: WooCommerce Create Customer with Billing and Order
  slug: woocommerce-create-customer-with-billing-order-workflow
- description: Create a parent category, a child category under it, and a product in the child.
  name: WooCommerce Create Nested Category and Product
  slug: woocommerce-create-nested-category-product-workflow
- description: Place an order, mark it completed, then issue a refund against it.
  name: WooCommerce Create Order and Refund
  slug: woocommerce-create-order-and-refund-workflow
- description: Place an order and attach an internal or customer-facing note to it.
  name: WooCommerce Create Order with Note
  slug: woocommerce-create-order-with-note-workflow
- description: Create a product, then create a coupon restricted to that product.
  name: WooCommerce Create Product and Targeted Coupon
  slug: woocommerce-create-product-coupon-workflow
- description: Create a variable product and add a single purchasable variation to it.
  name: WooCommerce Create Variable Product with Variation
  slug: woocommerce-create-variable-product-with-variation-workflow
- description: Onboard a customer, place and complete their order, then refund it end to end.
  name: WooCommerce Customer Order Refund Lifecycle
  slug: woocommerce-customer-order-refund-lifecycle-workflow
- description: Place a guest order, annotate it with a note, then refund it.
  name: WooCommerce Guest Order with Note and Refund
  slug: woocommerce-guest-order-note-refund-workflow
- description: Create a webhook subscribed to an order event and confirm it was registered.
  name: WooCommerce Register Order Webhook
  slug: woocommerce-register-order-webhook-workflow
- description: Find a product category by slug and create it only if it does not already exist.
  name: WooCommerce Upsert Product Category
  slug: woocommerce-upsert-category-workflow
- description: Find a coupon by its code and create it only if it does not already exist.
  name: WooCommerce Upsert Coupon by Code
  slug: woocommerce-upsert-coupon-by-code-workflow
- description: Find a customer by email and create the account only if it does not already exist.
  name: WooCommerce Upsert Customer by Email
  slug: woocommerce-upsert-customer-by-email-workflow
- description: Find a product by its SKU and create it only if no matching product exists.
  name: WooCommerce Upsert Product by SKU
  slug: woocommerce-upsert-product-by-sku-workflow
artifact_total: 305
asyncapis:
- description: The WooCommerce webhook system delivers real-time HTTP POST event notifications to a subscriber-configured endpoint URL whenever specific store events occur. Supported topics cover create, update, del
  name: WooCommerce Webhook Events
  slug: woocommerce-webhooks-asyncapi
collections:
- collection_type: postman
  name: WooCommerce REST API
  slug: postman-woocommerce-rest-api
- collection_type: postman
  name: WooCommerce Store API
  slug: postman-woocommerce-store-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WooCommerce REST Cart API
  slug: open-woocommerce-cart-api
- collection_type: open
  name: WooCommerce REST Cart Checkout API
  slug: open-woocommerce-checkout-api
- collection_type: open
  name: WooCommerce REST Cart Coupons API
  slug: open-woocommerce-coupons-api
- collection_type: open
  name: WooCommerce REST Cart Customers API
  slug: open-woocommerce-customers-api
- collection_type: open
  name: WooCommerce REST Cart Order Notes API
  slug: open-woocommerce-order-notes-api
- collection_type: open
  name: WooCommerce REST Cart Order Refunds API
  slug: open-woocommerce-order-refunds-api
- collection_type: open
  name: WooCommerce REST Cart Orders API
  slug: open-woocommerce-orders-api
- collection_type: open
  name: WooCommerce REST Cart Payment Gateways API
  slug: open-woocommerce-payment-gateways-api
- collection_type: open
  name: WooCommerce REST Cart Product Attributes API
  slug: open-woocommerce-product-attributes-api
- collection_type: open
  name: WooCommerce REST Cart Product Categories API
  slug: open-woocommerce-product-categories-api
- collection_type: open
  name: WooCommerce REST Cart Product Tags API
  slug: open-woocommerce-product-tags-api
- collection_type: open
  name: WooCommerce REST Cart Product Variations API
  slug: open-woocommerce-product-variations-api
- collection_type: open
  name: WooCommerce REST Cart Products API
  slug: open-woocommerce-products-api
- collection_type: open
  name: WooCommerce REST Cart Reports API
  slug: open-woocommerce-reports-api
- collection_type: open
  name: WooCommerce REST API
  slug: open-woocommerce-rest-api
- collection_type: open
  name: WooCommerce REST Cart Shipping Zones API
  slug: open-woocommerce-shipping-zones-api
- collection_type: open
  name: WooCommerce Store API
  slug: open-woocommerce-store-api
- collection_type: open
  name: WooCommerce REST Cart System Status API
  slug: open-woocommerce-system-status-api
- collection_type: open
  name: WooCommerce REST Cart Tax Rates API
  slug: open-woocommerce-tax-rates-api
- collection_type: open
  name: WooCommerce REST Cart Webhooks API
  slug: open-woocommerce-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/woocommerce-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/woocommerce-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/woocommerce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/woocommerce-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/woocommerce/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-category-variable-product-variation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-category-and-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-customer-and-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-customer-with-billing-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-nested-category-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-order-and-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-order-with-note-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-product-coupon-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-create-variable-product-with-variation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-customer-order-refund-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-guest-order-note-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-register-order-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-upsert-category-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-upsert-coupon-by-code-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-upsert-customer-by-email-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/woocommerce-upsert-product-by-sku-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/woocommerce
- group: company
  title: ''
  type: Website
  url: https://woocommerce.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.woocommerce.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.woocommerce.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.woocommerce.com/docs/getting-started/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/woocommerce/woocommerce
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/woocommerce
- group: company
  title: ''
  type: Blog
  url: https://developer.woocommerce.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://woocommerce.com/support/
- group: operate
  title: ''
  type: Forums
  url: https://wordpress.org/support/plugin/woocommerce/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.woocommerce.com/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.woocommerce.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/woocommerce-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/woocommerce-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/woocommerce-vocabulary.yaml
- group: build
  title: WooCommerce REST API JavaScript Library
  type: Tools
  url: https://github.com/woocommerce/woocommerce-rest-api-js-lib
- group: build
  title: WooCommerce REST API PHP Library
  type: Tools
  url: https://github.com/woocommerce/wc-api-php
- group: build
  title: WooCommerce QIT MCP Server
  type: Tools
  url: https://github.com/woocommerce/qit-mcp
- group: build
  title: WooCommerce MCP Ability Plugin
  type: Tools
  url: https://github.com/woocommerce/wc-mcp-ability
- group: build
  title: WooCommerce REST API JS Library (npm)
  type: SDKs
  url: https://www.npmjs.com/package/@woocommerce/woocommerce-rest-api
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/woocommerce/wc-mcp-ability
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.woocommerce.com/llms.txt
created: '2026-05-03'
description: WooCommerce is the world's most popular open-source eCommerce platform, built on WordPress. It provides a comprehensive REST API for managing products, orders, customers, coupons, reports, webhooks, and store settings, plus a public-facing Store API for headless frontends. WooCommerce also delivers real-time events via webhooks for order, product, customer, and subscription lifecycle changes.
examples:
- key_count: 39
  name: Woocommerce Order Example
  slug: woocommerce-order-example
- key_count: 61
  name: Woocommerce Product Example
  slug: woocommerce-product-example
- key_count: 11
  name: Woocommerce Rest Api Address Example
  slug: woocommerce-rest-api-address-example
- key_count: 3
  name: Woocommerce Rest Api Batch Product Request Example
  slug: woocommerce-rest-api-batch-product-request-example
- key_count: 3
  name: Woocommerce Rest Api Batch Product Response Example
  slug: woocommerce-rest-api-batch-product-response-example
- key_count: 17
  name: Woocommerce Rest Api Coupon Example
  slug: woocommerce-rest-api-coupon-example
- key_count: 13
  name: Woocommerce Rest Api Coupon Input Example
  slug: woocommerce-rest-api-coupon-input-example
- key_count: 10
  name: Woocommerce Rest Api Customer Download Example
  slug: woocommerce-rest-api-customer-download-example
- key_count: 15
  name: Woocommerce Rest Api Customer Example
  slug: woocommerce-rest-api-customer-example
- key_count: 8
  name: Woocommerce Rest Api Customer Input Example
  slug: woocommerce-rest-api-customer-input-example
- key_count: 13
  name: Woocommerce Rest Api Line Item Example
  slug: woocommerce-rest-api-line-item-example
- key_count: 3
  name: Woocommerce Rest Api Meta Data Example
  slug: woocommerce-rest-api-meta-data-example
- key_count: 25
  name: Woocommerce Rest Api Order Example
  slug: woocommerce-rest-api-order-example
- key_count: 9
  name: Woocommerce Rest Api Order Input Example
  slug: woocommerce-rest-api-order-input-example
- key_count: 5
  name: Woocommerce Rest Api Order Note Example
  slug: woocommerce-rest-api-order-note-example
- key_count: 3
  name: Woocommerce Rest Api Order Note Input Example
  slug: woocommerce-rest-api-order-note-input-example
- key_count: 7
  name: Woocommerce Rest Api Order Refund Example
  slug: woocommerce-rest-api-order-refund-example
- key_count: 5
  name: Woocommerce Rest Api Order Refund Input Example
  slug: woocommerce-rest-api-order-refund-input-example
- key_count: 9
  name: Woocommerce Rest Api Payment Gateway Example
  slug: woocommerce-rest-api-payment-gateway-example
- key_count: 2
  name: Woocommerce Rest Api Payment Gateway Input Example
  slug: woocommerce-rest-api-payment-gateway-input-example
- key_count: 6
  name: Woocommerce Rest Api Product Attribute Example
  slug: woocommerce-rest-api-product-attribute-example
- key_count: 9
  name: Woocommerce Rest Api Product Category Example
  slug: woocommerce-rest-api-product-category-example
- key_count: 5
  name: Woocommerce Rest Api Product Category Input Example
  slug: woocommerce-rest-api-product-category-input-example
- key_count: 30
  name: Woocommerce Rest Api Product Example
  slug: woocommerce-rest-api-product-example
- key_count: 4
  name: Woocommerce Rest Api Product Image Example
  slug: woocommerce-rest-api-product-image-example
- key_count: 20
  name: Woocommerce Rest Api Product Input Example
  slug: woocommerce-rest-api-product-input-example
- key_count: 13
  name: Woocommerce Rest Api Product Variation Example
  slug: woocommerce-rest-api-product-variation-example
- key_count: 9
  name: Woocommerce Rest Api Product Variation Input Example
  slug: woocommerce-rest-api-product-variation-input-example
- key_count: 11
  name: Woocommerce Rest Api Sales Report Example
  slug: woocommerce-rest-api-sales-report-example
- key_count: 8
  name: Woocommerce Rest Api Shipping Method Example
  slug: woocommerce-rest-api-shipping-method-example
- key_count: 3
  name: Woocommerce Rest Api Shipping Zone Example
  slug: woocommerce-rest-api-shipping-zone-example
- key_count: 3
  name: Woocommerce Rest Api System Status Example
  slug: woocommerce-rest-api-system-status-example
- key_count: 11
  name: Woocommerce Rest Api Tax Rate Example
  slug: woocommerce-rest-api-tax-rate-example
- key_count: 9
  name: Woocommerce Rest Api Webhook Example
  slug: woocommerce-rest-api-webhook-example
- key_count: 5
  name: Woocommerce Rest Api Webhook Input Example
  slug: woocommerce-rest-api-webhook-input-example
- key_count: 5
  name: Woocommerce Store Api Add Cart Item Input Example
  slug: woocommerce-store-api-add-cart-item-input-example
- key_count: 5
  name: Woocommerce Store Api Attribute Term Example
  slug: woocommerce-store-api-attribute-term-example
- key_count: 2
  name: Woocommerce Store Api Cart Customer Input Example
  slug: woocommerce-store-api-cart-customer-input-example
- key_count: 14
  name: Woocommerce Store Api Cart Example
  slug: woocommerce-store-api-cart-example
- key_count: 11
  name: Woocommerce Store Api Cart Item Example
  slug: woocommerce-store-api-cart-item-example
- key_count: 5
  name: Woocommerce Store Api Cart Shipping Rate Example
  slug: woocommerce-store-api-cart-shipping-rate-example
- key_count: 11
  name: Woocommerce Store Api Cart Totals Example
  slug: woocommerce-store-api-cart-totals-example
- key_count: 4
  name: Woocommerce Store Api Checkout Example
  slug: woocommerce-store-api-checkout-example
- key_count: 6
  name: Woocommerce Store Api Checkout Input Example
  slug: woocommerce-store-api-checkout-input-example
- key_count: 9
  name: Woocommerce Store Api Checkout Order Example
  slug: woocommerce-store-api-checkout-order-example
- key_count: 3
  name: Woocommerce Store Api Product Collection Data Example
  slug: woocommerce-store-api-product-collection-data-example
- key_count: 11
  name: Woocommerce Store Api Store Address Example
  slug: woocommerce-store-api-store-address-example
- key_count: 5
  name: Woocommerce Store Api Store Brand Example
  slug: woocommerce-store-api-store-brand-example
- key_count: 8
  name: Woocommerce Store Api Store Order Example
  slug: woocommerce-store-api-store-order-example
- key_count: 6
  name: Woocommerce Store Api Store Product Attribute Example
  slug: woocommerce-store-api-store-product-attribute-example
- key_count: 8
  name: Woocommerce Store Api Store Product Category Example
  slug: woocommerce-store-api-store-product-category-example
- key_count: 23
  name: Woocommerce Store Api Store Product Example
  slug: woocommerce-store-api-store-product-example
- key_count: 7
  name: Woocommerce Store Api Store Product Image Example
  slug: woocommerce-store-api-store-product-image-example
- key_count: 10
  name: Woocommerce Store Api Store Product Price Example
  slug: woocommerce-store-api-store-product-price-example
- key_count: 6
  name: Woocommerce Store Api Store Product Tag Example
  slug: woocommerce-store-api-store-product-tag-example
- key_count: 7
  name: Woocommerce Store Api Store Review Example
  slug: woocommerce-store-api-store-review-example
- key_count: 13
  name: Woocommerce Webhook Example
  slug: woocommerce-webhook-example
features:
- Free open-source WordPress plugin
- 0% revenue share, no platform fees
- 'Hosting: $25-$350/month from chosen provider'
- 'Payment processing: ~2.50%-2.90% + $0.30 (gateway-dependent)'
- 'Extensions: $29-$299/year each'
- REST API at /wp-json/wc/v3/
- OAuth 1.0a + WooCommerce Consumer Keys
- Webhooks for order, customer, product events
- Bulk operations up to 100 items/request
- WordPress ecosystem of themes and plugins
- WooCommerce Stripe, WooPayments, PayPal, Square gateways
- WooCommerce Subscriptions for recurring billing
- WooCommerce Shipping for label printing
- WooCommerce Marketplace for extensions
- Multilingual via WPML/Polylang
- Run multiple gateways simultaneously
finops:
- name: Woocommerce Finops
  service_category: E-Commerce
  slug: woocommerce-finops
graphqls:
- description: WooCommerce provides GraphQL support via the **WPGraphQL WooCommerce** extension (also known as **WooGraphQL**). This is an open-source WordPress plugin that exposes WooCommerce store data through a G
  name: WooCommerce GraphQL
  slug: woocommerce-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/woocommerce.png
integrations:
- description: WooCommerce runs as a WordPress plugin and uses the WordPress REST API infrastructure.
  name: WordPress
- description: Official PayPal payment gateway integration for WooCommerce.
  name: PayPal
- description: Official Stripe payment gateway integration.
  name: Stripe
- description: Order fulfillment and shipping integration.
  name: ShipStation
- description: Email marketing integration for customer segmentation and abandoned cart.
  name: Mailchimp
- description: Official Reddit for WooCommerce integration for ad conversion tracking.
  name: Reddit Ads
- description: Official Pinterest for WooCommerce integration for product sync.
  name: Pinterest
json_schemas:
- name: WooCommerce Order
  property_count: 39
  slug: woocommerce-order
- name: WooCommerce Product
  property_count: 61
  slug: woocommerce-product
- name: Address
  property_count: 11
  slug: woocommerce-rest-api-address
- name: BatchProductRequest
  property_count: 3
  slug: woocommerce-rest-api-batch-product-request
- name: BatchProductResponse
  property_count: 3
  slug: woocommerce-rest-api-batch-product-response
- name: CouponInput
  property_count: 13
  slug: woocommerce-rest-api-coupon-input
- name: Coupon
  property_count: 17
  slug: woocommerce-rest-api-coupon
- name: CustomerDownload
  property_count: 10
  slug: woocommerce-rest-api-customer-download
- name: CustomerInput
  property_count: 8
  slug: woocommerce-rest-api-customer-input
- name: Customer
  property_count: 15
  slug: woocommerce-rest-api-customer
- name: LineItem
  property_count: 13
  slug: woocommerce-rest-api-line-item
- name: MetaData
  property_count: 3
  slug: woocommerce-rest-api-meta-data
- name: OrderInput
  property_count: 9
  slug: woocommerce-rest-api-order-input
- name: OrderNoteInput
  property_count: 3
  slug: woocommerce-rest-api-order-note-input
- name: OrderNote
  property_count: 5
  slug: woocommerce-rest-api-order-note
- name: OrderRefundInput
  property_count: 5
  slug: woocommerce-rest-api-order-refund-input
- name: OrderRefund
  property_count: 7
  slug: woocommerce-rest-api-order-refund
- name: Order
  property_count: 25
  slug: woocommerce-rest-api-order
- name: PaymentGatewayInput
  property_count: 2
  slug: woocommerce-rest-api-payment-gateway-input
- name: PaymentGateway
  property_count: 9
  slug: woocommerce-rest-api-payment-gateway
- name: ProductAttribute
  property_count: 6
  slug: woocommerce-rest-api-product-attribute
- name: ProductCategoryInput
  property_count: 5
  slug: woocommerce-rest-api-product-category-input
- name: ProductCategory
  property_count: 9
  slug: woocommerce-rest-api-product-category
- name: ProductImage
  property_count: 4
  slug: woocommerce-rest-api-product-image
- name: ProductInput
  property_count: 20
  slug: woocommerce-rest-api-product-input
- name: Product
  property_count: 30
  slug: woocommerce-rest-api-product
- name: ProductVariationInput
  property_count: 9
  slug: woocommerce-rest-api-product-variation-input
- name: ProductVariation
  property_count: 13
  slug: woocommerce-rest-api-product-variation
- name: SalesReport
  property_count: 11
  slug: woocommerce-rest-api-sales-report
- name: ShippingMethod
  property_count: 8
  slug: woocommerce-rest-api-shipping-method
- name: ShippingZone
  property_count: 3
  slug: woocommerce-rest-api-shipping-zone
- name: SystemStatus
  property_count: 3
  slug: woocommerce-rest-api-system-status
- name: TaxRate
  property_count: 11
  slug: woocommerce-rest-api-tax-rate
- name: WebhookInput
  property_count: 5
  slug: woocommerce-rest-api-webhook-input
- name: Webhook
  property_count: 9
  slug: woocommerce-rest-api-webhook
- name: AddCartItemInput
  property_count: 5
  slug: woocommerce-store-api-add-cart-item-input
- name: AttributeTerm
  property_count: 5
  slug: woocommerce-store-api-attribute-term
- name: CartCustomerInput
  property_count: 2
  slug: woocommerce-store-api-cart-customer-input
- name: CartItem
  property_count: 11
  slug: woocommerce-store-api-cart-item
- name: Cart
  property_count: 14
  slug: woocommerce-store-api-cart
- name: CartShippingRate
  property_count: 5
  slug: woocommerce-store-api-cart-shipping-rate
- name: CartTotals
  property_count: 11
  slug: woocommerce-store-api-cart-totals
- name: CheckoutInput
  property_count: 6
  slug: woocommerce-store-api-checkout-input
- name: CheckoutOrder
  property_count: 9
  slug: woocommerce-store-api-checkout-order
- name: Checkout
  property_count: 4
  slug: woocommerce-store-api-checkout
- name: ProductCollectionData
  property_count: 3
  slug: woocommerce-store-api-product-collection-data
- name: StoreAddress
  property_count: 11
  slug: woocommerce-store-api-store-address
- name: StoreBrand
  property_count: 5
  slug: woocommerce-store-api-store-brand
- name: StoreOrder
  property_count: 8
  slug: woocommerce-store-api-store-order
- name: StoreProductAttribute
  property_count: 6
  slug: woocommerce-store-api-store-product-attribute
- name: StoreProductCategory
  property_count: 8
  slug: woocommerce-store-api-store-product-category
- name: StoreProductImage
  property_count: 7
  slug: woocommerce-store-api-store-product-image
- name: StoreProductPrice
  property_count: 10
  slug: woocommerce-store-api-store-product-price
- name: StoreProduct
  property_count: 23
  slug: woocommerce-store-api-store-product
- name: StoreProductTag
  property_count: 6
  slug: woocommerce-store-api-store-product-tag
- name: StoreReview
  property_count: 7
  slug: woocommerce-store-api-store-review
- name: WooCommerce Webhook
  property_count: 13
  slug: woocommerce-webhook
json_structures:
- name: Woocommerce Order Structure
  property_count: 39
  slug: woocommerce-order-structure
- name: Woocommerce Product Structure
  property_count: 61
  slug: woocommerce-product-structure
- name: Woocommerce Rest Api Address Structure
  property_count: 11
  slug: woocommerce-rest-api-address-structure
- name: Woocommerce Rest Api Batch Product Request Structure
  property_count: 3
  slug: woocommerce-rest-api-batch-product-request-structure
- name: Woocommerce Rest Api Batch Product Response Structure
  property_count: 3
  slug: woocommerce-rest-api-batch-product-response-structure
- name: Woocommerce Rest Api Coupon Input Structure
  property_count: 13
  slug: woocommerce-rest-api-coupon-input-structure
- name: Woocommerce Rest Api Coupon Structure
  property_count: 17
  slug: woocommerce-rest-api-coupon-structure
- name: Woocommerce Rest Api Customer Download Structure
  property_count: 10
  slug: woocommerce-rest-api-customer-download-structure
- name: Woocommerce Rest Api Customer Input Structure
  property_count: 8
  slug: woocommerce-rest-api-customer-input-structure
- name: Woocommerce Rest Api Customer Structure
  property_count: 15
  slug: woocommerce-rest-api-customer-structure
- name: Woocommerce Rest Api Line Item Structure
  property_count: 13
  slug: woocommerce-rest-api-line-item-structure
- name: Woocommerce Rest Api Meta Data Structure
  property_count: 3
  slug: woocommerce-rest-api-meta-data-structure
- name: Woocommerce Rest Api Order Input Structure
  property_count: 9
  slug: woocommerce-rest-api-order-input-structure
- name: Woocommerce Rest Api Order Note Input Structure
  property_count: 3
  slug: woocommerce-rest-api-order-note-input-structure
- name: Woocommerce Rest Api Order Note Structure
  property_count: 5
  slug: woocommerce-rest-api-order-note-structure
- name: Woocommerce Rest Api Order Refund Input Structure
  property_count: 5
  slug: woocommerce-rest-api-order-refund-input-structure
- name: Woocommerce Rest Api Order Refund Structure
  property_count: 7
  slug: woocommerce-rest-api-order-refund-structure
- name: Woocommerce Rest Api Order Structure
  property_count: 25
  slug: woocommerce-rest-api-order-structure
- name: Woocommerce Rest Api Payment Gateway Input Structure
  property_count: 2
  slug: woocommerce-rest-api-payment-gateway-input-structure
- name: Woocommerce Rest Api Payment Gateway Structure
  property_count: 9
  slug: woocommerce-rest-api-payment-gateway-structure
- name: Woocommerce Rest Api Product Attribute Structure
  property_count: 6
  slug: woocommerce-rest-api-product-attribute-structure
- name: Woocommerce Rest Api Product Category Input Structure
  property_count: 5
  slug: woocommerce-rest-api-product-category-input-structure
- name: Woocommerce Rest Api Product Category Structure
  property_count: 9
  slug: woocommerce-rest-api-product-category-structure
- name: Woocommerce Rest Api Product Image Structure
  property_count: 4
  slug: woocommerce-rest-api-product-image-structure
- name: Woocommerce Rest Api Product Input Structure
  property_count: 20
  slug: woocommerce-rest-api-product-input-structure
- name: Woocommerce Rest Api Product Structure
  property_count: 30
  slug: woocommerce-rest-api-product-structure
- name: Woocommerce Rest Api Product Variation Input Structure
  property_count: 9
  slug: woocommerce-rest-api-product-variation-input-structure
- name: Woocommerce Rest Api Product Variation Structure
  property_count: 13
  slug: woocommerce-rest-api-product-variation-structure
- name: Woocommerce Rest Api Sales Report Structure
  property_count: 11
  slug: woocommerce-rest-api-sales-report-structure
- name: Woocommerce Rest Api Shipping Method Structure
  property_count: 8
  slug: woocommerce-rest-api-shipping-method-structure
- name: Woocommerce Rest Api Shipping Zone Structure
  property_count: 3
  slug: woocommerce-rest-api-shipping-zone-structure
- name: Woocommerce Rest Api System Status Structure
  property_count: 3
  slug: woocommerce-rest-api-system-status-structure
- name: Woocommerce Rest Api Tax Rate Structure
  property_count: 11
  slug: woocommerce-rest-api-tax-rate-structure
- name: Woocommerce Rest Api Webhook Input Structure
  property_count: 5
  slug: woocommerce-rest-api-webhook-input-structure
- name: Woocommerce Rest Api Webhook Structure
  property_count: 9
  slug: woocommerce-rest-api-webhook-structure
- name: Woocommerce Store Api Add Cart Item Input Structure
  property_count: 5
  slug: woocommerce-store-api-add-cart-item-input-structure
- name: Woocommerce Store Api Attribute Term Structure
  property_count: 5
  slug: woocommerce-store-api-attribute-term-structure
- name: Woocommerce Store Api Cart Customer Input Structure
  property_count: 2
  slug: woocommerce-store-api-cart-customer-input-structure
- name: Woocommerce Store Api Cart Item Structure
  property_count: 11
  slug: woocommerce-store-api-cart-item-structure
- name: Woocommerce Store Api Cart Shipping Rate Structure
  property_count: 5
  slug: woocommerce-store-api-cart-shipping-rate-structure
- name: Woocommerce Store Api Cart Structure
  property_count: 14
  slug: woocommerce-store-api-cart-structure
- name: Woocommerce Store Api Cart Totals Structure
  property_count: 11
  slug: woocommerce-store-api-cart-totals-structure
- name: Woocommerce Store Api Checkout Input Structure
  property_count: 6
  slug: woocommerce-store-api-checkout-input-structure
- name: Woocommerce Store Api Checkout Order Structure
  property_count: 9
  slug: woocommerce-store-api-checkout-order-structure
- name: Woocommerce Store Api Checkout Structure
  property_count: 4
  slug: woocommerce-store-api-checkout-structure
- name: Woocommerce Store Api Product Collection Data Structure
  property_count: 3
  slug: woocommerce-store-api-product-collection-data-structure
- name: Woocommerce Store Api Store Address Structure
  property_count: 11
  slug: woocommerce-store-api-store-address-structure
- name: Woocommerce Store Api Store Brand Structure
  property_count: 5
  slug: woocommerce-store-api-store-brand-structure
- name: Woocommerce Store Api Store Order Structure
  property_count: 8
  slug: woocommerce-store-api-store-order-structure
- name: Woocommerce Store Api Store Product Attribute Structure
  property_count: 6
  slug: woocommerce-store-api-store-product-attribute-structure
- name: Woocommerce Store Api Store Product Category Structure
  property_count: 8
  slug: woocommerce-store-api-store-product-category-structure
- name: Woocommerce Store Api Store Product Image Structure
  property_count: 7
  slug: woocommerce-store-api-store-product-image-structure
- name: Woocommerce Store Api Store Product Price Structure
  property_count: 10
  slug: woocommerce-store-api-store-product-price-structure
- name: Woocommerce Store Api Store Product Structure
  property_count: 23
  slug: woocommerce-store-api-store-product-structure
- name: Woocommerce Store Api Store Product Tag Structure
  property_count: 6
  slug: woocommerce-store-api-store-product-tag-structure
- name: Woocommerce Store Api Store Review Structure
  property_count: 7
  slug: woocommerce-store-api-store-review-structure
- name: Woocommerce Webhook Structure
  property_count: 13
  slug: woocommerce-webhook-structure
jsonld:
- class_count: 0
  name: Woocommerce Context
  property_count: 8
  slug: woocommerce-context
- class_count: 4
  name: Woocommerce Order Schema.Json Context
  property_count: 36
  slug: woocommerce-order-schema.json-context
- class_count: 5
  name: Woocommerce Product Schema.Json Context
  property_count: 57
  slug: woocommerce-product-schema.json-context
- class_count: 2
  name: Woocommerce Rest Api Batch Product Context
  property_count: 3
  slug: woocommerce-rest-api-batch-product-context
- class_count: 11
  name: Woocommerce Rest Api Context
  property_count: 81
  slug: woocommerce-rest-api-context
- class_count: 2
  name: Woocommerce Rest Api Coupon Context
  property_count: 12
  slug: woocommerce-rest-api-coupon-context
- class_count: 4
  name: Woocommerce Rest Api Customer Context
  property_count: 25
  slug: woocommerce-rest-api-customer-context
- class_count: 2
  name: Woocommerce Rest Api Line Context
  property_count: 12
  slug: woocommerce-rest-api-line-context
- class_count: 1
  name: Woocommerce Rest Api Meta Context
  property_count: 3
  slug: woocommerce-rest-api-meta-context
- class_count: 5
  name: Woocommerce Rest Api Order Context
  property_count: 25
  slug: woocommerce-rest-api-order-context
- class_count: 1
  name: Woocommerce Rest Api Order Note Context
  property_count: 3
  slug: woocommerce-rest-api-order-note-context
- class_count: 1
  name: Woocommerce Rest Api Order Refund Context
  property_count: 5
  slug: woocommerce-rest-api-order-refund-context
- class_count: 2
  name: Woocommerce Rest Api Payment Context
  property_count: 8
  slug: woocommerce-rest-api-payment-context
- class_count: 1
  name: Woocommerce Rest Api Payment Gateway Context
  property_count: 2
  slug: woocommerce-rest-api-payment-gateway-context
- class_count: 3
  name: Woocommerce Rest Api Product Category Context
  property_count: 3
  slug: woocommerce-rest-api-product-category-context
- class_count: 7
  name: Woocommerce Rest Api Product Context
  property_count: 33
  slug: woocommerce-rest-api-product-context
- class_count: 2
  name: Woocommerce Rest Api Product Variation Context
  property_count: 12
  slug: woocommerce-rest-api-product-variation-context
- class_count: 1
  name: Woocommerce Rest Api Sales Context
  property_count: 11
  slug: woocommerce-rest-api-sales-context
- class_count: 3
  name: Woocommerce Rest Api Shipping Context
  property_count: 8
  slug: woocommerce-rest-api-shipping-context
- class_count: 3
  name: Woocommerce Rest Api System Context
  property_count: 14
  slug: woocommerce-rest-api-system-context
- class_count: 2
  name: Woocommerce Rest Api Tax Context
  property_count: 10
  slug: woocommerce-rest-api-tax-context
- class_count: 2
  name: Woocommerce Rest Api Webhook Context
  property_count: 4
  slug: woocommerce-rest-api-webhook-context
- class_count: 1
  name: Woocommerce Store Api Add Cart Item Context
  property_count: 5
  slug: woocommerce-store-api-add-cart-item-context
- class_count: 3
  name: Woocommerce Store Api Attribute Context
  property_count: 3
  slug: woocommerce-store-api-attribute-context
- class_count: 3
  name: Woocommerce Store Api Cart Context
  property_count: 33
  slug: woocommerce-store-api-cart-context
- class_count: 2
  name: Woocommerce Store Api Cart Customer Context
  property_count: 12
  slug: woocommerce-store-api-cart-customer-context
- class_count: 2
  name: Woocommerce Store Api Cart Shipping Context
  property_count: 10
  slug: woocommerce-store-api-cart-shipping-context
- class_count: 3
  name: Woocommerce Store Api Checkout Context
  property_count: 24
  slug: woocommerce-store-api-checkout-context
- class_count: 3
  name: Woocommerce Store Api Context
  property_count: 37
  slug: woocommerce-store-api-context
- class_count: 1
  name: Woocommerce Store Api Product Collection Context
  property_count: 5
  slug: woocommerce-store-api-product-collection-context
- class_count: 10
  name: Woocommerce Store Api Store Context
  property_count: 61
  slug: woocommerce-store-api-store-context
- class_count: 7
  name: Woocommerce Store Api Store Product Context
  property_count: 26
  slug: woocommerce-store-api-store-product-context
- class_count: 4
  name: Woocommerce Webhook Schema.Json Context
  property_count: 10
  slug: woocommerce-webhook-schema.json-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: WooCommerce
nav: Providers
network: true
overview: 'WooCommerce publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Webhook Events, Cart API, Checkout API, and 17 more. Tagged areas include E-Commerce, Open-Source, Order, Product, and WordPress.


  The WooCommerce catalog on APIs.io includes 1 event-driven AsyncAPI specification, 33 JSON-LD contexts, and 3 Spectral governance rulesets.


  WooCommerce''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, engineering blog, support, release notes, and 36 more developer resources.'
plans:
- name: Woocommerce Plans Pricing
  plan_count: 4
  slug: woocommerce-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Woocommerce Rate Limits
  slug: woocommerce-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: WooCommerce API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: woocommerce-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: WooCommerce API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: woocommerce-jsonschema-spectral-rules
- effective_rule_count: 86
  extends:
  - spectral:oas
  name: WooCommerce API Rules
  rule_count: 45
  severity_counts:
    error: 12
    hint: 0
    info: 5
    warn: 28
  slug: woocommerce-spectral-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 80.7
    developer_ergonomics: 69.0
    discoverability: 61.1
    governance: 28.8
    operational_transparency: 34.2
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/woocommerce/refs/heads/main/screenshots/woocommerce-2026-06-20T201543.png
security:
- kind: authentication
  name: Woocommerce Authentication
  slug: woocommerce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Woocommerce Domain Security
  slug: woocommerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Woocommerce Vulnerability Disclosure
  slug: woocommerce-vulnerability-disclosure
  summary_line: Hackerone
slug: woocommerce
tags:
- E-Commerce
- Open-Source
- Order
- Product
- WordPress
use_cases:
- description: Build custom React or Vue frontends using the Store API for products, cart, and checkout.
  name: Headless Storefront
- description: Sync orders and inventory with ERP systems via the REST API and webhooks.
  name: ERP Integration
- description: Automate order fulfillment workflows using webhook notifications and REST API updates.
  name: Order Fulfillment
- description: Sync product catalog from a PIM system to WooCommerce via the REST API.
  name: Product Catalog Sync
- description: Pull sales reports and customer data via the Reports API for BI tools.
  name: Analytics and Reporting
website: https://woocommerce.com
---
