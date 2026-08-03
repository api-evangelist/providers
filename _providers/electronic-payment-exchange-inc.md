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
api_count: 1
apis:
- description: EPX card-not-present and card-present payment processing surface — Hosted Checkout, Hosted Pay Page, Browser Post API, and the North EPX Custom Pay REST API — handling sales, authorizations, captures,
  name: EPX Payments API
  slug: epx-payments-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electronic-payment-exchange-inc-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.north.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.north.com/products/online/epx-hosted-checkout/integration-guide
- group: docs
  title: ''
  type: APIReference
  url: https://developer.north.com/supplemental-resources/epx-data-dictionary/transaction-request-fields
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.north.com/products/online/epx-hosted-checkout/integration-guide
- group: company
  title: ''
  type: Blog
  url: https://developer.north.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.epx.com/contact
- group: start
  title: ''
  type: Login
  url: https://websuite.epx.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epx.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.paymentshub.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/electronic-payment-exchange-inc-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/electronic-payment-exchange-inc-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/electronic-payment-exchange-inc-llms.txt
created: '2026-07-17'
description: Electronic Payment Exchange (EPX) is a full-stack, PCI-compliant payments platform that has processed card, ACH, and alternative payments for merchants and banks across the United States, Canada, Europe, Latin America, and the Caribbean for more than forty years. Now part of North (North American Bancard), EPX combines the roles of ISO, merchant acquirer, gateway, and front-end and back-end processor under one contract. Its BRIC technology issues a unique token for every transaction so cardholder data never touches the merchant environment. Developers integrate through EPX Hosted Checkout, the Hosted Pay Page, the Browser Post API, and the North EPX Custom Pay REST API, all documented on the North Developer portal, supporting sales, authorizations, captures, refunds, voids, recurring billing, and batch settlement with EMV, tokenization, and encryption throughout.
image: https://www.epx.com/app/default/assets/addons/default/epx/epx_theme-theme/resources/853506e8a63744c7bc743bafcdf8072d.gif?v=1784398777
layout: provider
modified: '2026-07-19'
name: Electronic payment Exchange Inc
nav: Providers
network: true
overview: 'Electronic payment Exchange Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Processing, Merchant Acquiring, and Payment Gateway.


  Electronic payment Exchange Inc''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 8 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 27.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 27.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Electronic Payment Exchange Inc Authentication
  slug: electronic-payment-exchange-inc-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Electronic Payment Exchange Inc Domain Security
  slug: electronic-payment-exchange-inc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: electronic-payment-exchange-inc
tags:
- Company
- Payments
- Payment Processing
- Merchant Acquiring
- Payment Gateway
- Tokenization
- Credit Card Processing
- ACH
- Fintech
website: https://developer.north.com/
---
