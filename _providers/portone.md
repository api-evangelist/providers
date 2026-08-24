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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 89
  human_in_the_loop: 34
  name: Portone Agentic Access
  operation_count: 147
  slug: portone-agentic-access
  summary_line: 147 operations · 89 acting · 34 human-in-the-loop
api_count: 20
apis:
- description: Legacy V1 (Iamport) REST API on api.iamport.kr — token-authenticated (POST /users/getToken with imp_key/imp_secret) payment lookup, cancellation, non-authenticated and scheduled payments, virtual acco
  name: PortOne REST API (V1, legacy Iamport)
  slug: portone-rest-api-v1
- description: The B2b API from PortOne — 26 operation(s) for b2b.
  name: PortOne B2b API
  slug: portone-b2b-api
- description: The Banks API from PortOne — 1 operation(s) for banks.
  name: PortOne Banks API
  slug: portone-banks-api
- description: The Billing Keys API from PortOne — 4 operation(s) for billing keys.
  name: PortOne Billing Keys API
  slug: portone-billing-keys-api
- description: The Cash Receipts API from PortOne — 1 operation(s) for cash receipts.
  name: PortOne Cash Receipts API
  slug: portone-cash-receipts-api
- description: The Checkout Profiles API from PortOne — 1 operation(s) for checkout profiles.
  name: PortOne Checkout Profiles API
  slug: portone-checkout-profiles-api
- description: The Identity Verifications API from PortOne — 5 operation(s) for identity verifications.
  name: PortOne Identity Verifications API
  slug: portone-identity-verifications-api
- description: The Kakaopay API from PortOne — 1 operation(s) for kakaopay.
  name: PortOne Kakaopay API
  slug: portone-kakaopay-api
- description: The Login API from PortOne — 1 operation(s) for login.
  name: PortOne Login API
  slug: portone-login-api
- description: The Payment Events By Cursor API from PortOne — 1 operation(s) for payment events by cursor.
  name: PortOne Payment Events By Cursor API
  slug: portone-payment-events-by-cursor-api
- description: The Payment Gateways API from PortOne — 1 operation(s) for payment gateways.
  name: PortOne Payment Gateways API
  slug: portone-payment-gateways-api
- description: The Payment Reconciliations API from PortOne — 2 operation(s) for payment reconciliations.
  name: PortOne Payment Reconciliations API
  slug: portone-payment-reconciliations-api
- description: The Payment Schedules API from PortOne — 2 operation(s) for payment schedules.
  name: PortOne Payment Schedules API
  slug: portone-payment-schedules-api
- description: The Payment Sessions API from PortOne — 3 operation(s) for payment sessions.
  name: PortOne Payment Sessions API
  slug: portone-payment-sessions-api
- description: The Payments API from PortOne — 18 operation(s) for payments.
  name: PortOne Payments API
  slug: portone-payments-api
- description: The Payments By Cursor API from PortOne — 1 operation(s) for payments by cursor.
  name: PortOne Payments By Cursor API
  slug: portone-payments-by-cursor-api
- description: The Paymentwall API from PortOne — 1 operation(s) for paymentwall.
  name: PortOne Paymentwall API
  slug: portone-paymentwall-api
- description: The Platform API from PortOne — 44 operation(s) for platform.
  name: PortOne Platform API
  slug: portone-platform-api
- description: The Promotions API from PortOne — 1 operation(s) for promotions.
  name: PortOne Promotions API
  slug: portone-promotions-api
- description: The Token API from PortOne — 1 operation(s) for token.
  name: PortOne Token API
  slug: portone-token-api
artifact_total: 69
asyncapis:
- description: ''
  name: Portone Webhooks
  slug: portone-webhooks
collections:
- collection_type: postman
  name: PortOne B2b API
  slug: postman-portone-b2b-api
- collection_type: postman
  name: PortOne B2b Banks API
  slug: postman-portone-banks-api
- collection_type: postman
  name: PortOne B2b Billing Keys API
  slug: postman-portone-billing-keys-api
- collection_type: postman
  name: PortOne B2b Cash Receipts API
  slug: postman-portone-cash-receipts-api
- collection_type: postman
  name: PortOne B2b Checkout Profiles API
  slug: postman-portone-checkout-profiles-api
- collection_type: postman
  name: PortOne B2b Identity Verifications API
  slug: postman-portone-identity-verifications-api
- collection_type: postman
  name: PortOne B2b Kakaopay API
  slug: postman-portone-kakaopay-api
- collection_type: postman
  name: PortOne B2b Login API
  slug: postman-portone-login-api
- collection_type: postman
  name: PortOne B2b Payment Events By Cursor API
  slug: postman-portone-payment-events-by-cursor-api
- collection_type: postman
  name: PortOne B2b Payment Gateways API
  slug: postman-portone-payment-gateways-api
- collection_type: postman
  name: PortOne B2b Payment Reconciliations API
  slug: postman-portone-payment-reconciliations-api
- collection_type: postman
  name: PortOne B2b Payment Schedules API
  slug: postman-portone-payment-schedules-api
- collection_type: postman
  name: PortOne B2b Payment Sessions API
  slug: postman-portone-payment-sessions-api
- collection_type: postman
  name: PortOne B2b Payments API
  slug: postman-portone-payments-api
