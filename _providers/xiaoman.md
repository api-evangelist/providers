---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 71
  human_in_the_loop: 0
  name: Xiaoman Agentic Access
  operation_count: 172
  slug: xiaoman-agentic-access
  summary_line: 172 operations · 71 acting
api_count: 1
apis:
- baseURL: https://go.okki.ai
  baseurl_source: declared
  description: The Companies API from OKKI Go (go.okki.ai) — 4 operations for B2B company search, unlock, profile and decision-maker email retrieval.
  name: OKKI Go Companies API
  slug: xiaoman-companies-api
- baseURL: https://go.okki.ai
  baseurl_source: declared
  description: The Contacts API from OKKI Go (go.okki.ai) — 1 retired operation (POST /api/v1/contacts/search returns 410 Gone; use company unlock + profileEmails).
  name: OKKI Go Contacts API
  slug: xiaoman-contacts-api
- baseURL: https://go.okki.ai
  baseurl_source: declared
  description: The Credits API from OKKI Go (go.okki.ai) — 1 operation returning remaining company-search points and EDM email quota.
  name: OKKI Go Credits API
  slug: xiaoman-credits-api
- baseURL: https://api-sandbox.xiaoman.cn
  baseurl_source: declared
  description: The 产品 (products and general CRM) module of the Xiaoman OKKI CRM Open API — 113 operations across products, customers, leads, opportunities, orders, quotations, payments, suppliers, inventory, users a
  name: Xiaoman (OKKI CRM) 产品 API
  slug: xiaoman-default-api
- baseURL: https://go.okki.ai
  baseurl_source: declared
  description: The Emails API from OKKI Go (go.okki.ai) — 6 operations for batch and personalized cold-outreach email sending and per-mail delivery tracking.
  name: OKKI Go Emails API
  slug: xiaoman-emails-api
- baseURL: https://api-sandbox.xiaoman.cn
  baseurl_source: declared
  description: The s7.1 release group of the Xiaoman OKKI CRM Open API — 35 operations covering customer detail/field dictionaries, follow-up trails, inventory, capital accounts and reporting.
  name: Xiaoman (OKKI CRM) s7.1 API
  slug: xiaoman-s7-1-api
- baseURL: https://go.okki.ai
  baseurl_source: declared
  description: The Dev Ops API from Xiaoman (OKKI) — 6 operation(s) for dev ops.
  name: Xiaoman (OKKI) Dev Ops API
  slug: xiaoman-dev-ops-api
artifact_total: 32
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
  href: https://artifacts.apis.io/xiaoman/agentic-access/xiaoman-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xiaoman-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/xiaoman/security/xiaoman-domain-security.yml
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
  href: https://artifacts.apis.io/xiaoman/authentication/xiaoman-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xiaoman-authentication.yml
- group: auth
  href: https://artifacts.apis.io/xiaoman/scopes/xiaoman-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/xiaoman-scopes.yml
- group: design
  href: https://artifacts.apis.io/xiaoman/conventions/xiaoman-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xiaoman-conventions.yml
- group: design
  href: https://artifacts.apis.io/xiaoman/errors/xiaoman-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xiaoman-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xiaoman/conformance/xiaoman-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xiaoman-conformance.yml
- group: design
  href: https://artifacts.apis.io/xiaoman/lifecycle/xiaoman-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xiaoman-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/xiaoman/rate-limits/xiaoman-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xiaoman-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/xiaoman/plans/xiaoman-plans.yml
  title: ''
  type: Plans
  url: plans/xiaoman-plans.yml
- group: design
  href: https://artifacts.apis.io/xiaoman/asyncapi/xiaoman-crm-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/xiaoman-crm-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/xiaoman/mcp/xiaoman-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/xiaoman-mcp.yml
- group: build
  href: https://artifacts.apis.io/xiaoman/packages/xiaoman-packages.yml
  title: ''
  type: Packages
  url: packages/xiaoman-packages.yml
- group: build
  href: https://artifacts.apis.io/xiaoman/packages/xiaoman-packages.yml
  title: ''
  type: SDKs
  url: packages/xiaoman-packages.yml
- group: build
  href: https://artifacts.apis.io/xiaoman/cli/xiaoman-cli.yml
  title: ''
  type: CLI
  url: cli/xiaoman-cli.yml
- group: agent
  href: https://artifacts.apis.io/xiaoman/llms/xiaoman-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xiaoman-llms.txt
- group: agent
  href: https://artifacts.apis.io/xiaoman/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/xiaoman/skills/okki-go/SKILL.md
  title: ''
  type: AgentSkill
  url: skills/okki-go/SKILL.md
- group: other
  href: https://artifacts.apis.io/xiaoman/overlays/xiaoman-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xiaoman-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/xiaoman/mcp/xiaoman-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/xiaoman-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/xiaoman/data-model/xiaoman-data-model.yml
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
finops:
- has_sources: true
  method: derived
  name: Xiaoman Finops
  primary_unit: 500 points + 2,500 edm
  service_category: ''
  slug: xiaoman-finops
  template: false
image: https://www.xiaoman.cn/favicon.ico
layout: provider
modified: '2026-08-13'
name: Xiaoman (OKKI)
nav: Providers
network: true
overview: 'Xiaoman (OKKI) publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including OKKI Go Companies API, OKKI Go Contacts API, OKKI Go Credits API, and 4 more. Tagged areas include Company, CRM, Foreign Trade, B2B, and Sales.


  The Xiaoman (OKKI) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Xiaoman (OKKI)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 29 more developer resources.'
plans:
- name: Xiaoman Plans
  plan_count: 5
  slug: xiaoman-plans
- name: Xiaoman Price Estimates
  plan_count: 0
  slug: xiaoman-price-estimates
random_paper: 5
rate_limits:
- limit_count: 3
  name: Xiaoman Rate Limits
  slug: xiaoman-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Xiaoman (OKKI) API Rules
  rule_count: 56
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 9
  slug: xiaoman-rules
scopes:
- name: Xiaoman Scopes
  scope_count: 12
  slug: xiaoman-scopes
  summary_line: 12 scopes · password/clientCredentials
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 32.2
    developer_ergonomics: 79.0
    discoverability: 73.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 62.5
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/xiaoman/xiaoman-2026-08-17T083013.png
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
