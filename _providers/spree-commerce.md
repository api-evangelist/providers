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
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 311
  human_in_the_loop: 5
  name: Spree Commerce Agentic Access
  operation_count: 524
  slug: spree-commerce-agentic-access
  summary_line: 524 operations · 311 acting · 5 human-in-the-loop
api_count: 5
apis:
- description: Outbound webhook event system - the Spree server emits signed JSON payloads for order, product, customer, payment, and shipment lifecycle events. The webhook envelope carries an id, event name, create
  name: Spree Webhooks
  slug: webhooks
- description: Official TypeScript SDK for the Spree Store API - typed clients, auth helpers, and resource methods. Distributed via npm as @spree/sdk and consumed by the Next.js storefront, custom storefronts, and s
  name: '@spree/sdk (TypeScript Store API SDK)'
  slug: sdk
- description: Official TypeScript SDK for the Spree Admin API. Provides a typed client for managing products, orders, customers, and store configuration from Node.js services and admin tools.
  name: '@spree/admin-sdk (TypeScript Admin API SDK)'
  slug: admin-sdk
- description: Command-line tool for managing Spree Commerce projects - scaffolding new apps, running the dev server, managing Docker, and orchestrating common project tasks. Installed via npm and exposed as the spr
  name: '@spree/cli'
  slug: cli
- description: One-line project generator for new Spree Commerce installations - mirrors create-next-app and create-medusa-app patterns. Bootstraps a working Rails-based Spree project from the spree-starter template
  name: create-spree-app
  slug: create-spree-app
- description: Open-source Next.js storefront talking to the Spree Storefront API - cart, checkout, account, multi-region, one-page checkout, and Stripe, Adyen, and PayPal payments. MIT licensed.
  name: Spree Next.js Storefront
  slug: nextjs-storefront
- description: Spree 5 storefront built with Ruby on Rails and a visual page builder. Reference implementation for teams that want a Rails-monolith storefront on top of Spree rather than a separate JavaScript runtim
  name: Spree Rails Storefront
  slug: rails-storefront
- description: Reference Spree application template used to bootstrap new Spree installations - includes Docker Compose, the recommended gem set, and a sensible default configuration for self-hosted deployments.
  name: spree-starter (Application Template)
  slug: starter
- description: Extension for running and administering multiple stores from a single Spree installation - per-store products, taxonomies, domains, and configuration.
  name: spree-multi-store
  slug: multi-store
- description: Official Stripe payments integration for Spree, including support for Stripe Connect. Wires Spree's payment lifecycle to Stripe Payment Intents and Webhooks.
  name: Spree Stripe Integration
  slug: stripe
- description: Official Adyen payments platform integration for Spree Commerce - payment methods, capture, refund, and webhook handling against the Adyen API.
  name: Spree Adyen Integration
  slug: adyen
- description: Official PayPal Checkout integration extension for Spree - PayPal buttons, order flow, capture, and refund.
  name: Spree PayPal Checkout Integration
  slug: paypal-checkout
- description: Officially certified Avalara AvaTax tax-calculation integration for Spree - real-time tax calculation, address validation, and document filing against AvaTax.
  name: Spree Avalara AvaTax Integration
  slug: avatax
- description: Official Klaviyo marketing-platform integration for Spree - syncs customers, orders, and product events to Klaviyo for email and SMS lifecycle marketing.
  name: Spree Klaviyo Integration
  slug: klaviyo
- description: Official Google Analytics 4 integration for Spree - ecommerce event tracking and measurement on top of the Spree storefronts.
  name: Spree Google Analytics 4 Integration
  slug: google-analytics
- description: CLI tool for generating and managing Spree Commerce extensions - scaffolds the gemspec, engine, migrations, and conventions used by the Spree extension ecosystem.
  name: spree_extension (Extension Generator CLI)
  slug: extension
- description: Internal developer tooling for working on Spree itself - debuggers, profilers, dummy data generators, and helpers used by Spree's core contributors and extension authors.
  name: Spree Dev Tools
  slug: dev-tools
- description: Rails plugin maintained under the Spree organization that lets Spree stores customize ERB views without forking the underlying templates. Core extension primitive in the Spree ecosystem.
  name: deface (Rails View Customization)
  slug: deface
