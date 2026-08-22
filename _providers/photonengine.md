---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Photonengine Agentic Access
  operation_count: 8
  slug: photonengine-agentic-access
  summary_line: 8 operations · 7 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: 'The core Photon protocol - NOT a REST or JSON API. Clients connect through a Name Server to a Master Server (matchmaking/lobby) and then a Game Server (room gameplay), exchanging a proprietary binary '
  name: Photon Realtime Transport Protocol
  slug: photonengine-realtime-transport-api
- description: 'Photon Unity Networking 2, the original high-level Unity multiplayer SDK layered over the Photon Realtime transport protocol (same binary messages, same UDP/TCP/WebSocket transports). Still supported '
  name: Photon PUN (Photon Unity Networking) API
  slug: photonengine-pun-api
- description: Photon's current-generation, high-level networking framework for Unity, supporting Shared Mode, Client-Host, and dedicated Server Mode topologies with state-authoritative simulation. Runs its own tick
  name: Photon Fusion Networking API
  slug: photonengine-fusion-api
- description: Photon's deterministic, ECS-based simulation framework that ships player inputs (not state) across all clients in lockstep, re-simulating identically on every machine. Transport is the shared Photon R
  name: Photon Quantum Deterministic Simulation API
  slug: photonengine-quantum-api
- description: Cross-platform low-latency voice chat built directly on top of Photon Realtime - it inherits Realtime's matchmaking, rooms, and interest groups and streams Opus-encoded audio frames as Realtime events
  name: Photon Voice API
  slug: photonengine-voice-api
- description: A separately billed Photon Cloud service (its own AppId type) for text messaging, presence, and friend lists, dedicated Chat Servers speaking the same Photon Realtime-style binary protocol over UDP/TC
  name: Photon Chat API
  slug: photonengine-chat-api
- description: Legacy UDP-based Unity netcode product from Exit Games. No longer actively developed and not recommended for new projects - superseded by Photon Fusion. Documented here for completeness since it remai
  name: Photon Bolt (Legacy, Deprecated)
  slug: photonengine-bolt-api
- description: Endpoint Photon's server calls to validate a connecting client's credentials. You implement this; Photon is the caller.
  name: Photon Engine Custom Authentication API
  slug: photonengine-custom-authentication-api
- description: Endpoints Photon's Game Server calls (HTTP POST) at points in a room's lifecycle. You implement these; Photon is the caller.
  name: Photon Engine Room Lifecycle WebHooks API
  slug: photonengine-room-lifecycle-webhooks-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of Photon's **WebSocket transport** for the Photon Realtime binary protocol. Photon Realtime (and everything built on it - PUN, Fusion, Quantum, Voice, Chat) is **not** a JSON
  name: Photon Realtime Transport Protocol over WebSocket
  slug: photonengine-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Photon WebHooks and Webservice Contract Custom Authentication API
  slug: open-photonengine-custom-authentication-api
- collection_type: open
  name: Photon WebHooks and Webservice Contract Custom Authentication Room Lifecycle WebHooks API
  slug: open-photonengine-room-lifecycle-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/photonengine-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/photonengine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photonengine-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exitgames
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/photon-engine
- group: company
  title: ''
  type: Website
  url: https://www.photonengine.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.photonengine.com
- group: commercial
  title: ''
  type: Plans
  url: plans/photonengine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/photonengine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/photonengine-finops.yml
created: '2026-07-03'
description: Photon Engine (Exit Games) builds cross-platform multiplayer game networking backends - Photon Fusion, Photon Quantum, Photon Unity Networking (PUN), Photon Voice, Photon Chat, and the legacy Photon Bolt - all layered on the proprietary Photon Realtime transport protocol. Photon's core product is protocol-first and SDK-first, not REST-first - game clients exchange a custom binary message format (operation requests, operation responses, and events) with Name Server, Master Server, and Game Server roles, over UDP or TCP by default and, importantly, over WebSocket (ws:// unsecured, wss:// secured on port 443) as a first-class documented transport for WebGL and browser-hosted clients. Photon's own hosted surface exposes no general-purpose callable REST API for gameplay; the only genuinely HTTP surfaces are outbound - Room Lifecycle WebHooks (Photon POSTs room/join/leave/event/property/close notifications to a developer-hosted URL) and the Custom Authentication webservice contract
  (Photon calls out to a developer-hosted HTTP(S) endpoint to validate client tokens before allowing a connection). Pricing and account management are handled through the Photon Cloud Dashboard web UI, not a documented public REST API.
finops:
- name: Photonengine Finops
  service_category: Gaming and Multiplayer Networking
  slug: photonengine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/photonengine.png
layout: provider
modified: '2026-07-03'
name: Photon Engine
nav: Providers
network: true
overview: 'Photon Engine publishes 3 APIs on the [APIs.io](https://apis.io/) network: Photon Realtime Transport Protocol, Custom Authentication API, and Room Lifecycle WebHooks API. Tagged areas include Gaming, Multiplayer, Realtime, Netcode, and Game Networking.


  The Photon Engine catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Photon Engine''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Photonengine Plans Pricing
  plan_count: 6
  slug: photonengine-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Photonengine Rate Limits
  slug: photonengine-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Photon Engine API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: photonengine-asyncapi-spectral-rules
score:
  band: thin
  composite: 35.3
  delta: -7.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 55.6
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/photonengine/refs/heads/main/screenshots/photonengine-2026-08-17T081233.png
security:
- kind: domain-security
  name: Photonengine Domain Security
  slug: photonengine-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Photonengine Vulnerability Disclosure
  slug: photonengine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: photonengine
tags:
- Gaming
- Multiplayer
- Realtime
- Netcode
- Game Networking
- WebSocket
- Binary Protocol
website: https://www.photonengine.com
---
