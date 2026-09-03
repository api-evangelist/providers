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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Streamyard Agentic Access
  operation_count: 14
  slug: streamyard-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.streamyard.com
  baseurl_source: declared
  description: Manage live broadcasts and recordings. Broadcasts represent a streaming or recording session in the StreamYard studio.
  name: StreamYard Broadcasts API
  slug: streamyard-broadcasts-api
- baseURL: https://api.streamyard.com
  baseurl_source: declared
  description: Manage streaming destinations — the platforms where broadcasts are streamed or published. Supported platforms include YouTube, Facebook, LinkedIn, Twitter/X, Twitch, and custom RTMP endpoints.
  name: StreamYard Destinations API
  slug: streamyard-destinations-api
- baseURL: https://api.streamyard.com
  baseurl_source: declared
  description: Access recorded broadcasts. Once a broadcast ends, recordings become available for download.
  name: StreamYard Recordings API
  slug: streamyard-recordings-api
artifact_total: 25
collections:
- collection_type: postman
  name: StreamYard Broadcasts API
  slug: postman-streamyard-broadcasts-api
- collection_type: postman
  name: StreamYard Broadcasts Destinations API
  slug: postman-streamyard-destinations-api
- collection_type: postman
  name: StreamYard Broadcasts Recordings API
  slug: postman-streamyard-recordings-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: StreamYard Broadcasts API
  slug: open-streamyard-broadcasts-api
- collection_type: open
  name: StreamYard Broadcasts Destinations API
  slug: open-streamyard-destinations-api
- collection_type: open
  name: StreamYard Broadcasts Recordings API
  slug: open-streamyard-recordings-api
- collection_type: open
  name: StreamYard API
  slug: open-streamyard
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/streamyard/overview
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
overview: 'StreamYard publishes 3 APIs on the [APIs.io](https://apis.io/) network: Broadcasts API, Destinations API, and Recordings API. Tagged areas include Broadcasting, Live Streaming, Multistreaming, Recordings, and Video.


  The StreamYard catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StreamYard''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 16 more developer resources.'
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
- effective_rule_count: 5
  extends: []
  name: StreamYard API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: streamyard-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: StreamYard API Rules
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
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 13.6
    contract_quality: 64.6
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Multistreaming
- Recordings
- Video
website: https://streamyard.com
---
