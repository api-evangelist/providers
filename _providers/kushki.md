---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Kushki Agentic Access
  operation_count: 28
  slug: kushki-agentic-access
  summary_line: 28 operations · 20 acting
api_count: 5
apis:
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: 'Create, update, retrieve, charge, and cancel scheduled card subscriptions and one-click recurring payments. Plans support monthly, weekly, daily, biweekly, quarterly, and yearly periodicity, fixed or '
  name: Kushki Subscriptions API
  slug: kushki-subscriptions-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: 'Disburse funds to suppliers, partners, payroll, marketplace sellers, and refunds via bank transfer, card push, or cash pickup. Supports same-day and standard rails, batch upload, and country-specific '
  name: Kushki Payouts API
  slug: kushki-payouts-api
- description: Real-time event notifications for approved, declined, voided, refunded, and captured transactions across every product (card, transfer, cash, subscription, payout). Webhooks ship a signed JSON payload
  name: Kushki Webhooks
  slug: kushki-webhooks
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Branch / sucursal management
  name: Kushki Branches API
  slug: kushki-branches-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Sale, void, and settlement for card-present
  name: Kushki Card Present Charges API
  slug: kushki-card-present-charges-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Cash voucher generation and lookup
  name: Kushki Cash API
  slug: kushki-cash-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Direct charge against a previously created card token
  name: Kushki Charges API
  slug: kushki-charges-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Two-step authorize + capture flow
  name: Kushki Pre-Authorization API
  slug: kushki-pre-authorization-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Kushki One terminal management
  name: Kushki Terminals API
  slug: kushki-terminals-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Card tokenization (client-side via Kushki.js, returns a one-time transactionToken)
  name: Kushki Tokens API
  slug: kushki-tokens-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Bank-rail transfer charges
  name: Kushki Transfer API
  slug: kushki-transfer-api
- baseURL: https://api.kushkipagos.com
  baseurl_source: declared
  description: Void or refund a previously captured charge
  name: Kushki Voids and Refunds API
  slug: kushki-voids-and-refunds-api
artifact_total: 97
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kushki Card Payments Branches API
  slug: open-kushki-branches-api
- collection_type: open
  name: Kushki Card Payments API
  slug: open-kushki-card-payments-api
- collection_type: open
  name: Kushki Card Present API
  slug: open-kushki-card-present-api
- collection_type: open
  name: Kushki Card Payments Branches Card Present Charges API
  slug: open-kushki-card-present-charges-api
- collection_type: open
  name: Kushki Card Payments Branches Cash API
  slug: open-kushki-cash-api
- collection_type: open
  name: Kushki Cash Payments API
  slug: open-kushki-cash-payments-api
- collection_type: open
  name: Kushki Card Payments Branches Charges API
  slug: open-kushki-charges-api
- collection_type: open
  name: Kushki Merchants and Branches API
  slug: open-kushki-merchants-api
- collection_type: open
  name: Kushki Card Payments Branches Payouts API
  slug: open-kushki-payouts-api
- collection_type: open
  name: Kushki Card Payments Branches Pre-Authorization API
  slug: open-kushki-pre-authorization-api
- collection_type: open
  name: Kushki Card Payments Branches Subscriptions API
  slug: open-kushki-subscriptions-api
- collection_type: open
  name: Kushki Card Payments Branches Terminals API
  slug: open-kushki-terminals-api
- collection_type: open
  name: Kushki Card Payments Branches Tokens API
  slug: open-kushki-tokens-api
- collection_type: open
  name: Kushki Card Payments Branches Transfer API
  slug: open-kushki-transfer-api
- collection_type: open
  name: Kushki Transfer Payments API
  slug: open-kushki-transfer-payments-api
- collection_type: open
  name: Kushki Card Payments Branches Voids and Refunds API
  slug: open-kushki-voids-and-refunds-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kushki-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kushki-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kushki-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://kushkipagos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kushki.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.kushkipagos.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kushki.com/
