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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Creatify Agentic Access
  operation_count: 31
  slug: creatify-agentic-access
  summary_line: 31 operations · 13 acting
api_count: 10
apis:
- description: Lipsync v1/v2 and Aurora avatar video generation.
  name: Creatify AI Avatar API
  slug: creatify-ai-avatar-api
- description: Enhance and stylize existing videos (modeled).
  name: Creatify AI Editing API
  slug: creatify-ai-editing-api
- description: Convert a text script into a short-form video (deprecated).
  name: Creatify AI Shorts API
  slug: creatify-ai-shorts-api
- description: Generate videos from customizable templates (modeled).
  name: Creatify Custom Templates API
  slug: creatify-custom-templates-api
- description: Turn a URL into a short-form video ad.
  name: Creatify Link-to-Video API
  slug: creatify-link-to-video-api
- description: Background-music categories and tracks (modeled).
  name: Creatify Music API
  slug: creatify-music-api
- description: Catalog of 1500+ AI avatars/personas.
  name: Creatify Personas API
  slug: creatify-personas-api
- description: Generate video ads from product images (modeled).
  name: Creatify Product-to-Video API
  slug: creatify-product-to-video-api
- description: Generate voiceovers from text.
  name: Creatify Text-to-Speech API
  slug: creatify-text-to-speech-api
- description: Catalog of AI voices and accents.
  name: Creatify Voices API
  slug: creatify-voices-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Creatify AI Avatar API
  slug: open-creatify-ai-avatar-api
- collection_type: open
  name: Creatify AI Avatar AI Editing API
  slug: open-creatify-ai-editing-api
- collection_type: open
  name: Creatify AI Avatar AI Shorts API
  slug: open-creatify-ai-shorts-api
- collection_type: open
  name: Creatify AI Avatar Custom Templates API
  slug: open-creatify-custom-templates-api
- collection_type: open
  name: Creatify AI Avatar Link-to-Video API
  slug: open-creatify-link-to-video-api
- collection_type: open
  name: Creatify AI Avatar Music API
  slug: open-creatify-music-api
- collection_type: open
  name: Creatify AI Avatar Personas API
  slug: open-creatify-personas-api
- collection_type: open
  name: Creatify AI Avatar Product-to-Video API
  slug: open-creatify-product-to-video-api
- collection_type: open
  name: Creatify AI Avatar Text-to-Speech API
  slug: open-creatify-text-to-speech-api
- collection_type: open
  name: Creatify AI Avatar Voices API
  slug: open-creatify-voices-api
- collection_type: open
  name: Creatify API
  slug: open-creatify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/creatify-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/creatify-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creatify-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/creatify-ai
- group: company
  title: ''
  type: Website
  url: https://creatify.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.creatify.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/creatify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/creatify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/creatify-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://creatify.ai/blog
created: '2026-07-11'
description: Creatify is an AI avatar and marketing-video generation platform that turns product URLs, scripts, images, and text into short-form video ads narrated by ultra-realistic AI avatars. The Creatify API (base https://api.creatify.ai/api, authenticated with X-API-ID / X-API-KEY headers) exposes AI Avatar (Lipsync v1/v2 and Aurora image-to-avatar), Link-to-Video, AI Shorts and Custom Template video generation, Text-to-Speech and voice cloning, a 1500+ Persona/avatar catalog, a voice catalog, and a music library. Generation is asynchronous - create a job, then poll the job by id or receive a webhook - with billing metered in credits.
finops:
- name: Creatify Finops
  service_category: AI and Machine Learning
  slug: creatify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/creatify.png
layout: provider
modified: '2026-07-11'
name: Creatify
nav: Providers
network: true
overview: 'Creatify publishes 10 APIs on the [APIs.io](https://apis.io/) network, including AI Avatar API, AI Editing API, AI Shorts API, and 7 more. Tagged areas include AI Avatars, Video Generation, AI Video, Generative AI, and Marketing Video.


  Creatify''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Creatify Plans Pricing
  plan_count: 6
  slug: creatify-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Creatify Rate Limits
  slug: creatify-rate-limits
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creatify/refs/heads/main/screenshots/creatify-2026-07-25T210659.png
security:
- kind: authentication
  name: Creatify Authentication
  slug: creatify-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Creatify Domain Security
  slug: creatify-domain-security
  summary_line: HSTS · DMARC
slug: creatify
tags:
- AI Avatars
- Video Generation
- AI Video
- Generative AI
- Marketing Video
- Text-to-Speech
- UGC Ads
- AI Avatar
website: https://creatify.ai
---
