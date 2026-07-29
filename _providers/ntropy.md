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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 42
  human_in_the_loop: 1
  name: Ntropy Agentic Access
  operation_count: 77
  slug: ntropy-agentic-access
  summary_line: 77 operations · 42 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: Ledger operations
  name: Ntropy Account Holder API
  slug: ntropy-account-holder-api
- description: The accountHolders API from Ntropy — 2 operation(s) for accountholders.
  name: Ntropy accountHolders API
  slug: ntropy-accountholders-api
- description: The bank statements API allows you to view and enrich transactions found in bank statements. Below is a table with the description of each of the statuses and steps that each bank statement goes throu
  name: Ntropy Bank statements API
  slug: ntropy-bank-statements-api
- description: The bankStatements API from Ntropy — 4 operation(s) for bankstatements.
  name: Ntropy bankStatements API
  slug: ntropy-bankstatements-api
- description: The batches API from Ntropy — 3 operation(s) for batches.
  name: Ntropy batches API
  slug: ntropy-batches-api
- description: The categories API from Ntropy — 2 operation(s) for categories.
  name: Ntropy categories API
  slug: ntropy-categories-api
- description: Transaction enrichment.
  name: Ntropy Enrichment API
  slug: ntropy-enrichment-api
- description: The entities API from Ntropy — 4 operation(s) for entities.
  name: Ntropy entities API
  slug: ntropy-entities-api
- description: The Labels API from Ntropy — 2 operation(s) for labels.
  name: Ntropy Labels API
  slug: ntropy-labels-api
- description: Miscellaneous endpoint.
  name: Ntropy Misc API
  slug: ntropy-misc-api
- description: The personalization API from Ntropy — 6 operation(s) for personalization.
  name: Ntropy personalization API
  slug: ntropy-personalization-api
- description: The recurrence API from Ntropy — 1 operation(s) for recurrence.
  name: Ntropy recurrence API
  slug: ntropy-recurrence-api
- description: The Reporting API from Ntropy — 2 operation(s) for reporting.
  name: Ntropy Reporting API
  slug: ntropy-reporting-api
- description: The reports API from Ntropy — 2 operation(s) for reports.
  name: Ntropy reports API
  slug: ntropy-reports-api
- description: The transactions API from Ntropy — 3 operation(s) for transactions.
  name: Ntropy transactions API
  slug: ntropy-transactions-api
- description: The webhooks API from Ntropy — 2 operation(s) for webhooks.
  name: Ntropy webhooks API
  slug: ntropy-webhooks-api
artifact_total: 22
asyncapis:
- description: Event-driven notifications from the Ntropy API. Ntropy POSTs an event to the registered webhook url. If a token was set at creation it is sent in the X-Ntropy-Token header. Delivery is at-least-once (
  name: Ntropy Webhooks
  slug: ntropy-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://ntropy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ntropy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ntropy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ntropy.com/documentation/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ntropy.com/onboarding
- group: operate
  title: ''
  type: Support
  url: https://docs.ntropy.com/support
- group: company
  title: ''
  type: Blog
  url: https://ntropy.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ntropy-network
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.ntropy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ntropy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ntropy.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/ntropy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ntropy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ntropy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ntropy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ntropy-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/ntropy-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/ntropy-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ntropy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ntropy-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ntropy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ntropy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ntropy-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ntropy-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ntropy-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ntropy-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ntropy-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/ntropy-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ntropy-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Ntropy provides a financial data standardization and enrichment API that turns raw bank transactions and bank-statement PDFs into structured, contextual data. Its products cover transaction enrichment (categorization, entity/merchant identification and recurring-payment detection), bank-statement OCR and extraction, account-holder ledgers, entity resolution, personalization rules, and event webhooks. The v3 REST API (base https://api.ntropy.com) uses API-key header auth, cursor pagination, and a credit-based rate model, and is used for underwriting, transaction approval, personal finance, customer retention and accounting. Ntropy is a fintech company backed by QED Investors; it ships an official Python SDK and a first-party MCP server.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ntropy.png
layout: provider
mcp_servers:
- description: ''
  name: ntropy-mcp.yml
  slug: ntropy-mcpyml
modified: '2026-07-20'
name: Ntropy
nav: Providers
network: true
overview: 'Ntropy publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account Holder API, accountHolders API, Bank statements API, and 13 more. Tagged areas include Company, Fintech, Transaction Enrichment, Financial Data, and Data Enrichment.


  The Ntropy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ntropy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 52
rate_limits:
- limit_count: 24
  name: Ntropy Rate Limits
  slug: ntropy-rate-limits
score:
  band: developing
  composite: 52.8
  delta: -2.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.3
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 60.5
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ntropy Authentication
  slug: ntropy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ntropy Domain Security
  slug: ntropy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ntropy
tags:
- Company
- Fintech
- Transaction Enrichment
- Financial Data
- Data Enrichment
- Bank Statements
- Categorization
- Underwriting
website: https://ntropy.com/
---
