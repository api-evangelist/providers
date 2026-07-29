---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 72
  human_in_the_loop: 2
  name: Fat Zebra Agentic Access
  operation_count: 133
  slug: fat-zebra-agentic-access
  summary_line: 133 operations · 72 acting · 2 human-in-the-loop
api_count: 4
apis:
- description: 'The core Fat Zebra payments Gateway — 98 documented operations across 73 paths covering purchases, authorizations and captures, refunds and voids, card tokenization (credit_cards), customers and bank '
  name: Fat Zebra Gateway API
  slug: fat-zebra-gateway-api
- description: The Partner (v2) API for ISOs and software platforms to programmatically create and manage their own sub-merchants and acquirer connections — 30 operations across 22 paths covering partner self/identi
  name: Fat Zebra Partner API
  slug: fat-zebra-partner-api
- description: An early usage-based Billing API (OpenAPI 3.0.3) exposing billing entities and a batch usage-record push for metered billing against customers. Documented server is the sandbox host billing.pmnts-sand
  name: Fat Zebra Billing API
  slug: fat-zebra-billing-api
- description: A Third-Party Processor (TPP) merchant onboarding API for the FDMS acquiring integration (OpenAPI 3.0.3) — create and list merchants and an internal onboard operation. Documented server is the sandbox
  name: Fat Zebra FDMS TPP Merchant Onboarding API
  slug: fat-zebra-fdms-tpp-merchant-onboarding-api
artifact_total: 10
asyncapis:
- description: ''
  name: Fat Zebra Webhooks
  slug: fat-zebra-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fat-zebra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fat-zebra-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fat-zebra-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fat-zebra-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fatzebra.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fatzebra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fatzebra.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fatzebra.com/reference/purchases
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fatzebra.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fatzebra.com/changelog/welcome-to-pmnts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fatzebra
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fatzebra.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fatzebra.com/platform/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.fatzebra.com/company/news
- group: operate
  title: ''
  type: Support
  url: https://www.fatzebra.com/contact/support
- group: auth
  title: ''
  type: Security
  url: https://www.fatzebra.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fatzebra.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/fat-zebra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fat-zebra-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fat-zebra-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fat-zebra-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fat-zebra-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fat-zebra-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/fat-zebra-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.fatzebra.com/docs/pci-certification
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fat-zebra-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/fat-zebra-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fat-zebra-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.fatzebra.com/changelog/welcome-to-pmnts
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fat-zebra-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fat-zebra-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fat-zebra-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/fat-zebra-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fat-zebra-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fat-zebra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-accept-a-card-payment.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-authorize-and-capture.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-tokenize-and-charge.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/fat-zebra-board-a-submerchant.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fat-zebra-changelog.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.fatzebra.com/contact/sales
created: '2026-07-24'
description: Fat Zebra is an Australian payments company (founded 2012, Sydney) providing a card-present and card-not-present payment gateway and processing platform for merchants, ISOs, and software platforms across Australia and New Zealand. Its API-first Gateway handles Visa, Mastercard, and Amex purchases, authorizations and captures, refunds and voids, card tokenization, 3D Secure, recurring payment plans, direct debits and direct credits over local bank rails, chargeback handling, batch processing, and hosted payment pages (PayNow), alongside wallet acceptance for Apple Pay, Google Pay, and Click to Pay. A separate Partner API lets platforms and ISOs create and board their own sub-merchants onto acquirer connections programmatically. The developer surface is a genuine, well-documented ReadMe hub at docs.fatzebra.com with four downloadable OpenAPI definitions, and the runtime platform is branded pmnts (gateway.pmnts.io). Authentication is HTTP Basic using a username and API token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: fat-zebra-mcp.yml
  slug: fat-zebra-mcpyml
modified: '2026-07-24'
name: Fat Zebra
nav: Providers
network: true
overview: 'Fat Zebra publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Gateway API, Partner API, Billing API, and 1 more. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Acquiring.


  The Fat Zebra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fat Zebra''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, engineering blog, and 34 more developer resources.'
random_paper: 1
score:
  band: strong
  composite: 57.5
  delta: -1.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fat-zebra/refs/heads/main/screenshots/fat-zebra-2026-07-25T214245.png
security:
- kind: authentication
  name: Fat Zebra Authentication
  slug: fat-zebra-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fat Zebra Domain Security
  slug: fat-zebra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fat Zebra Trust Center
  slug: fat-zebra-trust-center
  summary_line: PCI DSS
slug: fat-zebra
tags:
- Payments
- Australia
- Payment Gateway
- Payment Processing
- Acquiring
- Card Payments
- Tokenization
- Recurring Billing
- Direct Debit
- Hosted Payment Pages
- Merchant Onboarding
website: https://www.fatzebra.com/
---
