---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 258
  human_in_the_loop: 0
  name: Vopay Agentic Access
  operation_count: 404
  slug: vopay-agentic-access
  summary_line: 404 operations · 258 acting
api_count: 23
apis:
- description: VoPay's Accounts API — 44 documented operation(s) across 40 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Accounts API
  slug: vopay-account-api-reference
- description: VoPay's Account Onboarding API — 9 documented operation(s) across 9 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Account Onboarding API
  slug: vopay-account-onboarding
- description: VoPay's Bill Pay API — 8 documented operation(s) across 8 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Bill Pay API
  slug: vopay-bill-pay-references
- description: VoPay's Blocked Accounts API — 3 documented operation(s) across 3 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Blocked Accounts API
  slug: vopay-blocked-accounts-api-reference
- description: VoPay's Branding API — 6 documented operation(s) across 6 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Branding API
  slug: vopay-branding-api-reference
- description: VoPay's Client Accounts API — 41 documented operation(s) across 40 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Client Accounts API
  slug: vopay-client-accounts
- description: VoPay's Contact API — 15 documented operation(s) across 15 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Contact API
  slug: vopay-contact
- description: VoPay's Convenience Fees API — 6 documented operation(s) across 2 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Convenience Fees API
  slug: vopay-convenience-fee-api-reference
- description: VoPay's Dispute Management Endpoints API — 11 documented operation(s) across 11 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Dispute Management Endpoints API
  slug: vopay-dispute-management-api-reference
- description: VoPay's eLinx API — 5 documented operation(s) across 3 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay eLinx API
  slug: vopay-elinx
- description: VoPay's File Conversion API — 8 documented operation(s) across 8 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay File Conversion API
  slug: vopay-file-conversion-api-reference
- description: VoPay's Global Cash Management API — 35 documented operation(s) across 35 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Global Cash Management API
  slug: vopay-global-cash-management
- description: VoPay's Integrations and Support API — 32 documented operation(s) across 32 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Integrations and Support API
  slug: vopay-integrations-and-support
- description: VoPay's IQ11 API — 8 documented operation(s) across 7 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay IQ11 API
  slug: vopay-iq11
- description: VoPay's Payments API — 1 documented operation(s) across 1 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Payments API
  slug: vopay-payment-api-reference
- description: VoPay's Payment Methods API — 51 documented operation(s) across 51 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Payment Methods API
  slug: vopay-payment-method-api-reference
- description: VoPay's Payment Rails API — 85 documented operation(s) across 85 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Payment Rails API
  slug: vopay-payment-rails-api-reference
- description: VoPay's Ping API — 3 documented operation(s) across 3 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Ping API
  slug: vopay-ping
- description: VoPay's Remittance API API — 1 documented operation(s) across 1 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Remittance API API
  slug: vopay-remittance-api-reference
- description: VoPay's Scheduled Payments API — 6 documented operation(s) across 5 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Scheduled Payments API
  slug: vopay-scheduled-payments-api-reference
- description: VoPay's Transaction Management API — 7 documented operation(s) across 7 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Transaction Management API
  slug: vopay-transaction-management
- description: VoPay's Verification API — 13 documented operation(s) across 13 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Verification API
  slug: vopay-verification
- description: VoPay's Virtual Accounts API — 6 documented operation(s) across 5 path(s) on VoPay's API-first embedded finance platform for Canadian and cross-border money movement.
  name: VoPay Virtual Accounts API
  slug: vopay-virtual-account-api-reference
artifact_total: 29
asyncapis:
- description: VoPay webhook (event notification) surface. VoPay delivers 24 event types via HTTP POST to the URL configured with account/webhook-url or partner/webhook-url. Every payload carries a ValidationKey = s
  name: VoPay Webhooks
  slug: vopay-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vopay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vopay-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vopay-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://vopay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vopay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vopay.com/docs/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vopay.com/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vopay.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://vopay.com/api-sandbox/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vopay.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://vopay.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.vopay.com/
- group: operate
  title: ''
  type: Support
  url: https://vopay.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vopay.com/legal/term-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vopay.com/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vopay
- group: auth
  title: ''
  type: Authentication
  url: authentication/vopay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vopay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vopay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vopay-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/vopay-decline-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vopay-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vopay-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vopay-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vopay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vopay-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/vopay-packages.yml
- group: design
  title: ''
  type: Components
  url: components/vopay-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vopay-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vopay-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vopay-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vopay-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/vopay-tool-crosswalk.yml
- group: auth
  title: ''
  type: Security
  url: https://vopay.com/.well-known/security.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/vopay-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vopay-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/vopay-eft-collect-funds.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/vopay-verify-bank-account-iq11.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/vopay-interac-request-money.md
created: '2026-07-24'
description: VoPay is a Vancouver, Canada based fintech offering an API-first embedded finance and payments-as-a-service platform that lets software companies, marketplaces, lenders, and enterprises move money across Canadian and North American bank rails from a single set of REST endpoints. Its Fintech-as-a-Service suite spans EFT, Interac e-Transfer, ACH, RTP/FedNow/FedWire, VoPay Instant, card and digital-wallet payments, cross-border and global cash management, virtual accounts, ledgering, scheduled and recurring payments, bank-account verification (IQ11), KYC/AML onboarding, and dispute management. VoPay ships a genuine public developer portal (docs.vopay.com) with a sandbox, an OpenAPI-backed API reference segmented by product, webhooks for transaction and account events, and API-key-plus-shared-secret signature authentication with IP whitelisting. Its home market is Canada, where it operates as an API-native money-movement layer over Interac and Payments Canada rails.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: vopay-mcp.yml
  slug: vopay-mcpyml
modified: '2026-07-24'
name: VoPay
nav: Providers
network: true
overview: 'VoPay publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Account Onboarding API, Bill Pay API, and 20 more. Tagged areas include Payments, Canada, Embedded Finance, Payments as a Service, and Account-to-Account.


  The VoPay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VoPay''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 32 more developer resources.'
random_paper: 95
score:
  band: developing
  composite: 52.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.3
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Vopay Authentication
  slug: vopay-authentication
  summary_line: apiKey/signature · 1 scheme
- kind: domain-security
  name: Vopay Domain Security
  slug: vopay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vopay Vulnerability Disclosure
  slug: vopay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vopay
tags:
- Payments
- Canada
- Embedded Finance
- Payments as a Service
- Account-to-Account
- EFT
- Interac e-Transfer
- ACH
- Real-Time Payments
- Cross-Border
- Money Transfer
- Bank Account Verification
- KYC
- Virtual Accounts
- Open Banking
website: https://vopay.com/
---
