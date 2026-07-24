---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    well_known_catalog: false
  schema_version: 0.1
  score: 86.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Methodfi Agentic Access
  operation_count: 128
  slug: methodfi-agentic-access
  summary_line: 128 operations · 55 acting
api_count: 42
apis:
- description: Attribute data for accounts
  name: MethodFi Account Attributes API
  slug: methodfi-account-attributes-api
- description: Balance data for accounts
  name: MethodFi Account Balances API
  slug: methodfi-account-balances-api
- description: Card brand information for accounts
  name: MethodFi Account Card Brands API
  slug: methodfi-account-card-brands-api
- description: Consent management for accounts
  name: MethodFi Account Consent API
  slug: methodfi-account-consent-api
- description: Payment instruments for accounts
  name: MethodFi Account Payment Instruments API
  slug: methodfi-account-payment-instruments-api
- description: Payoff data for accounts
  name: MethodFi Account Payoffs API
  slug: methodfi-account-payoffs-api
- description: Products associated with accounts
  name: MethodFi Account Products API
  slug: methodfi-account-products-api
- description: Sensitive data for accounts
  name: MethodFi Account Sensitive API
  slug: methodfi-account-sensitive-api
- description: Subscriptions for accounts
  name: MethodFi Account Subscriptions API
  slug: methodfi-account-subscriptions-api
- description: Transactions for accounts
  name: MethodFi Account Transactions API
  slug: methodfi-account-transactions-api
- description: Update records for accounts
  name: MethodFi Account Updates API
  slug: methodfi-account-updates-api
- description: Verification sessions for accounts
  name: MethodFi Account Verification Sessions API
  slug: methodfi-account-verification-sessions-api
- description: Financial accounts (ACH, liability, clearing, debit card)
  name: MethodFi Accounts API
  slug: methodfi-accounts-api
- description: Card product definitions
  name: MethodFi Card Products API
  slug: methodfi-card-products-api
- description: Client-side Element endpoints
  name: MethodFi Elements API
  slug: methodfi-elements-api
- description: Individuals, corporations, and receive-only entities
  name: MethodFi Entities API
  slug: methodfi-entities-api
- description: Attribute data for entities
  name: MethodFi Entity Attributes API
  slug: methodfi-entity-attributes-api
- description: Account connection sessions for entities
  name: MethodFi Entity Connects API
  slug: methodfi-entity-connects-api
- description: Consent management for entities
  name: MethodFi Entity Consent API
  slug: methodfi-entity-consent-api
- description: Credit score data for entities
  name: MethodFi Entity Credit Scores API
  slug: methodfi-entity-credit-scores-api
- description: Identity verification data for entities
  name: MethodFi Entity Identities API
  slug: methodfi-entity-identities-api
- description: Products associated with entities
  name: MethodFi Entity Products API
  slug: methodfi-entity-products-api
- description: Subscriptions for entities
  name: MethodFi Entity Subscriptions API
  slug: methodfi-entity-subscriptions-api
- description: Vehicle data for entities
  name: MethodFi Entity Vehicles API
  slug: methodfi-entity-vehicles-api
- description: Verification sessions for entities
  name: MethodFi Entity Verification Sessions API
  slug: methodfi-entity-verification-sessions-api
- description: Webhook event log
  name: MethodFi Events API
  slug: methodfi-events-api
- description: Request forwarding with sensitive data injection
  name: MethodFi Forwarding Requests API
  slug: methodfi-forwarding-requests-api
- description: Method-managed accounts
  name: MethodFi Managed Accounts API
  slug: methodfi-managed-accounts-api
- description: Merchant directory
  name: MethodFi Merchants API
  slug: methodfi-merchants-api
- description: Opal client-side session and token management
  name: MethodFi Opal API
  slug: methodfi-opal-api
- description: Reversals for payments
  name: MethodFi Payment Reversals API
  slug: methodfi-payment-reversals-api
- description: ACH and clearing payments
  name: MethodFi Payments API
  slug: methodfi-payments-api
- description: Health check endpoint
  name: MethodFi Ping API
  slug: methodfi-ping-api
- description: Public key discovery endpoints for Message-Level Encryption.
  name: MethodFi Public Keys API
  slug: methodfi-public-keys-api
- description: Downloadable reports
  name: MethodFi Reports API
  slug: methodfi-reports-api
- description: Secure secret storage
  name: MethodFi Secrets API
  slug: methodfi-secrets-api
- description: Sandbox account simulation
  name: MethodFi Simulate Accounts API
  slug: methodfi-simulate-accounts-api
- description: Sandbox entity simulation
  name: MethodFi Simulate Entities API
  slug: methodfi-simulate-entities-api
- description: Sandbox event simulation
  name: MethodFi Simulate Events API
  slug: methodfi-simulate-events-api
- description: Sandbox payment simulation
  name: MethodFi Simulate Payments API
  slug: methodfi-simulate-payments-api
- description: Team and API key management
  name: MethodFi Teams API
  slug: methodfi-teams-api
- description: Webhook subscriptions
  name: MethodFi Webhooks API
  slug: methodfi-webhooks-api
artifact_total: 48
asyncapis:
- description: ''
  name: Methodfi Webhooks
  slug: methodfi-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/methodfi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/methodfi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/methodfi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/methodfi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/methodfi-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/methodfi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/methodfi-packages.yml
- group: design
  title: ''
  type: Components
  url: components/methodfi-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/methodfi-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/methodfi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://methodfi.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/methodfi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/methodfi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://methodfi.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/methodfi-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/methodfi-decline-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/methodfi-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/methodfi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/methodfi-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/methodfi-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/methodfi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/methodfi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://methodfi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.methodfi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.methodfi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.methodfi.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.methodfi.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://methodfi.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MethodFi
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/methodfi/method-api
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.methodfi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://methodfi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://methodfi.com/privacy
created: '2026-07-17'
description: Method (Method Financial) is the infrastructure layer for consumer liability data and payments. Its API lets developers create entities, verify identity, and use Connect to discover a user's complete liability picture across 15,000+ institutions (credit cards, auto loans, student loans, mortgages, personal loans) without credential sharing, then normalize that data and move money via ACH to pay down those liabilities. Additional products include credit scores, card-brand enrichment, financial attributes, transactions, updates/subscriptions for monitoring, reports, and embeddable UI (Opal/Elements). Method powers lending, personal finance management, and commerce/card-linking use cases.
image: https://framerusercontent.com/assets/ZHgWyxIoZ4u3muxNTrEuOhP9o.jpg
layout: provider
mcp_servers:
- description: ''
  name: methodfi-mcp.yml
  slug: methodfi-mcpyml
modified: '2026-07-20'
name: MethodFi
nav: Providers
network: true
overview: 'MethodFi publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Account Attributes API, Account Balances API, Account Card Brands API, and 39 more. Tagged areas include Company, Fintech, Liability Data, Payments, and Lending.


  The MethodFi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MethodFi''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 27 more developer resources.'
random_paper: 32
rate_limits:
- limit_count: 0
  name: Methodfi Rate Limits
  slug: methodfi-rate-limits
score:
  band: strong
  composite: 61.0
  delta: 0.8
  facets:
    commercial_clarity: 42.1
    contract_quality: 73.8
    developer_ergonomics: 82.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 60.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Methodfi Authentication
  slug: methodfi-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Methodfi Domain Security
  slug: methodfi-domain-security
  summary_line: TLSv1.2 · DMARC
slug: methodfi
tags:
- Company
- Fintech
- Liability Data
- Payments
- Lending
- Personal Finance
- Credit
- ACH
- Debt
- Identity Verification
website: https://methodfi.com
---
