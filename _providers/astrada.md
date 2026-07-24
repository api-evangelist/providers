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
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Astrada Agentic Access
  operation_count: 50
  slug: astrada-agentic-access
  summary_line: 50 operations · 21 acting
api_count: 15
apis:
- description: Manage connected bank accounts. Bank accounts are created automatically when a bank link enrollment is completed.
  name: Astrada bank-accounts API
  slug: astrada-bank-accounts-api
- description: Manage bank enrollment links. A bank link represents an invitation for a user to connect their bank account via Plaid.
  name: Astrada bank-links API
  slug: astrada-bank-links-api
- description: Manage bank subscriptions (Plaid connections). A subscription represents an active connection to a financial institution.
  name: Astrada bank-subscriptions API
  slug: astrada-bank-subscriptions-api
- description: Access bank transactions synced from connected accounts. Transactions are ingested via Plaid and can be matched against card transactions.
  name: Astrada bank-transactions API
  slug: astrada-bank-transactions-api
- description: BIN Lookup
  name: Astrada bin-lookup API
  slug: astrada-bin-lookup-api
- description: Card resource
  name: Astrada card API
  slug: astrada-card-api
- description: Card Subscription resource
  name: Astrada card-subscription API
  slug: astrada-card-subscription-api
- description: Card Verification
  name: Astrada card-verification API
  slug: astrada-card-verification-api
- description: Enrollment methods resource
  name: Astrada enrollment-methods API
  slug: astrada-enrollment-methods-api
- description: Network bulk feed resource
  name: Astrada network-bulk-feeds API
  slug: astrada-network-bulk-feeds-api
- description: Subaccount resource
  name: Astrada subaccounts API
  slug: astrada-subaccounts-api
- description: Access transaction matches between bank and card transactions, including confidence scores and match reasoning.
  name: Astrada transaction-matches API
  slug: astrada-transaction-matches-api
- description: Transaction messages resource
  name: Astrada transaction-messages API
  slug: astrada-transaction-messages-api
- description: Transaction resource
  name: Astrada transactions API
  slug: astrada-transactions-api
- description: Manage webhooks
  name: Astrada webhooks API
  slug: astrada-webhooks-api
artifact_total: 24
asyncapis:
- description: Webhook event surface for the Astrada API, generated from the documented Event Types and webhook delivery mechanics. Astrada delivers events via HTTP POST to registered HTTPS endpoints with at-least-o
  name: Astrada Webhook Events
  slug: astrada-events-asyncapi
- description: ''
  name: Astrada Webhooks
  slug: astrada-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://astrada.co/
- group: start
  title: ''
  type: Portal
  url: https://docs.astrada.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.astrada.co/docs/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.astrada.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.astrada.co/docs/getting-started-1
- group: company
  title: ''
  type: Blog
  url: https://astrada.co/blog
- group: operate
  title: ''
  type: Support
  url: https://astrada.co/company/contact
- group: start
  title: ''
  type: SignUp
  url: https://astrada.co/company/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.astrada.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astrada.co/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astrada.co/legal
- group: auth
  title: ''
  type: Security
  url: https://astrada.co/security
- group: auth
  title: ''
  type: Compliance
  url: https://astrada.co/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/astrada-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/astrada-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/astrada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/astrada-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/astrada-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/astrada-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/astrada-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/astrada-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/astrada-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/astrada-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/astrada-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/astrada-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/astrada-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/astrada-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astrada-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/astrada-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astrada-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/astrada-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/astrada-trust-center.yml
created: '2026-07-17'
description: Astrada is the data layer for autonomous finance, providing real-time, structured card transaction data pulled directly from the card networks rather than relying on delayed bank feeds. Its Transaction Data API lets expense management, travel, and accounting/ERP platforms enroll corporate cards (with 3DS cardholder verification), receive real-time transaction messages and enriched transactions, link bank accounts, and auto-reconcile card-to-bank activity. Founded in 2024 by Salman Syed (ex-Mastercard, Marqeta, Fidel API), Astrada is PCI DSS v4 Level 1 certified, a Mastercard Start Path and Visa Ventures portfolio company, and is backed by QED Investors.
image: https://files.readme.io/45785f4-brandmark-blue.svg
layout: provider
mcp_servers:
- description: ''
  name: astrada-mcp.yml
  slug: astrada-mcpyml
modified: '2026-07-18'
name: Astrada
nav: Providers
network: true
overview: 'Astrada publishes 15 APIs on the [APIs.io](https://apis.io/) network, including bank-accounts API, bank-links API, bank-subscriptions API, and 12 more. Tagged areas include Company, Fintech, Payments, Card Data, and Transaction Data.


  The Astrada catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Astrada''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 26 more developer resources.'
random_paper: 22
scopes:
- name: Astrada Scopes
  scope_count: 34
  slug: astrada-scopes
  summary_line: 34 scopes · implicit
score:
  band: strong
  composite: 64.8
  delta: 6.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.0
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 58.5
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 100.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Astrada Authentication
  slug: astrada-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Astrada Domain Security
  slug: astrada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Astrada Vulnerability Disclosure
  slug: astrada-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Astrada Trust Center
  slug: astrada-trust-center
  summary_line: PCI DSS v4 Level 1 Service Provider, GDPR, CCPA
slug: astrada
tags:
- Company
- Fintech
- Payments
- Card Data
- Transaction Data
- Reconciliation
- Expense Management
- Data Infrastructure
website: https://astrada.co/
---
