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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Youtube Agentic Access
  operation_count: 9
  slug: google-youtube-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 8
apis:
- description: The Activities API from YouTube Data — 1 operation(s) for activities.
  name: YouTube Data Activities API
  slug: google-youtube-activities-api
- description: The Channels API from YouTube Data — 1 operation(s) for channels.
  name: YouTube Data Channels API
  slug: google-youtube-channels-api
- description: The CommentThreads API from YouTube Data — 1 operation(s) for commentthreads.
  name: YouTube Data CommentThreads API
  slug: google-youtube-commentthreads-api
- description: The PlaylistItems API from YouTube Data — 1 operation(s) for playlistitems.
  name: YouTube Data PlaylistItems API
  slug: google-youtube-playlistitems-api
- description: The Playlists API from YouTube Data — 1 operation(s) for playlists.
  name: YouTube Data Playlists API
  slug: google-youtube-playlists-api
- description: The Search API from YouTube Data — 1 operation(s) for search.
  name: YouTube Data Search API
  slug: google-youtube-search-api
- description: The Subscriptions API from YouTube Data — 1 operation(s) for subscriptions.
  name: YouTube Data Subscriptions API
  slug: google-youtube-subscriptions-api
- description: The Videos API from YouTube Data — 1 operation(s) for videos.
  name: YouTube Data Videos API
  slug: google-youtube-videos-api
artifact_total: 28
collections:
- collection_type: postman
  name: YouTube Data Activities API
  slug: postman-google-youtube-activities-api
- collection_type: postman
  name: YouTube Data Activities Channels API
  slug: postman-google-youtube-channels-api
- collection_type: postman
  name: YouTube Data Activities CommentThreads API
  slug: postman-google-youtube-commentthreads-api
- collection_type: postman
  name: YouTube Data Activities PlaylistItems API
  slug: postman-google-youtube-playlistitems-api
- collection_type: postman
  name: YouTube Data Activities Playlists API
  slug: postman-google-youtube-playlists-api
- collection_type: postman
  name: YouTube Data Activities Search API
  slug: postman-google-youtube-search-api
- collection_type: postman
  name: YouTube Data Activities Subscriptions API
  slug: postman-google-youtube-subscriptions-api
- collection_type: postman
  name: YouTube Data Activities Videos API
  slug: postman-google-youtube-videos-api
- collection_type: open
  name: YouTube Data API
  slug: open-youtube
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/youtube-data/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-youtube-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-youtube-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-youtube-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-youtube-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-youtube-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/youtube
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/youtube
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/youtube
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/youtube/v3/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/youtube/v3
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/youtube/v3/guides/auth/client-side-web-apps
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/youtube/v3/guides/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/youtube.jsonld
- group: company
  title: ''
  type: Blog
  url: https://blog.youtube/rss/
created: '2026-03-13'
description: The YouTube Data API v3 lets you incorporate YouTube functionality into your own application. You can use the API to fetch search results, manage videos, playlists, channels, subscriptions, and access activity data. It supports reading and writing YouTube data using RESTful operations with OAuth 2.0 authentication.
finops:
- name: Google Youtube Finops
  service_category: API
  slug: google-youtube-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-youtube.png
json_schemas:
- name: YouTube Video
  property_count: 7
  slug: youtube
jsonld:
- class_count: 15
  name: Youtube Context
  property_count: 4
  slug: youtube
layout: provider
modified: '2026-05-19'
name: YouTube Data
nav: Providers
network: true
overview: 'YouTube Data publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Channels API, CommentThreads API, and 5 more. Tagged areas include Channels, Google, Media, Playlists, and Search.


  The YouTube Data catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  YouTube Data''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 12 more developer resources.'
plans:
- name: Google Youtube Plans Pricing
  plan_count: 3
  slug: google-youtube-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Google Youtube Rate Limits
  slug: google-youtube-rate-limits
rules:
- name: YouTube Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-youtube-jsonschema-spectral-rules
scopes:
- name: Google Youtube Scopes
  scope_count: 3
  slug: google-youtube-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 63.1
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 70.5
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-youtube/refs/heads/main/screenshots/google-youtube-2026-06-20T182249.png
security:
- kind: authentication
  name: Google Youtube Authentication
  slug: google-youtube-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Google Youtube Domain Security
  slug: google-youtube-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Youtube Vulnerability Disclosure
  slug: google-youtube-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-youtube
tags:
- Channels
- Google
- Media
- Playlists
- Search
- Streaming
- Video
- YouTube
website: https://developers.google.com/youtube
---
