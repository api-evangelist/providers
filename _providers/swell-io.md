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
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 71
  human_in_the_loop: 1
  name: Swell Io Agentic Access
  operation_count: 135
  slug: swell-io-agentic-access
  summary_line: 135 operations · 71 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'Experimental (alpha) GraphQL endpoint that exposes a curated subset of the storefront commerce model — products, attributes, categories, accounts, sessions, carts, orders, payments, payment settings, '
  name: Swell GraphQL API
  slug: swell-graphql-api
- description: Event-driven HTTP callbacks for cart, order, subscription, payment, account, and product lifecycle events. Configurable via the dashboard (Developer → Webhooks) or programmatically through the Backend
  name: Swell Webhooks
  slug: swell-webhooks-api
- description: Swell Apps extend the platform with custom data models (added fields or new entities), events (triggering functions, webhooks, and notifications), edge functions deployed to 200+ locations with no col
  name: Swell Apps Platform
  slug: swell-apps-platform
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Saved shipping/billing addresses on an account.
  name: Swell Account Addresses API
  slug: swell-io-account-addresses-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Authenticated customer account operations.
  name: Swell Account API
  slug: swell-io-account-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Saved payment cards on an account.
  name: Swell Account Cards API
  slug: swell-io-account-cards-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Store credit balances and transactions per account.
  name: Swell Account Credits API
  slug: swell-io-account-credits-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Login, logout, and session recovery.
  name: Swell Account Session API
  slug: swell-io-account-session-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Customer accounts including billing/shipping, saved cards, and history.
  name: Swell Accounts API
  slug: swell-io-accounts-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Product attributes used for filtering and faceted search.
  name: Swell Attributes API
  slug: swell-io-attributes-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Session-scoped shopping cart for the current visitor.
  name: Swell Cart API
  slug: swell-io-cart-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Pending purchase requests that can be converted into orders.
  name: Swell Carts API
  slug: swell-io-carts-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Category tree and product taxonomy.
  name: Swell Categories API
  slug: swell-io-categories-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Cart conversion and order placement.
  name: Swell Checkout API
  slug: swell-io-checkout-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Pages, custom data models, and stored records.
  name: Swell Content API
  slug: swell-io-content-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Coupon definitions with codes, redemptions, and discount rules.
  name: Swell Coupons API
  slug: swell-io-coupons-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Event records emitted by the platform.
  name: Swell Events API
  slug: swell-io-events-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Stored files (images, attachments) served via Swell CDN.
  name: Swell Files API
  slug: swell-io-files-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Gift cards, debit transactions, and gift card products.
  name: Swell Gift Cards API
  slug: swell-io-gift-cards-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Invoices generated for subscription billing cycles and B2B orders.
  name: Swell Invoices API
  slug: swell-io-invoices-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Customer orders, line items, financial totals, and lifecycle.
  name: Swell Orders API
  slug: swell-io-orders-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Payment transactions, refunds, and gateway settlement.
  name: Swell Payments API
  slug: swell-io-payments-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Product catalog including variants, options, bundles, gift cards, and subscription products.
  name: Swell Products API
  slug: swell-io-products-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Automatic promotion rules applied at cart and checkout.
  name: Swell Promotions API
  slug: swell-io-promotions-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Shareable purchase links that prefill a cart.
  name: Swell Purchase Links API
  slug: swell-io-purchase-links-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Refund records linked to a payment.
  name: Swell Refunds API
  slug: swell-io-refunds-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Customer return merchandise authorizations.
  name: Swell Returns API
  slug: swell-io-returns-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Fulfillment shipments, tracking, and split fulfillment.
  name: Swell Shipments API
  slug: swell-io-shipments-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Stock levels and stock adjustments across locations.
  name: Swell Stock API
  slug: swell-io-stock-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Public store settings, currencies, payment settings, and menus.
  name: Swell Store API
  slug: swell-io-store-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Plan templates that define billing schedule and price for recurring products.
  name: Swell Subscription Plans API
  slug: swell-io-subscription-plans-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Recurring billing subscriptions and plans.
  name: Swell Subscriptions API
  slug: swell-io-subscriptions-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Variant-level inventory and pricing under a parent product.
  name: Swell Variants API
  slug: swell-io-variants-api
