---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Manages purchase orders and payment processing across multiple payment methods including credit card, debit 3DS, boleto, and PIX. Supports post-authorization capture, card tokenization, payment splitt
  name: PagBank Orders API
  slug: pagbank-orders-api
- description: Dedicated API for PIX instant payment infrastructure in Brazil. Supports immediate charge creation via QR codes, payment receipt confirmation, and real-time notifications for PIX transactions.
  name: PagBank PIX API
  slug: pagbank-pix-api
- description: OAuth 2.0 authorization API enabling platform integrations (SaaS and marketplace models) to connect applications with third-party PagBank user accounts for delegated payment processing actions.
  name: PagBank Connect API
  slug: pagbank-connect-api
- description: Subscription billing API for managing recurring charges. Handles subscription creation, billing cycles, payment method updates, and recurring payment indicators for installment plans.
  name: PagBank Recurring Payments API
  slug: pagbank-recurring-payments-api
- description: Hosted checkout solution that redirects customers to a PagBank-managed payment page. Simplifies PCI compliance for merchants by offloading card data handling to PagBank infrastructure.
  name: PagBank Checkout API
  slug: pagbank-checkout-api
- description: Enables platform partners to create and manage third-party PagBank accounts programmatically. Used by marketplace and SaaS platforms to onboard sellers and sub-merchants.
  name: PagBank Account Registration API
  slug: pagbank-account-registration-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pagbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pagbank.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pagbank.com.br/docs/apis-pagbank
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pagbank.com.br/docs/primeiros-passos
- group: docs
  title: ''
  type: APIReference
  url: https://developer.pagbank.com.br/reference/introducao
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pagseguro/
- group: company
  title: ''
  type: Blog
  url: https://developer.pagbank.com.br/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://pagbank.com.br/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pagbank.com.br/
- group: other
  title: ''
  type: X
  url: https://twitter.com/PagBank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pagbank
- group: commercial
  title: ''
  type: Plans
  url: plans/pagbank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pagbank-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pagbank-finops.yml
created: '2026-06-13'
description: PagBank (formerly PagSeguro) is a Brazilian digital bank and payment platform operated by PagoSeguro Internet Instituição de Pagamento S/A, a subsidiary of Universo Online (UOL). It provides REST APIs for Pix instant transfers, credit and debit card processing, e-commerce checkout, boleto bancário, recurring payments, POS terminal integration, and financial account management. PagBank serves e-commerce merchants, SaaS platforms, and marketplaces across Brazil and supports over 29.5 million customers.
finops:
- name: Pagbank Finops
  service_category: ''
  slug: pagbank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pagbank.png
layout: provider
modified: '2026-06-13'
name: PagBank
nav: Providers
network: true
overview: 'PagBank publishes 1 API on the [APIs.io](https://apis.io/) network: Orders API. Tagged areas include Payments, Digital Banking, Brazil, PIX, and Fintech.


  PagBank''s developer surface includes documentation, getting-started guide, API reference, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Pagbank Plans Pricing
  plan_count: 2
  slug: pagbank-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 0
  name: Pagbank Rate Limits
  slug: pagbank-rate-limits
score:
  band: thin
  composite: 28.4
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pagbank/refs/heads/main/screenshots/pagbank-2026-06-20T191323.png
security:
- kind: domain-security
  name: Pagbank Domain Security
  slug: pagbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pagbank
tags:
- Payments
- Digital Banking
- Brazil
- PIX
- Fintech
- E-Commerce
- POS
- Recurring Payments
- Boleto
website: https://pagbank.com.br/
---
