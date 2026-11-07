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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1985
  human_in_the_loop: 18
  name: Shopify Agentic Access
  operation_count: 4988
  slug: shopify-agentic-access
  summary_line: 4988 operations · 1985 acting · 18 human-in-the-loop
api_count: 3
apis:
- description: The GraphQL Admin API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillment, and more. GraphQL is th
  name: Shopify GraphQL Admin API
  slug: graphql-admin-api
- description: The Storefront API is a GraphQL API that provides commerce primitives to build custom, scalable, and performant shopping experiences on any platform, including the web, apps, and games. It enables cus
  name: Shopify Storefront API
  slug: storefront-api
- description: The Customer Account API offers a secure way to access private customer-scoped data, enabling you to build personalized, customer-authenticated experiences in your custom storefronts or apps. Customer
  name: Shopify Customer Account API
  slug: customer-account-api
- description: The Partner API provides access to data in the Partners Dashboard, including transactions that impact your earnings, app events, and for participating partners, Experts Marketplace opportunities. It i
  name: Shopify Partner API
  slug: partner-api
- description: The Payments Apps API enables approved Shopify Payments Partners to access their Shopify Payments account and payments app configuration data. It provides access to payment sessions and allows buildin
  name: Shopify Payments Apps API
  slug: payments-apps-api
- description: Liquid is a template language created by Shopify and available as an open source project on GitHub. The Liquid reference documents the tags, filters, and objects that you can use to build Shopify them
  name: Shopify Liquid API
  slug: liquid-api
- description: Shopify Functions allow developers to customize the backend logic that powers parts of Shopify. Functions are compiled to WebAssembly and enable custom discounts, payment customizations, delivery cust
  name: Shopify Functions API
  slug: functions-api
- description: The Discount Function API enables developers to create a single discount that applies to cart lines, order subtotals, and shipping rates. It replaces the previous separate Product, Order, and Shipping
  name: Shopify Discount Function API
  slug: discount-function-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Shopify webhooks enable apps to receive notifications about particular events in a shop. They are useful for keeping your app in sync with Shopify data or as a trigger to perform additional actions af
  name: Shopify Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List my app's webhook subscriptions
    question: Which webhook subscriptions has my app registered with the store?
  - id: createWebhook
    intent: Subscribe to a store event with a webhook
    question: How do I get notified at my own URL whenever a store event happens?
  - id: getWebhookCount
    intent: Count webhook subscriptions
    question: How many webhook subscriptions does my app currently have?
  - id: getWebhook
    intent: Get one webhook subscription
    question: Where is a particular webhook subscription sending its events?
  - id: updateWebhook
    intent: Change an existing webhook subscription
    question: My endpoint moved; can I point an existing webhook at a new address?
  - id: deleteWebhook
    intent: Delete a webhook subscription
    question: How can I stop receiving events for a webhook I no longer need?
  phrasing_ops: 6
  slug: webhooks-api
- description: Shopify App Bridge enables apps to render UI in the Shopify app home surface and seamlessly integrate with the Shopify admin. It provides APIs for navigation menus, save bars, title bars, toast notifi
  name: Shopify App Bridge
  slug: app-bridge
- description: The App Home API provides the surface where apps render their main UI within the Shopify admin. It supports Polaris web components for building consistent, accessible interfaces that integrate seamles
  name: Shopify App Home API
  slug: app-home-api
- description: Checkout UI extensions let app developers build custom functionality that merchants can install at defined points in the checkout flow, including product information, shipping, payment, order summary,
  name: Shopify Checkout UI Extensions API
  slug: checkout-ui-extensions-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Multipass login is for store owners who have a separate website and a Shopify store, enabling seamless single sign-on by redirecting users and automatically logging them in. Requires a Shopify Plus pl
  name: Shopify Multipass API
  phrasing_intents:
  - id: multipassLogin
    intent: Log a customer in with a Multipass token
    question: How do I sign a customer into the storefront from my own site using Multipass?
  phrasing_ops: 1
  slug: multipass-api
- description: POS UI extensions enable app developers to build custom functionality for Shopify Point of Sale. Extensions can add functionality to the cart, post- purchase, and other POS surfaces for in-person reta
  name: Shopify POS UI Extensions API
  slug: pos-ui-extensions-api
- description: Admin UI extensions allow developers to extend the Shopify admin with custom UI components. Extensions can render in product details, order details, customer details, and other admin surfaces.
  name: Shopify Admin Extensions API
  slug: admin-extensions-api
- description: Hydrogen is Shopify's React-based framework for building custom storefronts powered by the Storefront API. It provides commerce-optimized components, hooks, and utilities for building fast, dynamic he
  name: Shopify Hydrogen
  slug: hydrogen
- description: 'Polaris is Shopify''s unified UI framework built on web components for delivering a consistent experience across the platform. It provides a library of UI components, tokens, and icons that developers '
  name: Shopify Polaris
  slug: polaris
- description: Shopify CLI is a command-line tool that helps developers create Shopify apps, themes, and custom storefronts. It accelerates development with scaffolding, local development servers, and deployment too
  name: Shopify CLI
  slug: shopify-cli
- description: The About API from Shopify — 6 operation(s) for about.
  name: Shopify About API
  phrasing_intents:
  - id: deprecated_202001_get_users_current
    intent: Get the staff account behind my token (API 2020-01)
    question: Which Shopify staff user is my access token acting as, on version 2020-01?
  - id: deprecated_202004_get_users_current
    intent: Get the staff account behind my token (API 2020-04)
    question: Whose account does my current access token belong to under the 2020-04 release?
  - id: deprecated_202007_get_users_current
    intent: Get the staff account behind my token (API 2020-07)
    question: Is there a way to confirm which admin user an access token maps to in 2020-07?
  - id: get_users_current
    intent: Get the staff account behind my token (API 2020-10)
    question: How do I find out which user my online access token is logged in as on 2020-10?
  - id: deprecated_202101_get_users_current
    intent: Get the staff account behind my token (API 2021-01)
    question: What user account is attached to the access token I use with 2021-01?
  - id: deprecated_unstable_get_users_current
    intent: Get the staff account behind my token (unstable API)
    question: Which user does the unstable API say owns my access token?
  phrasing_ops: 6
  slug: shopify-about-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage access scopes and tokens
  name: Shopify Access API
  phrasing_intents:
  - id: listAccessScopes
    intent: See which access scopes my token has
    question: Which permissions has the merchant actually granted my app's access token?
  - id: deprecated_202001_create_storefront_access_tokens
    intent: Issue a Storefront access token (API 2020-01)
    question: How can I generate a new Storefront API token through the 2020-01 Admin API?
  - id: deprecated_202001_get_storefront_access_tokens
    intent: List Storefront access tokens (API 2020-01)
    question: Which Storefront API tokens has my app issued, according to the 2020-01 Admin API?
  - id: deprecated_202001_delete_storefront_access_tokens_param_storefront_access_token_id
    intent: Revoke a Storefront access token (API 2020-01)
    question: How can I revoke a leaked Storefront API token on the 2020-01 Admin API?
  - id: deprecated_202004_create_storefront_access_tokens
    intent: Issue a Storefront access token (API 2020-04)
    question: What's the 2020-04 call for creating a Storefront API access token?
  - id: deprecated_202004_get_storefront_access_tokens
    intent: List Storefront access tokens (API 2020-04)
    question: What storefront access tokens exist for my app on API version 2020-04?
  - id: deprecated_202004_delete_storefront_access_tokens_param_storefront_access_token_id
    intent: Revoke a Storefront access token (API 2020-04)
    question: What's the 2020-04 way to remove a storefront access token I no longer use?
  - id: deprecated_202007_create_storefront_access_tokens
    intent: Issue a Storefront access token (API 2020-07)
    question: Using the 2020-07 release, can my app create its own Storefront API token?
  phrasing_ops: 19
  slug: shopify-access-api
- description: The Account API from Shopify — 12 operation(s) for account.
  name: Shopify Account API
  phrasing_intents:
  - id: deprecated_202001_create_customers_param_customer_id_account_activation_url
    intent: Get a customer account activation link (API 2020-01)
    question: How do I generate an activation URL for a customer who hasn't activated their account, on API 2020-01?
  - id: deprecated_202001_create_customers_param_customer_id_send_invite
    intent: Email a customer an account invite (API 2020-01)
    question: Which 2020-01 call emails a customer an invitation to create their store account?
  - id: deprecated_202004_create_customers_param_customer_id_account_activation_url
    intent: Get a customer account activation link (API 2020-04)
    question: What April 2020 endpoint returns an activation URL for a customer whose account is still disabled?
  - id: deprecated_202004_create_customers_param_customer_id_send_invite
    intent: Email a customer an account invite (API 2020-04)
    question: How can I send a customer their account invite email with the April 2020 API?
  - id: deprecated_202007_create_customers_param_customer_id_account_activation_url
    intent: Get a customer account activation link (API 2020-07)
    question: Where do I get an account activation URL for an unactivated customer on the July 2020 API?
  - id: deprecated_202007_create_customers_param_customer_id_send_invite
    intent: Email a customer an account invite (API 2020-07)
    question: What's the July 2020 call to email a customer an account invite?
  - id: create_customers_param_customer_id_account_activation_url
    intent: Get a customer account activation link (API 2020-10)
    question: How do I get an activation URL for a customer who never activated their account, on the 2020-10 API?
  - id: create_customers_param_customer_id_send_invite
    intent: Email a customer an account invite (API 2020-10)
    question: Can I email a customer an invite to activate their account with the current 2020-10 API?
  phrasing_ops: 12
  slug: shopify-account-api
- description: The Active API from Shopify — 6 operation(s) for active.
  name: Shopify Active API
  phrasing_intents:
  - id: deprecated_202001_update_recurring_application_charges_param_recurring_application_charge_id_customize
    intent: Raise an app subscription's usage cap (2020-01)
    question: How do I change the capped amount on an active recurring app charge with API version 2020-01?
  - id: deprecated_202004_update_recurring_application_charges_param_recurring_application_charge_id_customize
    intent: Change a recurring charge's capped amount (2020-04)
    question: Which 2020-04 call adjusts the maximum a usage-based app subscription can bill?
  - id: deprecated_202007_update_recurring_application_charges_param_recurring_application_charge_id_customize
    intent: Update the cap on an active app charge (2020-07)
    question: Does the 2020-07 API let me lift the capped amount of a recurring charge that's already active?
  - id: update_recurring_application_charges_param_recurring_application_charge_id_customize
    intent: Update a recurring charge's capped amount (2020-10)
    question: Can I update the capped amount of an active recurring charge on the current 2020-10 version?
  - id: deprecated_202101_update_recurring_application_charges_param_recurring_application_charge_id_customize
    intent: Customize an active charge's cap (2021-01)
    question: Is changing a recurring application charge's capped amount possible with version 2021-01?
  - id: deprecated_unstable_update_recurring_application_charges_param_recurring_application_charge_id_customize
    intent: Update a recurring charge's cap (unstable version)
    question: Can I test raising a recurring charge's capped amount against the unstable API version?
  phrasing_ops: 6
  slug: shopify-active-api
- description: The Address API from Shopify — 30 operation(s) for address.
  name: Shopify Address API
  phrasing_intents:
  - id: deprecated_202001_create_customers_param_customer_id_addresses
    intent: Add an address to a customer (2020-01 API)
    question: How do I add a new shipping address to a customer on the 2020-01 Admin API?
  - id: deprecated_202001_get_customers_param_customer_id_addresses_param_address_id
    intent: Look up one customer address (2020-01 API)
    question: How do I fetch a single saved address for a customer on the 2020-01 API?
  - id: deprecated_202001_update_customers_param_customer_id_addresses_param_address_id
    intent: Edit a customer address (2020-01 API)
    question: How do I correct a typo in a customer's saved address on the 2020-01 API?
  - id: deprecated_202001_delete_customers_param_customer_id_addresses_param_address_id
    intent: Remove a customer address (2020-01 API)
    question: How do I delete an outdated address from a customer's address list on 2020-01?
  - id: deprecated_202001_update_customers_param_customer_id_addresses_param_address_id_default
    intent: Set a customer's default address (2020-01 API)
    question: How do I make one of a customer's saved addresses their default on 2020-01?
  - id: deprecated_202004_create_customers_param_customer_id_addresses
    intent: Add an address to a customer (2020-04 API)
    question: What call on the 2020-04 release adds an extra address to a shopper's account?
  - id: deprecated_202004_get_customers_param_customer_id_addresses_param_address_id
    intent: Look up one customer address (2020-04 API)
    question: Can I read one specific address off a customer in the 2020-04 release?
  - id: deprecated_202004_update_customers_param_customer_id_addresses_param_address_id
    intent: Edit a customer address (2020-04 API)
    question: Which 2020-04 call modifies an address a customer already has on file?
  phrasing_ops: 42
  slug: shopify-address-api
- description: The Addresses API from Shopify — 12 operation(s) for addresses.
  name: Shopify Addresses API
  phrasing_intents:
  - id: deprecated_202001_get_customers_param_customer_id_addresses
    intent: List a customer's addresses (API 2020-01)
    question: How can I see every shipping and billing address saved for a customer on the 2020-01 API?
  - id: deprecated_202001_update_customers_param_customer_id_addresses_set
    intent: Bulk-change a customer's addresses (API 2020-01)
    question: Can I remove several of a customer's saved addresses in one call on the 2020-01 API?
  - id: deprecated_202004_get_customers_param_customer_id_addresses
    intent: List a customer's addresses (API 2020-04)
    question: What addresses does a customer have on file, per API version 2020-04?
  - id: deprecated_202004_update_customers_param_customer_id_addresses_set
    intent: Bulk-change a customer's addresses (API 2020-04)
    question: Is it possible to clean up a batch of a customer's old addresses together on 2020-04?
  - id: deprecated_202007_get_customers_param_customer_id_addresses
    intent: List a customer's addresses (API 2020-07)
    question: Using the 2020-07 release, where do I read all of a customer's addresses?
  - id: deprecated_202007_update_customers_param_customer_id_addresses_set
    intent: Bulk-change a customer's addresses (API 2020-07)
    question: Using the 2020-07 release, can I act on many customer addresses in a single request?
  - id: get_customers_param_customer_id_addresses
    intent: List a customer's addresses (current 2020-10)
    question: Which call lists a customer's addresses on the current 2020-10 version?
  - id: update_customers_param_customer_id_addresses_set
    intent: Bulk-change a customer's addresses (current 2020-10)
    question: Which call performs a bulk operation on a customer's addresses on the current 2020-10 version?
  phrasing_ops: 12
  slug: shopify-addresses-api
- description: The Admin API from Shopify — 6 operation(s) for admin.
  name: Shopify Admin API
  phrasing_intents:
  - id: deprecated_202001_update_metafields_param_metafield_id
    intent: Update a metafield (API 2020-01)
    question: How do I change an existing metafield using the 2020-01 Admin API?
  - id: deprecated_202004_update_metafields_param_metafield_id
    intent: Update a metafield (API 2020-04)
    question: Which April 2020 (2020-04) endpoint modifies a metafield that already exists?
  - id: deprecated_202007_update_metafields_param_metafield_id
    intent: Update a metafield (API 2020-07)
    question: My integration targets 2020-07; what updates a metafield there?
  - id: update_metafields_param_metafield_id
    intent: Update a metafield (API 2020-10)
    question: What is the 2020-10 call for revising a metafield?
  - id: deprecated_202101_update_metafields_param_metafield_id
    intent: Update a metafield (API 2021-01)
    question: Under the 2021-01 Admin API, where do I update a metafield?
  - id: deprecated_unstable_update_metafields_param_metafield_id
    intent: Update a metafield (unstable API)
    question: Is there an unstable-channel endpoint for updating a metafield?
  phrasing_ops: 6
  slug: shopify-admin-api
- description: The All API from Shopify — 107 operation(s) for all.
  name: Shopify All API
  phrasing_intents:
  - id: deprecated_202001_get_application_credits
    intent: List app credits issued (API 2020-01)
    question: Which application credits has my app granted to merchants on API version 2020-01?
  - id: deprecated_202004_get_application_credits
    intent: List app credits issued (API 2020-04)
    question: What credits have I given merchants toward my app fees, per release 2020-04?
  - id: deprecated_202007_get_application_credits
    intent: List app credits issued (API 2020-07)
    question: How can I review the app credits my app has handed out with version 2020-07?
  - id: get_application_credits
    intent: List app credits issued (API 2020-10)
    question: What application credits has my Shopify app issued to shops?
  - id: deprecated_202101_get_application_credits
    intent: List app credits issued (API 2021-01)
    question: Which credits toward future app charges exist, according to the 2021-01 release?
  - id: deprecated_unstable_get_application_credits
    intent: List app credits issued (unstable API)
    question: What app credits does the unstable API version report for my app?
  - id: deprecated_202001_get_customers_count
    intent: Count all customers (API 2020-01)
    question: How many customers does my store have, counted with API 2020-01?
  - id: deprecated_202001_get_customers_param_customer_id_orders
    intent: List a customer's orders (API 2020-01)
    question: What orders has one specific customer placed, per API version 2020-01?
  phrasing_ops: 107
  slug: shopify-all-api
- description: The Another API from Shopify — 12 operation(s) for another.
  name: Shopify Another API
  phrasing_intents:
  - id: deprecated_202001_update_orders_param_order_id_risks_param_risk_id
    intent: Update an order risk (2020-01 API)
    question: How do I change a fraud risk assessment my app recorded on an order, on 2020-01?
  - id: deprecated_202001_delete_orders_param_order_id_risks_param_risk_id
    intent: Delete an order risk (2020-01 API)
    question: How do I remove a fraud risk my app placed on an order, on the 2020-01 API?
  - id: deprecated_202004_update_orders_param_order_id_risks_param_risk_id
    intent: Update an order risk (2020-04 API)
    question: Which 2020-04 call modifies an existing order risk?
  - id: deprecated_202004_delete_orders_param_order_id_risks_param_risk_id
    intent: Delete an order risk (2020-04 API)
    question: Which 2020-04 endpoint deletes an order risk?
  - id: deprecated_202007_update_orders_param_order_id_risks_param_risk_id
    intent: Update an order risk (2020-07 API)
    question: Where do I update an order's risk entry in version 2020-07?
  - id: deprecated_202007_delete_orders_param_order_id_risks_param_risk_id
    intent: Delete an order risk (2020-07 API)
    question: Where is the 2020-07 call that throws away a risk flagged on an order?
  - id: update_orders_param_order_id_risks_param_risk_id
    intent: Update an order risk (2020-10 API)
    question: How can my fraud app revise the risk it flagged on an order using the 2020-10 API?
  - id: delete_orders_param_order_id_risks_param_risk_id
    intent: Delete an order risk (2020-10 API)
    question: How can I clear a risk flag my app raised on an order with the 2020-10 API?
  phrasing_ops: 18
  slug: shopify-another-api
