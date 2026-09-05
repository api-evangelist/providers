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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Puzzle Agentic Access
  operation_count: 81
  slug: puzzle-agentic-access
  summary_line: 81 operations · 38 acting
api_count: 2
apis:
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Accounts API from Puzzle — 3 operation(s) for accounts.
  name: Puzzle Accounts API
  slug: puzzle-accounts-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Attachments API from Puzzle — 1 operation(s) for attachments.
  name: Puzzle Attachments API
  slug: puzzle-attachments-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Bills API from Puzzle — 3 operation(s) for bills.
  name: Puzzle Bills API
  slug: puzzle-bills-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Company API from Puzzle — 10 operation(s) for company.
  name: Puzzle Company API
  slug: puzzle-company-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Customers API from Puzzle — 2 operation(s) for customers.
  name: Puzzle Customers API
  slug: puzzle-customers-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Departments API from Puzzle — 1 operation(s) for departments.
  name: Puzzle Departments API
  slug: puzzle-departments-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Documents API from Puzzle — 1 operation(s) for documents.
  name: Puzzle Documents API
  slug: puzzle-documents-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Invoices API from Puzzle — 2 operation(s) for invoices.
  name: Puzzle Invoices API
  slug: puzzle-invoices-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The JournalEntries API from Puzzle — 2 operation(s) for journalentries.
  name: Puzzle JournalEntries API
  slug: puzzle-journalentries-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The JournalEntry API from Puzzle — 2 operation(s) for journalentry.
  name: Puzzle JournalEntry API
  slug: puzzle-journalentry-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Locations API from Puzzle — 1 operation(s) for locations.
  name: Puzzle Locations API
  slug: puzzle-locations-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Metrics API from Puzzle — 5 operation(s) for metrics.
  name: Puzzle Metrics API
  slug: puzzle-metrics-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The OAuth API from Puzzle — 2 operation(s) for oauth.
  name: Puzzle OAuth API
  slug: puzzle-oauth-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Onboarding API from Puzzle — 1 operation(s) for onboarding.
  name: Puzzle Onboarding API
  slug: puzzle-onboarding-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Payroll API from Puzzle — 6 operation(s) for payroll.
  name: Puzzle Payroll API
  slug: puzzle-payroll-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Products API from Puzzle — 2 operation(s) for products.
  name: Puzzle Products API
  slug: puzzle-products-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Reports API from Puzzle — 7 operation(s) for reports.
  name: Puzzle Reports API
  slug: puzzle-reports-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Requests API from Puzzle — 1 operation(s) for requests.
  name: Puzzle Requests API
  slug: puzzle-requests-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Tasks API from Puzzle — 2 operation(s) for tasks.
  name: Puzzle Tasks API
  slug: puzzle-tasks-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Transactions API from Puzzle — 3 operation(s) for transactions.
  name: Puzzle Transactions API
  slug: puzzle-transactions-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The User API from Puzzle — 3 operation(s) for user.
  name: Puzzle User API
  slug: puzzle-user-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: The Vendors API from Puzzle — 2 operation(s) for vendors.
  name: Puzzle Vendors API
  slug: puzzle-vendors-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: Categories, classes, departments, and projects for classification.
  name: Puzzle Categories API
  slug: puzzle-categories-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: Companies connected to a Puzzle partner account.
  name: Puzzle Companies API
  slug: puzzle-companies-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: Upstream data connections that feed the ledger.
  name: Puzzle Integrations API
  slug: puzzle-integrations-api
- baseURL: https://api.puzzle.io/rest/v0
  baseurl_source: declared
  description: Double-entry journal entries against the general ledger.
  name: Puzzle Journal Entries API
  slug: puzzle-journal-entries-api
artifact_total: 64
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Puzzle Api Accounts API
  slug: open-puzzle-accounts-api
- collection_type: open
  name: Puzzle Api Accounts Attachments API
  slug: open-puzzle-attachments-api
- collection_type: open
  name: Puzzle Api Accounts Bills API
  slug: open-puzzle-bills-api
- collection_type: open
  name: Puzzle Accounting Accounts Categories API
  slug: open-puzzle-categories-api
- collection_type: open
  name: Puzzle Accounting Accounts Companies API
  slug: open-puzzle-companies-api
- collection_type: open
  name: Puzzle Api Accounts Company API
  slug: open-puzzle-company-api
- collection_type: open
  name: Puzzle Api Accounts Customers API
  slug: open-puzzle-customers-api
