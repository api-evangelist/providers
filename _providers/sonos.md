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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Cloud-based REST API for controlling Sonos players and groups: playback, volume, grouping, favorites, playlists, home theater, audio clips, and cloud-queue playback sessions, with OAuth 2.0 auth and e'
  name: Sonos Control API
  slug: sonos-control-api
artifact_total: 6
asyncapis:
- description: ''
  name: Sonos Events Webhooks
  slug: sonos-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.sonos.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sonos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sonos.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sonos.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sonos.com/docs/authorize
- group: start
  title: ''
  type: SignUp
  url: https://developer.sonos.com/
- group: operate
  title: ''
  type: Support
  url: https://support.sonos.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sonos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sonos.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sonos-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sonos-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sonos-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sonos-events-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sonos-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sonos-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sonos-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sonos-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sonos-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonos-domain-security.yml
created: '2026-07-17'
description: Sonos is a consumer audio company whose wireless home-sound systems are controlled programmatically through the Sonos Control API — a cloud-based REST API that lets third-party integrations discover a household's players and groups and drive playback, volume, grouping, favorites, playlists, home theater options, audio clips, and cloud-queue sessions. The API authenticates with OAuth 2.0 (authorization code grant) using the single playback-control-all scope, is organized into per-resource namespaces (households, groups, groupVolume, playback, playbackMetadata, playbackSession, playerVolume, favorites, playlists, audioClip, homeTheater), and delivers real-time state through an event-subscription (webhook callback) model.
image: https://www.sonos.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: sonos-mcp.yml
  slug: sonos-mcpyml
modified: '2026-07-21'
name: Sonos
nav: Providers
network: true
overview: 'Sonos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Audio, Music, and Smart Home.


  The Sonos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sonos'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 15 more developer resources.'
random_paper: 16
scopes:
- name: Sonos Scopes
  scope_count: 1
  slug: sonos-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 32.0
  delta: -6.4
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 37.5
    discoverability: 79.6
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 38.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: authentication
  name: Sonos Authentication
  slug: sonos-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sonos Domain Security
  slug: sonos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonos
tags:
- Company
- Consumer
- Audio
- Music
- Smart Home
- IoT
- Streaming
- Speakers
- Home Automation
- Voice
website: https://www.sonos.com/
---
