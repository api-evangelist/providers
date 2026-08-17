---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-08-17'
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
  name: apstal-mcp.yml
  slug: apstal-mcpyml
modified: '2026-08-13'
name: Apstal
nav: Providers
network: true
overview: 'Apstal publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include analytics, web-analytics, privacy, session-replay, and heatmaps.


  The Apstal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apstal''s developer surface includes authentication, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 26 more developer resources.'
plans:
- name: Apstal Plans Pricing
  plan_count: 3
  slug: apstal-plans-pricing
random_paper: 49
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
  band: strong
  composite: 58.2
  delta: 52.3
  facets:
    commercial_clarity: 84.2
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 70.4
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 5.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
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
- analytics
- web-analytics
- privacy
- session-replay
- heatmaps
- mcp
- agent-native
- cookieless
- llms-txt
- bigquery
- gdpr
- a2a
- agent-skills
- bot-detection
- core-web-vitals
website: https://apstal.com/docs
---
