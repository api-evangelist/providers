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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: The recommended tenant-scoped Open API for customers, tickets, organizations, agents, agent groups, departments, knowledge base, IM sessions, call center, outbound call tasks, questionnaires, work log
  name: Udesk Open API v2
  slug: udesk-open-api-v2
- description: Legacy Open API kept for existing integrations (tickets, customers, IM, call center, help center) with MD5 query-string signature auth; the docs recommend migrating to v2.
  name: Udesk Open API v1 (legacy)
  slug: udesk-open-api-v1-legacy
- description: Bot platform API for applications and robots, FAQ knowledge bases, bot sessions, task-flow entities, external LLM integration, and the robot webhook integration hook.
  name: Udesk Robot (GaussMind) API
  slug: udesk-robot-gaussmind-api
- description: Field-service / after-sales platform API — records, custom fields, filters, users, roles, queues, forms, approvals, SSO, event subscriptions, operation logs, and warehouse management.
  name: ServiceGo API
  slug: servicego-api
- description: Knowledge center service API for knowledge spaces, categories, Q&A knowledge items, and file knowledge, authenticated with a 50-minute Bearer token from /api/auth/open/token.
  name: Udesk KCS Knowledge API
  slug: udesk-kcs-knowledge-api
artifact_total: 10
asyncapis:
- description: 'Event surface derived from Udesk''s published webhook documentation (Udesk ships no AsyncAPI of its own). Three webhook families are documented: - **Open API event callbacks (webhook_v2)** — Udesk POST'
  name: Udesk Event Callbacks (Webhooks)
  slug: udesk-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/udesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.udesk.cn/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.udesk.cn/doc/
- group: docs
  title: ''
  type: Documentation
  url: https://www.udesk.cn/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://www.udesk.cn/doc/apiv2/intro/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.udesk.cn/doc/#_1
- group: operate
  title: ''
  type: Support
  url: https://udesk.udesk.cn/hc
- group: company
  title: ''
  type: Blog
  url: https://blog.udesk.cn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/udesk
- group: start
  title: ''
  type: SignUp
  url: https://cb.s2.udesk.cn/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.udesk.cn/terms_service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.udesk.cn/terms_service.html
- group: build
  title: ''
  type: Packages
  url: packages/udesk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/udesk-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/udesk-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/udesk-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/udesk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/udesk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/udesk-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/udesk-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/udesk-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/udesk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.udesk.cn/product_safety_features.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/udesk-trust-center.yml
- group: design
  title: ''
  type: Components
  url: components/udesk-components.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/udesk-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.udesk.cn/doc/apiv2/webhook_v2/
created: '2026-07-17'
description: Udesk, the flagship product of Beijing Wofeng Times Data Technology (沃丰科技/Wofeng Technology), is a Chinese intelligent customer service and customer-experience platform serving enterprises like Yili, BYD, Schneider Electric, and China Merchants Group. The suite spans omnichannel IM (20+ channels including WeChat, Weibo, and mini-programs), ticketing, a cloud call center with CC PaaS APIs, GaussMind LLM-powered chat/voice robots, ServiceGo field-service management, KCS knowledge management, and video customer service. Its developer center publishes REST-style Open APIs (v2 recommended, v1 legacy), event-callback webhooks, and mobile/web SDKs, all tenant-scoped with signed-request authentication.
image: https://www.udesk.cn/images/index/udesk_fav.ico
layout: provider
modified: '2026-07-21'
name: Udesk
nav: Providers
network: true
overview: 'Udesk publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Customer Service, Call Center, and Ticketing.


  The Udesk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Udesk''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 3
  name: Udesk Rate Limits
  slug: udesk-rate-limits
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 48.6
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/udesk/refs/heads/main/screenshots/udesk-2026-08-17T082537.png
security:
- kind: authentication
  name: Udesk Authentication
  slug: udesk-authentication
  summary_line: signature/bearer/jwt-sso · 7 schemes
- kind: domain-security
  name: Udesk Domain Security
  slug: udesk-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Udesk Trust Center
  slug: udesk-trust-center
  summary_line: ISO 27001:2013, CSA-STAR, 网络安全等级保护三级 (China MLPS Level 3), 可信云认证 NO.07014 (Trusted Cloud)
slug: udesk
tags:
- Company
- Enterprise
- Customer Service
- Call Center
- Ticketing
- Chatbots
- CRM
- Knowledge-Management
- Software-as-a-Service
- China
website: https://www.udesk.cn/
---
