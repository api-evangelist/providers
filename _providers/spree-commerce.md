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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 311
  human_in_the_loop: 5
  name: Spree Commerce Agentic Access
  operation_count: 524
  slug: spree-commerce-agentic-access
  summary_line: 524 operations · 311 acting · 5 human-in-the-loop
api_count: 97
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
- description: The Account / Address API from Spree Commerce — 2 operation(s) for account / address.
  name: Spree Commerce Account / Address API
  slug: spree-commerce-account-address-api
- description: The Account API from Spree Commerce — 1 operation(s) for account.
  name: Spree Commerce Account API
  slug: spree-commerce-account-api
- description: The Account / Credit Cards API from Spree Commerce — 3 operation(s) for account / credit cards.
  name: Spree Commerce Account / Credit Cards API
  slug: spree-commerce-account-credit-cards-api
- description: The Account / Orders API from Spree Commerce — 2 operation(s) for account / orders.
  name: Spree Commerce Account / Orders API
  slug: spree-commerce-account-orders-api
- description: The Addresses API from Spree Commerce — 2 operation(s) for addresses.
  name: Spree Commerce Addresses API
  slug: spree-commerce-addresses-api
- description: The Adjustments API from Spree Commerce — 2 operation(s) for adjustments.
  name: Spree Commerce Adjustments API
  slug: spree-commerce-adjustments-api
- description: The Adyen API from Spree Commerce — 3 operation(s) for adyen.
  name: Spree Commerce Adyen API
  slug: spree-commerce-adyen-api
- description: Admin user authentication
  name: Spree Commerce Authentication API
  slug: spree-commerce-authentication-api
- description: The Cart API from Spree Commerce — 1 operation(s) for cart.
  name: Spree Commerce Cart API
  slug: spree-commerce-cart-api
- description: The Cart / Coupons API from Spree Commerce — 3 operation(s) for cart / coupons.
  name: Spree Commerce Cart / Coupons API
  slug: spree-commerce-cart-coupons-api
- description: The Cart / Line Items API from Spree Commerce — 3 operation(s) for cart / line items.
  name: Spree Commerce Cart / Line Items API
  slug: spree-commerce-cart-line-items-api
- description: The Cart / Other API from Spree Commerce — 4 operation(s) for cart / other.
  name: Spree Commerce Cart / Other API
  slug: spree-commerce-cart-other-api
- description: Shopping cart management
  name: Spree Commerce Carts API
  slug: spree-commerce-carts-api
- description: The Checkout API from Spree Commerce — 2 operation(s) for checkout.
  name: Spree Commerce Checkout API
  slug: spree-commerce-checkout-api
- description: The Checkout / Payments API from Spree Commerce — 2 operation(s) for checkout / payments.
  name: Spree Commerce Checkout / Payments API
  slug: spree-commerce-checkout-payments-api
- description: The Checkout / Shipments API from Spree Commerce — 2 operation(s) for checkout / shipments.
  name: Spree Commerce Checkout / Shipments API
  slug: spree-commerce-checkout-shipments-api
- description: The Checkout / State API from Spree Commerce — 3 operation(s) for checkout / state.
  name: Spree Commerce Checkout / State API
  slug: spree-commerce-checkout-state-api
- description: The Checkout / Store Credit API from Spree Commerce — 2 operation(s) for checkout / store credit.
  name: Spree Commerce Checkout / Store Credit API
  slug: spree-commerce-checkout-store-credit-api
- description: The Classifications API from Spree Commerce — 2 operation(s) for classifications.
  name: Spree Commerce Classifications API
  slug: spree-commerce-classifications-api
- description: The CMS Pages API from Spree Commerce — 2 operation(s) for cms pages.
  name: Spree Commerce CMS Pages API
  slug: spree-commerce-cms-pages-api
- description: The CMS Sections API from Spree Commerce — 2 operation(s) for cms sections.
  name: Spree Commerce CMS Sections API
  slug: spree-commerce-cms-sections-api
- description: Store configuration — payment methods, tag autocomplete
  name: Spree Commerce Configuration API
  slug: spree-commerce-configuration-api
- description: The Countries API from Spree Commerce — 5 operation(s) for countries.
  name: Spree Commerce Countries API
  slug: spree-commerce-countries-api
- description: The Custom Fields API from Spree Commerce — 2 operation(s) for custom fields.
  name: Spree Commerce Custom Fields API
  slug: spree-commerce-custom-fields-api
- description: Customer management — profiles, addresses, store credits, credit cards
  name: Spree Commerce Customers API
  slug: spree-commerce-customers-api
- description: The Data Feeds API from Spree Commerce — 2 operation(s) for data feeds.
  name: Spree Commerce Data Feeds API
  slug: spree-commerce-data-feeds-api
- description: The Digital Assets API from Spree Commerce — 2 operation(s) for digital assets.
  name: Spree Commerce Digital Assets API
  slug: spree-commerce-digital-assets-api
