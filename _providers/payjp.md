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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 6
  name: Payjp Agentic Access
  operation_count: 24
  slug: payjp-agentic-access
  summary_line: 24 operations · 15 acting · 6 human-in-the-loop
api_count: 14
apis:
- description: The 3D Secure API from PAY.JP — 4 operation(s) for 3d secure.
  name: PAY.JP 3D Secure API
  slug: payjp-3d-secure-api
- description: The Account API from PAY.JP — 1 operation(s) for account.
  name: PAY.JP Account API
  slug: payjp-account-api
- description: The Balances API from PAY.JP — 2 operation(s) for balances.
  name: PAY.JP Balances API
  slug: payjp-balances-api
- description: The Cards API from PAY.JP — 2 operation(s) for cards.
  name: PAY.JP Cards API
  slug: payjp-cards-api
- description: The Charges API from PAY.JP — 6 operation(s) for charges.
  name: PAY.JP Charges API
  slug: payjp-charges-api
- description: The Customers API from PAY.JP — 2 operation(s) for customers.
  name: PAY.JP Customers API
  slug: payjp-customers-api
- description: The Events API from PAY.JP — 2 operation(s) for events.
  name: PAY.JP Events API
  slug: payjp-events-api
- description: The Plans API from PAY.JP — 2 operation(s) for plans.
  name: PAY.JP Plans API
  slug: payjp-plans-api
- description: The Platform API from PAY.JP — 4 operation(s) for platform.
  name: PAY.JP Platform API
  slug: payjp-platform-api
- description: The Statements API from PAY.JP — 3 operation(s) for statements.
  name: PAY.JP Statements API
  slug: payjp-statements-api
- description: The Subscriptions API from PAY.JP — 5 operation(s) for subscriptions.
  name: PAY.JP Subscriptions API
  slug: payjp-subscriptions-api
- description: The Terms API from PAY.JP — 2 operation(s) for terms.
  name: PAY.JP Terms API
  slug: payjp-terms-api
- description: The Tokens API from PAY.JP — 3 operation(s) for tokens.
  name: PAY.JP Tokens API
  slug: payjp-tokens-api
- description: The Transfers API from PAY.JP — 3 operation(s) for transfers.
  name: PAY.JP Transfers API
  slug: payjp-transfers-api
artifact_total: 24
asyncapis:
- description: ''
  name: Payjp Webhooks
  slug: payjp-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payjp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/payjp-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://pay.jp/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/payjp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payjp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payjp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/payjp-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/payjp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/payjp-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/payjp-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payjp-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/payjp-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/payjp-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/payjp-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/payjp-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/payjp-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/payjp-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/payjp-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/payjp-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payjp-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pay.jp
- group: operate
  title: ''
  type: Deprecation
  url: https://pay.jp/info
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/payjp-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/payjp.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payjp
- group: company
  title: ''
  type: Website
  url: https://pay.jp/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pay.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pay.jp/v1/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pay.jp/v1/started
- group: operate
  title: ''
  type: Support
  url: https://help.pay.jp/ja
- group: commercial
  title: ''
  type: Pricing
  url: https://pay.jp/plan
- group: start
  title: ''
  type: SignUp
  url: https://console.pay.jp/d/signup
- group: start
  title: ''
  type: Login
  url: https://console.pay.jp/d/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pay.jp/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pay.co.jp/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/payjp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payjp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/payjp-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pay.jp/info
created: '2026-07-17'
description: PAY.JP is an online payment service operated by PAY, Inc. (PAY株式会社) in Japan. Its Stripe-style REST API lets merchants create charges, tokenize cards, manage customers, run subscriptions (定期課金), and settle transfers (入金) in Japanese yen, with a Platform API (beta) for marketplace/multi-tenant payouts.
finops:
- name: Payjp Finops
  service_category: Payments and Financial Services
  slug: payjp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payjp.png
layout: provider
mcp_servers:
- description: ''
  name: payjp-mcp.yml
  slug: payjp-mcpyml
modified: '2026-07-18'
name: PAY.JP
nav: Providers
network: true
overview: 'PAY.JP publishes 14 APIs on the [APIs.io](https://apis.io/) network, including 3D Secure API, Account API, Balances API, and 11 more. Tagged areas include Payments, FinTech, Japan, Credit Cards, and Subscriptions.


  The PAY.JP catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PAY.JP''s developer surface includes authentication, sandbox, changelog, documentation, getting-started guide, support, pricing, and 33 more developer resources.'
plans:
- name: Payjp Plans Pricing
  plan_count: 6
  slug: payjp-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Payjp Rate Limits
  slug: payjp-rate-limits
score:
  band: exemplar
  composite: 73.4
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 63.5
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 84.2
  previous_composite: 73.4
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
  name: Payjp Authentication
  slug: payjp-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Payjp Domain Security
  slug: payjp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payjp Vulnerability Disclosure
  slug: payjp-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Payjp Trust Center
  slug: payjp-trust-center
  summary_line: PCI DSS
slug: payjp
tags:
- Payments
- FinTech
- Japan
- Credit Cards
- Subscriptions
- Tokenization
website: https://pay.jp/
---
