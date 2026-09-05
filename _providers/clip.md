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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 4.3
  scored_at: '2026-09-04'
api_count: 6
apis:
- description: Hosted checkout flow that redirects shoppers to a Clip-hosted payment page to capture card data and complete the charge. Returns the authorized payment back to the merchant via redirect plus a postbac
  name: Clip Checkout Redirect API
  slug: clip-checkout-redirect-api
- description: 'Server-side payment processing that tokenizes card data via the Card Token API and charges through the Payments API while keeping the checkout experience entirely on the merchant''s site. Supports 3DS '
  name: Clip Checkout Transparente API
  slug: clip-checkout-transparente-api
- description: Query individual transactions and list transactions across a date range from a Clip merchant account — used for reconciliation across both online Checkout and physical PinPad/POS sales.
  name: Clip Transactions API
  slug: clip-transactions-api
- description: Retrieve detailed deposit reports and deposit summaries for the merchant's Clip Cuenta over a date window (up to 90 days). Use to reconcile payouts to the merchant's bank against captured transactions
  name: Clip Deposits API
  slug: clip-deposits-api
- description: Create full or partial refunds against previously approved Clip payments and query refund status. Supports both Checkout and PinPad sourced transactions.
  name: Clip Refunds API
  slug: clip-refunds-api
- description: Drive a Clip PinPad device (fixed, high-volume terminal) from a merchant's own POS software — initiate card-present sales, query device status, capture authorizations, and reconcile against the Transa
  name: Clip PinPad API
  slug: clip-pinpad-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clip.mx
- group: start
  title: ''
  type: Portal
  url: https://www.payclip.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clip.mx
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clip.mx/docs/primeros-pasos
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clip.mx/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clip.mx/reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clip.mx/llms.txt
- group: operate
  title: ''
  type: FAQ
  url: https://developer.clip.mx/page/preguntas-frecuentes
- group: operate
  title: ''
  type: Forums
  url: https://developer.clip.mx/discuss
- group: design
  title: ''
  type: Webhooks
  url: https://developer.clip.mx/reference/referencia-postback-webhook
- group: auth
  title: ''
  type: Compliance
  url: https://developer.clip.mx/reference/pci-compliance
- group: operate
  title: ''
  type: Support
  url: https://ayuda.clip.mx/s/
- group: other
  title: ''
  type: Shop
  url: https://shop.clip.mx
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/clip-ultra
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/clip-pro-2
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/clip-total-3
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/clip-plus-2
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/clip-pinpad
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/checkout
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/link-de-cobro
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/clip-cuenta
- group: other
  title: ''
  type: Product
  url: https://www.clip.mx/empresas
- group: company
  title: ''
  type: Blog
  url: https://blog.clip.mx
- group: company
  title: ''
  type: Careers
  url: https://careers.clip.mx
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:corporate@payclip.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clip.mx/privacidad
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clip.mx/terminos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClipMX
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Payclip
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/clip_mx
- group: company
  title: ''
  type: LinkedIn
  url: https://mx.linkedin.com/company/payclip
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/clipmx
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/clip.mx/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCWihkxbz5A5xUc8QLnfkEOQ
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@clip.mx
created: '2026-05-24'
description: Clip (legal name Payclip) is a Mexico City-based fintech and SMB acquirer often described as the Square equivalent in Mexico. Founded in 2012, Clip enables merchants of all sizes to accept card, contactless, and QR payments through a family of mobile point-of-sale (mPOS) terminals — Clip Plus 2, Clip Pro 2, Clip Ultra, Clip Total 3, and the high-volume Clip PinPad — as well as Tap to Pay on iOS/Android smartphones, an online Checkout payment gateway, payment links, and the Clip Cuenta digital business account with same-day settlement and SMB loans. Clip operates the developer portal developer.clip.mx, which publishes the Checkout Redirect, Checkout Transparente, Transactions, Deposits, Refunds, and PinPad APIs along with the Checkout Transparente SDK and a Terminal SDK for embedding card acceptance into third-party POS apps. The company is backed by strategic investors including American Express Ventures, Banorte, Capital Group, and Morgan Stanley, and is consistently ranked
  among Mexico's top private fintech employers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clip.png
layout: provider
modified: '2026-05-24'
name: Clip
nav: Providers
network: true
overview: 'Clip publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Acquiring, SMB Payments, Point-of-Sale, and mPOS.


  Clip''s developer surface includes developer portal, getting-started guide, documentation, FAQ, support, engineering blog, YouTube channel, and 29 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 44.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 6.6
  previous_composite: 21.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clip/refs/heads/main/screenshots/clip-2026-06-20T174527.png
security:
- kind: domain-security
  name: Clip Domain Security
  slug: clip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clip
tags:
- Payments
- Acquiring
- SMB Payments
- Point-of-Sale
- mPOS
- Tap to Pay
- Card Acceptance
- Checkout
- Payment Gateway
- Payment Links
- Mexico
- Latin America
- Fintech
- PCI
website: https://www.clip.mx
---
