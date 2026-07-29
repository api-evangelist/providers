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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Lugg''s partner/developer REST API for embedding on-demand moving and delivery: OAuth2 authentication, quotes, bookings, multi-stop booking flows, schedules, and webhook endpoints, with a documented sa'
  name: Lugg API
  slug: lugg-api
artifact_total: 4
asyncapis:
- description: ''
  name: Lugg Webhooks Asyncapi
  slug: lugg-webhooks-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lugg.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lugg.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lugg.com
- group: company
  title: ''
  type: Website
  url: https://lugg.com
- group: company
  title: ''
  type: Blog
  url: https://lugg.com/blog
- group: auth
  title: ''
  type: Authentication
  url: authentication/lugg-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lugg-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lugg-webhooks-asyncapi.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lugg-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lugg-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lugg-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lugg-llms.txt
created: '2026-07-17'
description: 'Lugg is an on-demand moving and delivery service that connects customers with background-checked movers and trucks for same-day and scheduled jobs across 20+ U.S. metropolitan areas. Beyond consumer moves, Lugg handles furniture and appliance delivery, junk removal and donation pickups, and labor-only help, with real-time tracking and in-app payment. Lugg also publishes a partner / developer REST API (documented at docs.lugg.com, served from api.lugg.com) that lets retailers, marketplaces, and platforms embed Lugg delivery: it exposes OAuth2 authentication, quotes, bookings and multi-stop booking flows, schedules, and webhook endpoints, with a documented sandbox environment, pagination, rate limiting, and error semantics. Lugg is a Y Combinator-backed company.'
image: https://lugg.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Lugg
nav: Providers
network: true
overview: 'Lugg publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Delivery, Moving, and Last Mile.


  The Lugg catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lugg''s developer surface includes documentation, API reference, engineering blog, authentication, sandbox, and 7 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 31.3
  delta: 6.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/lugg/refs/heads/main/screenshots/lugg-2026-07-25T225649.png
security:
- kind: authentication
  name: Lugg Authentication
  slug: lugg-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lugg Domain Security
  slug: lugg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lugg
tags:
- Company
- Logistics
- Delivery
- Moving
- Last Mile
- Transportation
- On-Demand
- Webhooks
website: https://lugg.com
---