- group: operate
  title: ''
  type: Support
  url: https://soporte.kushkipagos.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kushkipagos.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kushki
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kushki/kushki-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kushki/kushki-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kushki/kushki-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kushki/kushki-ios-intel
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Kushki/kushki-ios-arm
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Kushki/kushki-woocommerce
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Kushki/kushki-magento
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Kushki/kushki-prestashop
- group: build
  title: ''
  type: Plugin
  url: https://github.com/Kushki/kushki-vtex
- group: build
  title: ''
  type: Examples
  url: https://github.com/Kushki/kushki-backend-examples
- group: build
  title: ''
  type: Examples
  url: https://github.com/Kushki/kushki-demo-php
- group: other
  title: ''
  type: Docker
  url: https://github.com/Kushki/kushki-docker
- group: start
  title: ''
  type: Console
  url: https://uat-console.kushkipagos.com/
- group: start
  title: ''
  type: Console
  url: https://console.kushkipagos.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kushki/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/kushkipagos
- group: auth
  title: ''
  type: Authentication
  url: https://docs.kushki.com/
- group: other
  title: ''
  type: Environments
  url: ''
- group: other
  title: ''
  type: Regions
  url: ''
- group: commercial
  title: ''
  type: Plans
  url: plans/kushki-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kushki-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kushki-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kushki-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/kushki-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kushkipagos.com/blog
created: '2026-05-24'
description: Kushki is an Ecuador-headquartered LatAm fintech operating as a regional non-banking acquirer for the Andean and Pacific Alliance markets — Ecuador, Colombia, Peru, Chile, Mexico, and Brazil. The Kushki API unifies card payments, scheduled and one-click subscriptions, bank transfers (PSE, Webpay Transferencia, SPEI, PIX), cash vouchers (OXXO, PagoEfectivo, Boleto), payouts/dispersions, and card-present (Kushki One POS) behind a single REST surface. Authentication is split across a Public-Merchant-Id (used in the browser to tokenize cards) and a Private-Merchant-Id (used server-side to charge). PCI DSS Level 1, 3DS 2.0, multi-layer anti-fraud, hosted fields, Kajita payment forms, Smartlinks, and e-commerce plugins (Shopify, VTEX, WooCommerce, Magento, PrestaShop) round out the platform.
examples:
- key_count: 2
  name: Kushki Create Card Charge Example
  slug: kushki-create-card-charge-example
- key_count: 2
  name: Kushki Create Cash Voucher Example
  slug: kushki-create-cash-voucher-example
- key_count: 2
  name: Kushki Create Subscription Example
  slug: kushki-create-subscription-example
- key_count: 2
  name: Kushki Init Payout Example
  slug: kushki-init-payout-example
- key_count: 2
  name: Kushki Init Transfer Charge Example
  slug: kushki-init-transfer-charge-example
- key_count: 14
  name: Kushki Webhook Event Example
  slug: kushki-webhook-event-example
