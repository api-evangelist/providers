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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-03'
api_count: 20
apis:
- description: Create, retrieve, update, list, and delete customers ("clientes"). The Customer object holds personal/business identifiers (CPF/CNPJ), contact details, address, default notification preferences, and S
  name: Asaas Customers API
  slug: customers
- description: Core billing endpoint for creating individual charges payable by Boleto, Pix, Credit Card, Debit Card, or "undefined" (let the payer choose). Supports capture, refund, partial refund, anticipation, fi
  name: Asaas Charges (Cobranças) API
  slug: charges
- description: Recurring-billing subscriptions with weekly, biweekly, monthly, bimonthly, quarterly, semiannual, and annual cycles. Supports end-date or open-ended schedules, automatic charge generation per cycle, v
  name: Asaas Subscriptions API
  slug: subscriptions
- description: Generate a fixed series of installment charges from a single installment plan - typical for splitting a total amount across N monthly boletos or credit-card charges.
  name: Asaas Installments (Parcelamentos) API
  slug: installments
- description: Endpoints for Pix instant payments - static and dynamic QR codes, Pix keys (CPF/CNPJ/email/phone/random), QR code decoding, transfer via Pix, and the new Pix Automático (recurring authorized Pix debit
  name: Asaas Pix API
  slug: pix
- description: Issue, retrieve, and reconcile Brazilian boleto bancário (bank slip) charges, with configurable fines, interest, discounts, and due-date updates. Includes a webhook event for cancellation of expired s
  name: Asaas Boleto API
  slug: boleto
- description: Tokenize credit cards client-side and process card charges server-side, including pre-authorization (capture later), capture, refund, and 3DS challenge handling. Supports recurring use of tokenized ca
  name: Asaas Credit Card API
  slug: credit-card
- description: Hosted checkout sessions that bundle one or more products / charges into a shareable payment URL. Supports multiple billing types, tax-document collection, and post-payment redirection.
  name: Asaas Checkout API
  slug: checkout
- description: Generate reusable payment links ("links de pagamento") for one-off or recurring collection over WhatsApp, SMS, email, or social. Each link can carry a fixed or buyer-defined amount.
  name: Asaas Payment Links API
  slug: payment-links
- description: Configure split rules on a charge so that the net amount is automatically distributed across one or more wallet IDs at settlement time - the basis for marketplaces and platforms built on Asaas.
  name: Asaas Split Payments API
  slug: split-payments
- description: 'Move funds out of the Asaas digital account: TED to external banks, Pix transfers to keys or banking details, and internal transfers between Asaas accounts, with optional scheduling.'
  name: Asaas Transfers API
  slug: transfers
- description: Pay external bills (boletos, concessionárias, GPS, DARF) from the Asaas digital account, with barcode-line lookup and scheduled execution.
  name: Asaas Bill Payments API
  slug: bill-payments
- description: Anticipate future receivables - boleto, card, and Pix - to receive funds before the original settlement date in exchange for a discount fee. Endpoints simulate, request, and list anticipations.
  name: Asaas Anticipations (Antecipação) API
  slug: anticipations
- description: Create and manage subaccounts under a master account for white-label and BaaS use cases. Supports KYC document submission, activation links, per-subaccount API keys, and consolidated reporting.
  name: Asaas Subaccounts / White-Label API
  slug: subaccounts
- description: Schedule, issue, and retrieve Brazilian electronic invoices (NFS-e) automatically tied to a charge or subscription, including municipal configuration and tax retention setup.
  name: Asaas Invoices (Nota Fiscal) API
  slug: invoices
- description: Hold funds in escrow ("contas de garantia") until a release condition is met, with API-driven release or refund. Common in marketplaces where buyer-protection windows are required.
  name: Asaas Escrow Accounts API
  slug: escrow
- description: Retrieve and dispute credit-card chargebacks, including evidence upload and status retrieval.
  name: Asaas Chargebacks API
  slug: chargebacks
- description: Retrieve the current account balance and the financial statement (extrato) of credits and debits for the Asaas digital account.
  name: Asaas Account Balance & Statement API
  slug: account-balance
- description: Top up Brazilian prepaid mobile lines by carrier and amount, debiting the Asaas account balance.
  name: Asaas Cell Phone Recharge API
  slug: cell-phone-recharge
- description: Event-driven HTTP callbacks for payment, subscription, transfer, anticipation, chargeback, account, and invoice events. Webhooks require a token (auto-generated as of Feb 2026) and Asaas signs request
  name: Asaas Webhooks API
  slug: webhooks
artifact_total: 45
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asaas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asaas.com/
- group: start
  title: ''
  type: Signup
  url: https://www.asaas.com/cadastro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.asaas.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.asaas.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.asaas.com/docs/visao-geral
- group: auth
  title: ''
  type: Authentication
  url: https://docs.asaas.com/docs/autenticacao-no-asaas
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.asaas.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.asaas.com/changelog
- group: other
  title: ''
  type: BreakingChanges
  url: https://docs.asaas.com/docs/breaking-changes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.asaas.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.asaas.com/precos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asaas.com/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asaas.com/politica-de-privacidade
- group: operate
  title: ''
  type: Support
  url: https://central.ajuda.asaas.com/hc/pt-br
- group: operate
  title: ''
  type: HelpCenter
  url: https://central.ajuda.asaas.com/hc/pt-br
- group: company
  title: ''
  type: Blog
  url: https://blog.asaas.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.asaas.com/llms.txt
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/asaas
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/asaas/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/asaas/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@asaas
created: '2026-05-25'
description: Asaas is a Brazilian financial-services and payments platform headquartered in Joinville, SC. It operates as a Banco Central-authorized payment institution and simplified credit company (SCD), offering small and medium businesses a digital account ("Conta Asaas") combined with collection, billing, and receivables tooling. The Asaas API (v3) at api.asaas.com is a REST/JSON surface covering Customers, Charges (Cobranças), Subscriptions, Installments, Pix (including Pix Automático recurring), Boleto, Credit Card, Checkout sessions, Payment Links, Split Payments, Transfers, Bill Payments, Anticipation of Receivables, Subaccounts / White-label, Invoices (Nota Fiscal), Escrow, Chargeback handling, Webhooks, and supporting services like Serasa default reporting, cell-phone recharges, and SMS / WhatsApp / email notifications. A full sandbox at sandbox.asaas.com, an Atlassian-hosted status page, a Discord developer community, and an llms.txt-indexed documentation site round out the developer
  experience. Asaas does not publish a first-party SDK on a GitHub org; the ecosystem is served by third-party community SDKs in Node.js, PHP, Python, Go, and Ruby plus e-commerce plugins for WooCommerce, Magento, and Nuvemshop.
features:
- description: Free monthly Conta Asaas with Mastercard debit card and unlimited internal transfers, positioned as a banking layer for SMBs.
  name: Digital Account
- description: Recurring authorized Pix debits for subscription-style billing in BRL, publicly released January 2026 alongside webhook support.
  name: Pix Automático
- description: Native marketplace splitting that distributes settled funds across multiple wallet IDs per charge.
  name: Split Payments
- description: On-demand or automatic anticipation of boleto, card, and Pix receivables against a discount fee.
  name: Anticipation of Receivables
- description: Create and KYC subaccounts via API for white-label and BaaS platforms; each subaccount has its own API key.
  name: White-Label Subaccounts
- description: Built-in notification engine over SMS, email, WhatsApp, and voice bot to chase overdue invoices; Asaas advertises ~80% default reduction.
  name: Automated Dunning
- description: Funds-in-guarantee accounts release on API-driven conditions for marketplace buyer protection.
  name: Escrow Accounts
- description: Schedule and issue Brazilian municipal NFS-e tied to a charge or subscription with tax-retention configuration.
  name: NFS-e Issuance
- description: Optional default reporting and credit-score lookups via Serasa tied to customer records.
  name: Serasa Reporting
- description: Full-feature sandbox.asaas.com environment for end-to-end integration testing before production.
  name: Sandbox
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asaas.png
integrations:
- description: Official Asaas plugin for WordPress / WooCommerce stores.
  name: WooCommerce
- description: Asaas extension for Magento 2 storefronts.
  name: Magento
- description: Native Asaas integration for Nuvemshop / Tiendanube Brazilian merchants.
  name: Nuvemshop
- description: No-code automation marketplace with Asaas triggers and actions for connecting to hundreds of SaaS tools.
  name: Pluga
- description: Community Zapier integrations bridge Asaas events to thousands of downstream apps.
  name: Zapier
layout: provider
modified: '2026-05-25'
name: Asaas
nav: Providers
network: true
overview: 'Asaas publishes 20 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Billing, Subscriptions, Pix, and Boleto.


  Asaas'' developer surface includes signup flow, documentation, API reference, getting-started guide, authentication, sandbox, changelog, and 15 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 27.9
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asaas/refs/heads/main/screenshots/asaas-2026-06-20T172451.png
security:
- kind: domain-security
  name: Asaas Domain Security
  slug: asaas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asaas
solutions:
- description: Free Brazilian digital account with debit card targeted at MEIs and SMBs.
  name: Conta Asaas (Digital Account)
- description: The core billing product covering boleto, Pix, and card via a single API and UI.
  name: Cobranças (Charges)
- description: Subaccount-based product for partners building branded payments experiences on top of Asaas.
  name: Whitelabel / BaaS
- description: Checkout / payment-link product for accepting payments without a full integration.
  name: Asaas Pay
tags:
- Payments
- Billing
- Subscriptions
- Pix
- Boleto
- Credit Card
- Checkout
- Split Payments
- Webhooks
- Digital Account
- Receivables
- Invoicing
- Brazil
- Fintech
- SMB
use_cases:
- description: Subscriptions API plus Pix Automático, boleto, or card to bill Brazilian SaaS customers in BRL with automated dunning.
  name: Recurring SaaS Billing
- description: Split Payments + Subaccounts + Escrow let marketplaces collect, hold, and disburse to sellers natively in BRL.
  name: Marketplace Settlement
- description: Service businesses (clinics, schools, gyms) automate billing, NFS-e issuance, and overdue-payment chasing via the Asaas dunning engine.
  name: Service-Business Collections
- description: ISVs embed Asaas under their brand using Subaccounts, KYC, and per-account API keys to ship a payments product without a banking stack.
  name: White-Label / BaaS
- description: Checkout sessions and payment links plug into custom storefronts and supported plugins for one-click Pix / boleto / card.
  name: E-commerce Checkout
website: https://www.asaas.com/
---
