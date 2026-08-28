---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Salla Agentic Access
  operation_count: 69
  slug: salla-agentic-access
  summary_line: 69 operations · 30 acting
api_count: 18
apis:
- description: Server-to-server event delivery covering order, product, customer, shipping, shipment, store branch, category, brand, abandoned cart, coupon, invoice, special offer, and review lifecycle events. Paylo
  name: Salla Webhooks
  slug: salla-webhooks
- description: JavaScript SDK and Twig-based theme engine for the storefront. Provides helper methods and REST proxies that let merchant themes and embedded components communicate with the Salla backend, plus a libr
  name: Salla Twilight SDK
  slug: twilight-sdk-api
- description: The Branches API from Salla — 2 operation(s) for branches.
  name: Salla Branches API
  slug: salla-branches-api
- description: The Brands API from Salla — 2 operation(s) for brands.
  name: Salla Brands API
  slug: salla-brands-api
- description: The Carts API from Salla — 1 operation(s) for carts.
  name: Salla Carts API
  slug: salla-carts-api
- description: The Categories API from Salla — 2 operation(s) for categories.
  name: Salla Categories API
  slug: salla-categories-api
- description: The Coupons API from Salla — 1 operation(s) for coupons.
  name: Salla Coupons API
  slug: salla-coupons-api
- description: The Customers API from Salla — 2 operation(s) for customers.
  name: Salla Customers API
  slug: salla-customers-api
- description: The Financial API from Salla — 2 operation(s) for financial.
  name: Salla Financial API
  slug: salla-financial-api
- description: The Localization API from Salla — 4 operation(s) for localization.
  name: Salla Localization API
  slug: salla-localization-api
- description: The OAuth API from Salla — 3 operation(s) for oauth.
  name: Salla OAuth API
  slug: salla-oauth-api
- description: The Orders API from Salla — 6 operation(s) for orders.
  name: Salla Orders API
  slug: salla-orders-api
- description: The Products API from Salla — 5 operation(s) for products.
  name: Salla Products API
  slug: salla-products-api
- description: The Shipments API from Salla — 4 operation(s) for shipments.
  name: Salla Shipments API
  slug: salla-shipments-api
- description: The Shipping API from Salla — 6 operation(s) for shipping.
  name: Salla Shipping API
  slug: salla-shipping-api
- description: The Store API from Salla — 1 operation(s) for store.
  name: Salla Store API
  slug: salla-store-api
- description: The Webhooks API from Salla — 3 operation(s) for webhooks.
  name: Salla Webhooks API
  slug: salla-webhooks-api
- description: The Zones API from Salla — 2 operation(s) for zones.
  name: Salla Zones API
  slug: salla-zones-api
arazzos:
- description: Find abandoned carts, look up the shopper, and issue a recovery coupon.
  name: Salla Abandoned Cart Recovery
  slug: salla-abandoned-cart-recovery-workflow
- description: Create a brand and category, then create a product assigned to both.
  name: Salla Catalog Taxonomy Setup
  slug: salla-catalog-taxonomy-setup-workflow
- description: Find a customer in a page of results and update them, otherwise create a new customer.
  name: Salla Upsert Customer
  slug: salla-customer-upsert-workflow
- description: Exchange an authorization code for an access token and confirm the merchant identity.
  name: Salla OAuth Token Exchange
  slug: salla-oauth-token-exchange-workflow
- description: Read an order, create its shipment, and advance the order status.
  name: Salla Order Fulfillment
  slug: salla-order-fulfillment-workflow
- description: List orders by status, then pull the full detail, history, and invoices for one.
  name: Salla Monitor and Audit Orders
  slug: salla-order-monitor-workflow
- description: Create a product, read it back, and confirm its generated SKUs.
  name: Salla Create and Verify Product
  slug: salla-product-create-verify-workflow
- description: Find a product by keyword and update it if it exists, otherwise create it.
  name: Salla Upsert Product by SKU
  slug: salla-product-upsert-workflow