- description: Monorepo with the Spree Rails engine, Admin, Store/Admin/Platform/ Storefront APIs, OpenAPI specs, TypeScript SDKs, CLI, and Next.js storefront. Released since 2007; latest stable release v5.4.3.
  name: Spree Core Repository (spree/spree)
  slug: core-repo
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Account / Address API from Spree Commerce — 2 operation(s) for account / address.
  name: Spree Commerce Account / Address API
  slug: spree-commerce-account-address-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Account API from Spree Commerce — 1 operation(s) for account.
  name: Spree Commerce Account API
  slug: spree-commerce-account-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Account / Credit Cards API from Spree Commerce — 3 operation(s) for account / credit cards.
  name: Spree Commerce Account / Credit Cards API
  slug: spree-commerce-account-credit-cards-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Account / Orders API from Spree Commerce — 2 operation(s) for account / orders.
  name: Spree Commerce Account / Orders API
  slug: spree-commerce-account-orders-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Addresses API from Spree Commerce — 2 operation(s) for addresses.
  name: Spree Commerce Addresses API
  slug: spree-commerce-addresses-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Adjustments API from Spree Commerce — 2 operation(s) for adjustments.
  name: Spree Commerce Adjustments API
  slug: spree-commerce-adjustments-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Adyen API from Spree Commerce — 3 operation(s) for adyen.
  name: Spree Commerce Adyen API
  slug: spree-commerce-adyen-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Admin user authentication
  name: Spree Commerce Authentication API
  slug: spree-commerce-authentication-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Cart API from Spree Commerce — 1 operation(s) for cart.
  name: Spree Commerce Cart API
  slug: spree-commerce-cart-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Cart / Coupons API from Spree Commerce — 3 operation(s) for cart / coupons.
  name: Spree Commerce Cart / Coupons API
  slug: spree-commerce-cart-coupons-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Cart / Line Items API from Spree Commerce — 3 operation(s) for cart / line items.
  name: Spree Commerce Cart / Line Items API
  slug: spree-commerce-cart-line-items-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Cart / Other API from Spree Commerce — 4 operation(s) for cart / other.
  name: Spree Commerce Cart / Other API
  slug: spree-commerce-cart-other-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Shopping cart management
  name: Spree Commerce Carts API
  slug: spree-commerce-carts-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Checkout API from Spree Commerce — 2 operation(s) for checkout.
  name: Spree Commerce Checkout API
  slug: spree-commerce-checkout-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Checkout / Payments API from Spree Commerce — 2 operation(s) for checkout / payments.
  name: Spree Commerce Checkout / Payments API
  slug: spree-commerce-checkout-payments-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Checkout / Shipments API from Spree Commerce — 2 operation(s) for checkout / shipments.
  name: Spree Commerce Checkout / Shipments API
  slug: spree-commerce-checkout-shipments-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Checkout / State API from Spree Commerce — 3 operation(s) for checkout / state.
  name: Spree Commerce Checkout / State API
  slug: spree-commerce-checkout-state-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Checkout / Store Credit API from Spree Commerce — 2 operation(s) for checkout / store credit.
  name: Spree Commerce Checkout / Store Credit API
  slug: spree-commerce-checkout-store-credit-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Classifications API from Spree Commerce — 2 operation(s) for classifications.
  name: Spree Commerce Classifications API
  slug: spree-commerce-classifications-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The CMS Pages API from Spree Commerce — 2 operation(s) for cms pages.
  name: Spree Commerce CMS Pages API
  slug: spree-commerce-cms-pages-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The CMS Sections API from Spree Commerce — 2 operation(s) for cms sections.
  name: Spree Commerce CMS Sections API
  slug: spree-commerce-cms-sections-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Store configuration — payment methods, tag autocomplete
  name: Spree Commerce Configuration API
  slug: spree-commerce-configuration-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Countries API from Spree Commerce — 5 operation(s) for countries.
  name: Spree Commerce Countries API
  slug: spree-commerce-countries-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Custom Fields API from Spree Commerce — 2 operation(s) for custom fields.
  name: Spree Commerce Custom Fields API
  slug: spree-commerce-custom-fields-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Customer management — profiles, addresses, store credits, credit cards
  name: Spree Commerce Customers API
  slug: spree-commerce-customers-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Data Feeds API from Spree Commerce — 2 operation(s) for data feeds.
  name: Spree Commerce Data Feeds API
  slug: spree-commerce-data-feeds-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Digital Assets API from Spree Commerce — 2 operation(s) for digital assets.
  name: Spree Commerce Digital Assets API
  slug: spree-commerce-digital-assets-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Digital Downloads API from Spree Commerce — 1 operation(s) for digital downloads.
  name: Spree Commerce Digital Downloads API
  slug: spree-commerce-digital-downloads-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Digital Links API from Spree Commerce — 3 operation(s) for digital links.
  name: Spree Commerce Digital Links API
  slug: spree-commerce-digital-links-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Digital product downloads
  name: Spree Commerce Digitals API
  slug: spree-commerce-digitals-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Exports API from Spree Commerce — 3 operation(s) for exports.
  name: Spree Commerce Exports API
  slug: spree-commerce-exports-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Gift Cards API from Spree Commerce — 4 operation(s) for gift cards.
  name: Spree Commerce Gift Cards API
  slug: spree-commerce-gift-cards-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Line Items API from Spree Commerce — 2 operation(s) for line items.
  name: Spree Commerce Line Items API
  slug: spree-commerce-line-items-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Markets, countries, currencies, and locales
  name: Spree Commerce Markets API
  slug: spree-commerce-markets-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Menu Items API from Spree Commerce — 3 operation(s) for menu items.
  name: Spree Commerce Menu Items API
  slug: spree-commerce-menu-items-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Menus API from Spree Commerce — 2 operation(s) for menus.
  name: Spree Commerce Menus API
  slug: spree-commerce-menus-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Guest and customer newsletter subscriptions (double opt-in)
  name: Spree Commerce Newsletter Subscribers API
  slug: spree-commerce-newsletter-subscribers-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Option Types API from Spree Commerce — 2 operation(s) for option types.
  name: Spree Commerce Option Types API
  slug: spree-commerce-option-types-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Option Values API from Spree Commerce — 2 operation(s) for option values.
  name: Spree Commerce Option Values API
  slug: spree-commerce-option-values-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Order Status API from Spree Commerce — 1 operation(s) for order status.
  name: Spree Commerce Order Status API
  slug: spree-commerce-order-status-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Order management — orders, items, payments, fulfillments, refunds, gift cards, store credits
  name: Spree Commerce Orders API
  slug: spree-commerce-orders-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Payment Methods API from Spree Commerce — 2 operation(s) for payment methods.
  name: Spree Commerce Payment Methods API
  slug: spree-commerce-payment-methods-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Payments API from Spree Commerce — 2 operation(s) for payments.
  name: Spree Commerce Payments API
  slug: spree-commerce-payments-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Store policies (return policy, privacy policy, terms of service)
  name: Spree Commerce Policies API
  slug: spree-commerce-policies-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Post Categories API from Spree Commerce — 2 operation(s) for post categories.
  name: Spree Commerce Post Categories API
  slug: spree-commerce-post-categories-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Posts API from Spree Commerce — 2 operation(s) for posts.
  name: Spree Commerce Posts API
  slug: spree-commerce-posts-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: Products, variants, and option types
  name: Spree Commerce Product Catalog API
  slug: spree-commerce-product-catalog-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Products API from Spree Commerce — 6 operation(s) for products.
  name: Spree Commerce Products API
  slug: spree-commerce-products-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Promotion Actions API from Spree Commerce — 2 operation(s) for promotion actions.
  name: Spree Commerce Promotion Actions API
  slug: spree-commerce-promotion-actions-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Promotion Categories API from Spree Commerce — 2 operation(s) for promotion categories.
  name: Spree Commerce Promotion Categories API
  slug: spree-commerce-promotion-categories-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Promotion Rules API from Spree Commerce — 2 operation(s) for promotion rules.
  name: Spree Commerce Promotion Rules API
  slug: spree-commerce-promotion-rules-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Promotions API from Spree Commerce — 11 operation(s) for promotions.
  name: Spree Commerce Promotions API
  slug: spree-commerce-promotions-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Roles API from Spree Commerce — 2 operation(s) for roles.
  name: Spree Commerce Roles API
  slug: spree-commerce-roles-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Shipments API from Spree Commerce — 9 operation(s) for shipments.
  name: Spree Commerce Shipments API
  slug: spree-commerce-shipments-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Shipping Categories API from Spree Commerce — 2 operation(s) for shipping categories.
  name: Spree Commerce Shipping Categories API
  slug: spree-commerce-shipping-categories-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Shipping Methods API from Spree Commerce — 2 operation(s) for shipping methods.
  name: Spree Commerce Shipping Methods API
  slug: spree-commerce-shipping-methods-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The States API from Spree Commerce — 2 operation(s) for states.
  name: Spree Commerce States API
  slug: spree-commerce-states-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Stock Items API from Spree Commerce — 2 operation(s) for stock items.
  name: Spree Commerce Stock Items API
  slug: spree-commerce-stock-items-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Stock Locations API from Spree Commerce — 2 operation(s) for stock locations.
  name: Spree Commerce Stock Locations API
  slug: spree-commerce-stock-locations-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Store Credit Categories API from Spree Commerce — 2 operation(s) for store credit categories.
  name: Spree Commerce Store Credit Categories API
  slug: spree-commerce-store-credit-categories-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Store Credit Types API from Spree Commerce — 2 operation(s) for store credit types.
  name: Spree Commerce Store Credit Types API
  slug: spree-commerce-store-credit-types-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Store Credits API from Spree Commerce — 2 operation(s) for store credits.
  name: Spree Commerce Store Credits API
  slug: spree-commerce-store-credits-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Stores API from Spree Commerce — 1 operation(s) for stores.
  name: Spree Commerce Stores API
  slug: spree-commerce-stores-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Stripe API from Spree Commerce — 4 operation(s) for stripe.
  name: Spree Commerce Stripe API
  slug: spree-commerce-stripe-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Tax Categories API from Spree Commerce — 2 operation(s) for tax categories.
  name: Spree Commerce Tax Categories API
  slug: spree-commerce-tax-categories-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Tax Rates API from Spree Commerce — 2 operation(s) for tax rates.
  name: Spree Commerce Tax Rates API
  slug: spree-commerce-tax-rates-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Taxonomies API from Spree Commerce — 2 operation(s) for taxonomies.
  name: Spree Commerce Taxonomies API
  slug: spree-commerce-taxonomies-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Taxons API from Spree Commerce — 5 operation(s) for taxons.
  name: Spree Commerce Taxons API
  slug: spree-commerce-taxons-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Token API from Spree Commerce — 1 operation(s) for token.
  name: Spree Commerce Token API
  slug: spree-commerce-token-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Users API from Spree Commerce — 2 operation(s) for users.
  name: Spree Commerce Users API
  slug: spree-commerce-users-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Variants API from Spree Commerce — 3 operation(s) for variants.
  name: Spree Commerce Variants API
  slug: spree-commerce-variants-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Vendors API from Spree Commerce — 10 operation(s) for vendors.
  name: Spree Commerce Vendors API
  slug: spree-commerce-vendors-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Webhook Events API from Spree Commerce — 1 operation(s) for webhook events.
  name: Spree Commerce Webhook Events API
  slug: spree-commerce-webhook-events-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Webhook Subscribers API from Spree Commerce — 2 operation(s) for webhook subscribers.
  name: Spree Commerce Webhook Subscribers API
  slug: spree-commerce-webhook-subscribers-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Wished Items API from Spree Commerce — 2 operation(s) for wished items.
  name: Spree Commerce Wished Items API
  slug: spree-commerce-wished-items-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Wishlists API from Spree Commerce — 9 operation(s) for wishlists.
  name: Spree Commerce Wishlists API
  slug: spree-commerce-wishlists-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Wishlists / Wished Items API from Spree Commerce — 5 operation(s) for wishlists / wished items.
  name: Spree Commerce Wishlists / Wished Items API
  slug: spree-commerce-wishlists-wished-items-api
