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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Vimeo Agentic Access
  operation_count: 17
  slug: vimeo-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 5
apis:
- description: AsyncAPI 2.6 specification for Vimeo's documented webhook surface, covering the Vimeo OTT customer and subscription lifecycle topics (customer.created, customer.product.renewed, customer.tvod.created,
  name: Vimeo Webhooks
  slug: webhooks
- description: The Albums API from Vimeo — 2 operation(s) for albums.
  name: Vimeo Albums API
  slug: vimeo-albums-api
- description: The Channels API from Vimeo — 3 operation(s) for channels.
  name: Vimeo Channels API
  slug: vimeo-channels-api
- description: The Users API from Vimeo — 2 operation(s) for users.
  name: Vimeo Users API
  slug: vimeo-users-api
- description: The Videos API from Vimeo — 3 operation(s) for videos.
  name: Vimeo Videos API
  slug: vimeo-videos-api
artifact_total: 13
collections:
- collection_type: open
  name: Vimeo Webhooks API
  slug: open-vimeo-asyncapi
- collection_type: open
  name: Vimeo API
  slug: open-vimeo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vimeo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vimeo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vimeo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vimeo-authentication.yml
- group: auth
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
graphqls:
- description: Vimeo is a professional video hosting platform. The API covers video upload and management, albums, showcases, channels, user management, analytics, OTT platform configuration, live streaming, caption
  name: Vimeo GraphQL API
  slug: vimeo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vimeo.png
layout: provider
modified: '2026-05-30'
name: Vimeo
nav: Providers
network: true
overview: 'Vimeo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Albums API, Channels API, and 2 more. Tagged areas include Video, Streaming, Video Hosting, Live Streaming, and Media.


  Vimeo''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 8 more developer resources.'
random_paper: 69
scopes:
- name: Vimeo Scopes
  scope_count: 6
  slug: vimeo-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 65.3
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vimeo/refs/heads/main/screenshots/vimeo-2026-06-20T201045.png
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