- description: The Applications API from Shopify — 86 operation(s) for applications.
  name: Shopify Applications API
  phrasing_intents:
  - id: deprecated_202001_get_reports_param_report_id
    intent: Get one of my app's reports (API 2020-01)
    question: How do I pull up a single report my app created on the 2020-01 Admin API?
  - id: deprecated_202004_get_reports_param_report_id
    intent: Get one of my app's reports (API 2020-04)
    question: Which call returns a report my app made when I'm pinned to API version 2020-04?
  - id: deprecated_202007_get_reports_param_report_id
    intent: Get one of my app's reports (API 2020-07)
    question: Where do I read back a report my app built, using the July 2020 Admin API?
  - id: get_reports_param_report_id
    intent: Get one of my app's reports (API 2020-10)
    question: What's the current 2020-10 way to retrieve a report my app created?
  - id: deprecated_202101_get_reports_param_report_id
    intent: Get one of my app's reports (API 2021-01)
    question: How can I look at one app report via the 2021-01 Admin API release?
  - id: deprecated_unstable_get_reports_param_report_id
    intent: Get one of my app's reports (unstable API)
    question: Can I retrieve a single app report through the unstable Admin API version?
  - id: deprecated_202001_create_application_charges
    intent: Bill a shop a one-time app charge (API 2020-01)
    question: How do I charge a merchant a single one-off fee for my app on the 2020-01 API?
  - id: deprecated_202001_get_application_charges
    intent: List one-time app charges (API 2020-01)
    question: How do I see every one-time charge my app has billed a shop, on API 2020-01?
  phrasing_ops: 104
  slug: shopify-applications-api
- description: The Approves API from Shopify — 1 operation(s) for approves.
  name: Shopify Approves API
  phrasing_intents:
  - id: deprecated_202001_create_comments_param_comment_id_approve
    intent: Approve a blog comment (API 2020-01)
    question: How can I approve a pending blog comment on my online store with the 2020-01 API?
  phrasing_ops: 1
  slug: shopify-approves-api
- description: The Article API from Shopify — 20 operation(s) for article.
  name: Shopify Article API
  phrasing_intents:
  - id: deprecated_202001_create_blogs_param_blog_id_articles
    intent: Publish a new article to a blog (2020-01)
    question: Can I post a new article to my store blog with the 2020-01 Admin API?
  - id: deprecated_202001_get_blogs_param_blog_id_articles_param_article_id
    intent: Get a blog article (2020-01)
    question: How do I read one article from a blog with the 2020-01 API?
  - id: deprecated_202001_update_blogs_param_blog_id_articles_param_article_id
    intent: Update a blog article (2020-01)
    question: Can I edit a published blog article with the 2020-01 API?
  - id: deprecated_202001_delete_blogs_param_blog_id_articles_param_article_id
    intent: Delete a blog article (2020-01)
    question: How do I delete an article from a blog on 2020-01?
  - id: deprecated_202004_create_blogs_param_blog_id_articles
    intent: Publish a new article to a blog (2020-04)
    question: Which 2020-04 endpoint creates a blog article?
  - id: deprecated_202004_get_blogs_param_blog_id_articles_param_article_id
    intent: Get a blog article (2020-04)
    question: Which 2020-04 call retrieves a single blog article?
  - id: deprecated_202004_update_blogs_param_blog_id_articles_param_article_id
    intent: Update a blog article (2020-04)
    question: Which 2020-04 call modifies a blog article?
  - id: deprecated_202004_delete_blogs_param_blog_id_articles_param_article_id
    intent: Delete a blog article (2020-04)
    question: Which 2020-04 call removes an article from a blog?
  phrasing_ops: 26
  slug: shopify-article-api
- description: The Assets API from Shopify — 6 operation(s) for assets.
  name: Shopify Assets API
  phrasing_intents:
  - id: deprecated_202001_get_themes_param_theme_id_assets
    intent: Read one theme file by its key (API 2020-01)
    question: How can I read the contents of a single Liquid template in my theme on API 2020-01?
  - id: deprecated_202001_update_themes_param_theme_id_assets
    intent: Create or update a theme file (API 2020-01)
    question: Can I upload an image into my theme from a URL with release 2020-01?
  - id: deprecated_202001_delete_themes_param_theme_id_assets
    intent: Delete a file from a theme (API 2020-01)
    question: How do I remove an unused snippet from a theme with API 2020-01?
  - id: deprecated_202004_get_themes_param_theme_id_assets
    intent: Read one theme file by its key (API 2020-04)
    question: What's inside a specific stylesheet or template of my theme, read through 2020-04?
  - id: deprecated_202004_update_themes_param_theme_id_assets
    intent: Create or update a theme file (API 2020-04)
    question: Which 2020-04 call adds or overwrites a file in a theme?
  - id: deprecated_202004_delete_themes_param_theme_id_assets
    intent: Delete a file from a theme (API 2020-04)
    question: Can I delete a leftover template from my theme through version 2020-04?
  - id: deprecated_202007_get_themes_param_theme_id_assets
    intent: Read one theme file by its key (API 2020-07)
    question: Where do I get the source of one theme template using 2020-07?
  - id: deprecated_202007_update_themes_param_theme_id_assets
    intent: Create or update a theme file (API 2020-07)
    question: Is there a 2020-07 endpoint to write a new asset into a theme?
  phrasing_ops: 18
  slug: shopify-assets-api
- description: The Associated API from Shopify — 31 operation(s) for associated.
  name: Shopify Associated API
  phrasing_intents:
  - id: deprecated_202001_get_orders_param_order_id_fulfillments
    intent: List an order's fulfillments (2020-01 API)
    question: How do I see every shipment made against an order on the 2020-01 API?
  - id: deprecated_202001_get_fulfillment_orders_param_fulfillment_order_id_fulfillments
    intent: List a fulfillment order's fulfillments (2020-01)
    question: How do I see the fulfillments created from one fulfillment order on 2020-01?
  - id: deprecated_202001_get_orders_param_order_id_fulfillments_count
    intent: Count an order's fulfillments (2020-01 API)
    question: How do I find out how many fulfillments an order has on the 2020-01 API?
  - id: deprecated_202001_update_orders_param_order_id_fulfillments_param_fulfillment_id
    intent: Update a fulfillment on an order (2020-01 API)
    question: How do I change the information on a fulfillment I already created, on 2020-01?
  - id: deprecated_202004_get_orders_param_order_id_fulfillments
    intent: List an order's fulfillments (2020-04 API)
    question: Which fulfillments has an order had so far, per the 2020-04 release?
  - id: deprecated_202004_get_fulfillment_orders_param_fulfillment_order_id_fulfillments
    intent: List a fulfillment order's fulfillments (2020-04)
    question: Which fulfillments belong to a specific fulfillment order under the 2020-04 release?
  - id: deprecated_202004_get_orders_param_order_id_fulfillments_count
    intent: Count an order's fulfillments (2020-04 API)
    question: What's the number of fulfillments on a given order, per the 2020-04 release?
  - id: deprecated_202004_update_orders_param_order_id_fulfillments_param_fulfillment_id
    intent: Update a fulfillment on an order (2020-04 API)
    question: Which 2020-04 call modifies an existing fulfillment on an order?
  phrasing_ops: 24
  slug: shopify-associated-api
- description: The Available API from Shopify — 6 operation(s) for available.
  name: Shopify Available API
  phrasing_intents:
  - id: deprecated_202001_get_checkouts_param_token_shipping_rates
    intent: List shipping rates for a checkout (API 2020-01)
    question: How do I see which shipping rates are available for a checkout on the 2020-01 API?
  - id: deprecated_202004_get_checkouts_param_token_shipping_rates
    intent: List shipping rates for a checkout (API 2020-04)
    question: Which April 2020 (2020-04) endpoint returns the shipping rates for a checkout?
  - id: deprecated_202007_get_checkouts_param_token_shipping_rates
    intent: List shipping rates for a checkout (API 2020-07)
    question: My sales channel targets 2020-07; what lists shipping rates for a checkout there?
  - id: get_checkouts_param_token_shipping_rates
    intent: List shipping rates for a checkout (API 2020-10)
    question: What is the 2020-10 call for getting available shipping rates on a checkout?
  - id: deprecated_202101_get_checkouts_param_token_shipping_rates
    intent: List shipping rates for a checkout (API 2021-01)
    question: Under the 2021-01 API, where do I look up shipping rates for a checkout?
  - id: deprecated_unstable_get_checkouts_param_token_shipping_rates
    intent: List shipping rates for a checkout (unstable API)
    question: Is there an unstable-channel endpoint for a checkout's shipping rates?
  phrasing_ops: 6
  slug: shopify-available-api
- description: The Balance API from Shopify — 7 operation(s) for balance.
  name: Shopify Balance API
  phrasing_intents:
  - id: deprecated_202001_get_shopify_payments_balance
    intent: Check the Shopify Payments balance (2020-01)
    question: How do I see my current Shopify Payments balance with API version 2020-01?
  - id: deprecated_202004_get_shopify_payments_balance
    intent: Get the payments account balance (2020-04)
    question: Which 2020-04 endpoint tells me how much money is in my payments account?
  - id: deprecated_202007_get_shopify_payments_balance
    intent: Read the current payments balance (2020-07)
    question: What does the 2020-07 API return for my payments balance?
  - id: get_shopify_payments_balance
    intent: Retrieve the payments balance (2020-10, current)
    question: What's my current balance, per the non-deprecated 2020-10 API?
  - id: deprecated_202101_get_shopify_payments_balance
    intent: Fetch the payments balance (2021-01)
    question: Can version 2021-01 return the payments account's current balance?
  - id: deprecated_unstable_get_shopify_payments_balance
    intent: Get the payments balance (unstable version)
    question: Can I read my payments balance from the unstable API version?
  phrasing_ops: 6
  slug: shopify-balance-api
- description: The Belong API from Shopify — 6 operation(s) for belong.
  name: Shopify Belong API
  phrasing_intents:
  - id: deprecated_202001_get_metafields
    intent: List metafields attached to a resource (2020-01)
    question: How do I list the metafields on a product image with the 2020-01 API?
  - id: deprecated_202004_get_metafields
    intent: List metafields attached to a resource (2020-04)
    question: Can I read extra data stored on a product image using release 2020-04?
  - id: deprecated_202007_get_metafields
    intent: List metafields attached to a resource (2020-07)
    question: Is there a 2020-07 endpoint to list metafields for a given owner?
  - id: get_metafields
    intent: List metafields attached to a resource
    question: What call lists a resource's metafields in the 2020-10 Admin API?
  - id: deprecated_202101_get_metafields
    intent: List metafields attached to a resource (2021-01)
    question: Does the January 2021 (2021-01) API let me list metafields by owner?
  - id: deprecated_unstable_get_metafields
    intent: List metafields attached to a resource (unstable)
    question: Can I list metafields through the unstable Admin API?
  phrasing_ops: 6
  slug: shopify-belong-api
- description: The Belonging API from Shopify — 12 operation(s) for belonging.
  name: Shopify Belonging API
  phrasing_intents:
  - id: deprecated_202001_get_collections_param_collection_id_products
    intent: List products in a collection (2020-01)
    question: How do I see which products belong to a collection using the 2020-01 API?
  - id: deprecated_202004_get_collections_param_collection_id_products
    intent: List products in a collection (2020-04)
    question: Which 2020-04 call returns the products inside a collection?
  - id: deprecated_202007_get_collections_param_collection_id_products
    intent: List products in a collection (2020-07)
    question: What 2020-07 endpoint lists a collection's products?
  - id: get_collections_param_collection_id_products
    intent: List products in a collection (2020-10)
    question: How can I list the products belonging to a collection on the 2020-10 API?
  - id: deprecated_202101_get_collections_param_collection_id_products
    intent: List products in a collection (2021-01)
    question: Is there a 2021-01 call to see all products in a collection?
  - id: deprecated_unstable_get_collections_param_collection_id_products
    intent: List products in a collection (unstable)
    question: Does the unstable API list the products that belong to a collection?
  phrasing_ops: 6
  slug: shopify-belonging-api
- description: The Blog API from Shopify — 14 operation(s) for blog.
  name: Shopify Blog API
  phrasing_intents:
  - id: deprecated_202001_create_blogs
    intent: Create a new store blog
    question: How do I start a brand-new blog on my online store with the 2020-01 API?
  - id: deprecated_202001_get_blogs_param_blog_id
    intent: Get a blog by ID
    question: Can I look up a single blog's settings by its ID?
  - id: deprecated_202001_update_blogs_param_blog_id
    intent: Update a blog
    question: How can I rename or change the settings of an existing blog?
  - id: deprecated_202001_delete_blogs_param_blog_id
    intent: Delete a blog
    question: How do I permanently remove a whole blog from my store?
  phrasing_ops: 4
  slug: shopify-blog-api
- description: The Cancel API from Shopify — 6 operation(s) for cancel.
  name: Shopify Cancel API
  phrasing_intents:
  - id: deprecated_202001_create_orders_param_order_id_fulfillments_param_fulfillment_id_cancel
    intent: Cancel an order fulfillment (API 2020-01)
    question: How do I cancel a fulfillment on an order using the 2020-01 Admin API?
  - id: deprecated_202004_create_orders_param_order_id_fulfillments_param_fulfillment_id_cancel
    intent: Cancel an order fulfillment (API 2020-04)
    question: Which April 2020 (2020-04) endpoint cancels a fulfillment that belongs to an order?
  - id: deprecated_202007_create_orders_param_order_id_fulfillments_param_fulfillment_id_cancel
    intent: Cancel an order fulfillment (API 2020-07)
    question: My app is pinned to 2020-07; what cancels a fulfillment there?
  - id: create_orders_param_order_id_fulfillments_param_fulfillment_id_cancel
    intent: Cancel an order fulfillment (API 2020-10)
    question: What is the 2020-10 way to cancel a fulfillment on one of my orders?
  - id: deprecated_202101_create_orders_param_order_id_fulfillments_param_fulfillment_id_cancel
    intent: Cancel an order fulfillment (API 2021-01)
    question: Under the 2021-01 Admin API, where do I cancel an order's fulfillment?
  - id: deprecated_unstable_create_orders_param_order_id_fulfillments_param_fulfillment_id_cancel
    intent: Cancel an order fulfillment (unstable API)
    question: Is there an unstable-channel endpoint for cancelling a fulfillment on an order?
  phrasing_ops: 6
  slug: shopify-cancel-api
- description: The Cancels API from Shopify — 12 operation(s) for cancels.
  name: Shopify Cancels API
  phrasing_intents:
  - id: deprecated_202001_create_fulfillments_param_fulfillment_id_cancel
    intent: Cancel a fulfillment (2020-01 API)
    question: How do I cancel a shipment I fulfilled by mistake on the 2020-01 API?
  - id: deprecated_202004_create_fulfillments_param_fulfillment_id_cancel
    intent: Cancel a fulfillment (2020-04 API)
    question: Which 2020-04 endpoint cancels a fulfillment?
  - id: deprecated_202007_create_fulfillments_param_fulfillment_id_cancel
    intent: Cancel a fulfillment (2020-07 API)
    question: Where do I cancel a fulfillment in version 2020-07?
  - id: create_fulfillments_param_fulfillment_id_cancel
    intent: Cancel a fulfillment (2020-10 API)
    question: How can I cancel a fulfillment that shouldn't have been created, using the 2020-10 API?
  - id: deprecated_202101_create_fulfillments_param_fulfillment_id_cancel
    intent: Cancel a fulfillment (2021-01 API)
    question: Can I cancel a fulfillment using the 2021-01 release?
  - id: deprecated_unstable_create_fulfillments_param_fulfillment_id_cancel
    intent: Cancel a fulfillment (unstable API)
    question: Is cancelling a fulfillment possible on the unstable API version?
  phrasing_ops: 6
  slug: shopify-cancels-api
- description: The Card API from Shopify — 24 operation(s) for card.
  name: Shopify Card API
  phrasing_intents:
  - id: deprecated_202001_create_gift_cards
    intent: Issue a new gift card (2020-01)
    question: How do I issue a new gift card with API version 2020-01?
  - id: deprecated_202001_get_gift_cards_param_gift_card_id
    intent: Retrieve a gift card by ID (2020-01)
    question: Can I look up a single gift card by its ID on API version 2020-01?
  - id: deprecated_202001_update_gift_cards_param_gift_card_id
    intent: Update a gift card (2020-01)
    question: Can I change an existing gift card through API version 2020-01?
  - id: deprecated_202001_create_gift_cards_param_gift_card_id_disable
    intent: Disable a gift card (2020-01)
    question: How do I disable a gift card so it can no longer be used, on 2020-01?
  - id: deprecated_202004_create_gift_cards
    intent: Create a gift card (2020-04)
    question: Can I create a gift card programmatically with the 2020-04 release?
  - id: deprecated_202004_get_gift_cards_param_gift_card_id
    intent: Get a gift card's details (2020-04)
    question: Where do I read one gift card's details on the 2020-04 release?
  - id: deprecated_202004_update_gift_cards_param_gift_card_id
    intent: Modify an existing gift card (2020-04)
    question: Can release 2020-04 modify a gift card after it has been issued?
  - id: deprecated_202004_create_gift_cards_param_gift_card_id_disable
    intent: Deactivate a gift card (2020-04)
    question: Which 2020-04 call stops a gift card from being redeemed?
  phrasing_ops: 30
  slug: shopify-card-api
- description: The Cards API from Shopify — 18 operation(s) for cards.
  name: Shopify Cards API
  phrasing_intents:
  - id: deprecated_202001_get_gift_cards
    intent: List gift cards (API 2020-01)
    question: Which gift cards has my Shopify Plus store issued, per API 2020-01?
  - id: deprecated_202001_get_gift_cards_count
    intent: Count gift cards (API 2020-01)
    question: How many gift cards exist in my store according to API 2020-01?
  - id: deprecated_202001_get_gift_cards_search
    intent: Search gift cards (API 2020-01)
    question: Can I search gift cards by code or balance with the 2020-01 API?
  - id: deprecated_202004_get_gift_cards
    intent: List gift cards (API 2020-04)
    question: What gift cards does version 2020-04 list for my shop?
  - id: deprecated_202004_get_gift_cards_count
    intent: Count gift cards (API 2020-04)
    question: What is the total number of gift cards on my store with version 2020-04?
  - id: deprecated_202004_get_gift_cards_search
    intent: Search gift cards (API 2020-04)
    question: Is there a 2020-04 search that finds a gift card from part of its code?
  - id: deprecated_202007_get_gift_cards
    intent: List gift cards (API 2020-07)
    question: Can I list every gift card in my store with API 2020-07?
  - id: deprecated_202007_get_gift_cards_count
    intent: Count gift cards (API 2020-07)
    question: How many enabled gift cards does my shop have on API 2020-07?
  phrasing_ops: 18
  slug: shopify-cards-api