- baseURL: https://demo.spreecommerce.org
  baseurl_source: declared
  description: The Zones API from Spree Commerce — 2 operation(s) for zones.
  name: Spree Commerce Zones API
  slug: spree-commerce-zones-api
- description: The Account / Address API from Spree Commerce — 2 operation(s) for account / address.
  name: Spree Commerce Account / Address API
  slug: spree-account-address-api
- description: The Account API from Spree Commerce — 1 operation(s) for account.
  name: Spree Commerce Account API
  slug: spree-account-api
- description: The Account / Credit Cards API from Spree Commerce — 3 operation(s) for account / credit cards.
  name: Spree Commerce Account / Credit Cards API
  slug: spree-account-credit-cards-api
- description: The Account / Orders API from Spree Commerce — 2 operation(s) for account / orders.
  name: Spree Commerce Account / Orders API
  slug: spree-account-orders-api
- description: The Addresses API from Spree Commerce — 2 operation(s) for addresses.
  name: Spree Commerce Addresses API
  slug: spree-addresses-api
- description: The Adjustments API from Spree Commerce — 2 operation(s) for adjustments.
  name: Spree Commerce Adjustments API
  slug: spree-adjustments-api
- description: The Adyen API from Spree Commerce — 3 operation(s) for adyen.
  name: Spree Commerce Adyen API
  slug: spree-adyen-api
