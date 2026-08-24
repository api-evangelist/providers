---
access_model:
  confidence: medium
  label: Demo-gated SaaS with an unauthenticated public lead-magnet API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://zoca.com/pricing
  - https://public.zoca.com/swagger.json
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1489
  human_in_the_loop: 37
  name: Zoca Agentic Access
  operation_count: 2624
  slug: zoca-agentic-access
  summary_line: 2624 operations · 1489 acting · 37 human-in-the-loop
api_count: 3
apis:
- description: The Zoca platform API — the backend the Zoca web application and the iOS/Android apps call. 1,413 paths and 1,700 operations covering scheduling and bookings, website generation and custom domains, Go
  name: Zoca Platform API
  slug: zoca-platform-api
- description: The Zoca tasks and automation service. 785 paths and 855 operations under /tasks/api/v1 covering the AI content queue and content planning, FrontDesk voice and SMS agent onboarding on Retell and Twili
  name: Zoca Tasks API
  slug: zoca-tasks-api
- description: Zoca's unauthenticated public surface — the 69 operations behind the free self-serve tools on zoca.com. Covers the Local Business Demand Tracker (keyword demand and keyword intelligence), Google Busin
  name: Zoca Public API
  slug: zoca-public-api
artifact_total: 11
asyncapis:
- description: ''
  name: Zoca Webhooks
  slug: zoca-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoca-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://zoca.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://zoca.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/zoca-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://zoca.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zoca.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zoca.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://zoca.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.zoca.com/login
- group: operate
  title: ''
  type: Support
  url: https://zoca.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoca-ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.zoca.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.zoca.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoca-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zoca-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zoca-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zoca-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoca-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zoca-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zoca-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zoca-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/zoca-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zoca-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zoca-llms.txt
- group: design
  title: ''
  type: Components
  url: components/zoca-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoca-domain-security.yml
created: '2026-07-17'
description: 'Zoca is an AI-powered marketing platform built for local beauty and wellness businesses — salons, spas, med spas and wellness clinics. It packages its automation as agents: a Discovery Agent that improves local ranking and Google Business Profile visibility, a Win Agent that converts inquiries into confirmed appointments over chat, SMS and voice, a Loyalty Agent that drives rebooking and retention, and a Social Agent that produces Instagram, TikTok and Facebook content. Zoca also runs free self-serve tools including a Local Business Demand Tracker, a Local Website Grader and a Google Business Profile Optimizer. Zoca is operated by ZOCAAI TECHNOLOGIES PRIVATE LIMITED, was founded in 2021, and is an Accel portfolio company. Zoca runs no developer program — no portal, no API reference, no SDK and no documented API — but it serves three real OpenAPI 3.0.0 documents publicly and unauthenticated at api.zoca.ai/swagger.json, tasks.zoca.ai/swagger.json and public.zoca.com/swagger.json,
  together describing 2,624 operations across 2,267 paths. Those are the application''s own backend contracts rather than a product, and they ship with minified operationIds and untyped schemas.'
image: https://cdn.prod.website-files.com/68137618ce08fc7361daa786/6824fbebce901ed009a1e222_3.avif
layout: provider
mcp_servers:
- description: ''
  name: Zoca MCP Server
  slug: zoca-mcp-server
modified: '2026-08-13'
name: Zoca
nav: Providers
network: true
overview: 'Zoca publishes 3 APIs on the [APIs.io](https://apis.io/) network: Platform API, Tasks API, and Public API. Tagged areas include Company, Artificial Intelligence, Marketing, Beauty and Wellness, and Local Business.


  The Zoca catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zoca''s developer surface includes pricing, engineering blog, signup flow, support, authentication, and 22 more developer resources.'
plans:
- name: Zoca Plans Pricing
  plan_count: 3
  slug: zoca-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 11
  name: Zoca Rate Limits
  slug: zoca-rate-limits
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 49.4
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoca/refs/heads/main/screenshots/zoca-2026-08-17T083114.png
security:
- kind: authentication
  name: Zoca Authentication
  slug: zoca-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zoca Domain Security
  slug: zoca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zoca Trust Center
  slug: zoca-trust-center
  summary_line: HIPAA
slug: zoca
tags:
- Company
- Artificial Intelligence
- Marketing
- Beauty and Wellness
- Local Business
- AI Agents
- Appointments
- Scheduling
- Booking
- Local SEO
- Google Business Profile
- Social-Media
- Salon Software
- Spa
- Software-as-a-Service
- Lead Generation
- Customer Retention
- Small Business
website: https://zoca.com/
---
