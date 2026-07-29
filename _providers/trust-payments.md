---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Server-to-server JSON API (the Secure Trading Payment Platform / STPP) for card processing and management on the TRU Connect gateway. Supports request types including AUTH, ACCOUNTCHECK, REFUND, SUBSC
  name: Trust Payments Webservices API
  slug: webservices-api
- description: Payout / disbursement capability exposed through the Webservices API, used to send funds out (for example refunds beyond original transactions and supported payout flows) via the STPP JSON interface o
  name: Trust Payments Payouts API
  slug: payouts-api
artifact_total: 5
asyncapis:
- description: ''
  name: Trust Payments Webhooks
  slug: trust-payments-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trust-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.trustpayments.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.trustpayments.com/hc/en-us/sections/360005821218-Webservices-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SecureTrading
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trustpayments.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trustpayments.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.trustpayments.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.trustpayments.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://myst.trustpayments.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustpayments.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustpayments.com/privacy-policy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.trustpayments.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trustpayments.com/get-started/
- group: operate
  title: ''
  type: Support
  url: https://www.trustpayments.com/contact-us/
- group: auth
  title: ''
  type: Authentication
  url: authentication/trust-payments-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trust-payments-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trust-payments-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/trust-payments-decline-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trust-payments-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trust-payments-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trust-payments-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.trustpayments.com/security/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trust-payments-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/trust-payments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trust-payments-packages.yml
- group: design
  title: ''
  type: Components
  url: components/trust-payments-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trust-payments-llms.txt
created: '2026-07-24'
description: Trust Payments is a London-headquartered payment gateway and processor (formerly Secure Trading / SecureTrading) operating across the United Kingdom, Europe, and the United States. It offers online, in-store point-of-sale, unattended, and mobile card acceptance, acquiring, alternative and local payment methods, tokenisation, recurring billing, payouts, and 3-D Secure authentication through its TRU Connect gateway. The developer surface centres on the Secure Trading Payment Platform (STPP) - a server-to-server JSON Webservices API for processing (AUTH, ACCOUNTCHECK, REFUND, SUBSCRIPTION, TRANSACTIONUPDATE, and TRANSACTIONQUERY), a JWT-authenticated client-side JavaScript Library for PCI-reduced hosted card fields, and mobile SDKs, all documented as reference articles in the Trust Payments help centre with Python, PHP, ReactJS, and Swift libraries published under the SecureTrading GitHub organisation. Trust Payments does not publish a downloadable OpenAPI/Swagger definition; production
  Webservices access requires PCI certification, account approval, and credential (key) exchange, so the surface is documentation-and-SDK driven rather than open self-serve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Trust Payments
nav: Providers
network: true
overview: 'Trust Payments publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and Acquiring.


  The Trust Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trust Payments'' developer surface includes documentation, API reference, pricing, engineering blog, getting-started guide, support, authentication, and 21 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 53.2
  delta: 7.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 45.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Trust Payments Authentication
  slug: trust-payments-authentication
  summary_line: credentials/jwt · 2 schemes
- kind: domain-security
  name: Trust Payments Domain Security
  slug: trust-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trust-payments
tags:
- Payments
- United Kingdom
- Payment Gateway
- Payment Processing
- Acquiring
- Card Payments
- Tokenization
- Subscriptions
- 3-D Secure
- Point of Sale
- Webhooks
- Payouts
website: https://www.trustpayments.com/
---
