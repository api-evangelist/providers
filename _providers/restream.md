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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Restream Agentic Access
  operation_count: 14
  slug: restream-agentic-access
  summary_line: 14 operations · 3 acting
api_count: 1
apis:
- description: 'WebSocket API for real-time streaming status updates. Connect to wss://streaming.api.restream.io/ws with an OAuth access token to receive incoming and outgoing stream events, platform status updates, '
  name: Restream Streaming Updates API
  slug: restream-streaming-updates-api
- description: 'WebSocket API for accessing and managing Restream Chat. Receive real-time chat messages from all connected streaming platforms (Twitch, YouTube, Facebook, Discord, LinkedIn, DLive) in a unified event '
  name: Restream Chat API
  slug: restream-chat-api
- baseURL: https://api.restream.io/v2
  baseurl_source: declared
  description: Channel management and configuration
  name: Restream Channels API
  slug: restream-channels-api
- baseURL: https://api.restream.io/v2
  baseurl_source: declared
  description: Live event management and scheduling
  name: Restream Events API
  slug: restream-events-api
- baseURL: https://api.restream.io/v2
  baseurl_source: declared
  description: Public platform information
  name: Restream Platforms API
  slug: restream-platforms-api
- baseURL: https://api.restream.io/v2
  baseurl_source: declared
  description: Stream key and SRT URL management
  name: Restream Stream Keys API
  slug: restream-stream-keys-api
- baseURL: https://api.restream.io/v2
  baseurl_source: declared
  description: User profile and account management
  name: Restream User API
  slug: restream-user-api
artifact_total: 38
collections:
- collection_type: postman
  name: Restream Channels API
  slug: postman-restream-channels-api
- collection_type: postman
  name: Restream Channels Events API
  slug: postman-restream-events-api
- collection_type: postman
  name: Restream Channels Platforms API
  slug: postman-restream-platforms-api
- collection_type: postman
  name: Restream Channels Stream Keys API
  slug: postman-restream-stream-keys-api
- collection_type: postman
  name: Restream Channels User API
  slug: postman-restream-user-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Restream Channels API
  slug: open-restream-channels-api
- collection_type: open
  name: Restream Channels Events API
  slug: open-restream-events-api
- collection_type: open
  name: Restream Channels Platforms API
  slug: open-restream-platforms-api
- collection_type: open
  name: Restream Channels Stream Keys API
  slug: open-restream-stream-keys-api
- collection_type: open
  name: Restream Channels User API
  slug: open-restream-user-api
- collection_type: open
  name: Restream API
  slug: open-restream
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/restream/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/restream-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/restream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/restream-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/restream-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/restreamio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://restream.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://restream.io/privacy
- group: start
  title: ''
  type: Signup
  url: https://app.restream.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.restream.io/login
- group: company
  title: ''
  type: Blog
  url: https://restream.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://restream.io/pricing
- group: company
  title: ''
  type: Website
  url: https://restream.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.restream.io
- group: auth
  title: ''
  type: Authentication
  url: https://developers.restream.io/guide/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/restreamio
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.restream.io/llms.txt
created: '2025-03-15'
description: Restream is a multistreaming platform that enables content creators and businesses to simultaneously broadcast live video to 30+ platforms including YouTube, Twitch, Facebook, LinkedIn, and more. The platform offers REST APIs and WebSocket connections for managing streams, channels, events, and chat.
examples:
- key_count: 4
  name: Restream Get Channel Example
  slug: restream-get-channel-example
- key_count: 4
  name: Restream Get Stream Key Example
  slug: restream-get-stream-key-example
- key_count: 4
  name: Restream List Platforms Example
  slug: restream-list-platforms-example
- key_count: 4
  name: Restream Refresh Token Example
  slug: restream-refresh-token-example
finops:
- name: Restream Finops
  service_category: Live Streaming
  slug: restream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/restream.png
json_schemas:
- name: Channel
  property_count: 7
  slug: restream-channel
- name: Event
  property_count: 7
  slug: restream-event
- name: Platform
  property_count: 4
  slug: restream-platform
json_structures:
- name: Restream Channel Structure
  property_count: 0
  slug: restream-channel-structure
- name: Restream Event Structure
  property_count: 0
  slug: restream-event-structure
jsonld:
- class_count: 19
  name: Restream Context
  property_count: 6
  slug: restream-context
layout: provider
modified: '2026-05-19'
name: Restream
nav: Providers
network: true
overview: 'Restream publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Events API, Platforms API, and 2 more. Tagged areas include Broadcast, Chat, Content Delivery, Live Streaming, and Multistreaming.


  The Restream catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Restream''s developer surface includes authentication, signup flow, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Restream Plans Pricing
  plan_count: 5
  slug: restream-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Restream Rate Limits
  slug: restream-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Restream API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: restream-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Restream API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: restream-rules
scopes:
- name: Restream Scopes
  scope_count: 7
  slug: restream-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 57.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 13.6
    contract_quality: 60.7
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/restream/refs/heads/main/screenshots/restream-2026-06-20T193034.png
security:
- kind: authentication
  name: Restream Authentication
  slug: restream-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Restream Domain Security
  slug: restream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: restream
tags:
- Broadcast
- Chat
- Content Delivery
- Live Streaming
- Multistreaming
- Video Streaming
website: https://restream.io
---
