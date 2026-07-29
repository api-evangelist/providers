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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'Hosted GraphQL API for uploading, creating, and sharing holograms (quilt and RGBD media) on the Looking Glass Blocks platform. Authenticated via Auth0 (OAuth 2.0). Official client: @lookingglass/block'
  name: Looking Glass Blocks API
  slug: looking-glass-blocks-api
- description: Local HTTP REST API exposed by the Looking Glass Bridge desktop runtime (2.2.0+) to control the on-device media player — create playlists, insert image/video entries (quilt and RGBD), and drive playba
  name: Looking Glass Bridge REST API
  slug: looking-glass-bridge-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://lookingglassfactory.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lookingglassfactory.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lookingglassfactory.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lookingglassfactory.com/software/looking-glass-bridge-sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Looking-Glass
- group: company
  title: ''
  type: Blog
  url: https://blog.lookingglassfactory.com/
- group: operate
  title: ''
  type: Support
  url: https://lookingglassfactory.com/resources
- group: start
  title: ''
  type: SignUp
  url: https://blocks.glass
- group: build
  title: ''
  type: Packages
  url: packages/looking-glass-factory-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/looking-glass-factory-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/looking-glass-factory-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/looking-glass-factory-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/looking-glass-factory-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/looking-glass-factory-llms.txt
created: '2026-07-17'
description: 'Looking Glass Factory builds group-viewable 3D holographic (light field) displays that require no headset — the Looking Glass Go, Portrait, and the 16", 27", 32", 65" and 86" Light Field and Hololuminescent displays. Beyond hardware it ships a real developer surface: the Looking Glass Bridge runtime exposes a local HTTP REST API for driving the on-device media player, the hosted Blocks GraphQL API at blocks.glass lets apps upload and share holograms (quilt and RGBD images/videos), and official SDKs cover JavaScript/TypeScript (bridge.js, blocks.js, WebXR), Python (Bridge Python SDK), C/C++/C# (Core SDK), plus Unity and Unreal Engine plugins. It was surfaced as a portfolio company of Foundry Group and enriched from its public developer documentation, GitHub org, and package registries.'
image: https://cdn.prod.website-files.com/6287baba42d48260dec3a37a/69b0dd694c6b84f4eb5ae9da_HLD-7-image8.jpg
layout: provider
modified: '2026-07-20'
name: Looking Glass Factory
nav: Providers
network: true
overview: 'Looking Glass Factory publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Holographic Displays, 3D, and Light Field.


  Looking Glass Factory''s developer surface includes documentation, getting-started guide, engineering blog, support, signup flow, authentication, and 8 more developer resources.'
random_paper: 37
score:
  band: emerging
  composite: 21.4
  delta: -1.6
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/looking-glass-factory/refs/heads/main/screenshots/looking-glass-factory-2026-07-25T225518.png
security:
- kind: authentication
  name: Looking Glass Factory Authentication
  slug: looking-glass-factory-authentication
  summary_line: oauth2/none · 2 schemes
- kind: domain-security
  name: Looking Glass Factory Domain Security
  slug: looking-glass-factory-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: looking-glass-factory
tags:
- Company
- Hardware
- Holographic Displays
- 3D
- Light Field
- Developer Tools
- SDK
- GraphQL
- WebXR
- AR VR
website: https://lookingglassfactory.com
---
