---
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
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: REST API for creating and managing payment jobs and payments — create, retrieve, and cancel payment jobs; capture, refund, and cancel individual payments; card tokenisation; and recurring payments. Pa
  name: Cashflows Gateway API
  slug: cashflows-gateway-api
- description: REST/JSON API for cardholder-not-present card payments with 3-D Secure support — authorisation, capture, void, refund, credit, IIN lookup, and 3-D Secure version 2 authentication and verification flow
  name: Cashflows Payments API
  slug: cashflows-payments-api
- description: API for connecting directly to the Cashflows acquiring network to authorise card transactions, authenticated with auth_id (Profile/Merchant ID) and auth_pass credential headers.
  name: Cashflows Remote Authentication API
  slug: cashflows-remote-authentication-api
- description: Standalone REST API for PCI-PTS secure Kinetic payment devices, served locally from the terminal (default http://127.0.0.1:8080) under /api/v2 — device info, ping/status, settings, transactions, scree
  name: Cashflows In-Person Payments API
  slug: cashflows-in-person-payments-api
artifact_total: 8
asyncapis:
- description: ''
  name: Cashflows Gateway Webhooks
  slug: cashflows-gateway-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cashflows-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cashflows.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cashflows.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cashflows.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cashflows.com/api_reference/api_reference_overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cashflows.com/getting_started/getting_started.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cashflows.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cashflows.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.cashflows.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.cashflows.com/contact/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cashflows.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cashflows.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.cashflows.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cashflows
- group: auth
  title: ''
  type: Authentication
  url: authentication/cashflows-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cashflows-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cashflows-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/cashflows-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cashflows-gateway-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/cashflows-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cashflows-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cashflows-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cashflows-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/cashflows-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cashflows-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cashflows-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cashflows-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cashflows-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cashflows-llms.txt
created: '2026-07-24'
description: Cashflows is a United Kingdom payment gateway and card acquirer, headquartered in London and a principal member of Visa and Mastercard, that helps businesses accept, process, and manage card payments across online, in-app, and in-person channels. Its product family spans a REST Cashflows Gateway (payment jobs, captures, refunds, tokenisation, recurring payments, and webhooks), hosted and embedded checkout, a cardholder-not-present Payments API with 3-D Secure, a Remote Authentication API for connecting to the acquiring network, and an In-Person Payments API served locally from Kinetic PCI-PTS terminals. Cashflows ships a genuine self-serve developer portal at developer.cashflows.com with reference documentation, a dedicated integration/sandbox environment, and webhook-based payment notifications, but it does not publish a downloadable OpenAPI/Swagger definition or a public Postman collection; its API reference is hand-authored HTML. Authentication is header-based (ConfigurationId
  plus a SHA-512 request hash for the Gateway, and auth_id/auth_pass for Remote Authentication) rather than OAuth.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: cashflows-mcp.yml
  slug: cashflows-mcpyml
modified: '2026-07-24T12:00:00Z'
name: Cashflows
nav: Providers
network: true
overview: 'Cashflows publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and Acquiring.


  The Cashflows catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cashflows'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, authentication, and 22 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 46.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 46.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cashflows/refs/heads/main/screenshots/cashflows-2026-07-25T204721.png
security:
- kind: authentication
  name: Cashflows Authentication
  slug: cashflows-authentication
  summary_line: apiKey/http-hash-signature/credential-pair · 3 schemes
- kind: domain-security
  name: Cashflows Domain Security
  slug: cashflows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cashflows
tags:
- Payments
- United Kingdom
- Payment Gateway
- Payment Processing
- Acquiring
- Card Payments
- In-Person Payments
- 3-D Secure
- Recurring Payments
- Webhooks
website: https://www.cashflows.com/
---
