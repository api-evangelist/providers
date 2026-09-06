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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 233
  human_in_the_loop: 2
  name: Campfire Agentic Access
  operation_count: 362
  slug: campfire-agentic-access
  summary_line: 362 operations · 233 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: Operations related to billing and the AP subledger.
  name: Campfire Accounts Payable API
  slug: campfire-accounts-payable-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: Operations related to invoicing and the AR subledger
  name: Campfire Accounts Receivable API
  slug: campfire-accounts-receivable-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: The Bank Reconciliation API from Campfire — 6 operation(s) for bank reconciliation.
  name: Campfire Bank Reconciliation API
  slug: campfire-bank-reconciliation-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: Operations related to accounts, transactions, and other bank-related data.
  name: Campfire Cash Management API
  slug: campfire-cash-management-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: The coa API from Campfire — 1 operation(s) for coa.
  name: Campfire coa API
  slug: campfire-coa-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: The Company Objects API from Campfire — 21 operation(s) for company objects.
  name: Campfire Company Objects API
  slug: campfire-company-objects-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: Operations related to core accounting data, such as the chart of accounts, entity management, and the general ledger.
  name: Campfire Core Accounting API
  slug: campfire-core-accounting-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: The Custom Fields API from Campfire — 1 operation(s) for custom fields.
  name: Campfire Custom Fields API
  slug: campfire-custom-fields-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: Operations related to financial statement generation and data aggregation.
  name: Campfire Financial Statements API
  slug: campfire-financial-statements-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: The Integrations API from Campfire — 3 operation(s) for integrations.
  name: Campfire Integrations API
  slug: campfire-integrations-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: Operations related to revenue recognition, contract management, and contract data aggregation.
  name: Campfire Revenue Recognition API
  slug: campfire-revenue-recognition-api
- baseURL: https://api.meetcampfire.com
  baseurl_source: declared
  description: Operations related to system and accounting settings configuration.
  name: Campfire Settings API
  slug: campfire-settings-api
artifact_total: 31
asyncapis:
- description: ''
  name: Campfire Webhooks
  slug: campfire-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Campfire Developer APIs Accounts Payable API
  slug: open-campfire-accounts-payable-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Accounts Receivable API
  slug: open-campfire-accounts-receivable-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Bank Reconciliation API
  slug: open-campfire-bank-reconciliation-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Cash Management API
  slug: open-campfire-cash-management-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable coa API
  slug: open-campfire-coa-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Company Objects API
  slug: open-campfire-company-objects-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Core Accounting API
  slug: open-campfire-core-accounting-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Custom Fields API
  slug: open-campfire-custom-fields-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Financial Statements API
  slug: open-campfire-financial-statements-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Integrations API
  slug: open-campfire-integrations-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Revenue Recognition API
  slug: open-campfire-revenue-recognition-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Settings API
  slug: open-campfire-settings-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/campfire-openapi-overlay.yaml
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
- description: 'Campfire exposes an official hosted (remote HTTP) MCP server that maps 12 tools directly onto its accounting, company-data, financial-reporting, and revenue/budget API endpoints, so AI tools (Cursor, '
  name: Campfire
  slug: campfire
modified: '2026-07-18'
name: Campfire
nav: Providers
network: true
overview: 'Campfire publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts Payable API, Accounts Receivable API, Bank Reconciliation API, and 9 more. Tagged areas include Company, Accounting, ERP, Finance, and Revenue Recognition.


  The Campfire catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Campfire''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
random_paper: 20
scopes:
- name: Campfire Scopes
  scope_count: 3
  slug: campfire-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 56.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 47.1
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Artificial Intelligence
website: https://docs.campfire.ai
---
