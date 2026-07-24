---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST payment gateway for accepting online card payments in Azerbaijan. Covers payment creation and hosted checkout, card registration/tokenization and saved-card charges, refunds and reversals, pre-au
  name: Epoint Payment API
  slug: epoint-payment-api
artifact_total: 5
asyncapis:
- description: ''
  name: Epoint Callbacks Webhooks
  slug: epoint-callbacks-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://epoint.az
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.epoint.az/en
- group: docs
  title: ''
  type: Documentation
  url: https://developer.epoint.az/en
- group: docs
  title: ''
  type: APIReference
  url: https://developer.epoint.az/en
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.epoint.az/en
- group: company
  title: ''
  type: Blog
  url: https://epoint.az/en/news
- group: operate
  title: ''
  type: Support
  url: https://epoint.az/en/contact
- group: start
  title: ''
  type: Login
  url: https://epoint.az/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://epoint.az/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://epoint.az/en/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/epoint-authentication.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/epoint-decline-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/epoint-decline-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/epoint-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/epoint-callbacks-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/epoint-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/epoint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/epoint-packages.yml
- group: design
  title: ''
  type: Components
  url: components/epoint-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/epoint-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/epoint-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/epoint-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epoint-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/epoint-llms.txt
created: '2026-07-17'
description: Epoint (epoint.az) is an Azerbaijani digital payment aggregator and e-commerce platform for small and medium enterprises, backed by 500 Global. It lets merchants accept online card payments on their website, mobile app, or social page and layers on card tokenization (saved cards), split payments, pre-authorization, installment payments, payouts to any Azerbaijani business card 24/7, wallets, invoicing, QR/link payments, recurring payments, and Apple Pay / Google Pay. Its REST payment API (base https://epoint.az/api/1) authenticates every request with a merchant public_key plus a SHA1 data+signature scheme and returns results both synchronously and via signed callbacks to the merchant's result_url.
image: https://epoint.az/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: epoint-mcp.yml
  slug: epoint-mcpyml
modified: '2026-07-19'
name: Epoint
nav: Providers
network: true
overview: 'Epoint publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Gateway, Fintech, and E-commerce.


  The Epoint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Epoint''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 39.0
  delta: 2.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 36.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Epoint Authentication
  slug: epoint-authentication
  summary_line: custom-signature · 1 scheme
- kind: domain-security
  name: Epoint Domain Security
  slug: epoint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: epoint
tags:
- Company
- Payments
- Payment Gateway
- Fintech
- E-commerce
- Card Payments
- Azerbaijan
- Apple Pay
- Google Pay
- Digital Wallet
website: https://epoint.az
---
