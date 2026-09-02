---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Xiaoman Agentic Access
  operation_count: 137
  slug: xiaoman-agentic-access
  summary_line: 137 operations · 57 acting
api_count: 1
apis:
- description: The Companies API from OKKI Go (go.okki.ai) — 4 operations for B2B company search, unlock, profile and decision-maker email retrieval.
  name: OKKI Go Companies API
  slug: xiaoman-companies-api
- description: The Contacts API from OKKI Go (go.okki.ai) — 1 retired operation (POST /api/v1/contacts/search returns 410 Gone; use company unlock + profileEmails).
  name: OKKI Go Contacts API
  slug: xiaoman-contacts-api
- description: The Credits API from OKKI Go (go.okki.ai) — 1 operation returning remaining company-search points and EDM email quota.
  name: OKKI Go Credits API
  slug: xiaoman-credits-api
- description: The 产品 (products and general CRM) module of the Xiaoman OKKI CRM Open API — 113 operations across products, customers, leads, opportunities, orders, quotations, payments, suppliers, inventory, users a
  name: Xiaoman (OKKI CRM) 产品 API
  slug: xiaoman-default-api
- description: The devops相关 module of the Xiaoman OKKI CRM Open API — 6 internal integration operations (DingTalk and TAPD webhooks, Sobot token, app version release).
  name: Xiaoman (OKKI CRM) devops相关 API
  slug: xiaoman-devops-api
- description: The Emails API from OKKI Go (go.okki.ai) — 6 operations for batch and personalized cold-outreach email sending and per-mail delivery tracking.
  name: OKKI Go Emails API
  slug: xiaoman-emails-api
- description: The s7.1 release group of the Xiaoman OKKI CRM Open API — 35 operations covering customer detail/field dictionaries, follow-up trails, inventory, capital accounts and reporting.
  name: Xiaoman (OKKI CRM) s7.1 API
  slug: xiaoman-s7-1-api
artifact_total: 31
asyncapis:
- description: ''
  name: Xiaoman Crm Webhooks
  slug: xiaoman-crm-webhooks
collections:
- collection_type: postman
  name: OKKI Go Companies API
  slug: postman-xiaoman-companies-api
- collection_type: postman
  name: OKKI Go Companies Contacts API
  slug: postman-xiaoman-contacts-api
- collection_type: postman
  name: OKKI Go Companies Credits API
  slug: postman-xiaoman-credits-api
- collection_type: postman
  name: OKKI Go Companies 产品 API
  slug: postman-xiaoman-default-api
- collection_type: postman
  name: OKKI Go Companies devops相关 API
  slug: postman-xiaoman-devops-api
- collection_type: postman
  name: OKKI Go Companies Emails API
  slug: postman-xiaoman-emails-api
- collection_type: postman
  name: OKKI Go Companies s7.1 API
  slug: postman-xiaoman-s7-1-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OKKI Go Companies API
  slug: open-xiaoman-companies-api
- collection_type: open
  name: OKKI Go Contacts API
  slug: open-xiaoman-contacts-api
- collection_type: open
  name: OKKI Go Credits API
  slug: open-xiaoman-credits-api
- collection_type: open
  name: Xiaoman (OKKI CRM) 产品 API
  slug: open-xiaoman-default-api
- collection_type: open
  name: Xiaoman (OKKI CRM) devops相关 API
  slug: open-xiaoman-devops-api
- collection_type: open
  name: OKKI Go Emails API
  slug: open-xiaoman-emails-api
- collection_type: open
  name: Xiaoman (OKKI CRM) s7.1 API
  slug: open-xiaoman-s7-1-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/xiaoman-okki/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xiaoman-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xiaoman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xiaoman.cn
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.xiaoman.cn
- group: docs
  title: ''
  type: Documentation
  url: https://open.xiaoman.cn
- group: docs
  title: ''
  type: APIReference
  url: https://open.xiaoman.cn
