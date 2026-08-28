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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: BANCOMAT Pay is a mobile payment service enabling Italian consumers to make e-commerce purchases and P2P transfers through a smartphone app linked to their bank account by phone number and IBAN. Merch
  name: BANCOMAT Pay
  slug: bancomat-pay
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bancomat-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bancomat-spa
- group: company
  title: ''
  type: Website
  url: https://bancomat.it/en
- group: company
  title: ''
  type: Website
  url: https://bancomat.it/en/the-company
- group: design
  title: ''
  type: SpectralRules
  url: rules/bancomat-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bancomat-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bancomat-context.jsonld
created: '2024-01-15'
description: BANCOMAT S.p.A. is Italy's leading payment network operator managing the PagoBancomat debit card scheme, ATM network, and BANCOMAT Pay mobile payment service. Launched in 1983 for ATM withdrawals and expanded in 1986 with PagoBancomat for PIN-based POS payments, the network underpins Italian electronic payment infrastructure. BANCOMAT Pay, introduced in 2019, enables mobile e-commerce and P2P payments linked to bank accounts via phone number and IBAN.
features:
- description: Italy's largest ATM cash withdrawal network operational since 1983.
  name: ATM Network
- description: PIN-based POS debit card payments accepted at millions of Italian merchants.
  name: PagoBancomat Debit
- description: Mobile app payment service for e-commerce and P2P transfers linked to bank accounts.
  name: BANCOMAT Pay Mobile
- description: QR code-based checkout integration for online and in-store merchants.
  name: QR Code Payments
- description: Deep integration with Italian banks enabling account-linked payment authorization.
  name: Bank Integration
- description: Person-to-person money transfers between Italian bank accounts via mobile app.
  name: P2P Transfers
finops:
- name: Bancomat Finops
  service_category: API
  slug: bancomat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bancomat.png
integrations:
- description: Integration via Nexi XPay Global payment gateway for merchant acceptance.
  name: Nexi
- description: Integration via Axerve/Fabrick for Italian e-commerce BANCOMAT Pay acceptance.
  name: Axerve (Fabrick)
- description: Integration via PPRO for international PSP access to BANCOMAT Pay.
  name: PPRO
- description: Integration via HiPay payment platform.
  name: HiPay
- description: Integration via Viva.com payment services.
  name: Viva.com
- description: Integration via PayPal Braintree payment gateway.
  name: PayPal Braintree
- description: Integration via Nuvei payment technology platform.
  name: Nuvei
jsonld:
- class_count: 0
  name: Bancomat Context
  property_count: 15
  slug: bancomat-context
layout: provider
modified: '2026-04-21'
name: Bancomat
nav: Providers
network: true
overview: 'Bancomat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ATM, Banking, Financial-Services, Italy, and Mobile Payments.


  The Bancomat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Bancomat Plans Pricing
  plan_count: 3
  slug: bancomat-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Bancomat Rate Limits
  slug: bancomat-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: Bancomat API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: bancomat-spectral-rules
score:
  band: emerging
  composite: 17.9
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 45.5
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 45.5
    operational_transparency: 7.9
  previous_composite: 16.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bancomat/refs/heads/main/screenshots/bancomat-2026-06-20T172935.png
security:
- kind: domain-security
  name: Bancomat Domain Security
  slug: bancomat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bancomat
tags:
- ATM
- Banking
- Financial-Services
- Italy
- Mobile Payments
- Payments
- Debit Cards
use_cases:
- description: Debit card ATM withdrawals across Italy's national banking network.
  name: ATM Cash Withdrawals
- description: PIN-based debit card payments at retail point-of-sale terminals.
  name: POS Debit Payments
- description: Online checkout integration via BANCOMAT Pay mobile app.
  name: E-Commerce Payments
- description: Person-to-person payments between bank accounts via mobile app.
  name: P2P Money Transfer
- description: Enable BANCOMAT Pay as a local Italian payment method for online stores.
  name: Merchant Acceptance
website: https://bancomat.it/en
---
