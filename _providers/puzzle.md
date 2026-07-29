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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Puzzle Agentic Access
  operation_count: 81
  slug: puzzle-agentic-access
  summary_line: 81 operations · 38 acting
api_count: 22
apis:
- description: The Accounts API from Puzzle — 3 operation(s) for accounts.
  name: Puzzle Accounts API
  slug: puzzle-accounts-api
- description: The Attachments API from Puzzle — 1 operation(s) for attachments.
  name: Puzzle Attachments API
  slug: puzzle-attachments-api
- description: The Bills API from Puzzle — 3 operation(s) for bills.
  name: Puzzle Bills API
  slug: puzzle-bills-api
- description: The Company API from Puzzle — 10 operation(s) for company.
  name: Puzzle Company API
  slug: puzzle-company-api
- description: The Customers API from Puzzle — 2 operation(s) for customers.
  name: Puzzle Customers API
  slug: puzzle-customers-api
- description: The Departments API from Puzzle — 1 operation(s) for departments.
  name: Puzzle Departments API
  slug: puzzle-departments-api
- description: The Documents API from Puzzle — 1 operation(s) for documents.
  name: Puzzle Documents API
  slug: puzzle-documents-api
- description: The Invoices API from Puzzle — 2 operation(s) for invoices.
  name: Puzzle Invoices API
  slug: puzzle-invoices-api
- description: The JournalEntries API from Puzzle — 2 operation(s) for journalentries.
  name: Puzzle JournalEntries API
  slug: puzzle-journalentries-api
- description: The JournalEntry API from Puzzle — 2 operation(s) for journalentry.
  name: Puzzle JournalEntry API
  slug: puzzle-journalentry-api
- description: The Locations API from Puzzle — 1 operation(s) for locations.
  name: Puzzle Locations API
  slug: puzzle-locations-api
- description: The Metrics API from Puzzle — 5 operation(s) for metrics.
  name: Puzzle Metrics API
  slug: puzzle-metrics-api
- description: The OAuth API from Puzzle — 2 operation(s) for oauth.
  name: Puzzle OAuth API
  slug: puzzle-oauth-api
- description: The Onboarding API from Puzzle — 1 operation(s) for onboarding.
  name: Puzzle Onboarding API
  slug: puzzle-onboarding-api
- description: The Payroll API from Puzzle — 6 operation(s) for payroll.
  name: Puzzle Payroll API
  slug: puzzle-payroll-api
- description: The Products API from Puzzle — 2 operation(s) for products.
  name: Puzzle Products API
  slug: puzzle-products-api
- description: The Reports API from Puzzle — 7 operation(s) for reports.
  name: Puzzle Reports API
  slug: puzzle-reports-api
- description: The Requests API from Puzzle — 1 operation(s) for requests.
  name: Puzzle Requests API
  slug: puzzle-requests-api
- description: The Tasks API from Puzzle — 2 operation(s) for tasks.
  name: Puzzle Tasks API
  slug: puzzle-tasks-api
- description: The Transactions API from Puzzle — 3 operation(s) for transactions.
  name: Puzzle Transactions API
  slug: puzzle-transactions-api
- description: The User API from Puzzle — 3 operation(s) for user.
  name: Puzzle User API
  slug: puzzle-user-api
- description: The Vendors API from Puzzle — 2 operation(s) for vendors.
  name: Puzzle Vendors API
  slug: puzzle-vendors-api
artifact_total: 29
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://puzzle-api.readme.io/docs/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://puzzle-api.readme.io/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://puzzle-api.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://puzzle-api.readme.io/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://puzzle.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://puzzle.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.puzzle.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://puzzle.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://puzzle.io/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.puzzle.io/
- group: company
  title: ''
  type: Website
  url: https://puzzle.io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/puzzle-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/puzzle-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/puzzle-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/puzzle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/puzzle-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/puzzle-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/puzzle-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/puzzle-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/puzzle-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/puzzle-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/puzzle-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/puzzle-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://puzzle.io/security
- group: agent
  title: ''
  type: WellKnown
  url: well-known/puzzle-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/puzzle-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/puzzle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/puzzle-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.puzzle.io
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puzzle-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/puzzle-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/puzzle-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/puzzle-components.yml
created: '2026-07-17'
description: 'Puzzle is an AI-powered accounting platform for startups, SMBs, and accounting firms, built around a real-time, append-only general ledger. Its agent-native architecture pairs deterministic Puzzle agents that draft categorization, reconciliation, and month-end close for human review with native integrations to banking, card, revenue, and payroll systems (Stripe, Brex, Mercury, Ramp, Gusto, Rippling, and more). The Puzzle Accounting API gives developers programmatic, OAuth 2.0 + PKCE-secured access to the same ledger: transactions, chart of accounts, journal entries, bills, invoices, vendors, customers, payroll, financial statements (income statement, balance sheet, cash activity), and metrics such as burn, runway, and revenue. A companion read-only MCP server connects AI tools like Claude, Cursor, and Windsurf to the ledger for natural-language financial analysis.'
image: https://puzzle.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: puzzle-mcp.yml
  slug: puzzle-mcpyml
modified: '2026-07-20'
name: Puzzle
nav: Providers
network: true
overview: 'Puzzle publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Bills API, and 19 more. Tagged areas include Company, Accounting, Financial, Bookkeeping, and Fintech.


  Puzzle''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 27 more developer resources.'
random_paper: 42
scopes:
- name: Puzzle Scopes
  scope_count: 21
  slug: puzzle-scopes
  summary_line: 21 scopes
score:
  band: developing
  composite: 50.6
  delta: 0.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 46.5
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 18.4
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Puzzle Authentication
  slug: puzzle-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Puzzle Domain Security
  slug: puzzle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Puzzle Vulnerability Disclosure
  slug: puzzle-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Puzzle Trust Center
  slug: puzzle-trust-center
  summary_line: SOC 2
slug: puzzle
tags:
- Company
- Accounting
- Financial
- Bookkeeping
- Fintech
- General Ledger
- Payroll
- Agent-Native
- MCP
website: https://puzzle.io
---
