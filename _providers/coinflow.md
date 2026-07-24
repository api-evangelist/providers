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
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 86.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 129
  human_in_the_loop: 3
  name: Coinflow Agentic Access
  operation_count: 180
  slug: coinflow-agentic-access
  summary_line: 180 operations · 129 acting · 3 human-in-the-loop
api_count: 14
apis:
- description: The authentication API from Coinflow — 3 operation(s) for authentication.
  name: Coinflow authentication API
  slug: coinflow-authentication-api
- description: The cardTokenization API from Coinflow — 3 operation(s) for cardtokenization.
  name: Coinflow cardTokenization API
  slug: coinflow-cardtokenization-api
- description: The checkout API from Coinflow — 33 operation(s) for checkout.
  name: Coinflow checkout API
  slug: coinflow-checkout-api
- description: The customers API from Coinflow — 15 operation(s) for customers.
  name: Coinflow customers API
  slug: coinflow-customers-api
- description: The events API from Coinflow — 1 operation(s) for events.
  name: Coinflow events API
  slug: coinflow-events-api
- description: The marketplace API from Coinflow — 11 operation(s) for marketplace.
  name: Coinflow marketplace API
  slug: coinflow-marketplace-api
- description: The merchant API from Coinflow — 49 operation(s) for merchant.
  name: Coinflow merchant API
  slug: coinflow-merchant-api
- description: The merchantSubscription API from Coinflow — 4 operation(s) for merchantsubscription.
  name: Coinflow merchantSubscription API
  slug: coinflow-merchantsubscription-api
- description: The redeem API from Coinflow — 4 operation(s) for redeem.
  name: Coinflow redeem API
  slug: coinflow-redeem-api
- description: The refund API from Coinflow — 4 operation(s) for refund.
  name: Coinflow refund API
  slug: coinflow-refund-api
- description: The subMerchant API from Coinflow — 3 operation(s) for submerchant.
  name: Coinflow subMerchant API
  slug: coinflow-submerchant-api
- description: The subscription API from Coinflow — 7 operation(s) for subscription.
  name: Coinflow subscription API
  slug: coinflow-subscription-api
- description: The utilities API from Coinflow — 3 operation(s) for utilities.
  name: Coinflow utilities API
  slug: coinflow-utilities-api
- description: The withdraw API from Coinflow — 30 operation(s) for withdraw.
  name: Coinflow withdraw API
  slug: coinflow-withdraw-api
artifact_total: 20
asyncapis:
- description: ''
  name: Coinflow Webhooks
  slug: coinflow-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://coinflow.cash/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coinflow.cash/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coinflow.cash/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coinflow.cash/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coinflow.cash/guides/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://coinflow.cash/blog/
- group: operate
  title: ''
  type: Support
  url: https://coinflow.cash/contact/
- group: start
  title: ''
  type: SignUp
  url: https://app.coinflow.cash/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinflow.cash/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinflow.cash/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinflow.cash/
- group: auth
  title: ''
  type: Security
  url: https://coinflow.cash/bug-bounty
- group: auth
  title: ''
  type: Compliance
  url: https://docs.coinflow.cash/guides/product-overview/key-concepts
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/coinflow-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coinflow-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coinflow-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/coinflow-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/coinflow-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coinflow-packages.yml
- group: design
  title: ''
  type: Components
  url: components/coinflow-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coinflow-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/coinflow-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coinflow-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/coinflow-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coinflow-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coinflow-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/coinflow-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coinflow-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coinflow-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coinflow-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/coinflow-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinflow-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coinflow-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coinflow-authentication.yml
created: '2026-07-17'
description: Coinflow is a stablecoin-native payments platform (backed by Pantera Capital) that lets software companies and marketplaces accept card, ACH, and crypto/USDC payments and send instant payouts across Solana, EVM, and Stellar rails. Its API covers checkout / pay-ins, PCI-compliant tokenized card-on-file, subscriptions, marketplace sub-merchant onboarding with KYC/KYB, refunds, withdrawals and merchant payouts, and HMAC-signed webhooks. Coinflow ships pre-built UI SDKs for React, React Native, Swift, Android, and Flutter, plus a sandbox environment with published test cards and 3DS triggers.
image: https://coinflow.cash/coinflow-og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: coinflow-mcp.yml
  slug: coinflow-mcpyml
modified: '2026-07-18'
name: Coinflow
nav: Providers
network: true
overview: 'Coinflow publishes 14 APIs on the [APIs.io](https://apis.io/) network, including authentication API, cardTokenization API, checkout API, and 11 more. Tagged areas include Company, Crypto, Payments, Stablecoin, and USDC.


  The Coinflow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coinflow''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, sandbox, and 29 more developer resources.'
random_paper: 49
score:
  band: developing
  composite: 57.3
  delta: 3.8
  facets:
    commercial_clarity: 42.1
    contract_quality: 58.4
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 53.5
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
  name: Coinflow Authentication
  slug: coinflow-authentication
  summary_line: apiKey · 7 schemes
- kind: domain-security
  name: Coinflow Domain Security
  slug: coinflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinflow Vulnerability Disclosure
  slug: coinflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coinflow
tags:
- Company
- Crypto
- Payments
- Stablecoin
- USDC
- Checkout
- Payouts
- Marketplace
- Web3
- Fintech
website: https://coinflow.cash/
---
