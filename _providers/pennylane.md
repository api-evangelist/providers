---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Pennylane Agentic Access
  operation_count: 46
  slug: pennylane-agentic-access
  summary_line: 46 operations · 27 acting
api_count: 19
apis:
- description: The Account API from Pennylane — 1 operation(s) for account.
  name: Pennylane Account API
  slug: pennylane-account-api
- description: The Accounting Exports API from Pennylane — 2 operation(s) for accounting exports.
  name: Pennylane Accounting Exports API
  slug: pennylane-accounting-exports-api
- description: The Bank Accounts API from Pennylane — 2 operation(s) for bank accounts.
  name: Pennylane Bank Accounts API
  slug: pennylane-bank-accounts-api
- description: The Billing Subscriptions API from Pennylane — 1 operation(s) for billing subscriptions.
  name: Pennylane Billing Subscriptions API
  slug: pennylane-billing-subscriptions-api
- description: The Categories API from Pennylane — 2 operation(s) for categories.
  name: Pennylane Categories API
  slug: pennylane-categories-api
- description: The Change Events API from Pennylane — 2 operation(s) for change events.
  name: Pennylane Change Events API
  slug: pennylane-change-events-api
- description: The Customer Invoices API from Pennylane — 7 operation(s) for customer invoices.
  name: Pennylane Customer Invoices API
  slug: pennylane-customer-invoices-api
- description: The Customers API from Pennylane — 4 operation(s) for customers.
  name: Pennylane Customers API
  slug: pennylane-customers-api
- description: The E-Invoicing API from Pennylane — 1 operation(s) for e-invoicing.
  name: Pennylane E-Invoicing API
  slug: pennylane-e-invoicing-api
- description: The File Attachments API from Pennylane — 1 operation(s) for file attachments.
  name: Pennylane File Attachments API
  slug: pennylane-file-attachments-api
- description: The Journals API from Pennylane — 2 operation(s) for journals.
  name: Pennylane Journals API
  slug: pennylane-journals-api
- description: The Ledger Accounts API from Pennylane — 2 operation(s) for ledger accounts.
  name: Pennylane Ledger Accounts API
  slug: pennylane-ledger-accounts-api
- description: The Ledger Entries API from Pennylane — 4 operation(s) for ledger entries.
  name: Pennylane Ledger Entries API
  slug: pennylane-ledger-entries-api
- description: The Mandates API from Pennylane — 2 operation(s) for mandates.
  name: Pennylane Mandates API
  slug: pennylane-mandates-api
- description: The Products API from Pennylane — 2 operation(s) for products.
  name: Pennylane Products API
  slug: pennylane-products-api
- description: The Quotes API from Pennylane — 2 operation(s) for quotes.
  name: Pennylane Quotes API
  slug: pennylane-quotes-api
- description: The Supplier Invoices API from Pennylane — 4 operation(s) for supplier invoices.
  name: Pennylane Supplier Invoices API
  slug: pennylane-supplier-invoices-api
- description: The Suppliers API from Pennylane — 2 operation(s) for suppliers.
  name: Pennylane Suppliers API
  slug: pennylane-suppliers-api
- description: The Transactions API from Pennylane — 2 operation(s) for transactions.
  name: Pennylane Transactions API
  slug: pennylane-transactions-api
artifact_total: 48
collections:
- collection_type: postman
  name: Pennylane Company Account API
  slug: postman-pennylane-account-api
- collection_type: postman
  name: Pennylane Company Account Accounting Exports API
  slug: postman-pennylane-accounting-exports-api
- collection_type: postman
  name: Pennylane Company Account Bank Accounts API
  slug: postman-pennylane-bank-accounts-api
- collection_type: postman
  name: Pennylane Company Account Billing Subscriptions API
  slug: postman-pennylane-billing-subscriptions-api
- collection_type: postman
  name: Pennylane Company Account Categories API
  slug: postman-pennylane-categories-api
- collection_type: postman
  name: Pennylane Company Account Change Events API
  slug: postman-pennylane-change-events-api
- collection_type: postman
  name: Pennylane Company Account Customer Invoices API
  slug: postman-pennylane-customer-invoices-api
- collection_type: postman
  name: Pennylane Company Account Customers API
  slug: postman-pennylane-customers-api
- collection_type: postman
  name: Pennylane Company Account E-Invoicing API
  slug: postman-pennylane-e-invoicing-api
