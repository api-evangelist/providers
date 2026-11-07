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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 1
  name: Ntropy Agentic Access
  operation_count: 77
  slug: ntropy-agentic-access
  summary_line: 77 operations · 37 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: Ledger operations
  name: Ntropy Account Holder API
  slug: ntropy-account-holder-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The bank statements API allows you to view and enrich transactions found in bank statements. Below is a table with the description of each of the statuses and steps that each bank statement goes throu
  name: Ntropy Bank statements API
  slug: ntropy-bank-statements-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The batches API from Ntropy — 3 operation(s) for batches.
  name: Ntropy Batches API
  slug: ntropy-batches-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The categories API from Ntropy — 2 operation(s) for categories.
  name: Ntropy Categories API
  slug: ntropy-categories-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: Transaction enrichment.
  name: Ntropy Enrichment API
  slug: ntropy-enrichment-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The entities API from Ntropy — 4 operation(s) for entities.
  name: Ntropy Entities API
  slug: ntropy-entities-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The Labels API from Ntropy — 2 operation(s) for labels.
  name: Ntropy Labels API
  slug: ntropy-labels-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: Miscellaneous endpoint.
  name: Ntropy Misc API
  slug: ntropy-misc-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The personalization API from Ntropy — 6 operation(s) for personalization.
  name: Ntropy Personalization API
  slug: ntropy-personalization-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The recurrence API from Ntropy — 1 operation(s) for recurrence.
  name: Ntropy Recurrence API
  slug: ntropy-recurrence-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The Reporting API from Ntropy — 2 operation(s) for reporting.
  name: Ntropy Reporting API
  slug: ntropy-reporting-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The reports API from Ntropy — 2 operation(s) for reports.
  name: Ntropy Reports API
  slug: ntropy-reports-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The transactions API from Ntropy — 3 operation(s) for transactions.
  name: Ntropy Transactions API
  slug: ntropy-transactions-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The webhooks API from Ntropy — 2 operation(s) for webhooks.
  name: Ntropy Webhooks API
  slug: ntropy-webhooks-api
- baseURL: https://api.ntropy.com
  baseurl_source: declared
  description: The Account Holders API from Ntropy — 2 operation(s) for account holders.
  name: Ntropy Account Holders API
  slug: ntropy-account-holders-api
artifact_total: 44
asyncapis:
- description: Event-driven notifications from the Ntropy API. Ntropy POSTs an event to the registered webhook url. If a token was set at creation it is sent in the X-Ntropy-Token header. Delivery is at-least-once (
  name: Ntropy Webhooks
  slug: ntropy-webhooks-asyncapi
collections:
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
- group: commercial
  href: https://artifacts.apis.io/ntropy/plans/ntropy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ntropy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ntropy/rate-limits/ntropy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ntropy-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/ntropy/capabilities/ntropy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ntropy-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/ntropy-network/ntropy-sdk/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/ntropy/overlays/ntropy-api-v3-overlay.yaml
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
  href: https://artifacts.apis.io/ntropy/packages/ntropy-packages.yml
  title: ''
  type: Packages
  url: packages/ntropy-packages.yml
- group: build
  href: https://artifacts.apis.io/ntropy/packages/ntropy-packages.yml
  title: ''
  type: SDKs
  url: packages/ntropy-packages.yml
- group: agent
  href: https://artifacts.apis.io/ntropy/mcp/ntropy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ntropy-mcp.yml
- group: build
  href: https://artifacts.apis.io/ntropy/mcp/ntropy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ntropy-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ntropy/llms/ntropy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ntropy-llms.txt
- group: agent
  href: https://artifacts.apis.io/ntropy/well-known/ntropy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ntropy-well-known.yml
- group: auth
  href: https://artifacts.apis.io/ntropy/authentication/ntropy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ntropy-authentication.yml
- group: agent
  href: https://artifacts.apis.io/ntropy/agentic-access/ntropy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ntropy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ntropy/security/ntropy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ntropy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ntropy/security/ntropy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ntropy-trust-center.yml
- group: design
  href: https://artifacts.apis.io/ntropy/conformance/ntropy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ntropy-conformance.yml
- group: design
  href: https://artifacts.apis.io/ntropy/errors/ntropy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ntropy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ntropy/lifecycle/ntropy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ntropy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ntropy/conventions/ntropy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ntropy-conventions.yml
- group: operate
  href: https://artifacts.apis.io/ntropy/changelog/ntropy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ntropy-changelog.yml
- group: design
  href: https://artifacts.apis.io/ntropy/data-model/ntropy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ntropy-data-model.yml
- group: operate
  href: https://artifacts.apis.io/ntropy/rate-limits/ntropy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ntropy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ntropy/plans/ntropy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ntropy-plans-pricing.yml
- group: docs
  href: https://artifacts.apis.io/ntropy/asyncapi/ntropy-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/ntropy-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/ntropy/asyncapi/ntropy-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/ntropy-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/ntropy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Ntropy provides a financial data standardization and enrichment API that turns raw bank transactions and bank-statement PDFs into structured, contextual data. Its products cover transaction enrichment (categorization, entity/merchant identification and recurring-payment detection), bank-statement OCR and extraction, account-holder ledgers, entity resolution, personalization rules, and event webhooks. The v3 REST API (base https://api.ntropy.com) uses API-key header auth, cursor pagination, and a credit-based rate model, and is used for underwriting, transaction approval, personal finance, customer retention and accounting. Ntropy is a fintech company backed by QED Investors; it ships an official Python SDK and a first-party MCP server.
finops:
- has_sources: true
  method: derived
  name: Ntropy Finops
  primary_unit: ''
  service_category: ''
  slug: ntropy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ntropy.png
layout: provider
mcp_servers:
- description: ''
  name: Ntropy MCP Server
  slug: ntropy-mcp-yml
modified: '2026-08-14'
name: Ntropy
nav: Providers
network: true
overview: 'Ntropy publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Holder API, Bank statements API, Batches API, and 12 more. Tagged areas include Company, Fintech, Transaction Enrichment, Financial Data, and Data Enrichment.


  The Ntropy catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ntropy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 35 more developer resources.'
plans:
- name: Ntropy Plans Pricing
  plan_count: 0
  slug: ntropy-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 24
  name: Ntropy Rate Limits
  slug: ntropy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Ntropy API Rules
  rule_count: 55
  severity_counts:
    error: 43
    hint: 0
    info: 3
    warn: 9
  slug: ntropy-rules
score:
  band: strong
  composite: 58.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 62.8
    developer_ergonomics: 70.8
    discoverability: 71.7
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 80.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 26.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ntropy/ntropy-2026-08-07T185714.png
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
skill_count: 3
skills:
- name: Enrich bank transactions with Ntropy
  slug: ntropy-enrich-transactions
- name: Manage Ntropy webhooks
  slug: ntropy-manage-webhooks
- name: Process a bank statement with Ntropy
  slug: ntropy-process-bank-statement
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
