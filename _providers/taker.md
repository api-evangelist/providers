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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Delivery-integration API connecting restaurants (Taker GO merchants) and delivery service providers (DSPs). Supports order creation, retrieval, cancellation, DSP re-routing, and asynchronous order-sta
  name: Taker GO Integration API
  slug: taker-go-integration-api
artifact_total: 5
asyncapis:
- description: ''
  name: Taker Webhooks
  slug: taker-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://taker.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.help.taker.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.help.taker.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.help.taker.io/
- group: company
  title: ''
  type: Blog
  url: https://taker.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://taker.io/blog/feed
- group: operate
  title: ''
  type: Support
  url: https://taker.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taker.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taker.io/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/taker-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taker-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/taker-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/taker-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taker-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taker-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/taker-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taker-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taker-domain-security.yml
created: '2026-07-17'
description: Taker is a Riyadh, Saudi Arabia-based restaurant technology company (founded 2018, backed by 500 Global) providing an all-in-one online ordering and restaurant-growth platform used by 1,000+ restaurants. Its product suite spans Taker Channels (branded web/mobile ordering), Taker GO (delivery operations), Taker Flow (operations optimization), Taker Grow (marketing automation), and Taker 360 (a unified dashboard across delivery aggregators). The Taker GO delivery-integration API connects restaurants and delivery service providers (DSPs) with bearer-token auth for order creation, tracking, cancellation, and asynchronous status delivery via webhooks, across published sandbox and production environments.
image: https://taker.io/wp-content/themes/taker-2026/assets/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: taker-mcp.yml
  slug: taker-mcpyml
modified: '2026-07-21'
name: Taker
nav: Providers
network: true
overview: 'Taker publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant Technology, Online Ordering, Food Delivery, and Delivery Integration.


  The Taker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Taker''s developer surface includes documentation, API reference, engineering blog, support, authentication, sandbox, and 13 more developer resources.'
random_paper: 71
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 36.8
  provenance:
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Taker Authentication
  slug: taker-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taker Domain Security
  slug: taker-domain-security
  summary_line: no transport/DNS hardening detected
slug: taker
tags:
- Company
- Restaurant Technology
- Online Ordering
- Food Delivery
- Delivery Integration
- Webhooks
- Saudi Arabia
- MENA
website: https://taker.io
---