- description: The Carrier API from Shopify — 12 operation(s) for carrier.
  name: Shopify Carrier API
  phrasing_intents:
  - id: deprecated_202001_create_carrier_services
    intent: Register a carrier service (2020-01 API)
    question: How do I add a carrier service so checkout can request live shipping rates on 2020-01?
  - id: deprecated_202001_get_carrier_services
    intent: List carrier services (2020-01 API)
    question: How do I see every carrier service registered on my store with the 2020-01 API?
  - id: deprecated_202001_update_carrier_services_param_carrier_service_id
    intent: Edit a carrier service (2020-01 API)
    question: How do I change the settings of an existing carrier service on the 2020-01 API?
  - id: deprecated_202001_get_carrier_services_param_carrier_service_id
    intent: Look up one carrier service (2020-01 API)
    question: How do I fetch a single carrier service by its ID on the 2020-01 API?
  - id: deprecated_202001_delete_carrier_services_param_carrier_service_id
    intent: Delete a carrier service (2020-01 API)
    question: How do I remove a carrier service I no longer need on the 2020-01 API?
  - id: deprecated_202004_create_carrier_services
    intent: Register a carrier service (2020-04 API)
    question: Which 2020-04 call sets up a new carrier service for calculated shipping?
  - id: deprecated_202004_get_carrier_services
    intent: List carrier services (2020-04 API)
    question: What carrier services does my store currently have under the 2020-04 release?
  - id: deprecated_202004_update_carrier_services_param_carrier_service_id
    intent: Edit a carrier service (2020-04 API)
    question: Which 2020-04 call modifies a carrier service that already exists?
  phrasing_ops: 30
  slug: shopify-carrier-api
- baseURL_template: https://{store}.myshopify.com
  baseurl_source: spec_template
  description: Manage the shopping cart
  name: Shopify Cart API
  phrasing_intents:
  - id: getCart
    intent: See what's in the shopper's cart
    question: What's currently in the shopper's cart, with totals and currency?
  - id: addToCart
    intent: Add product variants to the cart
    question: How do I add a product variant to the cart from my theme's JavaScript?
  - id: updateCart
    intent: Update cart quantities, note or discount
    question: Can I apply a discount code to the whole cart?
  - id: changeCartItem
    intent: Change a single cart line item
    question: How do I change the quantity of just one line in the cart?
  - id: clearCart
    intent: Empty the cart
    question: Is there a way to remove every item from the cart at once?
  - id: getCartShippingRates
    intent: Estimate shipping for the cart
    question: How much will shipping cost for this cart to a given postcode?
  phrasing_ops: 6
  slug: shopify-cart-api
- description: The Charge API from Shopify — 42 operation(s) for charge.
  name: Shopify Charge API
  phrasing_intents:
  - id: deprecated_202001_get_recurring_application_charges_param_recurring_application_charge_id
    intent: Get an app subscription charge (2020-01)
    question: How do I check the status of a merchant's recurring app charge with the 2020-01 API?
  - id: deprecated_202004_get_recurring_application_charges_param_recurring_application_charge_id
    intent: Get an app subscription charge (2020-04)
    question: Can I see whether a merchant accepted my app's monthly plan using release 2020-04?
  - id: deprecated_202007_get_recurring_application_charges_param_recurring_application_charge_id
    intent: Get an app subscription charge (2020-07)
    question: Is there a 2020-07 endpoint to retrieve one recurring application charge?
  - id: get_recurring_application_charges_param_recurring_application_charge_id
    intent: Get an app subscription charge
    question: What call retrieves a single recurring application charge in the 2020-10 Admin API?
  - id: deprecated_202101_get_recurring_application_charges_param_recurring_application_charge_id
    intent: Get an app subscription charge (2021-01)
    question: Does the January 2021 (2021-01) API let me view a recurring app charge?
  - id: deprecated_unstable_get_recurring_application_charges_param_recurring_application_charge_id
    intent: Get an app subscription charge (unstable)
    question: Can I retrieve a recurring application charge through the unstable Admin API?
  - id: deprecated_202001_create_recurring_application_charges_param_recurring_application_charge_id_usage_charges
    intent: Bill a usage charge on an app plan (2020-01)
    question: How do I bill a merchant for metered usage on top of their app plan with the 2020-01 API?
  - id: deprecated_202001_get_recurring_application_charges_param_recurring_application_charge_id_usage_charges_param_usage_charge_id
    intent: Get one usage charge (2020-01)
    question: How do I look up a single usage charge I billed with the 2020-01 API?
  phrasing_ops: 18
  slug: shopify-charge-api
- description: The Charges API from Shopify — 18 operation(s) for charges.
  name: Shopify Charges API
  phrasing_intents:
  - id: deprecated_202001_get_recurring_application_charges_param_recurring_application_charge_id_usage_charges
    intent: List usage charges on a subscription (API 2020-01)
    question: What usage charges has my app billed against a recurring charge on API 2020-01?
  - id: deprecated_202004_get_recurring_application_charges_param_recurring_application_charge_id_usage_charges
    intent: List usage charges on a subscription (API 2020-04)
    question: How do I see metered fees added to an app subscription through release 2020-04?
  - id: deprecated_202007_get_recurring_application_charges_param_recurring_application_charge_id_usage_charges
    intent: List usage charges on a subscription (API 2020-07)
    question: Can I review the usage-based fees on an app's recurring charge with 2020-07?
  - id: get_recurring_application_charges_param_recurring_application_charge_id_usage_charges
    intent: List usage charges on a subscription (API 2020-10)
    question: How do I list the usage charges my app added to a merchant's Shopify subscription?
  - id: deprecated_202101_get_recurring_application_charges_param_recurring_application_charge_id_usage_charges
    intent: List usage charges on a subscription (API 2021-01)
    question: What usage fees has an app subscription accrued, checked via release 2021-01?
  - id: deprecated_unstable_get_recurring_application_charges_param_recurring_application_charge_id_usage_charges
    intent: List usage charges on a subscription (unstable API)
    question: Can the unstable API show usage charges under a recurring application charge?
  phrasing_ops: 6
  slug: shopify-charges-api
- description: The Checkout API from Shopify — 36 operation(s) for checkout.
  name: Shopify Checkout API
  phrasing_intents:
  - id: deprecated_202001_create_checkouts
    intent: Start a new sales-channel checkout (API 2020-01)
    question: How does my sales channel app open a new checkout for a buyer on API 2020-01?
  - id: deprecated_202004_create_checkouts
    intent: Start a new sales-channel checkout (API 2020-04)
    question: Which 2020-04 call begins a checkout session from my sales channel?
  - id: deprecated_202007_create_checkouts
    intent: Start a new sales-channel checkout (API 2020-07)
    question: Can my channel app spin up a checkout for a customer using 2020-07?
  - id: create_checkouts
    intent: Start a new sales-channel checkout (API 2020-10)
    question: How do I create a checkout from a sales channel on 2020-10?
  - id: deprecated_202101_create_checkouts
    intent: Start a new sales-channel checkout (API 2021-01)
    question: Can I start a checkout for a buyer through version 2021-01?
  - id: deprecated_unstable_create_checkouts
    intent: Start a new sales-channel checkout (unstable API)
    question: Can the unstable API create a checkout for my sales channel?
  - id: deprecated_202001_create_checkouts_param_token_complete
    intent: Complete a checkout without payment (API 2020-01)
    question: How do I finish a checkout that needs no payment, like a free order, on 2020-01?
  - id: deprecated_202001_get_checkouts_param_token
    intent: Look up a checkout by token (API 2020-01)
    question: What's in a buyer's checkout right now, like line items and totals, on 2020-01?
  phrasing_ops: 36
  slug: shopify-checkout-api
- description: The Checkouts API from Shopify — 6 operation(s) for checkouts.
  name: Shopify Checkouts API
  phrasing_intents:
  - id: deprecated_202001_get_checkouts_count
    intent: Count abandoned checkouts, last 90 days (API 2020-01)
    question: How many abandoned checkouts has my store had in the past 90 days on API 2020-01?
  - id: deprecated_202004_get_checkouts_count
    intent: Count abandoned checkouts, last 90 days (API 2020-04)
    question: What's the number of carts customers left unfinished recently, per release 2020-04?
  - id: deprecated_202007_get_checkouts_count
    intent: Count abandoned checkouts, last 90 days (API 2020-07)
    question: How big is my abandoned-cart backlog this quarter, according to version 2020-07?
  - id: get_checkouts_count
    intent: Count abandoned checkouts, last 90 days (API 2020-10)
    question: What number of shoppers abandoned checkout over the past 90 days in 2020-10?
  - id: deprecated_202101_get_checkouts_count
    intent: Count abandoned checkouts, last 90 days (API 2021-01)
    question: How many checkouts went unpaid in the last three months, per 2021-01?
  - id: deprecated_unstable_get_checkouts_count
    intent: Count abandoned checkouts, last 90 days (unstable API)
    question: What does the unstable API report as my abandoned checkout count?
  phrasing_ops: 6
  slug: shopify-checkouts-api
- description: The Code API from Shopify — 36 operation(s) for code.
  name: Shopify Code API
  phrasing_intents:
  - id: deprecated_202001_create_price_rules_param_price_rule_id_discount_codes
    intent: Add a discount code to a price rule (2020-01)
    question: How do I add a new discount code to a price rule on the 2020-01 API?
  - id: deprecated_202001_update_price_rules_param_price_rule_id_discount_codes_param_discount_code_id
    intent: Change an existing discount code (2020-01)
    question: How can I edit a discount code that already exists, using the 2020-01 version?
  - id: deprecated_202001_get_price_rules_param_price_rule_id_discount_codes_param_discount_code_id
    intent: Look up one discount code by ID (2020-01)
    question: Can I fetch a single discount code by its ID on API version 2020-01?
  - id: deprecated_202001_delete_price_rules_param_price_rule_id_discount_codes_param_discount_code_id
    intent: Delete a discount code (2020-01)
    question: How do I permanently remove a discount code from a price rule in 2020-01?
  - id: deprecated_202001_get_discount_codes_lookup
    intent: Find where a discount code lives by its code (2020-01)
    question: Given only the text a shopper typed, where does that discount code live according to the 2020-01 lookup?
  - id: deprecated_202001_create_price_rules_param_price_rule_id_batch
    intent: Start a bulk discount code creation job (2020-01)
    question: How can I create many discount codes at once for a price rule on 2020-01?
  - id: deprecated_202001_get_price_rules_param_price_rule_id_batch_param_batch_id
    intent: Check a discount code creation job (2020-01)
    question: What is the status of my bulk discount code job on 2020-01?
  - id: deprecated_202001_get_price_rules_param_price_rule_id_batch_param_batch_id_discount_codes
    intent: List codes produced by a creation job (2020-01)
    question: Which discount codes did my batch creation job produce, using 2020-01?
  phrasing_ops: 48
  slug: shopify-code-api
- description: The Collect API from Shopify — 6 operation(s) for collect.
  name: Shopify Collect API
  phrasing_intents:
  - id: deprecated_202001_get_collects_param_collect_id
    intent: Get a product-to-collection link (API 2020-01)
    question: How do I look up one collect, the link between a product and a custom collection, on API 2020-01?
  - id: deprecated_202004_get_collects_param_collect_id
    intent: Get a product-to-collection link (API 2020-04)
    question: Which April 2020 call tells me which product and collection a collect ties together?
  - id: deprecated_202007_get_collects_param_collect_id
    intent: Get a product-to-collection link (API 2020-07)
    question: Where do I fetch a specific collect by ID on the July 2020 Admin API?
  - id: get_collects_param_collect_id
    intent: Get a product-to-collection link (API 2020-10)
    question: What's the current 2020-10 way to read a single collect?
  - id: deprecated_202101_get_collects_param_collect_id
    intent: Get a product-to-collection link (API 2021-01)
    question: How can I see which collection a product sits in via one collect on 2021-01?
  - id: deprecated_unstable_get_collects_param_collect_id
    intent: Get a product-to-collection link (unstable API)
    question: Can I retrieve a single collect through the unstable Admin API?
  phrasing_ops: 6
  slug: shopify-collect-api
- description: The Collection API from Shopify — 66 operation(s) for collection.
  name: Shopify Collection API
  phrasing_intents:
  - id: deprecated_202001_create_collects
    intent: Add a product to a custom collection (2020-01)
    question: Can I add a product to a custom collection through the 2020-01 Admin API?
  - id: deprecated_202001_delete_collects_param_collect_id
    intent: Remove a product from a collection (2020-01)
    question: How do I take a product out of a collection with the 2020-01 API?
  - id: deprecated_202004_create_collects
    intent: Add a product to a custom collection (2020-04)
    question: Could I put a product into a custom collection with version 2020-04?
  - id: deprecated_202004_delete_collects_param_collect_id
    intent: Remove a product from a collection (2020-04)
    question: What 2020-04 call removes a product from a collection?
  - id: deprecated_202007_create_collects
    intent: Add a product to a custom collection (2020-07)
    question: Which 2020-07 endpoint adds a product to a custom collection?
  - id: deprecated_202007_delete_collects_param_collect_id
    intent: Remove a product from a collection (2020-07)
    question: Which endpoint in 2020-07 drops a product from a collection?
  - id: create_collects
    intent: Add a product to a custom collection (2020-10)
    question: How can I add a product to a custom collection on the 2020-10 API version?
  - id: delete_collects_param_collect_id
    intent: Remove a product from a collection (2020-10)
    question: How can I remove a product from a collection in version 2020-10?
  phrasing_ops: 72
  slug: shopify-collection-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Retrieve collection data
  name: Shopify Collections API
  phrasing_intents:
  - id: getCollection
    intent: Get a collection by ID
    question: What details and metadata does Shopify hold for one of my collections?
  - id: listCollectionProducts
    intent: List the products in a collection
    question: Which products belong to one of my collections?
  - id: deprecated_202001_get_custom_collections
    intent: List custom collections (API 2020-01)
    question: Which manual (custom) collections does my shop have under API 2020-01?
  - id: deprecated_202001_get_custom_collections_count
    intent: Count custom collections (API 2020-01)
    question: How many manual collections are in my store according to API 2020-01?
  - id: deprecated_202004_get_custom_collections
    intent: List custom collections (API 2020-04)
    question: Can I look up a custom collection by its handle using API 2020-04?
  - id: deprecated_202004_get_custom_collections_count
    intent: Count custom collections (API 2020-04)
    question: What is the total number of custom collections in my shop on version 2020-04?
  - id: deprecated_202007_get_custom_collections
    intent: List custom collections (API 2020-07)
    question: Can I list custom collections published within a date range on API 2020-07?
  - id: deprecated_202007_get_custom_collections_count
    intent: Count custom collections (API 2020-07)
    question: How many custom collections were updated in a window, per the 2020-07 count?
  phrasing_ops: 26
  slug: shopify-collections-api
- description: The Comments API from Shopify — 8 operation(s) for comments.
  name: Shopify Comments API
  phrasing_intents:
  - id: deprecated_202001_get_comments
    intent: List blog article comments
    question: Which comments are waiting for moderation on my store's blog?
  - id: deprecated_202001_get_comments_count
    intent: Count blog comments
    question: How many comments has my blog received in total?
  - id: deprecated_202001_get_comments_param_comment_id
    intent: Get a single blog comment
    question: What exactly did a reader write in one particular blog comment?
  - id: deprecated_202001_create_comments_param_comment_id_spam
    intent: Mark a blog comment as spam
    question: What's the way to flag a junk comment on my blog as spam?
  - id: deprecated_202001_create_comments_param_comment_id_not_spam
    intent: Mark a blog comment as not spam
    question: A real reader's comment got caught as spam; can I mark it as legitimate?
  - id: deprecated_202001_create_comments_param_comment_id_remove
    intent: Remove a blog comment
    question: Can I take down an inappropriate comment from a blog article?
  - id: deprecated_202001_create_comments_param_comment_id_restore
    intent: Restore a removed blog comment
    question: I removed a comment by mistake; can I put it back?
  phrasing_ops: 7
  slug: shopify-comments-api
- description: The Complete API from Shopify — 6 operation(s) for complete.
  name: Shopify Complete API
  phrasing_intents:
  - id: deprecated_202001_create_orders_param_order_id_fulfillments_param_fulfillment_id_complete
    intent: Mark a fulfillment complete (2020-01)
    question: How do I mark an order's fulfillment as complete with the 2020-01 API?
  - id: deprecated_202004_create_orders_param_order_id_fulfillments_param_fulfillment_id_complete
    intent: Mark a fulfillment complete (2020-04)
    question: Which 2020-04 call sets a fulfillment's status to complete?
  - id: deprecated_202007_create_orders_param_order_id_fulfillments_param_fulfillment_id_complete
    intent: Mark a fulfillment complete (2020-07)
    question: What 2020-07 endpoint completes a fulfillment on an order?
  - id: create_orders_param_order_id_fulfillments_param_fulfillment_id_complete
    intent: Mark a fulfillment complete (2020-10)
    question: How can I complete a fulfillment for a Shopify order on 2020-10?
  - id: deprecated_202101_create_orders_param_order_id_fulfillments_param_fulfillment_id_complete
    intent: Mark a fulfillment complete (2021-01)
    question: Is there a 2021-01 call to mark a fulfillment complete?
  - id: deprecated_unstable_create_orders_param_order_id_fulfillments_param_fulfillment_id_complete
    intent: Mark a fulfillment complete (unstable)
    question: Does the unstable API let me mark a fulfillment as complete?
  phrasing_ops: 6
  slug: shopify-complete-api
- description: The Configuration API from Shopify — 6 operation(s) for configuration.
  name: Shopify Configuration API
  phrasing_intents:
  - id: deprecated_202001_get_shop
    intent: Get shop configuration (API 2020-01)
    question: What store settings does the 2020-01 API return for my shop?
  - id: deprecated_202004_get_shop
    intent: Get shop configuration (API 2020-04)
    question: Where can I read my store's configuration with the 2020-04 API?
  - id: deprecated_202007_get_shop
    intent: Get shop configuration (API 2020-07)
    question: Can I look up my shop's settings with API 2020-07?
  - id: get_shop
    intent: Get shop configuration (API 2020-10)
    question: What does my Shopify store's configuration look like on API 2020-10?
  - id: deprecated_202101_get_shop
    intent: Get shop configuration (API 2021-01)
    question: Does the 2021-01 API return my shop's configuration?
  - id: deprecated_unstable_get_shop
    intent: Get shop configuration (unstable API)
    question: Can I read my shop's configuration on the unstable API version?
  phrasing_ops: 6
  slug: shopify-configuration-api
