---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 63
  human_in_the_loop: 1
  name: Shift4 Agentic Access
  operation_count: 72
  slug: shift4-agentic-access
  summary_line: 72 operations · 63 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: 'Core card payment processing for the Shift4 Payment API — authorize, capture, sale, refund, and manage card transactions, including card entry, processing mode, dynamic currency conversion (DCC), and '
  name: Shift4 Transactions API
  slug: shift4-transactions-api
- description: Tokenization endpoints for the Shift4 Payment API — create, retrieve, and manage card tokens (single-use and card-on-file) plus the account updater for keeping stored credentials current.
  name: Shift4 Tokens API
  slug: shift4-tokens-api
- description: Gift card issuance and redemption for the Shift4 Payment API — activate, add value, redeem, balance-inquire, and manage stored-value gift card accounts.
  name: Shift4 Gift Cards API
  slug: shift4-gift-cards-api
- description: In-person and terminal control for the Shift4 Payment API — drive card-present devices, EMV/contactless acceptance, and the Commerce Engine for attended and unattended payment hardware.
  name: Shift4 Devices API
  slug: shift4-devices-api
- description: ACH bank-account payment endpoints for the Shift4 Payment API — create and manage ACH debit/credit transactions, backed by ACH webhook notifications for asynchronous status updates.
  name: Shift4 ACH API
  slug: shift4-ach-api
- description: Alternative payment methods for the Shift4 Payment API — QR-code payments (including Citcon, WeChat Pay, and Alipay) and PayPal acceptance.
  name: Shift4 Alternative & QR Payments API
  slug: shift4-alternative-payments-api
- description: Cardholder authentication and fraud controls for the Shift4 Payment API — 3D Secure (3DS) authentication flows plus risk scoring and rule evaluation.
  name: Shift4 3D Secure & Risk API
  slug: shift4-3d-secure-api
- description: Hosted payment link endpoints for the Shift4 Payment API — create, configure, share, and reconcile shareable payment links, with payment-link webhook notifications.
  name: Shift4 Payment Links API
  slug: shift4-payment-links-api
- description: Hosted checkout session endpoints for the Shift4 Payment API — create and retrieve checkout sessions for online payment collection, with checkout-session webhook notifications.
  name: Shift4 Checkout Sessions API
  slug: shift4-checkout-sessions-api
- description: Original Credit Transaction (OCT) endpoints for the Shift4 Payment API — push funds to cardholders for payouts and disbursements.
  name: Shift4 OCT Payouts API
  slug: shift4-oct-payouts-api
- description: Reporting and account endpoints for the Shift4 Payment API — transaction reports plus merchant and credentials lookups.
  name: Shift4 Reports & Merchants API
  slug: shift4-reports-api
artifact_total: 16
asyncapis:
- description: ''
  name: Shift4 Webhooks
  slug: shift4-webhooks
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/shift4-authorize-and-capture.md
- group: build
  title: ''
  type: SDKs
  url: https://docs.shift4.com/sdks/ios
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shift4-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shift4-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shift4-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shift4.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shift4.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shift4.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shift4.com/apis/payments-platform-rest/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shift4.com/guides/quickstart
- group: build
  title: ''
  type: PostmanCollection
  url: https://docs.shift4.com/tools/postman
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.shift4.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://docs.shift4.com/guides/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shift4.com
- group: build
  title: ''
  type: JavaScriptLibrary
  url: https://dev.shift4.com/docs/js/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shift4developer
- group: build
  title: ''
  type: Packages
  url: packages/shift4-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shift4-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shift4-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shift4-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shift4-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/shift4-payment-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/shift4-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.shift4.com/pdf/S4P-PCI-DSS-Roles-and-Responsibilities.pdf
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shift4-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/shift4-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shift4-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://docs.shift4.com/guides/deprecated/legacy-card-tokens
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shift4-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shift4-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shift4-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shift4-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shift4-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shift4-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/shift4-components.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
created: '2026-07-24'
description: 'Shift4 (NYSE: FOUR) is a US-based integrated payments and commerce technology company headquartered in Center Valley, Pennsylvania, and a Fortune 1000 business serving restaurants, hospitality, retail, gaming, stadiums, e-commerce, and nonprofit verticals. It operates as an end-to-end acquirer-processor, owning the full stack from its own gateway and card acquiring through in-person SkyTab POS hardware, online checkout, and alternative payment methods, and has expanded internationally through acquisitions including Finaro (Credorax), Global Blue, and others. Its public developer surface is genuinely API-native: a Redocly-powered developer portal at docs.shift4.com publishes the Shift4 Payment API, a single downloadable OpenAPI 3.1 definition (v1.7.57, 70 paths) covering card transactions, tokenization, gift cards, devices/terminals, ACH, QR and PayPal alternative payments, 3D Secure, payment links, checkout sessions, OCT payouts, and reporting, authenticated with a header AccessToken
  (API key) plus HMAC-SHA256 request signing and backed by webhook event notifications, a sandbox, SDKs, and a published Postman collection.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: shift4-mcp.yml
  slug: shift4-mcpyml
modified: '2026-07-24'
name: Shift4
nav: Providers
network: true
overview: 'Shift4 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Transactions API, Tokens API, Gift Cards API, and 8 more. Tagged areas include Payments, United States, Payment Processing, Payment Gateway, and Acquiring.


  The Shift4 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shift4''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, sandbox, and 29 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 50.8
  delta: -3.9
  facets:
    commercial_clarity: 7.9
    contract_quality: 72.0
    developer_ergonomics: 77.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Shift4 Authentication
  slug: shift4-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Shift4 Domain Security
  slug: shift4-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shift4
tags:
- Payments
- United States
- Payment Processing
- Payment Gateway
- Acquiring
- Payment Terminal
- Tokenization
- ACH
- 3D Secure
- Gift Cards
- Payment Links
- Card Present
website: https://www.shift4.com
---