- description: The Digital Downloads API from Spree Commerce — 1 operation(s) for digital downloads.
  name: Spree Commerce Digital Downloads API
  slug: spree-commerce-digital-downloads-api
- description: The Digital Links API from Spree Commerce — 3 operation(s) for digital links.
  name: Spree Commerce Digital Links API
  slug: spree-commerce-digital-links-api
- description: Digital product downloads
  name: Spree Commerce Digitals API
  slug: spree-commerce-digitals-api
- description: The Exports API from Spree Commerce — 3 operation(s) for exports.
  name: Spree Commerce Exports API
  slug: spree-commerce-exports-api
- description: The Gift Cards API from Spree Commerce — 4 operation(s) for gift cards.
  name: Spree Commerce Gift Cards API
  slug: spree-commerce-gift-cards-api
- description: The Line Items API from Spree Commerce — 2 operation(s) for line items.
  name: Spree Commerce Line Items API
  slug: spree-commerce-line-items-api
- description: Markets, countries, currencies, and locales
  name: Spree Commerce Markets API
  slug: spree-commerce-markets-api
- description: The Menu Items API from Spree Commerce — 3 operation(s) for menu items.
  name: Spree Commerce Menu Items API
  slug: spree-commerce-menu-items-api
- description: The Menus API from Spree Commerce — 2 operation(s) for menus.
  name: Spree Commerce Menus API
  slug: spree-commerce-menus-api
- description: Guest and customer newsletter subscriptions (double opt-in)
  name: Spree Commerce Newsletter Subscribers API
  slug: spree-commerce-newsletter-subscribers-api
- description: The Option Types API from Spree Commerce — 2 operation(s) for option types.
  name: Spree Commerce Option Types API
  slug: spree-commerce-option-types-api
- description: The Option Values API from Spree Commerce — 2 operation(s) for option values.
  name: Spree Commerce Option Values API
  slug: spree-commerce-option-values-api
- description: The Order Status API from Spree Commerce — 1 operation(s) for order status.
  name: Spree Commerce Order Status API
  slug: spree-commerce-order-status-api
- description: Order management — orders, items, payments, fulfillments, refunds, gift cards, store credits
  name: Spree Commerce Orders API
  slug: spree-commerce-orders-api
- description: The Payment Methods API from Spree Commerce — 2 operation(s) for payment methods.
  name: Spree Commerce Payment Methods API
  slug: spree-commerce-payment-methods-api
- description: The Payments API from Spree Commerce — 2 operation(s) for payments.
  name: Spree Commerce Payments API
  slug: spree-commerce-payments-api
- description: Store policies (return policy, privacy policy, terms of service)
  name: Spree Commerce Policies API
  slug: spree-commerce-policies-api
- description: The Post Categories API from Spree Commerce — 2 operation(s) for post categories.
  name: Spree Commerce Post Categories API
  slug: spree-commerce-post-categories-api
- description: The Posts API from Spree Commerce — 2 operation(s) for posts.
  name: Spree Commerce Posts API
  slug: spree-commerce-posts-api
- description: Products, variants, and option types
  name: Spree Commerce Product Catalog API
  slug: spree-commerce-product-catalog-api
- description: The Products API from Spree Commerce — 6 operation(s) for products.
  name: Spree Commerce Products API
  slug: spree-commerce-products-api
- description: The Promotion Actions API from Spree Commerce — 2 operation(s) for promotion actions.
  name: Spree Commerce Promotion Actions API
  slug: spree-commerce-promotion-actions-api
- description: The Promotion Categories API from Spree Commerce — 2 operation(s) for promotion categories.
  name: Spree Commerce Promotion Categories API
  slug: spree-commerce-promotion-categories-api
- description: The Promotion Rules API from Spree Commerce — 2 operation(s) for promotion rules.
  name: Spree Commerce Promotion Rules API
  slug: spree-commerce-promotion-rules-api
- description: The Promotions API from Spree Commerce — 11 operation(s) for promotions.
  name: Spree Commerce Promotions API
  slug: spree-commerce-promotions-api
- description: The Roles API from Spree Commerce — 2 operation(s) for roles.
  name: Spree Commerce Roles API
  slug: spree-commerce-roles-api
- description: The Shipments API from Spree Commerce — 9 operation(s) for shipments.
  name: Spree Commerce Shipments API
  slug: spree-commerce-shipments-api
- description: The Shipping Categories API from Spree Commerce — 2 operation(s) for shipping categories.
  name: Spree Commerce Shipping Categories API
  slug: spree-commerce-shipping-categories-api
- description: The Shipping Methods API from Spree Commerce — 2 operation(s) for shipping methods.
  name: Spree Commerce Shipping Methods API
  slug: spree-commerce-shipping-methods-api
- description: The States API from Spree Commerce — 2 operation(s) for states.
  name: Spree Commerce States API
  slug: spree-commerce-states-api
