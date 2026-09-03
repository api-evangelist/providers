---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: wss://stream.aisstream.io/v0/stream
  baseurl_source: declared
  description: Real-time global AIS vessel-tracking stream delivered over a single WebSocket at "wss://stream.aisstream.io/v0/stream". The client connects, sends a JSON subscription message (APIKey plus BoundingBoxe
  name: AISStream AIS Stream API
  slug: aisstream-ais-stream-api
artifact_total: 9
asyncapis:
- description: 'AsyncAPI 2.6 description of **AISStream.io**, a free service that streams global real-time AIS (Automatic Identification System) vessel-tracking data over a **WebSocket**. This is a real, documented, '
  name: AISStream Real-Time AIS Stream (WebSocket)
  slug: aisstream-asyncapi
collections:
- collection_type: open
  name: AISStream AIS Stream API (WebSocket)
  slug: open-aisstream
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aisstream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aisstream-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aisstream
- group: company
  title: ''
  type: Website
  url: https://aisstream.io
- group: docs
  title: ''
  type: Documentation
  url: https://aisstream.io/documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/aisstream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aisstream-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aisstream-finops.yml
created: '2026-07-12'
description: AISStream.io is a free service that streams global real-time AIS (Automatic Identification System) vessel-tracking data over a WebSocket. Clients register for a free API key, open a secure WebSocket to "wss://stream.aisstream.io/v0/stream", and send a JSON subscription message declaring one or more geographic bounding boxes plus optional MMSI and message-type filters. The server then pushes a continuous stream of AIS messages - PositionReport, ShipStaticData, and the full set of ITU-R M.1371 message types - each wrapped in an envelope carrying MessageType, MetaData, and the decoded Message. There is no REST API; the service is WebSocket-only.
finops:
- name: Aisstream Finops
  service_category: Location and Mapping
  slug: aisstream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aisstream.png
layout: provider
modified: '2026-07-12'
name: AISStream
nav: Providers
network: true
overview: 'AISStream publishes 1 API on the [APIs.io](https://apis.io/) network: AIS Stream API. Tagged areas include Vessel Tracking, AIS, Maritime, Ship Tracking, and Real-Time Data.


  The AISStream catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  AISStream''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Aisstream Plans Pricing
  plan_count: 1
  slug: aisstream-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Aisstream Rate Limits
  slug: aisstream-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: AISStream API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: aisstream-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 45.8
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 38.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aisstream/refs/heads/main/screenshots/aisstream-2026-07-25T195450.png
security:
- kind: authentication
  name: Aisstream Authentication
  slug: aisstream-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aisstream Domain Security
  slug: aisstream-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aisstream
tags:
- Vessel Tracking
- AIS
- Maritime
- Ship Tracking
- Real-Time Data
- WebSocket
- Streaming
- Ships
- Maritime Data
- Location
website: https://aisstream.io
---
