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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Shutterstock Agentic Access
  operation_count: 95
  slug: shutterstock-agentic-access
  summary_line: 95 operations · 28 acting
api_count: 10
apis:
- description: The audio API from Shutterstock — 11 operation(s) for audio.
  name: Shutterstock audio API
  slug: shutterstock-audio-api
- description: The computer_vision API from Shutterstock — 5 operation(s) for computer_vision.
  name: Shutterstock computer_vision API
  slug: shutterstock-computer-vision-api
- description: The contributors API from Shutterstock — 5 operation(s) for contributors.
  name: Shutterstock contributors API
  slug: shutterstock-contributors-api
- description: The editorial_images API from Shutterstock — 15 operation(s) for editorial_images.
  name: Shutterstock editorial_images API
  slug: shutterstock-editorial-images-api
- description: The editorial_video API from Shutterstock — 4 operation(s) for editorial_video.
  name: Shutterstock editorial_video API
  slug: shutterstock-editorial-video-api
- description: The images API from Shutterstock — 16 operation(s) for images.
  name: Shutterstock images API
  slug: shutterstock-images-api
- description: The oauth API from Shutterstock — 2 operation(s) for oauth.
  name: Shutterstock oauth API
  slug: shutterstock-oauth-api
- description: The test API from Shutterstock — 2 operation(s) for test.
  name: Shutterstock test API
  slug: shutterstock-test-api
- description: The users API from Shutterstock — 3 operation(s) for users.
  name: Shutterstock users API
  slug: shutterstock-users-api
- description: The videos API from Shutterstock — 12 operation(s) for videos.
  name: Shutterstock videos API
  slug: shutterstock-videos-api
artifact_total: 27
collections:
- collection_type: open
  name: Shutterstock API Reference
  slug: open-shutterstock
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shutterstock-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shutterstock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shutterstock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shutterstock-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shutterstock-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shutterstock
created: '2026-05-02'
description: Shutterstock is a leading global technology company providing high-quality images, videos, audio tracks, sound effects, and editorial content to businesses, individuals, and organizations worldwide. With a library of over 350 million assets, Shutterstock offers royalty-free creative content for marketing campaigns, website designs, social media, and more. The Shutterstock API provides programmatic access to search, browse, license, and download media assets, manage collections, access computer vision features, and handle OAuth 2.0 authentication. It also includes contributor profile management and user account operations.
examples:
- key_count: 4
  name: Shutterstock License Image Example
  slug: shutterstock-license-image-example
- key_count: 4
  name: Shutterstock Search Images Example
  slug: shutterstock-search-images-example
finops:
- name: Shutterstock Finops
  service_category: API
  slug: shutterstock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shutterstock.png
json_schemas:
- name: Shutterstock Image
  property_count: 13
  slug: shutterstock-image
- name: Shutterstock Video
  property_count: 15
  slug: shutterstock-video
json_structures:
- name: Shutterstock Image Structure
  property_count: 0
  slug: shutterstock-image-structure
jsonld:
- class_count: 14
  name: Shutterstock Context
  property_count: 20
  slug: shutterstock-context
layout: provider
modified: '2026-05-19'
name: Shutterstock
nav: Providers
network: true
overview: 'Shutterstock publishes 10 APIs on the [APIs.io](https://apis.io/) network, including audio API, computer_vision API, contributors API, and 7 more. Tagged areas include Images, Media, Photos, Stock Images, and Videos.


  The Shutterstock catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shutterstock''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Shutterstock Plans Pricing
  plan_count: 3
  slug: shutterstock-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Shutterstock Rate Limits
  slug: shutterstock-rate-limits
rules:
- name: Shutterstock API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shutterstock-jsonschema-spectral-rules
- name: Shutterstock API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: shutterstock-rules
scopes:
- name: Shutterstock Scopes
  scope_count: 6
  slug: shutterstock-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 51.9
  delta: 5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.3
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 46.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/shutterstock/refs/heads/main/screenshots/shutterstock-2026-06-20T193851.png
security:
- kind: authentication
  name: Shutterstock Authentication
  slug: shutterstock-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Shutterstock Domain Security
  slug: shutterstock-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Shutterstock Vulnerability Disclosure
  slug: shutterstock-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: shutterstock
tags:
- Images
- Media
- Photos
- Stock Images
- Videos
- Audio
- Licensing
- Creative Content
---
