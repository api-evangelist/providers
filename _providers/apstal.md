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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.7
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Hosted MCP server exposing Apstal analytics via JSON-RPC 2.0 over Streamable HTTP. Public tools (login, register, server_info) and authenticated tools (execute_sql, get_analytics, list_projects, regis
  name: Apstal MCP Server
  slug: apstal-mcp-server
- description: 'Documented REST surface for programmatic access to Apstal analytics: POST /api/v1/m for batched event ingestion (max 100 events per request), POST /api/v1/stream for rrweb session-replay chunk upload,'
  name: Apstal Analytics API
  slug: apstal-analytics-api
artifact_total: 9
asyncapis:
- description: ''
  name: Apstal Realtime Events
  slug: apstal-realtime-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apstal-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apstal-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/apstal-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apstal-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/apstal-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apstal-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apstal-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apstal-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apstal-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apstal.com
- group: commercial
  title: ''
  type: Plans
  url: plans/apstal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apstal-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/apstal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apstal-packages.yml
- group: design
  title: ''
  type: Components
  url: components/apstal-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apstal-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apstal-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://apstal.com/dpa
- group: other
  title: ''
  type: EventSurface
  url: asyncapi/apstal-realtime-events.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apstal.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://apstal.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apstal.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://apstal.com/docs/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://apstal.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://apstal.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://apstal.com/faq
- group: company
  title: ''
  type: Blog
  url: https://apstal.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apstal
- group: commercial
  title: ''
  type: Pricing
  url: https://apstal.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apstal.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apstal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apstal.com/privacy
created: '2026-07-22'
description: 'AI-first website analytics and visitor tracking platform that replaces traditional dashboards with a natural-language chatbot interface, offering conversational analytics, cookieless tracking, session replays, heatmaps, funnels, error tracking, Core Web Vitals and AI-agent traffic detection. Apstal is agent-native by design: its primary programmatic surface is a hosted MCP server at https://apstal.com/api/mcp (JSON-RPC 2.0 over Streamable HTTP, protocol 2025-06-18) whose tools/list is answerable anonymously, backed by a documented REST ingestion and stats API, a WebSocket real-time stream, an SSE natural-language query endpoint, an A2A agent card, two provider-authored Agent Skills, an llms.txt, OAuth 2.0 authorization-server and protected-resource metadata, and an MCP server card. The company is based in Poland and publishes a GDPR Data Processing Agreement.'
image: https://apstal.com/logos/apstal-mark.svg
layout: provider
mcp_servers:
- description: ''
  name: Apstal MCP Server
  slug: apstal-mcp-server
modified: '2026-08-13'
name: Apstal
nav: Providers
network: true
overview: 'Apstal publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Web Analytics, Privacy, Session Replay, and Heatmaps.


  The Apstal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apstal''s developer surface includes authentication, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 26 more developer resources.'
plans:
- name: Apstal Plans Pricing
  plan_count: 3
  slug: apstal-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Apstal Rate Limits
  slug: apstal-rate-limits
scopes:
- name: Apstal Scopes
  scope_count: 3
  slug: apstal-scopes
  summary_line: 3 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 58.0
    catalog_earned_first_party: 24.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 52.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apstal/refs/heads/main/screenshots/apstal-2026-07-25T200912.png
security:
- kind: authentication
  name: Apstal Authentication
  slug: apstal-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Apstal Domain Security
  slug: apstal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apstal
tags:
- Analytics
- Web Analytics
- Privacy
- Session Replay
- Heatmaps
- MCP
- agent-native
- Cookieless
- llms-txt
- BigQuery
- GDPR
- A2A
- Agent Skills
- Bot Detection
- Core Web Vitals
website: https://apstal.com/docs
---
