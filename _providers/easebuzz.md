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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 9.6
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: REST payment gateway API to initiate transactions, verify transaction status, and process refunds across 150+ payment options (cards, UPI, net banking, wallets, EMI). Requests are authenticated with a
  name: Easebuzz Payment Gateway API
  slug: easebuzz-payment-gateway-api
- description: REST payouts API (Wire) to disburse funds over NEFT, RTGS, IMPS and UPI, manage beneficiaries, run vendor and tax payments, and check payout/balance status, authenticated with a merchant key, salt and
  name: Easebuzz Wire Payouts API
  slug: easebuzz-wire-payouts-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/easebuzz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easebuzz.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.easebuzz.in/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.easebuzz.in/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.easebuzz.in/
- group: start
  title: ''
  type: SignUp
  url: https://easebuzz.in/merchant/signup/
- group: start
  title: ''
  type: Login
  url: https://easebuzz.in/merchant/login/
- group: operate
  title: ''
  type: Support
  url: https://support.easebuzz.in/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.easebuzz.in/
- group: company
  title: ''
  type: Blog
  url: https://easebuzz.in/explainers/
- group: commercial
  title: ''
  type: Pricing
  url: https://easebuzz.in/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easebuzz.in/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easebuzz.in/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/easebuzz
- group: build
  title: ''
  type: Packages
  url: packages/easebuzz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/easebuzz-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/easebuzz-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/easebuzz-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/easebuzz-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.easebuzz.in/docs/payment-gateway/i849ghebwytej-payment-gateway
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/easebuzz-llms.txt
created: '2026-07-17'
description: Easebuzz is an Indian payments and financial-technology platform providing Software-as-a-Service embedded with payments infrastructure for businesses across India. Its products include a payment gateway supporting 150+ payment options (cards, UPI, net banking, wallets, EMI, BNPL), payment links, and in-store POS; collections products such as EasyCollect subscriptions, InstaCollect virtual accounts, Slices payment splitting and FeesBuzz fee collection; Wire payouts over NEFT, RTGS, IMPS and UPI with vendor and tax payments; sub-merchant management for platforms and marketplaces; Easebuzz Neo connected banking APIs; and SaaS tools including SmartBilling, Teller, Forms and Webstore. Developers integrate through REST APIs authenticated with a merchant key, salt and SHA-512 request hash, backed by official SDKs and e-commerce plugins across web and mobile platforms.
image: https://ebz-static.s3.ap-south-1.amazonaws.com/easebuzz-static/easebuzz_technology_solutions.png
layout: provider
modified: '2026-07-18'
name: Easebuzz
nav: Providers
network: true
overview: 'Easebuzz publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payment Gateway, and Payouts.


  Easebuzz''s developer surface includes documentation, API reference, signup flow, support, engineering blog, pricing, authentication, and 14 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 36.4
  delta: 5.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.3
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Easebuzz Authentication
  slug: easebuzz-authentication
  summary_line: apiKey/customHash · 2 schemes
- kind: domain-security
  name: Easebuzz Domain Security
  slug: easebuzz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easebuzz
tags:
- Company
- Fintech
- Payments
- Payment Gateway
- Payouts
- Banking
- India
- UPI
- Subscriptions
- SDK
website: https://easebuzz.in/
---
