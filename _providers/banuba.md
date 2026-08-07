---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.7
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: The Banuba Face AR SDK provides AR face effects, beauty filters, and face tracking for mobile (iOS/Android), web, and desktop applications. The SDK includes real-time face detection, 3D face tracking,
  name: Banuba Face AR SDK
  slug: face-ar-sdk
- description: Banuba Video Editor SDK is a complete white-label video and photo editing solution for iOS and Android with AI features including auto-clipping, captions, beauty filters, AR effects, and music integra
  name: Banuba Video Editor SDK
  slug: video-editor-sdk
- description: Banuba Face Liveness SDK provides anti-spoofing technology that verifies a face is real and present in real time, used for identity verification and access control.
  name: Banuba Face Liveness SDK
  slug: face-liveness-sdk
artifact_total: 42
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/banuba-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/Banuba/ai-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/banuba
- group: company
  title: ''
  type: Website
  url: https://www.banuba.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.banuba.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.banuba.com/far-sdk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Banuba
- group: company
  title: ''
  type: Blog
  url: https://www.banuba.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banuba.com/privacy-policy
- group: design
  title: ''
  type: SpectralRules
  url: rules/banuba-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/banuba-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/banuba-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.banuba.com/llms.txt
created: '2024-12-16'
description: Banuba is an AR and AI technology company providing the Face AR SDK for augmented reality face effects, beauty filters, and virtual try-on experiences. The SDK supports iOS, Android, Web (HTML5), Windows, macOS, Unity, Flutter, and React Native. Use cases include live streaming beauty filters, video conferencing face effects, selfie editing, virtual makeup try-on, and face tracking for interactive applications.
examples:
- key_count: 7
  name: Areffect Example
  slug: areffect-example
- key_count: 7
  name: Beautyfilter Example
  slug: beautyfilter-example
features:
- description: Real-time AR face masks, filters, and accessories for live and recorded video.
  name: Face AR Effects
- description: Skin smoothing, face reshaping, eye enlargement, and makeup filters.
  name: Beauty Filters
- description: Precise 3D face landmark tracking for accurate AR effect placement.
  name: 3D Face Tracking
- description: Real-time background removal and replacement for video calls.
  name: Background Segmentation
- description: Virtual makeup, glasses, hair color, and accessory try-on experiences.
  name: Virtual Try-On
- description: ML-powered face detection with age, gender, and emotion analysis.
  name: AI Face Detection
- description: Native SDKs for iOS, Android, Web, Windows, macOS, Unity, Flutter, and React Native.
  name: Cross-Platform SDK
- description: Banuba Effect Player for creating custom AR effects without coding.
  name: Custom Effects Builder
finops:
- name: Banuba Finops
  service_category: API
  slug: banuba-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/banuba.png
json_schemas:
- name: AREffect
  property_count: 7
  slug: areffect
- name: BeautyFilter
  property_count: 7
  slug: beautyfilter
json_structures:
- name: Banuba Json Structure
  property_count: 0
  slug: banuba-json-structure
jsonld:
- class_count: 3
  name: Banuba Context
  property_count: 14
  slug: banuba-context
layout: provider
modified: '2026-04-21'
name: Banuba
nav: Providers
network: true
overview: 'Banuba publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AR, Augmented Reality, Beauty, Face Recognition, and Facial.


  The Banuba catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Banuba''s developer surface includes documentation, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Banuba Plans Pricing
  plan_count: 3
  slug: banuba-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 5
  name: Banuba Rate Limits
  slug: banuba-rate-limits
rules:
- name: Banuba API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: banuba-jsonschema-spectral-rules
- name: Banuba API Rules
  rule_count: 7
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 1
  slug: banuba-spectral-rules
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 34.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/screenshots/banuba-2026-06-20T172957.png
security:
- kind: domain-security
  name: Banuba Domain Security
  slug: banuba-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 13
skills:
- name: build-photo-editor
  slug: build-photo-editor-2
- name: build-photo-editor
  slug: build-photo-editor-3
- name: build-photo-editor
  slug: build-photo-editor-4
- name: build-photo-editor
  slug: build-photo-editor
- name: build-video-editor
  slug: build-video-editor-2
- name: build-video-editor
  slug: build-video-editor-3
- name: build-video-editor
  slug: build-video-editor-4
- name: build-video-editor
  slug: build-video-editor
- name: explain-video-editor-photo-editor-docs
  slug: explain-video-editor-photo-editor-docs-2
- name: explain-video-editor-photo-editor-docs
  slug: explain-video-editor-photo-editor-docs-3
- name: explain-video-editor-photo-editor-docs
  slug: explain-video-editor-photo-editor-docs-4
- name: explain-video-editor-photo-editor-docs
  slug: explain-video-editor-photo-editor-docs
- name: far-general
  slug: far-general
slug: banuba
tags:
- AR
- Augmented Reality
- Beauty
- Face Recognition
- Facial
- SDK
- Video
use_cases:
- description: Real-time beauty and AR filters for live streaming platforms.
  name: Live Streaming Beauty Filters
- description: Face effects and background segmentation for video call applications.
  name: Video Conferencing
- description: Beauty retouching and AR effects for mobile photo editing apps.
  name: Selfie and Photo Editing
- description: AI-powered virtual makeup try-on for beauty e-commerce.
  name: Virtual Makeup Try-On
- description: Face-based liveness detection and verification for security applications.
  name: Face Authentication
- description: Face-tracked AR avatars and character animation for games.
  name: Gaming and Entertainment
website: https://www.banuba.com/
---