- description: The Connects API from Shopify — 6 operation(s) for connects.
  name: Shopify Connects API
  phrasing_intents:
  - id: deprecated_202001_create_inventory_levels_connect
    intent: Stock an inventory item at a location (2020-01)
    question: How do I start tracking an inventory item at a new location on the 2020-01 API?
  - id: deprecated_202004_create_inventory_levels_connect
    intent: Stock an inventory item at a location (2020-04)
    question: Which 2020-04 call creates an inventory level so an item can be stocked at a location?
  - id: deprecated_202007_create_inventory_levels_connect
    intent: Stock an inventory item at a location (2020-07)
    question: Where do I connect an inventory item to a location in version 2020-07?
  - id: create_inventory_levels_connect
    intent: Stock an inventory item at a location (2020-10)
    question: How can I make a product variant stockable at another warehouse using the 2020-10 API?
  - id: deprecated_202101_create_inventory_levels_connect
    intent: Stock an inventory item at a location (2021-01)
    question: Can I connect an inventory item to a location using the 2021-01 release?
  - id: deprecated_unstable_create_inventory_levels_connect
    intent: Stock an inventory item at a location (unstable)
    question: Is connecting an inventory item to a location available on the unstable API?
  phrasing_ops: 6
  slug: shopify-connects-api
- description: The Contains API from Shopify — 6 operation(s) for contains.
  name: Shopify Contains API
  phrasing_intents:
  - id: deprecated_202001_create_themes
    intent: Create a theme from a zip file (2020-01)
    question: How do I upload a new theme from a zip file URL with the 2020-01 API?
  - id: deprecated_202004_create_themes
    intent: Create a theme from a zip file (2020-04)
    question: Can I add a theme to my store from a hosted zip on release 2020-04?
  - id: deprecated_202007_create_themes
    intent: Create a theme from a zip file (2020-07)
    question: Is there a 2020-07 endpoint for creating a theme?
  - id: create_themes
    intent: Create a theme from a zip file
    question: What call creates a theme in the 2020-10 Admin API?
  - id: deprecated_202101_create_themes
    intent: Create a theme from a zip file (2021-01)
    question: Does the January 2021 (2021-01) API let me create themes?
  - id: deprecated_unstable_create_themes
    intent: Create a theme from a zip file (unstable)
    question: Can I create a theme through the unstable Admin API?
  phrasing_ops: 6
  slug: shopify-contains-api
- description: The Count API from Shopify — 121 operation(s) for count.
  name: Shopify Count API
  phrasing_intents:
  - id: deprecated_202001_get_events_count
    intent: Count store events on API version 2020-01
    question: How many events has my shop logged, according to the 2020-01 Admin API?
  - id: deprecated_202004_get_events_count
    intent: Count store events on API version 2020-04
    question: What's the total number of store events on API version 2020-04?
  - id: deprecated_202007_get_events_count
    intent: Count store events on API version 2020-07
    question: With the July 2020 API (2020-07), what's my event count?
  - id: get_events_count
    intent: Count store events (current 2020-10 version)
    question: How many events are recorded for my store on the current 2020-10 API version?
  - id: deprecated_202101_get_events_count
    intent: Count store events on API version 2021-01
    question: Can I still count shop events on the deprecated 2021-01 version?
  - id: deprecated_unstable_get_events_count
    intent: Count store events on the unstable API version
    question: How can I count events against the unstable Admin API?
  - id: deprecated_202001_get_webhooks_count
    intent: Count webhook subscriptions on API 2020-01
    question: How many webhook subscriptions does my app have on API version 2020-01?
  - id: deprecated_202004_get_webhooks_count
    intent: Count webhook subscriptions on API 2020-04
    question: What's the number of webhooks registered with the 2020-04 Admin API?
  phrasing_ops: 56
  slug: shopify-count-api
- description: The Countries API from Shopify — 12 operation(s) for countries.
  name: Shopify Countries API
  phrasing_intents:
  - id: deprecated_202001_get_countries
    intent: List the store's shipping countries (API 2020-01)
    question: Which countries has my store set up for shipping and tax, using API 2020-01?
  - id: deprecated_202004_get_countries
    intent: List the store's shipping countries (API 2020-04)
    question: What countries are in my shop's settings when I call release 2020-04?
  - id: deprecated_202007_get_countries
    intent: List the store's shipping countries (API 2020-07)
    question: Where can my shop ship to, according to the 2020-07 countries endpoint?
  - id: get_countries
    intent: List the store's shipping countries (API 2020-10)
    question: How do I see all the countries my store has tax and shipping settings for on 2020-10?
  - id: deprecated_202101_get_countries
    intent: List the store's shipping countries (API 2021-01)
    question: What does the 2021-01 API report as my shop's configured countries?
  - id: deprecated_unstable_get_countries
    intent: List the store's shipping countries (unstable API)
    question: Which countries does the unstable Shopify API return for my store?
  phrasing_ops: 6
  slug: shopify-countries-api
- description: The Country API from Shopify — 18 operation(s) for country.
  name: Shopify Country API
  phrasing_intents:
  - id: deprecated_202001_delete_countries_param_country_id
    intent: Delete a shipping country (2020-01 API)
    question: How do I remove a country from my store's shipping countries on the 2020-01 API?
  - id: deprecated_202004_delete_countries_param_country_id
    intent: Delete a shipping country (2020-04 API)
    question: Which 2020-04 endpoint deletes a country from the shop?
  - id: deprecated_202007_delete_countries_param_country_id
    intent: Delete a shipping country (2020-07 API)
    question: Where do I delete a country record in version 2020-07?
  - id: delete_countries_param_country_id
    intent: Delete a shipping country (2020-10 API)
    question: How can I stop offering a country by deleting it with the 2020-10 API?
  - id: deprecated_202101_delete_countries_param_country_id
    intent: Delete a shipping country (2021-01 API)
    question: Can I delete a country using the 2021-01 release?
  - id: deprecated_unstable_delete_countries_param_country_id
    intent: Delete a shipping country (unstable API)
    question: Is removing a store country possible on the unstable API version?
  - id: deprecated_202001_get_countries_param_country_id_provinces_param_province_id
    intent: Look up one province of a country (2020-01 API)
    question: How do I fetch a single province or state for a country on the 2020-01 API?
  - id: deprecated_202004_get_countries_param_country_id_provinces_param_province_id
    intent: Look up one province of a country (2020-04 API)
    question: Which 2020-04 call returns one province by ID within a country?
  phrasing_ops: 12
  slug: shopify-country-api
- description: The County API from Shopify — 6 operation(s) for county.
  name: Shopify County API
  phrasing_intents:
  - id: deprecated_202001_get_countries_param_country_id
    intent: Get a shipping country (API 2020-01)
    question: What does API 2020-01 tell me about one country my shop ships to?
  - id: deprecated_202004_get_countries_param_country_id
    intent: Get a shipping country (API 2020-04)
    question: Can I retrieve one country record from my store with API 2020-04?
  - id: deprecated_202007_get_countries_param_country_id
    intent: Get a shipping country (API 2020-07)
    question: What details does version 2020-07 give for a specific country?
  - id: get_countries_param_country_id
    intent: Get a shipping country (API 2020-10)
    question: How do I look up a specific country in my Shopify store with API 2020-10?
  - id: deprecated_202101_get_countries_param_country_id
    intent: Get a shipping country (API 2021-01)
    question: Does version 2021-01 let me fetch one country by ID?
  - id: deprecated_unstable_get_countries_param_country_id
    intent: Get a shipping country (unstable API)
    question: Can I fetch a single country on the unstable API version?
  phrasing_ops: 6
  slug: shopify-county-api
- description: The Create API from Shopify — 34 operation(s) for create.
  name: Shopify Create API
  phrasing_intents:
  - id: deprecated_202001_create_products_param_product_id_images
    intent: Add an image to a product (2020-01)
    question: How do I add a new image to a product using API 2020-01?
  - id: deprecated_202004_create_products_param_product_id_images
    intent: Add an image to a product (2020-04)
    question: Which 2020-04 endpoint creates a product image?
  - id: deprecated_202007_create_products_param_product_id_images
    intent: Add an image to a product (2020-07)
    question: What call adds a product image in the 2020-07 API?
  - id: create_products_param_product_id_images
    intent: Add an image to a product
    question: My product needs another photo; where do I add it in version 2020-10?
  - id: deprecated_202101_create_products_param_product_id_images
    intent: Add an image to a product (2021-01)
    question: On 2021-01, how can I create a product image?
  - id: deprecated_unstable_create_products_param_product_id_images
    intent: Add an image to a product (unstable)
    question: Can I add a product image on the unstable API?
  - id: deprecated_202001_create_orders_param_order_id_fulfillments
    intent: Create a fulfillment for an order (2020-01)
    question: How do I fulfill line items on an order using API 2020-01?
  - id: deprecated_202004_create_orders_param_order_id_fulfillments
    intent: Create a fulfillment for an order (2020-04)
    question: Which 2020-04 endpoint creates a fulfillment for an order's line items?
  phrasing_ops: 18
  slug: shopify-create-api
- description: The Currencies API from Shopify — 6 operation(s) for currencies.
  name: Shopify Currencies API
  phrasing_intents:
  - id: deprecated_202001_get_currencies
    intent: List enabled shop currencies (API 2020-01)
    question: Which currencies is my shop set up to sell in, per API version 2020-01?
  - id: deprecated_202004_get_currencies
    intent: List enabled shop currencies (API 2020-04)
    question: What currencies can customers pay in on my store, asked through 2020-04?
  - id: deprecated_202007_get_currencies
    intent: List enabled shop currencies (API 2020-07)
    question: How do I find the currencies enabled for my store on release 2020-07?
  - id: get_currencies
    intent: List enabled shop currencies (API 2020-10)
    question: What currencies are enabled on my Shopify store right now?
  - id: deprecated_202101_get_currencies
    intent: List enabled shop currencies (API 2021-01)
    question: Which currencies does the 2021-01 API say my shop has enabled?
  - id: deprecated_unstable_get_currencies
    intent: List enabled shop currencies (unstable API)
    question: What currencies are enabled on my store according to the unstable API?
  phrasing_ops: 6
  slug: shopify-currencies-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage manual collections
  name: Shopify Custom Collections API
  phrasing_intents:
  - id: listCustomCollections
    intent: List custom collections
    question: Which manual collections have I set up in my Shopify store?
  - id: createCustomCollection
    intent: Create a custom collection
    question: How do I create a new hand-picked collection in my store?
  phrasing_ops: 2
  slug: shopify-custom-collections-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage customer addresses
  name: Shopify Customer Addresses API
  phrasing_intents:
  - id: listCustomerAddresses
    intent: List a customer's saved addresses
    question: What addresses does a customer have saved on their account?
  - id: createCustomerAddress
    intent: Add a new address to a customer
    question: Can I add another mailing address to an existing customer?
  phrasing_ops: 2
  slug: shopify-customer-addresses-api
- description: The Customer API from Shopify — 30 operation(s) for customer.
  name: Shopify Customer API
  phrasing_intents:
  - id: deprecated_202001_create_customers
    intent: Add a new customer to the store (2020-01)
    question: How do I add a new customer record to my store with API version 2020-01?
  - id: deprecated_202001_get_customers_param_customer_id
    intent: Retrieve one customer (2020-01)
    question: Can I look up a single customer by ID on API version 2020-01?
  - id: deprecated_202001_update_customers_param_customer_id
    intent: Update a customer (2020-01)
    question: Can I change an existing customer's record through API version 2020-01?
  - id: deprecated_202001_delete_customers_param_customer_id
    intent: Delete a customer (2020-01)
    question: How do I permanently remove a customer from my store on 2020-01?
  - id: deprecated_202004_create_customers
    intent: Create a customer (2020-04)
    question: Can I sign up a new customer programmatically with the 2020-04 release?
  - id: deprecated_202004_get_customers_param_customer_id
    intent: Get a customer's details (2020-04)
    question: Where do I read one customer's details on the 2020-04 release?
  - id: deprecated_202004_update_customers_param_customer_id
    intent: Modify a customer (2020-04)
    question: Can release 2020-04 modify a customer after they sign up?
  - id: deprecated_202004_delete_customers_param_customer_id
    intent: Remove a customer (2020-04)
    question: Which 2020-04 call deletes a customer for good?
  phrasing_ops: 24
  slug: shopify-customer-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage customer records
  name: Shopify Customers API
  phrasing_intents:
  - id: listCustomers
    intent: List customers
    question: How do I pull a list of my Shopify customers, up to 250 at a time?
  - id: createCustomer
    intent: Create a customer
    question: Can I add a new customer record and have a welcome email sent to them?
  - id: getCustomerCount
    intent: Count customers
    question: How many customers does my store have in total?
  - id: searchCustomers
    intent: Search customers by name, email or phone
    question: Can I find a customer by typing part of their email address or phone number?
  - id: getCustomer
    intent: Retrieve a customer
    question: What details are stored for one particular customer ID?
  - id: updateCustomer
    intent: Update a customer
    question: How can I change a customer's details after their record already exists?
  - id: listCustomerOrders
    intent: List a customer's orders
    question: What has a specific customer ordered from my shop?
  - id: deprecated_202001_get_customers
    intent: List customers (API 2020-01)
    question: Where is the customer list endpoint in the 2020-01 Admin API?
  phrasing_ops: 49
  slug: shopify-customers-api
- description: The Deletes API from Shopify — 108 operation(s) for deletes.
  name: Shopify Deletes API
  phrasing_intents:
  - id: deprecated_202001_delete_webhooks_param_webhook_id
    intent: Delete a webhook subscription (2020-01)
    question: Can I stop a webhook subscription from firing using the 2020-01 Admin API?
  - id: deprecated_202004_delete_webhooks_param_webhook_id
    intent: Delete a webhook subscription (2020-04)
    question: How do I unsubscribe a webhook in the April 2020 (2020-04) Admin API?
  - id: deprecated_202007_delete_webhooks_param_webhook_id
    intent: Delete a webhook subscription (2020-07)
    question: Can the 2020-07 API version tear down a webhook subscription I no longer need?
  - id: delete_webhooks_param_webhook_id
    intent: Delete a webhook subscription
    question: What call deletes a webhook subscription in the supported 2020-10 Admin API?
  - id: deprecated_202101_delete_webhooks_param_webhook_id
    intent: Delete a webhook subscription (2021-01)
    question: Is there a 2021-01 endpoint to remove a webhook subscription?
  - id: deprecated_unstable_delete_webhooks_param_webhook_id
    intent: Delete a webhook subscription (unstable)
    question: Can I delete a webhook subscription through the unstable Admin API version?
  - id: deprecated_202001_delete_inventory_levels
    intent: Remove an item's stock level at a location (2020-01)
    question: Can I disconnect an inventory item from a location with the 2020-01 API?
  - id: deprecated_202004_delete_inventory_levels
    intent: Remove an item's stock level at a location (2020-04)
    question: How do I remove an inventory level for one location in the 2020-04 Admin API?
  phrasing_ops: 50
  slug: shopify-deletes-api
- description: The Discount API from Shopify — 36 operation(s) for discount.
  name: Shopify Discount API
  phrasing_intents:
  - id: deprecated_202001_get_price_rules_param_price_rule_id_discount_codes
    intent: List a price rule's discount codes (API 2020-01)
    question: Which discount codes belong to a price rule, on API version 2020-01?
  - id: deprecated_202004_get_price_rules_param_price_rule_id_discount_codes
    intent: List a price rule's discount codes (API 2020-04)
    question: What promo codes are tied to a specific price rule in release 2020-04?
  - id: deprecated_202007_get_price_rules_param_price_rule_id_discount_codes
    intent: List a price rule's discount codes (API 2020-07)
    question: Can the 2020-07 API list the coupon codes that a price rule issued?
  - id: get_price_rules_param_price_rule_id_discount_codes
    intent: List a price rule's discount codes (API 2020-10)
    question: How do I list all the discount codes created for a Shopify price rule?
  - id: deprecated_202101_get_price_rules_param_price_rule_id_discount_codes
    intent: List a price rule's discount codes (API 2021-01)
    question: Which discount codes hang off a given price rule in the 2021-01 release?
  - id: deprecated_unstable_get_price_rules_param_price_rule_id_discount_codes
    intent: List a price rule's discount codes (unstable API)
    question: Can the unstable API version list a price rule's discount codes?
  phrasing_ops: 6
  slug: shopify-discount-api
- description: The Dispute API from Shopify — 1 operation(s) for dispute.
  name: Shopify Dispute API
  phrasing_intents:
  - id: deprecated_202001_get_shopify_payments_disputes_param_dispute_id
    intent: Get a Shopify Payments dispute
    question: How do I look up a chargeback dispute from Shopify Payments by its ID?
  phrasing_ops: 1
  slug: shopify-dispute-api
- description: The Endpoint API from Shopify — 8 operation(s) for endpoint.
  name: Shopify Endpoint API
  phrasing_intents:
  - id: deprecated_202001_create_application_charges_param_application_charge_id_activate
    intent: Activate a one-time app charge (deprecated, API 2020-01)
    question: After a merchant accepts my one-time app fee, how do I activate it on API 2020-01?
  - id: deprecated_202004_create_application_charges_param_application_charge_id_activate
    intent: Activate a one-time app charge (deprecated, API 2020-04)
    question: Can I still call the one-time charge activation step on version 2020-04?
  - id: deprecated_202007_create_application_charges_param_application_charge_id_activate
    intent: Activate a one-time app charge (deprecated, API 2020-07)
    question: Is the separate activate call for one-time app charges needed under 2020-07?
  - id: create_application_charges_param_application_charge_id_activate
    intent: Activate a one-time app charge (deprecated, API 2020-10)
    question: Does version 2020-10 still expose activation for one-time application charges?
  - id: deprecated_202001_create_recurring_application_charges_param_recurring_application_charge_id_activate
    intent: Activate an app subscription charge (deprecated, 2020-01)
    question: Once a merchant approves my app subscription, how do I activate it with 2020-01?
  - id: deprecated_202004_create_recurring_application_charges_param_recurring_application_charge_id_activate
    intent: Activate an app subscription charge (deprecated, 2020-04)
    question: Can I activate an approved recurring app plan through release 2020-04?
  - id: deprecated_202007_create_recurring_application_charges_param_recurring_application_charge_id_activate
    intent: Activate an app subscription charge (deprecated, 2020-07)
    question: Which 2020-07 call activates a recurring charge a store owner already accepted?
  - id: create_recurring_application_charges_param_recurring_application_charge_id_activate
    intent: Activate an app subscription charge (deprecated, 2020-10)
    question: Is the old recurring-charge activation step still callable in 2020-10?
  phrasing_ops: 8
  slug: shopify-endpoint-api
