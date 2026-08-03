---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-03'
api_count: 17
apis:
- description: End-customer onboarding — create and manage individual and business Applications, application forms, KYC/KYB document upload, verification, and beneficial owners.
  name: Unit Applications API
  slug: applications
- description: Manage created Customers (individual and business), authorized and API users, customer archival, and customer-scoped bearer tokens for end-user access.
  name: Unit Customers API
  slug: customers
- description: Deposit, credit, wallet (FBO) and DACA accounts — open, close, freeze and unfreeze, per-account limits, deposit products, customer relationships, and repayment information.
  name: Unit Accounts API
  slug: accounts
- description: Issue and manage debit and credit cards — create, close, freeze/unfreeze, replace, report lost or stolen, set per-card limits, and check secure PIN status, with mobile wallet integration.
  name: Unit Cards API
  slug: cards
- description: Move money via Book, ACH and wire Payments plus recurring, received (incoming ACH), and cash deposit flows, with counterparties, ACH returns, and institution routing-number lookups.
  name: Unit Payments API
  slug: payments
- description: Check payments (print-and-mail) and mobile check deposits — create, approve, cancel, return, confirm, and manage front and back check images.
  name: Unit Checks API
  slug: checks
- description: Real-time card authorization requests for programmatic approve/decline control, plus retrieval and listing of completed card authorizations.
  name: Unit Card Authorizations API
  slug: authorizations
- description: Retrieve and list card transaction disputes and track their status through the dispute lifecycle.
  name: Unit Disputes API
  slug: disputes
- description: List and retrieve account transactions across all payment, card, fee, and reward activity for reconciliation and ledgering.
  name: Unit Transactions API
  slug: transactions
- description: Retrieve monthly account statements as HTML or PDF, including bank-branded PDF statements for end customers.
  name: Unit Statements API
  slug: statements
- description: List and retrieve customer tax forms and download their PDF renderings for year-end reporting.
  name: Unit Tax Forms API
  slug: tax-forms
- description: Charge and reverse Fees on accounts and create or retrieve Rewards paid out to customer accounts.
  name: Unit Fees and Rewards API
  slug: fees-rewards
- description: Credit account repayments and recurring repayments — create, retrieve, and enable or disable scheduled repayments for lending programs.
  name: Unit Credit and Repayments API
  slug: credit
- description: Create, retrieve, and disable stop payments and positive-pay controls to block or match expected payments on accounts.
  name: Unit Stop Payments API
  slug: stop-payments
- description: Register webhook endpoints, enable or disable delivery, and list and retrieve the Events (resource state changes) Unit emits across the platform.
  name: Unit Webhooks and Events API
  slug: webhooks
- description: Sandbox-only simulation endpoints (received ACH payments, ATM deposits, card activation) plus store and ATM location reference data for testing integrations.
  name: Unit Sandbox and Reference API
  slug: sandbox
- description: Unit OpenAPI specifications from Unit — 117 path(s) described in OpenAPI.
  name: Unit OpenAPI specifications
  slug: unit-openapi-source
artifact_total: 43
asyncapis:
- description: ''
  name: Unit Events Webhooks
  slug: unit-events-webhooks
collections:
- collection_type: postman
  name: Unit Accounts API
  slug: postman-unit-accounts-openapi
- collection_type: postman
  name: Unit Applications API
  slug: postman-unit-applications-openapi
- collection_type: postman
  name: Unit Card Authorizations API
  slug: postman-unit-authorizations-openapi
- collection_type: postman
  name: Unit Cards API
  slug: postman-unit-cards-openapi
- collection_type: postman
  name: Unit Checks API
  slug: postman-unit-checks-openapi
- collection_type: postman
  name: Unit Credit and Repayments API
  slug: postman-unit-credit-openapi
- collection_type: postman
  name: Unit Customers API
  slug: postman-unit-customers-openapi
- collection_type: postman
  name: Unit Disputes API
  slug: postman-unit-disputes-openapi
- collection_type: postman
  name: Unit Fees and Rewards API
  slug: postman-unit-fees-rewards-openapi
