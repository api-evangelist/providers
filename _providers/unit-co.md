---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 73
  human_in_the_loop: 8
  name: Unit Co Agentic Access
  operation_count: 138
  slug: unit-co-agentic-access
  summary_line: 138 operations · 73 acting · 8 human-in-the-loop
api_count: 18
apis:
- description: Deposit and credit accounts.
  name: Unit Accounts API
  slug: unit-co-accounts-api
- description: Org-level and customer-level authentication tokens.
  name: Unit API Tokens API
  slug: unit-co-api-tokens-api
- description: Individual and business application onboarding (KYC/KYB).
  name: Unit Applications API
  slug: unit-co-applications-api
- description: Completed card authorizations and real-time authorization requests.
  name: Unit Authorizations API
  slug: unit-co-authorizations-api
- description: Debit and credit card issuance and management.
  name: Unit Cards API
  slug: unit-co-cards-api
- description: Check deposits and outbound check payments.
  name: Unit Checks API
  slug: unit-co-checks-api
- description: External bank accounts and routing-number institution lookups.
  name: Unit Counterparties API
  slug: unit-co-counterparties-api
- description: Repayments on credit accounts and receivables.
  name: Unit Credit and Repayments API
  slug: unit-co-credit-and-repayments-api
- description: Customer profiles created from approved applications.
  name: Unit Customers API
  slug: unit-co-customers-api
- description: Platform activity log.
  name: Unit Events API
  slug: unit-co-events-api
- description: Ad hoc fees and cashback-style rewards.
  name: Unit Fees and Rewards API
  slug: unit-co-fees-and-rewards-api
- description: Book, ACH, wire, recurring, and cash-deposit payments.
  name: Unit Payments API
  slug: unit-co-payments-api
- description: Stop payments and card/ACH disputes.
  name: Unit Risk and Fraud API
  slug: unit-co-risk-and-fraud-api
- description: Monthly account statements.
  name: Unit Statements API
  slug: unit-co-statements-api
- description: Annual tax documents.
  name: Unit Tax Forms API
  slug: unit-co-tax-forms-api
- description: Posted, immutable ledger entries.
  name: Unit Transactions API
  slug: unit-co-transactions-api
- description: Subscriptions that deliver events as signed HTTP callbacks.
  name: Unit Webhooks API
  slug: unit-co-webhooks-api
artifact_total: 80
asyncapis:
- description: ''
  name: Unit Co Events Webhooks
  slug: unit-co-events-webhooks
collections:
- collection_type: postman
  name: Unit Accounts API
  slug: postman-unit-co-accounts-openapi
- collection_type: postman
  name: Unit Applications API
  slug: postman-unit-co-applications-openapi
- collection_type: postman
  name: Unit Card Authorizations API
  slug: postman-unit-co-authorizations-openapi
- collection_type: postman
  name: Unit Cards API
  slug: postman-unit-co-cards-openapi
- collection_type: postman
  name: Unit Checks API
  slug: postman-unit-co-checks-openapi
- collection_type: postman
  name: Unit Credit and Repayments API
  slug: postman-unit-co-credit-openapi
- collection_type: postman
  name: Unit Customers API
  slug: postman-unit-co-customers-openapi
- collection_type: postman
  name: Unit Disputes API
  slug: postman-unit-co-disputes-openapi
- collection_type: postman
  name: Unit Fees and Rewards API
  slug: postman-unit-co-fees-rewards-openapi
- collection_type: postman
  name: Unit Payments API
  slug: postman-unit-co-payments-openapi
- collection_type: postman
  name: Unit Sandbox and Reference API
  slug: postman-unit-co-sandbox-openapi
- collection_type: postman
  name: Unit Statements API
  slug: postman-unit-co-statements-openapi
- collection_type: postman
  name: Unit Stop Payments API
  slug: postman-unit-co-stop-payments-openapi
- collection_type: postman
  name: Unit Tax Forms API
  slug: postman-unit-co-tax-forms-openapi
- collection_type: postman
  name: Unit Transactions API
  slug: postman-unit-co-transactions-openapi
- collection_type: postman
  name: Unit Webhooks and Events API
  slug: postman-unit-co-webhooks-openapi
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unit Accounts API
  slug: open-unit-co-accounts-api
- collection_type: open
  name: Unit Accounts API
  slug: open-unit-co-accounts
- collection_type: open
  name: Unit Accounts API Tokens API
  slug: open-unit-co-api-tokens-api
- collection_type: open
  name: Unit Accounts Applications API
  slug: open-unit-co-applications-api
- collection_type: open
  name: Unit Applications API
  slug: open-unit-co-applications
- collection_type: open
  name: Unit Accounts Authorizations API
  slug: open-unit-co-authorizations-api
- collection_type: open
  name: Unit Card Authorizations API
  slug: open-unit-co-authorizations
- collection_type: open
  name: Unit Accounts Cards API
  slug: open-unit-co-cards-api
- collection_type: open
  name: Unit Cards API
  slug: open-unit-co-cards
- collection_type: open
  name: Unit Accounts Checks API
  slug: open-unit-co-checks-api
- collection_type: open
  name: Unit Checks API
  slug: open-unit-co-checks
- collection_type: open
  name: Unit Accounts Counterparties API
  slug: open-unit-co-counterparties-api
- collection_type: open
  name: Unit Accounts Credit and Repayments API
  slug: open-unit-co-credit-and-repayments-api
