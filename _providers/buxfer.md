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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
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
artifact_total: 9
common:
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


  Buxfer''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 16 more developer resources.'
random_paper: 40
score:
  band: developing
  composite: 50.8
  delta: 2.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.5
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 48.3
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
