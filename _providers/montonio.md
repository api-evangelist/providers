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
    agent_skills: derived
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
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: JWT-authenticated REST API for collecting payments (bank payment initiation, cards, MobilePay, BLIK, BNPL / Hire-Purchase), creating and validating Orders, issuing Refunds, generating Payment Links, o
  name: Montonio Payments API (Stargate)
  slug: montonio-payments-api-stargate
- description: 'JWT-authenticated REST API for multi-carrier shipping: list carriers and shipping methods, fetch pickup points and courier services, calculate rates, create and update Shipments, generate and fetch La'
  name: Montonio Shipping API (v2)
  slug: montonio-shipping-api-v2
artifact_total: 6
asyncapis:
- description: ''
  name: Montonio Webhooks
  slug: montonio-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.montonio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.montonio.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.montonio.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.montonio.com/api/stargate/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.montonio.com/api/stargate/checklist
- group: auth
  title: ''
  type: Authentication
  url: authentication/montonio-authentication.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.montonio.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://partner.montonio.com/signup?locale=en_US
- group: start
  title: ''
  type: Login
  url: https://partner.montonio.com/login?locale=en_US
- group: operate
  title: ''
  type: Support
  url: https://help.montonio.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.montonio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.montonio.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.montonio.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/montonio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.montonio.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.montonio.com/legal
- group: build
  title: ''
  type: Packages
  url: packages/montonio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/montonio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/montonio-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/montonio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/montonio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/montonio-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/montonio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/montonio-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/montonio-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/montonio-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/montonio-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/montonio-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/montonio-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/montonio-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/montonio-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/montonio-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Montonio is an Estonian fintech providing a unified payments and shipping platform for e-commerce merchants across the Baltics, Poland, and Finland. Its developer platform exposes two JWT-authenticated REST APIs: the Payments API (Stargate) for bank payment initiation, card payments, MobilePay, BLIK, and Buy-Now-Pay-Later / Hire-Purchase financing, together with orders, refunds, payment links, checkout sessions and payout reporting; and the Shipping API (v2) for multi-carrier label printing, parcel tracking, pickup points, and shipment management. Montonio serves over 8,000 businesses, ships ready-made plugins for WooCommerce, Magento and PrestaShop, and publishes a first-party JavaScript SDK with embeddable checkout UI components.'
image: https://cdn.prod.website-files.com/6745c818f143d246f266b299/68b9ab2dc787d1c75659148a_Frame%201%20(3).png
layout: provider
mcp_servers:
- description: ''
  name: montonio-mcp.yml
  slug: montonio-mcpyml
modified: '2026-07-20'
name: Montonio
nav: Providers
network: true
overview: 'Montonio publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payment Processing, and Open Banking.


  The Montonio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Montonio''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, support, and 26 more developer resources.'
random_paper: 92
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 45.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Montonio Authentication
  slug: montonio-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Montonio Domain Security
  slug: montonio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: montonio
tags:
- Company
- Fintech
- Payments
- Payment Processing
- Open Banking
- E-commerce
- Shipping
- Logistics
- Financing
- Baltics
- Webhooks
- SDK
website: https://www.montonio.com
---
