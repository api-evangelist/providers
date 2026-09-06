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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.7
  scored_at: '2026-09-05'
api_count: 20
apis:
- description: Core Payments API on the AstroPay platform for creating, retrieving, and managing payment transactions across the AstroPay wallet network and supported local payment methods. Backs merchant pay-in flo
  name: AstroPay Payments API
  slug: astropay-payments-api
- description: Payout API on the AstroPay platform for sending funds to AstroPay wallets, bank accounts, and other supported destinations. Used for marketplace seller payouts, gaming withdrawals, payroll disbursemen
  name: AstroPay Payout API
  slug: astropay-payout-api
- description: PIX integration on the AstroPay platform for Brazil's instant payment rail. Create PIX charges, receive PIX payments, and issue PIX payouts backed by AstroPay's local Brazilian licensing.
  name: AstroPay PIX API
  slug: astropay-pix-api
- description: Cards Management API for programmatic issuance and lifecycle management of AstroPay virtual and physical prepaid cards. Used by businesses to issue branded cards to employees, contractors, marketplace
  name: AstroPay Cards Management API
  slug: astropay-cards-management-api
- description: Users Management API for creating and managing platform users associated with a merchant or partner account, including KYC linkage and access control to AstroPay platform resources.
  name: AstroPay Users Management API
  slug: astropay-users-management-api
- description: User Account Management API for managing the financial accounts attached to a platform user, including multicurrency balances, statements, and account settings.
  name: AstroPay User Account Management API
  slug: astropay-user-account-management-api
- description: Scheme Transfers API for moving funds across AstroPay accounts and between schemes inside the AstroPay network, supporting wallet-to-wallet transfers and internal book transfers.
  name: AstroPay Scheme Transfers API
  slug: astropay-scheme-transfers-api
- description: Savings Account API for creating and managing interest-bearing savings accounts attached to AstroPay platform users.
  name: AstroPay Savings Account API
  slug: astropay-savings-account-api
- description: Settlements API for retrieving merchant settlement files, reconciling settled transactions, and downloading settlement reports across the AstroPay platform.
  name: AstroPay Settlements API
  slug: astropay-settlements-api
- description: Tokenizer API and SDKs (iOS and Android) for PCI-compliant collection of sensitive card data. Cards are tokenized client-side and the token is used in server-to-server payment requests, reducing PCI s
  name: AstroPay Tokenizer API
  slug: astropay-tokenizer-api
- description: Partners Services API for integrators and partner platforms to manage sub-merchants, services, and partner-scoped resources on the AstroPay platform.
  name: AstroPay Partners Services API
  slug: astropay-partners-services-api
- description: Direct Payment API for processing local pay-ins via the AstroPay payment processing rail. Supports Brazil and Mexico with local payment methods (PIX, Boleto, OXXO, SPEI) for merchants integrating with
  name: AstroPay Direct Payment API
  slug: astropay-direct-payment-api
- description: Direct Withdrawal API for processing local payouts and withdrawals into bank accounts across Argentina, Brazil, Chile, India, and Peru. Used by marketplaces, gaming operators, and other payout-heavy b
  name: AstroPay Direct Withdrawal API
  slug: astropay-direct-withdrawal-api
