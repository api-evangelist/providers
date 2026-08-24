---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Qobuz Agentic Access
  operation_count: 12
  slug: qobuz-agentic-access
  summary_line: 12 operations
api_count: 6
apis:
- description: Album metadata retrieval and search
  name: Qobuz Albums API
  slug: qobuz-albums-api
- description: Artist metadata retrieval and search
  name: Qobuz Artists API
  slug: qobuz-artists-api
- description: User login and session management
  name: Qobuz Authentication API
  slug: qobuz-authentication-api
- description: Playlist retrieval and search
  name: Qobuz Playlists API
  slug: qobuz-playlists-api
- description: Cross-catalog search across all content types
  name: Qobuz Search API
  slug: qobuz-search-api
- description: Track metadata, streaming, and download URL generation
  name: Qobuz Tracks API
  slug: qobuz-tracks-api
artifact_total: 35
collections:
- collection_type: postman
  name: Qobuz Music Albums API
  slug: postman-qobuz-albums-api
- collection_type: postman
  name: Qobuz Music Albums Artists API
  slug: postman-qobuz-artists-api
- collection_type: postman
  name: Qobuz Music Albums Authentication API
  slug: postman-qobuz-authentication-api
- collection_type: postman
  name: Qobuz Music Albums Playlists API
  slug: postman-qobuz-playlists-api
- collection_type: postman
  name: Qobuz Music Albums Search API
  slug: postman-qobuz-search-api
- collection_type: postman
  name: Qobuz Music Albums Tracks API
  slug: postman-qobuz-tracks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qobuz Music Albums API
  slug: open-qobuz-albums-api
- collection_type: open
  name: Qobuz Music Albums Artists API
  slug: open-qobuz-artists-api
- collection_type: open
  name: Qobuz Music Albums Authentication API
  slug: open-qobuz-authentication-api
- collection_type: open
  name: Qobuz Music Albums Playlists API
  slug: open-qobuz-playlists-api
- collection_type: open
  name: Qobuz Music Albums Search API
  slug: open-qobuz-search-api
- collection_type: open
  name: Qobuz Music Albums Tracks API
  slug: open-qobuz-tracks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/qobuz/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qobuz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qobuz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qobuz-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.qobuz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/DJDoubleD/QobuzApiSharp
- group: commercial
  title: ''
  type: TermsOfService
  url: http://static.qobuz.com/apps/api/QobuzAPI-TermsofUse.pdf
- group: docs
  title: ''
  type: IntegrationGuidelines
  url: https://static.qobuz.com/apps/api/Qobuz-AppsGuidelines-V1.0.pdf
- group: operate
  title: ''
  type: Contact
  url: mailto:api@qobuz.com
- group: start
  title: ''
  type: Signup
  url: https://www.qobuz.com/us-en/music/streaming/offers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qobuz.com/us-en/music/streaming/offers
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qobuz.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qobuz.com/us-en/magazine
- group: company
  title: ''
  type: AppsPartners
  url: https://www.qobuz.com/us-en/discover/apps-partners
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qobuz/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Qobuz
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/qobuz
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DJDoubleD/QobuzApiSharp
- group: commercial
  title: ''
  type: Plans
  url: plans/qobuz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qobuz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qobuz-finops.yml
created: '2026-06-13'
description: Qobuz is a French hi-res audio streaming and download platform founded in 2007 and operated by Xandrie SA. It offers lossless FLAC streaming up to 24-bit/192 kHz and a hi-res download store covering over 100 million tracks across all genres. The Qobuz REST API (v0.2) is a partner-only interface that enables third-party applications — hi-fi hardware manufacturers, DAPs, music players, and streaming integrators — to search the catalog, retrieve album and artist metadata, generate authenticated streaming URLs, manage user playlists and favorites, and process purchases from the hi-res download store. API access requires contacting Qobuz directly at api@qobuz.com to obtain an app_id and app_secret. Consumer subscription plans (Studio Solo, Studio Duo, Studio Family, Sublime) provide the underlying access entitlement; partners and integrators are subject to the Qobuz API Terms of Use governed by French law. The service is deployed across France, Germany, and Canada infrastructure
  nodes monitored via a public status page.
examples:
- key_count: 34
  name: Album Get Response
  slug: album-get-response
- key_count: 25
  name: Track Get Response
  slug: track-get-response
- key_count: 8
  name: Track Getfileurl Response
  slug: track-getfileurl-response
- key_count: 2
  name: User Login Response
  slug: user-login-response
finops:
- name: Qobuz Finops
  service_category: Media and Entertainment
  slug: qobuz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qobuz.png
json_schemas:
- name: Album
  property_count: 38
  slug: album
- name: Artist
  property_count: 10
  slug: artist
- name: FileUrl
  property_count: 8
  slug: file-url
- name: Track
  property_count: 27
  slug: track
jsonld:
- class_count: 9
  name: Qobuz Context
  property_count: 45
  slug: qobuz-context
layout: provider
modified: '2026-06-13'
name: Qobuz
nav: Providers
network: true
overview: 'Qobuz publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Albums API, Artists API, Authentication API, and 3 more. Tagged areas include Music Streaming, Hi-Res Audio, FLAC, Lossless Audio, and Music Downloads.


  The Qobuz catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qobuz''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, and 14 more developer resources.'
plans:
- name: Qobuz Plans Pricing
  plan_count: 6
  slug: qobuz-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Qobuz Rate Limits
  slug: qobuz-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Qobuz API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: qobuz-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.0
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 9.8
    contract_quality: 65.0
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qobuz/refs/heads/main/screenshots/qobuz-2026-06-20T192346.png
security:
- kind: authentication
  name: Qobuz Authentication
  slug: qobuz-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Qobuz Domain Security
  slug: qobuz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qobuz
tags:
- Music Streaming
- Hi-Res Audio
- FLAC
- Lossless Audio
- Music Downloads
- Catalog Search
- Streaming URLs
- Music Metadata
- Audiophile
- France
website: https://www.qobuz.com/
---