- description: The Events API from Shopify — 30 operation(s) for events.
  name: Shopify Events API
  phrasing_intents:
  - id: deprecated_202001_get_events
    intent: List store activity events (API 2020-01)
    question: What has happened in my store recently, like products created or orders placed, on API 2020-01?
  - id: deprecated_202001_get_events_param_event_id
    intent: Get one store activity event (API 2020-01)
    question: Can I look up the details of one store activity event by its ID on 2020-01?
  - id: deprecated_202004_get_events
    intent: List store activity events (API 2020-04)
    question: Which changes to products, orders and collections were logged in my shop per 2020-04?
  - id: deprecated_202004_get_events_param_event_id
    intent: Get one store activity event (API 2020-04)
    question: What exactly happened in one logged store event, fetched with 2020-04?
  - id: deprecated_202007_get_events
    intent: List store activity events (API 2020-07)
    question: Can I audit what staff and apps changed in my store during a date range using 2020-07?
  - id: deprecated_202007_get_events_param_event_id
    intent: Get one store activity event (API 2020-07)
    question: Where do I read the full record of one store event on 2020-07?
  - id: get_events
    intent: List store activity events (API 2020-10)
    question: Which products or orders were deleted from my store lately, according to 2020-10 events?
  - id: get_events_param_event_id
    intent: Get one store activity event (API 2020-10)
    question: Can I see who or what triggered one particular store event on 2020-10?
  phrasing_ops: 30
  slug: shopify-events-api
- description: The Existing API from Shopify — 78 operation(s) for existing.
  name: Shopify Existing API
  phrasing_intents:
  - id: deprecated_202001_update_inventory_items_param_inventory_item_id
    intent: Update an inventory item (API 2020-01)
    question: How do I change an existing inventory item using the 2020-01 Admin API?
  - id: deprecated_202004_update_inventory_items_param_inventory_item_id
    intent: Update an inventory item (API 2020-04)
    question: Which April 2020 (2020-04) endpoint modifies an inventory item?
  - id: deprecated_202007_update_inventory_items_param_inventory_item_id
    intent: Update an inventory item (API 2020-07)
    question: My inventory app targets 2020-07; what updates an inventory item there?
  - id: update_inventory_items_param_inventory_item_id
    intent: Update an inventory item (API 2020-10)
    question: What is the 2020-10 call for updating an inventory item?
  - id: deprecated_202101_update_inventory_items_param_inventory_item_id
    intent: Update an inventory item (API 2021-01)
    question: Under the 2021-01 API, where do I update an inventory item?
  - id: deprecated_unstable_update_inventory_items_param_inventory_item_id
    intent: Update an inventory item (unstable API)
    question: Is there an unstable-channel endpoint for updating an inventory item?
  - id: deprecated_202001_update_redirects_param_redirect_id
    intent: Update a URL redirect (API 2020-01)
    question: How do I change an existing URL redirect on my online store with the 2020-01 API?
  - id: deprecated_202004_update_redirects_param_redirect_id
    intent: Update a URL redirect (API 2020-04)
    question: Which April 2020 (2020-04) endpoint modifies a URL redirect?
  phrasing_ops: 30
  slug: shopify-existing-api
- description: The Fulfillment API from Shopify — 155 operation(s) for fulfillment.
  name: Shopify Fulfillment API
  phrasing_intents:
  - id: deprecated_202001_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request
    intent: Request cancellation of a fulfillment order (2020-01)
    question: Using the 2020-01 API, how do I ask a fulfillment service to cancel an order it holds?
  - id: deprecated_202001_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request_accept
    intent: Accept a cancellation request (2020-01)
    question: As a fulfillment service on 2020-01, how do I agree to a merchant's cancellation request?
  - id: deprecated_202001_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request_reject
    intent: Reject a cancellation request (2020-01)
    question: How does a fulfillment service decline a cancellation request on 2020-01?
  - id: deprecated_202004_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request
    intent: Request cancellation of a fulfillment order (2020-04)
    question: In the 2020-04 Admin API, what call asks a fulfillment service to stop work on a fulfillment order?
  - id: deprecated_202004_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request_accept
    intent: Accept a cancellation request (2020-04)
    question: Which April 2020 call lets my fulfillment service accept a cancellation request?
  - id: deprecated_202004_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request_reject
    intent: Reject a cancellation request (2020-04)
    question: Which 2020-04 endpoint lets my service turn down a merchant's cancellation request?
  - id: deprecated_202007_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request
    intent: Request cancellation of a fulfillment order (2020-07)
    question: Which 2020-07 endpoint sends a fulfillment service a request to cancel?
  - id: deprecated_202007_create_fulfillment_orders_param_fulfillment_order_id_cancellation_request_accept
    intent: Accept a cancellation request (2020-07)
    question: What does a fulfillment service call to confirm a cancellation request in the 2020-07 version?
  phrasing_ops: 95
  slug: shopify-fulfillment-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage fulfillment workflows
  name: Shopify Fulfillment Orders API
  phrasing_intents:
  - id: listOrderFulfillmentOrders
    intent: List an order's fulfillment orders
    question: How do I see the fulfillment orders created for a customer's order?
  phrasing_ops: 1
  slug: shopify-fulfillment-orders-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage order fulfillments
  name: Shopify Fulfillments API
  phrasing_intents:
  - id: createFulfillment
    intent: Fulfill one or more fulfillment orders
    question: How do I mark items as fulfilled across several fulfillment orders at once?
  - id: updateFulfillmentTracking
    intent: Update a fulfillment's tracking info
    question: How can I change the tracking number on a shipment that's already fulfilled?
  - id: cancelFulfillment
    intent: Cancel a fulfillment
    question: How do I cancel a fulfillment that was created by mistake?
  phrasing_ops: 3
  slug: shopify-fulfillments-api
- description: The Get API from Shopify — 28 operation(s) for get.
  name: Shopify Get API
  phrasing_intents:
  - id: deprecated_202001_get_products_param_product_id_images_param_image_id
    intent: Get one product image (API 2020-01)
    question: How do I fetch a single image of a product by its ID on API 2020-01?
  - id: deprecated_202004_get_products_param_product_id_images_param_image_id
    intent: Get one product image (API 2020-04)
    question: Which April 2020 call returns one specific product image?
  - id: deprecated_202007_get_products_param_product_id_images_param_image_id
    intent: Get one product image (API 2020-07)
    question: Where do I read a single product photo's details on the July 2020 API?
  - id: get_products_param_product_id_images_param_image_id
    intent: Get one product image (API 2020-10)
    question: What's the 2020-10 way to retrieve one image from a product?
  - id: deprecated_202101_get_products_param_product_id_images_param_image_id
    intent: Get one product image (API 2021-01)
    question: How can I view a single product image by ID on the 2021-01 release?
  - id: deprecated_unstable_get_products_param_product_id_images_param_image_id
    intent: Get one product image (unstable API)
    question: Can I get one product image through the unstable Admin API?
  - id: deprecated_unknown_version_get_fetch_tracking_numbers
    intent: Get tracking numbers for fulfillments
    question: How does a fulfillment service supply tracking numbers for a merchant's orders?
  - id: deprecated_unknown_version_get_fetch_stock
    intent: Get stock levels from a fulfillment service
    question: How does a fulfillment service report inventory levels for a SKU?
  phrasing_ops: 8
  slug: shopify-get-api
- description: The Identifiers API from Shopify — 75 operation(s) for identifiers.
  name: Shopify Identifiers API
  phrasing_intents:
  - id: deprecated_202001_get_inventory_items_param_inventory_item_id
    intent: Look up an inventory item on API 2020-01
    question: How can I see one inventory item's details, like SKU and cost, on the 2020-01 API?
  - id: deprecated_202004_get_inventory_items_param_inventory_item_id
    intent: Look up an inventory item on API 2020-04
    question: What does a single inventory item look like on API version 2020-04?
  - id: deprecated_202007_get_inventory_items_param_inventory_item_id
    intent: Look up an inventory item on API 2020-07
    question: Using the 2020-07 release, where do I read one inventory item by ID?
  - id: get_inventory_items_param_inventory_item_id
    intent: Look up an inventory item (current 2020-10)
    question: Which call reads a single inventory item on the current 2020-10 version?
  - id: deprecated_202101_get_inventory_items_param_inventory_item_id
    intent: Look up an inventory item on API 2021-01
    question: Can I still retrieve an inventory item by ID on the deprecated 2021-01 version?
  - id: deprecated_unstable_get_inventory_items_param_inventory_item_id
    intent: Look up an inventory item on unstable API
    question: How can I read a single inventory item on the unstable Admin API?
  - id: deprecated_202001_get_locations_param_location_id
    intent: Get one store location on API 2020-01
    question: How can I see the address and details of one store location on the 2020-01 API?
  - id: deprecated_202004_get_locations_param_location_id
    intent: Get one store location on API 2020-04
    question: What does a single location record contain on API version 2020-04?
  phrasing_ops: 30
  slug: shopify-identifiers-api
- description: The Images API from Shopify — 18 operation(s) for images.
  name: Shopify Images API
  phrasing_intents:
  - id: deprecated_202001_update_products_param_product_id
    intent: Update a product, its variants and images (2020-01)
    question: How do I update a product along with its variants and images on API 2020-01?
  - id: deprecated_202004_update_products_param_product_id
    intent: Update a product, its variants and images (2020-04)
    question: Which April 2020 call edits a product together with its variants?
  - id: deprecated_202007_update_products_param_product_id
    intent: Update a product, its variants and images (2020-07)
    question: Where do I change a product's details and images on the July 2020 API?
  - id: update_products_param_product_id
    intent: Update a product, its variants and images (2020-10)
    question: What's the current 2020-10 way to update a product and its images?
  - id: deprecated_202101_update_products_param_product_id
    intent: Update a product, its variants and images (2021-01)
    question: How can I revise a product with its variants and images on the 2021-01 release?
  - id: deprecated_unstable_update_products_param_product_id
    intent: Update a product, its variants and images (unstable)
    question: Can I update a product and its images through the unstable Admin API?
  phrasing_ops: 6
  slug: shopify-images-api
- description: The Inventory API from Shopify — 43 operation(s) for inventory.
  name: Shopify Inventory API
  phrasing_intents:
  - id: deprecated_202001_get_inventory_items
    intent: Look up inventory items by ID (2020-01)
    question: How do I fetch several inventory items at once by their IDs with the 2020-01 API?
  - id: deprecated_202004_get_inventory_items
    intent: Look up inventory items by ID (2020-04)
    question: Can I pull SKU and cost details for a batch of inventory items on release 2020-04?
  - id: deprecated_202007_get_inventory_items
    intent: Look up inventory items by ID (2020-07)
    question: Is there a 2020-07 endpoint that retrieves a list of inventory items?
  - id: get_inventory_items
    intent: Look up inventory items by ID
    question: What call lists inventory items by ID in the 2020-10 Admin API?
  - id: deprecated_202101_get_inventory_items
    intent: Look up inventory items by ID (2021-01)
    question: Does the January 2021 (2021-01) API let me list inventory items?
  - id: deprecated_unstable_get_inventory_items
    intent: Look up inventory items by ID (unstable)
    question: Can I list inventory items through the unstable Admin API?
  - id: deprecated_202001_get_inventory_levels
    intent: List stock levels by item or location (2020-01)
    question: How can I see available quantities for several items across locations using 2020-01?
  - id: deprecated_202001_create_inventory_levels_adjust
    intent: Add or subtract available stock (2020-01)
    question: How do I add received stock to an item's count at one location with the 2020-01 API?
  phrasing_ops: 30
  slug: shopify-inventory-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage inventory item records
  name: Shopify Inventory Items API
  phrasing_intents:
  - id: listInventoryItems
    intent: List inventory items by ID
    question: How do I fetch several inventory items at once when I know their IDs?
  - id: getInventoryItem
    intent: Retrieve a single inventory item
    question: Which call returns one inventory item by its ID?
  - id: updateInventoryItem
    intent: Update an inventory item
    question: How do I update an existing inventory item?
  phrasing_ops: 3
  slug: shopify-inventory-items-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage inventory quantities at locations
  name: Shopify Inventory Levels API
  phrasing_intents:
  - id: listInventoryLevels
    intent: Look up stock levels by item or location
    question: How much stock of certain items do I have across my locations?
  - id: setInventoryLevel
    intent: Set an item's available quantity at a location
    question: After a stock count, how do I overwrite the available quantity of an item at one location?
  - id: listLocationInventoryLevels
    intent: List all stock levels at one location
    question: What does everything stocked at one warehouse look like?
  phrasing_ops: 3
  slug: shopify-inventory-levels-api
- description: The Lists API from Shopify — 291 operation(s) for lists.
  name: Shopify Lists API
  phrasing_intents:
  - id: deprecated_202001_get_reports
    intent: List reports (API 2020-01)
    question: Which custom reports exist in my Shopify store under the 2020-01 Admin API?
  - id: deprecated_202004_get_reports
    intent: List reports (API 2020-04)
    question: What analytics reports can I list on API version 2020-04?
  - id: deprecated_202007_get_reports
    intent: List reports (API 2020-07)
    question: What reports has my app created, according to the 2020-07 API?
  - id: get_reports
    intent: List reports (API 2020-10)
    question: Where do I see all the reports in my shop on the 2020-10 Admin API?
  - id: deprecated_202101_get_reports
    intent: List reports (API 2021-01)
    question: Does the 2021-01 API still let me list store reports?
  - id: deprecated_unstable_get_reports
    intent: List reports (unstable API)
    question: Can I list reports on the unstable Admin API version?
  - id: deprecated_202001_get_webhooks
    intent: List webhook subscriptions (API 2020-01)
    question: Which webhook subscriptions does my app have on API version 2020-01?
  - id: deprecated_202004_get_webhooks
    intent: List webhook subscriptions (API 2020-04)
    question: Can I list only the webhooks for one topic, like orders/create, on the 2020-04 API?
  phrasing_ops: 69
  slug: shopify-lists-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Retrieve store locations
  name: Shopify Locations API
  phrasing_intents:
  - id: listLocations
    intent: List a shop's locations
    question: What locations does my store have, like warehouses and retail stores?
  - id: getLocationCount
    intent: Count a shop's locations
    question: How many locations does my shop have?
  - id: getLocation
    intent: Get a single location
    question: How do I look up the details of one location by its ID in Shopify?
  phrasing_ops: 3
  slug: shopify-locations-api
- description: The Order API from Shopify — 129 operation(s) for order.
  name: Shopify Order API
  phrasing_intents:
  - id: deprecated_202001_create_orders
    intent: Create an order (API 2020-01)
    question: How do I create a new order through the 2020-01 Admin API?
  - id: deprecated_202001_get_orders_param_order_id
    intent: Retrieve one order (API 2020-01)
    question: What does a single order look like when fetched by ID on the 2020-01 API?
  - id: deprecated_202001_update_orders_param_order_id
    intent: Update an order (API 2020-01)
    question: Which 2020-01 endpoint changes an existing order?
  - id: deprecated_202001_create_orders_param_order_id_close
    intent: Close an order (API 2020-01)
    question: How do I close an order once it is complete, using 2020-01?
  - id: deprecated_202001_create_orders_param_order_id_open
    intent: Re-open a closed order (API 2020-01)
    question: Can a closed order be re-opened on the 2020-01 API?
  - id: deprecated_202004_create_orders
    intent: Create an order (API 2020-04)
    question: Which April 2020 (2020-04) endpoint places a new order in my shop?
  - id: deprecated_202004_get_orders_param_order_id
    intent: Retrieve one order (API 2020-04)
    question: Where do I look up a specific order by its ID in the April 2020 (2020-04) API?
  - id: deprecated_202004_update_orders_param_order_id
    intent: Update an order (API 2020-04)
    question: Which April 2020 endpoint modifies an order that already exists?
  phrasing_ops: 16
  slug: shopify-order-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage orders
  name: Shopify Orders API
  phrasing_intents:
  - id: listOrders
    intent: List recent orders with filters
    question: Which of my store's orders from the last 60 days are still unfulfilled?
  - id: createOrder
    intent: Record an order from an external channel
    question: How do I import a sale made on another channel as an order in Shopify?
  - id: getOrderCount
    intent: Count orders matching filters
    question: How many orders did I get since the start of the month?
  - id: getOrder
    intent: Get one order's details
    question: What line items and totals are on a specific order?
  - id: updateOrder
    intent: Update an order's note, tags or contact info
    question: Can I change the shipping address on an order that's already been placed?
  - id: deleteOrder
    intent: Delete an order
    question: Why can't I delete an order that was paid through an online gateway?
  - id: cancelOrder
    intent: Cancel an order and optionally restock
    question: How do I cancel an order and put the items back in stock?
  - id: closeOrder
    intent: Close an order as completed
    question: Can I mark a finished order as closed once it's done?
  phrasing_ops: 23
  slug: shopify-orders-api
- baseURL_template: https://{store}.myshopify.com
  baseurl_source: spec_template
  description: Search suggestions for products, collections, pages, and articles
  name: Shopify Predictive Search API
  phrasing_intents:
  - id: getPredictiveSearchResults
    intent: Get search-as-you-type suggestions
    question: How do I show live search suggestions as shoppers type in my storefront?
  phrasing_ops: 1
  slug: shopify-predictive-search-api