- description: Accept AstroPay Checkout — a hosted and embedded payment acceptance flow that lets merchants accept AstroPay wallet payments alongside local payment methods. Supports offsite (redirect), embedded (ifr
  name: AstroPay Checkout API
  slug: astropay-checkout-api
- description: 'QR Payments API for in-person and point-of-sale acceptance. Includes a Payment Code API (create, update, status, exchange rate) and a POS API (create, get, search) for issuing QR codes that customers '
  name: AstroPay QR Payments API
  slug: astropay-qr-payments-api
- description: Wallet-on-File API for linking an AstroPay wallet to a merchant account so funds can be pulled in one-click for recurring purchases. Covers account linking (including singular generator), partner bran
  name: AstroPay Wallet-on-File API
  slug: astropay-wallet-on-file-api
- description: Wallet Payouts / Cashouts v1 API for sending payouts to AstroPay wallet holders, including closed-loop transactions back to the originating wallet. Supports merchant onboarding, status checks, and cal
  name: AstroPay Cashouts API
  slug: astropay-cashouts-api
- description: Transaction Report API exposing merchant balance and transaction export endpoints for reconciliation, accounting, and reporting across both the Accept AstroPay and Payment Processing surfaces.
  name: AstroPay Transaction Report API
  slug: astropay-transaction-report-api
- description: Platform-wide webhook callback system for AstroPay. Webhooks are signed and delivered for asynchronous payment, payout, card, wallet-on-file, and account events across the entire AstroPay platform.
  name: AstroPay Webhooks
  slug: astropay-webhooks
- description: Pre-built integrations that drop AstroPay acceptance into popular e-commerce platforms without custom development. Shopify is the first supported platform, with additional plugins in development.
  name: AstroPay E-Commerce Plugins
  slug: astropay-ecommerce-plugins
artifact_total: 48
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astropay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astropay.com
- group: start
  title: ''
  type: Portal
  url: https://developers.astropay.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.astropay.com/docs/platform/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.astropay.com/docs/platform/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://developers.astropay.com/docs/platform/authentication
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.astropay.com/docs/platform/errors-codes
- group: design
  title: ''
  type: Webhooks
  url: https://developers.astropay.com/docs/platform/callbacks/webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.astropay.com/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.astropay.com
- group: operate
  title: ''
  type: Support
  url: https://business-support.astropay.com/
- group: operate
  title: ''
  type: Help
  url: https://app.astropay.com/help
- group: operate
  title: ''
  type: Contact
  url: https://developers.astropay.com/contact/
- group: start
  title: ''
  type: Signup
  url: https://business.astropay.com
- group: other
  title: ''
  type: Personal
  url: https://www.astropay.com/personal
- group: other
  title: ''
  type: Business
  url: https://www.astropay.com/business
- group: company
  title: ''
  type: Blog
  url: https://www.astropay.com/blog
- group: company
  title: ''
  type: Careers
  url: https://astropay.careers.hibob.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astropay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/astropay
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/astropayglobal
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AstroPayGlobal
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/astropayglobal/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/astropay
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@astropayglobal
- group: build
  title: ''
  type: SDKs
  url: https://developers.astropay.com/docs/platform/tokenizer/ios-sdk/getting-started
- group: build
  title: ''
  type: SDKs
  url: https://developers.astropay.com/docs/platform/tokenizer/android-sdk/getting-started
- group: build
  title: ''
  type: SDKs
  url: https://developers.astropay.com/docs/accept-astropay/checkout/private/payments-lib-react-native/getting-started
- group: build
  title: ''
  type: Plugins
  url: https://developers.astropay.com/docs/accept-astropay/ecommerce-plugins/shopify
created: '2026-05-24'
description: AstroPay is a Uruguay-founded fintech and electronic money institution offering a multicurrency wallet, virtual and physical AstroCards, FX, and cross-border money transfers for consumers across Latin America, plus a business platform that lets merchants accept payments, issue cards, manage payroll, and pay out to wallets and bank accounts. AstroPay is regulated as an EMI in the UK, Denmark, Isle of Man, and Brazil, and operates the AstroPay wallet across Argentina, Brazil, Chile, Mexico, Peru, Colombia, Uruguay, and additional global corridors with support for ARS, BRL, CLP, COP, EUR, GBP, MXN, PEN, USD, USDT, and UYU. For developers, AstroPay exposes a comprehensive REST platform spanning payments, payouts, PIX instant payments in Brazil, issued cards, savings accounts, scheme transfers, user account management, tokenization (PCI-compliant card collection), settlements, transaction reporting, hosted and embedded Checkout, QR-code POS, Wallet-on-File account linking, Cashouts,
  and Webhooks — accessed through `developers.astropay.com` with HMAC-signed callbacks and an OAuth/API-key authentication model.
features:
- AstroPay multicurrency wallet across LatAm and global corridors (ARS, BRL, CLP, COP, EUR, GBP, MXN, PEN, USD, USDT, UYU)
- AstroCard virtual and physical prepaid cards with global acceptance
- Currency exchange and FX with Infinite-tier preferential rates
- Cross-border money transfers to bank accounts worldwide
- Local pay-in via PIX, Boleto, OXXO, SPEI, and other LatAm payment methods
- Local payout/withdrawal rails in Argentina, Brazil, Chile, Peru, and India
- Accept AstroPay Checkout — hosted, embedded (iframe/web component), and React Native integration modes
- QR Payments with POS API and Payment Code API for in-person acceptance
- Wallet-on-File one-click recurring purchases via account linking
- Cards-as-a-Service issuing for businesses (virtual and physical, branded)
- PCI-compliant Tokenizer with iOS and Android SDKs to reduce merchant PCI scope
- Savings accounts for end users (yield-bearing balances)
- Settlements API and Transaction Report API for merchant reconciliation
- Signed webhook callbacks for asynchronous event delivery
- Shopify plugin and additional e-commerce integrations
- Business Portal with payment links, POS management, payroll, and settlements
- Regulated as an EMI in the UK, Denmark, Isle of Man, and Brazil
- 24/7 multilingual support and bank-grade encryption
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astropay.png
layout: provider
modified: '2026-05-24'
name: AstroPay
nav: Providers
network: true
overview: 'AstroPay publishes 20 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Payment Processing, Payouts, Wallets, and Digital Wallet.


  AstroPay''s developer surface includes developer portal, documentation, getting-started guide, authentication, changelog, support, signup flow, and 22 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 16.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astropay/refs/heads/main/screenshots/astropay-2026-06-20T172512.png
security:
- kind: domain-security
  name: Astropay Domain Security
  slug: astropay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astropay
solutions:
- Gaming and iGaming payments — deposits and withdrawals via local methods and AstroPay wallet
- Online marketplaces — split payouts to LatAm sellers in local currency
- Cross-border payroll — pay remote workers and contractors into AstroPay wallets
- Travel and ticketing — accept AstroPay across LatAm travelers
- Cryptocurrency on/off-ramps via USDT support
- E-commerce checkout — Shopify and custom storefronts
- Streaming and subscriptions — recurring billing through Wallet-on-File
- Remittance — bank deposits and wallet-to-wallet transfers
- Financial services and embedded finance for partner platforms
tags:
- Payments
- Payment Processing
- Payouts
- Wallets
- Digital Wallet
- Multi-Currency
- Cards
- Card Issuing
- Pix
- LatAm
- Latin America
- Brazil
- Argentina
- Mexico
- Chile
- Peru
- Colombia
- Uruguay
- Fintech
- Foreign Exchange
- Cross-Border Payments
- Checkout
- QR Payments
- Tokenization
- Embedded Finance
- Money Transfer
- Remittance
- Gaming Payments
- Marketplace Payments
- Payroll
website: https://www.astropay.com
---
