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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Single-endpoint GraphQL API (queries, mutations and websocket subscriptions) for building display, control and monitoring apps on top of Soundtrack — now-playing, playback control, device pairing, sch
  name: Soundtrack API
  slug: soundtrack-api
artifact_total: 5
asyncapis:
- description: 'Event/streaming surface of the Soundtrack API, derived from the GraphQL Subscriptions root type via introspection. Clients subscribe over websocket to the single GraphQL endpoint (token supplied as a '
  name: Soundtrack API — GraphQL Subscriptions
  slug: soundtrack-your-brand-subscriptions-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundtrack-your-brand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soundtrackyourbrand.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.soundtrackyourbrand.com/v2/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.soundtrackyourbrand.com/v2/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.soundtrackyourbrand.com/v2/explore
- group: start
  title: ''
  type: GettingStarted
  url: https://api.soundtrackyourbrand.com/v2/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.soundtrackyourbrand.com/v2/docs/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soundtrack.io/
- group: company
  title: ''
  type: Blog
  url: https://www.soundtrackyourbrand.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.soundtrackyourbrand.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soundtrackyourbrand
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soundtrackyourbrand.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.soundtrackyourbrand.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.soundtrackyourbrand.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soundtrackyourbrand.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soundtrackyourbrand.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundtrack-your-brand-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soundtrack-your-brand-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/soundtrack-your-brand-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soundtrack-your-brand-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soundtrack-your-brand-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/soundtrack-your-brand-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/soundtrack-your-brand-subscriptions-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/soundtrack-your-brand-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soundtrack-your-brand-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/soundtrack-your-brand-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Soundtrack Your Brand (Soundtrack) is a Stockholm-based business music streaming company that provides licensed background music for physical spaces such as retail stores, restaurants, cafes, hotels and gyms. Its Soundtrack API is a single-endpoint GraphQL API that lets partners and customers build display, control and monitoring applications on top of Soundtrack: read what is currently playing in a sound zone, control playback, pair playback devices, and manage schedules, playlists and music libraries across accounts and locations. The API is free for paying Soundtrack customers and is complemented by a partner-gated native Player SDK for embedding Soundtrack playback in hardware.'
image: https://api.soundtrackyourbrand.com/v2/docs/img/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: soundtrack-your-brand-mcp.yml
  slug: soundtrack-your-brand-mcpyml
modified: '2026-07-21'
name: Soundtrack Your Brand
nav: Providers
network: true
overview: 'Soundtrack Your Brand publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Music Streaming, Background Music, and GraphQL.


  The Soundtrack Your Brand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Soundtrack Your Brand''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, pricing, and 20 more developer resources.'
random_paper: 68
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.0
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 49.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Soundtrack Your Brand Authentication
  slug: soundtrack-your-brand-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Soundtrack Your Brand Domain Security
  slug: soundtrack-your-brand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundtrack-your-brand
tags:
- Company
- Music
- Music Streaming
- Background Music
- GraphQL
- Retail
- Hospitality
- Audio
- API
website: https://www.soundtrackyourbrand.com
---