- description: The Product API from Shopify — 54 operation(s) for product.
  name: Shopify Product API
  phrasing_intents:
  - id: deprecated_202001_create_products
    intent: Create a product (API 2020-01)
    question: Can I add a new product to my Shopify catalog with the 2020-01 Admin API?
  - id: deprecated_202001_get_products_param_product_id
    intent: Get one product (API 2020-01)
    question: What does API 2020-01 return when I look up one product by ID?
  - id: deprecated_202004_create_products
    intent: Create a product (API 2020-04)
    question: Is there a 2020-04 endpoint for creating a new product?
  - id: deprecated_202004_get_products_param_product_id
    intent: Get one product (API 2020-04)
    question: Can I pull the full record of one product with API 2020-04?
  - id: deprecated_202007_create_products
    intent: Create a product (API 2020-07)
    question: Can I create products in my store using version 2020-07?
  - id: deprecated_202007_get_products_param_product_id
    intent: Get one product (API 2020-07)
    question: What details does version 2020-07 give me for a single product?
  - id: create_products
    intent: Create a product (API 2020-10)
    question: How do I create a new product in my Shopify store with API 2020-10?
  - id: get_products_param_product_id
    intent: Get one product (API 2020-10)
    question: Can I retrieve a single product's details with API 2020-10?
  phrasing_ops: 12
  slug: shopify-product-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage images associated with products
  name: Shopify Product Images API
  phrasing_intents:
  - id: listProductImages
    intent: List a product's images
    question: Which photos are attached to one of my products?
  - id: createProductImage
    intent: Add an image to a product
    question: How do I upload a new photo to a product?
  - id: getProductImageCount
    intent: Count a product's images
    question: How many images does a given product have?
  - id: getProductImage
    intent: Get one product image
    question: What alt text and position does a specific product image have?
  - id: updateProductImage
    intent: Update a product image's alt text or position
    question: Can I change the alt text on an existing product photo for accessibility?
  - id: deleteProductImage
    intent: Delete a product image
    question: How can I remove an outdated photo from a product?
  phrasing_ops: 6
  slug: shopify-product-images-api
- baseURL_template: https://{store}.myshopify.com
  baseurl_source: spec_template
  description: Get product recommendations
  name: Shopify Product Recommendations API
  phrasing_intents:
  - id: getProductRecommendations
    intent: Get recommended products for a product
    question: How can I show 'you may also like' products on a product page?
  phrasing_ops: 1
  slug: shopify-product-recommendations-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage product variants
  name: Shopify Product Variants API
  phrasing_intents:
  - id: listProductVariants
    intent: List a product's variants
    question: What sizes, colors and other variants does one of my Shopify products have?
  - id: createProductVariant
    intent: Add a new variant to a product
    question: How do I add a new size or color option as a variant on an existing product?
  phrasing_ops: 2
  slug: shopify-product-variants-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage products in a Shopify store
  name: Shopify Products API
  phrasing_intents:
  - id: listProducts
    intent: List products in the store
    question: How do I list all the products from a particular vendor in my Shopify store?
  - id: createProduct
    intent: Create a new product
    question: How do I add a new product to my catalog through the Admin API?
  - id: getProductCount
    intent: Count products matching filters
    question: How many products do I have in the store in total?
  - id: getProduct
    intent: Get a product by ID
    question: How do I look up one product by its ID, with its variants, images and options?
  - id: updateProduct
    intent: Update an existing product
    question: How do I change the details of a product that's already in my store?
  - id: deleteProduct
    intent: Delete a product
    question: How do I permanently delete a product from my store?
  - id: getProductByHandle
    intent: Look up a storefront product by its handle
    question: Can I get a product's details from the storefront using just its URL handle?
  phrasing_ops: 7
  slug: shopify-products-api
- description: The Published API from Shopify — 30 operation(s) for published.
  name: Shopify Published API
  phrasing_intents:
  - id: deprecated_202001_get_collection_listings_param_collection_listing_id_product_ids
    intent: List product IDs in a collection listing (2020-01)
    question: Which product IDs are published to a collection listing, in API 2020-01?
  - id: deprecated_202004_get_collection_listings_param_collection_listing_id_product_ids
    intent: List product IDs in a collection listing (2020-04)
    question: How do I see which products my sales channel has in a collection listing, on 2020-04?
  - id: deprecated_202007_get_collection_listings_param_collection_listing_id_product_ids
    intent: List product IDs in a collection listing (2020-07)
    question: What call returns a collection listing's published product IDs in 2020-07?
  - id: get_collection_listings_param_collection_listing_id_product_ids
    intent: List product IDs published to a collection listing
    question: Which products in this collection are published to my channel, on 2020-10?
  - id: deprecated_202101_get_collection_listings_param_collection_listing_id_product_ids
    intent: List product IDs in a collection listing (2021-01)
    question: On 2021-01, how can I get product IDs published to a collection listing?
  - id: deprecated_unstable_get_collection_listings_param_collection_listing_id_product_ids
    intent: List product IDs in a collection listing (unstable)
    question: Can I list a collection listing's product IDs on the unstable API?
  phrasing_ops: 6
  slug: shopify-published-api
- description: The Redirect API from Shopify — 12 operation(s) for redirect.
  name: Shopify Redirect API
  phrasing_intents:
  - id: deprecated_202001_create_redirects
    intent: Create a URL redirect (API 2020-01)
    question: Can I send shoppers from an old store URL to a new one using the 2020-01 API?
  - id: deprecated_202001_get_redirects_param_redirect_id
    intent: Get one redirect (API 2020-01)
    question: Where does a given redirect point, checked on API version 2020-01?
  - id: deprecated_202004_create_redirects
    intent: Create a URL redirect (API 2020-04)
    question: How do I forward a retired product URL to a new page with the 2020-04 release?
  - id: deprecated_202004_get_redirects_param_redirect_id
    intent: Get one redirect (API 2020-04)
    question: What target path is a specific redirect sending traffic to under 2020-04?
  - id: deprecated_202007_create_redirects
    intent: Create a URL redirect (API 2020-07)
    question: Can I add a storefront redirect when my app is pinned to 2020-07?
  - id: deprecated_202007_get_redirects_param_redirect_id
    intent: Get one redirect (API 2020-07)
    question: How can I inspect one redirect's path and target on the 2020-07 release?
  - id: create_redirects
    intent: Create a URL redirect (API 2020-10)
    question: How do I redirect an old storefront URL to a new location in Shopify?
  - id: get_redirects_param_redirect_id
    intent: Get one redirect (API 2020-10)
    question: What does an existing redirect point to, using the 2020-10 API?
  phrasing_ops: 12
  slug: shopify-redirect-api
- description: The Refund API from Shopify — 6 operation(s) for refund.
  name: Shopify Refund API
  phrasing_intents:
  - id: deprecated_202001_get_orders_param_order_id_refunds_param_refund_id
    intent: Retrieve a refund on an order (2020-01)
    question: How do I look up a specific refund on an order using API 2020-01?
  - id: deprecated_202004_get_orders_param_order_id_refunds_param_refund_id
    intent: Retrieve a refund on an order (2020-04)
    question: Which 2020-04 endpoint retrieves one refund from an order?
  - id: deprecated_202007_get_orders_param_order_id_refunds_param_refund_id
    intent: Retrieve a refund on an order (2020-07)
    question: What call returns a single refund's details in the 2020-07 API?
  - id: get_orders_param_order_id_refunds_param_refund_id
    intent: Retrieve a refund on an order
    question: A customer asked about their refund; where do I pull it up on 2020-10?
  - id: deprecated_202101_get_orders_param_order_id_refunds_param_refund_id
    intent: Retrieve a refund on an order (2021-01)
    question: On 2021-01, how can I fetch a refund by its ID?
  - id: deprecated_unstable_get_orders_param_order_id_refunds_param_refund_id
    intent: Retrieve a refund on an order (unstable)
    question: Can I retrieve a specific refund on the unstable API?
  phrasing_ops: 6
  slug: shopify-refund-api
- description: The Reports API from Shopify — 12 operation(s) for reports.
  name: Shopify Reports API
  phrasing_intents:
  - id: deprecated_202001_create_reports
    intent: Create a custom analytics report (2020-01)
    question: How do I create a custom report from a ShopifyQL query with API version 2020-01?
  - id: deprecated_202001_update_reports_param_report_id
    intent: Update a report (2020-01)
    question: Can I change a custom report I already made through API version 2020-01?
  - id: deprecated_202001_delete_reports_param_report_id
    intent: Delete a report (2020-01)
    question: How do I permanently remove a custom report on 2020-01?
  - id: deprecated_202004_create_reports
    intent: Create a ShopifyQL report (2020-04)
    question: Can I save a ShopifyQL query as a named report with the 2020-04 release?
  - id: deprecated_202004_update_reports_param_report_id
    intent: Modify a report (2020-04)
    question: Can release 2020-04 modify a report after it is created?
  - id: deprecated_202004_delete_reports_param_report_id
    intent: Remove a report (2020-04)
    question: Which 2020-04 call deletes a report for good?
  - id: deprecated_202007_create_reports
    intent: Add a new report (2020-07)
    question: Does the 2020-07 API let my app publish a report defined by ShopifyQL?
  - id: deprecated_202007_update_reports_param_report_id
    intent: Edit a report (2020-07)
    question: Does the 2020-07 API allow editing a report that already exists?
  phrasing_ops: 18
  slug: shopify-reports-api
- description: The Resource API from Shopify — 12 operation(s) for resource.
  name: Shopify Resource API
  phrasing_intents:
  - id: deprecated_202001_create_metafields
    intent: Attach a metafield to a resource (2020-01)
    question: How do I store custom data on a store resource as a metafield with API version 2020-01?
  - id: deprecated_202004_create_metafields
    intent: Create a metafield (2020-04)
    question: Which 2020-04 endpoint saves extra custom fields on a resource?
  - id: deprecated_202007_create_metafields
    intent: Add a metafield to a resource (2020-07)
    question: Does the 2020-07 API let me extend a resource with a metafield?
  - id: create_metafields
    intent: Create a metafield (2020-10, current version)
    question: What's the way to create a metafield on the current 2020-10 version?
  - id: deprecated_202101_create_metafields
    intent: Create a metafield (2021-01)
    question: Is creating a metafield possible with version 2021-01?
  - id: deprecated_unstable_create_metafields
    intent: Create a metafield (unstable version)
    question: Can I test creating a metafield against the unstable API version?
  phrasing_ops: 6
  slug: shopify-resource-api
- description: The Retrieves API from Shopify — 619 operation(s) for retrieves.
  name: Shopify Retrieves API
  phrasing_intents:
  - id: deprecated_202001_get_webhooks_param_webhook_id
    intent: Retrieve a webhook subscription (API 2020-01)
    question: How do I look up one webhook subscription by ID on the 2020-01 API?
  - id: deprecated_202004_get_webhooks_param_webhook_id
    intent: Retrieve a webhook subscription (API 2020-04)
    question: Which April 2020 (2020-04) endpoint returns a single webhook subscription?
  - id: deprecated_202007_get_webhooks_param_webhook_id
    intent: Retrieve a webhook subscription (API 2020-07)
    question: My app is pinned to 2020-07; what reads back one webhook subscription there?
  - id: get_webhooks_param_webhook_id
    intent: Retrieve a webhook subscription (API 2020-10)
    question: What is the 2020-10 call for retrieving one webhook subscription?
  - id: deprecated_202101_get_webhooks_param_webhook_id
    intent: Retrieve a webhook subscription (API 2021-01)
    question: Under the 2021-01 API, where do I inspect a single webhook subscription?
  - id: deprecated_unstable_get_webhooks_param_webhook_id
    intent: Retrieve a webhook subscription (unstable API)
    question: Is there an unstable-channel endpoint for reading one webhook subscription?
  - id: deprecated_202001_get_script_tags_param_script_tag_id
    intent: Retrieve a script tag (API 2020-01)
    question: How do I read a single script tag my app injected into the storefront, on 2020-01?
  - id: deprecated_202004_get_script_tags_param_script_tag_id
    intent: Retrieve a script tag (API 2020-04)
    question: Which April 2020 (2020-04) endpoint returns one script tag by ID?
  phrasing_ops: 24
  slug: shopify-retrieves-api
- description: The Script API from Shopify — 18 operation(s) for script.
  name: Shopify Script API
  phrasing_intents:
  - id: deprecated_202001_create_script_tags
    intent: Create a storefront script tag (2020-01)
    question: How do I load my app's script on the storefront with a script tag, on API 2020-01?
  - id: deprecated_202001_update_script_tags_param_script_tag_id
    intent: Update a script tag (2020-01)
    question: How do I change an existing script tag using API 2020-01?
  - id: deprecated_202004_create_script_tags
    intent: Create a storefront script tag (2020-04)
    question: Which 2020-04 endpoint creates a script tag?
  - id: deprecated_202004_update_script_tags_param_script_tag_id
    intent: Update a script tag (2020-04)
    question: Which 2020-04 endpoint updates a script tag?
  - id: deprecated_202007_create_script_tags
    intent: Create a storefront script tag (2020-07)
    question: What call creates a new script tag in the 2020-07 API?
  - id: deprecated_202007_update_script_tags_param_script_tag_id
    intent: Update a script tag (2020-07)
    question: What call modifies an existing script tag in the 2020-07 API?
  - id: create_script_tags
    intent: Create a storefront script tag
    question: My app needs JavaScript on the storefront; how do I create a script tag on 2020-10?
  - id: update_script_tags_param_script_tag_id
    intent: Update a script tag
    question: My storefront script tag needs changes; how do I update it on 2020-10?
  phrasing_ops: 12
  slug: shopify-script-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Retrieve shop configuration
  name: Shopify Shop API
  phrasing_intents:
  - id: getShop
    intent: Get the store's settings and details
    question: What currency and timezone is my store set to?
  phrasing_ops: 1
  slug: shopify-shop-api
- baseURL_template: https://{store}.myshopify.com/admin/api/2025-01
  baseurl_source: spec_template
  description: Manage automated collections
  name: Shopify Smart Collections API
  phrasing_intents:
  - id: listSmartCollections
    intent: List smart (automated) collections
    question: How do I see all the automated collections in my store?
  phrasing_ops: 1
  slug: shopify-smart-collections-api
- description: The Summaries API from Shopify — 18 operation(s) for summaries.
  name: Shopify Summaries API
  phrasing_intents:
  - id: deprecated_202001_delete_products_param_product_id_images_param_image_id
    intent: Delete an image from a product (API 2020-01)
    question: How do I take a photo off a product listing with API 2020-01?
  - id: deprecated_202004_delete_products_param_product_id_images_param_image_id
    intent: Delete an image from a product (API 2020-04)
    question: Can I get rid of an outdated product photo via release 2020-04?
  - id: deprecated_202007_delete_products_param_product_id_images_param_image_id
    intent: Delete an image from a product (API 2020-07)
    question: Can version 2020-07 delete a single picture from a product?
  - id: delete_products_param_product_id_images_param_image_id
    intent: Delete an image from a product (API 2020-10)
    question: What's the 2020-10 request to remove a product image?
  - id: deprecated_202101_delete_products_param_product_id_images_param_image_id
    intent: Delete an image from a product (API 2021-01)
    question: How can I clear a wrong photo from a product using 2021-01?
  - id: deprecated_unstable_delete_products_param_product_id_images_param_image_id
    intent: Delete an image from a product (unstable API)
    question: Can I delete a product image through the unstable API version?
  - id: deprecated_202001_get_fulfillment_services
    intent: List fulfillment services (API 2020-01)
    question: Which fulfillment services has my app registered on the store, per API 2020-01?
  - id: deprecated_202001_get_fulfillment_services_param_fulfillment_service_id
    intent: Get one fulfillment service (API 2020-01)
    question: How is a particular fulfillment service configured, read through 2020-01?
  phrasing_ops: 30
  slug: shopify-summaries-api
- description: The Versions API from Shopify — 26 operation(s) for versions.
  name: Shopify Versions API
  phrasing_intents:
  - id: deprecated_202001_create_countries
    intent: Add a country to the store (2020-01)
    question: Can I add a new country to my store settings with the 2020-01 Admin API?
  - id: deprecated_202001_update_countries_param_country_id
    intent: Update a store country (2020-01)
    question: How do I edit one of my store's countries on 2020-01?
  - id: deprecated_202004_create_countries
    intent: Add a country to the store (2020-04)
    question: Which 2020-04 endpoint adds a country to the shop?
  - id: deprecated_202004_update_countries_param_country_id
    intent: Update a store country (2020-04)
    question: What 2020-04 call modifies a country I already set up?
  - id: deprecated_202007_create_countries
    intent: Add a country to the store (2020-07)
    question: What 2020-07 endpoint creates a country for my shop?
  - id: deprecated_202007_update_countries_param_country_id
    intent: Update a store country (2020-07)
    question: Is updating a country supported in 2020-07?
  - id: create_countries
    intent: Add a country to the store (2020-10)
    question: How can I add a country to my Shopify store on version 2020-10?
  - id: update_countries_param_country_id
    intent: Update a store country (2020-10)
    question: How can I update a country in the 2020-10 release?
  phrasing_ops: 18
  slug: shopify-versions-api
arazzos:
- description: Confirm a product exists, add a new variant to it, then read the variant list back.
  name: Shopify Add a Variant to an Existing Product
  slug: shopify-add-variant-to-product-workflow
- description: Read a product and branch on its status, archiving it only when it is still active.
  name: Shopify Archive a Stale Product
  slug: shopify-archive-stale-product-workflow
- description: Confirm an order, cancel it with a reason and restock, then read the cancelled order back.
  name: Shopify Cancel and Restock an Order
  slug: shopify-cancel-and-refund-order-workflow
- description: Tag an order, close it to mark it completed, then read the closed order back.
  name: Shopify Tag and Close an Order
  slug: shopify-close-and-archive-order-workflow
- description: Create a custom collection, confirm a product, then read the collection back.
  name: Shopify Create Collection With a Product
  slug: shopify-create-collection-with-product-workflow
- description: Create a customer record, attach a mailing address, then read the customer back.
  name: Shopify Create Customer With Address
  slug: shopify-create-customer-with-address-workflow
- description: Place an order, locate its fulfillment order, create a fulfillment with tracking, and read the order back.
  name: Shopify Create Order and Fulfill
  slug: shopify-create-order-and-fulfill-workflow
- description: Create a product, add a priced variant to it, then read the finished product back.
  name: Shopify Create Product With Variant
  slug: shopify-create-product-with-variant-workflow
- description: Find a custom collection by title, then list the products it contains.
  name: Shopify Find Collection and List Its Products
  slug: shopify-find-collection-and-list-products-workflow
- description: Resolve an order's fulfillment order, create a fulfillment with tracking, and confirm the result.
  name: Shopify Fulfill an Existing Order
  slug: shopify-fulfill-existing-order-workflow
- description: Create a product, add a variant, resolve a location, and set its starting inventory.
  name: Shopify Launch a Product With Stock
  slug: shopify-launch-product-with-stock-workflow
- description: Create a pending (quote-style) order, mark it paid, then read the completed order back.
  name: Shopify Quote to Paid Order
  slug: shopify-quote-to-paid-order-workflow
- description: Create a webhook subscription for a topic, then read it back to confirm registration.
  name: Shopify Register a Webhook Subscription
  slug: shopify-register-webhook-workflow
- description: Read a variant to find its inventory item, resolve a location, and set the available quantity.
  name: Shopify Restock a Product Variant
  slug: shopify-restock-product-variant-workflow
