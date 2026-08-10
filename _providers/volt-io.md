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
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Volt Io Agentic Access
  operation_count: 21
  slug: volt-io-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 7
apis:
- description: 'Volt''s Global Payments API initiates account-to-account (pay by bank) payments across open-banking and real-time schemes (UK Faster Payments, SEPA, Pix, PayTo and more), creating payments, retrieving '
  name: Volt Payments API
  slug: volt-payments-api
- description: The Mandates API manages recurring account-to-account payments, including variable recurring payments (VRP) and mandate lifecycle, letting merchants set up and collect repeat bank payments under a cus
  name: Volt Mandates API
  slug: volt-mandates-api
- description: The Accounts API powers Volt Accounts and virtual IBANs for settlement, collections, payouts and refunds, giving merchants programmatic named accounts for receiving and disbursing funds within the Vol
  name: Volt Accounts API
  slug: volt-accounts-api
- description: The Verify (Account Identification) API confirms bank account ownership and details before payment, supporting confirmation-of-payee style checks to reduce misdirected payments and fraud.
  name: Volt Verify API
  slug: volt-verify-api
- description: The Reporting (Reporter) API exposes transaction, settlement and reconciliation data so merchants can retrieve reports on payments, payouts and account activity across the Volt platform.
  name: Volt Reporting API
  slug: volt-reporting-api
- description: The Authentication API issues OAuth2 access tokens for the Volt gateway. A POST to /oauth exchanges client_id, client_secret and username/password (resource-owner password grant) for a Bearer access_t
  name: Volt Authentication API
  slug: volt-authentication-api
- description: Volt Global Api Accounts from Volt, described in OpenAPI.
  name: Volt Global Api Accounts
  slug: volt-io-accounts-common
artifact_total: 13
asyncapis:
- description: ''
  name: Volt Io Webhooks
  slug: volt-io-webhooks
common:
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
  name: volt-io-mcp.yml
  slug: volt-io-mcpyml
modified: '2026-07-24'
name: Volt
nav: Providers
network: true
overview: 'Volt publishes 2 APIs on the [APIs.io](https://apis.io/) network: Accounts API and Global Api Accounts. Tagged areas include Payments, United Kingdom, Open Banking, Account-to-Account, and Real-Time Payments.


  The Volt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Volt''s developer surface includes authentication, sandbox, pricing, signup flow, documentation, API reference, getting-started guide, and 30 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 52.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 52.7
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
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