- collection_type: postman
  name: Unit Payments API
  slug: postman-unit-payments-openapi
- collection_type: postman
  name: Unit Sandbox and Reference API
  slug: postman-unit-sandbox-openapi
- collection_type: postman
  name: Unit Statements API
  slug: postman-unit-statements-openapi
- collection_type: postman
  name: Unit Stop Payments API
  slug: postman-unit-stop-payments-openapi
- collection_type: postman
  name: Unit Tax Forms API
  slug: postman-unit-tax-forms-openapi
- collection_type: postman
  name: Unit Transactions API
  slug: postman-unit-transactions-openapi
- collection_type: postman
  name: Unit Webhooks and Events API
  slug: postman-unit-webhooks-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/unit/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/unit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unit.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.unit.co/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.unit.co/docs/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unit-finance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unit-finance
- group: company
  title: ''
  type: Blog
  url: https://www.unit.co/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unit.co/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unit.co/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unit.co/
- group: auth
  title: ''
  type: Security
  url: https://www.unit.co/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/unit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unit-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unit-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.unit.co/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.unit.co/docs/api/getting-started/tooling
- group: start
  title: ''
  type: SignUp
  url: https://app.unit.co/
- group: build
  title: ''
  type: Postman
  url: https://unit.co/docs/UnitAPI.postman_collection.json
- group: auth
  title: ''
  type: Compliance
  url: https://www.unit.co/security
- group: operate
  title: ''
  type: Deprecation
  url: https://www.unit.co/docs/api/using-the-api#deprecations
- group: auth
  title: ''
  type: Authentication
  url: authentication/unit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unit-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/unit-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/unit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unit-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unit-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unit-ach-return-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unit-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unit-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unit-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unit-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/unit-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unit-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unit-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/unit-openapi-source-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unit-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-08'
description: Unit is a US Banking-as-a-Service (BaaS) platform that lets companies embed banking, cards, and payments into their own products. Its REST API — organized around Applications, Customers, Accounts (deposit, credit, wallet/FBO, DACA), Cards, Payments (book, ACH, wire, recurring, received, cash deposit), Checks, Card Authorizations, Disputes, Transactions, Statements, Tax Forms, Fees & Rewards, Credit repayments, Stop Payments, and Webhooks — is authenticated with organization and customer bearer tokens and secured with idempotency keys and resource tagging. Unit publishes a public OpenAPI 3.0.2 specification (openapi-unit-sdk) and generates official Node, Python, Ruby, and Java SDKs from it.
finops:
- name: Unit Finops
  service_category: FinTech
  slug: unit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unit.png
layout: provider
mcp_servers:
- description: ''
  name: unit-mcp.yml
  slug: unit-mcpyml
modified: '2026-07-23'
name: Unit
nav: Providers
network: true
overview: 'Unit publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Customers API, Accounts API, and 14 more. Tagged areas include FinTech, BaaS, Banking, Payments, and Card Issuing.


  The Unit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unit''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, signup flow, sandbox, and 36 more developer resources.'
plans:
- name: Unit Plans Pricing
  plan_count: 2
  slug: unit-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 1
  name: Unit Rate Limits
  slug: unit-rate-limits
scopes:
- name: Unit Scopes
  scope_count: 46
  slug: unit-scopes
  summary_line: 46 scopes
score:
  band: strong
  composite: 63.6
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 47.3
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 84.2
  previous_composite: 63.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unit/refs/heads/main/screenshots/unit-2026-06-20T200056.png
security:
- kind: authentication
  name: Unit Authentication
  slug: unit-authentication
  summary_line: http/oauth2-bearer · 1 scheme
- kind: domain-security
  name: Unit Domain Security
  slug: unit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unit Vulnerability Disclosure
  slug: unit-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unit Trust Center
  slug: unit-trust-center
  summary_line: SOC 2, PCI DSS
slug: unit
tags:
- FinTech
- BaaS
- Banking
- Payments
- Card Issuing
- ACH
- United States
- Embedded Finance
- Deposit Accounts
- Open Finance
website: https://www.unit.co/
---
