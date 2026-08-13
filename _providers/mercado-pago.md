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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Mercado Pago Agentic Access
  operation_count: 60
  slug: mercado-pago-agentic-access
  summary_line: 60 operations · 31 acting
api_count: 44
apis:
- description: 'Hosted, pre-configured checkout experience. Merchants create a preference via API, then redirect the buyer to a Mercado Pago hosted page that handles UI, payment-method selection, 3DS, and returns to '
  name: Mercado Pago Checkout Pro
  slug: checkout-pro
- description: 'Composable web components ("bricks") merchants embed in their own UI — card form, wallet, payment-method picker, status screen, security code. Lets merchants assemble a branded checkout while Mercado '
  name: Mercado Pago Checkout Bricks
  slug: checkout-bricks
- description: Full server-side checkout control. Tokenise cards client-side, create a payment server-side, manage 3DS challenges, handle capture, refund, and installments — all without redirecting the buyer.
  name: Mercado Pago Checkout API
  slug: checkout-api
- description: Next-generation unified Orders API consolidating payments, captures, refunds, and transactions under a single resource. Supports multi-method orders, partial captures, partial refunds, and async proce
  name: Mercado Pago Orders API
  slug: orders
- description: Recurring payment subscriptions (preapproval) with scheduling, shared plans, free trial, proration, and pause / resume / cancel. Supports both subscription plans (preapproval_plan) and per-customer pr
  name: Mercado Pago Subscriptions API
  slug: subscriptions
- description: No-code / low-code link generation for collecting a one-off or recurring payment via shareable URL or button — SMS, WhatsApp, email, social.
  name: Mercado Pago Payment Links API
  slug: payment-links
- description: Manage stored customers and tokenised cards for one-click and recurring payments. CRUD for customers, addresses, and card tokens.
  name: Mercado Pago Customers & Cards API
  slug: customers-cards
- description: Aggregate a preference + its payments into a single merchant_order resource for reconciliation, multi-payment handling, and order lifecycle.
  name: Mercado Pago Merchant Orders API
  slug: merchant-orders
- description: Integrates merchant systems with Mercado Pago Point card readers for in-person payments. Push an amount to a paired terminal, manage stores, points-of-sale, and terminals, and reconcile via the same p
  name: Mercado Pago Point API (POS)
  slug: point
- description: Static and dynamic QR code APIs for in-person collection, with order-linked status retrieval and webhook callbacks. Underpins the Mercado Pago wallet QR pay flow.
  name: Mercado Pago QR API
  slug: qr
- description: Retrieve and respond to chargebacks, including dispute reason codes and lifecycle states.
  name: Mercado Pago Chargebacks API
  slug: chargebacks
- description: Post-sale claims, mediations, evidence upload, messages, and notification retrieval for resolving buyer disputes.
  name: Mercado Pago Claims & Disputes API
  slug: claims
- description: Generate, configure, and download release / settlement / account-money reports for reconciliation and accounting.
  name: Mercado Pago Reports API
  slug: reports
- description: 'OAuth 2.0 authorisation-code flow for platform integrations: marketplaces and partners obtain delegated access tokens on behalf of merchants.'
  name: Mercado Pago OAuth 2.0 API
  slug: oauth
- description: Event-driven notifications for payments, refunds, chargebacks, subscriptions, merchant orders, and account changes. Webhooks are signed with an x-signature header so receivers can verify authenticity.
  name: Mercado Pago Webhooks / Notifications
  slug: webhooks
- description: Official Node.js / TypeScript SDK wrapping the Mercado Pago REST APIs for payments, preferences, subscriptions, customers, cards, and merchant orders.
  name: Mercado Pago Node.js SDK
  slug: sdk-node
- description: Official Python SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago Python SDK
  slug: sdk-python
- description: Official PHP SDK wrapping the Mercado Pago REST APIs. Used by the WooCommerce plugin and most LATAM PHP merchant stacks.
  name: Mercado Pago PHP SDK
  slug: sdk-php
- description: Official Ruby SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago Ruby SDK
  slug: sdk-ruby
- description: Official Java SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago Java SDK
  slug: sdk-java
- description: Official .NET / C# SDK wrapping the Mercado Pago REST APIs.
  name: Mercado Pago .NET SDK
  slug: sdk-dotnet
- description: Official Go SDK for the Mercado Pago REST APIs.
  name: Mercado Pago Go SDK
  slug: sdk-go
- description: Official iOS / Swift mobile SDK providing card tokenisation, hosted payment screens, and Checkout integration for native iOS apps.
  name: Mercado Pago iOS SDK
  slug: sdk-ios
