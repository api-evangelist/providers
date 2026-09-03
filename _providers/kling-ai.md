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
  - '{''url'': ''https://klingai.com'', ''status'': 301, ''note'': ''declared website redirects to https://kling.ai/ — a different registrable domain (klingai.com -> kling.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Kling Ai Agentic Access
  operation_count: 17
  slug: kling-ai-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Resource-pack balance and consumption.
  name: Kling AI Account API
  slug: kling-ai-account-api
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Generate still images with the Kolors models.
  name: Kling AI Image Generation API
  slug: kling-ai-image-generation-api
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Animate images into video.
  name: Kling AI Image-to-Video API
  slug: kling-ai-image-to-video-api
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Sync a subject's lips to speech or audio.
  name: Kling AI Lip-Sync API
  slug: kling-ai-lip-sync-api
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Generate video from a text prompt.
  name: Kling AI Text-to-Video API
  slug: kling-ai-text-to-video-api
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Apply preset creative effects to images.
  name: Kling AI Video Effects API
  slug: kling-ai-video-effects-api
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Extend an existing generated video.
  name: Kling AI Video Extension API
  slug: kling-ai-video-extension-api
- baseURL: https://api.klingai.com/v1
  baseurl_source: declared
  description: Composite a garment onto a person image.
  name: Kling AI Virtual Try-On API
  slug: kling-ai-virtual-try-on-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kling AI Open Platform Account API
  slug: open-kling-ai-account-api
- collection_type: open
  name: Kling AI Open Platform Account Image Generation API
  slug: open-kling-ai-image-generation-api
- collection_type: open
  name: Kling AI Open Platform Account Image-to-Video API
  slug: open-kling-ai-image-to-video-api
- collection_type: open
  name: Kling AI Open Platform Account Lip-Sync API
  slug: open-kling-ai-lip-sync-api
- collection_type: open
  name: Kling AI Open Platform Account Text-to-Video API
  slug: open-kling-ai-text-to-video-api
- collection_type: open
  name: Kling AI Open Platform Account Video Effects API
  slug: open-kling-ai-video-effects-api
- collection_type: open
  name: Kling AI Open Platform Account Video Extension API
  slug: open-kling-ai-video-extension-api
- collection_type: open
  name: Kling AI Open Platform Account Virtual Try-On API
  slug: open-kling-ai-virtual-try-on-api
- collection_type: open
  name: Kling AI Open Platform API
  slug: open-kling-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kling-ai-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kling-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kling-ai
- group: company
  title: ''
  type: Website
  url: https://klingai.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.klingai.com/global/dev/document-api/quickStart/productIntroduction/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/kling-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kling-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kling-ai-finops.yml
created: '2026-07-11'
description: Kling AI is Kuaishou's generative video AI platform. The Kling AI Open Platform (developer API) turns text and images into video and imagery through an asynchronous create-a-task then query-the-task workflow, covering text-to-video, image-to-video, multi-image-to-video, video extension, lip-sync, video effects, image generation (Kolors), and Kolors virtual try-on. The API authenticates with a JWT signed from an Access Key / Secret Key pair and is billed against prepaid resource packs.
finops:
- name: Kling Ai Finops
  service_category: AI and Machine Learning
  slug: kling-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kling-ai.png
layout: provider
modified: '2026-07-11'
name: Kling AI
nav: Providers
network: true
overview: 'Kling AI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Image Generation API, Image-to-Video API, and 5 more. Tagged areas include Video Generation, AI Video, Generative AI, Text-to-Video, and Image-to-Video.


  Kling AI''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Kling Ai Plans Pricing
  plan_count: 3
  slug: kling-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Kling Ai Rate Limits
  slug: kling-ai-rate-limits
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kling-ai/refs/heads/main/screenshots/kling-ai-2026-07-25T223947.png
security:
- kind: authentication
  name: Kling Ai Authentication
  slug: kling-ai-authentication
  summary_line: http · 1 scheme
slug: kling-ai
tags:
- Video Generation
- AI Video
- Generative AI
- Text-to-Video
- Image-to-Video
- Artificial Intelligence
- Generative Video
- Lip Sync
- Virtual Try-On
- Image-Generation
website: https://klingai.com
---