- baseURL: https://api.swell.store
  baseurl_source: declared
  description: Webhook subscriptions for receiving event callbacks.
  name: Swell Webhooks API
  slug: swell-io-webhooks-api
arazzos:
- description: Create a backend cart with items and apply a coupon code to it.
  name: Swell Create Cart and Apply Coupon
  slug: swell-io-apply-coupon-to-cart-workflow
- description: Create a cart, populate its items, then convert it into an order.
  name: Swell Build Cart and Convert to Order
  slug: swell-io-build-cart-convert-order-workflow
- description: Locate an account's active subscription and cancel it, branching when none exists.
  name: Swell Find and Cancel Active Subscription
  slug: swell-io-cancel-subscription-workflow
- description: Record a payment against an order, then issue a refund against that payment.
  name: Swell Capture and Refund Payment
  slug: swell-io-capture-refund-payment-workflow
- description: Create a category and then create a product assigned to that category.
  name: Swell Create Category and Product
  slug: swell-io-categorize-product-workflow
- description: Create a product in the catalog and immediately retrieve it to confirm it was stored.
  name: Swell Create and Verify Product
  slug: swell-io-create-product-workflow
- description: Create a recurring subscription for an account and product, then read it back.
  name: Swell Create and Verify Subscription
  slug: swell-io-create-subscription-workflow
- description: Look up a customer by email and reuse it or create it, then place an order.
  name: Swell Find-or-Create Customer and Order
  slug: swell-io-find-or-create-customer-order-workflow
- description: Create a customer account and immediately place an order for that account.
  name: Swell Onboard Customer and Place Order
  slug: swell-io-onboard-customer-order-workflow
- description: Validate a coupon code, then apply it to the session cart only when it is valid.
  name: Swell Storefront Validate and Apply Coupon
  slug: swell-io-storefront-apply-coupon-workflow
- description: Look up a product, add it to the session cart, then submit the cart as an order.
  name: Swell Storefront Add Item and Submit Order
  slug: swell-io-storefront-checkout-workflow
- description: Create a storefront customer account and immediately authenticate the session.
  name: Swell Storefront Register and Log In
  slug: swell-io-storefront-register-login-workflow
- description: Read the session cart, then update the quantity of one of its line items.
  name: Swell Storefront Adjust Cart Item Quantity
  slug: swell-io-storefront-update-cart-item-workflow
artifact_total: 157
collections:
- collection_type: postman
  name: Swell Backend API
  slug: postman-swell-backend-api
- collection_type: postman
  name: Swell Frontend API
  slug: postman-swell-frontend-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swell Backend API
  slug: open-swell-backend-api
- collection_type: open
  name: Swell Frontend API
  slug: open-swell-frontend-api
- collection_type: open
  name: Swell Backend Account Addresses API
  slug: open-swell-io-account-addresses-api
- collection_type: open
  name: Swell Backend Addresses Account API
  slug: open-swell-io-account-api
- collection_type: open
  name: Swell Backend Account Addresses Account Cards API
  slug: open-swell-io-account-cards-api
- collection_type: open
  name: Swell Backend Account Addresses Account Credits API
  slug: open-swell-io-account-credits-api
- collection_type: open
  name: Swell Backend Account Addresses Account Session API
  slug: open-swell-io-account-session-api
- collection_type: open
  name: Swell Backend Account Addresses Accounts API
  slug: open-swell-io-accounts-api
- collection_type: open
  name: Swell Backend Account Addresses Attributes API
  slug: open-swell-io-attributes-api
- collection_type: open
  name: Swell Backend Account Addresses Cart API
  slug: open-swell-io-cart-api
- collection_type: open
  name: Swell Backend Account Addresses Carts API
  slug: open-swell-io-carts-api
- collection_type: open
  name: Swell Backend Account Addresses Categories API
  slug: open-swell-io-categories-api
- collection_type: open
  name: Swell Backend Account Addresses Checkout API
  slug: open-swell-io-checkout-api
- collection_type: open
  name: Swell Backend Account Addresses Content API
  slug: open-swell-io-content-api
- collection_type: open
  name: Swell Backend Account Addresses Coupons API
  slug: open-swell-io-coupons-api
