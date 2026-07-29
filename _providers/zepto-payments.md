---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Zepto Payments Agentic Access
  operation_count: 72
  slug: zepto-payments-agentic-access
  summary_line: 72 operations · 37 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Zepto's core account-to-account payments API — move money over the New Payments Platform (NPP), BECS Direct Entry and PayID with payments, payouts, payment requests, transfers, refunds, agreements, co
  name: Zepto API
  slug: zepto-api
- description: Programmatic PayTo mandate management and real-time collection — create, amend, suspend, reactivate and cancel PayTo agreements, then collect authorised real-time payments and issue refunds against th
  name: Zepto PayTo API
  slug: payto-api
- description: Confirmation of Payee (CoP) account validation — verify that a payee's account name matches the account details in real time before initiating a payment, reducing misdirected payments and payment frau
  name: Zepto Validate API (Confirmation of Payee)
  slug: validate-cop-api
- description: Disputes and investigations (Beta) — raise and manage payment disputes, respond to action requests (accept, reject, upload evidence) and simulate incoming investigation messages in sandbox.
  name: Zepto Investigations API
  slug: investigations-api
- description: Client management (Alpha) — create and manage sub-clients and their Merchant Category Codes (MCC) for platform and marketplace models operating on top of Zepto's rails.
  name: Zepto Clients API
  slug: clients-api
- description: Merchant reporting — download PayTo settlement reports by report date for reconciliation of collected and settled funds.
  name: Zepto Merchant Reports API
  slug: merchant-reports-api
- description: Webhook event notifications — subscribe to asynchronous payment and account events (for example float_accounts.unmatched_credit.received) to drive real-time reconciliation and payment status handling.
  name: Zepto Notifications API (Webhooks)
  slug: notifications-api
artifact_total: 22
asyncapis:
- description: ''
  name: Zepto Payments Notifications Webhooks
  slug: zepto-payments-notifications-webhooks
collections:
- collection_type: postman
  name: Zepto Clients API (Alpha)
  slug: postman-zepto-payments-clients
- collection_type: postman
  name: Zepto Investigations API
  slug: postman-zepto-payments-investigations
- collection_type: postman
  name: Zepto Merchant Reports API
  slug: postman-zepto-payments-merchant-reports
- collection_type: postman
  name: Notifications
  slug: postman-zepto-payments-notifications
- collection_type: postman
  name: Zepto PayTo API
  slug: postman-zepto-payments-pay-to
- collection_type: postman
  name: Zepto Validate API (Confirmation of Payee)
  slug: postman-zepto-payments-validate-cop
- collection_type: postman
  name: Zepto API
  slug: postman-zepto-payments-zepto
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zepto/overview
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zepto-payments-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zepto-payments-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zepto-payments-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zepto-payments-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zepto-payments-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://zepto.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zepto.com.au/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zeptopayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zeptopayments.com/reference/openapi-specifications
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zeptopayments.com/docs/getting-started-in-sandbox
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.zeptopayments.com/reference/change-log
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zeptopayments.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.zepto.money/en/
- group: start
  title: ''
  type: Login
  url: https://go.zeptopayments.com/sign_in
- group: company
  title: ''
  type: Blog
  url: https://zepto.com.au/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zepto-payments
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zepto.com.au/website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zepto.com.au/legal-and-privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zeptofs
- group: build
  title: ''
  type: Packages
  url: packages/zepto-payments-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zepto-payments-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zepto-payments-security.txt
- group: auth
  title: ''
  type: Security
  url: https://zepto.com.au/uploads/documents/Vulnerability-Disclosure-Policy.pdf
- group: auth
  title: ''
  type: TrustCenter
  url: security/zepto-payments-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://zepto.com.au/platform-and-accreditations
- group: design
  title: ''
  type: Conformance
  url: conformance/zepto-payments-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zepto-payments-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zepto-payments-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zepto-payments-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zepto-payments-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zepto-payments-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/zepto-payments-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zepto-payments-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zepto-payments-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zepto-payments-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zepto-payments-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zepto-payments-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zepto-payments-zepto-overlay.yaml
created: '2026-07-24'
description: 'Zepto is a Gold Coast, Australia based account-to-account (A2A) payments company that gives merchants and platforms programmable, real-time access to Australia''s core money-movement rails. Its unified REST API moves money over the New Payments Platform (NPP) for instant account-to-account payments, PayTo for mandated real-time debits, PayID addressing, BECS Direct Entry (direct debit and direct credit), and stored-value float accounts, with real-time messaging, settlement and reconciliation. Zepto is the first non-authorised-deposit-taking institution (non-ADI) approved to connect directly to the NPP as a "Connected Institution" for PayTo, positioning it as an infrastructure-grade money-movement provider rather than a card acquirer. Its API posture is genuinely developer-first and API-native: a public ReadMe developer portal, a full sandbox, idempotent asynchronous payment flows, webhook notifications, and seven downloadable OpenAPI specifications covering the core payments
  API, PayTo, Confirmation of Payee (Validate), disputes, clients, merchant reports and notifications.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: zepto-payments-mcp.yml
  slug: zepto-payments-mcpyml
modified: '2026-07-24'
name: Zepto
nav: Providers
network: true
overview: 'Zepto publishes 7 APIs on the [APIs.io](https://apis.io/) network, including PayTo API, Validate API (Confirmation of Payee), and 5 more. Tagged areas include Payments, Australia, Real-Time Payments, Account-to-Account, and New Payments Platform.


  The Zepto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zepto''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, engineering blog, sandbox, and 33 more developer resources.'
random_paper: 25
scopes:
- name: Zepto Payments Scopes
  scope_count: 9
  slug: zepto-payments-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: strong
  composite: 57.8
  delta: -4.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.2
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 85.7
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Zepto Payments Authentication
  slug: zepto-payments-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zepto Payments Domain Security
  slug: zepto-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zepto Payments Vulnerability Disclosure
  slug: zepto-payments-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zepto Payments Trust Center
  slug: zepto-payments-trust-center
  summary_line: PCI DSS Level 1 (v4.0), ISO/IEC 27001, ASAE 3150 (independently certified by RSM Australia), CIS Benchmark Level 2, ISO 9362 (registered SWIFT BIC SPPYAU22)
slug: zepto-payments
tags:
- Payments
- Australia
- Real-Time Payments
- Account-to-Account
- New Payments Platform
- PayTo
- PayID
- Direct Entry
- Open Banking
- Money Movement
website: https://zepto.com.au/
---
