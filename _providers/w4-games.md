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
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: W4 Cloud (W4GD) is a managed multiplayer backend-as-a-service for the Godot game engine, consumed through the w4gd Godot editor addon (a GDScript SDK). It provides player authentication, a Supabase/Po
  name: W4 Cloud
  slug: w4-cloud
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.w4games.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.w4.gd/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.w4.gd/
- group: docs
  title: ''
  type: APIReference
  url: https://sdk.w4.gd/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.w4.gd/tutorials/getting_started/index.html
- group: operate
  title: ''
  type: Support
  url: https://gitlab.com/W4Games/sdk/support/-/issues
- group: company
  title: ''
  type: Blog
  url: https://www.w4games.com/blog
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/W4Games
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.w4games.com/terms
- group: start
  title: ''
  type: Login
  url: https://www.w4games.com/web/login
- group: auth
  title: ''
  type: Authentication
  url: authentication/w4-games-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/w4-games-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/w4-games-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/w4-games-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/w4-games-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/w4-games-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/w4-games-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/w4-games-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/w4-games-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/w4-games-domain-security.yml
created: '2026-07-17'
description: W4 Games is the company commercializing the open-source Godot game engine. It provides hands-on professional services (adoption, architecture, performance, production readiness), advanced console ports and mobile/XR platform work, and premium enterprise support for studios shipping with Godot. Its developer product is W4 Cloud (W4GD) — a managed multiplayer backend-as-a-service for Godot covering player authentication, a Supabase/PostgREST database accessed through the W4 Relational Mapper (W4RM) ORM, realtime, storage, matchmaking and lobbies, WebRTC, analytics, and Agones-based dedicated game-server fleets. W4 Cloud is consumed through the w4gd Godot editor addon (GDScript SDK) rather than a standalone public REST API. Backed by Lux Capital.
image: https://www.w4games.com/web/image/website/1/favicon?unique=24d32a3
layout: provider
modified: '2026-07-21'
name: W4 Games
nav: Providers
network: true
overview: 'W4 Games publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Game Development, Godot, and Multiplayer.


  W4 Games'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 13 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 28.8
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/w4-games/refs/heads/main/screenshots/w4-games-2026-09-02T170345.png
security:
- kind: authentication
  name: W4 Games Authentication
  slug: w4-games-authentication
  summary_line: apiKey/http-bearer-jwt/oauth2 · 3 schemes
- kind: domain-security
  name: W4 Games Domain Security
  slug: w4-games-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: w4-games
tags:
- Company
- Gaming
- Game Development
- Godot
- Multiplayer
- Backend-as-a-Service
- SDK
- Cloud
- Game Servers
- Real-Time
website: https://www.w4games.com
---