- collection_type: postman
  name: Pennylane Company Account File Attachments API
  slug: postman-pennylane-file-attachments-api
- collection_type: postman
  name: Pennylane Company Account Journals API
  slug: postman-pennylane-journals-api
- collection_type: postman
  name: Pennylane Company Account Ledger Accounts API
  slug: postman-pennylane-ledger-accounts-api
- collection_type: postman
  name: Pennylane Company Account Ledger Entries API
  slug: postman-pennylane-ledger-entries-api
- collection_type: postman
  name: Pennylane Company Account Mandates API
  slug: postman-pennylane-mandates-api
- collection_type: postman
  name: Pennylane Company Account Products API
  slug: postman-pennylane-products-api
- collection_type: postman
  name: Pennylane Company Account Quotes API
  slug: postman-pennylane-quotes-api
- collection_type: postman
  name: Pennylane Company Account Supplier Invoices API
  slug: postman-pennylane-supplier-invoices-api
- collection_type: postman
  name: Pennylane Company Account Suppliers API
  slug: postman-pennylane-suppliers-api
- collection_type: postman
  name: Pennylane Company Account Transactions API
  slug: postman-pennylane-transactions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pennylane/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pennylane-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pennylane-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pennylane.com/fr/securite
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pennylane-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://app.pennylane.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pennylane-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pennylane-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pennylane-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/pennylane-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pennylane-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pennylane-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pennylane-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pennylane-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/pennylane-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/pennylane-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pennylane-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pennylane-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pennylane.com
- group: operate
  title: ''
  type: Deprecation
  url: https://pennylane.readme.io/docs/migrate-from-api-v1-to-v2
- group: design
  title: ''
  type: Conventions
  url: conventions/pennylane-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pennylane-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pennylane-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pennylane-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pennylane
- group: company
  title: ''
  type: Website
  url: https://www.pennylane.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pennylane.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://pennylane.readme.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://pennylane.readme.io/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pennylane-hq
- group: operate
  title: ''
  type: Support
  url: https://help.pennylane.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pennylane.readme.io/docs/api-contract-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pennylane.com/fr/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://start.pennylane.com
- group: commercial
  title: ''
  type: Plans
  url: plans/pennylane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pennylane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pennylane-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pennylane.readme.io/changelog
created: '2026-07-17'
description: Pennylane is a French financial and accounting operating system for SMEs and accounting firms. The Company API (v2) lets companies, firms, and integration partners access and sync invoicing, accounting, banking, and financial data over a REST interface, and automate end-to-end workflows. V2 is the stable version; V1 is deprecated. All amounts are in EUR and the platform is built around French accounting (FEC exports, Plateforme Agréée e-invoicing, SEPA/GoCardless mandates).
finops:
- name: Pennylane Finops
  service_category: Finance and Accounting Software
  slug: pennylane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pennylane.png
layout: provider
mcp_servers:
- description: ''
  name: pennylane-mcp.yml
  slug: pennylane-mcpyml
modified: '2026-07-17'
name: Pennylane
nav: Providers
network: true
overview: 'Pennylane publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounting Exports API, Bank Accounts API, and 16 more. Tagged areas include Accounting, Invoicing, Fintech, Financial Data, and Banking.


  Pennylane''s developer surface includes authentication, changelog, sandbox, documentation, getting-started guide, support, signup flow, and 32 more developer resources.'
plans:
- name: Pennylane Plans Pricing
  plan_count: 3
  slug: pennylane-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Pennylane Rate Limits
  slug: pennylane-rate-limits
scopes:
- name: Pennylane Scopes
  scope_count: 23
  slug: pennylane-scopes
  summary_line: 23 scopes
score:
  band: exemplar
  composite: 66.8
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 57.4
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 76.3
  previous_composite: 66.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
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
security:
- kind: authentication
  name: Pennylane Authentication
  slug: pennylane-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Pennylane Domain Security
  slug: pennylane-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Pennylane Vulnerability Disclosure
  slug: pennylane-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pennylane Trust Center
  slug: pennylane-trust-center
  summary_line: ISO 27001, SOC 2, GDPR
slug: pennylane
tags:
- Accounting
- Invoicing
- Fintech
- Financial Data
- Banking
- France
- SME
website: https://www.pennylane.com/
---
