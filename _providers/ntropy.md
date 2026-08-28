---
access_model:
  confidence: high
  label: Self-serve signup with free trial credits; pricing behind the dashboard
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - https://docs.ntropy.com/onboarding
  - https://docs.ntropy.com/introduction
  - plans/ntropy-plans-pricing.yml
  trial: true
  try_now: false
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-26'
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
artifact_total: 41
asyncapis:
- description: Event-driven notifications from the Ntropy API. Ntropy POSTs an event to the registered webhook url. If a token was set at creation it is sent in the X-Ntropy-Token header. Delivery is at-least-once (
  name: Ntropy Webhooks
  slug: ntropy-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference Account Holder API
  slug: open-ntropy-account-holder-api
- collection_type: open
  name: API Reference Account Holder accountHolders API
  slug: open-ntropy-accountholders-api
- collection_type: open
  name: API Reference Account Holder Bank statements API
  slug: open-ntropy-bank-statements-api
- collection_type: open
  name: API Reference Account Holder bankStatements API
  slug: open-ntropy-bankstatements-api
- collection_type: open
  name: API Reference Account Holder batches API
  slug: open-ntropy-batches-api
- collection_type: open
  name: API Reference Account Holder categories API
  slug: open-ntropy-categories-api
- collection_type: open
  name: API Reference Account Holder Enrichment API
  slug: open-ntropy-enrichment-api
- collection_type: open
  name: API Reference Account Holder entities API
  slug: open-ntropy-entities-api
- collection_type: open
  name: API Reference Account Holder Labels API
  slug: open-ntropy-labels-api
- collection_type: open
  name: API Reference Account Holder Misc API
  slug: open-ntropy-misc-api
- collection_type: open
  name: API Reference Account Holder personalization API
  slug: open-ntropy-personalization-api
- collection_type: open
  name: API Reference Account Holder recurrence API
  slug: open-ntropy-recurrence-api
- collection_type: open
  name: API Reference Account Holder Reporting API
  slug: open-ntropy-reporting-api
- collection_type: open
  name: API Reference Account Holder reports API
  slug: open-ntropy-reports-api
- collection_type: open
  name: API Reference Account Holder transactions API
  slug: open-ntropy-transactions-api
- collection_type: open
  name: API Reference Account Holder webhooks API
  slug: open-ntropy-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ntropy-api-v3-overlay.yaml
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
- group: start
  title: ''
  type: Login
  url: https://dashboard.ntropy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ntropy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ntropy.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ntropy.com/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/17988251/UVsQriab
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ntropy.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ntropy-network/ntropy-sdk
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ntropy-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ntropy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ntropy-well-known.yml
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
- group: auth
  title: ''
  type: TrustCenter
  url: security/ntropy-trust-center.yml
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
- group: commercial
  title: ''
  type: Plans
  url: plans/ntropy-plans-pricing.yml
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
  name: Ntropy MCP Server
  slug: ntropy-mcp-server
modified: '2026-08-14'
name: Ntropy
nav: Providers
network: true
overview: 'Ntropy publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account Holder API, accountHolders API, Bank statements API, and 13 more. Tagged areas include Company, Fintech, Transaction Enrichment, Financial Data, and Data Enrichment.


  The Ntropy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ntropy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 31 more developer resources.'
plans:
- name: Ntropy Plans Pricing
  plan_count: 0
  slug: ntropy-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 24
  name: Ntropy Rate Limits
  slug: ntropy-rate-limits
score:
  band: strong
  composite: 62.1
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 65.4
    developer_ergonomics: 70.8
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 45.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ntropy/refs/heads/main/screenshots/ntropy-2026-08-07T185714.png
security:
- kind: authentication
  name: Ntropy Authentication
  slug: ntropy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ntropy Domain Security
  slug: ntropy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ntropy Trust Center
  slug: ntropy-trust-center
  summary_line: SOC 2 Type 2
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
