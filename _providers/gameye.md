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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Gameye Agentic Access
  operation_count: 10
  slug: gameye-agentic-access
  summary_line: 10 operations · 4 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Artifacts API from Gameye — 1 operation(s) for artifacts.
  name: Gameye Artifacts API
  slug: gameye-artifacts-api
- description: The Available Location API from Gameye — 1 operation(s) for available location.
  name: Gameye Available Location API
  slug: gameye-available-location-api
- description: The Logs API from Gameye — 1 operation(s) for logs.
  name: Gameye Logs API
  slug: gameye-logs-api
- description: The Session API from Gameye — 4 operation(s) for session.
  name: Gameye Session API
  slug: gameye-session-api
- description: The Tag API from Gameye — 1 operation(s) for tag.
  name: Gameye Tag API
  slug: gameye-tag-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Pick an available region for an image, start a session, and read its host/ports.
  name: Allocate a Gameye session and get its connection address
  slug: gameye-allocate-session
- description: Start a session, register players joining, then remove players leaving.
  name: Manage the player roster on a Gameye session
  slug: gameye-player-lifecycle
- description: Pull a session's logs, terminate it, then download a diagnostic artifact.
  name: Stream logs, stop a Gameye session, and download an artifact
  slug: gameye-session-teardown
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://gameye.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gameye.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://gameye.com/docs/api-v2/
- group: docs
  title: ''
  type: APIReference
  url: https://gameye.com/docs/api-v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://gameye.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://gameye.com/docs/support/getting-support/
- group: company
  title: ''
  type: Blog
  url: https://gameye.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gameye
- group: operate
  title: ''
  type: Roadmap
  url: https://gameye.com/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://gameye.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://trial.gameye.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gameye.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gameye.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://gameye.com/status/
- group: operate
  title: ''
  type: ChangeLog
  url: https://gameye.com/docs/changelogs/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gameye-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gameye-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gameye-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gameye-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/gameye-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gameye-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gameye-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/gameye-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gameye-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gameye-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/gameye-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gameye-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gameye-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gameye-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gameye-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gameye-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gameye-allocate-session.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gameye-player-lifecycle.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/gameye-session-teardown.yml
created: '2026-07-17'
description: Gameye is a managed game server orchestration platform for multiplayer game studios, founded in 2017 in Rotterdam (Gameye B.V.). It runs dedicated, containerized game servers across bare metal, cloud, and edge providers behind a single REST API — the Session API. Studios call POST /session with a region and a Docker image; Gameye selects the best available location, starts a container in about half a second, and returns the host IP and mapped ports players connect to. Capacity-based pricing carries no egress fees, and the platform is matchmaker-agnostic (Pragma Engine, Nakama, PlayFab, FlexMatch). Gameye has orchestrated 120M+ sessions with a 99.99% uptime SLA and serves studios including Torn Banner Studios (Chivalry 2) and Remedy Entertainment.
image: https://static.gameye.com/images/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: ''
  name: gameye-mcp.yml
  slug: gameye-mcpyml
modified: '2026-07-19'
name: Gameye
nav: Providers
network: true
overview: 'Gameye publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Available Location API, Logs API, and 2 more. Tagged areas include Company, Game Server Hosting, Game Server Orchestration, Multiplayer, and Containers.


  Gameye''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 52.3
  delta: -2.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 53.7
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gameye/refs/heads/main/screenshots/gameye-2026-07-25T215424.png
security:
- kind: authentication
  name: Gameye Authentication
  slug: gameye-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gameye Domain Security
  slug: gameye-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gameye
tags:
- Company
- Game Server Hosting
- Game Server Orchestration
- Multiplayer
- Containers
- Infrastructure
- Gaming
- Edge Computing
- DevOps
website: https://gameye.com
---
