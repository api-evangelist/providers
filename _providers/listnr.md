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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Listnr Agentic Access
  operation_count: 6
  slug: listnr-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 3
apis:
- description: Poll the status of asynchronous conversion jobs.
  name: Listnr Jobs API
  slug: listnr-jobs-api
- description: Convert SSML text or an article URL into audio.
  name: Listnr Text-to-Speech API
  slug: listnr-text-to-speech-api
- description: List the AI voices available on Listnr.
  name: Listnr Voices API
  slug: listnr-voices-api
artifact_total: 10
collections:
- collection_type: open
  name: Listnr Text-to-Speech API
  slug: open-listnr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/listnr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listnr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/listnr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listnr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-listnr
- group: company
  title: ''
  type: Website
  url: https://listnr.ai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/team-listnr/text-to-speech-api
- group: start
  title: ''
  type: SignUp
  url: https://voices.listnr.tech
- group: commercial
  title: ''
  type: Plans
  url: plans/listnr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/listnr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/listnr-finops.yml
created: '2026-07-11'
description: Listnr AI is a text-to-speech and AI voice platform offering 1,000+ ultra-realistic voices across 142+ languages and accents, used for voiceovers, podcasts, and text-to-video. Beyond the web app, Listnr exposes a documented public Text-to-Speech API (base https://bff.listnr.tech/api/tts/v1) that converts SSML text or article URLs into MP3/WAV audio synchronously or asynchronously, lists available voices, and reports async job status. API keys are generated from the Listnr dashboard at voices.listnr.tech and passed via an x-listnr-token header.
finops:
- name: Listnr Finops
  service_category: AI and Machine Learning
  slug: listnr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listnr.png
layout: provider
modified: '2026-07-11'
name: Listnr
nav: Providers
network: true
overview: 'Listnr publishes 3 APIs on the [APIs.io](https://apis.io/) network: Jobs API, Text-to-Speech API, and Voices API. Tagged areas include AI, Text to Speech, TTS, Voice, and Speech Synthesis.


  Listnr''s developer surface includes authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Listnr Plans Pricing
  plan_count: 4
  slug: listnr-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 3
  name: Listnr Rate Limits
  slug: listnr-rate-limits
score:
  band: thin
  composite: 37.9
  delta: -5.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/listnr/refs/heads/main/screenshots/listnr-2026-07-25T225328.png
security:
- kind: authentication
  name: Listnr Authentication
  slug: listnr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Listnr Domain Security
  slug: listnr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: listnr
tags:
- AI
- Text to Speech
- TTS
- Voice
- Speech Synthesis
- Audio
- Voiceover
website: https://listnr.ai
---
