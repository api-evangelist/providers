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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 79.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Paypay Agentic Access
  operation_count: 10
  slug: paypay-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 2
apis:
- description: Everything involved in the payment life cycle
  name: PayPay Payment API
  slug: paypay-payment-api
- description: The Payments API from PayPay — 1 operation(s) for payments.
  name: PayPay Payments API
  slug: paypay-payments-api
artifact_total: 7
asyncapis:
- description: ''
  name: Paypay Webhooks
  slug: paypay-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.paypay.ne.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://www.paypay.ne.jp/opa/doc/v1.0/dynamicqrcode
- group: docs
  title: ''
  type: APIReference
  url: https://www.paypay.ne.jp/opa/doc/v1.0/dynamicqrcode
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.paypay.ne.jp/
- group: start
  title: ''
  type: SignUp
  url: https://developer.paypay.ne.jp/
- group: operate
  title: ''
  type: Support
  url: https://integration.paypay.ne.jp/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paypay
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/paypay-opa-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/paypay-opa-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paypay-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/paypay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paypay-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paypay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paypay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paypay-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/paypay-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paypay-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/paypay-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paypay-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paypay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paypay-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paypay-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paypay-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paypay-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paypay-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paypay-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paypay-agentic-access.yml
created: '2026-07-17'
description: PayPay is Japan's largest QR/barcode mobile-payment network (a SoftBank / Yahoo Japan / Paytm joint venture) with tens of millions of users. Its Open Payment API (OPA v2) lets payment partners and merchants collect payments from PayPay wallet users through dynamic QR codes, web checkout (Web Cashier), app-invoke deep links, and a pre-authorize-and-capture flow. The REST API (base //apigw.paypay.ne.jp) is secured with HMAC-SHA256 request signatures, settles in JPY, sends transaction webhooks plus daily reconciliation files, and ships official Node, PHP, Python and Java SDKs under the github.com/paypay organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paypay.png
layout: provider
mcp_servers:
- description: ''
  name: paypay-mcp.yml
  slug: paypay-mcpyml
modified: '2026-07-20'
name: PayPay
nav: Providers
network: true
overview: 'PayPay publishes 2 APIs on the [APIs.io](https://apis.io/) network: Payment API and Payments API. Tagged areas include Company, Fintech, Payments, Mobile Payments, and QR Code Payments.


  The PayPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayPay''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 21 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 44.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 53.5
    developer_ergonomics: 78.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Paypay Authentication
  slug: paypay-authentication
  summary_line: http/hmac · 2 schemes
- kind: domain-security
  name: Paypay Domain Security
  slug: paypay-domain-security
  summary_line: TLSv1.3
slug: paypay
tags:
- Company
- Fintech
- Payments
- Mobile Payments
- QR Code Payments
- Digital Wallet
- Japan
- Merchant Payments
website: https://developer.paypay.ne.jp/
---
