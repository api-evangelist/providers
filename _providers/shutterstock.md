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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Shutterstock Agentic Access
  operation_count: 95
  slug: shutterstock-agentic-access
  summary_line: 95 operations · 28 acting
api_count: 1
apis:
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The audio API from Shutterstock — 11 operation(s) for audio.
  name: Shutterstock audio API
  slug: shutterstock-audio-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The computer_vision API from Shutterstock — 5 operation(s) for computer_vision.
  name: Shutterstock computer_vision API
  slug: shutterstock-computer-vision-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The contributors API from Shutterstock — 5 operation(s) for contributors.
  name: Shutterstock contributors API
  slug: shutterstock-contributors-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The editorial_images API from Shutterstock — 15 operation(s) for editorial_images.
  name: Shutterstock editorial_images API
  slug: shutterstock-editorial-images-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The editorial_video API from Shutterstock — 4 operation(s) for editorial_video.
  name: Shutterstock editorial_video API
  slug: shutterstock-editorial-video-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The images API from Shutterstock — 16 operation(s) for images.
  name: Shutterstock images API
  slug: shutterstock-images-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The oauth API from Shutterstock — 2 operation(s) for oauth.
  name: Shutterstock oauth API
  slug: shutterstock-oauth-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The test API from Shutterstock — 2 operation(s) for test.
  name: Shutterstock test API
  slug: shutterstock-test-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The users API from Shutterstock — 3 operation(s) for users.
  name: Shutterstock users API
  slug: shutterstock-users-api
- baseURL: https://api.shutterstock.com
  baseurl_source: declared
  description: The videos API from Shutterstock — 12 operation(s) for videos.
  name: Shutterstock videos API
  slug: shutterstock-videos-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shutterstock API Reference audio API
  slug: open-shutterstock-audio-api
- collection_type: open
  name: Shutterstock API Reference audio computer_vision API
  slug: open-shutterstock-computer-vision-api
- collection_type: open
  name: Shutterstock API Reference audio contributors API
  slug: open-shutterstock-contributors-api
- collection_type: open
  name: Shutterstock API Reference audio editorial_images API
  slug: open-shutterstock-editorial-images-api
- collection_type: open
  name: Shutterstock API Reference audio editorial_video API
  slug: open-shutterstock-editorial-video-api
- collection_type: open
  name: Shutterstock API Reference audio images API
  slug: open-shutterstock-images-api
- collection_type: open
  name: Shutterstock API Reference audio oauth API
  slug: open-shutterstock-oauth-api
- collection_type: open
  name: Shutterstock API Reference audio test API
  slug: open-shutterstock-test-api
- collection_type: open
  name: Shutterstock API Reference audio users API
  slug: open-shutterstock-users-api
- collection_type: open
  name: Shutterstock API Reference audio videos API
  slug: open-shutterstock-videos-api
- collection_type: open
  name: Shutterstock API Reference
  slug: open-shutterstock
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shutterstock-capability-edges.yml
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
overview: 'Shutterstock publishes 10 APIs on the [APIs.io](https://apis.io/) network, including audio API, computer_vision API, contributors API, and 7 more. Tagged areas include Image, Media, Photos, Stock Images, and Videos.


  The Shutterstock catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shutterstock''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Shutterstock Plans Pricing
  plan_count: 3
  slug: shutterstock-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Shutterstock Rate Limits
  slug: shutterstock-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Shutterstock API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shutterstock-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Shutterstock API Rules
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
  composite: 43.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 75.6
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Image
- Media
- Photos
- Stock Images
- Videos
- Audio
- Licensing
- Creative Content
---