- description: CORS allowlist for storefront and admin client origins
  name: Spree Commerce Allowed Origins API
  slug: spree-allowed-origins-api
- description: Secret and publishable API keys
  name: Spree Commerce API Keys API
  slug: spree-api-keys-api
- description: Admin user login, logout, token refresh, and current user profile
  name: Spree Commerce Authentication API
  slug: spree-authentication-api
- description: The Cart API from Spree Commerce — 1 operation(s) for cart.
  name: Spree Commerce Cart API
  slug: spree-cart-api
- description: The Cart / Coupons API from Spree Commerce — 3 operation(s) for cart / coupons.
  name: Spree Commerce Cart / Coupons API
  slug: spree-cart-coupons-api
- description: The Cart / Line Items API from Spree Commerce — 3 operation(s) for cart / line items.
  name: Spree Commerce Cart / Line Items API
  slug: spree-cart-line-items-api
- description: The Cart / Other API from Spree Commerce — 4 operation(s) for cart / other.
  name: Spree Commerce Cart / Other API
  slug: spree-cart-other-api
- description: Shopping cart management
  name: Spree Commerce Carts API
  slug: spree-carts-api
- description: Sales channels and product publication across channels
  name: Spree Commerce Channels API
  slug: spree-channels-api
- description: The Checkout API from Spree Commerce — 2 operation(s) for checkout.
  name: Spree Commerce Checkout API
  slug: spree-checkout-api
- description: The Checkout / Payments API from Spree Commerce — 2 operation(s) for checkout / payments.
  name: Spree Commerce Checkout / Payments API
  slug: spree-checkout-payments-api
- description: The Checkout / Shipments API from Spree Commerce — 2 operation(s) for checkout / shipments.
  name: Spree Commerce Checkout / Shipments API
  slug: spree-checkout-shipments-api
- description: The Checkout / State API from Spree Commerce — 3 operation(s) for checkout / state.
  name: Spree Commerce Checkout / State API
  slug: spree-checkout-state-api
- description: The Checkout / Store Credit API from Spree Commerce — 2 operation(s) for checkout / store credit.
  name: Spree Commerce Checkout / Store Credit API
  slug: spree-checkout-store-credit-api
- description: The Classifications API from Spree Commerce — 2 operation(s) for classifications.
  name: Spree Commerce Classifications API
  slug: spree-classifications-api
- description: The CMS Pages API from Spree Commerce — 2 operation(s) for cms pages.
  name: Spree Commerce CMS Pages API
  slug: spree-cms-pages-api
- description: The CMS Sections API from Spree Commerce — 2 operation(s) for cms sections.
  name: Spree Commerce CMS Sections API
  slug: spree-cms-sections-api
- description: The Countries API from Spree Commerce — 5 operation(s) for countries.
  name: Spree Commerce Countries API
  slug: spree-countries-api
- description: Custom field definitions for products, variants, customers, and other resources
  name: Spree Commerce Custom Fields API
  slug: spree-custom-fields-api
- description: Customer groups for segmenting customers (e.g. wholesale, VIP) used by pricing and promotions
  name: Spree Commerce Customer Groups API
  slug: spree-customer-groups-api
- description: Customer profiles, addresses, credit cards, and store credits
  name: Spree Commerce Customers API
  slug: spree-customers-api
- description: The Data Feeds API from Spree Commerce — 2 operation(s) for data feeds.
  name: Spree Commerce Data Feeds API
  slug: spree-data-feeds-api