- description: The Stock Items API from Spree Commerce — 2 operation(s) for stock items.
  name: Spree Commerce Stock Items API
  slug: spree-commerce-stock-items-api
- description: The Stock Locations API from Spree Commerce — 2 operation(s) for stock locations.
  name: Spree Commerce Stock Locations API
  slug: spree-commerce-stock-locations-api
- description: The Store Credit Categories API from Spree Commerce — 2 operation(s) for store credit categories.
  name: Spree Commerce Store Credit Categories API
  slug: spree-commerce-store-credit-categories-api
- description: The Store Credit Types API from Spree Commerce — 2 operation(s) for store credit types.
  name: Spree Commerce Store Credit Types API
  slug: spree-commerce-store-credit-types-api
- description: The Store Credits API from Spree Commerce — 2 operation(s) for store credits.
  name: Spree Commerce Store Credits API
  slug: spree-commerce-store-credits-api
- description: The Stores API from Spree Commerce — 1 operation(s) for stores.
  name: Spree Commerce Stores API
  slug: spree-commerce-stores-api
- description: The Stripe API from Spree Commerce — 4 operation(s) for stripe.
  name: Spree Commerce Stripe API
  slug: spree-commerce-stripe-api
- description: The Tax Categories API from Spree Commerce — 2 operation(s) for tax categories.
  name: Spree Commerce Tax Categories API
  slug: spree-commerce-tax-categories-api
- description: The Tax Rates API from Spree Commerce — 2 operation(s) for tax rates.
  name: Spree Commerce Tax Rates API
  slug: spree-commerce-tax-rates-api
- description: The Taxonomies API from Spree Commerce — 2 operation(s) for taxonomies.
  name: Spree Commerce Taxonomies API
  slug: spree-commerce-taxonomies-api
- description: The Taxons API from Spree Commerce — 5 operation(s) for taxons.
  name: Spree Commerce Taxons API
  slug: spree-commerce-taxons-api
- description: The Token API from Spree Commerce — 1 operation(s) for token.
  name: Spree Commerce Token API
  slug: spree-commerce-token-api
- description: The Users API from Spree Commerce — 2 operation(s) for users.
  name: Spree Commerce Users API
  slug: spree-commerce-users-api
- description: The Variants API from Spree Commerce — 3 operation(s) for variants.
  name: Spree Commerce Variants API
  slug: spree-commerce-variants-api
- description: The Vendors API from Spree Commerce — 10 operation(s) for vendors.
  name: Spree Commerce Vendors API
  slug: spree-commerce-vendors-api
- description: The Webhook Events API from Spree Commerce — 1 operation(s) for webhook events.
  name: Spree Commerce Webhook Events API
  slug: spree-commerce-webhook-events-api
- description: The Webhook Subscribers API from Spree Commerce — 2 operation(s) for webhook subscribers.
  name: Spree Commerce Webhook Subscribers API
  slug: spree-commerce-webhook-subscribers-api
- description: The Wished Items API from Spree Commerce — 2 operation(s) for wished items.
  name: Spree Commerce Wished Items API
  slug: spree-commerce-wished-items-api
- description: The Wishlists API from Spree Commerce — 9 operation(s) for wishlists.
  name: Spree Commerce Wishlists API
  slug: spree-commerce-wishlists-api
- description: The Wishlists / Wished Items API from Spree Commerce — 5 operation(s) for wishlists / wished items.
  name: Spree Commerce Wishlists / Wished Items API
  slug: spree-commerce-wishlists-wished-items-api
- description: The Zones API from Spree Commerce — 2 operation(s) for zones.
  name: Spree Commerce Zones API
  slug: spree-commerce-zones-api
artifact_total: 108
collections:
- collection_type: open
  name: Admin API
  slug: open-spree-commerce-admin-api
- collection_type: open
  name: Authentication
  slug: open-spree-commerce-oauth-api
- collection_type: open
  name: Platform API
  slug: open-spree-commerce-platform-api
- collection_type: open
  name: Store API
  slug: open-spree-commerce-store-api
- collection_type: open
  name: Storefront API
  slug: open-spree-commerce-storefront-api
common:
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
overview: 'Spree Commerce publishes 78 APIs on the [APIs.io](https://apis.io/) network, including Account / Address API, Account API, Account / Credit Cards API, and 75 more. Tagged areas include Commerce, Headless, eCommerce, Open Source, and Ruby on Rails.


  Spree Commerce''s developer surface includes authentication, engineering blog, documentation, API reference, GitHub presence, pricing, release notes, and 6 more developer resources.'
plans:
- name: Spree Commerce Plans Pricing
  plan_count: 2
  slug: spree-commerce-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 2
  name: Spree Commerce Rate Limits
  slug: spree-commerce-rate-limits
score:
  band: thin
  composite: 40.0
  delta: -3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.5
    developer_ergonomics: 28.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 78
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- eCommerce
- Open Source
- Ruby on Rails
- Ruby
- TypeScript
website: https://spreecommerce.org/
---
