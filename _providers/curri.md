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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 39.4
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: GraphQL API for requesting delivery quotes, booking on-demand and scheduled deliveries, managing and canceling deliveries, and tracking drivers in real time via webhooks or long polling.
  name: Curri GraphQL API
  slug: curri-graphql-api
artifact_total: 6
asyncapis:
- description: ''
  name: Curri Webhooks
  slug: curri-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.curri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.curri.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curri.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.curri.com/docs/queries-and-mutations/appendix
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.curri.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.curri.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.curri.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.curri.com/signup/create
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curri.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curri.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.curri.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.curri.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curri-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/curri-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/curri-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/curri-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curri-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curri-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curri-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curri-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/curri-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curri-domain-security.yml
created: '2026-07-17'
description: Curri is a last-mile and same-day delivery platform built for construction and industrial supplies. It lets distributors and suppliers dispatch on-demand drivers (Hotshots), run dedicated recurring fleets, and orchestrate a vetted nationwide carrier network including LTL freight — with smart vehicle matching, live tracking and ETAs, digital proof-of-delivery, and route planning. Curri's GraphQL API (https://api.curri.com/graphql) connects a customer's own systems to the platform so they can request quotes, book and manage deliveries, and track drivers in real time without logging into the app. Authentication is HTTP Basic with an issued API key plus a separate Sandbox key for test bookings.
image: https://www.curri.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: curri-mcp.yml
  slug: curri-mcpyml
modified: '2026-07-18'
name: Curri
nav: Providers
network: true
overview: 'Curri publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vertical Software, Delivery, Logistics, and Last Mile.


  The Curri catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Curri''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 41.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curri/refs/heads/main/screenshots/curri-2026-07-25T210950.png
security:
- kind: authentication
  name: Curri Authentication
  slug: curri-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Curri Domain Security
  slug: curri-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Curri Trust Center
  slug: curri-trust-center
  summary_line: trust center published
slug: curri
tags:
- Company
- Vertical Software
- Delivery
- Logistics
- Last Mile
- Freight
- Construction
- Supply Chain
- GraphQL
website: https://www.curri.com/
---