- description: Resolve the primary location, set an item's available quantity there, then verify the new level.
  name: Shopify Set Inventory at a Location
  slug: shopify-set-inventory-at-location-workflow
- description: Read an order and branch on its fulfillment status to apply the appropriate tag.
  name: Shopify Tag an Order by Fulfillment Status
  slug: shopify-tag-order-by-fulfillment-status-workflow
- description: Confirm an order, update a fulfillment's tracking details, then read the order back.
  name: Shopify Update Fulfillment Tracking
  slug: shopify-update-fulfillment-tracking-workflow
- description: Read an inventory item, update its unit cost and tracking flag, then read it back.
  name: Shopify Update an Inventory Item Cost
  slug: shopify-update-inventory-item-cost-workflow
- description: Search for a customer by email and update it if it exists, otherwise create it.
  name: Shopify Upsert a Customer by Email
  slug: shopify-upsert-customer-by-email-workflow
- description: Find or create a customer by email, then place an order for that customer.
  name: Shopify Upsert Customer Then Place Order
  slug: shopify-upsert-customer-then-order-workflow
- description: Find a product by exact title and update it if it exists, otherwise create it.
  name: Shopify Upsert a Product by Title
  slug: shopify-upsert-product-by-title-workflow
- description: Find a webhook subscription for a topic and update its address if it exists, otherwise create it.
  name: Shopify Upsert a Webhook by Topic
  slug: shopify-upsert-webhook-by-topic-workflow
artifact_total: 394
asyncapis:
- description: ''
  name: Shopify Webhooks
  slug: shopify-webhooks
collections:
- collection_type: postman
  name: Shopify Admin REST API
  slug: postman-shopify-admin-rest-api
- collection_type: postman
  name: Shopify Ajax API
  slug: postman-shopify-ajax-api
- collection_type: postman
  name: Shopify  API
  slug: postman-shopify-api
- collection_type: postman
  name: Shopify Multipass API
  slug: postman-shopify-multipass-api
- collection_type: postman
  name: Shopify Webhooks API
  slug: postman-shopify-webhooks-api
- collection_type: open
  name: Shopify Admin REST About API
  slug: open-shopify-about-api
- collection_type: open
  name: Shopify Admin REST About Access API
  slug: open-shopify-access-api
- collection_type: open
  name: Shopify Admin REST About Account API
  slug: open-shopify-account-api
- collection_type: open
  name: Shopify Admin REST About Accounts API
  slug: open-shopify-accounts-api
- collection_type: open
  name: Shopify Admin REST About Activation API
  slug: open-shopify-activation-api
- collection_type: open
  name: Shopify Admin REST About Active API
  slug: open-shopify-active-api
- collection_type: open
  name: Shopify Admin REST About Address API
  slug: open-shopify-address-api
- collection_type: open
  name: Shopify Admin REST About Addresses API
  slug: open-shopify-addresses-api
- collection_type: open
  name: Shopify REST About Admin API
  slug: open-shopify-admin-api
- collection_type: open
  name: Shopify Admin REST API
  slug: open-shopify-admin-rest-api
- collection_type: open
  name: Shopify Ajax API
  slug: open-shopify-ajax-api
- collection_type: open
  name: Shopify Admin REST About All API
  slug: open-shopify-all-api
- collection_type: open
  name: Shopify Admin REST About Amount API
  slug: open-shopify-amount-api
- collection_type: open
  name: Shopify Admin REST About Another API
  slug: open-shopify-another-api
- collection_type: open
  name: Shopify  API
  slug: open-shopify-api
- collection_type: open
  name: Shopify Admin REST About Applications API
  slug: open-shopify-applications-api
- collection_type: open
  name: Shopify Admin REST About Approves API
  slug: open-shopify-approves-api
- collection_type: open
  name: Shopify Admin REST About Article API
  slug: open-shopify-article-api
- collection_type: open
  name: Shopify Admin REST About Assets API
  slug: open-shopify-assets-api
- collection_type: open
  name: Shopify Admin REST About Associated API
  slug: open-shopify-associated-api
- collection_type: open
  name: Shopify Admin REST About Authenticated API
  slug: open-shopify-authenticated-api
- collection_type: open
  name: Shopify Admin REST About Authors API
  slug: open-shopify-authors-api
- collection_type: open
  name: Shopify Admin REST About Available API
  slug: open-shopify-available-api
- collection_type: open
  name: Shopify Admin REST About Balance API
  slug: open-shopify-balance-api
- collection_type: open
  name: Shopify Admin REST About Belong API
  slug: open-shopify-belong-api
- collection_type: open
  name: Shopify Admin REST About Belonging API
  slug: open-shopify-belonging-api
- collection_type: open
  name: Shopify Admin REST About Blog API
  slug: open-shopify-blog-api
- collection_type: open
  name: Shopify Admin REST About Blogs API
  slug: open-shopify-blogs-api
- collection_type: open
  name: Shopify Admin REST About Bulk API
  slug: open-shopify-bulk-api
- collection_type: open
  name: Shopify Admin REST About Calls API
  slug: open-shopify-calls-api
- collection_type: open
  name: Shopify Admin REST About Cancel API
  slug: open-shopify-cancel-api
- collection_type: open
  name: Shopify Admin REST About Cancels API
  slug: open-shopify-cancels-api
- collection_type: open
  name: Shopify Admin REST About Card API
  slug: open-shopify-card-api
- collection_type: open
  name: Shopify Admin REST About Cards API
  slug: open-shopify-cards-api
- collection_type: open
  name: Shopify Admin REST About Carrier API
  slug: open-shopify-carrier-api
- collection_type: open
  name: Shopify Admin REST About Cart API
  slug: open-shopify-cart-api
- collection_type: open
  name: Shopify Admin REST About Charge API
  slug: open-shopify-charge-api
- collection_type: open
  name: Shopify Admin REST About Charges API
  slug: open-shopify-charges-api
- collection_type: open
  name: Shopify Admin REST About Checkout API
  slug: open-shopify-checkout-api
- collection_type: open
  name: Shopify Admin REST About Checkouts API
  slug: open-shopify-checkouts-api
- collection_type: open
  name: Shopify Admin REST About Code API
  slug: open-shopify-code-api
- collection_type: open
  name: Shopify Admin REST About Collect API
  slug: open-shopify-collect-api
- collection_type: open
  name: Shopify Admin REST About Collection API
  slug: open-shopify-collection-api
- collection_type: open
  name: Shopify Admin REST About Collections API
  slug: open-shopify-collections-api
- collection_type: open
  name: Shopify Admin REST About Comments API
  slug: open-shopify-comments-api
- collection_type: open
  name: Shopify Admin REST About Complete API
  slug: open-shopify-complete-api
- collection_type: open
  name: Shopify Admin REST About Configuration API
  slug: open-shopify-configuration-api
- collection_type: open
  name: Shopify Admin REST About Connects API
  slug: open-shopify-connects-api
- collection_type: open
  name: Shopify Admin REST About Contains API
  slug: open-shopify-contains-api
- collection_type: open
  name: Shopify Admin REST About Count API
  slug: open-shopify-count-api
- collection_type: open
  name: Shopify Admin REST About Countries API
  slug: open-shopify-countries-api
- collection_type: open
  name: Shopify Admin REST About Country API
  slug: open-shopify-country-api
- collection_type: open
  name: Shopify Admin REST About Counts API
  slug: open-shopify-counts-api
- collection_type: open
  name: Shopify Admin REST About County API
  slug: open-shopify-county-api
- collection_type: open
  name: Shopify Admin REST About Create API
  slug: open-shopify-create-api
- collection_type: open
  name: Shopify Admin REST About Creation API
  slug: open-shopify-creation-api
- collection_type: open
  name: Shopify Admin REST About Credit API
  slug: open-shopify-credit-api
- collection_type: open
  name: Shopify Admin REST About Currencies API
  slug: open-shopify-currencies-api
- collection_type: open
  name: Shopify Admin REST About Current API
  slug: open-shopify-current-api
- collection_type: open
  name: Shopify Admin REST About Custom API
  slug: open-shopify-custom-api
- collection_type: open
  name: Shopify Admin REST About Custom Collections API
  slug: open-shopify-custom-collections-api
- collection_type: open
  name: Shopify Admin REST About Customer Addresses API
  slug: open-shopify-customer-addresses-api
- collection_type: open
  name: Shopify Admin REST About Customer API
  slug: open-shopify-customer-api
- collection_type: open
  name: Shopify Admin REST About Customers API
  slug: open-shopify-customers-api
- collection_type: open
  name: Shopify Admin REST About Date API
  slug: open-shopify-date-api
- collection_type: open
  name: Shopify Admin REST About Days API
  slug: open-shopify-days-api
- collection_type: open
  name: Shopify Admin REST About Deletes API
  slug: open-shopify-deletes-api
- collection_type: open
  name: Shopify Admin REST About Disables API
  slug: open-shopify-disables-api
- collection_type: open
  name: Shopify Admin REST About Discount API
  slug: open-shopify-discount-api
- collection_type: open
  name: Shopify Admin REST About Dispute API
  slug: open-shopify-dispute-api
- collection_type: open
  name: Shopify Admin REST About Disputes API
  slug: open-shopify-disputes-api
- collection_type: open
  name: Shopify Admin REST About Enabled API
  slug: open-shopify-enabled-api
- collection_type: open
  name: Shopify Admin REST About Endpoint API
  slug: open-shopify-endpoint-api
- collection_type: open
  name: Shopify Admin REST About Events API
  slug: open-shopify-events-api
- collection_type: open
  name: Shopify Admin REST About Existing API
  slug: open-shopify-existing-api
- collection_type: open
  name: Shopify Admin REST About Files API
  slug: open-shopify-files-api
- collection_type: open
  name: Shopify Admin REST About Format API
  slug: open-shopify-format-api
- collection_type: open
  name: Shopify Admin REST About Fulfillment API
  slug: open-shopify-fulfillment-api
- collection_type: open
  name: Shopify Admin REST About Fulfillment Orders API
  slug: open-shopify-fulfillment-orders-api
- collection_type: open
  name: Shopify Admin REST About Fulfillments API
  slug: open-shopify-fulfillments-api
- collection_type: open
  name: Shopify Admin REST About Generate API
  slug: open-shopify-generate-api
- collection_type: open
  name: Shopify Admin REST About Get API
  slug: open-shopify-get-api
- collection_type: open
  name: Shopify Admin REST About Gift API
  slug: open-shopify-gift-api
- collection_type: open
  name: Shopify Admin REST About Have API
  slug: open-shopify-have-api
- collection_type: open
  name: Shopify Admin REST About Holds API
  slug: open-shopify-holds-api
- collection_type: open
  name: Shopify Admin REST About Identifiers API
  slug: open-shopify-identifiers-api
- collection_type: open
  name: Shopify Admin REST About Image API
  slug: open-shopify-image-api
- collection_type: open
  name: Shopify Admin REST About Images API
  slug: open-shopify-images-api
- collection_type: open
  name: Shopify Admin REST About Information API
  slug: open-shopify-information-api
- collection_type: open
  name: Shopify Admin REST About Inventory API
  slug: open-shopify-inventory-api
- collection_type: open
  name: Shopify Admin REST About Inventory Items API
  slug: open-shopify-inventory-items-api
- collection_type: open
  name: Shopify Admin REST About Inventory Levels API
  slug: open-shopify-inventory-levels-api
- collection_type: open
  name: Shopify Admin REST About Invites API
  slug: open-shopify-invites-api
- collection_type: open
  name: Shopify Admin REST About Issued API
  slug: open-shopify-issued-api
- collection_type: open
  name: Shopify Admin REST About Item API
  slug: open-shopify-item-api
- collection_type: open
  name: Shopify Admin REST About Items API
  slug: open-shopify-items-api
- collection_type: open
  name: Shopify Admin REST About Jobs API
  slug: open-shopify-jobs-api
- collection_type: open
  name: Shopify Admin REST About Keys API
  slug: open-shopify-keys-api
- collection_type: open
  name: Shopify Admin REST About Levels API
  slug: open-shopify-levels-api
- collection_type: open
  name: Shopify Admin REST About Line API
  slug: open-shopify-line-api
- collection_type: open
  name: Shopify Admin REST About Listing API
  slug: open-shopify-listing-api
- collection_type: open
  name: Shopify Admin REST About Listings API
  slug: open-shopify-listings-api
- collection_type: open
  name: Shopify Admin REST About Lists API
  slug: open-shopify-lists-api
- collection_type: open
  name: Shopify Admin REST About Location API
  slug: open-shopify-location-api
- collection_type: open
  name: Shopify Admin REST About Locations API
  slug: open-shopify-locations-api
- collection_type: open
  name: Shopify Admin REST About Make API
  slug: open-shopify-make-api
- collection_type: open
  name: Shopify Admin REST About Managed API
  slug: open-shopify-managed-api
- collection_type: open
  name: Shopify Admin REST About Many API
  slug: open-shopify-many-api
- collection_type: open
  name: Shopify Admin REST About Mark API
  slug: open-shopify-mark-api
- collection_type: open
  name: Shopify Admin REST About Match API
  slug: open-shopify-match-api
- collection_type: open
  name: Shopify Admin REST About Merchant API
  slug: open-shopify-merchant-api
- collection_type: open
  name: Shopify Admin REST About Metafields API
  slug: open-shopify-metafields-api
- collection_type: open
  name: Shopify Admin REST About Modifies API
  slug: open-shopify-modifies-api
- collection_type: open
  name: Shopify Admin REST About Modify API
  slug: open-shopify-modify-api
- collection_type: open
  name: Shopify Admin REST About Move API
  slug: open-shopify-move-api
- collection_type: open
  name: Shopify Admin REST About Moves API
  slug: open-shopify-moves-api
- collection_type: open
  name: Shopify Admin REST About Multipass API
  slug: open-shopify-multipass-api
- collection_type: open
  name: Shopify Admin REST About Multiple API
  slug: open-shopify-multiple-api
- collection_type: open
  name: Shopify Admin REST About Number API
  slug: open-shopify-number-api
- collection_type: open
  name: Shopify Admin REST About Numbers API
  slug: open-shopify-numbers-api
- collection_type: open
  name: Shopify Admin REST About Open API
  slug: open-shopify-open-api
- collection_type: open
  name: Shopify Admin REST About Operations API
  slug: open-shopify-operations-api
- collection_type: open
  name: Shopify Admin REST About Order API
  slug: open-shopify-order-api
- collection_type: open
  name: Shopify Admin REST About Ordered API
  slug: open-shopify-ordered-api
- collection_type: open
  name: Shopify Admin REST About Orders API
  slug: open-shopify-orders-api
- collection_type: open
  name: Shopify Admin REST About Particular API
  slug: open-shopify-particular-api
- collection_type: open
  name: Shopify Admin REST About Past API
  slug: open-shopify-past-api
- collection_type: open
  name: Shopify Admin REST About Payments API
  slug: open-shopify-payments-api
- collection_type: open
  name: Shopify Admin REST About Payouts API
  slug: open-shopify-payouts-api
- collection_type: open
  name: Shopify Admin REST About Policies API
  slug: open-shopify-policies-api
- collection_type: open
  name: Shopify Admin REST About Predictive Search API
  slug: open-shopify-predictive-search-api
- collection_type: open
  name: Shopify Admin REST About Previously API
  slug: open-shopify-previously-api
- collection_type: open
  name: Shopify Admin REST About Private API
  slug: open-shopify-private-api
- collection_type: open
  name: Shopify Admin REST About Product API
  slug: open-shopify-product-api
- collection_type: open
  name: Shopify Admin REST About Product Images API
  slug: open-shopify-product-images-api
- collection_type: open
  name: Shopify Admin REST About Product Recommendations API
  slug: open-shopify-product-recommendations-api
- collection_type: open
  name: Shopify Admin REST About Product Variants API
  slug: open-shopify-product-variants-api
- collection_type: open
  name: Shopify Admin REST About Products API
  slug: open-shopify-products-api
- collection_type: open
  name: Shopify Admin REST About Progress API
  slug: open-shopify-progress-api
- collection_type: open
  name: Shopify Admin REST About Providing API
  slug: open-shopify-providing-api
- collection_type: open
  name: Shopify Admin REST About Province API
  slug: open-shopify-province-api
- collection_type: open
  name: Shopify Admin REST About Public API
  slug: open-shopify-public-api
- collection_type: open
  name: Shopify Admin REST About Publish API
  slug: open-shopify-publish-api
- collection_type: open
  name: Shopify Admin REST About Published API
  slug: open-shopify-published-api
- collection_type: open
  name: Shopify Admin REST About Queries API
  slug: open-shopify-queries-api
- collection_type: open
  name: Shopify Admin REST About Rates API
  slug: open-shopify-rates-api
- collection_type: open
  name: Shopify Admin REST About Ready API
  slug: open-shopify-ready-api
- collection_type: open
  name: Shopify Admin REST About Recurring API
  slug: open-shopify-recurring-api
- collection_type: open
  name: Shopify Admin REST About Redirect API
  slug: open-shopify-redirect-api
- collection_type: open
  name: Shopify Admin REST About Redirects API
  slug: open-shopify-redirects-api
- collection_type: open
  name: Shopify Admin REST About Refund API
  slug: open-shopify-refund-api
- collection_type: open
  name: Shopify Admin REST About Refunds API
  slug: open-shopify-refunds-api
- collection_type: open
  name: Shopify Admin REST About Releases API
  slug: open-shopify-releases-api
- collection_type: open
  name: Shopify Admin REST About Reports API
  slug: open-shopify-reports-api
- collection_type: open
  name: Shopify Admin REST About Requests API
  slug: open-shopify-requests-api
- collection_type: open
  name: Shopify Admin REST About Required API
  slug: open-shopify-required-api
- collection_type: open
  name: Shopify Admin REST About Resource API
  slug: open-shopify-resource-api
- collection_type: open
  name: Shopify Admin REST About Retrieves API
  slug: open-shopify-retrieves-api
- collection_type: open
  name: Shopify Admin REST About Risk API
  slug: open-shopify-risk-api
- collection_type: open
  name: Shopify Admin REST About Rules API
  slug: open-shopify-rules-api
- collection_type: open
  name: Shopify Admin REST About Saved API
  slug: open-shopify-saved-api
- collection_type: open
  name: Shopify Admin REST About Scheduled API
  slug: open-shopify-scheduled-api
- collection_type: open
  name: Shopify Admin REST About Scopes API
  slug: open-shopify-scopes-api
- collection_type: open
  name: Shopify Admin REST About Script API
  slug: open-shopify-script-api
- collection_type: open
  name: Shopify Admin REST About Search API
  slug: open-shopify-search-api
