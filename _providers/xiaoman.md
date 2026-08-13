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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Xiaoman Agentic Access
  operation_count: 137
  slug: xiaoman-agentic-access
  summary_line: 137 operations · 57 acting
api_count: 7
apis:
- description: The Companies API from Xiaoman (OKKI) — 4 operation(s) for companies.
  name: Xiaoman (OKKI) Companies API
  slug: xiaoman-companies-api
- description: The Contacts API from Xiaoman (OKKI) — 1 operation(s) for contacts.
  name: Xiaoman (OKKI) Contacts API
  slug: xiaoman-contacts-api
- description: The Credits API from Xiaoman (OKKI) — 1 operation(s) for credits.
  name: Xiaoman (OKKI) Credits API
  slug: xiaoman-credits-api
- description: The 产品 API from Xiaoman (OKKI) — 113 operation(s) for 产品.
  name: Xiaoman (OKKI) 产品 API
  slug: xiaoman-default-api
- description: The devops相关 API from Xiaoman (OKKI) — 6 operation(s) for devops相关.
  name: Xiaoman (OKKI) devops相关 API
  slug: xiaoman-devops-api
- description: The Emails API from Xiaoman (OKKI) — 6 operation(s) for emails.
  name: Xiaoman (OKKI) Emails API
  slug: xiaoman-emails-api
- description: The s7.1 API from Xiaoman (OKKI) — 35 operation(s) for s7.1.
  name: Xiaoman (OKKI) s7.1 API
  slug: xiaoman-s7-1-api
artifact_total: 23
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
created: '2026-07-17'
description: Xiaoman Technology (小满科技, OKKI) is an AI-powered foreign-trade sales platform under Alibaba International Station, serving Chinese B2B exporters with the OKKI CRM, OKKI AiReach multi-channel customer acquisition, OKKI Shops site building, and OKKI Go, a B2B prospecting engine built for AI agents. The OKKI CRM Open API (open.xiaoman.cn) exposes 125 OAuth2 module-scoped operations across customers, leads, opportunities, products, sales and purchase orders, quotations, payments, suppliers, inventory, users, and Pro-plan webhook message-push subscriptions. The OKKI Go API (go.okki.ai) provides company search, contact unlock, and cold-email outreach, shipped with a provider-published Agent Skill on npm (@okki-global/okki-go) that installs into Claude Code, Cursor, and other agent runtimes. Originally surfaced as a Qiming portfolio company.
image: https://www.xiaoman.cn/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: xiaoman-mcp.yml
  slug: xiaoman-mcpyml
modified: '2026-07-21'
name: Xiaoman (OKKI)
nav: Providers
network: true
overview: 'Xiaoman (OKKI) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Contacts API, Credits API, and 4 more. Tagged areas include Company, CRM, Foreign Trade, B2B, and Sales.


  The Xiaoman (OKKI) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Xiaoman (OKKI)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 25 more developer resources.'
plans:
- name: Xiaoman Plans
  plan_count: 4
  slug: xiaoman-plans
random_paper: 29
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
  band: strong
  composite: 61.2
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 62.5
    developer_ergonomics: 78.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 61.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
