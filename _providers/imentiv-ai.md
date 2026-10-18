---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Imentiv Ai Agentic Access
  operation_count: 61
  slug: imentiv-ai-agentic-access
  summary_line: 61 operations · 34 acting
api_count: 1
apis:
- baseURL: https://api.imentiv.ai
  baseurl_source: declared
  description: 'The AI Insights API provides conversational AI-powered analysis of emotional data from your media content. **Features:** - Ask natural language questions about detected emotions, patterns, and trends '
  name: Imentiv AI AI Insights API
  slug: imentiv-ai-ai-insights-api-api
- baseURL: https://api.imentiv.ai
  baseurl_source: declared
  description: 'The Audio Emotion Analysis API processes audio files or YouTube URLs to analyze emotions and transcripts. The API provides: **Speaker Diarization:** Identifies and segments audio by speakers. **Audio '
  name: Imentiv AI Audio Emotion API
  slug: imentiv-ai-audio-emotion-api-api
- baseURL: https://api.imentiv.ai
  baseurl_source: declared
  description: The Image Emotion Recognition API by Imentiv analyzes human facial expressions in an image and returns the detected emotions. It can detect multiple faces and evaluate each face's emotional state, pro
  name: Imentiv AI Image Emotion API
  slug: imentiv-ai-image-emotion-api-api
- baseURL: https://api.imentiv.ai
  baseurl_source: declared
  description: The Report API provides comprehensive emotion analysis reports in PDF format for analyzed media content. **Features:** - Generate detailed PDF reports for video emotion analysis - Includes visual char
  name: Imentiv AI Report API
  slug: imentiv-ai-report-api-api
- baseURL: https://api.imentiv.ai
  baseurl_source: declared
  description: The Text Emotion Analysis API by Imentiv analyzes a given piece of text and returns the detected emotional tone(s). **Features:** - The API processes the text, detects emotions for each paragraph, and
  name: Imentiv AI Text Emotion API
  slug: imentiv-ai-text-emotion-api-api
- baseURL: https://api.imentiv.ai
  baseurl_source: declared
  description: The Video Emotion Analysis API by Imentiv analyzes the emotional states of individuals in a video. It performs multi-modal emotion detection using facial expressions, audio, and text transcript, and h
  name: Imentiv AI Video Emotion API
  slug: imentiv-ai-video-emotion-api-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Welcome to Imentiv AI AI Insights API API
  slug: open-imentiv-ai-ai-insights-api-api
- collection_type: open
  name: Welcome to Imentiv AI AI Insights API Audio Emotion API API
  slug: open-imentiv-ai-audio-emotion-api-api
- collection_type: open
  name: Welcome to Imentiv AI AI Insights API Image Emotion API API
  slug: open-imentiv-ai-image-emotion-api-api
- collection_type: open
  name: Welcome to Imentiv AI AI Insights API Report API API
  slug: open-imentiv-ai-report-api-api
- collection_type: open
  name: Welcome to Imentiv AI AI Insights API Text Emotion API API
  slug: open-imentiv-ai-text-emotion-api-api
- collection_type: open
  name: Welcome to Imentiv AI AI Insights API Video Emotion API API
  slug: open-imentiv-ai-video-emotion-api-api
- collection_type: open
  name: Welcome to Imentiv AI
  slug: open-imentiv-ai
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/imentiv-ai/refs/heads/main/rate-limits/imentiv-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/imentiv-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/imentiv-ai/refs/heads/main/finops/imentiv-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/imentiv-ai-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://imentiv.ai/pricing/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/imentiv-ai/refs/heads/main/plans/imentiv-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/imentiv-ai-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://imentiv.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://imentiv.ai/blog/feed.xml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/imentiv-ai/refs/heads/main/agentic-access/imentiv-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/imentiv-ai-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/imentiv-ai/refs/heads/main/security/imentiv-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imentiv-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/imentiv-ai/refs/heads/main/authentication/imentiv-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/imentiv-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/imentivai
- group: company
  title: ''
  type: Website
  url: https://imentiv.ai/
created: '2025-02-09'
description: Imentiv AI is an AI-powered platform for analyzing the emotional makeup of videos. The platform uses advanced artificial intelligence to make videos emotionally smart by detecting and analyzing emotions in video content.
finops:
- has_sources: false
  method: generated
  name: Imentiv Ai Finops
  primary_unit: ''
  service_category: API
  slug: imentiv-ai-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imentiv-ai.png
layout: provider
modified: '2026-10-06'
name: Imentiv AI
nav: Providers
network: true
overview: 'Imentiv AI publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Insights API, Audio Emotion API, Image Emotion API, and 3 more. Tagged areas include Artificial Intelligence, Emotion Detection, Machine Learning, and Video Analysis.


  Imentiv AI''s developer surface includes pricing, engineering blog, authentication, and 8 more developer resources.'
plans:
- name: Imentiv Ai Plans Pricing
  plan_count: 6
  slug: imentiv-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Imentiv Ai Rate Limits
  slug: imentiv-ai-rate-limits
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 45.7
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 25.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/imentiv-ai/refs/heads/main/screenshots/imentiv-ai-2026-06-20T183248.png
security:
- kind: authentication
  name: Imentiv Ai Authentication
  slug: imentiv-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Imentiv Ai Domain Security
  slug: imentiv-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: imentiv-ai
tags:
- Artificial Intelligence
- Emotion Detection
- Machine Learning
- Video Analysis
website: https://imentiv.ai/
---