- description: Resolve a courier, create a shipment, read it back, and branch on whether to cancel.
  name: Salla Shipment Lifecycle
  slug: salla-shipment-lifecycle-workflow
- description: Register a shipping company, create a delivery zone for it, and read the zone back.
  name: Salla Shipping Zone Setup
  slug: salla-shipping-zone-setup-workflow
- description: Inspect existing webhook subscriptions, subscribe to an event, and confirm registration.
  name: Salla Webhook Subscription Setup
  slug: salla-webhook-subscription-workflow
artifact_total: 97
collections:
- collection_type: postman
  name: Salla Apps API
  slug: postman-salla-apps-api
- collection_type: postman
  name: Salla Shipping and Fulfillment API
  slug: postman-salla-shipping-fulfillment-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salla Apps API
  slug: open-salla-apps-api
- collection_type: open
  name: Salla Apps Branches API
  slug: open-salla-branches-api
- collection_type: open
  name: Salla Apps Branches Brands API
  slug: open-salla-brands-api
- collection_type: open
  name: Salla Apps Branches Carts API
  slug: open-salla-carts-api
- collection_type: open
  name: Salla Apps Branches Categories API
  slug: open-salla-categories-api
- collection_type: open
  name: Salla Apps Branches Coupons API
  slug: open-salla-coupons-api
- collection_type: open
  name: Salla Apps Branches Customers API
  slug: open-salla-customers-api
- collection_type: open
  name: Salla Apps Branches Financial API
  slug: open-salla-financial-api
- collection_type: open
  name: Salla Apps Branches Localization API
  slug: open-salla-localization-api
- collection_type: open
  name: Salla Merchant API
  slug: open-salla-merchant-api
- collection_type: open
  name: Salla Apps Branches OAuth API
  slug: open-salla-oauth-api
- collection_type: open
  name: Salla Apps Branches Orders API
  slug: open-salla-orders-api
- collection_type: open
  name: Salla Apps Branches Products API
  slug: open-salla-products-api
- collection_type: open
  name: Salla Apps Branches Shipments API
  slug: open-salla-shipments-api
- collection_type: open
  name: Salla Apps Branches Shipping API
  slug: open-salla-shipping-api
- collection_type: open
  name: Salla Shipping and Fulfillment API
  slug: open-salla-shipping-fulfillment-api
- collection_type: open
  name: Salla Apps Branches Store API
  slug: open-salla-store-api
- collection_type: open
  name: Salla Apps Branches Webhooks API
  slug: open-salla-webhooks-api
- collection_type: open
  name: Salla Webhooks
  slug: open-salla-webhooks-asyncapi
- collection_type: open
  name: Salla Apps Branches Zones API
  slug: open-salla-zones-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salla-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salla-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salla/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-abandoned-cart-recovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-catalog-taxonomy-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-customer-upsert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-oauth-token-exchange-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-order-fulfillment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-order-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-product-create-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-product-upsert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-shipment-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-shipping-zone-setup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salla-webhook-subscription-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://salla.com
- group: docs
  title: ''
  type: Documentation
  url: https://salla.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.salla.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.salla.dev/421117m0
- group: start
  title: ''
  type: Signup
  url: https://salla.partners/login
- group: start
  title: ''
  type: Console
  url: https://salla.partners
- group: commercial
  title: ''
  type: Pricing
  url: https://salla.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://salla.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://salla.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://salla.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salla.sa/
- group: operate
  title: ''
  type: Support
  url: mailto:support@salla.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.salla.dev/421127m0
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SallaApp
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/salla-app/salla-e-commerce-platform/overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/salla-app/salla-e-commerce-platform/collection/a2rh372/merchant-apis-v2-6-7
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@sallaapp
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sallaApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salla-app
- group: build
  title: ''
  type: CLI
  url: https://github.com/SallaApp/Salla-CLI
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SallaApp/laravel-starter-kit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SallaApp/express-starter-kit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SallaApp/oauth2-merchant
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SallaApp/passport-strategy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SallaApp/webhook-actions-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SallaApp/ZATCA
- group: build
  title: ''
  type: Tools
  url: https://github.com/SallaApp/theme-raed
