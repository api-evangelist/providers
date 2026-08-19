---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 17
apis:
- description: Create, list, retrieve, and manage orders — the top-level payment object in the Pagar.me Core API v5. Each order can contain one or more charges paid via credit card, debit card, Pix, boleto, voucher,
  name: Pagar.me Orders API
  slug: pagarme-orders-api
- description: Manage individual charges (cobranças) — the unit of capture inside an order. Get a charge, edit its payment method or saved card, capture a pre-authorized amount, refund all or part of it, and inspect
  name: Pagar.me Charges API
  slug: pagarme-charges-api
- description: Create and manage end-customer (buyer) records — personal data, CPF/CNPJ, contact info, and addresses — so that orders, subscriptions, and saved cards can be tied to a stable customer identity. Underp
  name: Pagar.me Customers API
  slug: pagarme-customers-api
- description: Tokenize, save, and edit credit/debit cards inside a Pagar.me customer wallet, off-load PCI scope, and reuse cards for one-click buy and recurring charges. Supports network token (token de bandeira) i
  name: Pagar.me Cards API
  slug: pagarme-cards-api
- description: Define reusable recurring billing plans — pricing, billing cycle (days/weeks/months), trial period, installment count, accepted payment methods, and items — to back subscription products. Plans are th
  name: Pagar.me Plans API
  slug: pagarme-plans-api
- description: Create customer subscriptions either from a saved plan or as standalone (avulsa) subscriptions, renew billing cycles, edit payment method / card / discount / minimum price, change items, and inspect e
  name: Pagar.me Subscriptions API
  slug: pagarme-subscriptions-api
- description: Onboard and manage recipients (recebedores) — the sub-merchants that receive split payments in a marketplace. Create the recipient, run the KYC / prova de vida flow, attach bank accounts, configure au
  name: Pagar.me Recipients API
  slug: pagarme-recipients-api
- description: Create, cancel, list, and retrieve transfers from a recipient's Pagar.me balance to their registered bank account, plus pull the official transfer receipt (comprovante). Pair with the Withdrawals obje
  name: Pagar.me Transfers API
  slug: pagarme-transfers-api
- description: Inspect the per-recipient balance ledger — every credit, debit, fee, refund, chargeback, anticipation, transfer, and adjustment that moves money in or out of a Pagar.me account. The canonical source o
  name: Pagar.me Balance Operations API
  slug: pagarme-balance-operations-api
- description: List the merchant's future receivables — the installments of credit-card sales that will settle over the coming weeks and months. The basis for cash-flow forecasting and for any anticipation simulatio
  name: Pagar.me Receivables API
  slug: pagarme-receivables-api
- description: Anticipate receivables (antecipação) — Pagar.me's working-capital product that lets a merchant or marketplace recipient pull future credit-card installments to today's balance for a fee. Supports spot
  name: Pagar.me Anticipation API
  slug: pagarme-anticipation-api
- description: 'Retrieve settlements (pagamentos) — the actual money movements out of Pagar.me to recipients — individually, in bulk, or scoped to a specific recipient. Closes the loop between the Balance Operations '
  name: Pagar.me Settlements API
  slug: pagarme-settlements-api
- description: 'List and retrieve disputes (disputas) and chargebacks raised against the merchant''s transactions, including the new chargeback-specific charge status. Lets risk and finance teams reconcile losses and '
  name: Pagar.me Disputes & Chargebacks API
  slug: pagarme-disputes-api
- description: Generate, list, retrieve, activate, and cancel payment links — short URLs that wrap a Pagar.me Checkout for sale-by-link, WhatsApp commerce, Instagram bio links, and lightweight invoicing. Includes th
  name: Pagar.me Payment Links API
  slug: pagarme-payment-links-api
- description: Manage contract effects and Unidades de Recebíveis (URs) under the Brazilian Central Bank's Resoluções BCB 264 and 349 receivables-registry regime. List contract effects, contest a contract, list cont
  name: Pagar.me Contracts & URs API
  slug: pagarme-contracts-api
- description: Subscribe to and receive signed webhook events for every meaningful state change on Pagar.me — order.paid, charge.captured, charge.refunded, subscription.created, recipient.kyc_updated, dispute.opened
  name: Pagar.me Webhooks API
  slug: pagarme-webhooks-api
- description: Pagar.me's drop-in hosted Checkout. Embed Pagar.me's PCI-compliant payment form to take credit card, Pix, and boleto for one-off orders and subscriptions, with first-class AI/agent integration pattern
  name: Pagar.me Hosted Checkout
  slug: pagarme-checkout-pagarme
artifact_total: 54
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pagar-me-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://pagar.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pagar.me
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pagar.me/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pagar.me/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pagar.me/reference/getting-started-with-your-api
- group: auth
  title: ''
  type: Authentication
  url: https://docs.pagar.me/docs/chaves-de-acesso
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.pagar.me/reference/rate-limit
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pagar.me/reference/segurança-1
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pagar.me/docs/ip-allowlist
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pagar.me/llms.txt
- group: start
  title: ''
  type: Console
  url: https://id.pagar.me/signin
