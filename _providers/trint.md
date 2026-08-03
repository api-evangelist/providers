---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Trint Agentic Access
  operation_count: 20
  slug: trint-agentic-access
  summary_line: 20 operations · 9 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Export transcripts and captions in various formats.
  name: Trint Export API
  slug: trint-export-api
- description: Live/realtime transcription via an RTMP media stream.
  name: Trint Realtime API
  slug: trint-realtime-api
- description: List and retrieve transcripts (files), folders, and shared drives.
  name: Trint Transcripts and Files API
  slug: trint-transcripts-and-files-api
- description: Translate transcripts into other languages.
  name: Trint Translations API
  slug: trint-translations-api
- description: Upload or ingest media and start automatic transcription.
  name: Trint Upload and Transcribe API
  slug: trint-upload-and-transcribe-api
- description: Register callbacks for transcription lifecycle events.
  name: Trint Webhooks API
  slug: trint-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Trint API
  slug: open-trint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trint-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trint-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trint
- group: company
  title: ''
  type: Website
  url: https://trint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.trint.com
- group: commercial
  title: ''
  type: Plans
  url: plans/trint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trint-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://trint.com/blog
created: '2026-07-11'
description: Trint is an AI-powered audio and video transcription platform built for media, journalism, and enterprise content teams. It transcribes speech to text in dozens of languages, offers a collaborative editor, translation, and story-building tools, and exposes a documented REST API at dev.trint.com for uploading and transcribing media, listing and exporting transcripts (JSON, text, CSV, Word, SRT captions, EDL, Premiere XML), translating, running realtime transcription over an RTMP stream, and receiving webhook events.
finops:
- name: Trint Finops
  service_category: AI and Machine Learning
  slug: trint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trint.png
layout: provider
modified: '2026-07-11'
name: Trint
nav: Providers
network: true
overview: 'Trint publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Export API, Realtime API, Transcripts and Files API, and 3 more. Tagged areas include Audio Transcription, Transcription, Speech-to-Text, Media, and Journalism.


  Trint''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Trint Plans Pricing
  plan_count: 3
  slug: trint-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 4
  name: Trint Rate Limits
  slug: trint-rate-limits
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Trint Authentication
  slug: trint-authentication
  summary_line: http/apiKey · 2 schemes
slug: trint
tags:
- Audio Transcription
- Transcription
- Speech-to-Text
- Media
- Journalism
- AI
- Captions
website: https://trint.com/
---
