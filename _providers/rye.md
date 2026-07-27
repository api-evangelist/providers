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
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 84.6
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Rye Agentic Access
  operation_count: 39
  slug: rye-agentic-access
  summary_line: 39 operations · 19 acting
api_count: 13
apis:
- description: The Betas API from Rye — 1 operation(s) for betas.
  name: Rye Betas API
  slug: rye-betas-api
- description: The Billing API from Rye — 6 operation(s) for billing.
  name: Rye Billing API
  slug: rye-billing-api
- description: The Brands API from Rye — 1 operation(s) for brands.
  name: Rye Brands API
  slug: rye-brands-api
- description: The Checkout Intents API from Rye — 6 operation(s) for checkout intents.
  name: Rye Checkout Intents API
  slug: rye-checkout-intents-api
- description: The Commissions API from Rye — 2 operation(s) for commissions.
  name: Rye Commissions API
  slug: rye-commissions-api
- description: The Events API from Rye — 3 operation(s) for events.
  name: Rye Events API
  slug: rye-events-api
- description: The Merchant Connectors API from Rye — 1 operation(s) for merchant connectors.
  name: Rye Merchant Connectors API
  slug: rye-merchant-connectors-api
- description: The Orders API from Rye — 3 operation(s) for orders.
  name: Rye Orders API
  slug: rye-orders-api
- description: The Payment Gateways API from Rye — 1 operation(s) for payment gateways.
  name: Rye Payment Gateways API
  slug: rye-payment-gateways-api
- description: The Products API from Rye — 4 operation(s) for products.
  name: Rye Products API
  slug: rye-products-api
- description: The Returns API from Rye — 2 operation(s) for returns.
  name: Rye Returns API
  slug: rye-returns-api
- description: The Shipments API from Rye — 2 operation(s) for shipments.
  name: Rye Shipments API
  slug: rye-shipments-api
- description: The Test Helpers API from Rye — 6 operation(s) for test helpers.
  name: Rye Test Helpers API
  slug: rye-test-helpers-api
artifact_total: 21
asyncapis:
- description: ''
  name: Rye Webhooks
  slug: rye-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rye.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://rye.com/docs/api-v2/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://rye.com/docs/api-v2-experimental/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://rye.com/docs/api-v2/example-flows/simple-checkout
- group: operate
  title: ''
  type: Support
  url: https://rye.com/docs/api-v2/support
- group: company
  title: ''
  type: Blog
  url: https://rye.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rye-com
- group: commercial
  title: ''
  type: Pricing
  url: https://rye.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.rye.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rye.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rye.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/41015610-24cc0f8a-4b7f-4aa2-9f52-8d7ba30a67b7
- group: operate
  title: ''
  type: StatusPage
  url: https://ryestatus.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.rye.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/rye-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rye-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/rye-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rye-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rye-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rye-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rye-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rye-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/rye-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/rye-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rye-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/rye-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rye-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://rye.com/docs/api-v2/migrate-from-v1
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rye-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://rye.com/docs/api-v2/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rye-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rye-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rye-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rye-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/rye-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rye-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rye-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rye-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Rye is agentic commerce infrastructure - a Universal Checkout API that turns any product URL into a completed order without redirecting the shopper. Developers pass a product URL and buyer details and receive price, tax, shipping and delivery estimates, then confirm with a tokenized payment method (Stripe, Basis Theory, pre-funded drawdown balance, or x402/USDC) to place the order across thousands of merchants including Shopify stores and Amazon. Rye combines AI browser automation with fraud-mitigation and caches successful flows as deterministic workflows, advertising 90%+ order reliability, sub-35s offer resolution, and 99.9% uptime. The platform ships official TypeScript, Python, and Java SDKs, HMAC-signed webhooks, a staging sandbox with test products and simulated shipment/return helpers, Rewards UI React components, and a returns/refunds lifecycle. Rye is an a16z portfolio company.
image: https://rye.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: rye-mcp.yml
  slug: rye-mcpyml
modified: '2026-07-21'
name: Rye
nav: Providers
network: true
overview: 'Rye publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Betas API, Billing API, Brands API, and 10 more. Tagged areas include Company, Commerce, E-Commerce, Checkout, and Payments.


  The Rye catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rye''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 64
rate_limits:
- limit_count: 5
  name: Rye Rate Limits
  slug: rye-rate-limits
score:
  band: exemplar
  composite: 70.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.4
    developer_ergonomics: 84.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 94.7
  previous_composite: 70.6
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Rye Authentication
  slug: rye-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rye Domain Security
  slug: rye-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Rye Vulnerability Disclosure
  slug: rye-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Rye Trust Center
  slug: rye-trust-center
  summary_line: PCI DSS Level 1
slug: rye
tags:
- Company
- Commerce
- E-Commerce
- Checkout
- Payments
- Agentic Commerce
- AI Agents
- Universal Checkout
- Shopping
website: https://rye.com/docs
---
