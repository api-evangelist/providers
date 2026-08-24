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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Peachpayments Agentic Access
  operation_count: 13
  slug: peachpayments-agentic-access
  summary_line: 13 operations · 7 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: OAuth 2.0 token generation for Checkout, Payouts, and Reconciliation.
  name: Peach Payments Authentication API
  slug: peachpayments-authentication-api
- description: Hosted, Embedded, and Embedded Express checkout sessions.
  name: Peach Payments Checkout API
  slug: peachpayments-checkout-api
- description: Shareable, single-use and bulk payment links.
  name: Peach Payments Payment Links API
  slug: peachpayments-payment-links-api
- description: Server-to-server debit and refund transactions.
  name: Peach Payments Payments API
  slug: peachpayments-payments-api
- description: Merchant-initiated payouts and bank account verification.
  name: Peach Payments Payouts API
  slug: peachpayments-payouts-api
- description: Settlement and transaction reconciliation reporting.
  name: Peach Payments Reconciliation API
  slug: peachpayments-reconciliation-api
artifact_total: 29
asyncapis:
- description: ''
  name: Peachpayments Webhooks
  slug: peachpayments-webhooks
collections:
- collection_type: postman
  name: Peach Payments Authentication API
  slug: postman-peachpayments-authentication-api
- collection_type: postman
  name: Peach Payments Authentication Checkout API
  slug: postman-peachpayments-checkout-api
- collection_type: postman
  name: Peach Payments Authentication Payment Links API
  slug: postman-peachpayments-payment-links-api
- collection_type: postman
  name: Peach Authentication Payments API
  slug: postman-peachpayments-payments-api
- collection_type: postman
  name: Peach Payments Authentication Payouts API
  slug: postman-peachpayments-payouts-api
- collection_type: postman
  name: Peach Payments Authentication Reconciliation API
  slug: postman-peachpayments-reconciliation-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Peach Payments Authentication API
  slug: open-peachpayments-authentication-api
- collection_type: open
  name: Peach Payments Authentication Checkout API
  slug: open-peachpayments-checkout-api
- collection_type: open
  name: Peach Payments Authentication Payment Links API
  slug: open-peachpayments-payment-links-api
- collection_type: open
  name: Peach Authentication Payments API
  slug: open-peachpayments-payments-api
- collection_type: open
  name: Peach Payments Authentication Payouts API
  slug: open-peachpayments-payouts-api
- collection_type: open
  name: Peach Payments Authentication Reconciliation API
  slug: open-peachpayments-reconciliation-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/peachpayments-mcp.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/peach-payments/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/peachpayments-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/peachpayments-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/peachpayments-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/peachpayments-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/peachpayments-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peachpayments-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/peachpayments-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/peachpayments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/peachpayments-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peachpayments-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/peachpayments-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/peachpayments-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/peachpayments-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/peachpayments-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/peachpayments-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.peachpayments.com
- group: start
  title: ''
  type: Sandbox
  url: sandbox/peachpayments-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/peachpayments-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/peachpayments-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/peachpayments-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/peachpayments-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/peachpayments-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peach-payments
- group: company
  title: ''
  type: Website
  url: https://www.peachpayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.peachpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.peachpayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.peachpayments.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.peachpayments.com/docs/product-portfolio-overview
- group: operate
  title: ''
  type: Support
  url: https://www.peachpayments.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.peachpayments.com/scale
- group: commercial
  title: ''
  type: Pricing
  url: https://www.peachpayments.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://www.peachpayments.com/get-started
- group: start
  title: ''
  type: Login
  url: https://dashboard.peachpayments.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peachpayments.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peachpayments.com/legal
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/peachpayments/peach-payments-public-workspace
- group: commercial
  title: ''
  type: Plans
  url: plans/peachpayments-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/peachpayments-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/peachpayments-finops.yml
created: '2026-07-17'
description: Peach Payments is a pan-African payment orchestration gateway founded in 2012 in Cape Town, South Africa, operating across South Africa, Kenya, and Mauritius. Its PCI DSS Level 1 platform exposes REST APIs for Checkout (Hosted, Embedded, Embedded Express), server-to-server Payments, Payment Links, Payouts, and Reconciliation, supporting cards plus local methods like PayShap, Capitec Pay, 1Voucher, Mobicred, M-PESA, and MauCAS in ZAR, KES, and MUR.
finops:
- name: Peachpayments Finops
  service_category: Payments and Financial Services
  slug: peachpayments-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peachpayments.png
layout: provider
mcp_servers:
- description: ''
  name: Peach Payments MCP Server
  slug: peach-payments-mcp-server
modified: '2026-07-17'
name: Peach Payments
nav: Providers
network: true
overview: 'Peach Payments publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Checkout API, Payment Links API, and 3 more. Tagged areas include Payments, Fintech, Africa, Payment Gateway, and Checkout.


  The Peach Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Peach Payments'' developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 35 more developer resources.'
plans:
- name: Peachpayments Plans Pricing
  plan_count: 2
  slug: peachpayments-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Peachpayments Rate Limits
  slug: peachpayments-rate-limits
score:
  band: exemplar
  composite: 72.7
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 30.3
    contract_quality: 64.5
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 71.1
  previous_composite: 72.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peachpayments/refs/heads/main/screenshots/peachpayments-2026-08-07T191724.png
security:
- kind: authentication
  name: Peachpayments Authentication
  slug: peachpayments-authentication
  summary_line: http/inline-credentials · 3 schemes
- kind: domain-security
  name: Peachpayments Domain Security
  slug: peachpayments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Peachpayments Vulnerability Disclosure
  slug: peachpayments-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Peachpayments Trust Center
  slug: peachpayments-trust-center
  summary_line: PCI DSS Level 1, PCI DSS v4.0
slug: peachpayments
tags:
- Payments
- Fintech
- Africa
- Payment Gateway
- Checkout
- Payouts
website: https://www.peachpayments.com/
---
