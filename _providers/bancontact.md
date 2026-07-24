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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for accepting Bancontact payments online and via QR code. Enables merchants to create payment transactions, generate QR codes, handle callbacks, and process refunds. The API is organized arou
  name: Bancontact Payconiq Acceptance API
  slug: payconiq-acceptance-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bancontact-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bancontactpayconiqcompany
- group: company
  title: ''
  type: Website
  url: https://www.bancontact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bancontactpro.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/bancontact-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bancontact-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bancontact-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.bancontactpro.com/llms.txt
created: '2025-01-01'
description: Bancontact is Belgium's most popular electronic payment system, operating through the Bancontact Payconiq Company (now transitioning to Bancontact Pro brand). The platform provides debit card payments, QR code payments, and mobile payments via the Payconiq by Bancontact app. The REST API enables merchants to accept payments online, in-app, and via QR codes with settlement in Belgian bank accounts.
features:
- description: Accept Bancontact debit card payments in e-commerce checkouts.
  name: Online Payments
- description: Generate QR codes for in-store and contactless payment acceptance.
  name: QR Code Payments
- description: Payconiq by Bancontact app integration for mobile checkout.
  name: Mobile App Payments
- description: Real-time payment status notifications via webhook callbacks.
  name: Webhooks
- description: Programmatic refund processing for completed transactions.
  name: Refunds
- description: EUR-denominated payments with Belgian bank account settlement.
  name: Multi-currency
- description: Mobile deep links to open the Payconiq app directly from merchant checkout.
  name: Deep Links
finops:
- name: Bancontact Finops
  service_category: API
  slug: bancontact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bancontact.png
jsonld:
- class_count: 0
  name: Bancontact Context
  property_count: 18
  slug: bancontact-context
layout: provider
modified: '2026-04-21'
name: Bancontact
nav: Providers
network: true
overview: 'Bancontact publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Belgium, Debit Cards, E-Commerce, and Fintech.


  The Bancontact catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bancontact''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Bancontact Plans Pricing
  plan_count: 3
  slug: bancontact-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 5
  name: Bancontact Rate Limits
  slug: bancontact-rate-limits
rules:
- name: Bancontact API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 6
  slug: bancontact-spectral-rules
score:
  band: thin
  composite: 30.1
  delta: -1.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 15.1
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 47.4
    operational_transparency: 31.6
  previous_composite: 31.2
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bancontact/refs/heads/main/screenshots/bancontact-2026-06-20T172938.png
security:
- kind: domain-security
  name: Bancontact Domain Security
  slug: bancontact-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bancontact
tags:
- Banking
- Belgium
- Debit Cards
- E-Commerce
- Fintech
- Payments
use_cases:
- description: Accept Bancontact as a local Belgian payment method at checkout.
  name: E-Commerce Checkout
- description: In-store and restaurant QR code payment acceptance.
  name: QR Code POS
- description: Integrate Bancontact into iOS and Android apps.
  name: Mobile In-App Payments
- description: Payment links and QR codes for invoicing and B2C collections.
  name: Invoice Payments
- description: Recurring payment collection from Belgian consumers.
  name: Subscription Billing
website: https://www.bancontact.com/
---
