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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Ziina Agentic Access
  operation_count: 8
  slug: ziina-agentic-access
  summary_line: 8 operations · 5 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Retrieve the authenticated account profile.
  name: Ziina Account API
  slug: ziina-account-api
- description: Service status.
  name: Ziina HealthCheck API
  slug: ziina-healthcheck-api
- description: The Log API from Ziina — 1 operation(s) for log.
  name: Ziina Log API
  slug: ziina-log-api
- description: Create and retrieve payment intents (hosted/embedded checkout).
  name: Ziina PaymentIntent API
  slug: ziina-paymentintent-api
- description: Issue and retrieve refunds against a payment intent.
  name: Ziina Refund API
  slug: ziina-refund-api
- description: Initiate and retrieve peer transfers between Ziina accounts.
  name: Ziina Transfer API
  slug: ziina-transfer-api
- description: Register or delete a webhook endpoint for payment events.
  name: Ziina Webhook API
  slug: ziina-webhook-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a payment intent, then poll it until the payment reaches a terminal status. Seed inputs with test=true to run in Ziina test mode.
  name: Ziina - accept a payment and confirm
  slug: ziina-accept-payment.arazzo
- description: Issue a refund against an existing payment intent, then poll the refund until it reaches a terminal status.
  name: Ziina - refund a payment and confirm
  slug: ziina-refund-payment.arazzo
artifact_total: 28
asyncapis:
- description: Event surface for Ziina payment webhooks. When a webhook URL is registered (POST /webhook), Ziina delivers events as HTTP POST callbacks over HTTPS to that URL. Non-2xx responses are retried up to 3 t
  name: Ziina Webhooks
  slug: ziina-webhooks-asyncapi
collections:
- collection_type: postman
  name: Ziina Account API
  slug: postman-ziina-account-api
- collection_type: postman
  name: Ziina Account HealthCheck API
  slug: postman-ziina-healthcheck-api
- collection_type: postman
  name: Ziina Account Log API
  slug: postman-ziina-log-api
- collection_type: postman
  name: Ziina Account PaymentIntent API
  slug: postman-ziina-paymentintent-api
- collection_type: postman
  name: Ziina Account Refund API
  slug: postman-ziina-refund-api
- collection_type: postman
  name: Ziina Account Transfer API
  slug: postman-ziina-transfer-api
- collection_type: postman
  name: Ziina Account Webhook API
  slug: postman-ziina-webhook-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ziina/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ziina-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ziina-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ziina-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ziina-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ziina-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ziina-co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ziina
- group: company
  title: ''
  type: Website
  url: https://ziina.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ziina.com
- group: commercial
  title: ''
  type: Plans
  url: plans/ziina-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ziina-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ziina-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ziina.com/blog
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ziina-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ziina-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ziina-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ziina-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ziina-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/ziina-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ziina-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ziina-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ziina-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ziina-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ziina-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ziina-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ziina-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ziina-openapi-overlay.yaml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/ziina-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ziina-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ziina-accept-payment.arazzo.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ziina-refund-payment.arazzo.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ziina.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ziina.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ziina.com/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://ziina.com/help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://ziina.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://ziina.com/business/connect
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ziina.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ziina.com/privacy
created: '2026-07-17'
description: Ziina is a Dubai-based (UAE) fintech offering an instant money and payments platform for consumers and businesses. Its REST API lets developers create hosted and embedded payment intents, issue refunds, run peer transfers between Ziina accounts, and register webhooks. Amounts are in the currency's minor unit (fils for AED), auth is HTTP bearer (JWT) via OAuth 2.0 scopes, and settlement is in AED with multi-currency acceptance.
finops:
- name: Ziina Finops
  service_category: Payments and Financial Services
  slug: ziina-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ziina.png
layout: provider
mcp_servers:
- description: ''
  name: ziina-mcp.yml
  slug: ziina-mcpyml
modified: '2026-07-17'
name: Ziina
nav: Providers
network: true
overview: 'Ziina publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, HealthCheck API, Log API, and 4 more. Tagged areas include Payments, Fintech, UAE, MENA, and Money Transfer.


  The Ziina catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ziina''s developer surface includes authentication, documentation, engineering blog, sandbox, getting-started guide, API reference, support, and 34 more developer resources.'
plans:
- name: Ziina Plans Pricing
  plan_count: 3
  slug: ziina-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 1
  name: Ziina Rate Limits
  slug: ziina-rate-limits
scopes:
- name: Ziina Scopes
  scope_count: 7
  slug: ziina-scopes
  summary_line: 7 scopes
score:
  band: strong
  composite: 65.7
  delta: -2.6
  facets:
    commercial_clarity: 100.0
    contract_quality: 55.7
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 34.2
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 84.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ziina Authentication
  slug: ziina-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ziina Domain Security
  slug: ziina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ziina Vulnerability Disclosure
  slug: ziina-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ziina Trust Center
  slug: ziina-trust-center
  summary_line: PCI DSS
slug: ziina
tags:
- Payments
- Fintech
- UAE
- MENA
- Money Transfer
- Wallet
website: https://ziina.com/
---
