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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful partner API for international mass payments — live FX rate quotes, recipient account management, and automated payment processing to 170+ countries in 50+ currencies. Authenticated with API ke
  name: OFX Payments API
  slug: ofx-payments-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.ofx.com/en-us/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ofx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ofx.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ofx.com/en-us/partner-with-us/api/
- group: start
  title: ''
  type: SignUp
  url: https://app.ofx.com/registration
- group: start
  title: ''
  type: Login
  url: https://app.ofx.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ofx.com/en-us/transfer-rates/
- group: operate
  title: ''
  type: Support
  url: https://www.ofx.com/en-us/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.ofx.com/en-us/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ofx.com/en-us/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ofx.com/en-us/legal/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.ofx.com/en-us/legal/sanctions-compliance-resources/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ozforex-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ozforex-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ozforex-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ozforex-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ozforex-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ozforex-well-known.yml
created: '2026-07-17'
description: 'OFX (formerly OzForex) is a global money-transfer and international-payments company that has been moving and managing money globally for over 25 years, trading as USForex Inc. in North America. Beyond consumer and business FX, OFX offers a partner Payments API: a RESTful API for international mass payments to 170+ countries in 50+ currencies, covering live exchange-rate quotes, recipient account management, and automated payment processing for invoices, payroll, and bulk supplier payments. Developers can build and test against an open sandbox environment before going live, authenticating with API keys. OFX is a registered Money Service Business with FinCEN (NMLS #1021624) and a licensed money transmitter across multiple U.S. states.'
image: https://www.ofx.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: OFX (OzForex)
nav: Providers
network: true
overview: 'OFX (OzForex) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Money Transfer, Foreign Exchange, and International Payments.


  OFX (OzForex)''s developer surface includes documentation, getting-started guide, signup flow, pricing, support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 32.9
  delta: -2.6
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 79.6
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 35.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ozforex Authentication
  slug: ozforex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ozforex Domain Security
  slug: ozforex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ozforex
tags:
- Company
- Consumer
- Money Transfer
- Foreign Exchange
- International Payments
- Payments
- Currency
- Fintech
website: https://www.ofx.com/en-us/
---