- description: The Digital Assets API from Spree Commerce — 2 operation(s) for digital assets.
  name: Spree Commerce Digital Assets API
  slug: spree-digital-assets-api
- description: The Digital Downloads API from Spree Commerce — 1 operation(s) for digital downloads.
  name: Spree Commerce Digital Downloads API
  slug: spree-digital-downloads-api
- description: The Digital Links API from Spree Commerce — 3 operation(s) for digital links.
  name: Spree Commerce Digital Links API
  slug: spree-digital-links-api
- description: Digital product downloads
  name: Spree Commerce Digitals API
  slug: spree-digitals-api
- description: Async CSV exports of admin resources
  name: Spree Commerce Exports API
  slug: spree-exports-api
- description: Order fulfillments — shipments, fulfill, cancel, resume, split
  name: Spree Commerce Fulfillments API
  slug: spree-fulfillments-api
- description: Gift cards and gift card batches
  name: Spree Commerce Gift Cards API
  slug: spree-gift-cards-api
- description: The Line Items API from Spree Commerce — 2 operation(s) for line items.
  name: Spree Commerce Line Items API
  slug: spree-line-items-api
- description: Markets — geographic groupings of countries used for pricing, tax, and fulfillment rules
  name: Spree Commerce Markets API
  slug: spree-markets-api
- description: The Menu Items API from Spree Commerce — 3 operation(s) for menu items.
  name: Spree Commerce Menu Items API
  slug: spree-menu-items-api
- description: The Menus API from Spree Commerce — 2 operation(s) for menus.
  name: Spree Commerce Menus API
  slug: spree-menus-api
- description: Guest and customer newsletter subscriptions (double opt-in)
  name: Spree Commerce Newsletter Subscribers API
  slug: spree-newsletter-subscribers-api
- description: Option types and option values used to build product variants (e.g. Size, Color)
  name: Spree Commerce Option Types API
  slug: spree-option-types-api
- description: The Option Values API from Spree Commerce — 2 operation(s) for option values.
  name: Spree Commerce Option Values API
  slug: spree-option-values-api
- description: The Order Status API from Spree Commerce — 1 operation(s) for order status.
  name: Spree Commerce Order Status API
  slug: spree-order-status-api
- description: Orders, order items, applied gift cards, and applied store credits
  name: Spree Commerce Orders API
  slug: spree-orders-api
- description: Configured payment providers and their available types
  name: Spree Commerce Payment Methods API
  slug: spree-payment-methods-api
- description: Order payments — list, capture, void
  name: Spree Commerce Payments API
  slug: spree-payments-api
- description: Store policies (return policy, privacy policy, terms of service)
  name: Spree Commerce Policies API
  slug: spree-policies-api
- description: The Post Categories API from Spree Commerce — 2 operation(s) for post categories.
  name: Spree Commerce Post Categories API
  slug: spree-post-categories-api
- description: The Posts API from Spree Commerce — 2 operation(s) for posts.
  name: Spree Commerce Posts API
  slug: spree-posts-api
- description: Prices and price lists for currency-, market-, and customer-group-specific pricing
  name: Spree Commerce Pricing API
  slug: spree-pricing-api
- description: Products and categories
  name: Spree Commerce Product Catalog API
  slug: spree-product-catalog-api
- description: Products, taxons/categories, product custom field values, and bulk product operations
  name: Spree Commerce Products API
  slug: spree-products-api
- description: The Promotion Actions API from Spree Commerce — 2 operation(s) for promotion actions.
  name: Spree Commerce Promotion Actions API
  slug: spree-promotion-actions-api
- description: The Promotion Categories API from Spree Commerce — 2 operation(s) for promotion categories.
  name: Spree Commerce Promotion Categories API
  slug: spree-promotion-categories-api
- description: The Promotion Rules API from Spree Commerce — 2 operation(s) for promotion rules.
  name: Spree Commerce Promotion Rules API
  slug: spree-promotion-rules-api
- description: Promotions, promotion rules, promotion actions, and coupon codes
  name: Spree Commerce Promotions API
  slug: spree-promotions-api
- description: Order refunds
  name: Spree Commerce Refunds API
  slug: spree-refunds-api
- description: The Roles API from Spree Commerce — 2 operation(s) for roles.
  name: Spree Commerce Roles API
  slug: spree-roles-api
- description: Store-level settings — store profile, tags, store credit categories
  name: Spree Commerce Settings API
  slug: spree-settings-api
- description: The Shipments API from Spree Commerce — 9 operation(s) for shipments.
  name: Spree Commerce Shipments API
  slug: spree-shipments-api
- description: The Shipping Categories API from Spree Commerce — 2 operation(s) for shipping categories.
  name: Spree Commerce Shipping Categories API
  slug: spree-shipping-categories-api
- description: The Shipping Methods API from Spree Commerce — 2 operation(s) for shipping methods.
  name: Spree Commerce Shipping Methods API
  slug: spree-shipping-methods-api
- description: Admin users, roles, and invitations to the store
  name: Spree Commerce Staff API
  slug: spree-staff-api
- description: The States API from Spree Commerce — 2 operation(s) for states.
  name: Spree Commerce States API
  slug: spree-states-api