- collection_type: open
  name: Unit Credit and Repayments API
  slug: open-unit-co-credit
- collection_type: open
  name: Unit Accounts Customers API
  slug: open-unit-co-customers-api
- collection_type: open
  name: Unit Customers API
  slug: open-unit-co-customers
- collection_type: open
  name: Unit Disputes API
  slug: open-unit-co-disputes
- collection_type: open
  name: Unit Accounts Events API
  slug: open-unit-co-events-api
- collection_type: open
  name: Unit Accounts Fees and Rewards API
  slug: open-unit-co-fees-and-rewards-api
- collection_type: open
  name: Unit Fees and Rewards API
  slug: open-unit-co-fees-rewards
- collection_type: open
  name: Unit OpenAPI specifications
  slug: open-unit-co-openapi-source
- collection_type: open
  name: Unit Accounts Payments API
  slug: open-unit-co-payments-api
- collection_type: open
  name: Unit Payments API
  slug: open-unit-co-payments
- collection_type: open
  name: Unit Accounts Risk and Fraud API
  slug: open-unit-co-risk-and-fraud-api
- collection_type: open
  name: Unit Sandbox and Reference API
  slug: open-unit-co-sandbox
- collection_type: open
  name: Unit Accounts Statements API
  slug: open-unit-co-statements-api
- collection_type: open
  name: Unit Statements API
  slug: open-unit-co-statements
- collection_type: open
  name: Unit Stop Payments API
  slug: open-unit-co-stop-payments
- collection_type: open
  name: Unit Accounts Tax Forms API
  slug: open-unit-co-tax-forms-api
- collection_type: open
  name: Unit Tax Forms API
  slug: open-unit-co-tax-forms
- collection_type: open
  name: Unit Accounts Transactions API
  slug: open-unit-co-transactions-api
- collection_type: open
  name: Unit Transactions API
  slug: open-unit-co-transactions
- collection_type: open
  name: Unit Accounts Webhooks API
  slug: open-unit-co-webhooks-api
- collection_type: open
  name: Unit Webhooks and Events API
  slug: open-unit-co-webhooks
- collection_type: open
  name: Unit API
  slug: open-unit-co
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/unit-co-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unit-co-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/unit-co-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unit-co-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unit-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unit-co-authentication.yml
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
  type: Website
  url: https://www.unit.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.unit.co/docs/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/unit-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unit-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unit-co-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.unit.co/blog/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/unit/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.unit.co/docs
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
  type: OAuthScopes
  url: scopes/unit-co-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unit-co-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/unit-co-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/unit-co-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unit-co-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unit-co-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unit-co-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unit-co-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unit-co-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unit-co-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/unit-co-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unit-co-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unit-co-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unit-co-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/unit-co-openapi-source-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unit-co-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-02'
description: Unit is a Banking-as-a-Service (BaaS) platform that lets companies embed deposit accounts, cards, payments, and lending into their own products without becoming a bank. A single REST API, built on the JSON:API specification (media type application/vnd.api+json) and secured with Bearer/JWT tokens, covers onboarding (Applications), Customers, Deposit and Credit Accounts, Debit and Credit Cards, real-time card Authorizations, Payments (Book, ACH, Wire, Recurring, Cash Deposits), Counterparties, Checks, Transactions, Statements, Tax Forms, Fees, Rewards, Credit and Repayments, and Events delivered as signed HTTP webhooks. Unit publishes an official OpenAPI 3.0.2 specification (github.com/unit-finance/openapi-unit-sdk) plus generated Node.js, Python, Ruby, and Java SDKs. Sandbox runs at api.s.unit.sh; production access is provisioned per signed BaaS agreement with Unit's partner banks.
finops:
- name: Unit Co Finops
  service_category: Banking as a Service
  slug: unit-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unit-co.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived one-to-one from the Unit OpenAPI operations. Unit does not publish a hosted/remote MCP server; this is a proposed mapping so the operations can be exposed as agent t
  name: Unit MCP Server
  slug: unit-mcp-server
modified: '2026-08-08'
name: Unit
nav: Providers
network: true
overview: 'Unit publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Tokens API, Applications API, and 14 more. Tagged areas include Fintech, BaaS, Banking, Payments, and Card Issuing.


  The Unit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unit''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, signup flow, sandbox, and 36 more developer resources.'
plans:
- name: Unit Co Plans Pricing
  plan_count: 2
  slug: unit-co-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Unit Co Rate Limits
  slug: unit-co-rate-limits
scopes:
- name: Unit Co Scopes
  scope_count: 46
  slug: unit-co-scopes
  summary_line: 46 scopes
score:
  band: exemplar
  composite: 71.8
  coverage:
    artifact_dirs: 27
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 58.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 71.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 84.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unit-co/refs/heads/main/screenshots/unit-co-2026-06-20T200056.png
security:
- kind: authentication
  name: Unit Co Authentication
  slug: unit-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unit Co Domain Security
  slug: unit-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unit Co Vulnerability Disclosure
  slug: unit-co-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unit Co Trust Center
  slug: unit-co-trust-center
  summary_line: SOC 2, PCI DSS
slug: unit-co
tags:
- Fintech
- BaaS
- Banking
- Payments
- Card Issuing
- ACH
- Lending
- JSON:API
website: https://www.unit.co/
---
