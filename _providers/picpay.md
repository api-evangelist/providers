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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: Public REST API on appws.picpay.com that lets merchants charge a PicPay user's wallet from an ecommerce checkout. Creates a payment with a referenceId, returns a payment URL plus a QR code for the buy
  name: PicPay Ecommerce Checkout API
  slug: picpay-ecommerce-checkout-api
- description: 'Unified payment gateway API for accepting credit cards, PIX, and the PicPay wallet through transparent, standard, or lightbox checkout flows. Exposes charges, charge cancellation, card vault storage, '
  name: PicPay Gateway Checkout API
  slug: picpay-gateway-checkout-api
- description: REST API for accepting PIX (Brazil's instant payment rail) as a payment method in ecommerce. Supports PIX cobrança (charge / QR code generation), payment confirmation, refunds, and webhook notificatio
  name: PicPay PIX API
  slug: picpay-pix-api
- description: Lets merchants accept remote sales by generating a hosted PicPay checkout link that can be paid with credit card, PIX, or the PicPay wallet. Useful for social-commerce, invoicing, and conversational s
  name: PicPay Payment Link API
  slug: picpay-payment-link-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/picpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.picpay.com
- group: start
  title: ''
  type: Portal
  url: https://developers-business.picpay.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://picpay.github.io/picpay-docs-digital-payments/
- group: docs
  title: ''
  type: Documentation
  url: https://picpay.github.io/picpay-docs-ms-ecommerce-checkout/en/docs/introduction/
- group: other
  title: ''
  type: Business
  url: https://www.picpay.com/site/parapme
- group: other
  title: ''
  type: Product
  url: https://www.picpay.com
- group: other
  title: ''
  type: Product
  url: https://www.picpay.com
- group: other
  title: ''
  type: Product
  url: https://www.picpay.com
- group: other
  title: ''
  type: Product
  url: https://www.picpay.com
- group: other
  title: ''
  type: Product
  url: https://www.picpay.com
- group: other
  title: ''
  type: Product
  url: https://www.picpay.com
- group: other
  title: ''
  type: ParentCompany
  url: https://jfinvest.com.br/en/business/picpay/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.picpay.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.picpay.com/
- group: company
  title: ''
  type: Newsroom
  url: https://meu.picpay.com/imprensa
- group: company
  title: ''
  type: Careers
  url: https://carreiras.picpay.com/
- group: operate
  title: ''
  type: Support
  url: https://meu.picpay.com/ajuda
- group: operate
  title: ''
  type: Contact
  url: mailto:negocios@atendimento.picpay.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PicPay
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PicPay/magento2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PicPay/ecommerce-integration-shopify
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PicPay/ecommerce-integration-wake
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/PicPay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/picpay
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@picpay
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/picpay
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meu.picpay.com/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meu.picpay.com/politica-de-privacidade
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/br/app/picpay-conta-cart%C3%A3o-e-pix/id606130353
- group: other
  title: ''
  type: PlayStore
  url: https://play.google.com/store/apps/details?id=com.picpay
created: '2026-05-25'
description: PicPay is a Brazilian fintech super-app and digital bank serving over 67 million users with a digital wallet, payment account, credit and debit cards, personal loans, investments (Cofrinho / fixed income), insurance, and PIX-based money movement. Founded in 2012 and acquired by J&F Investimentos (the holding company behind JBS) in 2015, PicPay is controlled today by J&F Participações and in 2024 incorporated the retail customer base of Banco Original to consolidate the group's consumer banking strategy. For developers and merchants, PicPay Business exposes a set of REST APIs that let online stores accept the PicPay wallet, credit/debit cards, PIX, and payment links as payment methods. The historical Ecommerce Public API on appws.picpay.com is authenticated with the x-picpay-token / x-seller-token headers and remains in use for direct wallet checkout. A newer unified business developer portal at developers-business.picpay.com publishes the Gateway PicPay Checkout API, Carteira
  PicPay Wallet API, PIX API, and Payment Link API, all of which now use OAuth 2.0 client_credentials bearer JWTs minted at api.picpay.com/oauth2/token (5-minute TTL) and webhook callbacks for payment status notifications. PicPay also publishes GitHub repos for Magento, Shopify, and Wake ecommerce integrations, plus its open developer documentation for the wallet and PIX APIs under picpay.github.io. PicPay reported a return to profitability in 2023 and is reportedly working with Citigroup on a U.S. IPO.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/picpay.png
layout: provider
modified: '2026-05-25'
name: PicPay
nav: Providers
network: true
overview: 'PicPay publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Digital Wallet, Digital Bank, Neobank, and Fintech.


  PicPay''s developer surface includes developer portal, documentation, engineering blog, support, YouTube channel, and 26 more developer resources.'
random_paper: 81
score:
  band: emerging
  composite: 19.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/picpay/refs/heads/main/screenshots/picpay-2026-06-20T191659.png
security:
- kind: domain-security
  name: Picpay Domain Security
  slug: picpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: picpay
tags:
- Payments
- Digital Wallet
- Digital Bank
- Neobank
- Fintech
- PIX
- Ecommerce
- Checkout
- Credit Card
- Loans
- Investments
- Insurance
- Brazil
- Latin America
- Super App
website: https://www.picpay.com
---