- description: The Stock Items API from Spree Commerce — 2 operation(s) for stock items.
  name: Spree Commerce Stock Items API
  slug: spree-stock-items-api
- description: Warehouses and physical fulfillment locations
  name: Spree Commerce Stock Locations API
  slug: spree-stock-locations-api
- description: The Store Credit Categories API from Spree Commerce — 2 operation(s) for store credit categories.
  name: Spree Commerce Store Credit Categories API
  slug: spree-store-credit-categories-api
- description: The Store Credit Types API from Spree Commerce — 2 operation(s) for store credit types.
  name: Spree Commerce Store Credit Types API
  slug: spree-store-credit-types-api
- description: The Store Credits API from Spree Commerce — 2 operation(s) for store credits.
  name: Spree Commerce Store Credits API
  slug: spree-store-credits-api
- description: The Stores API from Spree Commerce — 1 operation(s) for stores.
  name: Spree Commerce Stores API
  slug: spree-stores-api
- description: The Stripe API from Spree Commerce — 4 operation(s) for stripe.
  name: Spree Commerce Stripe API
  slug: spree-stripe-api
- description: The Tax Categories API from Spree Commerce — 2 operation(s) for tax categories.
  name: Spree Commerce Tax Categories API
  slug: spree-tax-categories-api
- description: The Tax Rates API from Spree Commerce — 2 operation(s) for tax rates.
  name: Spree Commerce Tax Rates API
  slug: spree-tax-rates-api
- description: The Taxonomies API from Spree Commerce — 2 operation(s) for taxonomies.
  name: Spree Commerce Taxonomies API
  slug: spree-taxonomies-api
- description: The Taxons API from Spree Commerce — 5 operation(s) for taxons.
  name: Spree Commerce Taxons API
  slug: spree-taxons-api
- description: The Users API from Spree Commerce — 2 operation(s) for users.
  name: Spree Commerce Users API
  slug: spree-users-api
- description: Product variants — the individual SKUs (size/color combinations) sold under a product
  name: Spree Commerce Variants API
  slug: spree-variants-api
- description: The Vendors API from Spree Commerce — 10 operation(s) for vendors.
  name: Spree Commerce Vendors API
  slug: spree-vendors-api
- description: The Webhook Events API from Spree Commerce — 1 operation(s) for webhook events.
  name: Spree Commerce Webhook Events API
  slug: spree-webhook-events-api
- description: The Webhook Subscribers API from Spree Commerce — 2 operation(s) for webhook subscribers.
  name: Spree Commerce Webhook Subscribers API
  slug: spree-webhook-subscribers-api
- description: Webhook endpoints and webhook delivery history
  name: Spree Commerce Webhooks API
  slug: spree-webhooks-api
- description: The Wished Items API from Spree Commerce — 2 operation(s) for wished items.
  name: Spree Commerce Wished Items API
  slug: spree-wished-items-api
- description: The Wishlists API from Spree Commerce — 9 operation(s) for wishlists.
  name: Spree Commerce Wishlists API
  slug: spree-wishlists-api
- description: The Wishlists / Wished Items API from Spree Commerce — 5 operation(s) for wishlists / wished items.
  name: Spree Commerce Wishlists / Wished Items API
  slug: spree-wishlists-wished-items-api
- description: The Zones API from Spree Commerce — 2 operation(s) for zones.
  name: Spree Commerce Zones API
  slug: spree-zones-api
artifact_total: 273
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Admin Account / Address API
  slug: open-spree-commerce-account-address-api
- collection_type: open
  name: Admin / Address Account API
  slug: open-spree-commerce-account-api
- collection_type: open
  name: Admin Account / Address Account / Credit Cards API
  slug: open-spree-commerce-account-credit-cards-api
- collection_type: open
  name: Admin Account / Address Account / Orders API
  slug: open-spree-commerce-account-orders-api
- collection_type: open
  name: Admin Account / Address Addresses API
  slug: open-spree-commerce-addresses-api
- collection_type: open
  name: Admin Account / Address Adjustments API
  slug: open-spree-commerce-adjustments-api
- collection_type: open
  name: Admin API
  slug: open-spree-commerce-admin-api
- collection_type: open
  name: Admin Account / Address Adyen API
  slug: open-spree-commerce-adyen-api
- collection_type: open
  name: Admin Account / Address Authentication API
  slug: open-spree-commerce-authentication-api
- collection_type: open
  name: Admin Account / Address Cart API
  slug: open-spree-commerce-cart-api
- collection_type: open
  name: Admin Account / Address Cart / Coupons API
  slug: open-spree-commerce-cart-coupons-api
- collection_type: open
  name: Admin Account / Address Cart / Line Items API
  slug: open-spree-commerce-cart-line-items-api
- collection_type: open
  name: Admin Account / Address Cart / Other API
  slug: open-spree-commerce-cart-other-api
- collection_type: open
  name: Admin Account / Address Carts API
  slug: open-spree-commerce-carts-api
- collection_type: open
  name: Admin Account / Address Checkout API
  slug: open-spree-commerce-checkout-api
- collection_type: open
  name: Admin Account / Address Checkout / Payments API
  slug: open-spree-commerce-checkout-payments-api
- collection_type: open
  name: Admin Account / Address Checkout / Shipments API
  slug: open-spree-commerce-checkout-shipments-api
- collection_type: open
  name: Admin Account / Address Checkout / State API
  slug: open-spree-commerce-checkout-state-api
