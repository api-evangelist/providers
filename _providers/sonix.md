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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Sonix Agentic Access
  operation_count: 22
  slug: sonix-agentic-access
  summary_line: 22 operations · 11 acting
api_count: 1
apis:
- description: Generate summaries, chapters, sentiment, and entity analysis from transcripts.
  name: Sonix AI Analysis API
  slug: sonix-ai-analysis-api
- description: Export transcripts as subtitles, captions, documents, and media burn-ins.
  name: Sonix Exports API
  slug: sonix-exports-api
- description: Organize media into folders.
  name: Sonix Folders API
  slug: sonix-folders-api
- description: Upload and manage audio and video media files for transcription.
  name: Sonix Media API
  slug: sonix-media-api
- description: Retrieve and edit transcripts produced from media.
  name: Sonix Transcripts API
  slug: sonix-transcripts-api
- description: Translate a completed transcript into another language.
  name: Sonix Translations API
  slug: sonix-translations-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sonix AI Analysis API
  slug: open-sonix-ai-analysis-api
- collection_type: open
  name: Sonix AI Analysis Exports API
  slug: open-sonix-exports-api
- collection_type: open
  name: Sonix AI Analysis Folders API
  slug: open-sonix-folders-api
- collection_type: open
  name: Sonix AI Analysis Media API
  slug: open-sonix-media-api
- collection_type: open
  name: Sonix AI Analysis Transcripts API
  slug: open-sonix-transcripts-api
- collection_type: open
  name: Sonix AI Analysis Translations API
  slug: open-sonix-translations-api
- collection_type: open
  name: Sonix API
  slug: open-sonix
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sonix-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sonix-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonix-ai
- group: company
  title: ''
  type: Website
  url: https://sonix.ai
- group: docs
  title: ''
  type: Documentation
  url: https://sonix.ai/docs/api
- group: commercial
  title: ''
  type: Plans
  url: plans/sonix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sonix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sonix-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sonix.ai/resources
created: '2026-07-11'
description: Sonix is an AI-powered platform for automated audio and video transcription, subtitles, and translation. It transcribes in 54+ languages with speaker labels and word-level timestamps, translates transcripts into 55+ languages, generates subtitles and captions (SRT, VTT, TXT, JSON, DOCX, PDF), and runs AI analysis (summaries, chapters, sentiment, entities). The Sonix REST API - available to subscribers - lets developers upload media, poll transcription status, retrieve and edit transcripts, export subtitles, and translate, all authorized with a Bearer API key against https://api.sonix.ai/v1.
finops:
- name: Sonix Finops
  service_category: AI and Machine Learning
  slug: sonix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sonix.png
layout: provider
modified: '2026-07-11'
name: Sonix
nav: Providers
network: true
overview: 'Sonix publishes 6 APIs on the [APIs.io](https://apis.io/) network, including AI Analysis API, Exports API, Folders API, and 3 more. Tagged areas include Audio Transcription, Transcription, Speech-to-Text, Subtitles, and Captions.


  Sonix''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Sonix Plans Pricing
  plan_count: 5
  slug: sonix-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Sonix Rate Limits
  slug: sonix-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.2
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Sonix Authentication
  slug: sonix-authentication
  summary_line: http · 1 scheme
slug: sonix
tags:
- Audio Transcription
- Transcription
- Speech-to-Text
- Subtitles
- Captions
- Translation
- Artificial Intelligence
- Media
website: https://sonix.ai
---
