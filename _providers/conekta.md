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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 72
  human_in_the_loop: 0
  name: Conekta Agentic Access
  operation_count: 113
  slug: conekta-agentic-access
  summary_line: 113 operations · 72 acting
api_count: 25
apis:
- description: The Antifraud API from Conekta — 4 operation(s) for antifraud.
  name: Conekta Antifraud API
  slug: conekta-antifraud-api
- description: The Api Keys API from Conekta — 2 operation(s) for api keys.
  name: Conekta Api Keys API
  slug: conekta-api-keys-api
- description: The Balances API from Conekta — 1 operation(s) for balances.
  name: Conekta Balances API
  slug: conekta-balances-api
- description: The Charges API from Conekta — 4 operation(s) for charges.
  name: Conekta Charges API
  slug: conekta-charges-api
- description: The Companies API from Conekta — 5 operation(s) for companies.
  name: Conekta Companies API
  slug: conekta-companies-api
- description: The Customers API from Conekta — 4 operation(s) for customers.
  name: Conekta Customers API
  slug: conekta-customers-api
- description: The Discounts API from Conekta — 2 operation(s) for discounts.
  name: Conekta Discounts API
  slug: conekta-discounts-api
- description: The Events API from Conekta — 3 operation(s) for events.
  name: Conekta Events API
  slug: conekta-events-api
- description: The Logs API from Conekta — 2 operation(s) for logs.
  name: Conekta Logs API
  slug: conekta-logs-api
- description: The Orders API from Conekta — 6 operation(s) for orders.
  name: Conekta Orders API
  slug: conekta-orders-api
- description: The Payment Link API from Conekta — 5 operation(s) for payment link.
  name: Conekta Payment Link API
  slug: conekta-payment-link-api
- description: The Payment Methods API from Conekta — 2 operation(s) for payment methods.
  name: Conekta Payment Methods API
  slug: conekta-payment-methods-api
- description: The Payout Orders API from Conekta — 3 operation(s) for payout orders.
  name: Conekta Payout Orders API
  slug: conekta-payout-orders-api
- description: The Plans API from Conekta — 2 operation(s) for plans.
  name: Conekta Plans API
  slug: conekta-plans-api
- description: The Products API from Conekta — 2 operation(s) for products.
  name: Conekta Products API
  slug: conekta-products-api
- description: The Shipping Contacts API from Conekta — 2 operation(s) for shipping contacts.
  name: Conekta Shipping Contacts API
  slug: conekta-shipping-contacts-api
- description: The Shippings API from Conekta — 2 operation(s) for shippings.
  name: Conekta Shippings API
  slug: conekta-shippings-api
- description: All subscription-related endpoints including creation, management, and events
  name: Conekta Subscriptions API
  slug: conekta-subscriptions-api
- description: Customer portal endpoints for subscriptions
  name: Conekta Subscriptions - Customer Portal API
  slug: conekta-subscriptions-customer-portal-api
- description: The Taxes API from Conekta — 2 operation(s) for taxes.
  name: Conekta Taxes API
  slug: conekta-taxes-api
- description: The Tokens API from Conekta — 1 operation(s) for tokens.
  name: Conekta Tokens API
  slug: conekta-tokens-api
- description: The Transactions API from Conekta — 2 operation(s) for transactions.
  name: Conekta Transactions API
  slug: conekta-transactions-api
- description: The Transfers API from Conekta — 2 operation(s) for transfers.
  name: Conekta Transfers API
  slug: conekta-transfers-api
- description: The Webhook keys API from Conekta — 2 operation(s) for webhook keys.
  name: Conekta Webhook keys API
  slug: conekta-webhook-keys-api
- description: The Webhooks API from Conekta — 3 operation(s) for webhooks.
  name: Conekta Webhooks API
  slug: conekta-webhooks-api
artifact_total: 62
collections:
- collection_type: open
  name: Conekta API
  slug: open-conekta-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/conekta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conekta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/conekta-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.conekta.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.conekta.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.conekta.com/docs/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.conekta.com/docs/inicio-rápido-pagos-únicos-con-component
- group: docs
  title: ''
  type: Documentation
  url: https://developers.conekta.com/reference
- group: auth
  title: ''
  type: Authentication
  url: https://developers.conekta.com/reference/autenticación
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.conekta.com/reference/errores
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.conekta.com/docs/códigos-de-error-http
- group: docs
  title: ''
  type: Documentation
  url: https://developers.conekta.com/docs/eventos-conekta
- group: docs
  title: ''
  type: Documentation
  url: https://developers.conekta.com/docs/configurar-un-webhook
- group: docs
  title: ''
  type: Documentation
  url: https://developers.conekta.com/docs/autenticación-webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://developers.conekta.com/docs/reintentos-de-notificación
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.conekta.com/changelog/versión-220
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.conekta.com/changelog/version-21
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/conekta
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/conekta/openapi
- group: build
  title: ''
  type: Tools
  url: https://github.com/conekta/mcp-server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-.net
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-elements
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/conekta-elements-react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/conekta/component-flutter
- group: build
  title: ''
  type: SDKs
  url: https://developers.conekta.com/android
