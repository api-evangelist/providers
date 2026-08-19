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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 2
  name: Ozow Agentic Access
  operation_count: 5
  slug: ozow-agentic-access
  summary_line: 5 operations · 2 acting · 2 human-in-the-loop
api_count: 4
apis:
- description: Retrieve the list of supported banks for the payment flow.
  name: Ozow Banks API
  slug: ozow-banks-api
- description: Create and initiate instant EFT payment requests.
  name: Ozow Payments API
  slug: ozow-payments-api
- description: Refund previously completed EFT payments from the merchant float.
  name: Ozow Refunds API
  slug: ozow-refunds-api
- description: Query transaction status by Ozow reference or merchant reference.
  name: Ozow Transactions API
  slug: ozow-transactions-api
artifact_total: 23
asyncapis:
- description: ''
  name: Ozow Webhooks
  slug: ozow-webhooks
collections:
- collection_type: postman
  name: Ozow Banks API
  slug: postman-ozow-banks-api
- collection_type: postman
  name: Ozow Banks Payments API
  slug: postman-ozow-payments-api
- collection_type: postman
  name: Ozow Banks Refunds API
  slug: postman-ozow-refunds-api
- collection_type: postman
  name: Ozow Banks Transactions API
  slug: postman-ozow-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ozow Banks API
  slug: open-ozow-banks-api
- collection_type: open
  name: Ozow Banks Payments API
  slug: open-ozow-payments-api
- collection_type: open
  name: Ozow Banks Refunds API
  slug: open-ozow-refunds-api
- collection_type: open
  name: Ozow Banks Transactions API
  slug: open-ozow-transactions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ozow/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ozow-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ozow-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ozow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ozow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ozow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://za.linkedin.com/company/ozowsecurepayments
- group: company
  title: ''
  type: Website
  url: https://ozow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hub.ozow.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/ozow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ozow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ozow-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ozow.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.ozow.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://hub.ozow.com/docs
- group: operate
  title: ''
  type: Support
  url: https://ozow.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://ozow.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.ozow.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ozow.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ozow.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/ozow-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ozow-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ozow-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/ozow-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/ozow-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/ozow-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ozow-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/ozow-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ozow-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ozow-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ozow-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/ozow-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ozow-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ozow-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Ozow (formerly i-Pay) is a South African fintech providing an instant EFT / "Pay by Bank" payment gateway. Merchants create a server-side payment request, redirect the customer to the Ozow secure bank-selection flow, and reconcile via a server-to-server notification. The REST API is ZAR-only (CountryCode ZA), authenticated with an ApiKey header and a SHA512 HashCheck built from a merchant PrivateKey.
finops:
- name: Ozow Finops
  service_category: Payment Processing
  slug: ozow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ozow.png
layout: provider
mcp_servers:
- description: ''
  name: ozow-mcp.yml
  slug: ozow-mcpyml
modified: '2026-07-17'
name: Ozow
nav: Providers
network: true
overview: 'Ozow publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Banks API, Payments API, Refunds API, and 1 more. Tagged areas include Payments, Instant EFT, Pay by Bank, Fintech, and South Africa.


  The Ozow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ozow''s developer surface includes authentication, documentation, engineering blog, getting-started guide, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Ozow Plans Pricing
  plan_count: 2
  slug: ozow-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Ozow Rate Limits
  slug: ozow-rate-limits
score:
  band: strong
  composite: 58.9
  delta: -1.9
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 30.3
    contract_quality: 64.3
    developer_ergonomics: 32.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 28.9
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ozow/refs/heads/main/screenshots/ozow-2026-08-07T191227.png
security:
- kind: authentication
  name: Ozow Authentication
  slug: ozow-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ozow Domain Security
  slug: ozow-domain-security
  summary_line: HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ozow Vulnerability Disclosure
  slug: ozow-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ozow Trust Center
  slug: ozow-trust-center
  summary_line: PCI DSS Level 1, ISO/IEC 27001
slug: ozow
tags:
- Payments
- Instant EFT
- Pay by Bank
- Fintech
- South Africa
website: https://ozow.com/
---
