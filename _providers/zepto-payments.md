---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Zepto Payments Agentic Access
  operation_count: 72
  slug: zepto-payments-agentic-access
  summary_line: 72 operations · 37 acting · 1 human-in-the-loop
api_count: 7
apis:
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Modify existing agreements
  name: Zepto Agreement modification API
  slug: zepto-payments-agreement-modification-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Create and query agreements
  name: Zepto Agreements API
  slug: zepto-payments-agreements-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Resolve the display name associated with a PayID alias
  name: Zepto Alias Resolution API
  slug: zepto-payments-alias-resolution-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Your currently linked up bank accounts.
  name: Zepto Bank Accounts API
  slug: zepto-payments-bank-accounts-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: The Zepto Clients API allows registration of clients who indirectly use the Zepto platform via your Zepto integration.
  name: Zepto Clients API
  slug: zepto-payments-clients-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: 'Your Contacts form an address book of parties with whom you can interact. In order to initiate any type of transaction you must first have the party in your Contact list. <aside class="notice">In the '
  name: Zepto Contacts API
  slug: zepto-payments-contacts-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: The Contacts (Receivable) API from Zepto — 4 operation(s) for contacts (receivable).
  name: Zepto Contacts (Receivable) API
  slug: zepto-payments-contacts-receivable-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: The CoP Account Validations API from Zepto — 1 operation(s) for cop account validations.
  name: Zepto CoP Account Validations API
  slug: zepto-payments-cop-account-validations-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: The Zepto Disputes API is for managing disputes. Access to this API is limited. Please contact Zepto for more information.
  name: Zepto Disputes (Beta) API
  slug: zepto-payments-disputes-beta-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Webhooks relating to out of band activity on float bank accounts
  name: Zepto Float Accounts API
  slug: zepto-payments-float-accounts-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: A Payment Request (PR) is used to collect funds, via direct debit, from one of your Contacts (as long as there is an accepted Agreement in place). <div class="middle-header">Applicable scenarios</div>
  name: Zepto Payment Requests API
  slug: zepto-payments-payment-requests-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Make payments using an existing agreement
  name: Zepto Payments API
  slug: zepto-payments-payments-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: 'This endpoint gives you some control over a transaction: * After it has been created; and * Before it has been submitted to the banks. <aside class="notice"> Payments and Payment Requests are made up '
  name: Zepto Payouts API
  slug: zepto-payments-payouts-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: The PayTo Settlement API from Zepto — 1 operation(s) for payto settlement.
  name: Zepto PayTo Settlement API
  slug: zepto-payments-payto-settlement-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Test your connectivity and authentication.
  name: Zepto Ping API
  slug: zepto-payments-ping-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: 'Refunds can be issued for any successfully completed Payment Request transaction. This includes: 1. Payment Requests for direct debit payments **(Collections)**: 2. Payment Requests for funds received'
  name: Zepto Refunds API
  slug: zepto-payments-refunds-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: 'Refund existing settled PayTo Payments ## Beta Release We''re excited to announce that this feature is now in beta! While we''ll aim to minimize breaking changes, some adjustments may occur as we refine'
  name: Zepto Refunds (Beta) API
  slug: zepto-payments-refunds-beta-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: Special testing endpoints that only exist in the sandbox environment.
  name: Zepto Sandbox Only API
  slug: zepto-payments-sandbox-only-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: By default, the transactions endpoint provides a detailed look at all past, current and future debits & credits related to your account. <aside class="notice">Want to also know about the debits & cred
  name: Zepto Transactions API
  slug: zepto-payments-transactions-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: 'This endpoint lets you Transfer funds between any bank & float accounts registered under your Zepto account: 1. **From**: Bank Account **To**: Float Account: * Topping up a float account via Direct De'
  name: Zepto Transfers API
  slug: zepto-payments-transfers-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: All about the currently authenticated user.
  name: Zepto Users API
  slug: zepto-payments-users-api
- baseURL: https://api.zeptopayments.com
  baseurl_source: declared
  description: The Webhooks API from Zepto — 4 operation(s) for webhooks.
  name: Zepto Webhooks API
  slug: zepto-payments-webhooks-api
artifact_total: 44
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
- collection_type: open
  name: Zepto Clients API (Alpha)
  slug: open-zepto-payments-clients
- collection_type: open
  name: Zepto Investigations API
  slug: open-zepto-payments-investigations
- collection_type: open
  name: Zepto Merchant Reports API
  slug: open-zepto-payments-merchant-reports
- collection_type: open
  name: Notifications
  slug: open-zepto-payments-notifications
- collection_type: open
  name: Zepto PayTo API
  slug: open-zepto-payments-pay-to
- collection_type: open
  name: Zepto Validate API (Confirmation of Payee)
  slug: open-zepto-payments-validate-cop
- collection_type: open
  name: Zepto API
  slug: open-zepto-payments-zepto
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zepto-payments-capability-edges.yml
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
  name: Zepto MCP Server
  slug: zepto-mcp-server
modified: '2026-07-24'
name: Zepto
nav: Providers
network: true
overview: 'Zepto publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Agreement modification API, Agreements API, Alias Resolution API, and 19 more. Tagged areas include Payments, Australia, Real-Time Payments, Account-to-Account, and New Payments Platform.


  The Zepto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zepto''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, engineering blog, sandbox, and 34 more developer resources.'
random_paper: 18
scopes:
- name: Zepto Payments Scopes
  scope_count: 9
  slug: zepto-payments-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 64.1
    developer_ergonomics: 61.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zepto-payments/refs/heads/main/screenshots/zepto-payments-2026-08-17T083057.png
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