- collection_type: open
  name: Swell Backend Account Addresses Events API
  slug: open-swell-io-events-api
- collection_type: open
  name: Swell Backend Account Addresses Files API
  slug: open-swell-io-files-api
- collection_type: open
  name: Swell Backend Account Addresses Gift Cards API
  slug: open-swell-io-gift-cards-api
- collection_type: open
  name: Swell Backend Account Addresses Invoices API
  slug: open-swell-io-invoices-api
- collection_type: open
  name: Swell Backend Account Addresses Orders API
  slug: open-swell-io-orders-api
- collection_type: open
  name: Swell Backend Account Addresses Payments API
  slug: open-swell-io-payments-api
- collection_type: open
  name: Swell Backend Account Addresses Products API
  slug: open-swell-io-products-api
- collection_type: open
  name: Swell Backend Account Addresses Promotions API
  slug: open-swell-io-promotions-api
- collection_type: open
  name: Swell Backend Account Addresses Purchase Links API
  slug: open-swell-io-purchase-links-api
- collection_type: open
  name: Swell Backend Account Addresses Refunds API
  slug: open-swell-io-refunds-api
- collection_type: open
  name: Swell Backend Account Addresses Returns API
  slug: open-swell-io-returns-api
- collection_type: open
  name: Swell Backend Account Addresses Shipments API
  slug: open-swell-io-shipments-api
- collection_type: open
  name: Swell Backend Account Addresses Stock API
  slug: open-swell-io-stock-api
- collection_type: open
  name: Swell Backend Account Addresses Store API
  slug: open-swell-io-store-api
- collection_type: open
  name: Swell Backend Account Addresses Subscription Plans API
  slug: open-swell-io-subscription-plans-api
- collection_type: open
  name: Swell Backend Account Addresses Subscriptions API
  slug: open-swell-io-subscriptions-api
- collection_type: open
  name: Swell Backend Account Addresses Variants API
  slug: open-swell-io-variants-api
- collection_type: open
  name: Swell Backend Account Addresses Webhooks API
  slug: open-swell-io-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swell-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swell-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swell-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/swell/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-apply-coupon-to-cart-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-build-cart-convert-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-cancel-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-capture-refund-payment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-categorize-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-create-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-create-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-find-or-create-customer-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-onboard-customer-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-storefront-apply-coupon-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-storefront-checkout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-storefront-register-login-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/swell-io-storefront-update-cart-item-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.swell.is/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.swell.is/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.swell.is
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.swell.is/guides/quickstart-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.swell.is/guides/core-concepts/platform-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.swell.is/pricing
- group: start
  title: ''
  type: Signup
  url: https://swell.store/signup
- group: start
  title: ''
  type: Login
  url: https://swell.store/admin/login
- group: start
  title: ''
  type: Console
  url: https://swell.store/admin
- group: operate
  title: ''
  type: StatusPage
  url: https://status.swell.store/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.swell.is/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.swell.is/blog
- group: operate
  title: ''
  type: Support
  url: https://www.swell.is/help
- group: operate
  title: ''
  type: Contact
  url: https://www.swell.is/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swell.is/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swell.is/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swellstores
- group: operate
  title: ''
  type: Forums
  url: https://github.com/orgs/swellstores/discussions
- group: other
  title: ''
  type: X
  url: https://x.com/swellcommerce
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swellcommerce/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/swellstores/swell-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/swellstores/swell-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/swellstores/swell-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/swellstores/swellpy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/swellstores/apps-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/swellstores/app-types
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/horizon
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/origin-theme
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/verswell-commerce
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/nextjs-commerce
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/nextjs-builder
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/storefront-react-ai-template
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/swell-claude-plugins
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/skills
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/easyblocks
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/proxima-app
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/contentful-app
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/honest-reviews-app
- group: other
  title: ''
  type: Resources
  url: https://github.com/swellstores/community
- group: design
  title: ''
  type: SpectralRules
  url: rules/swell-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/swell-io-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/swell-io-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/swell-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swell-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swell-io-finops.yml