- group: build
  title: ''
  type: SDKs
  url: https://developers.conekta.com/ios-skd
- group: build
  title: ''
  type: SDKs
  url: https://developers.conekta.com/checkout-tokenizer-sdk
- group: build
  title: ''
  type: SDKs
  url: https://developers.conekta.com/xamarin
- group: build
  title: ''
  type: Plugins
  url: https://github.com/conekta/ct-woocommerce-plugin
- group: build
  title: ''
  type: Plugins
  url: https://github.com/conekta/customer-magento-plugin
- group: start
  title: ''
  type: Signup
  url: https://panel.conekta.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.conekta.com/precios
- group: commercial
  title: ''
  type: Plans
  url: plans/conekta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conekta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/conekta-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://conekta.com/blog
created: '2026-05-24T00:00:00.000Z'
description: Conekta is a Mexico-based payment processor that lets businesses accept credit and debit cards, OXXO cash vouchers, SPEI bank transfers, Apple Pay, Google Pay, and Buy Now Pay Later through a single PCI-DSS Level 1 certified API. The platform serves the Mexican market with Spanish-language documentation, CNBV-aligned compliance, and full Orders, Charges, Customers, Subscriptions, Payment Links, Antifraud, Webhooks, Payouts, and Balances resources. Conekta publishes its OpenAPI 3.1 specification publicly under MIT license, ships official SDKs for PHP, Node.js, Python, Ruby, .NET, and Java, and offers mobile components for Android, iOS, Flutter, and React Native plus plugins for major e-commerce platforms.
examples:
- key_count: 2
  name: Conekta Create Order Card Example
  slug: conekta-create-order-card-example
- key_count: 2
  name: Conekta Create Order Oxxo Example
  slug: conekta-create-order-oxxo-example
- key_count: 2
  name: Conekta Create Order Spei Example
  slug: conekta-create-order-spei-example
- key_count: 2
  name: Conekta Create Webhook Example
  slug: conekta-create-webhook-example
features:
- Card payments — Visa, Mastercard, American Express (debit and credit, domestic and international)
- OXXO cash payment vouchers with reference numbers expiring on a configurable date
- SPEI bank transfer payments via CLABE references
- Apple Pay and Google Pay support through Checkout Component and Tokenizer
- Buy Now Pay Later (Pago en plazos) and Meses Sin Intereses (MSI) installment plans
- Subscriptions API with Plans, trial periods, and a customer portal
- Payment Links — shareable hosted checkout URLs
- Antifraud — managed whitelist and blacklist rules per merchant
- 3D Secure 2 authentication for card-present-not-present transactions
- Webhooks for asynchronous order, charge, subscription, and payout events with signature verification and configurable retries
- Payout Orders and Transfers APIs for moving funds out of the Conekta balance
- Balances API for inspecting available, retained, and pending funds
- Companies API for multi-entity / marketplace structures with X-Child-Company-Id header
- PCI-DSS Level 1 certified tokenization via Checkout Tokenizer and mobile SDKs
- Official OpenAPI 3.1 specification published under MIT license at github.com/conekta/openapi
- Bearer token authentication with mandatory Accept-Language header (es / en) for localized responses
- Spanish-language API documentation and error messages aligned with Mexico (CNBV-regulated) market
- Official SDKs for PHP, Node.js, Python, Ruby, .NET, Java, plus Android, iOS, Flutter, and React Native components
- Pre-built integrations for Shopify, VTEX, Magento, WooCommerce, PrestaShop, and Tiendanube
- MCP server for AI agent integration
finops:
- name: Conekta Finops
  service_category: Payments
  slug: conekta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conekta.png
json_schemas:
- name: Conekta Charge
  property_count: 14
  slug: conekta-charge
- name: Conekta Customer
  property_count: 16
  slug: conekta-customer
- name: Conekta Order
  property_count: 17
  slug: conekta-order
jsonld:
- class_count: 0
  name: Conekta Context
  property_count: 7
  slug: conekta-context
layout: provider
modified: '2026-05-24'
name: Conekta
nav: Providers
network: true
overview: 'Conekta publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Antifraud API, Api Keys API, Balances API, and 22 more. Tagged areas include Payments, Payment Processing, Cards, Cash, and OXXO.


  The Conekta catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Conekta''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, tooling, signup flow, and 34 more developer resources.'
plans:
- name: Conekta Plans Pricing
  plan_count: 5
  slug: conekta-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 2
  name: Conekta Rate Limits
  slug: conekta-rate-limits
rules:
- name: Conekta API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: conekta-jsonschema-spectral-rules
- name: Conekta API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 1
    info: 3
    warn: 4
  slug: conekta-rules
score:
  band: developing
  composite: 55.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 75.4
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conekta/refs/heads/main/screenshots/conekta-2026-06-20T174849.png
security:
- kind: authentication
  name: Conekta Authentication
  slug: conekta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Conekta Domain Security
  slug: conekta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conekta
tags:
- Payments
- Payment Processing
- Cards
- Cash
- OXXO
- SPEI
- Mexico
- Latin America
- LATAM
- Fintech
- Subscriptions
- Antifraud
- Checkout
- BNPL
- 3D Secure
website: https://www.conekta.com
---
