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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Soundtrack's public GraphQL API for building display, control and monitoring apps on top of the Soundtrack business music service. Query now-playing and schedule state, control playback on sound zones
  name: Soundtrack API
  slug: soundtrack-api
artifact_total: 5
asyncapis:
- description: Real-time event surface of the Soundtrack GraphQL API, delivered via GraphQL subscriptions over WebSocket. Derived from live introspection of https://api.soundtrackyourbrand.com/v2 (13 subscription fi
  name: Soundtrack API — Real-time Subscriptions
  slug: soundtrackyourbrand-subscriptions-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundtrackyourbrand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soundtrack.io/
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
  url: https://api.soundtrackyourbrand.com/v2/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.soundtrackyourbrand.com/v2/docs/the-basics
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soundtrack.io/
- group: operate
  title: ''
  type: Support
  url: https://help.soundtrack.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soundtrackyourbrand
- group: start
  title: ''
  type: SignUp
  url: https://app.soundtrack.io/signup/
- group: start
  title: ''
  type: Login
  url: https://app.soundtrack.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soundtrack.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soundtrack.io/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soundtrack.io/legal/
- group: company
  title: ''
  type: Blog
  url: https://www.soundtrack.io/blog/
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundtrackyourbrand-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/soundtrackyourbrand-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soundtrackyourbrand-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/soundtrackyourbrand-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/soundtrackyourbrand-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soundtrackyourbrand-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/soundtrackyourbrand-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soundtrackyourbrand-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/soundtrackyourbrand-subscriptions-asyncapi.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/soundtrackyourbrand-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/soundtrackyourbrand-mcp.yml
created: '2026-07-17'
description: Soundtrack Your Brand (now branded simply "Soundtrack", soundtrack.io) is a business music streaming service that provides licensed background music for physical spaces such as retail stores, restaurants, cafes, hotels and gyms. Originally spun out of Spotify, the company curates and schedules music across a customer's locations and sound zones, and exposes a public GraphQL API (api.soundtrackyourbrand.com/v2) that lets developers build display, control and monitoring apps on top of Soundtrack — reading now-playing state, controlling playback (play/pause/skip/volume) on sound zones, managing playlists, schedules and music libraries, and subscribing to real-time updates. The API is free for paying Soundtrack customers and authenticates with an API token. Surfaced originally as a portfolio company of Balderton Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundtrackyourbrand.png
layout: provider
mcp_servers:
- description: ''
  name: Soundtrack Your Brand MCP Server
  slug: soundtrack-your-brand-mcp-server
modified: '2026-07-21'
name: Soundtrack Your Brand
nav: Providers
network: true
overview: 'Soundtrack Your Brand publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Streaming, Business Music, and Media.


  The Soundtrack Your Brand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Soundtrack Your Brand''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, engineering blog, and 19 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 37.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soundtrackyourbrand/refs/heads/main/screenshots/soundtrackyourbrand-2026-08-17T082007.png
security:
- kind: authentication
  name: Soundtrackyourbrand Authentication
  slug: soundtrackyourbrand-authentication
  summary_line: http-bearer/token · 1 scheme
- kind: domain-security
  name: Soundtrackyourbrand Domain Security
  slug: soundtrackyourbrand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundtrackyourbrand
tags:
- Company
- Music
- Streaming
- Business Music
- Media
- Entertainment
- GraphQL
- Playback Control
- Retail
website: https://www.soundtrack.io/
---
