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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Beam's v1 REST payments API — payment links, charges, refunds, transactions, card authorizations (auth/capture/cancel), network tokenization, and Beam Bolt in-person payments.
  name: Beam API v1
  slug: beam-api-v1
artifact_total: 6
asyncapis:
- description: ''
  name: Beam Checkout Webhooks
  slug: beam-checkout-webhooks
collections:
- collection_type: postman
  name: '[For merchant test] Playground (SANDBOX) version 1.14.0'
  slug: postman-beam-checkout-playground
common:
- group: company
  title: ''
  type: Website
  url: https://www.beamcheckout.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.beamcheckout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beamcheckout.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beamcheckout.com/v1/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beamcheckout.com/get-started/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/beam-checkout-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beam-checkout-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/beam-checkout-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beam-checkout-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/beam-checkout-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beam-checkout-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beamcheckout.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.beamcheckout.com/get-started/migrating-from-v0
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/beam-checkout-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/beam-checkout-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beam-checkout-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/beam-checkout-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/beam-checkout-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beam-checkout-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beam-checkout-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/beam-checkout-data-model.yml
- group: build
  title: ''
  type: Postman
  url: postman/beam-checkout-playground.postman_collection.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beam-checkout-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beamcheckout.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.beamcheckout.com/getstarted
- group: operate
  title: ''
  type: Support
  url: https://guides.beamcheckout.com/hc/en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beamcheckout.com/tncs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beamcheckout.com/privacy
created: '2026-07-17'
description: Beam is a Thailand-focused payments platform that lets businesses accept payments across in-person and online channels. Its products include Beam Checkout (online payments for social media, websites, and apps via hosted payment links and a Charges API), Beam Bolt (an in-person payment device), and Beam Bridge (embedded payments for partner platforms). Beam supports cards, e-wallets, QR PromptPay, installments, and Alipay+, with card authorization/capture, refunds, tokenization, 3DS, and CIT/MIT recurring flows. The v1 REST API uses HTTP Basic auth (merchantId:apiKey), idempotency keys, HMAC-signed webhooks, and a playground sandbox. Beam states it is PCI DSS compliant and compliant with Bank of Thailand regulations. Backed by Peak XV, Partech, and SeaX Ventures.
image: https://www.beamcheckout.com/assets/beam-thumbnail.jpg
layout: provider
mcp_servers:
- description: ''
  name: beam-checkout-mcp.yml
  slug: beam-checkout-mcpyml
modified: '2026-07-18'
name: Beam Checkout
nav: Providers
network: true
overview: 'Beam Checkout publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Payments, Checkout, and Card Payments.


  The Beam Checkout catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Beam Checkout''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, pricing, and 21 more developer resources.'
random_paper: 28
score:
  band: developing
  composite: 54.8
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 63.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 54.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beam-checkout/refs/heads/main/screenshots/beam-checkout-2026-07-25T202537.png
security:
- kind: authentication
  name: Beam Checkout Authentication
  slug: beam-checkout-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Beam Checkout Domain Security
  slug: beam-checkout-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: beam-checkout
tags:
- Company
- Financial Services
- Payments
- Checkout
- Card Payments
- Webhooks
- Thailand
- Fintech
website: https://www.beamcheckout.com/
---
