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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: List accounts and balances.
  name: Buxfer Accounts API
  slug: buxfer-accounts-api
- description: Obtain an ephemeral API token.
  name: Buxfer Authentication API
  slug: buxfer-authentication-api
- description: Tags, budgets, reminders.
  name: Buxfer Organization API
  slug: buxfer-organization-api
- description: Groups, contacts and loans for shared expenses.
  name: Buxfer Social API
  slug: buxfer-social-api
- description: Create, edit, delete, list and import transactions.
  name: Buxfer Transactions API
  slug: buxfer-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Buxfer Accounts API
  slug: open-buxfer-accounts-api
- collection_type: open
  name: Buxfer Accounts Authentication API
  slug: open-buxfer-authentication-api
- collection_type: open
  name: Buxfer Accounts Organization API
  slug: open-buxfer-organization-api
- collection_type: open
  name: Buxfer Accounts Social API
  slug: open-buxfer-social-api
- collection_type: open
  name: Buxfer Accounts Transactions API
  slug: open-buxfer-transactions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/buxfer-openapi-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/buxfer-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.buxfer.com/help/security
- group: agent
  title: ''
  type: WellKnown
  url: well-known/buxfer-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.buxfer.com/help/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.buxfer.com/help/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.buxfer.com/help/api
- group: operate
  title: ''
  type: Support
  url: https://www.buxfer.com/help/
- group: company
  title: ''
  type: Blog
  url: https://blog.buxfer.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buxfer.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.buxfer.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.buxfer.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buxfer.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buxfer.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/buxfer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/buxfer-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/buxfer-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/buxfer-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buxfer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buxfer-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/buxfer-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buxfer-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buxfer-domain-security.yml
created: '2026-07-17'
description: Buxfer is a personal finance and money management platform that consolidates bank, investment and retirement accounts in one place. It connects to 20,000+ banks across 70+ countries, tracks assets in 100+ currencies, and provides budgeting with real-time alerts, expense forecasting, net-worth projection, automatic transaction tagging with custom rules, investment and retirement planning, shared-expense groups, and encrypted cloud backups to Dropbox, Google Drive or OneDrive. Buxfer exposes a JSON HTTP API for reading accounts, transactions, tags, budgets, reminders, groups, contacts and loans, and for creating, editing and deleting transactions and uploading statements. Authentication uses a login call that returns an ephemeral token passed on every subsequent request. Buxfer is a Y Combinator company.
image: https://www.buxfer.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: buxfer-mcp.yml
  slug: buxfer-mcpyml
modified: '2026-07-18'
name: Buxfer
nav: Providers
network: true
overview: 'Buxfer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Organization API, and 2 more. Tagged areas include Company, Personal Finance, Money Management, Budgeting, and Banking.


  Buxfer''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 46.5
  delta: 2.3
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 55.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 44.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buxfer/refs/heads/main/screenshots/buxfer-2026-07-25T204124.png
security:
- kind: authentication
  name: Buxfer Authentication
  slug: buxfer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Buxfer Domain Security
  slug: buxfer-domain-security
  summary_line: TLSv1.2 · HSTS
- kind: trust-center
  name: Buxfer Trust Center
  slug: buxfer-trust-center
  summary_line: ISO 27001, PCI DSS
slug: buxfer
tags:
- Company
- Personal Finance
- Money Management
- Budgeting
- Banking
- Fintech
- Financial Data
- Transactions
- Investments
- Expense Tracking
website: https://www.buxfer.com/help/api
---
