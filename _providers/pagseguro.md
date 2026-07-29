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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Pagseguro Agentic Access
  operation_count: 47
  slug: pagseguro-agentic-access
  summary_line: 47 operations · 27 acting · 1 human-in-the-loop
api_count: 33
apis:
- description: Core REST surface for creating and managing orders and their associated charges across credit card, debit card with 3DS, boleto, and Pix. Covers capture, cancel, refund, fees retrieval, and stored-car
  name: PagBank Orders API
  slug: orders
- description: Hosted checkout and shareable payment-link generation. Merchants create, activate, deactivate, and retrieve checkouts; PagBank renders the UI, handles payment-method selection and 3DS, and returns the
  name: PagBank Checkout & Payment Link API
  slug: checkout
- description: Issues the public keys used for client-side card encryption in PagBank's transparent checkout. Lets merchants tokenise card data in the browser so raw PAN never reaches their servers.
  name: PagBank Public Keys API
  slug: public-keys
- description: Recurring-billing surface with plans, subscribers, subscriptions, invoices, coupons, refunds, and retry management. Supports activate, suspend, cancel, and per-subscriber payment-method updates.
  name: PagBank Recurring / Subscriptions API
  slug: recurring
- description: Pix (Brazilian Central Bank instant-payment rail) charge creation and collection. Supports QR-code generation, due-date Pix (Pix Cobrança), and payment status retrieval, integrated into the Orders flo
  name: PagBank Pix API
  slug: pix
- description: Boleto Bancário issuance and collection. Generates a printable / scannable boleto tied to an Order, with status callbacks once the buyer pays at a bank, lottery house, or via internet banking.
  name: PagBank Boleto API
  slug: boleto
- description: Payment-division (split) settlement for marketplaces and platforms. Splits a single charge across multiple receivers (with optional custody / release control) so each seller is settled directly by Pag
  name: PagBank Marketplace / Split API
  slug: split
- description: OAuth-style authorisation surface that lets a third-party application act on behalf of a PagBank account holder. Includes SMS and challenge verification, access-token issuance, refresh, and revoke.
  name: PagBank Connect / OAuth API
  slug: connect
- description: Lets PagBank partners create and query merchant accounts on behalf of third parties — the on-ramp for platforms that want to onboard sub-merchants into the PagBank ecosystem.
  name: PagBank Account Registration API
  slug: accounts
- description: Electronic Data Interchange surface for downloading transaction and settlement statements for reconciliation — a structured replacement for manual CSV/PDF statement processing.
  name: PagBank EDI API
  slug: edi
- description: Issues digital certificates for mTLS authentication, layered on top of bearer-token auth for higher-trust integrations and sensitive payouts / Pix Bacen flows.
  name: PagBank Digital Certificate (mTLS) API
  slug: certificates
- description: Event-driven notifications for order, charge, subscription, refund, and checkout state changes. Webhooks are signed so receivers can verify authenticity end-to-end.
  name: PagBank Webhooks / Notifications
  slug: webhooks
- description: Official PHP integration library for PagSeguro / PagBank.
  name: PagSeguro PHP SDK
  slug: sdk-php
- description: Official Java integration library for PagSeguro / PagBank.
  name: PagSeguro Java SDK
  slug: sdk-java
- description: Official Ruby integration library for PagSeguro / PagBank.
  name: PagSeguro Ruby SDK
  slug: sdk-ruby
- description: Official .NET / C# integration library for PagSeguro / PagBank.
  name: PagSeguro .NET SDK
  slug: sdk-dotnet
- description: Bluetooth / Android terminal integration for PagBank's Moderninha and Minizinha card readers, enabling third-party apps to drive in-person card and Pix payments on PagBank hardware.
  name: PagBank PlugPag (Terminal Integration)
  slug: plugpag
- description: Android service wrapper for integrating with the Moderninha / Minizinha terminal family — the official higher-level SDK on top of PlugPag.
  name: PagBank PlugPagServiceWrapper
  slug: plugpag-service-wrapper
- description: Official WooCommerce plugin embedding PagBank checkout, Pix, boleto, and card payments in WordPress storefronts.
  name: PagBank for WooCommerce
  slug: woocommerce
- description: Official Magento 2 / Adobe Commerce payment module for PagBank.
  name: PagBank Payment for Magento / Adobe Commerce
  slug: magento
- description: Official PrestaShop transparent-checkout integration module for PagSeguro / PagBank.
  name: PagSeguro PrestaShop Module
  slug: prestashop
- description: The Accounts API from PagSeguro / PagBank — 2 operation(s) for accounts.
  name: PagSeguro / PagBank Accounts API
  slug: pagseguro-accounts-api
- description: The Charges API from PagSeguro / PagBank — 4 operation(s) for charges.
  name: PagSeguro / PagBank Charges API
  slug: pagseguro-charges-api
- description: The Checkout API from PagSeguro / PagBank — 4 operation(s) for checkout.
  name: PagSeguro / PagBank Checkout API
  slug: pagseguro-checkout-api
