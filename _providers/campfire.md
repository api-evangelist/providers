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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 233
  human_in_the_loop: 2
  name: Campfire Agentic Access
  operation_count: 362
  slug: campfire-agentic-access
  summary_line: 362 operations · 233 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: Operations related to billing and the AP subledger.
  name: Campfire Accounts Payable API
  slug: campfire-accounts-payable-api
- description: Operations related to invoicing and the AR subledger
  name: Campfire Accounts Receivable API
  slug: campfire-accounts-receivable-api
- description: The Bank Reconciliation API from Campfire — 6 operation(s) for bank reconciliation.
  name: Campfire Bank Reconciliation API
  slug: campfire-bank-reconciliation-api
- description: Operations related to accounts, transactions, and other bank-related data.
  name: Campfire Cash Management API
  slug: campfire-cash-management-api
- description: The coa API from Campfire — 1 operation(s) for coa.
  name: Campfire coa API
  slug: campfire-coa-api
- description: The Company Objects API from Campfire — 21 operation(s) for company objects.
  name: Campfire Company Objects API
  slug: campfire-company-objects-api
- description: Operations related to core accounting data, such as the chart of accounts, entity management, and the general ledger.
  name: Campfire Core Accounting API
  slug: campfire-core-accounting-api
- description: The Custom Fields API from Campfire — 1 operation(s) for custom fields.
  name: Campfire Custom Fields API
  slug: campfire-custom-fields-api
- description: Operations related to financial statement generation and data aggregation.
  name: Campfire Financial Statements API
  slug: campfire-financial-statements-api
- description: The Integrations API from Campfire — 3 operation(s) for integrations.
  name: Campfire Integrations API
  slug: campfire-integrations-api
- description: Operations related to revenue recognition, contract management, and contract data aggregation.
  name: Campfire Revenue Recognition API
  slug: campfire-revenue-recognition-api
- description: Operations related to system and accounting settings configuration.
  name: Campfire Settings API
  slug: campfire-settings-api
artifact_total: 18
asyncapis:
- description: ''
  name: Campfire Webhooks
  slug: campfire-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/campfire-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/campfire-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/campfire-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/campfire-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/campfire-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/campfire-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/campfire-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://campfire.ai/blog/announcing-soc-2-type-2-compliance-at-campfire
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/campfire-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/campfire-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/campfire-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/campfire-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/campfire-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/campfire-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/campfire-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/campfire-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.campfire.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.campfire.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.campfire.ai/api-reference/cash-management/list-bank-accounts
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.campfire.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@meetcampfire.com
- group: company
  title: ''
  type: Blog
  url: https://campfire.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://campfire.ai/changelog
- group: start
  title: ''
  type: Login
  url: https://app.meetcampfire.com
- group: start
  title: ''
  type: SignUp
  url: https://campfire.ai/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://campfire.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://campfire.ai/privacy-policy
created: '2026-07-17'
description: Campfire is an AI-native ERP built for high-growth startups and mid-market finance teams outgrowing QuickBooks or Xero, or replacing NetSuite and Sage Intacct. It automates core accounting work — general ledger, bank reconciliation, accounts payable and receivable, revenue recognition, close management, and financial reporting — with an AI assistant (Ember). Campfire ships developer-first REST APIs (188 paths / 362 operations across Cash Management, Core Accounting, Accounts Payable/Receivable, Revenue Recognition, Financial Statements, and Integrations), an official hosted Model Context Protocol (MCP) server, and outbound webhooks. Founded 2023; backed by Accel, Ribbit Capital, Foundation Capital, Capital49, and Y Combinator.
image: https://cdn.sanity.io/images/zu7n19wi/production/97e3241f607c6a5bfab50ffb0bcdb75b63fd5071-9781x5136.png?rect=0,13,9781,5111&w=1200&h=627&fit=crop&auto=format
layout: provider
mcp_servers:
- description: ''
  name: campfire-mcp.yml
  slug: campfire-mcpyml
modified: '2026-07-18'
name: Campfire
nav: Providers
network: true
overview: 'Campfire publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts Payable API, Accounts Receivable API, Bank Reconciliation API, and 9 more. Tagged areas include Company, Accounting, ERP, Finance, and Revenue Recognition.


  The Campfire catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Campfire''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 29
scopes:
- name: Campfire Scopes
  scope_count: 3
  slug: campfire-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.1
  delta: 1.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 57.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/campfire/refs/heads/main/screenshots/campfire-2026-07-25T204311.png
security:
- kind: authentication
  name: Campfire Authentication
  slug: campfire-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Campfire Domain Security
  slug: campfire-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: campfire
tags:
- Company
- Accounting
- ERP
- Finance
- Revenue Recognition
- Accounts Payable
- Accounts Receivable
- AI
website: https://docs.campfire.ai
---