- collection_type: postman
  name: PortOne B2b Payments By Cursor API
  slug: postman-portone-payments-by-cursor-api
- collection_type: postman
  name: PortOne B2b Paymentwall API
  slug: postman-portone-paymentwall-api
- collection_type: postman
  name: PortOne B2b Platform API
  slug: postman-portone-platform-api
- collection_type: postman
  name: PortOne B2b Promotions API
  slug: postman-portone-promotions-api
- collection_type: postman
  name: PortOne B2b Token API
  slug: postman-portone-token-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PortOne B2b API
  slug: open-portone-b2b-api
- collection_type: open
  name: PortOne B2b Banks API
  slug: open-portone-banks-api
- collection_type: open
  name: PortOne B2b Billing Keys API
  slug: open-portone-billing-keys-api
- collection_type: open
  name: PortOne B2b Cash Receipts API
  slug: open-portone-cash-receipts-api
- collection_type: open
  name: PortOne B2b Checkout Profiles API
  slug: open-portone-checkout-profiles-api
- collection_type: open
  name: PortOne B2b Identity Verifications API
  slug: open-portone-identity-verifications-api
- collection_type: open
  name: PortOne B2b Kakaopay API
  slug: open-portone-kakaopay-api
- collection_type: open
  name: PortOne B2b Login API
  slug: open-portone-login-api
- collection_type: open
  name: PortOne B2b Payment Events By Cursor API
  slug: open-portone-payment-events-by-cursor-api
- collection_type: open
  name: PortOne B2b Payment Gateways API
  slug: open-portone-payment-gateways-api
- collection_type: open
  name: PortOne B2b Payment Reconciliations API
  slug: open-portone-payment-reconciliations-api
- collection_type: open
  name: PortOne B2b Payment Schedules API
  slug: open-portone-payment-schedules-api
- collection_type: open
  name: PortOne B2b Payment Sessions API
  slug: open-portone-payment-sessions-api
- collection_type: open
  name: PortOne B2b Payments API
  slug: open-portone-payments-api
- collection_type: open
  name: PortOne B2b Payments By Cursor API
  slug: open-portone-payments-by-cursor-api
- collection_type: open
  name: PortOne B2b Paymentwall API
  slug: open-portone-paymentwall-api
- collection_type: open
  name: PortOne B2b Platform API
  slug: open-portone-platform-api
- collection_type: open
  name: PortOne B2b Promotions API
  slug: open-portone-promotions-api
- collection_type: open
  name: PortOne B2b Token API
  slug: open-portone-token-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/portone/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/portone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/portone-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/portone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/portone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/portone-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portoneglobal
- group: company
  title: ''
  type: Website
  url: https://portone.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.portone.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/portone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/portone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/portone-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://developers.portone.io/opi/ko/support/release-note
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.portone.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.portone.io/opi/ko/quick-guide/payment
- group: operate
  title: ''
  type: Support
  url: https://developers.portone.io/opi/ko/support/contact
- group: start
  title: ''
  type: SignUp
  url: https://admin.portone.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terms.portone.io/
- group: build
  title: ''
  type: Packages
  url: packages/portone-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/portone-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/portone-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/portone-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/portone-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/portone-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/portone-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/portone-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/portone-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/portone-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/portone-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/portone-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/portone-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/portone-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://iamport.github.io/service-status/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.portone.io/api/backward-compatibility
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/portone-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/portone-webhooks.yml
created: '2026-07-17'
description: PortOne (formerly Iamport) is a Korea-based payment orchestration platform that lets online businesses integrate one API to reach 100+ Korean and global payment methods and PSPs. The V2 REST API (api.portone.io) covers payments, billing keys, scheduled/recurring payments, identity verification, cash receipts, B2B tax invoices, and partner settlement, with the legacy V1 API still served at api.iamport.kr.
finops:
- name: Portone Finops
  service_category: Payments and Financial Services
  slug: portone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portone.png
layout: provider
mcp_servers:
- description: ''
  name: PortOne MCP Server
  slug: portone-mcp-server
modified: '2026-07-17'
name: PortOne
nav: Providers
network: true
overview: 'PortOne publishes 19 APIs on the [APIs.io](https://apis.io/) network, including B2b API, Banks API, Billing Keys API, and 16 more. Tagged areas include Payments, Payment Orchestration, Fintech, Korea, and Billing.


  The PortOne catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PortOne''s developer surface includes authentication, documentation, engineering blog, getting-started guide, support, signup flow, CLI, and 31 more developer resources.'
plans:
- name: Portone Plans Pricing
  plan_count: 3
  slug: portone-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Portone Rate Limits
  slug: portone-rate-limits
score:
  band: strong
  composite: 61.8
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 65.4
    developer_ergonomics: 78.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 65.8
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portone/refs/heads/main/screenshots/portone-2026-08-17T081325.png
security:
- kind: authentication
  name: Portone Authentication
  slug: portone-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Portone Domain Security
  slug: portone-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Portone Vulnerability Disclosure
  slug: portone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Portone Trust Center
  slug: portone-trust-center
  summary_line: PCI DSS, ISMS
slug: portone
tags:
- Payments
- Payment Orchestration
- Fintech
- Korea
- Billing
- Identity Verification
website: https://portone.io/
---
