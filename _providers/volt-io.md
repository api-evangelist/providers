---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Volt Io Agentic Access
  operation_count: 21
  slug: volt-io-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- description: 'Volt''s Global Payments API initiates account-to-account (pay by bank) payments across open-banking and real-time schemes (UK Faster Payments, SEPA, Pix, PayTo and more), creating payments, retrieving '
  name: Volt Payments API
  slug: volt-payments-api
- description: The Mandates API manages recurring account-to-account payments, including variable recurring payments (VRP) and mandate lifecycle, letting merchants set up and collect repeat bank payments under a cus
  name: Volt Mandates API
  slug: volt-mandates-api
- description: The Verify (Account Identification) API confirms bank account ownership and details before payment, supporting confirmation-of-payee style checks to reduce misdirected payments and fraud.
  name: Volt Verify API
  slug: volt-verify-api
- description: The Reporting (Reporter) API exposes transaction, settlement and reconciliation data so merchants can retrieve reports on payments, payouts and account activity across the Volt platform.
  name: Volt Reporting API
  slug: volt-reporting-api
- description: The Authentication API issues OAuth2 access tokens for the Volt gateway. A POST to /oauth exchanges client_id, client_secret and username/password (resource-owner password grant) for a Bearer access_t
  name: Volt Authentication API
  slug: volt-authentication-api
- description: Verification services for ensuring beneficiary account ownership.
  name: Volt Account Holder Verification API
  slug: volt-io-account-holder-verification-api
- description: Management of accounts.
  name: Volt Accounts API
  slug: volt-io-accounts-api
- description: Issuance and management of account aliases for global reconciliation.
  name: Volt Aliases API
  slug: volt-io-aliases-api
- description: Named account order operations.
  name: Volt Named Accounts API
  slug: volt-io-named-accounts-api
- description: Operations related to sandbox operations.
  name: Volt Sandbox API
  slug: volt-io-sandbox-api
- description: Operations related to movement of funds, including payouts, settlements, and internal transactions.
  name: Volt Transactions API
  slug: volt-io-transactions-api
- description: Operations related to trusted accounts.
  name: Volt Trusted accounts API
  slug: volt-io-trusted-accounts-api
artifact_total: 18
asyncapis:
- description: ''
  name: Volt Io Webhooks
  slug: volt-io-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/volt-io-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/volt-io-accounts-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/volt-io-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/volt-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volt-io-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/volt-io-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/volt-io-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://www.volt.io/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/volt-io-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/volt-io-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/volt-io-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/volt-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/volt-io-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/volt-io-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/volt-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/volt-io-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/volt-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://volt.io/compliance/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/volt-io-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.volt.io/implementation/payments/migration-guide
- group: start
  title: ''
  type: Sandbox
  url: sandbox/volt-io-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/volt-io-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/volt-io-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volt-io
- group: commercial
  title: ''
  type: Pricing
  url: https://volt.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://docs.volt.io/onboarding
- group: company
  title: ''
  type: Website
  url: https://volt.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://volt.io/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.volt.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.volt.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.volt.io/get-started
- group: operate
  title: ''
  type: StatusPage
  url: https://status.volt.io/
- group: company
  title: ''
  type: Blog
  url: https://volt.io/content-hub/
- group: company
  title: ''
  type: Newsroom
  url: https://volt.io/newsroom/
- group: start
  title: ''
  type: Login
  url: https://fuzebox.volt.io/
- group: operate
  title: ''
  type: Support
  url: https://volt.io/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://volt.io/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://volt.io/legal/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voltio
created: '2026-07-24'
description: 'Volt is a London-headquartered real-time payments company that operates a global account-to-account (A2A) "pay by bank" network built on open banking rails. Founded in 2019, Volt connects merchants to bank-initiated payments across the UK (Faster Payments / Open Banking under PSD2), Europe (SEPA), Brazil (Pix), Australia (PayTo), and other real-time schemes through a single API, so shoppers pay directly from their bank account without cards. Its platform spans payment initiation, refunds, payouts, recurring payments (mandates / variable recurring payments), Volt Accounts and virtual IBANs for settlement and collections, account verification (confirmation of payee), and reconciliation reporting. Volt sells to merchants and PSPs across ecommerce, travel, gaming, iGaming and financial services, and is FCA-authorised in its home market of the United Kingdom. Volt ships a genuine, API-native developer surface: a public developer portal and OpenAPI-backed API reference at docs.volt.io,
  a single production gateway host (gateway.volt.io) with a sandbox, OAuth2 authentication, and webhooks for asynchronous payment events. The docs.volt.io API reference renders schemas server-side, but Volt publishes a real OpenAPI 3.0.1 definition for its Accounts API (virtual IBANs, named accounts, settlement) in the github.com/volt-io/volt-io-accounts repository, and ships first-party mobile checkout SDKs (iOS/Android) plus e-commerce plugins in the same GitHub organization.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Volt MCP Server
  slug: volt-mcp-server
modified: '2026-07-24'
name: Volt
nav: Providers
network: true
overview: 'Volt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account Holder Verification API, Accounts API, Aliases API, and 4 more. Tagged areas include Payments, United Kingdom, Open Banking, Account-to-Account, and Real-Time Payments.


  The Volt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Volt''s developer surface includes authentication, sandbox, pricing, signup flow, documentation, API reference, getting-started guide, and 33 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 62.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/volt-io/refs/heads/main/screenshots/volt-io-2026-08-17T082816.png
security:
- kind: authentication
  name: Volt Io Authentication
  slug: volt-io-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Volt Io Domain Security
  slug: volt-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Volt Io Vulnerability Disclosure
  slug: volt-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: volt-io
tags:
- Payments
- United Kingdom
- Open Banking
- Account-to-Account
- Real-Time Payments
- Payment Initiation
- Payouts
- Recurring Payments
- Cross-Border
- Pay by Bank
website: https://volt.io/
---
