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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Captions Ai Agentic Access
  operation_count: 15
  slug: captions-ai-agentic-access
  summary_line: 15 operations · 9 acting
api_count: 6
apis:
- description: Generate UGC-style AI advertising videos using AI creators
  name: Captions AI Ads API
  slug: captions-ai-ai-ads-api
- description: Generate talking-head videos using community AI avatars or AI Twins
  name: Captions AI Creator API
  slug: captions-ai-ai-creator-api
- description: Text-to-speech audio generation
  name: Captions Audio API
  slug: captions-ai-audio-api
- description: Render static text overlays onto videos
  name: Captions Meta Text Overlays API
  slug: captions-ai-meta-text-overlays-api
- description: Add AI captions to videos and manage caption templates
  name: Captions Video Captions API
  slug: captions-ai-video-captions-api
- description: Create and list AI-generated videos
  name: Captions Videos API
  slug: captions-ai-videos-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/captions-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/captions-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/captions-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://captions.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://captions.ai/help/docs/api/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mirage-ai-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/captionsapp
- group: other
  title: ''
  type: X
  url: https://x.com/getcaptionsapp
- group: company
  title: ''
  type: Blog
  url: https://captions.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://captions.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://captions.ai/help/whats-new
- group: commercial
  title: ''
  type: Plans
  url: plans/captions-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/captions-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/captions-ai-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/captions-ai-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/captions-ai-context.jsonld
created: '2026-06-12'
description: Captions is an AI-powered video creation and editing platform developed by Mirage, a New York-based AI research and product company. The platform enables creators and businesses to generate, edit, caption, dub, and translate talking-head videos at scale using generative AI. The Captions API — served under the Mirage API umbrella — exposes capabilities for automated video captioning, AI Creator video generation (using community avatars or personal AI Twins), AI Ads video generation, and bulk video management, all authenticated via API key and billed on a per-second-of-video credit model. Captions supports output in 30+ languages with automatic language detection, lip-sync dubbing, and direct publishing integrations for TikTok, Instagram, and YouTube.
examples:
- key_count: 5
  name: Captions Ai Add Captions Example
  slug: captions-ai-add-captions-example
- key_count: 6
  name: Captions Ai Creator Submit Example
  slug: captions-ai-creator-submit-example
- key_count: 6
  name: Captions Ai Generate Video Example
  slug: captions-ai-generate-video-example
finops:
- name: Captions Ai Finops
  service_category: ''
  slug: captions-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/captions-ai.png
json_schemas:
- name: MACaptionTemplate
  property_count: 5
  slug: captions-ai-caption-template
- name: CreatorJobPollResponse
  property_count: 4
  slug: captions-ai-creator-job
- name: MAVideo
  property_count: 12
  slug: captions-ai-video
jsonld:
- class_count: 3
  name: Captions Ai Context
  property_count: 31
  slug: captions-ai-context
layout: provider
modified: '2026-06-12'
name: Captions
nav: Providers
network: true
overview: 'Captions publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Ads API, AI Creator API, Audio API, and 3 more. Tagged areas include AI Video, Video Generation, Video Captioning, AI Dubbing, and Lip Sync.


  The Captions catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Captions'' developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 11 more developer resources.'
plans:
- name: Captions Ai Plans Pricing
  plan_count: 6
  slug: captions-ai-plans-pricing
random_paper: 95
rate_limits:
- limit_count: 6
  name: Captions Ai Rate Limits
  slug: captions-ai-rate-limits
rules:
- name: Captions API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: captions-ai-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/captions-ai/refs/heads/main/screenshots/captions-ai-2026-06-20T173943.png
security:
- kind: authentication
  name: Captions Ai Authentication
  slug: captions-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Captions Ai Domain Security
  slug: captions-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: captions-ai
tags:
- AI Video
- Video Generation
- Video Captioning
- AI Dubbing
- Lip Sync
- AI Twin
- Text to Video
- Generative AI
- Video Translation
website: https://captions.ai/
---
