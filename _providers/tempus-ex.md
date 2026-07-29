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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'FusionFeed aggregates sports data and media (schedules, rosters, official and automated statistics, telemetry, scoreboard, and live/VOD video) into a single GraphQL-first API (with an interchangeable '
  name: FusionFeed
  slug: fusionfeed
artifact_total: 6
asyncapis:
- description: Live push of sports data from FusionFeed over WebSocket. Subscriptions use the graphql-ws protocol (legacy subscriptions-transport-ws is also supported). Authentication is provided in the connection-i
  name: FusionFeed Realtime (GraphQL Subscriptions)
  slug: tempus-ex-fusionfeed-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tempus-ex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tempus-ex.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tempus-ex.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tempus-ex.com/fusionfeed
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tempus-ex.com/fusionfeed/graphql/explorer-and-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tempus-ex.com/fusionfeed
- group: operate
  title: ''
  type: Support
  url: mailto:support@tempus-ex.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tempus-ex
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tempus-ex.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tempus-ex-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tempus-ex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tempus-ex-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tempus-ex-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tempus-ex-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tempus-ex-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tempus-ex-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tempus-ex-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/tempus-ex-fusionfeed-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tempus-ex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tempus-ex-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tempus Ex is a sports data and media technology company (part of Infinite Athlete) whose FusionFeed API aggregates data and media from many on-site sources into a single API for gridiron football (NFL and NCAA) and association football (soccer). FusionFeed provides schedules, game-by-game rosters, official and AI-automated statistics, low-latency X/Y telemetry for players, officials and the ball, scoreboard data, and live/VOD video (HLS and sub-second SRT) including computer-vision products such as bounding boxes, skeletal pose estimation, camera calibration and virtual FusionCams. The API is offered as a GraphQL-first interface (with WebSocket subscriptions via graphql-ws) and an interchangeable REST interface, both versioned under /v2/, with a Fusion Query Language (FQL) for powerful play/event search.
image: https://docs.tempus-ex.com/images/fusionfeed.svg
layout: provider
mcp_servers:
- description: ''
  name: tempus-ex-mcp.yml
  slug: tempus-ex-mcpyml
modified: '2026-07-21'
name: Tempus Ex
nav: Providers
network: true
overview: 'Tempus Ex publishes 1 API on the [APIs.io](https://apis.io/) network: FusionFeed. Tagged areas include Company, Sports Data, Sports, Video, and Streaming.


  The Tempus Ex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tempus Ex''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 16 more developer resources.'
random_paper: 56
rate_limits:
- limit_count: 0
  name: Tempus Ex Rate Limits
  slug: tempus-ex-rate-limits
score:
  band: thin
  composite: 38.0
  delta: 4.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.1
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 34.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tempus Ex Authentication
  slug: tempus-ex-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Tempus Ex Domain Security
  slug: tempus-ex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tempus-ex
tags:
- Company
- Sports Data
- Sports
- Video
- Streaming
- Telemetry
- GraphQL
- REST
- Media
- NFL
- Analytics
website: https://tempus-ex.com
---
