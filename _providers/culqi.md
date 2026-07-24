---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 25
  human_in_the_loop: 7
  name: Culqi Agentic Access
  operation_count: 46
  slug: culqi-agentic-access
  summary_line: 46 operations · 25 acting · 7 human-in-the-loop
api_count: 12
apis:
- description: 3-D Secure charge confirmation on the secure host.
  name: Culqi 3DS API
  slug: culqi-3ds-api
- description: Cards saved against a customer for recurring or one-click charges.
  name: Culqi Cards API
  slug: culqi-cards-api
- description: One-time charges (cargos) against a token or saved card.
  name: Culqi Charges API
  slug: culqi-charges-api
- description: Stored customer (cliente) profiles.
  name: Culqi Customers API
  slug: culqi-customers-api
- description: Webhook event objects representing account activity.
  name: Culqi Events API
  slug: culqi-events-api
- description: Card BIN / IIN metadata lookup.
  name: Culqi Iins API
  slug: culqi-iins-api
- description: Payment orders for PagoEfectivo (CIP) and bank-transfer / cash-agent flows.
  name: Culqi Orders API
  slug: culqi-orders-api
- description: Recurring-billing plan definitions.
  name: Culqi Plans API
  slug: culqi-plans-api
- description: Full or partial refunds (devoluciones) of a charge.
  name: Culqi Refunds API
  slug: culqi-refunds-api
- description: Subscriptions linking a saved card to a plan.
  name: Culqi Subscriptions API
  slug: culqi-subscriptions-api
- description: Client-side tokenization of card and Yape credentials on the secure host.
  name: Culqi Tokens API
  slug: culqi-tokens-api
- description: Settlement transfers (abonos) paid out to the merchant.
  name: Culqi Transfers API
  slug: culqi-transfers-api
artifact_total: 22
asyncapis:
- description: ''
  name: Culqi Events Webhooks
  slug: culqi-events-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/culqi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/culqi-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/culqi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/culqi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/culqi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/culqi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/culqi
- group: company
  title: ''
  type: Website
  url: https://culqi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.culqi.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/culqi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/culqi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/culqi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/team-culqi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.culqi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.culqi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.culqi.com/es/documentacion/primeros-pasos/introduccion/
- group: operate
  title: ''
  type: Support
  url: https://culqi.com/centro-de-ayuda/
- group: commercial
  title: ''
  type: Pricing
  url: https://culqi.com/precios/
- group: start
  title: ''
  type: SignUp
  url: https://afiliate.culqi.com/
- group: start
  title: ''
  type: Login
  url: https://culqipanel.culqi.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://culqi.com/terminos_y_condiciones/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://culqi.com/politicas-de-privacidad/
- group: build
  title: ''
  type: Postman
  url: collections/culqi.postman_collection.json
- group: build
  title: ''
  type: Packages
  url: packages/culqi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/culqi-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/culqi-sandbox.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/culqi-decline-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/culqi-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/culqi-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/culqi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/culqi-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/culqi-openapi-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/culqi-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/culqi-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/culqi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/culqi-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/culqi-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/culqi-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/culqi-components.yml
- group: auth
  title: ''
  type: Security
  url: security/culqi-vulnerability-disclosure.yml
created: '2026-07-17'
description: Culqi is a Peruvian online payments platform and a Grupo Credicorp / Krealo company. Its REST API v2 lets businesses accept card, Yape, PagoEfectivo, mobile wallet and Cuotealo (installment) payments in PEN and USD, with card data tokenized client-side against a PCI-scoped secure host and all money movement, subscriptions and webhooks driven from a server-side secret key.
finops:
- name: Culqi Finops
  service_category: Payment Processing
  slug: culqi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/culqi.png
layout: provider
mcp_servers:
- description: ''
  name: culqi-mcp.yml
  slug: culqi-mcpyml
modified: '2026-07-17'
name: Culqi
nav: Providers
network: true
overview: 'Culqi publishes 12 APIs on the [APIs.io](https://apis.io/) network, including 3DS API, Cards API, Charges API, and 9 more. Tagged areas include Payments, Payment Gateway, FinTech, Peru, and LatAm.


  The Culqi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Culqi''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, pricing, and 34 more developer resources.'
plans:
- name: Culqi Plans Pricing
  plan_count: 5
  slug: culqi-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 2
  name: Culqi Rate Limits
  slug: culqi-rate-limits
score:
  band: exemplar
  composite: 71.6
  delta: 1.2
  facets:
    commercial_clarity: 100.0
    contract_quality: 66.4
    developer_ergonomics: 84.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 70.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Culqi Authentication
  slug: culqi-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Culqi Domain Security
  slug: culqi-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Culqi Vulnerability Disclosure
  slug: culqi-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Culqi Trust Center
  slug: culqi-trust-center
  summary_line: PCI DSS Level 1
slug: culqi
tags:
- Payments
- Payment Gateway
- FinTech
- Peru
- LatAm
- Cards
- Yape
website: https://culqi.com/
---
