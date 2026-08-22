---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Fatora's REST API for hosted-checkout payment collection, card tokenization, refunds and payment verification, plus CRUD over invoices, clients and products and AI content helpers. Payment endpoints a
  name: Fatora REST API
  slug: fatora-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fatora-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://fatora.io/ar/security/
- group: company
  title: ''
  type: Website
  url: https://fatora.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fatora.io/api/
- group: docs
  title: ''
  type: Documentation
  url: https://fatora.io/api/
- group: docs
  title: ''
  type: APIReference
  url: https://fatora-api.stoplight.io/docs/API-reference/ZG9jOjE-fatora-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://fatora.io/api/introduction.php
- group: auth
  title: ''
  type: Authentication
  url: authentication/fatora-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fatora-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/fatora-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fatora-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fatora-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fatora-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fatora-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fatora-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fatora-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fatora-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MaktApp
- group: commercial
  title: ''
  type: Pricing
  url: https://fatora.io/ar/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.fatora.io/register/
- group: start
  title: ''
  type: Login
  url: https://app.fatora.io/login/
- group: operate
  title: ''
  type: Support
  url: https://fatora.io/ar/help-center/
- group: operate
  title: ''
  type: HelpCenter
  url: https://fatora.io/ar/help-center/
- group: company
  title: ''
  type: Blog
  url: https://fatora.io/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fatora.io/ar/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fatora.io/en/privacy-en/
created: '2026-07-17'
description: Fatora is a Qatar-based online invoicing and payment platform operated by MaktApp, serving more than 120,000 merchants across Arabic-speaking markets in the Gulf and wider MENA region. It combines professional invoicing, a hosted online store, POS/cashier tooling, WhatsApp/SMS/email payment links, and a card payment gateway (routing through processors such as Stripe, TAP and TESS) behind a single merchant account. Fatora publishes a REST API at api.fatora.io/v1 for programmatic checkout, tokenization, refunds and payment verification, plus full CRUD over invoices, clients and products, and AI helpers for product content. First-party SDKs are provided for PHP, Laravel, .NET, JavaScript, React, iOS, Android and Ionic, alongside ready-made plugins for WooCommerce, Magento, OpenCart, PrestaShop, Shopify and Wix. This profile was enriched from Fatora's public developer surface.
image: https://fatora.io/assets/img/logo/fatora-logo.png
layout: provider
modified: '2026-07-19'
name: Fatora
nav: Providers
network: true
overview: 'Fatora publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Invoicing, Payment Gateway, E-commerce, and Billing.


  Fatora''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, pricing, signup flow, and 19 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 35.3
  delta: 1.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 34.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fatora/refs/heads/main/screenshots/fatora-2026-07-25T214251.png
security:
- kind: authentication
  name: Fatora Authentication
  slug: fatora-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fatora Domain Security
  slug: fatora-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fatora Trust Center
  slug: fatora-trust-center
  summary_line: PCI DSS
slug: fatora
tags:
- Payments
- Invoicing
- Payment Gateway
- E-commerce
- Billing
- Fintech
- Checkout
- MENA
- Qatar
- SaaS
website: https://fatora.io
---