- group: start
  title: ''
  type: Signup
  url: https://www.pagar.me/ofertas
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pagar.me/ofertas
- group: operate
  title: ''
  type: Support
  url: https://pagarme.helpjuice.com/
- group: company
  title: ''
  type: Blog
  url: https://pagar.me/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pagarme
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/pagarme-nodejs-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/pagarme-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/pagarme-php-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/pagarme-ruby-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/pagarme-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/pagarme-net-standard-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/pagarme-core-api-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pagarme/node-boleto
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pagar.me/page/guias-pagarme
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pagar.me/docs/autenticação-via-3ds
created: '2026-05-25'
description: Pagar.me is the API-first online payments platform from Stone Co., one of Brazil's largest financial technology companies. Often called "the Stripe of Brazil," Pagar.me provides Brazilian e-commerce merchants, marketplaces, SaaS companies, and subscription businesses with a single REST API and a set of official SDKs to accept credit and debit cards, Pix instant payments, boletos, vouchers, and digital wallets, with built-in 3DS 2.0 anti-fraud, payment splitting and recipient management for marketplaces, recurring billing through plans and subscriptions, anticipation of receivables, payment links, an embedded Checkout, and signed webhooks. The Pagar.me Core API v5 (2021-09-01) is the current stable surface, exposed at https://api.pagar.me/core/v5 with HTTP Basic authentication, and is backed by SDKs in Node.js, Python, PHP, Ruby, Java, .NET, and Go. Pagar.me is PCI DSS Level 1 certified and powers payments for Brazilian brands including Leroy Merlin, Casa & Vídeo, Polishop, Usaflex,
  and Catarse.
features:
- description: Credit and debit cards across all major Brazilian brands, Pix (instant), boleto bancário (including DDA), private label cards, vouchers, and digital wallets — all behind a single Orders/Charges API.
  name: Brazilian payment methods, first-class
- description: First-class recipients (recebedores), KYC / prova de vida, sub-merchant management, and configurable split rules per charge or order — the backbone of every Brazilian marketplace built on Pagar.me.
  name: Marketplace split payments and recipients
- description: Plans + Subscriptions API for SaaS, streaming, education, and club-of-the-month businesses, including standalone (avulsa) subscriptions, cycle renewal, plan editing, and one-click-buy via the customer wallet.
  name: Recurring billing
- description: Built-in fraud screening and 3DS 2.0 challenge flows (including a HUB integration manual and v1-to-v2 migration guide) to reduce chargebacks and meet card-network mandates.
  name: Anti-fraud with 3DS 2.0
- description: Working-capital product that lets the merchant pull tomorrow's credit-card installments to today's balance via the Anticipation API, with limits inspection and spot simulation.
  name: Anticipation of receivables
- description: PCI-scoped tokenization, network tokens (token de bandeira), and the Card Updater service that automatically refreshes cards on file when issuers re-issue them — keeping subscription cohorts alive.
  name: Tokenization and Card Updater
- description: Drop-in PCI-compliant payment form plus shareable payment links for sale-by-link, WhatsApp commerce, and Instagram-bio commerce. Documented "Checkout Skills" for AI-assisted integration.
  name: Hosted Checkout and Payment Links
- description: First-party modules for Magento 2 / Adobe Commerce, WooCommerce, VTEX, Nuvemshop, and Shopify that wrap the Core API behind a click-to-install plugin.
  name: E-commerce platform modules
- description: Signed webhook events for every order, charge, subscription, recipient, and dispute state change — the asynchronous spine of any production integration.
  name: Webhooks with signature verification
- description: Native support for the Brazilian Central Bank's receivables-registry regime — contract effects, contests, and Unidades de Recebíveis (URs) per recipient.
  name: Receivables registry compliance (Res 264/349)
- description: Pagar.me holds the highest PCI DSS Level 1 certification, so merchants can tokenize and store cards through Pagar.me and stay out of full PCI scope themselves.
  name: PCI DSS Level 1
- description: Maintained Node.js/TypeScript, Python, PHP, Ruby, Java, .NET Standard, and Go SDKs generated from the Core API v5 spec, all published from the pagarme GitHub org.
  name: Official SDKs in seven languages
- description: A documented llms.txt index, OpenAPI-formatted reference, and "Checkout Skills" patterns explicitly aimed at Claude Code, Codex, Cursor, and Copilot users wiring Pagar.me into agents and coding assistants.
  name: AI-assistant-friendly docs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pagar-me.png
integrations:
- description: Pagar.me is Stone Co.'s API-driven online payments brand; the two share regulatory infrastructure, anti-fraud rails, and the Stone API migration path documented in Pagar.me's release notes.
  name: Stone Co.
