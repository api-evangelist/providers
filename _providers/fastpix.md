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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Fastpix Agentic Access
  operation_count: 42
  slug: fastpix-agentic-access
  summary_line: 42 operations · 21 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: Video views, metrics, dimensions, errors, and timeseries analytics.
  name: FastPix Data API
  slug: fastpix-data-api
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: Retrieve DRM configurations for protected playback.
  name: FastPix DRM API
  slug: fastpix-drm-api
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: AI-driven media enrichment - summaries, chapters, moderation, named entities, subtitles.
  name: FastPix In-Video AI API
  slug: fastpix-in-video-ai-api
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: Create and manage live streams and their playback.
  name: FastPix Live Streaming API
  slug: fastpix-live-streaming-api
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: Upload, import, manage, and encode video-on-demand media.
  name: FastPix On-Demand API
  slug: fastpix-on-demand-api
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: Manage playback IDs for media and live streams.
  name: FastPix Playback API
  slug: fastpix-playback-api
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: Manage keys used to sign JWTs for secure, tokenized playback.
  name: FastPix Signing Keys API
  slug: fastpix-signing-keys-api
- baseURL: https://api.fastpix.io/v1
  baseurl_source: declared
  description: Restream a live stream to third-party RTMP destinations.
  name: FastPix Simulcast API
  slug: fastpix-simulcast-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FastPix Data API
  slug: open-fastpix-data-api
- collection_type: open
  name: FastPix Data DRM API
  slug: open-fastpix-drm-api
- collection_type: open
  name: FastPix Data In-Video AI API
  slug: open-fastpix-in-video-ai-api
- collection_type: open
  name: FastPix Data Live Streaming API
  slug: open-fastpix-live-streaming-api
- collection_type: open
  name: FastPix Data On-Demand API
  slug: open-fastpix-on-demand-api
- collection_type: open
  name: FastPix Data Playback API
  slug: open-fastpix-playback-api
- collection_type: open
  name: FastPix Data Signing Keys API
  slug: open-fastpix-signing-keys-api
- collection_type: open
  name: FastPix Data Simulcast API
  slug: open-fastpix-simulcast-api
- collection_type: open
  name: FastPix API
  slug: open-fastpix
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fastpix-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fastpix-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fastpix-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fastpix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastpix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fastpix-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FastPix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fastpix
- group: company
  title: ''
  type: Website
  url: https://www.fastpix.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fastpix.io
- group: commercial
  title: ''
  type: Plans
  url: plans/fastpix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fastpix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fastpix-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fastpix.com/blog
created: '2026-07-01'
description: FastPix is a developer-first video platform offering APIs for video on-demand (upload, ingest, encoding, playback), live streaming, simulcasting, secure and DRM playback, in-video AI (transcription, summaries, chapters, moderation), and video views analytics. A Mux-style, pay-per-minute video infrastructure with a single REST API at api.fastpix.io/v1 using Basic auth.
finops:
- name: Fastpix Finops
  service_category: Media and Streaming
  slug: fastpix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fastpix.png
layout: provider
modified: '2026-07-01'
name: FastPix
nav: Providers
network: true
overview: 'FastPix publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Data API, DRM API, In-Video AI API, and 5 more. Tagged areas include Video, Streaming, Live Streaming, Video-on-Demand, and Encoding.


  FastPix''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Fastpix Plans Pricing
  plan_count: 4
  slug: fastpix-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Fastpix Rate Limits
  slug: fastpix-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.6
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fastpix/refs/heads/main/screenshots/fastpix-2026-07-25T214247.png
security:
- kind: authentication
  name: Fastpix Authentication
  slug: fastpix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fastpix Domain Security
  slug: fastpix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fastpix Vulnerability Disclosure
  slug: fastpix-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Fastpix Trust Center
  slug: fastpix-trust-center
  summary_line: ISO 27001, GDPR
slug: fastpix
tags:
- Video
- Streaming
- Live Streaming
- Video-on-Demand
- Encoding
- Playback
- Video Analytics
website: https://www.fastpix.io/
---
