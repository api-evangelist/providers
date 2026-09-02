---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The 合思开放平台 (Ekuaibao / HOSE Open Platform) REST API. 200+ documented operations across contacts, corporation, budgets, expense flows, forms, fee types, pay, payer info, checking bills, city and curren
  name: Ekuaibao Open API
  slug: ekuaibao-open-api
artifact_total: 5
asyncapis:
- description: ''
  name: Ekuaibao Outbound Webhooks
  slug: ekuaibao-outbound-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ekuaibao.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ekuaibao.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ekuaibao.com/docs/open-api/getting-started/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ekuaibao.com/docs/open-api/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ekuaibao.com/docs/open-api/getting-started/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ekuaibao
- group: company
  title: ''
  type: Blog
  url: https://www.ekuaibao.com/news.html
- group: start
  title: ''
  type: SignUp
  url: https://www.ekuaibao.com/register.html
- group: start
  title: ''
  type: Login
  url: https://app.ekuaibao.com/web/app.html#/login
- group: operate
  title: ''
  type: Support
  url: https://www.ekuaibao.com/contact.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ekuaibao.com/website-static/user-agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ekuaibao.com/website-static/user-policy.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ekuaibao.com/updateLog/update-log
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ekuaibao-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ekuaibao-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ekuaibao-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ekuaibao-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ekuaibao-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ekuaibao-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ekuaibao-outbound-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ekuaibao-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ekuaibao-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ekuaibao-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ekuaibao-domain-security.yml
created: '2026-07-17'
description: 'Ekuaibao (合思 / HOSE, formerly 易快报) is a Chinese AI-powered spend-management and expense-control SaaS platform used by more than 7,000 enterprises. It unifies expense reimbursement, business-travel booking and management, corporate payment and settlement, invoice OCR and validation, budget control, BI analytics and electronic accounting archiving. The company operates the 合思开放平台 (Ekuaibao Open Platform), a substantial REST API of 200+ documented operations across two dozen modules — contacts, corporation, budgets, expense flows, forms, fee types, pay and payer info, city and currency master data, data links, matrices, delegates and outbound-message webhooks — letting external systems (OA, ERP, HR, travel) synchronize staff, departments, budgets, documents, invoices and approvals. Access is token-based: an appKey/appSecurity pair is exchanged for a short-lived accessToken (v1) or a JWT-based tenant/platform token (v3).'
image: https://www.ekuaibao.com/uploads/20260421/35efafc6cff1340314ddb0f441d3ecf1.png
layout: provider
mcp_servers:
- description: ''
  name: Ekuaibao MCP Server
  slug: ekuaibao-mcp-server
modified: '2026-07-19'
name: Ekuaibao
nav: Providers
network: true
overview: 'Ekuaibao publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Expense Management, Spend Management, and Travel And Expense.


  The Ekuaibao catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ekuaibao''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, changelog, and 17 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 31.3
  provenance:
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ekuaibao/refs/heads/main/screenshots/ekuaibao-2026-07-25T213044.png
security:
- kind: authentication
  name: Ekuaibao Authentication
  slug: ekuaibao-authentication
  summary_line: accessToken/jwt · 4 schemes
- kind: domain-security
  name: Ekuaibao Domain Security
  slug: ekuaibao-domain-security
  summary_line: TLSv1.2 · HSTS
slug: ekuaibao
tags:
- Company
- Enterprise
- Expense Management
- Spend Management
- Travel And Expense
- Reimbursement
- Finance
- Accounting
- Invoicing
- Software-as-a-Service
- China
website: https://www.ekuaibao.com/
---
