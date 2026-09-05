---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Trint Agentic Access
  operation_count: 20
  slug: trint-agentic-access
  summary_line: 20 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://upload.trint.com
  baseurl_source: declared
  description: Export transcripts and captions in various formats.
  name: Trint Export API
  slug: trint-export-api
- baseURL: https://upload.trint.com
  baseurl_source: declared
  description: Live/realtime transcription via an RTMP media stream.
  name: Trint Realtime API
  slug: trint-realtime-api
- baseURL: https://upload.trint.com
  baseurl_source: declared
  description: List and retrieve transcripts (files), folders, and shared drives.
  name: Trint Transcripts and Files API
  slug: trint-transcripts-and-files-api
- baseURL: https://upload.trint.com
  baseurl_source: declared
  description: Translate transcripts into other languages.
  name: Trint Translations API
  slug: trint-translations-api
- baseURL: https://upload.trint.com
  baseurl_source: declared
  description: Upload or ingest media and start automatic transcription.
  name: Trint Upload and Transcribe API
  slug: trint-upload-and-transcribe-api
- baseURL: https://upload.trint.com
  baseurl_source: declared
  description: Register callbacks for transcription lifecycle events.
  name: Trint Webhooks API
  slug: trint-webhooks-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trint Export API
  slug: open-trint-export-api
- collection_type: open
  name: Trint Export Realtime API
  slug: open-trint-realtime-api
- collection_type: open
  name: Trint Export Transcripts and Files API
  slug: open-trint-transcripts-and-files-api
- collection_type: open
  name: Trint Export Translations API
  slug: open-trint-translations-api
- collection_type: open
  name: Trint Export Upload and Transcribe API
  slug: open-trint-upload-and-transcribe-api
- collection_type: open
  name: Trint Export Webhooks API
  slug: open-trint-webhooks-api
- collection_type: open
  name: Trint API
  slug: open-trint
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/trint-capability-edges.yml
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


  Trint''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Trint Plans Pricing
  plan_count: 3
  slug: trint-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Trint Rate Limits
  slug: trint-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trint/refs/heads/main/screenshots/trint-2026-09-02T164239.png
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
- Artificial Intelligence
- Captions
website: https://trint.com/
---