- description: Official Android / Kotlin mobile SDK for tokenisation, payment screens, and Checkout integration in native Android apps.
  name: Mercado Pago Android SDK
  slug: sdk-android
- description: 'Command-line interface for managing Mercado Pago integrations: trigger test events, inspect webhook deliveries, scaffold sample apps, and run local listeners. Distributed via a Homebrew tap.'
  name: Mercado Pago CLI
  slug: cli
- description: Model Context Protocol server exposing Mercado Pago APIs as tools for AI agents and IDE assistants. Enables agent-driven payment, preference, and checkout workflows from Anthropic, OpenAI, and other M
  name: Mercado Pago MCP Server
  slug: mcp
- description: Official WooCommerce gateway plugin enabling Mercado Pago Checkout Pro, Bricks, and Checkout API payment methods in WordPress stores.
  name: Mercado Pago WooCommerce Plugin
  slug: woocommerce
- description: Official n8n workflow automation node for orchestrating Mercado Pago operations alongside other SaaS apps.
  name: Mercado Pago n8n Node
  slug: n8n
- description: OAuth 2.0 authorisation flows
  name: Mercado Pago Authentication API
  slug: mercado-pago-authentication-api
- description: Tokenised customer cards
  name: Mercado Pago Cards API
  slug: mercado-pago-cards-api
- description: Read chargebacks and disputes
  name: Mercado Pago Chargebacks API
  slug: mercado-pago-chargebacks-api
- description: Buyer claims, mediations, and evidence
  name: Mercado Pago Claims API
  slug: mercado-pago-claims-api
- description: Stored customers and addresses
  name: Mercado Pago Customers API
  slug: mercado-pago-customers-api
- description: Aggregated preference + payments order resource
  name: Mercado Pago Merchant Orders API
  slug: mercado-pago-merchant-orders-api
- description: Unified Orders API (next-generation checkout)
  name: Mercado Pago Orders API
  slug: mercado-pago-orders-api
- description: Discover available payment methods
  name: Mercado Pago Payment Methods API
  slug: mercado-pago-payment-methods-api
- description: Create, capture, refund, and search payments
  name: Mercado Pago Payments API
  slug: mercado-pago-payments-api
- description: Subscription plans
  name: Mercado Pago Plans API
  slug: mercado-pago-plans-api
- description: In-person POS (stores, terminals)
  name: Mercado Pago Point API
  slug: mercado-pago-point-api
- description: Checkout Pro preferences
  name: Mercado Pago Preferences API
  slug: mercado-pago-preferences-api
- description: QR-code in-person collection
  name: Mercado Pago QR API
  slug: mercado-pago-qr-api
- description: Refund payments
  name: Mercado Pago Refunds API
  slug: mercado-pago-refunds-api
- description: Settlement and release reports
  name: Mercado Pago Reports API
  slug: mercado-pago-reports-api
- description: Recurring preapproval subscriptions
  name: Mercado Pago Subscriptions API
  slug: mercado-pago-subscriptions-api
artifact_total: 68
asyncapis:
- description: Mercado Pago webhook notifications for payments, refunds, chargebacks, merchant orders, subscriptions, and POS events. Webhook payloads include `x-signature` and `x-request-id` headers — receivers MUS
  name: Mercado Pago Webhooks (IPN / Webhooks v2)
  slug: mercado-pago-asyncapi
collections:
- collection_type: open
  name: Mercado Pago REST API
  slug: open-mercado-pago
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/mercadopago/sdk-nodejs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/mercadopago/sdk-nodejs/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/mercadopago/sdk-nodejs/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/mercadopago/sdk-nodejs/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/mercadopago/sdk-nodejs/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mercado-pago-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercado-pago-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mercado-pago-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mercado-pago-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.mercadopago.com/
- group: other
  title: ''
  type: Developers
  url: https://www.mercadopago.com.br/developers/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.mercadopago.com.br/developers/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.mercadopago.com.br/developers/en/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mercadopago.com.br/developers/en/docs/your-integrations/credentials
- group: operate
  title: ''
  type: Status
  url: https://status.mercadopago.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercadopago
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mercadopago
- group: other
  title: ''
  type: HomebrewTap
  url: https://github.com/mercadopago/homebrew-tap
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/mercadopagodevelopers
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/mercado-pago/refs/heads/main/plans/mercado-pago-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/mercado-pago/refs/heads/main/rate-limits/mercado-pago-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/mercado-pago/refs/heads/main/finops/mercado-pago-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/mercado-pago/refs/heads/main/vocabulary/mercado-pago-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/mercado-pago/refs/heads/main/json-ld/mercado-pago-context.jsonld
- group: design
  title: ''
  type: SpectralRuleset
  url: https://raw.githubusercontent.com/api-evangelist/mercado-pago/refs/heads/main/rules/mercado-pago-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.mercadopago.com.ar/developers/en/news
