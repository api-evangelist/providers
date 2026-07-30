---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Playlists that auto-play when Bridge starts
  name: Looking Glass Autostart API
  slug: looking-glass-autostart-api
- description: Enumerate connected Looking Glass displays
  name: Looking Glass Devices API
  slug: looking-glass-devices-api
- description: Multi-user Bridge sessions (orchestrations)
  name: Looking Glass Orchestration API
  slug: looking-glass-orchestration-api
- description: Transport controls for the Bridge media player
  name: Looking Glass Playback API
  slug: looking-glass-playback-api
- description: Create, edit and delete hologram playlists
  name: Looking Glass Playlist API
  slug: looking-glass-playlist-api
- description: Bridge and API version information
  name: Looking Glass Version API
  slug: looking-glass-version-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://lookingglassfactory.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lookingglassfactory.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lookingglassfactory.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lookingglassfactory.com/software/looking-glass-bridge-sdk/web-application-integration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Looking-Glass
- group: company
  title: ''
  type: Blog
  url: https://blog.lookingglassfactory.com
- group: commercial
  title: ''
  type: Pricing
  url: https://checkout.lookingglassfactory.com
- group: start
  title: ''
  type: SignUp
  url: https://blocks.glass
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lookingglassfactory.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lookingglassfactory.com/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/looking-glass-bridge-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/looking-glass-bridge-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/looking-glass-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/looking-glass-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/looking-glass-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/looking-glass-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/looking-glass-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/looking-glass-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/looking-glass-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/looking-glass-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/looking-glass-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/looking-glass-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://lookingglassfactory.com/product-security-policy
created: '2026-07-17'
description: 'Looking Glass Factory builds light field (holographic) displays — group-viewable 3D screens ranging from the pocket-sized Looking Glass Go to 16", 27", 32" and 65" panels — plus the software that drives them. For developers, the core surface is Looking Glass Bridge: a local runtime that exposes an HTTP REST API on http://localhost:33334/ for enumerating connected displays, opening the media player, building playlists of Quilt and RGBD holograms, and controlling playback. Around it Looking Glass ships official client libraries — the typesafe bridge.js (@lookingglass/bridge), a WebXR polyfill (@lookingglass/webxr) that targets the displays from any WebXR framework, a Python Bridge SDK, the legacy HoloPlay Core C/C++/C# SDK, and engine plugins for Unity, Unreal and Blender. Looking Glass Blocks (blocks.glass) hosts holograms on the internet. The company is backed by Uncork Capital and headquartered in Brooklyn, New York.'
image: https://lookingglassfactory.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: looking-glass-mcp.yml
  slug: looking-glass-mcpyml
modified: '2026-07-20'
name: Looking Glass
nav: Providers
network: true
overview: 'Looking Glass publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Autostart API, Devices API, Orchestration API, and 3 more. Tagged areas include Company, Holographic Displays, Light Field, 3D, and Developer Tools.


  Looking Glass'' developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 39.2
  delta: -2.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 40.7
    developer_ergonomics: 47.3
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/looking-glass/refs/heads/main/screenshots/looking-glass-2026-07-25T225514.png
security:
- kind: authentication
  name: Looking Glass Authentication
  slug: looking-glass-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Looking Glass Domain Security
  slug: looking-glass-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Looking Glass Vulnerability Disclosure
  slug: looking-glass-vulnerability-disclosure
  summary_line: contact published
slug: looking-glass
tags:
- Company
- Holographic Displays
- Light Field
- 3D
- Developer Tools
- WebXR
- Hardware
- Holograms
- Media Player
website: https://lookingglassfactory.com
---
