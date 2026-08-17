---
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
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Azupay Agentic Access
  operation_count: 37
  slug: azupay-agentic-access
  summary_line: 37 operations · 25 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: 'Receive real-time account-to-account payments from customers by creating PayID-addressed payment requests. Create, retrieve, search, delete, and refund PaymentRequests; poll payment status to confirm '
  name: Azupay PaymentRequest API (AzupayId)
  slug: azupay-payment-request-api
- description: Send outbound NPP payments to a PayID or to a BSB and account number, then poll for settlement status. Search prior payments. Part of Azupay's AzupayOut disbursement/payout product for real-time money
  name: Azupay Payment API (AzupayOut)
  slug: azupay-payment-api
- description: Establish and manage PayTo payment agreements and initiate eligible debits against them. Create, amend, change status, and search agreements; create payment agreement requests; schedule payments; init
  name: Azupay PaymentAgreement & Initiation API (AzupayTo / PayTo)
  slug: azupay-payment-agreement-api
- description: 'Reduce misdirected-payment and fraud risk with real-time account checks. Confirm a payee''s BSB/account number and name via Confirmation of Payee (CoP), check whether an account issuer can receive NPP '
  name: Azupay Account Check API (Confirmation of Payee)
  slug: azupay-check-accounts-api
- description: Retrieve daily transaction reports by month or date range, obtain time-limited download links for reports, and check the current balance of an Azupay client account.
  name: Azupay Report & Balance API
  slug: azupay-reports-api
- description: Manage the platform configuration for an Azupay integration. Create, replace, and disable sub-clients; provision, retrieve, and update API keys for sub merchants; enable and read OAuth 2.0 configurati
  name: Azupay Clients & API Key Management API
  slug: azupay-configuration-api
artifact_total: 18
asyncapis:
- description: ''
  name: Azupay Webhooks
  slug: azupay-webhooks
collections:
- collection_type: open
  name: Azupay Check Accounts API
  slug: open-azupay-check-accounts
- collection_type: open
  name: Azupay Configuration API
  slug: open-azupay-configuration
- collection_type: open
  name: Azupay Payment Agreement API
  slug: open-azupay-payment-agreement
- collection_type: open
  name: Azupay Payment Request API
  slug: open-azupay-payment-request
- collection_type: open
  name: Azupay Payment API
  slug: open-azupay-payment
- collection_type: open
  name: Azupay Reports & Balance API
  slug: open-azupay-reports
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azupay-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azupay-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azupay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://azupay.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.azupay.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.azupay.com.au/docs/getting-started-1
- group: docs
  title: ''
  type: APIReference
  url: https://developer.azupay.com.au/reference/createpayidpaymentrequest
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.azupay.com.au/docs/getting-started-1
- group: start
  title: ''
  type: SignUp
  url: https://developer.azupay.com.au/docs/signing-up
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.azupay.com.au/changelog
- group: design
  title: ''
  type: Webhooks
  url: https://developer.azupay.com.au/docs/webhooks
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcentre.azupay.com.au/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azupay.com.au/
- group: commercial
  title: ''
  type: Pricing
  url: https://azupay.com.au/pricing
- group: company
  title: ''
  type: Blog
  url: https://azupay.com.au/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azupay.com.au/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://azupay.com.au/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://dashboard.azupay.com.au/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azupay-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/azupay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/azupay-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/azupay-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.azupay.com.au/docs/getting-started-1
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/azupay-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/azupay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/azupay-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/azupay-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/azupay-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/azupay-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/azupay-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/azupay-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/azupay-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: 'Azupay is an Australian real-time payments company that moves money over the New Payments Platform (NPP), the account-to-account rails operated by Australian Payments Plus. It is API-first: merchants and platforms embed Azupay to receive payments via PayID (AzupayId), send outbound payments to a PayID or BSB/account number (AzupayOut), and collect recurring or on-demand debits through PayTo mandates and payment agreements (AzupayTo). Azupay also offers Confirmation of Payee (CoP) account checks and PayID enquiry to reduce misdirected-payment and fraud risk, batch/file (ABA and SFTP) processing for bulk payouts and collections, reporting, balance management, sub-client and API-key management, and hosted UX apps (Pay by Bank, Disbursements, Subscriptions). Its public developer portal documents a REST API at api.azupay.com.au/v1 with a UAT environment, authenticated by API key (secret and distributable keys in the Authorization header) with OAuth 2.0 client-credentials available
  as an additional server-to-server option, plus webhooks for asynchronous payment status. Home market is Australia; the surface is genuinely self-serve and documented, though production access and some capabilities (sub-clients, OAuth2) are enabled per client by Azupay.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: azupay-mcp.yml
  slug: azupay-mcpyml
modified: '2026-07-24'
name: Azupay
nav: Providers
network: true
overview: 'Azupay publishes 6 APIs on the [APIs.io](https://apis.io/) network, including PaymentRequest API (AzupayId), Payment API (AzupayOut), PaymentAgreement & Initiation API (AzupayTo / PayTo), and 3 more. Tagged areas include Payments, Australia, Real-Time Payments, Account-to-Account, and New Payments Platform.


  The Azupay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Azupay''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, changelog, pricing, and 26 more developer resources.'
random_paper: 70
scopes:
- name: Azupay Scopes
  scope_count: 1
  slug: azupay-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 55.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 69.7
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    conformance: derived
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
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 58.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azupay/refs/heads/main/screenshots/azupay-2026-07-25T202124.png
security:
- kind: authentication
  name: Azupay Authentication
  slug: azupay-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Azupay Domain Security
  slug: azupay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azupay
tags:
- Payments
- Australia
- Real-Time Payments
- Account-to-Account
- New Payments Platform
- PayID
- PayTo
- Money Transfer
- Confirmation of Payee
- Open Banking
website: https://azupay.com.au/
---
