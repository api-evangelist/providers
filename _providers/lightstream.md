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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 30
  human_in_the_loop: 2
  name: Lightstream Agentic Access
  operation_count: 45
  slug: lightstream-agentic-access
  summary_line: 45 operations · 30 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: The Authentication Service provides token services for clients
  name: Lightstream AuthenticationService API
  slug: lightstream-authenticationservice-api
- description: The Backend Authentication Service provides token services for partner backend systems
  name: Lightstream BackendAuthenticationService API
  slug: lightstream-backendauthenticationservice-api
- description: The Collection Service operates on collections, which contain projects and collection live sources used in projects.
  name: Lightstream CollectionService API
  slug: lightstream-collectionservice-api
- description: The Destination Service operates on Project Destinations. Destinations designate where a Broadcast associated with a Project is distributed downstream.
  name: Lightstream DestinationService API
  slug: lightstream-destinationservice-api
- description: The event API provides a mechanism for you to subscribe and publish events between your backend services and the composition, as well as receive events from the live and layout api.
  name: Lightstream EventService API
  slug: lightstream-eventservice-api
- description: Layers
  name: Lightstream LayerService API
  slug: lightstream-layerservice-api
- description: Layouts
  name: Lightstream LayoutService API
  slug: lightstream-layoutservice-api
- description: The Project Service operates on a Project.
  name: Lightstream ProjectService API
  slug: lightstream-projectservice-api
- description: The Public Authentication Service provides token verification services
  name: Lightstream PublicAuthenticationService API
  slug: lightstream-publicauthenticationservice-api
- description: The Source Service operates on Collection Live Sources and Project Sources.
  name: Lightstream SourceService API
  slug: lightstream-sourceservice-api
artifact_total: 26
asyncapis:
- description: Event-driven view of the API.stream Event API. The Event API provides a bidirectional publish/subscribe channel between a partner's backend services, the compositor and connected clients, and also car
  name: API.stream Event API
  slug: lightstream-event-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Event AuthenticationService API
  slug: open-lightstream-authenticationservice-api
- collection_type: open
  name: Event AuthenticationService BackendAuthenticationService API
  slug: open-lightstream-backendauthenticationservice-api
- collection_type: open
  name: Event AuthenticationService CollectionService API
  slug: open-lightstream-collectionservice-api
- collection_type: open
  name: Event AuthenticationService DestinationService API
  slug: open-lightstream-destinationservice-api
- collection_type: open
  name: Event AuthenticationService EventService API
  slug: open-lightstream-eventservice-api
- collection_type: open
  name: Event AuthenticationService LayerService API
  slug: open-lightstream-layerservice-api
- collection_type: open
  name: Event AuthenticationService LayoutService API
  slug: open-lightstream-layoutservice-api
- collection_type: open
  name: Event AuthenticationService ProjectService API
  slug: open-lightstream-projectservice-api
- collection_type: open
  name: Event AuthenticationService PublicAuthenticationService API
  slug: open-lightstream-publicauthenticationservice-api
- collection_type: open
  name: Event AuthenticationService SourceService API
  slug: open-lightstream-sourceservice-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lightstream-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lightstream-event-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightstream-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://golightstream.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.api.stream/
- group: docs
  title: ''
  type: Documentation
  url: https://www.api.stream/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.api.stream/docs/api/live/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.api.stream/docs/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightstream-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightstream-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/lightstream-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/golightstream
- group: operate
  title: ''
  type: Support
  url: https://golightstream.com/support/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/lightstream
- group: company
  title: ''
  type: Blog
  url: https://golightstream.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.stream/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightstream-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://golightstream.com/studio/#plans
- group: start
  title: ''
  type: SignUp
  url: https://studio.golightstream.com/welcome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.stream/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.stream/privacy-policy/
- group: design
  title: ''
  type: Conventions
  url: conventions/lightstream-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightstream-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightstream-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightstream-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightstream-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightstream-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightstream-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/lightstream-examples.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/lightstream-event-asyncapi.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lightstream-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/lightstream-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lightstream-changelog.yml
created: '2026-07-17'
description: 'Lightstream (Infiniscene, Inc.) is a Techstars-backed live video company best known for Lightstream Studio, a browser-based streaming studio used by creators to broadcast to Twitch, YouTube and other destinations without installing desktop encoding software. Lightstream also operates API.stream, its developer platform, which exposes the same cloud video pipeline to development partners as three API-first services: a Live API for managing collections, projects, sources, destinations and broadcasts; a Layout API for building and animating layered scene compositions; and an Event API for publishing and subscribing to real-time events across collaborators, guests and renderers. All three services are defined as gRPC Protobuf contracts and fronted by gRPC-Web and REST gateways, secured with a JWT access-token model and role-based permissions (HOST, COHOST, CONTRIBUTOR, GUEST, VIEWER), with first-party JavaScript/TypeScript SDKs and a Studio Kit for embedding a full studio experience.'
image: https://raw.githubusercontent.com/golightstream/api.stream-sdk/main/build/logo-dark.png
layout: provider
mcp_servers:
- description: ''
  name: Lightstream MCP Server
  slug: lightstream-mcp-server
modified: '2026-07-19'
name: Lightstream
nav: Providers
network: true
overview: 'Lightstream publishes 10 APIs on the [APIs.io](https://apis.io/) network, including AuthenticationService API, BackendAuthenticationService API, CollectionService API, and 7 more. Tagged areas include Company, Video, Live Streaming, Broadcasting, and WebRTC.


  The Lightstream catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lightstream''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 27 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 24
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 62.2
    developer_ergonomics: 68.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightstream/refs/heads/main/screenshots/lightstream-2026-07-25T225138.png
security:
- kind: authentication
  name: Lightstream Authentication
  slug: lightstream-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lightstream Domain Security
  slug: lightstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightstream
tags:
- Company
- Video
- Live Streaming
- Broadcasting
- WebRTC
- RTMP
- Media
- Compositing
- Real-Time
- Event
- gRPC
- Creator Tools
website: https://golightstream.com/
---
