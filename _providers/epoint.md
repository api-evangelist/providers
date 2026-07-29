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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-07-28'
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
random_paper: 15
score:
  band: developing
  composite: 43.0
  delta: 4.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 7.9
  previous_composite: 39.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epoint/refs/heads/main/screenshots/epoint-2026-07-25T213527.png
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
