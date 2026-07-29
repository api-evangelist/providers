---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 10
  human_in_the_loop: 0
  name: Happyscribe Agentic Access
  operation_count: 20
  slug: happyscribe-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 7
apis:
- description: Render finished transcripts into downloadable files.
  name: Happy Scribe Exports API
  slug: happyscribe-exports-api
- description: Reusable glossaries and style guides attachable to orders.
  name: Happy Scribe Glossaries and Style Guides API
  slug: happyscribe-glossaries-and-style-guides-api
- description: Create and track transcription, subtitling, and translation orders.
  name: Happy Scribe Orders API
  slug: happyscribe-orders-api
- description: Manage members and roles within an organization.
  name: Happy Scribe Organization Memberships API
  slug: happyscribe-organization-memberships-api
- description: Organizations (workspaces) the authenticated user belongs to.
  name: Happy Scribe Organizations API
  slug: happyscribe-organizations-api
- description: List, retrieve, update, and delete transcriptions.
  name: Happy Scribe Transcriptions API
  slug: happyscribe-transcriptions-api
- description: Signed upload URLs for local media files.
  name: Happy Scribe Uploads API
  slug: happyscribe-uploads-api
artifact_total: 13
collections:
- collection_type: open
  name: Happy Scribe API
  slug: open-happyscribe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/happyscribe-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/happyscribe-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/happyscribe
- group: company
  title: ''
  type: Website
  url: https://www.happyscribe.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.happyscribe.com
- group: commercial
  title: ''
  type: Plans
  url: plans/happyscribe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/happyscribe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/happyscribe-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.happyscribe.com/blog
created: '2026-07-11'
description: Happy Scribe is a transcription, subtitling, and translation platform. Its REST API (base https://www.happyscribe.com/api/v1, Bearer-token auth) turns audio and video into text with automatic (machine) or professional (human) transcription, generates and translates subtitles/captions, and exports finished transcripts into 15+ formats (SRT, VTT, STL, DOCX, PDF, TXT, JSON, CSV, XLSX, plus editing-suite formats like Adobe Premiere XML, Final Cut Pro XML, EDL, and Avid DS). Work is organized under organizations and folders, files are ingested by URL or signed upload, and webhooks notify consumers when transcriptions complete.
finops:
- name: Happyscribe Finops
  service_category: AI and Machine Learning
  slug: happyscribe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/happyscribe.png
layout: provider
modified: '2026-07-11'
name: Happy Scribe
nav: Providers
network: true
overview: 'Happy Scribe publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Exports API, Glossaries and Style Guides API, Orders API, and 4 more. Tagged areas include Audio Transcription, Transcription, Speech-to-Text, Subtitles, and Captions.


  Happy Scribe''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Happyscribe Plans Pricing
  plan_count: 5
  slug: happyscribe-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 4
  name: Happyscribe Rate Limits
  slug: happyscribe-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/happyscribe/refs/heads/main/screenshots/happyscribe-2026-07-25T220659.png
security:
- kind: authentication
  name: Happyscribe Authentication
  slug: happyscribe-authentication
  summary_line: http · 1 scheme
slug: happyscribe
tags:
- Audio Transcription
- Transcription
- Speech-to-Text
- Subtitles
- Captions
- Translation
website: https://www.happyscribe.com
---
