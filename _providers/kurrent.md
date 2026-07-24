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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
api_count: 9
apis:
- description: 'The primary protocol for KurrentDB. The published protocol buffer definitions cover the v2 streams service (multi-stream appends, reads), the schema registry service, the secondary index service, and '
  name: KurrentDB gRPC API
  slug: kurrentdb-grpc-api
- description: Node administration operations
  name: Kurrent Admin API
  slug: kurrent-admin-api
- description: Cluster gossip
  name: Kurrent Gossip API
  slug: kurrent-gossip-api
- description: Node information and configuration
  name: Kurrent Info API
  slug: kurrent-info-api
- description: Create, manage and query projections
  name: Kurrent Projections API
  slug: kurrent-projections-api
- description: Node statistics
  name: Kurrent Statistics API
  slug: kurrent-statistics-api
- description: Append to, read from and manage event streams
  name: Kurrent Streams API
  slug: kurrent-streams-api
- description: Persistent (competing consumer) subscription management and consumption
  name: Kurrent Subscriptions API
  slug: kurrent-subscriptions-api
- description: User account management
  name: Kurrent Users API
  slug: kurrent-users-api
artifact_total: 15
asyncapis:
- description: ''
  name: Kurrent Connectors Webhooks
  slug: kurrent-connectors-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kurrent.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kurrent.io/dev-center/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kurrent.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kurrent.io/server/v26.1/http-api/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kurrent.io/getting-started/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://eventstore.freshdesk.com/support/login
- group: operate
  title: ''
  type: HelpCenter
  url: https://discuss.kurrent.io/
- group: company
  title: ''
  type: Blog
  url: https://www.kurrent.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.kurrent.io/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kurrent-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kurrent.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://identity.eventstore.com/login
- group: start
  title: ''
  type: Login
  url: https://console.kurrent.cloud/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kurrent.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kurrent.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eventstore.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.kurrent.io/releases
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/Phn9pmCw3t
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Kurrent_io
- group: learn
  title: ''
  type: Training
  url: https://academy.kurrent.io
- group: build
  title: ''
  type: Packages
  url: packages/kurrent-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kurrent-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kurrent-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kurrent-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kurrent-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kurrent-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kurrent-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kurrent-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kurrent-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kurrent-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kurrent-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kurrent-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kurrent-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kurrent-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kurrent-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/kurrent-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kurrent-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kurrent-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kurrent-connectors-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.kurrent.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/kurrent-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kurrent-domain-security.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/kurrent-streams.proto
- group: other
  title: ''
  type: Overlay
  url: overlays/kurrent-kurrentdb-http-api-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/kurrent-kurrentdb-http-api-openapi.yml
created: '2026-07-17'
description: Kurrent — formerly Event Store Ltd — builds KurrentDB, an event-native database purpose-built to store, process and deliver application state changes as an immutable, append-only log of events. Where a traditional CRUD database overwrites rows and discards the history that produced them, KurrentDB retains every state change as a first-class event, giving applications a complete audit trail, temporal queries and the ability to replay history to rebuild state or seed new read models. The product line spans KurrentDB (open-source and commercial, self-hosted), Kurrent Cloud (managed clusters on AWS, Azure and Google Cloud), Kurrent Enterprise, and Capacitor, a shared memory layer for agentic coding. Developers integrate over a primary gRPC protocol with official client SDKs for .NET, Java, Node.js, Python, Go and Rust, or over the native AtomPub-style HTTP API. Connectors move events in and out of Kafka, MongoDB, Elasticsearch, RabbitMQ, Pulsar, SQL and HTTP endpoints. KurrentDB
  is widely used for event sourcing, CQRS, event-driven microservices, change data capture and, increasingly, as durable memory for AI agents.
image: https://www.kurrent.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: kurrent-mcp.yml
  slug: kurrent-mcpyml
modified: '2026-07-19'
name: Kurrent
nav: Providers
network: true
overview: 'Kurrent publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Gossip API, Info API, and 5 more. Tagged areas include Company, Database, Event Sourcing, Event Streaming, and Event Driven Architecture.


  The Kurrent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kurrent''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
random_paper: 14
scopes:
- name: Kurrent Scopes
  scope_count: 14
  slug: kurrent-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: strong
  composite: 61.1
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 65.5
    developer_ergonomics: 87.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 61.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Kurrent Authentication
  slug: kurrent-authentication
  summary_line: http/mutualTLS/openIdConnect · 3 schemes
- kind: domain-security
  name: Kurrent Domain Security
  slug: kurrent-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Kurrent Trust Center
  slug: kurrent-trust-center
  summary_line: trust center published
slug: kurrent
tags:
- Company
- Database
- Event Sourcing
- Event Streaming
- Event Driven Architecture
- CQRS
- Data Infrastructure
- Developer Tools
- Cloud
- Open Source
- gRPC
- Agentic AI
website: https://www.kurrent.io/
---
