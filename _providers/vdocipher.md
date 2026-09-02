---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Vdocipher Agentic Access
  operation_count: 12
  slug: vdocipher-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: Create, list, and search folders.
  name: VdoCipher Folders API
  slug: vdocipher-folders-api
- description: Video metadata, files, posters, and captions.
  name: VdoCipher Meta API
  slug: vdocipher-meta-api
- description: Generate OTP and playbackInfo for authorized playback.
  name: VdoCipher Playback API
  slug: vdocipher-playback-api
- description: List and search video tags.
  name: VdoCipher Tags API
  slug: vdocipher-tags-api
- description: Obtain upload credentials and check transcoding status.
  name: VdoCipher Upload API
  slug: vdocipher-upload-api
- description: List, search, retrieve, edit, and delete videos.
  name: VdoCipher Videos API
  slug: vdocipher-videos-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VdoCipher Server Folders API
  slug: open-vdocipher-folders-api
- collection_type: open
  name: VdoCipher Server Folders Meta API
  slug: open-vdocipher-meta-api
- collection_type: open
  name: VdoCipher Server Folders Playback API
  slug: open-vdocipher-playback-api
- collection_type: open
  name: VdoCipher Server Folders Tags API
  slug: open-vdocipher-tags-api
- collection_type: open
  name: VdoCipher Server Folders Upload API
  slug: open-vdocipher-upload-api
- collection_type: open
  name: VdoCipher Server Folders Videos API
  slug: open-vdocipher-videos-api
- collection_type: open
  name: VdoCipher Server API
  slug: open-vdocipher
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vdocipher-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vdocipher-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vdocipher-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VdoCipher
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vdocipher
- group: company
  title: ''
  type: Website
  url: https://www.vdocipher.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.vdocipher.com/docs/server/
- group: commercial
  title: ''
  type: Plans
  url: plans/vdocipher-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vdocipher-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vdocipher-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.vdocipher.com/blog/feed/
created: '2026-07-01'
description: VdoCipher is a secure video hosting platform that delivers Hollywood-grade DRM (Google Widevine and Apple FairPlay) encrypted streaming for e-learning and OTT businesses. Its server-side REST API handles video upload, media management, folders, dynamic viewer watermarking, and OTP/playbackInfo generation for authorized playback, all secured with an Apisecret authorization header.
finops:
- name: Vdocipher Finops
  service_category: Media and Content Delivery
  slug: vdocipher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vdocipher.png
layout: provider
modified: '2026-07-01'
name: VdoCipher
nav: Providers
network: true
overview: 'VdoCipher publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Folders API, Meta API, Playback API, and 3 more. Tagged areas include Video, Secure Video Hosting, DRM, Streaming, and E-Learning.


  VdoCipher''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Vdocipher Plans Pricing
  plan_count: 4
  slug: vdocipher-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Vdocipher Rate Limits
  slug: vdocipher-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Vdocipher Authentication
  slug: vdocipher-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vdocipher Domain Security
  slug: vdocipher-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vdocipher
tags:
- Video
- Secure Video Hosting
- DRM
- Streaming
- E-Learning
- OTT
- Watermarking
website: https://www.vdocipher.com/
---