- description: The Connect API from PagSeguro / PagBank — 6 operation(s) for connect.
  name: PagSeguro / PagBank Connect API
  slug: pagseguro-connect-api
- description: The Coupons API from PagSeguro / PagBank — 2 operation(s) for coupons.
  name: PagSeguro / PagBank Coupons API
  slug: pagseguro-coupons-api
- description: The Invoices API from PagSeguro / PagBank — 2 operation(s) for invoices.
  name: PagSeguro / PagBank Invoices API
  slug: pagseguro-invoices-api
- description: The Orders API from PagSeguro / PagBank — 2 operation(s) for orders.
  name: PagSeguro / PagBank Orders API
  slug: pagseguro-orders-api
- description: The Plans API from PagSeguro / PagBank — 4 operation(s) for plans.
  name: PagSeguro / PagBank Plans API
  slug: pagseguro-plans-api
- description: The PublicKeys API from PagSeguro / PagBank — 2 operation(s) for publickeys.
  name: PagSeguro / PagBank PublicKeys API
  slug: pagseguro-publickeys-api
- description: The Refunds API from PagSeguro / PagBank — 2 operation(s) for refunds.
  name: PagSeguro / PagBank Refunds API
  slug: pagseguro-refunds-api
- description: The Subscribers API from PagSeguro / PagBank — 3 operation(s) for subscribers.
  name: PagSeguro / PagBank Subscribers API
  slug: pagseguro-subscribers-api
- description: The Subscriptions API from PagSeguro / PagBank — 5 operation(s) for subscriptions.
  name: PagSeguro / PagBank Subscriptions API
  slug: pagseguro-subscriptions-api
artifact_total: 40
collections:
- collection_type: open
  name: PagBank / PagSeguro REST API
  slug: open-pagseguro
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pagseguro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pagseguro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pagseguro-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pagbank.com.br/
- group: company
  title: ''
  type: ConsumerWebsite
  url: https://pagseguro.uol.com.br/
- group: other
  title: ''
  type: Developers
  url: https://developer.pagbank.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pagbank.com.br/docs/apis-pagbank
- group: docs
  title: ''
  type: APIReference
  url: https://developer.pagbank.com.br/reference/introducao
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pagbank.com.br/docs/primeiros-passos-pagbank
- group: auth
  title: ''
  type: Authentication
  url: https://developer.pagbank.com.br/v1/docs/dev-autenticacao
- group: other
  title: ''
  type: Environments
  url: https://developer.pagbank.com.br/docs/ambientes-disponiveis
- group: design
  title: ''
  type: Webhooks
  url: https://developer.pagbank.com.br/docs/webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.pagbank.com.br/changelog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/pagseguro
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/10863174/TVetc6HV
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.pagseguro.com/
created: '2026-05-25'
description: PagSeguro (operating consumer-facing under the PagBank brand) is one of Brazil's largest payment processors and digital-banking platforms. Originally spun out of UOL (Universo Online) and listed on the NYSE under PAGS, the company offers an end-to-end financial stack covering online payments, in-person card acceptance via the Moderninha and Minizinha terminal families, Pix instant payments, boleto, credit and debit cards, recurring subscriptions, marketplace split, payouts, account-as-a-service, and a digital bank with cards, credit, and investments. Its developer portal at developer.pagbank.com.br exposes a REST API surface (Orders, Charges, Public Keys, Checkout, Recurring, Connect/OAuth, Account Registration, EDI, Webhooks) backed by official SDKs in PHP, Java, Ruby, and .NET, plus WooCommerce, Magento/Adobe Commerce, and PrestaShop plugins.
finops:
- name: Pagseguro Finops
  service_category: API
  slug: pagseguro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pagseguro.png
layout: provider
modified: '2026-05-25'
name: PagSeguro / PagBank
nav: Providers
network: true
overview: 'PagSeguro / PagBank publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Charges API, Checkout API, and 9 more. Tagged areas include Payments, Checkout, Pix, Boleto, and Cards.


  PagSeguro / PagBank''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, GitHub presence, and 10 more developer resources.'
plans:
- name: Pagseguro Plans Pricing
  plan_count: 2
  slug: pagseguro-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Pagseguro Rate Limits
  slug: pagseguro-rate-limits
score:
  band: thin
  composite: 37.9
  delta: -2.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 41.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 60.5
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pagseguro/refs/heads/main/screenshots/pagseguro-2026-06-20T191324.png
security:
- kind: authentication
  name: Pagseguro Authentication
  slug: pagseguro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pagseguro Domain Security
  slug: pagseguro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pagseguro
tags:
- Payments
- Checkout
- Pix
- Boleto
- Cards
- Subscriptions
- Recurring
- POS
- Card Reader
- Marketplace
- Split
- Payouts
- Digital Bank
- Brazil
- Latin America
- Fintech
website: https://pagbank.com.br/
---