- collection_type: open
  name: Admin Account / Address Checkout / Store Credit API
  slug: open-spree-commerce-checkout-store-credit-api
- collection_type: open
  name: Admin Account / Address Classifications API
  slug: open-spree-commerce-classifications-api
- collection_type: open
  name: Admin Account / Address CMS Pages API
  slug: open-spree-commerce-cms-pages-api
- collection_type: open
  name: Admin Account / Address CMS Sections API
  slug: open-spree-commerce-cms-sections-api
- collection_type: open
  name: Admin Account / Address Configuration API
  slug: open-spree-commerce-configuration-api
- collection_type: open
  name: Admin Account / Address Countries API
  slug: open-spree-commerce-countries-api
- collection_type: open
  name: Admin Account / Address Custom Fields API
  slug: open-spree-commerce-custom-fields-api
- collection_type: open
  name: Admin Account / Address Customers API
  slug: open-spree-commerce-customers-api
- collection_type: open
  name: Admin Account / Address Data Feeds API
  slug: open-spree-commerce-data-feeds-api
- collection_type: open
  name: Admin Account / Address Digital Assets API
  slug: open-spree-commerce-digital-assets-api
- collection_type: open
  name: Admin Account / Address Digital Downloads API
  slug: open-spree-commerce-digital-downloads-api
- collection_type: open
  name: Admin Account / Address Digital Links API
  slug: open-spree-commerce-digital-links-api
- collection_type: open
  name: Admin Account / Address Digitals API
  slug: open-spree-commerce-digitals-api
- collection_type: open
  name: Admin Account / Address Exports API
  slug: open-spree-commerce-exports-api
- collection_type: open
  name: Admin Account / Address Gift Cards API
  slug: open-spree-commerce-gift-cards-api
- collection_type: open
  name: Admin Account / Address Line Items API
  slug: open-spree-commerce-line-items-api
- collection_type: open
  name: Admin Account / Address Markets API
  slug: open-spree-commerce-markets-api
- collection_type: open
  name: Admin Account / Address Menu Items API
  slug: open-spree-commerce-menu-items-api
- collection_type: open
  name: Admin Account / Address Menus API
  slug: open-spree-commerce-menus-api
- collection_type: open
  name: Admin Account / Address Newsletter Subscribers API
  slug: open-spree-commerce-newsletter-subscribers-api
- collection_type: open
  name: Authentication
  slug: open-spree-commerce-oauth-api
- collection_type: open
  name: Admin Account / Address Option Types API
  slug: open-spree-commerce-option-types-api
- collection_type: open
  name: Admin Account / Address Option Values API
  slug: open-spree-commerce-option-values-api
- collection_type: open
  name: Admin Account / Address Order Status API
  slug: open-spree-commerce-order-status-api
- collection_type: open
  name: Admin Account / Address Orders API
  slug: open-spree-commerce-orders-api
- collection_type: open
  name: Admin Account / Address Payment Methods API
  slug: open-spree-commerce-payment-methods-api
- collection_type: open
  name: Admin Account / Address Payments API
  slug: open-spree-commerce-payments-api
- collection_type: open
  name: Platform API
  slug: open-spree-commerce-platform-api
- collection_type: open
  name: Admin Account / Address Policies API
  slug: open-spree-commerce-policies-api
- collection_type: open
  name: Admin Account / Address Post Categories API
  slug: open-spree-commerce-post-categories-api
- collection_type: open
  name: Admin Account / Address Posts API
  slug: open-spree-commerce-posts-api
- collection_type: open
  name: Admin Account / Address Product Catalog API
  slug: open-spree-commerce-product-catalog-api
- collection_type: open
  name: Admin Account / Address Products API
  slug: open-spree-commerce-products-api
- collection_type: open
  name: Admin Account / Address Promotion Actions API
  slug: open-spree-commerce-promotion-actions-api
- collection_type: open
  name: Admin Account / Address Promotion Categories API
  slug: open-spree-commerce-promotion-categories-api
- collection_type: open
  name: Admin Account / Address Promotion Rules API
  slug: open-spree-commerce-promotion-rules-api
- collection_type: open
  name: Admin Account / Address Promotions API
  slug: open-spree-commerce-promotions-api
- collection_type: open
  name: Admin Account / Address Roles API
  slug: open-spree-commerce-roles-api
- collection_type: open
  name: Admin Account / Address Shipments API
  slug: open-spree-commerce-shipments-api
- collection_type: open
  name: Admin Account / Address Shipping Categories API
  slug: open-spree-commerce-shipping-categories-api
- collection_type: open
  name: Admin Account / Address Shipping Methods API
  slug: open-spree-commerce-shipping-methods-api
- collection_type: open
  name: Admin Account / Address States API
  slug: open-spree-commerce-states-api
- collection_type: open
  name: Admin Account / Address Stock Items API
  slug: open-spree-commerce-stock-items-api
- collection_type: open
  name: Admin Account / Address Stock Locations API
  slug: open-spree-commerce-stock-locations-api
- collection_type: open
  name: Store API
  slug: open-spree-commerce-store-api
- collection_type: open
  name: Admin Account / Address Store Credit Categories API
  slug: open-spree-commerce-store-credit-categories-api
- collection_type: open
  name: Admin Account / Address Store Credit Types API
  slug: open-spree-commerce-store-credit-types-api