features:
- Regional non-banking acquirer covering Ecuador, Colombia, Peru, Chile, Mexico, and Brazil from a single integration
- Card tokenization via Kushki.js Hosted Fields, iOS SDK, and Android SDK (PAN never touches the merchant server)
- One-step charge and two-step pre-authorization + capture for card-not-present transactions
- Deferred / installment payments with merchant-defined months and rate-of-interest
- Webpay Plus, Webpay OneClick, and Webpay Transferencia integration on the Chilean rail
- 3DS 1.0 and 3DS 2.0 issuer authentication, with liability shift handling
- Apple Pay support on card-present and card-not-present
- PSE bank-transfer flow for Colombia, SPEI for Mexico, PIX for Brazil
- Cash voucher generation for OXXO, 7-Eleven, PagoEfectivo, Boleto, and regional correspondent networks
- Card-Present POS via Kushki One terminals and the Raw Card Present API with encryption envelope
- Payouts (dispersions) to bank accounts, cards, and cash pickup with batch upload and country compliance metadata
- Scheduled and one-click subscriptions with monthly / weekly / quarterly / yearly periodicity
- Smartlinks shareable payment links for chat, SMS, email, and social channels
- Kajita customizable hosted payment form
- Payment button hosted redirect flow
- Branch / sucursal management for marketplaces, franchises, and aggregators
- Webhook notifications with signed payloads, retry policy, and exponential backoff
- 4+ layer anti-fraud stack (Sift Science, in-house rules, 3DS, velocity checks, behavioural signals)
- PCI DSS Level 1 compliance and PCI-compliant Hosted Fields JS library
- E-commerce plugins for Shopify, VTEX, WooCommerce, Magento, and PrestaShop
- Official SDKs for PHP, iOS (Swift, INTEL + ARM processors), and Android (Kotlin)
- UAT sandbox at api-uat.kushkipagos.com with documented test card numbers
- Public/private merchant key authentication model (Public-Merchant-Id, Private-Merchant-Id headers)
- Status page at status.kushkipagos.com and support knowledge base at soporte.kushkipagos.com
finops:
- name: Kushki Finops
  service_category: Payments and Financial Services
  slug: kushki-finops
image: https://kushki-cdn-production.s3.amazonaws.com/docs/Logo+Kushki+3+Horizontal+White+2019+08.png
integrations:
- Shopify
- VTEX
- WooCommerce
- Magento
- PrestaShop
- Webpay (Transbank)
- Apple Pay
- Sift Science (anti-fraud)
- PIX (Banco Central do Brasil)
- SPEI (Banco de México)
- PSE (ACH Colombia)
- OXXO
- 7-Eleven
- PagoEfectivo
- Boleto Bancário
json_schemas:
- name: Kushki Charge
  property_count: 10
  slug: kushki-charge
- name: Kushki Subscription
  property_count: 9
  slug: kushki-subscription
- name: Kushki Card Token
  property_count: 3
  slug: kushki-token
- name: Kushki Webhook Event
  property_count: 14
  slug: kushki-webhook-event
jsonld:
- class_count: 0
  name: Kushki Context
  property_count: 6
  slug: kushki-context
layout: provider
modified: '2026-05-24'
name: Kushki
nav: Providers
network: true
overview: 'Kushki publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Subscriptions API, Payouts API, Branches API, and 8 more. Tagged areas include Payments, LatAm, Andean Region, Card Payments, and Subscription.


  The Kushki catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Kushki''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, support, code examples, and 26 more developer resources.'
plans:
- name: Kushki Plans Pricing
  plan_count: 6
  slug: kushki-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Kushki Rate Limits
  slug: kushki-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kushki API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kushki-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Kushki API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: kushki-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 70.7
    developer_ergonomics: 73.8
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kushki/refs/heads/main/screenshots/kushki-2026-06-20T184217.png
security:
- kind: authentication
  name: Kushki Authentication
  slug: kushki-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Kushki Domain Security
  slug: kushki-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kushki
tags:
- Payments
- LatAm
- Andean Region
- Card Payments
- Subscription
- Cash
- Bank Transfers
- Payouts
- PSE
- Webpay
- SPEI
- Pix
- OXXO
- PagoEfectivo
- Fintech
- Ecuador
- Colombia
- Peru
- Chile
- Mexico
- Brazil
use_cases:
- LatAm e-commerce checkout with card, cash, and bank transfer in one integration
- Marketplace payouts to sellers across Andean and Pacific Alliance countries
- SaaS subscription billing with one-click recurring payments
- Cross-border ride-hailing, food-delivery, and gig-economy disbursements
- Omnichannel retail combining Kushki One POS with e-commerce checkout
- Cash-first commerce in markets where cash share remains >40% of consumer payments
- Franchise and multi-branch sub-merchant management for regional brands
- PIX-first checkout in Brazil with card fallback
- PSE bank-transfer integration for Colombian high-ticket purchases
- SPEI mass payouts in Mexico for marketplace sellers
website: https://kushkipagos.com/
---
