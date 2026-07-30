---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful HTTP/JSON API for Imgur covering images, albums, the public gallery, comments, accounts, tags, topics, meme generation, and notifications.
  name: Imgur API v3
  slug: imgur-api-v3
artifact_total: 49
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imgur-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://imgur.com/
- group: start
  title: ''
  type: Portal
  url: https://api.imgur.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.imgur.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imgur.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imgur.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.imgur.com/
- group: company
  title: ''
  type: Blog
  url: https://imgur.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Imgur
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/imgur
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Imgur/imgurpython
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Imgur/Hermes
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Imgur/mandible
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Imgur/incus
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Imgur/incusjs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DamienDennehy/Imgur.API
- group: design
  title: ''
  type: SpectralRules
  url: rules/imgur-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/imgur-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/imgur-context.jsonld
created: '2026-05-28'
description: Imgur is a popular image and album hosting platform whose REST API (v3) exposes the full platform — upload, retrieve, vote, comment, gallery, account, tags, topics — over HTTP/JSON. Anonymous reads/writes are supported with a Client-ID; per-user actions use OAuth2 access tokens. Commercial use is routed through RapidAPI's metered tiers.
examples:
- key_count: 2
  name: Imgur Createcomment Example
  slug: imgur-createComment-example
- key_count: 2
  name: Imgur Getaccount Example
  slug: imgur-getAccount-example
- key_count: 2
  name: Imgur Getalbum Example
  slug: imgur-getAlbum-example
- key_count: 2
  name: Imgur Getgallery Example
  slug: imgur-getGallery-example
- key_count: 2
  name: Imgur Getimage Example
  slug: imgur-getImage-example
- key_count: 2
  name: Imgur Getratelimitcredits Example
  slug: imgur-getRateLimitCredits-example
- key_count: 2
  name: Imgur Issueaccesstoken Example
  slug: imgur-issueAccessToken-example
- key_count: 2
  name: Imgur Uploadimage Example
  slug: imgur-uploadImage-example
features:
- description: Anonymous or authenticated upload via binary, base64, or remote URL.
  name: Image Upload
- description: Group images into ordered, privacy-aware collections.
  name: Albums
- description: Hot / top / user sections with sort and time windows.
  name: Public Gallery
- description: Threaded comments and up/down voting on gallery items.
  name: Comments & Voting
- description: Folksonomy tagging and editor-curated topic channels.
  name: Tags & Topics
- description: Generate memes from default templates.
  name: Meme Generation
- description: Per-user notification feed for replies, followers, and gallery events.
  name: Notifications
- description: GET /3/credits returns current client and user quota usage.
  name: Rate-Limit Introspection
finops:
- name: Imgur Finops
  service_category: ''
  slug: imgur-finops
image: https://s.imgur.com/images/favicon-152.png
integrations:
- description: Imgur grew up alongside Reddit; Reddit posts frequently embed Imgur links.
  name: Reddit
- description: Many Discord bots use Imgur for ephemeral image storage.
  name: Discord
- description: Popular Windows screenshot tool uploads directly to Imgur via Client-ID.
  name: ShareX
- description: Commercial Imgur API access is routed through RapidAPI's marketplace.
  name: RapidAPI
- description: Official and community SDKs cover Python, .NET, Swift, and Go ecosystems.
  name: imgurpython, Imgur.API, Hermes
json_schemas:
- name: Imgur OAuth2 Access Token
  property_count: 7
  slug: imgur-access-token
- name: Imgur Account
  property_count: 13
  slug: imgur-account
- name: Imgur Album
  property_count: 22
  slug: imgur-album
- name: Imgur Comment
  property_count: 16
  slug: imgur-comment
- name: Imgur Gallery Item
  property_count: 23
  slug: imgur-gallery-item
- name: Imgur Image
  property_count: 27
  slug: imgur-image
- name: Imgur Tag
  property_count: 14
  slug: imgur-tag
json_structures:
- name: Imgur Account Structure
  property_count: 0
  slug: imgur-account-structure
- name: Imgur Album Structure
  property_count: 0
  slug: imgur-album-structure
- name: Imgur Comment Structure
  property_count: 0
  slug: imgur-comment-structure
- name: Imgur Gallery Item Structure
  property_count: 0
  slug: imgur-gallery-item-structure
- name: Imgur Image Structure
  property_count: 0
  slug: imgur-image-structure
jsonld:
- class_count: 20
  name: Imgur Context
  property_count: 13
  slug: imgur-context
layout: provider
modified: '2026-05-30'
name: Imgur
nav: Providers
network: true
overview: 'Imgur publishes 1 API on the [APIs.io](https://apis.io/) network: API v3. Tagged areas include Photography, Images, Image Hosting, Albums, and Gallery.


  The Imgur catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Imgur''s developer surface includes developer portal, documentation, support, engineering blog, Stack Overflow tag, and 14 more developer resources.'
plans:
- name: Imgur Plans Pricing
  plan_count: 4
  slug: imgur-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 0
  name: Imgur Rate Limits
  slug: imgur-rate-limits
rules:
- name: Imgur API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: imgur-jsonschema-spectral-rules
- name: Imgur API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: imgur-rules
score:
  band: developing
  composite: 55.0
  delta: -4.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 74.2
    developer_ergonomics: 39.1
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 59.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imgur/refs/heads/main/screenshots/imgur-2026-06-20T183301.png
security:
- kind: domain-security
  name: Imgur Domain Security
  slug: imgur-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: imgur
solutions:
- description: Client-ID based, non-commercial use within daily/hourly quotas at $0.
  name: Free Anonymous Tier
- description: Per-user authenticated access for apps acting on behalf of an Imgur user.
  name: OAuth2 User Tier
- description: Basic / Pro / Ultra / Mega tiers on RapidAPI for commercial use cases.
  name: RapidAPI Commercial Tiers
tags:
- Photography
- Images
- Image Hosting
- Albums
- Gallery
- Social
- Memes
- Content Sharing
- Public APIs
use_cases:
- description: Apps and forums offload image hosting to Imgur's free Client-ID tier.
  name: User-Generated Content Hosting
- description: Bots and Discord/Reddit integrations upload generated images on the fly.
  name: Meme & Social Content Pipelines
- description: Desktop tools (ShareX, Greenshot) push screenshots to anonymous Imgur links.
  name: Screenshot Sharing
- description: iOS/Android apps use the iOS/Android SDKs to upload user photos.
  name: Mobile App Image Pipelines
- description: Editors fetch hot/top gallery feeds to surface trending images on third-party sites.
  name: Gallery Content Curation
website: https://imgur.com/
---
