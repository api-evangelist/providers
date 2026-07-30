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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Matrix Agentic Access
  operation_count: 20
  slug: matrix-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 20
apis:
- description: REST API used by Matrix clients to communicate with a homeserver, covering login, room creation and management, message sending, sync, device management, end-to-end encryption, and push notifications.
  name: Matrix Client-Server API
  slug: client-server-api
- description: Federation API that lets Matrix homeservers exchange events, presence, and key information with one another over signed JSON requests.
  name: Matrix Server-Server (Federation) API
  slug: server-server-api
- description: API used by application services (bridges, bots) to integrate with a homeserver, claim namespaces, and exchange events.
  name: Matrix Application Service API
  slug: application-service-api
- description: API for looking up Matrix user IDs from third-party identifiers such as email addresses and phone numbers via federated identity servers.
  name: Matrix Identity Service API
  slug: identity-service-api
- description: Push Gateway API homeservers use to deliver notifications to mobile push services on behalf of Matrix clients.
  name: Matrix Push Gateway API
  slug: push-gateway-api
- description: The Account API from Matrix — 1 operation(s) for account.
  name: Matrix Account API
  slug: matrix-account-api
- description: The Capabilities API from Matrix — 1 operation(s) for capabilities.
  name: Matrix Capabilities API
  slug: matrix-capabilities-api
- description: The CreateRoom API from Matrix — 1 operation(s) for createroom.
  name: Matrix CreateRoom API
  slug: matrix-createroom-api
- description: The Devices API from Matrix — 1 operation(s) for devices.
  name: Matrix Devices API
  slug: matrix-devices-api
- description: The Directory API from Matrix — 1 operation(s) for directory.
  name: Matrix Directory API
  slug: matrix-directory-api
- description: The Join API from Matrix — 1 operation(s) for join.
  name: Matrix Join API
  slug: matrix-join-api
- description: The Keys API from Matrix — 1 operation(s) for keys.
  name: Matrix Keys API
  slug: matrix-keys-api
- description: The Login API from Matrix — 1 operation(s) for login.
  name: Matrix Login API
  slug: matrix-login-api
- description: The Logout API from Matrix — 1 operation(s) for logout.
  name: Matrix Logout API
  slug: matrix-logout-api
- description: The Profile API from Matrix — 2 operation(s) for profile.
  name: Matrix Profile API
  slug: matrix-profile-api
- description: The PublicRooms API from Matrix — 1 operation(s) for publicrooms.
  name: Matrix PublicRooms API
  slug: matrix-publicrooms-api
- description: The Refresh API from Matrix — 1 operation(s) for refresh.
  name: Matrix Refresh API
  slug: matrix-refresh-api
- description: The Register API from Matrix — 1 operation(s) for register.
  name: Matrix Register API
  slug: matrix-register-api
- description: The Rooms API from Matrix — 4 operation(s) for rooms.
  name: Matrix Rooms API
  slug: matrix-rooms-api
- description: The Sync API from Matrix — 1 operation(s) for sync.
  name: Matrix Sync API
  slug: matrix-sync-api
artifact_total: 27
asyncapis:
- description: AsyncAPI description of the Matrix Client-Server sync mechanism. Matrix delivers real-time events to clients through the `/_matrix/client/v3/sync` endpoint, which is a long-lived HTTPS GET request (HT
  name: Matrix Client-Server Sync API
  slug: matrix-sync-asyncapi
collections:
- collection_type: open
  name: Matrix Client-Server API
  slug: open-matrix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/matrix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/matrix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matrix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matrix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matrix-org
- group: company
  title: ''
  type: Website
  url: https://matrix.org
- group: docs
  title: ''
  type: Documentation
  url: https://spec.matrix.org/latest/
- group: docs
  title: ''
  type: Specification Repository
  url: https://github.com/matrix-org/matrix-spec
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matrix-org
- group: start
  title: ''
  type: Signup
  url: https://matrix.org/try-matrix/
- group: operate
  title: ''
  type: Support
  url: https://matrix.org/support/
- group: company
  title: ''
  type: Blog
  url: https://matrix.org/blog/feed/
created: '2026-05-11'
description: Matrix is an open standard and decentralized protocol for real-time communication, providing federated messaging, voice, video, and IoT signalling across independently operated homeservers. The Matrix specification defines several REST APIs (Client-Server, Server-Server, Application Service, Identity Service, and Push Gateway) that interoperate across the federation. Authentication is typically performed via Bearer access tokens, with newer flows using OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matrix.png
layout: provider
modified: '2026-05-11'
name: Matrix
nav: Providers
network: true
overview: 'Matrix publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account API, Capabilities API, CreateRoom API, and 12 more. Tagged areas include Messaging, Decentralized, Federated, Open Standard, and Real-Time Communication.


  The Matrix catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Matrix''s developer surface includes authentication, documentation, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 5
rules:
- name: Matrix API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: matrix-asyncapi-spectral-rules
score:
  band: thin
  composite: 31.9
  delta: -5.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 59.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 5.3
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/matrix/refs/heads/main/screenshots/matrix-2026-06-20T185038.png
security:
- kind: authentication
  name: Matrix Authentication
  slug: matrix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Matrix Domain Security
  slug: matrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Matrix Vulnerability Disclosure
  slug: matrix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: matrix
tags:
- Messaging
- Decentralized
- Federated
- Open Standard
- Real-Time Communication
- VoIP
website: https://matrix.org
---