created: '2026-05-25'
description: Mercado Pago is the payments and financial-services arm of Mercado Libre, Latin America's largest e-commerce and fintech platform. Founded in 2003, it processes a substantial share of LatAm digital payments across Brazil (PIX, Boleto, cards), Argentina, Mexico (SPEI, OXXO), Chile, Colombia, Peru, and Uruguay, with consumer wallet, merchant acquiring, card issuing, lending, and crypto products layered on top. The developer portal at developers.mercadopago.com exposes a deep payments stack — Checkout Pro (hosted), Checkout Bricks (composable web components), Checkout API (full server-side control), Orders API (next-gen checkout), Subscriptions, Payment Links, Point (in-person card readers), and QR payments — backed by REST APIs and official SDKs in Node.js / TypeScript, Python, PHP, Ruby, Java, .NET, Go, iOS, and Android, plus a CLI, an MCP server for AI agents, e-commerce plugins (WooCommerce, VTEX, Tiendanube, Shopify), and an n8n integration. Regional developer portals (.com.ar,
  .com.br, .com.mx, .com.cl, .com.co, .com.pe, .com.uy) localise docs and pricing per LATAM market.
examples:
- key_count: 2
  name: Mercado Pago Create Payment Example
  slug: mercado-pago-create-payment-example
- key_count: 2
  name: Mercado Pago Create Preference Example
  slug: mercado-pago-create-preference-example
- key_count: 2
  name: Mercado Pago Create Subscription Example
  slug: mercado-pago-create-subscription-example
- key_count: 2
  name: Mercado Pago Refund Payment Example
  slug: mercado-pago-refund-payment-example
- key_count: 2
  name: Mercado Pago Webhook Payment Example
  slug: mercado-pago-webhook-payment-example
finops:
- name: Mercado Pago Finops
  service_category: Payments
  slug: mercado-pago-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercado-pago.png
json_schemas:
- name: Mercado Pago Payment
  property_count: 17
  slug: mercado-pago-payment
- name: Mercado Pago Checkout Preference
  property_count: 11
  slug: mercado-pago-preference
- name: Mercado Pago Refund
  property_count: 7
  slug: mercado-pago-refund
- name: Mercado Pago Subscription (Preapproval)
  property_count: 11
  slug: mercado-pago-subscription
json_structures:
- name: Mercado Pago Payment Structure
  property_count: 14
  slug: mercado-pago-payment-structure
- name: Mercado Pago Preference Structure
  property_count: 10
  slug: mercado-pago-preference-structure
jsonld:
- class_count: 33
  name: Mercado Pago Context
  property_count: 0
  slug: mercado-pago-context
layout: provider
modified: '2026-05-25'
name: Mercado Pago
nav: Providers
network: true
overview: 'Mercado Pago publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Webhooks / Notifications, Authentication API, Cards API, and 14 more. Tagged areas include Payments, Checkout, Subscriptions, POS, and QR.


  The Mercado Pago catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Mercado Pago''s developer surface includes authentication, documentation, API reference, getting-started guide, status page, engineering blog, and 20 more developer resources.'
plans:
- name: Mercado Pago Plans Pricing
  plan_count: 2
  slug: mercado-pago-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 3
  name: Mercado Pago Rate Limits
  slug: mercado-pago-rate-limits
rules:
- name: Mercado Pago API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: mercado-pago-asyncapi-spectral-rules
- name: Mercado Pago API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mercado-pago-jsonschema-spectral-rules
- name: Mercado Pago API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: mercado-pago-rules
scopes:
- name: Mercado Pago Scopes
  scope_count: 3
  slug: mercado-pago-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 66.7
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 52.1
    operational_transparency: 52.6
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mercado-pago/refs/heads/main/screenshots/mercado-pago-2026-06-20T185325.png
security:
- kind: authentication
  name: Mercado Pago Authentication
  slug: mercado-pago-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Mercado Pago Domain Security
  slug: mercado-pago-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mercado-pago
tags:
- Payments
- Checkout
- Subscriptions
- POS
- QR
- PIX
- SDKs
- Wallet
- Acquiring
- Lending
- Issuing
- Latin America
- Brazil
- Argentina
- Mexico
- Chile
- Colombia
- Peru
- Uruguay
- Fintech
website: https://www.mercadopago.com/
---
