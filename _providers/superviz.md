---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Superviz Agentic Access
  operation_count: 6
  slug: superviz-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.superviz.com
  baseurl_source: declared
  description: Realtime channels active for a room.
  name: SuperViz Channels API
  slug: superviz-channels-api
- baseURL: https://api.superviz.com
  baseurl_source: declared
  description: Contextual comments (annotations) created via the Collaboration SDK.
  name: SuperViz Comments API
  slug: superviz-comments-api
- baseURL: https://api.superviz.com
  baseurl_source: declared
  description: Video huddle / meeting statistics.
  name: SuperViz Meetings API
  slug: superviz-meetings-api
- baseURL: https://api.superviz.com
  baseurl_source: declared
  description: Participants currently connected to realtime channels.
  name: SuperViz Presence API
  slug: superviz-presence-api
- baseURL: https://api.superviz.com
  baseurl_source: declared
  description: Publishing events into realtime channels from a backend.
  name: SuperViz Realtime API
  slug: superviz-realtime-api
- baseURL: https://api.superviz.com
  baseurl_source: declared
  description: Collaboration rooms and their participants.
  name: SuperViz Rooms API
  slug: superviz-rooms-api
artifact_total: 22
asyncapis:
- description: 'AsyncAPI 2.6 description of SuperViz''s genuinely event/channel-based surfaces: 1. **Realtime channels** - SuperViz is a real-time synchronization platform. Clients using `@superviz/sdk` / `@superviz/r'
  name: SuperViz Realtime Channels & Webhooks
  slug: superviz-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SuperViz REST Channels API
  slug: open-superviz-channels-api
- collection_type: open
  name: SuperViz REST Channels Comments API
  slug: open-superviz-comments-api
- collection_type: open
  name: SuperViz REST Channels Meetings API
  slug: open-superviz-meetings-api
- collection_type: open
  name: SuperViz REST Channels Presence API
  slug: open-superviz-presence-api
- collection_type: open
  name: SuperViz REST Channels Realtime API
  slug: open-superviz-realtime-api
- collection_type: open
  name: SuperViz REST Channels Rooms API
  slug: open-superviz-rooms-api
- collection_type: open
  name: SuperViz REST API
  slug: open-superviz
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/superviz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superviz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superviz-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://superviz.com/blog
created: '2026-07-01'
description: SuperViz provides real-time collaboration and data-synchronization infrastructure for web applications - presence, realtime data channels, video huddle/meetings, contextual comments, and mouse pointers. The product is SDK-first (@superviz/sdk and @superviz/react-sdk initialized with a developer key), supported by a REST API at api.superviz.com for participants, presence, channels, rooms, comments, and meetings, an event-driven realtime channel API, and webhooks.
finops:
- name: Superviz Finops
  service_category: Developer Tools and Collaboration
  slug: superviz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superviz.png
layout: provider
modified: '2026-07-01'
name: SuperViz
nav: Providers
network: true
overview: 'SuperViz publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Comments API, Meetings API, and 3 more. Tagged areas include Real-Time, Collaboration, Presence, Synchronization, and Video.


  The SuperViz catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SuperViz''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Superviz Plans Pricing
  plan_count: 3
  slug: superviz-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Superviz Rate Limits
  slug: superviz-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: SuperViz API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: superviz-asyncapi-spectral-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 22.5
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 31.6
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superviz/refs/heads/main/screenshots/superviz-2026-08-17T082204.png
security:
- kind: authentication
  name: Superviz Authentication
  slug: superviz-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Superviz Domain Security
  slug: superviz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: superviz
tags:
- Real-Time
- Collaboration
- Presence
- Synchronization
- Video
- WebRTC
- SDK
---