- collection_type: open
  name: Shopify Admin REST About Searches API
  slug: open-shopify-searches-api
- collection_type: open
  name: Shopify Admin REST About Sends API
  slug: open-shopify-sends-api
- collection_type: open
  name: Shopify Admin REST About Sent API
  slug: open-shopify-sent-api
- collection_type: open
  name: Shopify Admin REST About Sessions API
  slug: open-shopify-sessions-api
- collection_type: open
  name: Shopify Admin REST About Sets API
  slug: open-shopify-sets-api
- collection_type: open
  name: Shopify Admin REST About Shipping API
  slug: open-shopify-shipping-api
- collection_type: open
  name: Shopify Admin REST About Shop API
  slug: open-shopify-shop-api
- collection_type: open
  name: Shopify Admin REST About Single API
  slug: open-shopify-single-api
- collection_type: open
  name: Shopify Admin REST About Smart API
  slug: open-shopify-smart-api
- collection_type: open
  name: Shopify Admin REST About Smart Collections API
  slug: open-shopify-smart-collections-api
- collection_type: open
  name: Shopify Admin REST About Spam API
  slug: open-shopify-spam-api
- collection_type: open
  name: Shopify Admin REST About Specific API
  slug: open-shopify-specific-api
- collection_type: open
  name: Shopify Admin REST About Storefront API
  slug: open-shopify-storefront-api
- collection_type: open
  name: Shopify Admin REST About Subscriptions API
  slug: open-shopify-subscriptions-api
- collection_type: open
  name: Shopify Admin REST About Summaries API
  slug: open-shopify-summaries-api
- collection_type: open
  name: Shopify Admin REST About Tender API
  slug: open-shopify-tender-api
- collection_type: open
  name: Shopify Admin REST About Theme API
  slug: open-shopify-theme-api
- collection_type: open
  name: Shopify Admin REST About Themes API
  slug: open-shopify-themes-api
- collection_type: open
  name: Shopify Admin REST About Time API
  slug: open-shopify-time-api
- collection_type: open
  name: Shopify Admin REST About Tokens API
  slug: open-shopify-tokens-api
- collection_type: open
  name: Shopify Admin REST About Topic API
  slug: open-shopify-topic-api
- collection_type: open
  name: Shopify Admin REST About Tracking API
  slug: open-shopify-tracking-api
- collection_type: open
  name: Shopify Admin REST About Transactions API
  slug: open-shopify-transactions-api
- collection_type: open
  name: Shopify Admin REST About Type API
  slug: open-shopify-type-api
- collection_type: open
  name: Shopify Admin REST About Update API
  slug: open-shopify-update-api
- collection_type: open
  name: Shopify Admin REST About Usage API
  slug: open-shopify-usage-api
- collection_type: open
  name: Shopify Admin REST About Used API
  slug: open-shopify-used-api
- collection_type: open
  name: Shopify Admin REST About Users API
  slug: open-shopify-users-api
- collection_type: open
  name: Shopify Admin REST About Variants API
  slug: open-shopify-variants-api
- collection_type: open
  name: Shopify Admin REST About Vault API
  slug: open-shopify-vault-api
- collection_type: open
  name: Shopify Admin REST About Versions API
  slug: open-shopify-versions-api
- collection_type: open
  name: Shopify Admin REST About Webhook Subscriptions API
  slug: open-shopify-webhook-subscriptions-api
- collection_type: open
  name: Shopify Admin REST About Webhooks API
  slug: open-shopify-webhooks-api
- collection_type: open
  name: Shopify Admin REST About Zip API
  slug: open-shopify-zip-api
- collection_type: open
  name: Shopify Admin REST About Zones API
  slug: open-shopify-zones-api
common:
- group: design
  href: https://artifacts.apis.io/shopify/rules/shopify-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/shopify-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/shopify/rules/shopify-rules.yml
  title: ''
  type: Spectral
  url: rules/shopify-rules.yml
- group: design
  href: https://artifacts.apis.io/shopify/rules/shopify-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/shopify-jsonschema-spectral-rules.yml
- group: other
  href: https://artifacts.apis.io/shopify/hosts/shopify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shopify-hosts.yml
- group: build
  href: https://artifacts.apis.io/shopify/integrations/shopify-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/shopify-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/shopify/vendors/shopify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shopify-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/shopify/finops/shopify-finops.yml
  title: ''
  type: FinOps
  url: finops/shopify-finops.yml
- group: other
  href: https://artifacts.apis.io/shopify/vendor-facets/shopify-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/shopify-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/shopify/capabilities/shopify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shopify-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/shopify/security/shopify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/shopify-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/shopify/agentic-access/shopify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shopify-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/shopify/security/shopify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shopify-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/shopify/authentication/shopify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shopify-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/shopify/overview
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-add-variant-to-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-add-variant-to-product-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-archive-stale-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-archive-stale-product-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-cancel-and-refund-order-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-cancel-and-refund-order-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-close-and-archive-order-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-close-and-archive-order-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-create-collection-with-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-collection-with-product-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-create-customer-with-address-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-customer-with-address-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-create-order-and-fulfill-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-order-and-fulfill-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-create-product-with-variant-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-create-product-with-variant-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-find-collection-and-list-products-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-find-collection-and-list-products-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-fulfill-existing-order-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-fulfill-existing-order-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-launch-product-with-stock-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-launch-product-with-stock-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-quote-to-paid-order-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-quote-to-paid-order-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-register-webhook-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-register-webhook-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-restock-product-variant-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-restock-product-variant-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-set-inventory-at-location-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-set-inventory-at-location-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-tag-order-by-fulfillment-status-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-tag-order-by-fulfillment-status-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-update-fulfillment-tracking-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-update-fulfillment-tracking-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-update-inventory-item-cost-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-update-inventory-item-cost-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-upsert-customer-by-email-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-customer-by-email-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-upsert-customer-then-order-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-customer-then-order-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-upsert-product-by-title-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-product-by-title-workflow.yml
- group: design
  href: https://artifacts.apis.io/shopify/arazzo/shopify-upsert-webhook-by-topic-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/shopify-upsert-webhook-by-topic-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopify
- group: docs
  title: ''
  type: Documentation
  url: https://shopify.dev/docs
- group: design
  title: ''
  type: Versioning
  url: https://shopify.dev/docs/api/usage/versioning
- group: auth
  title: ''
  type: Authentication
  url: https://shopify.dev/docs/api/usage/authentication
- group: build
  title: ''
  type: CLI
  url: https://shopify.dev/docs/api/shopify-cli
- group: docs
  title: ''
  type: Documentation
  url: https://shopify.dev/docs/api
- group: start
  title: ''
  type: Portal
  url: https://shopify.dev
- group: build
  title: ''
  type: SDKs
  url: https://shopify.dev/docs/api/libraries-and-templates
- group: operate
  title: ''
  type: RateLimits
  url: https://shopify.dev/docs/api/usage/rate-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://shopify.dev/changelog
- group: design
  title: ''
  type: Versioning
  url: https://shopify.dev/docs/api/usage/versioning
- group: operate
  title: ''
  type: StatusPage
  url: https://www.shopifystatus.com
- group: operate
  title: ''
  type: Support
  url: https://community.shopify.dev/c/dev-platform/32
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shopify.com/legal/api-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopify.com/legal/privacy
- group: start
  title: ''
  type: Signup
  url: https://partners.shopify.com/signup
- group: design
  title: ''
  type: Webhooks
  url: https://shopify.dev/docs/apps/build/webhooks
- group: auth
  href: https://artifacts.apis.io/shopify/security/shopify-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/shopify-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: AuthenticationDocs
  url: https://shopify.dev/docs/apps/build/authentication-authorization
- group: auth
  title: ''
  type: Access Scopes
  url: https://shopify.dev/docs/api/usage/access-scopes
- group: operate
  title: ''
  type: Forums
  url: https://community.shopify.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Shopify
- group: company
  title: ''
  type: Blog
  url: https://shopify.engineering/
- group: other
  title: ''
  type: Headless
  url: https://shopify.dev/docs/storefronts/headless
- group: other
  title: ''
  type: Design System
  url: https://shopify.dev/docs/api/polaris
- group: other
  title: ''
  type: App Bridge
  url: https://shopify.dev/docs/api/app-bridge
- group: other
  title: ''
  type: Application Marketplace
  url: https://apps.shopify.com
- group: company
  title: ''
  type: Partner Program
  url: https://www.shopify.com/partners
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@shopifydevs
- group: start
  title: ''
  type: GettingStarted
  url: https://shopify.dev/docs/apps/build
- group: build
  title: ''
  type: Extensions
  url: https://shopify.dev/docs/apps/build/app-extensions
- group: other
  title: ''
  type: Themes
  url: https://shopify.dev/docs/themes
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/shopify
- group: company
  title: ''
  type: Website
  url: https://www.shopify.com
- group: start
  title: ''
  type: Login
  url: https://accounts.shopify.com
- group: operate
  title: ''
  type: Community
  url: https://community.shopify.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: https://shopify.dev/docs/api/release-notes
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Shopify/shopify-app-js
- group: build
  title: ''
  type: SDKs
  url: https://shopify.dev/docs/storefronts/headless/additional-sdks
- group: build
  href: https://artifacts.apis.io/shopify/packages/shopify-packages.yml
  title: ''
  type: Packages
  url: packages/shopify-packages.yml
- group: build
  href: https://artifacts.apis.io/shopify/packages/shopify-packages.yml
  title: ''
  type: SDKs
  url: packages/shopify-packages.yml
- group: agent
  href: https://artifacts.apis.io/shopify/well-known/shopify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shopify-well-known.yml
- group: auth
  href: https://artifacts.apis.io/shopify/well-known/shopify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shopify-security.txt
- group: agent
  href: https://artifacts.apis.io/shopify/mcp/shopify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/shopify-mcp.yml
- group: build
  href: https://artifacts.apis.io/shopify/mcp/shopify-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/shopify-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/shopify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/shopify/overlays/shopify-admin-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shopify-admin-rest-overlay.yaml
- group: other
  href: https://artifacts.apis.io/shopify/overlays/shopify-ajax-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shopify-ajax-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/shopify/conformance/shopify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shopify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/shopify/security/shopify-trust-center.yml
  title: ''
  type: Compliance
  url: security/shopify-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/shopify/security/shopify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/shopify-trust-center.yml
- group: design
  href: https://artifacts.apis.io/shopify/errors/shopify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shopify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shopify/lifecycle/shopify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shopify-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://shopify.dev/docs/api/usage/versioning#deprecation-practices
- group: auth
  href: https://artifacts.apis.io/shopify/scopes/shopify-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/shopify-scopes.yml
- group: design
  href: https://artifacts.apis.io/shopify/conventions/shopify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shopify-conventions.yml
- group: design
  href: https://artifacts.apis.io/shopify/conventions/shopify-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/shopify-conventions.yml
- group: start
  href: https://artifacts.apis.io/shopify/sandbox/shopify-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/shopify-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/shopify/changelog/shopify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shopify-changelog.yml
- group: build
  href: https://artifacts.apis.io/shopify/cli/shopify-cli.yml
  title: ''
  type: CLI
  url: cli/shopify-cli.yml
- group: design
  href: https://artifacts.apis.io/shopify/components/shopify-components.yml
  title: ''
  type: Components
  url: components/shopify-components.yml
- group: design
  href: https://artifacts.apis.io/shopify/data-model/shopify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shopify-data-model.yml
- group: design
  href: https://artifacts.apis.io/shopify/asyncapi/shopify-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shopify-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/shopify/plans/shopify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shopify-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/shopify/rate-limits/shopify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shopify-rate-limits.yml
- group: docs
  href: https://artifacts.apis.io/shopify/graphql/shopify-storefront-api.graphql
  title: ''
  type: GraphQL
  url: graphql/shopify-storefront-api.graphql
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shopify.com/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://shopify.dev/docs/api
created: '2024-04-14'
description: Shopify is a complete commerce platform that lets you start, grow, and manage a business, selling online, in person, on marketplaces, through social channels, and now inside AI chats. Its developer platform exposes GraphQL Admin, Storefront and Customer Account APIs, a legacy Admin REST surface, 206 webhook topics, Shopify Functions, Hydrogen and the Shopify CLI, so apps and integrations can extend Shopify for merchants and buyers alike. Shopify also runs four MCP servers bound to the Universal Commerce Protocol, letting AI agents search a cross-merchant catalog, build carts, complete checkouts and track orders.
examples:
- key_count: 4
  name: Shopify Create Product Example
  slug: shopify-create-product-example
- key_count: 4
  name: Shopify List Orders Example
  slug: shopify-list-orders-example
features:
- REST Admin API with leaky-bucket throttling (40 req/app/store)
- GraphQL Admin API with cost-based throttling (1,000 pts on Standard, 2,000 on Plus)
- Storefront API for headless commerce
- 'Plans: Basic ($29), Grow ($79), Advanced ($299), Plus ($2,300)'
- Online card transaction fees from 2.25% (Plus) to 2.9% (Basic)
- Third-party gateway fees from 0% (Plus) to 2% (Basic)
- AI assistant for commerce included on all plans
- Up to 200 POS Pro locations on Plus
- B2B / wholesale on Plus
- Customizable checkout on Plus
- Bulk operations for large data exports without rate-limit hits
- Webhooks for order, customer, inventory, and product events
- OAuth 2.0 app authentication
- Shopify Functions for backend customization
- Shopify Markets for region-specific currencies and pricing
finops:
- has_sources: true
  method: derived
  name: Shopify Finops
  primary_unit: location
  service_category: ''
  slug: shopify-finops
  template: false
graphqls:
- description: The GraphQL Admin API lets you build apps and integrations that extend and enhance the Shopify admin. It provides access to products, customers, orders, inventory, fulfillment, and more. GraphQL is th
  name: Shopify GraphQL API
  slug: shopify-graphql
image: https://cdn.shopify.com/shopifycloud/brochure/assets/brand-assets/shopify-logo.png
json_schemas:
- name: Shopify Collection
  property_count: 13
  slug: shopify-collection
- name: Shopify Customer
  property_count: 22
  slug: shopify-customer
- name: Shopify Fulfillment
  property_count: 18
  slug: shopify-fulfillment
- name: Shopify Inventory Item
  property_count: 12
  slug: shopify-inventory-item
- name: Shopify Order
  property_count: 36
  slug: shopify-order
- name: Shopify Product
  property_count: 18
  slug: shopify-product
- name: WebhookInput
  property_count: 4
  slug: shopify-webhook-input
- name: Webhook
  property_count: 9
  slug: shopify-webhook
json_structures:
- name: Shopify Order Structure
  property_count: 0
  slug: shopify-order-structure
- name: Shopify Product Structure
  property_count: 0
  slug: shopify-product-structure
jsonld:
- class_count: 75
  name: Shopify Context
  property_count: 29
  slug: shopify-context
layout: provider
mcp_servers:
- description: Shopify ships more MCP surface than any other commerce platform in this catalog, across four distinct servers. One is a hosted, anonymous, cross-merchant server on Shopify's own domain (Global Catalog
  name: Shopify Global Catalog MCP (remote) + Storefront/Cart/Checkout MCP + Dev MCP (stdio)
  slug: shopify-global-catalog-mcp-remote-storefront-cart-checkout-mcp-dev-mcp-stdio
modified: '2026-09-16'
name: Shopify
nav: Providers
network: true
overview: 'Shopify publishes 102 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks API, Multipass API, About API, and 99 more. Tagged areas include Commerce, E-Commerce, Payments, Retail, and Shopping Cart.


  The Shopify catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Shopify''s developer surface includes authentication, documentation, CLI, developer portal, changelog, support, signup flow, and 97 more developer resources.'
plans:
- name: Shopify Plans Pricing
  plan_count: 9
  slug: shopify-plans-pricing
- name: Shopify Price Estimates
  plan_count: 0
  slug: shopify-price-estimates
random_paper: 2
rate_limits:
- limit_count: 7
  name: Shopify Rate Limits
  slug: shopify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Shopify — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shopify-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Shopify API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 5
  slug: shopify-rules
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Shopify API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: shopify-spectral-rules
scopes:
- name: Shopify Scopes
  scope_count: 137
  slug: shopify-scopes
  summary_line: 137 scopes · authorization_code/token_exchange
score:
  band: exemplar
  composite: 84.6
  coverage:
    artifact_dirs: 46
    catalog_earned: 91.5
    catalog_earned_first_party: 29.0
    catalog_gap: 23.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 70.7
    developer_ergonomics: 96.4
    discoverability: 71.7
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 84.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 24.4
      derived: 0
      marker_coverage: 0.0
      total: 86
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 41.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shopify/shopify-2026-06-20T165931.png
security:
- kind: authentication
  name: Shopify Authentication
  slug: shopify-authentication
  summary_line: apiKey/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Shopify Domain Security
  slug: shopify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shopify Vulnerability Disclosure
  slug: shopify-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Shopify Trust Center
  slug: shopify-trust-center
  summary_line: PCI DSS, SOC 2 Type II, SOC 3
skill_count: 21
skills:
- name: shopify-admin
  slug: shopify-admin
- name: shopify-app-store-review
  slug: shopify-app-store-review
- name: shopify-custom-data
  slug: shopify-custom-data
- name: shopify-customer
  slug: shopify-customer
- name: shopify-dev
  slug: shopify-dev
- name: shopify-functions
  slug: shopify-functions
- name: shopify-hydrogen
  slug: shopify-hydrogen
- name: shopify-liquid
  slug: shopify-liquid
- name: shopify-onboarding-dev
  slug: shopify-onboarding-dev
- name: shopify-onboarding-merchant
  slug: shopify-onboarding-merchant
- name: shopify-partner
  slug: shopify-partner
- name: shopify-payments-apps
  slug: shopify-payments-apps
- name: shopify-polaris-admin-extensions
  slug: shopify-polaris-admin-extensions
- name: shopify-polaris-app-home
  slug: shopify-polaris-app-home
- name: shopify-polaris-checkout-extensions
  slug: shopify-polaris-checkout-extensions
- name: shopify-polaris-customer-account-extensions
  slug: shopify-polaris-customer-account-extensions
- name: shopify-pos-ui
  slug: shopify-pos-ui
- name: shopify-shopifyql
  slug: shopify-shopifyql
- name: shopify-storefront-graphql
  slug: shopify-storefront-graphql
- name: shopify-use-shopify-cli
  slug: shopify-use-shopify-cli
- name: ucp
  slug: ucp
slug: shopify
tags:
- Commerce
- E-Commerce
- Payments
- Retail
- Shopping Cart
- T1
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- Point-of-Sale
- Canada
website: https://www.shopify.com
---
