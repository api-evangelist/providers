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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Vimeo Agentic Access
  operation_count: 17
  slug: vimeo-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 1
apis:
- description: AsyncAPI 2.6 specification for Vimeo's documented webhook surface, covering the Vimeo OTT customer and subscription lifecycle topics (customer.created, customer.product.renewed, customer.tvod.created,
  name: Vimeo Webhooks
  slug: webhooks
- baseURL: https://api.vimeo.com
  baseurl_source: declared
  description: The Albums API from Vimeo — 2 operation(s) for albums.
  name: Vimeo Albums API
  slug: vimeo-albums-api
- baseURL: https://api.vimeo.com
  baseurl_source: declared
  description: The Channels API from Vimeo — 3 operation(s) for channels.
  name: Vimeo Channels API
  slug: vimeo-channels-api
- baseURL: https://api.vimeo.com
  baseurl_source: declared
  description: The Users API from Vimeo — 2 operation(s) for users.
  name: Vimeo Users API
  slug: vimeo-users-api
- baseURL: https://api.vimeo.com
  baseurl_source: declared
  description: The Videos API from Vimeo — 3 operation(s) for videos.
  name: Vimeo Videos API
  slug: vimeo-videos-api
artifact_total: 18
collections:
- collection_type: open
  name: Vimeo Albums API
  slug: open-vimeo-albums-api
- collection_type: open
  name: Vimeo Webhooks API
  slug: open-vimeo-asyncapi
- collection_type: open
  name: Vimeo Albums Channels API
  slug: open-vimeo-channels-api
- collection_type: open
  name: Vimeo Albums Users API
  slug: open-vimeo-users-api
- collection_type: open
  name: Vimeo Albums Videos API
  slug: open-vimeo-videos-api
- collection_type: open
  name: Vimeo API
  slug: open-vimeo
common:
- group: other
  href: https://artifacts.apis.io/vimeo/capabilities/vimeo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vimeo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/vimeo/agentic-access/vimeo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vimeo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/vimeo/security/vimeo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vimeo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vimeo/security/vimeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vimeo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vimeo/authentication/vimeo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vimeo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vimeo/scopes/vimeo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vimeo-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vimeo
- group: company
  title: ''
  type: Website
  url: https://vimeo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vimeo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.vimeo.com/
- group: start
  title: ''
  type: Signup
  url: https://vimeo.com/join
- group: commercial
  title: ''
  type: Pricing
  url: https://vimeo.com/upgrade
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vimeo
- group: company
  title: ''
  type: Blog
  url: https://vimeo.com/blog/feed
created: '2026-05-11'
description: Vimeo is a video hosting, creation, and streaming platform for creators, businesses, and enterprises that provides ad-free video hosting, live streaming, video editing, analytics, and OTT distribution. The Vimeo REST API enables programmatic upload, management, embedding, and analytics of videos, albums, channels, groups, and users using Bearer token (OAuth 2.0) authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vimeo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.vimeo.com over HTTP.
  name: Vimeo MCP Server
  slug: vimeo
modified: '2026-05-30'
name: Vimeo
nav: Providers
network: true
overview: 'Vimeo publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks, Albums API, Channels API, and 2 more. Tagged areas include Video, Streaming, Video Hosting, Live Streaming, and Media.


  The Vimeo catalog on APIs.io includes 1 Spectral governance ruleset.


  Vimeo''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 9 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Vimeo API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: vimeo-rules
scopes:
- name: Vimeo Scopes
  scope_count: 6
  slug: vimeo-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 53.2
    developer_ergonomics: 45.2
    discoverability: 68.3
    operational_transparency: 13.2
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vimeo/vimeo-2026-06-20T201045.png
security:
- kind: authentication
  name: Vimeo Authentication
  slug: vimeo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Vimeo Domain Security
  slug: vimeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vimeo Vulnerability Disclosure
  slug: vimeo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: vimeo
tags:
- Video
- Streaming
- Video Hosting
- Live Streaming
- Media
- OTT
website: https://vimeo.com
---
