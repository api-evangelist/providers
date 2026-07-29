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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Houndify platform provides HTTP and WebSocket APIs that accept text or audio queries and return actionable JSON responses. Built on SoundHound's Speech-to-Meaning and Deep Meaning Understanding te
  name: Houndify Voice AI API
  slug: houndify-voice-ai-api
- description: A high-accuracy music recognition API capable of identifying copyrighted music from as little as 2 to 10 seconds of audio with sub-second latency for streamed requests. Designed for enterprise integra
  name: SoundHound Music Fingerprint Identification API
  slug: soundhound-music-fingerprint-identification-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundhound-domain-security.yml
- group: other
  title: ''
  type: Developer Platform
  url: https://www.soundhound.com/voice-ai-products/developer/
- group: company
  title: ''
  type: Blog
  url: https://www.soundhound.com/voice-ai-resources/
- group: company
  title: ''
  type: Newsroom
  url: https://www.soundhound.com/newsroom/press-releases/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/soundhound
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.houndify.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://www.soundhound.com/contact/
- group: start
  title: ''
  type: Signup
  url: https://www.houndify.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.houndify.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://www.saashub.com/soundhound-status
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.soundhound.com/news-releases
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/soundhound/refs/heads/main/finops/soundhound.yml
created: '2026-06-13'
description: SoundHound AI is a voice AI and audio intelligence platform offering the Houndify conversational voice assistant API and a music fingerprint identification API. Developers can build voice-enabled applications using HTTP and WebSocket endpoints that accept audio or text queries and return structured JSON, powered by SoundHound's proprietary Speech-to-Meaning and Deep Meaning Understanding technologies.
finops:
- name: Soundhound
  service_category: ''
  slug: soundhound
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundhound.png
layout: provider
modified: '2026-06-13'
name: SoundHound
nav: Providers
network: true
overview: 'SoundHound publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Voice AI, Conversational AI, Music Recognition, Audio Intelligence, and Speech Recognition.


  SoundHound''s developer surface includes engineering blog, GitHub presence, signup flow, and 9 more developer resources.'
plans:
- name: Houndify Voice Ai
  plan_count: 2
  slug: houndify-voice-ai
- name: Music Id
  plan_count: 2
  slug: music-id
random_paper: 17
rate_limits:
- limit_count: 0
  name: Houndify Voice Ai
  slug: houndify-voice-ai
- limit_count: 0
  name: Music Id
  slug: music-id
score:
  band: emerging
  composite: 20.6
  delta: -2.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soundhound/refs/heads/main/screenshots/soundhound-2026-06-20T194221.png
security:
- kind: domain-security
  name: Soundhound Domain Security
  slug: soundhound-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundhound
tags:
- Voice AI
- Conversational AI
- Music Recognition
- Audio Intelligence
- Speech Recognition
- Natural Language Processing
---
