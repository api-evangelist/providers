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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 13
apis:
- description: The Cielo E-commerce API (also known as Cielo API 3.0) is the company's flagship online payment processing API. It accepts credit cards from Visa, Mastercard, Amex, Elo, Aura, JCB, Diners, Discover, a
  name: Cielo E-commerce API
  slug: cielo-ecommerce-api
- description: Cielo 3DS 2.2 is an EMVCo-compliant cardholder authentication service exposed via the Braspag MPI endpoint. It confirms that the buyer is the legitimate cardholder for card-not-present transactions on
  name: Cielo 3DS 2.2 Authentication API
  slug: cielo-3ds-api
- description: Cielo Pix API exposes the Brazilian Central Bank's instant-payment rails on a Cielo-hosted endpoint. It implements OAuth 2.0 Client Credentials with mutual-TLS, certificate-bound access tokens, and an
  name: Cielo Pix API
  slug: cielo-pix-api
- description: The Cielo Payment Link API lets merchants generate short, shareable payment URLs for sale on social media, WhatsApp, SMS, or email without a full storefront. Authentication uses OAuth 2.0 client crede
  name: Cielo Payment Link API
  slug: cielo-payment-link-api
- description: Cielo Checkout is a hosted payment-page solution that handles credit card, debit, Pix, and boleto flows end-to-end, including PCI scope reduction and post-payment notifications. Merchants generate che
  name: Cielo Checkout API
  slug: cielo-checkout-api
