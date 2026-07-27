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
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 90.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 3
  name: Fazz Agentic Access
  operation_count: 8
  slug: fazz-agentic-access
  summary_line: 8 operations · 3 acting · 3 human-in-the-loop
api_count: 5
apis:
- description: Indonesia-market payments and disbursements (v4-ID) covering local virtual accounts and bank transfers, billed in IDR. Shares the Fazz/Xfers v4 request patterns with region-specific methods and destin
  name: Fazz Indonesia Payments API (v4-ID)
  slug: fazz-indonesia-payments-api
- description: HTTP POST webhook callbacks that notify your endpoint of payment and disbursement status changes in JSON, verified against your account signing secret.
  name: Fazz Callbacks (Webhooks)
  slug: fazz-callbacks
- description: Send API — disburse funds to recipients (payouts).
  name: Fazz Disbursements API
  slug: fazz-disbursements-api
- description: Create reusable payment method objects (PayNow, virtual bank account).
  name: Fazz Payment Methods API
  slug: fazz-payment-methods-api
- description: Accept API — create and query payments (collections).
  name: Fazz Payments API
  slug: fazz-payments-api
artifact_total: 15
asyncapis:
- description: ''
  name: Fazz Webhooks
  slug: fazz-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fazz-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fazz-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fazz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fazz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fazz-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xfers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fazz-financial
- group: company
  title: ''
  type: Website
  url: https://fazz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fazz.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/fazz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fazz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fazz-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/fazz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fazz-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fazz-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fazz-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fazz-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fazz-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/fazz-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fazz-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fazz-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fazz-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fazz-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fazz-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fazz-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fazz-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fazz-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/fazz.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fazz.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fazz.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support-sg.fazz.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fazz.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fazz.com/privacy-policy
created: '2026-07-17'
description: Fazz is a Southeast Asian business banking and payments group formed from the 2021 merger of Indonesia's Payfazz and Singapore's Xfers. Its Fazz Business Payments API (served on the xfers.io hosts) lets platforms accept payments via local methods like PayNow QR and virtual bank accounts, and send bulk disbursements across Singapore (SGD) and Indonesia (IDR). Not to be confused with the consumer-facing Payfazz agent app.
finops:
- name: Fazz Finops
  service_category: Financial Services
  slug: fazz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fazz.png
layout: provider
mcp_servers:
- description: ''
  name: fazz-mcp.yml
  slug: fazz-mcpyml
modified: '2026-07-17'
name: Fazz
nav: Providers
network: true
overview: 'Fazz publishes 3 APIs on the [APIs.io](https://apis.io/) network: Disbursements API, Payment Methods API, and Payments API. Tagged areas include Fintech, Payments, Business Banking, Disbursements, and Southeast Asia.


  The Fazz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fazz''s developer surface includes authentication, documentation, changelog, sandbox, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Fazz Plans Pricing
  plan_count: 2
  slug: fazz-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 1
  name: Fazz Rate Limits
  slug: fazz-rate-limits
score:
  band: strong
  composite: 61.3
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 60.2
    developer_ergonomics: 76.1
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 61.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fazz/refs/heads/main/screenshots/fazz-2026-07-25T214301.png
security:
- kind: authentication
  name: Fazz Authentication
  slug: fazz-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fazz Domain Security
  slug: fazz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fazz Vulnerability Disclosure
  slug: fazz-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Fazz Trust Center
  slug: fazz-trust-center
  summary_line: trust center published
slug: fazz
tags:
- Fintech
- Payments
- Business Banking
- Disbursements
- Southeast Asia
- PayNow
- Virtual Accounts
website: https://fazz.com/
---