created: '2026-05-25'
description: Swell is a customizable, API-first headless commerce platform powering modern B2C, B2B, subscription, and marketplace experiences. It exposes a server-side Backend API for managing the full commerce data model (products, variants, carts, orders, payments, refunds, shipments, returns, subscriptions, accounts, invoices, coupons, promotions, gift cards, content, files, events, webhooks) plus a public-key client-side Frontend API for storefronts and an experimental GraphQL endpoint. The platform ships official Node and PHP libraries, a universal JavaScript SDK (Swell.js), headless storefront starters for Next.js (Horizon, verswell-commerce, nextjs-commerce) and Nuxt (Origin), a Swell Apps platform with CLI and Apps SDK for extending the data and logic layers via custom data models, events, notifications, webhooks, and edge functions running in 200+ locations, plus AI coding-agent skills and Claude Code plugins.
examples:
- key_count: 2
  name: Swell Account Create Example
  slug: swell-account-create-example
- key_count: 2
  name: Swell Cart Add Item Example
  slug: swell-cart-add-item-example
- key_count: 2
  name: Swell Order Create Example
  slug: swell-order-create-example
- key_count: 2
  name: Swell Product Create Example
  slug: swell-product-create-example
- key_count: 2
  name: Swell Subscription Create Example
  slug: swell-subscription-create-example
- key_count: 5
  name: Swell Webhook Event Example
  slug: swell-webhook-event-example
features:
- description: Every commerce primitive — products, carts, orders, subscriptions — is exposed as a REST resource with full CRUD and rich querying.
  name: Customizable, API-first core
- description: Build any storefront — Next.js, Nuxt, Astro, mobile, native — against the public-key Frontend API and Swell.js SDK.
  name: Headless storefront
- description: First-class recurring billing with plans, trials, intervals, billing limits, and dunning baked into products and orders.
  name: Native subscriptions
- description: Account groups, volume pricing, invoicing, and price lists for B2B and wholesale alongside D2C flows.
  name: B2B and wholesale
- description: Multi-vendor selling with split fulfillment, vendor accounts, and per-vendor reporting.
  name: Marketplaces
- description: Built-in internationalization for global stores including priced currencies on higher plans.
  name: 230 currencies, 170 languages
- description: Extend the data model, events, notifications, and admin UI via the Swell Apps platform; functions run in 200+ locations with no cold start.
  name: Apps platform with edge functions
- description: Official Node and PHP libraries use a custom protocol on port 8443 for improved performance and caching versus plain HTTPS.
  name: Custom wire protocol
- description: Powerful `where` filters with comparison, logical, and array operators, plus `expand`, `include`, `sort`, `search`, and field projection.
  name: MongoDB-style querying
- description: Reliable event delivery with documented retry schedule, auto-disable, and a published source-IP allowlist for inbound verification.
  name: Webhooks with retries and IP allowlist
- description: Official Claude Code plugins and AI coding-agent skills for Swell-aware development workflows.
  name: AI coding-agent skills
finops:
- name: Swell Io Finops
  service_category: ''
  slug: swell-io-finops
graphqls:
- description: 'Experimental (alpha) GraphQL endpoint that exposes a curated subset of the storefront commerce model — products, attributes, categories, accounts, sessions, carts, orders, payments, payment settings, '
  name: Swell GraphQL API
  slug: swell-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swell-io.png
integrations:
- description: Default card processing and tokenization for most Swell stores.
  name: Stripe
- description: PayPal Express, billing agreements, and subscription processing.
  name: PayPal
- description: Multi-currency card processing.
  name: Braintree
- description: Card processing gateway.
  name: Authorize.net
- description: Fast, account-based checkout via Amazon.
  name: Amazon Pay
- description: Mobile wallet payments.
  name: Apple Pay
- description: Digital wallet payments.
  name: Google Pay
- description: Buy-now-pay-later installments.
  name: Klarna
- description: Buy-now-pay-later financing.
  name: Affirm
- description: Prepaid voucher payments.
  name: Paysafecard
- description: Payment service provider integration.
  name: QuickPay
- description: Omnichannel gift card and loyalty programs.
  name: 99Minds.io
- description: Email, SMS, mobile push, and web marketing automation.
  name: Klaviyo
- description: Email marketing and automation.
  name: Mailchimp
- description: Email and SMS marketing platform.
  name: Omnisend
- description: Subscription retention and dunning.
  name: Churn Buster
- description: Offline marketing campaign attribution.
  name: Oppizi