- description: The Cielo Refunds API processes single and batch refund requests against captured transactions. Authentication is OAuth 2.0 Client Credentials issued against a Keycloak realm (MulesoftPRD / MulesoftHM
  name: Cielo Refunds API
  slug: cielo-refunds-api
- description: The Cielo Chargeback API gives merchants programmatic access to dispute lifecycle management. It uses OAuth 2.0 Client Credentials plus mTLS against the cielo-chargeback-sys-external service. Endpoint
  name: Cielo Chargeback API
  slug: cielo-chargeback-api
- description: The Cielo Conciliador API (powered by F360) provides programmatic access to financial reconciliation data including card installments, title installments, customer and supplier lists, and bank stateme
  name: Cielo Conciliador API
  slug: cielo-conciliador-api
- description: The Cielo Promo API lets partner platforms surface merchant promotions and discounts to cardholders. It uses an OAuth 2.0 authorization-code flow with Client-Id and Bearer access tokens. Endpoints cov
  name: Cielo Promo API
  slug: cielo-promo-api
- description: The Cielo LIO (now Cielo Smart) Remote Integration API lets ERP and commercial-automation systems drive payment operations on Cielo's Android POS terminals over the cloud. The platform also supports D
  name: Cielo LIO Remote Integration API
  slug: cielo-lio-remote-api
- description: The Cielo BIN Query service returns metadata for a card BIN (Bank Identification Number) — issuing brand, card type, and additional rules — so e-commerce checkouts can validate the data shoppers enter
  name: Cielo BIN Query API
  slug: cielo-bin-query-api
- description: The Cielo E-Wallets API extends the e-Commerce API with support for digital-wallet payment methods, letting merchants accept Apple Pay, Google Pay, Samsung Pay, and other regional wallets via the same
  name: Cielo E-Wallets API
  slug: cielo-e-wallets-api
- description: 'Cielo Tap on Phone (Cielo Tap) is the company''s SoftPOS solution: it turns an NFC-capable smartphone into a card acceptance device with no separate hardware. Tap on Phone SDKs are distributed through '
  name: Cielo Tap on Phone
  slug: cielo-tap-on-phone
artifact_total: 54
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cielo-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.cielo.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developercielo.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cielo.com.br/
- group: start
  title: ''
  type: Console
  url: https://minhaconta.cielo.com.br/
- group: start
  title: ''
  type: Signup
  url: https://www.cielo.com.br/credenciamento
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cielo.com.br/maquininha-cartao
- group: start
  title: ''
  type: GettingStarted
  url: https://developercielo.github.io/tutorial/
- group: docs
  title: ''
  type: APIReference
  url: https://developercielo.github.io/manual/cielo-ecommerce
- group: operate
  title: ''
  type: Support
  url: https://atendimento.cielo.com.br/
- group: operate
  title: ''
  type: Contact
  url: https://atendimento.cielo.com.br/
- group: other
  title: Investor Relations
  type: Hub
  url: https://ri.cielo.com.br/
- group: company
  title: ''
  type: Blog
  url: https://www.cielo.com.br/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DeveloperCielo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/DeveloperCielo/developercielo.github.io
- group: learn
  title: ''
  type: Tutorials
  url: https://github.com/DeveloperCielo/Tutorial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cielo
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/cielobrasil
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/cielo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cielo.com.br/politica-de-privacidade
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cielo.com.br/termos-de-uso
- group: build
  title: Python SDK (API 3.0)
  type: SDKs
  url: https://github.com/DeveloperCielo/API-3.0-Python
- group: build
  title: PHP Checkout Library
  type: SDKs
  url: https://github.com/DeveloperCielo/CheckoutCielo-Library
- group: build
  title: Python Webservice 1.5 SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/python-cielo-webservice
- group: build
  title: LIO Remote Java SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/LIO-SDK-API-Integracao-Remota-v1-Java
- group: build
  title: LIO Remote Android SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/LIO-SDK-API-Integracao-Remota-v1-Android
- group: build
  title: LIO Remote C# SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/LIO-SDK-API-Integracao-Remota-v1-CSHARP
- group: build
  title: LIO Remote PHP SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/LIO-SDK-API-Integracao-Remota-v1-PHP
- group: build
  title: BIN Query Android SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/cielo-bin-query-android
- group: build
  title: BIN Query iOS SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/cielo-bin-query-ios
- group: build
  title: BIN Query Dart SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/cielo-bin-query-dart
- group: build
  title: Payment Link iOS SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/Link-de-Pagamento-iOS
- group: build
  title: Payment Link Android SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/Link-de-Pagamento-Android
- group: build
  title: Payment Link Dart SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/Link-de-Pagamento-Dart
- group: build
  title: Tap on Phone SDK
  type: SDKs
  url: https://github.com/DeveloperCielo/TapOnPhone
- group: build
  title: EDI Integration Manual
  type: GitHubRepository
  url: https://github.com/DeveloperCielo/EDI
- group: build
  title: Backoffice 3.0 Tutorial
  type: GitHubRepository
  url: https://github.com/DeveloperCielo/Tutorial-Backoffice-3.0
- group: other
  title: E-commerce Best Practices (Luhn / BIN)
  type: BestPractices
  url: https://github.com/DeveloperCielo/Boas-praticas-de-ecommerce
- group: build
  title: Payment Methods Enablement Procedures
  type: GitHubRepository
  url: https://github.com/DeveloperCielo/Habilitacao-meios-de-pagamento
created: '2026-05-25'
description: Cielo is one of the largest Brazilian card acquirers and a publicly traded company (B3:CIEL3), originally formed as a joint venture between Banco Bradesco and Banco do Brasil. The company processes credit, debit, Pix, QR Code, and boleto transactions for hundreds of thousands of merchants across Brazil, providing both in-person acquiring through its family of Cielo Smart (formerly LIO) Android POS terminals and Tap on Phone, and online payment processing through its e-Commerce API, Checkout, Payment Links, and Braspag gateway. Cielo exposes a broad developer surface through developercielo.github.io and the newer docs.cielo.com.br portal, including APIs for sales, queries, tokenization, 3DS 2.2 authentication, Pix with mTLS, chargeback management, refunds, reconciliation (Conciliador), and merchant promotions, along with open-source SDKs in Python, PHP, Java, C#, Kotlin, Swift, and Dart published from the DeveloperCielo GitHub organization.
features:
- One of the largest Brazilian card acquirers, listed on B3 as CIEL3
- Originally a joint venture of Banco Bradesco and Banco do Brasil
- Accepts 80+ card brands, Pix, QR Code, NFC, and boleto
- Family of Cielo Smart (formerly LIO) Android POS terminals (Flash, Smart)
- SoftPOS via Cielo Tap (Tap on Phone) — no separate hardware
- Online acquiring via Cielo e-Commerce API (Cielo API 3.0)
- Hosted Cielo Checkout and Payment Links for low-code acceptance
- 3DS 2.2 authentication via Braspag MPI with liability shift
- Tokenization and recurring payments via the e-Commerce API
- Pix via OAuth 2.0 with certificate-bound tokens and mTLS
- Programmatic chargeback and refund lifecycle management
- Financial reconciliation via Cielo Conciliador (F360-powered)
- Promotion distribution to cardholders via Cielo Promo
- Braspag-powered Gateway, Payment Split, and Risk Management
- Pre-built connectors for major Brazilian e-commerce platforms
- Open-source SDKs across Python, PHP, Java, C#, Kotlin, Swift, Dart
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cielo.png
integrations:
- description: Founding shareholder; Bradesco distribution channels onboard Cielo to their merchant base.
  name: Banco Bradesco
- description: Founding shareholder; co-acquires and refers merchants from the Banco do Brasil network.
  name: Banco do Brasil
- description: Cielo subsidiary providing the Gateway de Pagamento, Payment Split, Risk Management, and 3DS 2.2 MPI used across Cielo's APIs.
  name: Braspag
- description: Powers the Cielo Conciliador reconciliation API exposed at financas.f360.com.br.
  name: F360
- description: Underlying instant-payments rail that the Cielo Pix API surfaces to merchants and platforms.
  name: Banco Central do Brasil (BCB) Pix
- description: Card schemes accepted across Cielo e-Commerce, Checkout, and POS terminals (80+ brands total).
  name: Visa, Mastercard, Elo, Amex, Hipercard
- description: Digital wallets supported via the Cielo E-Wallets API and Tap on Phone.
  name: Apple Pay, Google Pay, Samsung Pay
- description: Pre-built e-commerce connectors documented on docs.cielo.com.br for major Brazilian commerce platforms.
  name: VTEX, Magento, WooCommerce, Shopify-style platforms
layout: provider
modified: '2026-05-25'
name: Cielo
nav: Providers
network: true
overview: 'Cielo publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Acquiring, Fintech, Brazil, and Point of Sale.


  Cielo''s developer surface includes developer portal, documentation, developer console, signup flow, pricing, getting-started guide, API reference, and 32 more developer resources.'
random_paper: 50
score:
  band: emerging
  composite: 26.3
  delta: -3.4
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cielo/refs/heads/main/screenshots/cielo-2026-06-20T174344.png
security:
- kind: domain-security
  name: Cielo Domain Security
  slug: cielo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cielo
solutions:
- description: API-first online acquiring stack including the e-Commerce API, Checkout, Payment Links, 3DS, BIN Query, and E-Wallets.
  name: Cielo e-Commerce
- description: Android POS hardware and software platform supporting local, deep-link, and remote integration models.
  name: Cielo Smart (LIO)
- description: SoftPOS / Tap on Phone solution turning NFC smartphones into card acceptance devices.
  name: Cielo Tap
- description: Cielo's enterprise gateway brand providing advanced acquiring, payment split, and risk-management services.
  name: Braspag
- description: Promotion distribution channel exposing merchant discounts to consumer-facing partner apps.
  name: Cielo Promo
- description: Reconciliation and back-office reporting platform powered by F360.
  name: Cielo Conciliador
tags:
- Payments
- Acquiring
- Fintech
- Brazil
- Point of Sale
- Card Processing
use_cases:
- description: Brick-and-mortar merchants accept credit, debit, Pix, and contactless payments through Cielo Smart Android POS terminals (formerly LIO) with local, deep-link, or remote integration.
  name: In-Person Card Acceptance
- description: Micro-entrepreneurs and field sales reps accept contactless card payments directly on their NFC-capable smartphones via Cielo Tap, without renting a dedicated POS device.
  name: SoftPOS / Tap on Phone
- description: E-commerce platforms use the Cielo e-Commerce API (API 3.0) to authorize, capture, void, and tokenize card transactions on Visa, Mastercard, Elo, Amex, Hipercard, and more.
  name: Online Card Acquiring
- description: Merchants with limited engineering capacity use Cielo Checkout or Payment Links to accept payments via shareable URLs on WhatsApp, Instagram, and SMS without building a storefront.
  name: Hosted Checkout and Payment Links
- description: Platforms generate immediate and recurring Pix charges, receive real-time settlement events via webhooks, and issue refunds through the Pix API with mTLS-secured access.
  name: Pix Charges and Refunds
- description: Online merchants reduce chargeback exposure by routing card-not-present transactions through Cielo's Braspag MPI for liability-shifted authentication.
  name: 3DS 2.2 Authentication
- description: Operations teams query, accept, refuse, and document chargebacks and process refunds in bulk via dedicated APIs with letter-generation and evidence-download endpoints.
  name: Dispute and Refund Management
- description: Finance teams reconcile sales, fees, and settlement events using the Cielo Conciliador API (F360) to pull card and title installments, bank statements, and parameterised reports.
  name: Financial Reconciliation
- description: Subscription businesses save card-on-file via Cielo's tokenization endpoints and bill on a recurring schedule with Zero Auth validation between charges.
  name: Recurring Payments and Tokenization
- description: Partner apps and fintechs surface enrolled merchant discounts to cardholders through the Cielo Promo API, retrieving promotion lists, establishment data, and cardholder transaction history.
  name: Merchant Promotion Distribution
website: https://developercielo.github.io/
---