- group: build
  title: ''
  type: Tools
  url: https://github.com/SallaApp/twilight-vscode-extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/SallaApp/embedded-sdk-playground
- group: build
  title: ''
  type: Tools
  url: https://github.com/SallaApp/store-events-tracker-starter-kit
- group: operate
  title: ''
  type: Forums
  url: https://t.me/sallaDevelopers
- group: design
  title: ''
  type: SpectralRules
  url: rules/salla-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salla-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/salla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salla-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/salla-finops.yml
created: '2026-05-24'
description: Salla is a Saudi Arabia-based e-commerce platform — often called the Shopify of the Middle East — that lets merchants launch, operate, and grow Arabic-first online stores without code. Founded in 2016 in Makkah by Nawaf Hariri and Salman Butt, Salla now powers more than 80,000 active stores. The platform exposes a Merchant REST API (https://api.salla.dev/admin/v2), an OAuth 2.0 Partners authorization service, signed webhooks for the full storefront lifecycle, a Shipping and Fulfillment app contract, the Twilight theme engine and JavaScript SDK, the Salla CLI, and official starter kits for PHP/Laravel and Node.js/Express. Backed by Sanabil (PIF), STV, Investcorp, Vision Ventures, and Raed Ventures, Salla raised a $130M pre-IPO round in 2024.
examples:
- key_count: 3
  name: Salla Create Order Example
  slug: salla-create-order-example
- key_count: 4
  name: Salla List Products Example
  slug: salla-list-products-example
features:
- description: Storefront builder with Arabic-first UX, RTL support, and localized payment, shipping, and tax integrations built for the GCC market.
  name: Arabic-First No-Code Store Builder
- description: REST API at https://api.salla.dev/admin/v2 covering products, orders, customers, branches, brands, categories, currencies, languages, coupons, taxes, abandoned carts, shipping, and store settings.
  name: Salla Merchant API
- description: OAuth 2.0 authorization with 14-day access tokens and 1-month refresh window; scoped per app via the Partners Portal.
  name: OAuth 2.0 Partners Authorization
- description: HMAC SHA-256 signed webhooks (X-Salla-Signature / X-Salla-Security-Strategy headers) for order, product, customer, shipping, shipment, store, category, brand, abandoned-cart, coupon, invoice, special offer, and review events — with per-subscription conditional rules.
  name: Webhooks with Conditional Rules
- description: JavaScript SDK plus Twig-based theme engine with pre-built web components (cart, checkout, login, search, product display) for storefront customization.
  name: Twilight Theme Engine and SDK
- description: Command-line tool for scaffolding, developing, and publishing Salla apps and themes to the Partners Portal.
  name: Salla CLI
- description: A Shipping and Fulfillment API contract that lets logistics providers plug directly into the Salla shipment flow.
  name: Shipping App Contract
- description: First-class support for Saudi Arabia's ZATCA (Fatoora) e-invoicing QR code requirement via the official open-source PHP package.
  name: ZATCA E-Invoicing
- description: Embedded SDK lets partner apps render inside the merchant dashboard; the Salla App Store distributes third-party apps to 80,000+ stores.
  name: Embedded SDK and Apps Marketplace
- description: Native integrations with STC Pay, mada, Apple Pay, Tabby, Tamara, HyperPay, Mada Pay, Aramex, SMSA, DHL, J&T, and other regional payment and logistics providers.
  name: Saudi Payments and Logistics
finops:
- name: Salla Finops
  service_category: Commerce Platform
  slug: salla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salla.png
integrations:
- description: Native STC Bank digital wallet payment option across all Salla-powered stores.
  name: STC Bank
- description: Buy-now-pay-later integrations widely used in the GCC market.
  name: Tabby and Tamara
- description: Apple Pay and the Saudi mada national payment network.
  name: Apple Pay and mada
- description: Regional payment gateways supporting cards, wallets, and bank transfers.
  name: HyperPay and Moyasar
- description: Pre-built shipping integrations for Saudi Arabia and GCC delivery.
  name: Aramex, SMSA, J&T, DHL
- description: Saudi Arabian Zakat, Tax and Customs Authority e-invoicing.
  name: ZATCA
- description: Customer notifications and conversational commerce.
  name: WhatsApp Business
- description: Email and customer marketing automation.
  name: Mailchimp and Klaviyo
- description: Storefront pixels and conversion tracking for GCC-focused ad platforms.
  name: Snapchat and TikTok Pixels
json_schemas:
- name: Salla Customer
  property_count: 14
  slug: salla-customer
- name: Salla Order
  property_count: 16
  slug: salla-order
- name: Salla Product
  property_count: 21
  slug: salla-product
jsonld:
- class_count: 0
  name: Salla Context
  property_count: 5
  slug: salla-context
layout: provider
modified: '2026-05-24'
name: Salla
nav: Providers
network: true
overview: 'Salla publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Branches API, Brands API, and 14 more. Tagged areas include Arabic, E-Commerce, GCC, Headless Commerce, and Merchant.


  The Salla catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salla''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, developer console, pricing, and 45 more developer resources.'
plans:
- name: Salla Plans Pricing
  plan_count: 5
  slug: salla-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Salla Rate Limits
  slug: salla-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Salla API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: salla-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Salla API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 3
  slug: salla-rules
scopes:
- name: Salla Scopes
  scope_count: 11
  slug: salla-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.3
  delta: 0.8
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 28.8
    contract_quality: 68.5
    developer_ergonomics: 85.7
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 68.4
  previous_composite: 72.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 94.1
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salla/refs/heads/main/screenshots/salla-2026-06-20T193358.png
security:
- kind: authentication
  name: Salla Authentication
  slug: salla-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Salla Domain Security
  slug: salla-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: salla
solutions:
- description: Merchants of any size launching an online store with Arabic-first UX, regional payments, and built-in logistics.
  name: Sellers
- description: Developers and agencies building apps, themes, and integrations distributed through the Salla Partners Portal and App Store.
  name: Partners
- description: Logistics providers offering their service to 80,000+ merchants by implementing the Salla Shipping App contract.
  name: Shipping Companies
- description: Larger brands needing custom themes, dedicated infrastructure, and bespoke commercial terms.
  name: Enterprise
tags:
- Arabic
- E-Commerce
- GCC
- Headless Commerce
- Merchant
- MENA
- Online Stores
- Retail
- Saudi Arabia
- SMB
- Storefront
use_cases:
- description: Build custom apps published in the Salla App Store that extend merchant capabilities — inventory sync, order routing, marketing automation, ERP integration.
  name: Custom Merchant Apps
- description: Sync orders, products, customers, and invoices to SAP, Oracle NetSuite, Odoo, Zoho Books, QuickBooks, or custom accounting systems.
  name: ERP and Accounting Integrations
- description: Build custom Twilight themes or headless storefronts that render Salla catalog and checkout through a fully custom front end.
  name: Custom Storefronts and Themes
- description: Logistics companies expose their pickup, label printing, tracking, and return surface as a Salla Shipping App to serve every merchant on the platform.
  name: Shipping Provider Onboarding
- description: Subscribe to customer, order, and abandoned-cart webhooks to drive CRM, email, SMS, and WhatsApp campaigns through Mailchimp, Klaviyo, or in-house automation.
  name: Marketing and CRM Automation
- description: Use the Merchant API plus Naftiko capabilities to power AI agents that browse catalog, place orders, track shipments, and respond to merchant questions.
  name: AI Shopping Assistants
- description: Generate the Saudi ZATCA Phase-1 / Phase-2 e-invoicing QR code on every receipt to remain compliant with Saudi Arabian tax authority requirements.
  name: ZATCA Compliance
website: https://salla.com
---