- description: Official Magento 2 module (github.com/pagarme/magento2) with full installation, configuration, and feature-activation documentation.
  name: Magento 2 / Adobe Commerce
- description: Official WooCommerce plugin (github.com/pagarme/woocommerce) with dashboard, payment methods, and feature-activation documentation.
  name: WooCommerce
- description: Pagar.me connector for VTEX, including marketplace seller flows, private-label card registration, and feature activation.
  name: VTEX
- description: Pagar.me Nuvemshop app for Brazilian SMB merchants — install via the Nuvemshop app store and configure from the Pagar.me dashboard.
  name: Nuvemshop
- description: Integration guide and feature-activation flow for using Pagar.me as a payment provider inside Shopify stores serving Brazilian buyers.
  name: Shopify
- description: Accept Google Pay payments on Brazilian Android devices through the same Orders / Charges surface, documented as a first-class payment method.
  name: Google Pay
- description: Native integration with Pix, Brazil's central-bank-run instant payment system, including a Pix simulator for testing.
  name: Pix (Brazilian Central Bank)
- description: Documented brand-specific behavior — Amex business model identifiers, Visa/Elo recurring IDs for external subscriptions, Visa capture deadlines, MCC validation rules, and brand retry programs.
  name: Card networks (Visa, Mastercard, Elo, Amex, Hipercard)
- description: Pagar.me HUB and direct 3DS 2.0 integration manuals for card-not-present authentication.
  name: 3DS 2.0
- description: First-class docs for integrating Pagar.me with Claude Code, Codex, Cursor, and Copilot via the llms.txt index and Checkout Skills.
  name: AI coding assistants
layout: provider
modified: '2026-05-25'
name: Pagar.me
nav: Providers
network: true
overview: 'Pagar.me publishes 17 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Financial Services, Fintech, Brazil, and Latin America.


  Pagar.me''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, developer console, signup flow, and 20 more developer resources.'
random_paper: 33
score:
  band: thin
  composite: 27.0
  delta: 0.7
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 81.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 26.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pagar-me/refs/heads/main/screenshots/pagar-me-2026-06-20T191321.png
security:
- kind: domain-security
  name: Pagar Me Domain Security
  slug: pagar-me-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: pagar-me
solutions:
- description: Hosted Checkout, Payment Links, and pre-built platform modules for merchants who want to accept Brazilian payments without writing API code.
  name: Pronto para usar (Ready-made)
- description: Direct Core API v5 + official SDK integration for marketplaces, SaaS billing, and high-volume merchants that need full control over the order, charge, split, and recurring lifecycles.
  name: Customizado (Custom)
- description: Complete checkout-to-settlement stack — Orders, Charges, Customers, Cards, anti-fraud, and hosted Checkout — for Brazilian online stores.
  name: E-commerce
- description: Recurring billing for SaaS, streaming, education, and club-of-the-month businesses on top of Plans, Subscriptions, the customer wallet, and the Card Updater.
  name: Subscriptions
- description: Recipients, KYC, split rules, transfers, and Res 264/349 receivables-registry support for multi-vendor Brazilian marketplaces.
  name: Marketplace
tags:
- Payments
- Financial Services
- Fintech
- Brazil
- Latin America
- Stone Co
- Pix
- Boleto
- Credit Card
- Marketplace
- Split Payments
- Subscriptions
- Recurring Billing
- Anti-Fraud
- 3DS
- Checkout
- Payment Links
- Webhooks
- E-commerce
- Anticipation
use_cases:
- description: Accept credit card, Pix, and boleto on a Brazilian online store via the Orders API, the hosted Checkout, or one of the platform modules (Magento, WooCommerce, VTEX, Nuvemshop, Shopify).
  name: Brazilian e-commerce checkout
- description: Onboard sellers as recipients, run KYC, configure split rules, and have Pagar.me settle each sub-merchant's share into their own bank account.
  name: Marketplace with payment splitting
- description: Charge recurring credit-card or Pix subscriptions through Plans and Subscriptions, with automatic retry, card updating, and chargeback handling.
  name: Subscription and SaaS billing
- description: Generate Pagar.me Payment Links and share them on WhatsApp, Instagram, or email for no-website-needed sales.
  name: Sale-by-link / social commerce
- description: Used by Brazilian crowdfunding platforms (e.g. Catarse) to collect pledges across multiple payment methods and split funds among project recipients.
  name: Crowdfunding and donations
- description: Anticipate receivables to convert credit-card installments into immediate cash to fund inventory, payroll, or marketing.
  name: Working-capital advance
- description: Wire Pagar.me into AI coding assistants and agents (Claude Code, Codex, Cursor, Copilot) using the documented llms.txt index and the Checkout Skills for orders and subscriptions.
  name: AI agents that take payments
website: https://pagar.me
---