- description: Hosted product search and discovery.
  name: Algolia
- description: Sales-tax calculation and filing.
  name: Avalara
- description: Headless CMS via the official Swell Contentful app.
  name: Contentful
- description: Visual page-building CMS.
  name: Builder.io
- description: Frontend deployment and edge hosting for Swell storefronts.
  name: Vercel
- description: Official Claude Code plugins and AI coding-agent skills for Swell development workflows.
  name: Anthropic Claude
json_schemas:
- name: Swell Account
  property_count: 21
  slug: swell-account
- name: Swell Cart
  property_count: 15
  slug: swell-cart
- name: Swell Order
  property_count: 25
  slug: swell-order
- name: Swell Payment
  property_count: 13
  slug: swell-payment
- name: Swell Product
  property_count: 33
  slug: swell-product
- name: Swell Subscription
  property_count: 16
  slug: swell-subscription
- name: Swell Webhook Subscription
  property_count: 7
  slug: swell-webhook
json_structures:
- name: Swell Account Structure
  property_count: 13
  slug: swell-account-structure
- name: Swell Order Structure
  property_count: 19
  slug: swell-order-structure
- name: Swell Product Structure
  property_count: 26
  slug: swell-product-structure
- name: Swell Subscription Structure
  property_count: 13
  slug: swell-subscription-structure
jsonld:
- class_count: 57
  name: Swell Io Context
  property_count: 0
  slug: swell-io-context
layout: provider
modified: '2026-05-25'
name: Swell
nav: Providers
network: true
overview: 'Swell publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Account Addresses API, Account API, Account Cards API, and 28 more. Tagged areas include Commerce, Headless Commerce, API-First, B2C, and B2B.


  The Swell catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Swell''s developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, developer console, changelog, and 55 more developer resources.'
plans:
- name: Swell Io Plans Pricing
  plan_count: 5
  slug: swell-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Swell Io Rate Limits
  slug: swell-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Swell API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: swell-io-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Swell API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: swell-rules
score:
  band: exemplar
  composite: 68.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 28.8
    contract_quality: 67.9
    developer_ergonomics: 85.7
    discoverability: 53.7
    governance: 28.8
    operational_transparency: 57.9
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swell-io/refs/heads/main/screenshots/swell-io-2026-06-20T194803.png
security:
- kind: authentication
  name: Swell Io Authentication
  slug: swell-io-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Swell Io Domain Security
  slug: swell-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swell-io
solutions:
- description: Headless storefronts for direct-to-consumer brands.
  name: D2C Commerce
- description: Wholesale catalogs, account groups, invoicing, and net-terms billing.
  name: B2B Commerce
- description: Native recurring billing with flexible plans, trials, and limits.
  name: Subscriptions
- description: Multi-vendor selling with split fulfillment and per-vendor reporting.
  name: Marketplaces
- description: Serve web, native, in-store, and agent surfaces from a single commerce backend.
  name: Omnichannel
- description: Custom-priced plans for merchants exceeding $10M annual sales with negotiated SLAs.
  name: Enterprise
tags:
- Commerce
- Headless Commerce
- API-First
- B2C
- B2B
- Subscription
- Marketplaces
- Wholesale
- Storefront
- Checkout
- Payments
- Cart
- Order
- Catalog
- Internationalization
use_cases:
- description: Power D2C storefronts with full control over product, cart, checkout, and payment UX.
  name: Direct-to-consumer brands
- description: Box-of-the-month, SaaS-style, replenishment, and membership models with native subscription billing.
  name: Subscription commerce
- description: Account-group pricing, invoicing, net terms, and bulk ordering for wholesale channels.
  name: B2B and wholesale
- description: Operate marketplaces with vendor onboarding, split fulfillment, and per-vendor payouts.
  name: Multi-vendor marketplaces
- description: Serve web, native mobile, in-store, and AI-agent surfaces from a single commerce backend.
  name: Headless omnichannel
- description: Back conversational commerce agents and AI shopping assistants with a clean, query-rich API.
  name: AI-driven commerce
- description: Combine Swell with best-of-breed CMS, search, payments, ERP, and analytics for enterprise stacks.
  name: Composable enterprise commerce
website: https://www.swell.is/
---