- group: start
  title: ''
  type: GettingStarted
  url: https://open.xiaoman.cn/doc-338269
- group: operate
  title: ''
  type: Support
  url: https://www.yuque.com/help.xiaoman
- group: company
  title: ''
  type: Blog
  url: https://www.xiaoman.cn/knowledge/
- group: start
  title: ''
  type: Login
  url: https://login.xiaoman.cn/login?system_id=v5client
- group: start
  title: ''
  type: SignUp
  url: https://www.xiaoman.cn/register.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xiaoman.cn/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xiaoman.cn/authorization.html
- group: commercial
  title: ''
  type: Pricing
  url: https://go.okki.ai/pricing
- group: auth
  title: ''
  type: Authentication
  url: authentication/xiaoman-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xiaoman-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xiaoman-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xiaoman-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xiaoman-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xiaoman-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xiaoman-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xiaoman-plans.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/xiaoman-crm-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xiaoman-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/xiaoman-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/xiaoman-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/xiaoman-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xiaoman-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/okki-go/SKILL.md
- group: other
  title: ''
  type: Overlay
  url: overlays/xiaoman-openapi-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/xiaoman-tool-crosswalk.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xiaoman-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/okki-op
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/okki-op/okki-go
created: '2026-07-17'
description: Xiaoman Technology (小满科技, OKKI) is an AI-powered foreign-trade sales platform under Alibaba International Station, serving Chinese B2B exporters with the OKKI CRM, OKKI AiReach multi-channel customer acquisition, OKKI Shops site building, and OKKI Go, a B2B prospecting engine built for AI agents. The OKKI CRM Open API (open.xiaoman.cn) exposes 119 OAuth2 module-scoped operations across customers, leads, opportunities, products, sales and purchase orders, quotations, payments, suppliers, inventory, users, and Pro-plan webhook message-push subscriptions. The OKKI Go API (go.okki.ai) provides company search, contact unlock, and cold-email outreach, shipped with a provider-published Agent Skill on npm (@okki-global/okki-go) that installs into Claude Code, Cursor, and other agent runtimes. Originally surfaced as a Qiming portfolio company.
image: https://www.xiaoman.cn/favicon.ico
layout: provider
mcp_servers:
- description: No official hosted MCP server was found for Xiaoman/OKKI. Notably, the provider ships agent access as a packaged Agent Skill instead (@okki-global/okki-go, see skills/) with script wrappers around the
  name: Xiaoman (OKKI) MCP Server
  slug: xiaoman-okki-mcp-server
modified: '2026-08-13'
name: Xiaoman (OKKI)
nav: Providers
network: true
overview: 'Xiaoman (OKKI) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including OKKI Go Companies API, OKKI Go Contacts API, OKKI Go Credits API, and 4 more. Tagged areas include Company, CRM, Foreign Trade, B2B, and Sales.


  The Xiaoman (OKKI) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Xiaoman (OKKI)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 29 more developer resources.'
plans:
- name: Xiaoman Plans
  plan_count: 4
  slug: xiaoman-plans
random_paper: 14
rate_limits:
- limit_count: 3
  name: Xiaoman Rate Limits
  slug: xiaoman-rate-limits
scopes:
- name: Xiaoman Scopes
  scope_count: 12
  slug: xiaoman-scopes
  summary_line: 12 scopes · password/clientCredentials
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 25
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -5.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 34.0
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: unknown
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/xiaoman/refs/heads/main/screenshots/xiaoman-2026-08-17T083013.png
security:
- kind: authentication
  name: Xiaoman Authentication
  slug: xiaoman-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Xiaoman Domain Security
  slug: xiaoman-domain-security
  summary_line: TLSv1.2
skill_count: 1
skills:
- name: okki-go
  slug: okki-go
slug: xiaoman
tags:
- Company
- CRM
- Foreign Trade
- B2B
- Sales
- Prospecting
- Email Marketing
- AI Agents
- China
- Alibaba
website: https://xiaoman.cn
---
