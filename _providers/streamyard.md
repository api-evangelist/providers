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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Streamyard Agentic Access
  operation_count: 14
  slug: streamyard-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 3
apis:
- description: Manage live broadcasts and recordings. Broadcasts represent a streaming or recording session in the StreamYard studio.
  name: StreamYard Broadcasts API
  slug: streamyard-broadcasts-api
- description: Manage streaming destinations — the platforms where broadcasts are streamed or published. Supported platforms include YouTube, Facebook, LinkedIn, Twitter/X, Twitch, and custom RTMP endpoints.
  name: StreamYard Destinations API
  slug: streamyard-destinations-api
- description: Access recorded broadcasts. Once a broadcast ends, recordings become available for download.
  name: StreamYard Recordings API
  slug: streamyard-recordings-api
artifact_total: 18
collections:
- collection_type: open
  name: StreamYard API
  slug: open-streamyard
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/streamyard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamyard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/streamyard-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/streamyard-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/streamyard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/streamyard
- group: company
  title: ''
  type: Website
  url: https://streamyard.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.streamyard.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.streamyard.com/docs
- group: other
  title: ''
  type: Dashboard
  url: https://streamyard.com/dashboard
- group: start
  title: ''
  type: Signup
  url: https://streamyard.com/signup
- group: start
  title: ''
  type: Login
  url: https://streamyard.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://streamyard.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://streamyard.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://streamyard.com/resources/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://streamyard.com/resources/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.streamyard.com
- group: operate
  title: ''
  type: Support
  url: https://streamyard.com/resources/support
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/openapi/streamyard-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/json-schema/streamyard-broadcast-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/json-ld/streamyard-context.jsonld
created: '2024-01-01'
description: StreamYard is a professional live streaming and recording studio in the browser. Stream directly to multiple platforms simultaneously including YouTube, Facebook, LinkedIn, Twitch, and Twitter/X. Interview remote guests, share screens, display overlays, and manage brand assets. The StreamYard API enables programmatic management of broadcasts, destinations, and recordings.
examples:
- key_count: 2
  name: Streamyard Create Broadcast Example
  slug: streamyard-create-broadcast-example
- key_count: 2
  name: Streamyard List Broadcasts Example
  slug: streamyard-list-broadcasts-example
finops:
- name: Streamyard Finops
  service_category: API
  slug: streamyard-finops
image: https://streamyard.com/assets/images/logo.png
json_schemas:
- name: StreamYard Broadcast
  property_count: 12
  slug: streamyard-broadcast
json_structures:
- name: Streamyard Broadcast Structure
  property_count: 0
  slug: streamyard-broadcast-structure
jsonld:
- class_count: 0
  name: Streamyard Context
  property_count: 3
  slug: streamyard-context
layout: provider
modified: '2026-05-19'
name: StreamYard
nav: Providers
network: true
overview: 'StreamYard publishes 3 APIs on the [APIs.io](https://apis.io/) network: Broadcasts API, Destinations API, and Recordings API. Tagged areas include Broadcasting, Live Streaming, Multi-Streaming, Recordings, and Video.


  The StreamYard catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StreamYard''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Streamyard Plans Pricing
  plan_count: 3
  slug: streamyard-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Streamyard Rate Limits
  slug: streamyard-rate-limits
rules:
- name: StreamYard API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: streamyard-jsonschema-spectral-rules
- name: StreamYard API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 6
  slug: streamyard-rules
scopes:
- name: Streamyard Scopes
  scope_count: 3
  slug: streamyard-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 62.4
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 64.6
    developer_ergonomics: 34.8
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 62.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/streamyard/refs/heads/main/screenshots/streamyard-2026-06-20T194622.png
security:
- kind: authentication
  name: Streamyard Authentication
  slug: streamyard-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Streamyard Domain Security
  slug: streamyard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: streamyard
tags:
- Broadcasting
- Live Streaming
- Multi-Streaming
- Recordings
- Video
website: https://streamyard.com
---
