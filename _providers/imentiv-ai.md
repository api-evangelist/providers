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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Imentiv Ai Agentic Access
  operation_count: 61
  slug: imentiv-ai-agentic-access
  summary_line: 61 operations · 34 acting
api_count: 6
apis:
- description: 'The AI Insights API provides conversational AI-powered analysis of emotional data from your media content. **Features:** - Ask natural language questions about detected emotions, patterns, and trends '
  name: Imentiv AI AI Insights API API
  slug: imentiv-ai-ai-insights-api-api
- description: 'The Audio Emotion Analysis API processes audio files or YouTube URLs to analyze emotions and transcripts. The API provides: **Speaker Diarization:** Identifies and segments audio by speakers. **Audio '
  name: Imentiv AI Audio Emotion API API
  slug: imentiv-ai-audio-emotion-api-api
- description: The Image Emotion Recognition API by Imentiv analyzes human facial expressions in an image and returns the detected emotions. It can detect multiple faces and evaluate each face's emotional state, pro
  name: Imentiv AI Image Emotion API API
  slug: imentiv-ai-image-emotion-api-api
- description: The Report API provides comprehensive emotion analysis reports in PDF format for analyzed media content. **Features:** - Generate detailed PDF reports for video emotion analysis - Includes visual char
  name: Imentiv AI Report API API
  slug: imentiv-ai-report-api-api
- description: The Text Emotion Analysis API by Imentiv analyzes a given piece of text and returns the detected emotional tone(s). **Features:** - The API processes the text, detects emotions for each paragraph, and
  name: Imentiv AI Text Emotion API API
  slug: imentiv-ai-text-emotion-api-api
- description: The Video Emotion Analysis API by Imentiv analyzes the emotional states of individuals in a video. It performs multi-modal emotion detection using facial expressions, audio, and text transcript, and h
  name: Imentiv AI Video Emotion API API
  slug: imentiv-ai-video-emotion-api-api
artifact_total: 13
collections:
- collection_type: open
  name: Welcome to Imentiv AI
  slug: open-imentiv-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imentiv-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imentiv-ai-domain-security.yml
- group: auth
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
- name: Imentiv Ai Finops
  service_category: API
  slug: imentiv-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imentiv-ai.png
layout: provider
modified: '2026-05-19'
name: Imentiv AI
nav: Providers
network: true
overview: 'Imentiv AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Insights API API, Audio Emotion API API, Image Emotion API API, and 3 more. Tagged areas include Artificial Intelligence, Emotion Detection, Machine Learning, and Video Analysis.


  Imentiv AI''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Imentiv Ai Plans Pricing
  plan_count: 3
  slug: imentiv-ai-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 5
  name: Imentiv Ai Rate Limits
  slug: imentiv-ai-rate-limits
score:
  band: emerging
  composite: 26.4
  delta: -8.3
  facets:
    commercial_clarity: 15.8
    contract_quality: 54.2
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
