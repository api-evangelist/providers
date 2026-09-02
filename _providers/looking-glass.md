---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Looking Glass Bridge Autostart API
  slug: open-looking-glass-autostart-api
- collection_type: open
  name: Looking Glass Bridge Autostart Devices API
  slug: open-looking-glass-devices-api
- collection_type: open
  name: Looking Glass Bridge Autostart Orchestration API
  slug: open-looking-glass-orchestration-api
- collection_type: open
  name: Looking Glass Bridge Autostart Playback API
  slug: open-looking-glass-playback-api
- collection_type: open
  name: Looking Glass Bridge Autostart Playlist API
  slug: open-looking-glass-playlist-api
- collection_type: open
  name: Looking Glass Bridge Autostart Version API
  slug: open-looking-glass-version-api
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
  url: openapi/_original/looking-glass-bridge-openapi.yml
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
  name: Looking Glass MCP Server
  slug: looking-glass-mcp-server
modified: '2026-07-20'
name: Looking Glass
nav: Providers
network: true
overview: 'Looking Glass publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Autostart API, Devices API, Orchestration API, and 3 more. Tagged areas include Company, Holographic Displays, Light Field, 3D, and Developer Tools.


  Looking Glass'' developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 40.1
    developer_ergonomics: 49.4
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 37.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
