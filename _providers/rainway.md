---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rainway Agentic Access
  operation_count: 2
  slug: rainway-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://hub-api.rainway.com/v0
  baseurl_source: declared
  description: Access active Rainway peers connected to the Rainway Network.
  name: Rainway Peers API
  slug: rainway-peers-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rainway Hub Peers API
  slug: open-rainway-peers-api
common:
- group: company
  title: ''
  type: Website
  url: https://docs.rainway.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rainway.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rainway.com/docs/what-is-rainway
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rainway.com/docs/api-getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rainway.com/reference/getpeers
- group: start
  title: ''
  type: SignUp
  url: https://hub.rainway.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RainwayApp
- group: operate
  title: ''
  type: StatusPage
  url: https://rainway.statuspage.io
- group: build
  title: ''
  type: Packages
  url: packages/rainway-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rainway-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rainway-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rainway-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rainway-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rainway-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rainway-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rainway-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rainway-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rainway-hub-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rainway-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rainway-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rainway-agentic-access.yml
created: '2026-07-17'
description: Rainway is a developer platform for interactive application streaming, letting you embed and run native apps anywhere in a few lines of code. Its Stream SDK is built on WebRTC and ships runtimes for the Web, React, Node.js (native), .NET and C++, handling secure peer connections, low-latency media streaming, network adaptation and input. A small RESTful Hub API exposes the active peers connected to the Rainway Network, authenticated with an API key pair, for building multi-peer architectures. Rainway originated as a consumer game-streaming app (2017; consumer app wound down in 2022) and pivoted to the Stream SDK; the docs, Hub, and published packages remain live.
image: https://avatars.githubusercontent.com/u/25223986?v=4
layout: provider
modified: '2026-07-20'
name: Rainway
nav: Providers
network: true
overview: 'Rainway publishes 1 API on the [APIs.io](https://apis.io/) network: Peers API. Tagged areas include Company, Streaming, Application Streaming, WebRTC, and Game Streaming.


  Rainway''s developer surface includes documentation, getting-started guide, API reference, signup flow, authentication, and 17 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 24.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rainway/refs/heads/main/screenshots/rainway-2026-09-02T152822.png
security:
- kind: authentication
  name: Rainway Authentication
  slug: rainway-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rainway Domain Security
  slug: rainway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: rainway
tags:
- Company
- Streaming
- Application Streaming
- WebRTC
- Game Streaming
- SDK
- Real-Time
- Developer Platform
website: https://docs.rainway.com
---