- collection_type: open
  name: Puzzle Api Accounts Departments API
  slug: open-puzzle-departments-api
- collection_type: open
  name: Puzzle Api Accounts Documents API
  slug: open-puzzle-documents-api
- collection_type: open
  name: Puzzle Accounting Accounts Integrations API
  slug: open-puzzle-integrations-api
- collection_type: open
  name: Puzzle Api Accounts Invoices API
  slug: open-puzzle-invoices-api
- collection_type: open
  name: Puzzle Accounting API
  slug: open-puzzle-io
- collection_type: open
  name: Puzzle Accounting Accounts Journal Entries API
  slug: open-puzzle-journal-entries-api
- collection_type: open
  name: Puzzle Api Accounts JournalEntries API
  slug: open-puzzle-journalentries-api
- collection_type: open
  name: Puzzle Api Accounts JournalEntry API
  slug: open-puzzle-journalentry-api
- collection_type: open
  name: Puzzle Api Accounts Locations API
  slug: open-puzzle-locations-api
- collection_type: open
  name: Puzzle Api Accounts Metrics API
  slug: open-puzzle-metrics-api
- collection_type: open
  name: Puzzle Api Accounts OAuth API
  slug: open-puzzle-oauth-api
- collection_type: open
  name: Puzzle Api Accounts Onboarding API
  slug: open-puzzle-onboarding-api
- collection_type: open
  name: Puzzle Api Accounts Payroll API
  slug: open-puzzle-payroll-api
- collection_type: open
  name: Puzzle Api Accounts Products API
  slug: open-puzzle-products-api
- collection_type: open
  name: Puzzle Api Accounts Reports API
  slug: open-puzzle-reports-api
- collection_type: open
  name: Puzzle Api Accounts Requests API
  slug: open-puzzle-requests-api
- collection_type: open
  name: Puzzle Api Accounts Tasks API
  slug: open-puzzle-tasks-api
- collection_type: open
  name: Puzzle Api Accounts Transactions API
  slug: open-puzzle-transactions-api
- collection_type: open
  name: Puzzle Api Accounts User API
  slug: open-puzzle-user-api
- collection_type: open
  name: Puzzle Api Accounts Vendors API
  slug: open-puzzle-vendors-api
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
  url: openapi/_original/puzzle-openapi-original.json
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
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/puzzlefin
- group: commercial
  title: ''
  type: Plans
  url: plans/puzzle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/puzzle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/puzzle-finops.yml
created: '2026-07-17'
description: 'Puzzle is an AI-powered accounting platform for startups, SMBs, and accounting firms, built around a real-time, append-only general ledger. Its agent-native architecture pairs deterministic Puzzle agents that draft categorization, reconciliation, and month-end close for human review with native integrations to banking, card, revenue, and payroll systems (Stripe, Brex, Mercury, Ramp, Gusto, Rippling, and more). The Puzzle Accounting API gives developers programmatic, OAuth 2.0 + PKCE-secured access to the same ledger: transactions, chart of accounts, journal entries, bills, invoices, vendors, customers, payroll, financial statements (income statement, balance sheet, cash activity), and metrics such as burn, runway, and revenue. A companion read-only MCP server connects AI tools like Claude, Cursor, and Windsurf to the ledger for natural-language financial analysis.'
finops:
- name: Puzzle Finops
  service_category: Accounting and Financial Management
  slug: puzzle-finops
image: https://puzzle.io/favicon.ico
layout: provider
mcp_servers:
- description: Puzzle publishes a read-only Model Context Protocol (MCP) server that connects AI tools to a company's real-time general ledger for natural-language financial analysis and reporting. Because third-par
  name: Puzzle MCP Server
  slug: puzzle-mcp-server
modified: '2026-08-08'
name: Puzzle
nav: Providers
network: true
overview: 'Puzzle publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Bills API, and 23 more. Tagged areas include Company, Accounting, Financial, Bookkeeping, and Fintech.


  Puzzle''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 31 more developer resources.'
plans:
- name: Puzzle Plans Pricing
  plan_count: 4
  slug: puzzle-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Puzzle Rate Limits
  slug: puzzle-rate-limits
scopes:
- name: Puzzle Scopes
  scope_count: 21
  slug: puzzle-scopes
  summary_line: 21 scopes
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 4.5
    contract_quality: 48.0
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/puzzle/refs/heads/main/screenshots/puzzle-2026-08-17T081407.png
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
- agent-native
- MCP
website: https://puzzle.io
---