- collection_type: open
  name: Admin Account / Address Store Credits API
  slug: open-spree-commerce-store-credits-api
- collection_type: open
  name: Storefront API
  slug: open-spree-commerce-storefront-api
- collection_type: open
  name: Admin Account / Address Stores API
  slug: open-spree-commerce-stores-api
- collection_type: open
  name: Admin Account / Address Stripe API
  slug: open-spree-commerce-stripe-api
- collection_type: open
  name: Admin Account / Address Tax Categories API
  slug: open-spree-commerce-tax-categories-api
- collection_type: open
  name: Admin Account / Address Tax Rates API
  slug: open-spree-commerce-tax-rates-api
- collection_type: open
  name: Admin Account / Address Taxonomies API
  slug: open-spree-commerce-taxonomies-api
- collection_type: open
  name: Admin Account / Address Taxons API
  slug: open-spree-commerce-taxons-api
- collection_type: open
  name: Admin Account / Address Token API
  slug: open-spree-commerce-token-api
- collection_type: open
  name: Admin Account / Address Users API
  slug: open-spree-commerce-users-api
- collection_type: open
  name: Admin Account / Address Variants API
  slug: open-spree-commerce-variants-api
- collection_type: open
  name: Admin Account / Address Vendors API
  slug: open-spree-commerce-vendors-api
- collection_type: open
  name: Admin Account / Address Webhook Events API
  slug: open-spree-commerce-webhook-events-api
- collection_type: open
  name: Admin Account / Address Webhook Subscribers API
  slug: open-spree-commerce-webhook-subscribers-api
- collection_type: open
  name: Admin Account / Address Wished Items API
  slug: open-spree-commerce-wished-items-api
- collection_type: open
  name: Admin Account / Address Wishlists API
  slug: open-spree-commerce-wishlists-api
- collection_type: open
  name: Admin Account / Address Wishlists / Wished Items API
  slug: open-spree-commerce-wishlists-wished-items-api
- collection_type: open
  name: Admin Account / Address Zones API
  slug: open-spree-commerce-zones-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/spree-commerce-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/spree/spree/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/spree/spree/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/spree/spree/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/spree/spree/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spree-commerce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spree-commerce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spree-commerce-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://spreecommerce.org/feed/
- group: company
  title: ''
  type: Website
  url: https://spreecommerce.org/
- group: docs
  title: ''
  type: Documentation
  url: https://dev-docs.spreecommerce.org/
- group: docs
  title: ''
  type: APIReference
  url: https://dev-docs.spreecommerce.org/api-reference/introduction
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spree
- group: commercial
  title: ''
  type: Pricing
  url: https://spreecommerce.org/pricing/
- group: start
  title: ''
  type: Demo
  url: https://demo.spreecommerce.org/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spree/spree/releases
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spree-commerce/
- group: other
  title: ''
  type: Suppliers
  url: https://github.com/spree/spree_multi_vendor
- group: docs
  title: ''
  type: Documentation
  url: https://spreecommerce.org/docs/developer/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://spreecommerce.org/blog/
created: '2026-05-25'
description: Spree Commerce is an open-source headless eCommerce platform originally released in 2007 and built on Ruby on Rails. The Spree server exposes a modern Store API (v3), an Admin API (v3), a Platform API (v2) used by internal/back-office integrations, and a Storefront API (v2) based on the JSON:API spec - all described with OpenAPI 3 - plus an OAuth 2.0 token endpoint for authentication. Developer surface includes the TypeScript Store and Admin SDKs (@spree/sdk and @spree/admin-sdk), the @spree/cli for managing Spree projects, the create-spree-app scaffolder, the open-source Next.js storefront, the spree-starter application template, the spree_extension generator for building Rails extensions, the deface view-customization plugin, official payments integrations (Stripe, Adyen, PayPal), marketing integrations (Klaviyo, Google Analytics), an Avalara/AvaTax extension, the spree_multi_vendor marketplace extension, and a Webhook event system for reacting to store events.
finops:
- name: Spree Commerce Finops
  service_category: API
  slug: spree-commerce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spree-commerce.png
layout: provider
modified: '2026-07-25'
name: Spree Commerce
nav: Providers
network: true
overview: 'Spree Commerce publishes 164 APIs on the [APIs.io](https://apis.io/) network, including Account / Address API, Account API, Account / Credit Cards API, and 161 more. Tagged areas include Commerce, Headless, E-Commerce, Open-Source, and Ruby on Rails.


  Spree Commerce''s developer surface includes authentication, engineering blog, documentation, API reference, GitHub presence, pricing, release notes, and 13 more developer resources.'
plans:
- name: Spree Commerce Plans Pricing
  plan_count: 2
  slug: spree-commerce-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Spree Commerce Rate Limits
  slug: spree-commerce-rate-limits
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 60.1
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 40.0
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 78
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spree-commerce/refs/heads/main/screenshots/spree-commerce-2026-06-20T194400.png
security:
- kind: authentication
  name: Spree Commerce Authentication
  slug: spree-commerce-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Spree Commerce Domain Security
  slug: spree-commerce-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spree-commerce
tags:
- Commerce
- Headless
- E-Commerce
- Open-Source
- Ruby on Rails
- Ruby
- TypeScript
website: https://spreecommerce.org/
---
