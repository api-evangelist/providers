---
access_model:
  confidence: high
  label: Sales-quoted MAU-based SDK licences with a 14-day demo token; TINT try-on plans are self-serve ($49-$1,599/mo)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.banuba.com/blog/banuba-face-ar-sdk-pricing-guide
  - https://docs.banuba.com/far-sdk/tutorials/capabilities/token_management
  - plans/banuba-plans-pricing.yml
  - sandbox/banuba-sandbox.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-09-21'
api_count: 4
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
- description: 'Banuba''s one hosted developer API: turns a single portrait image plus an audio track or script into a talking-photo video with lip-sync, facial expressions and full-body motion, rendered as an MP4 for'
  name: Banuba AI Talking Photo API
  slug: ai-talking-photo-api
artifact_total: 44
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/security/banuba-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/rules/banuba-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/banuba-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/vocabulary/banuba-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/banuba-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/json-ld/banuba-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/banuba-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.banuba.com/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/packages/banuba-packages.yml
  title: ''
  type: Packages
  url: packages/banuba-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/packages/banuba-packages.yml
  title: ''
  type: SDKs
  url: packages/banuba-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/cli/banuba-cli.yml
  title: ''
  type: CLI
  url: cli/banuba-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/components/banuba-components.yml
  title: ''
  type: Components
  url: components/banuba-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/changelog/banuba-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/banuba-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/lifecycle/banuba-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/banuba-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/authentication/banuba-authentication.yml
  title: ''
  type: Authentication
  url: authentication/banuba-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/conventions/banuba-conventions.yml
  title: ''
  type: Conventions
  url: conventions/banuba-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/plans/banuba-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/banuba-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/rate-limits/banuba-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/banuba-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/sandbox/banuba-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/banuba-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/llms/banuba-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banuba-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/llms/banuba-www-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banuba-www-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Banuba
- group: start
  title: ''
  type: DeveloperPortal
  url: https://community.banuba.com/
- group: operate
  title: ''
  type: Support
  url: https://www.banuba.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.banuba.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.banuba.com/banuba-pricing-face-ar-sdk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.banuba.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.banuba.com/facear-sdk/face-filters#form
- group: docs
  title: ''
  type: APIReference
  url: https://docs.banuba.com/far-sdk/api_docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.banuba.com/far-sdk/tutorials/development/basic_integration/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.banuba.com/far-sdk/tutorials/changelog/
- group: other
  title: ''
  type: X
  url: https://x.com/banubafacear
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCl6SgG453jxEjKxFXGmB4Lg
- group: operate
  title: ''
  type: Contact
  url: https://www.banuba.com/contact
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
modified: '2026-09-17'
name: Banuba
nav: Providers
network: true
overview: 'Banuba publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AR, Augmented Reality, Beauty, Face Recognition, and Facial.


  The Banuba catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Banuba''s developer surface includes documentation, GitHub presence, engineering blog, CLI, changelog, authentication, sandbox, and 33 more developer resources.'
plans:
- name: Banuba Plans Pricing
  plan_count: 6
  slug: banuba-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Banuba Rate Limits
  slug: banuba-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Banuba API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: banuba-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Banuba API Rules
  rule_count: 7
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 1
  slug: banuba-spectral-rules
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 66.3
    catalog_earned_first_party: 12.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 85.7
    discoverability: 72.2
    operational_transparency: 18.4
  previous_composite: 49.3
  provenance:
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/banuba/refs/heads/main/screenshots/banuba-2026-06-20T172957.png
security:
- kind: authentication
  name: Banuba Authentication
  slug: banuba-authentication
  summary_line: 3 schemes
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
