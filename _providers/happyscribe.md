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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Happyscribe Agentic Access
  operation_count: 20
  slug: happyscribe-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 1
apis:
- baseURL: https://www.happyscribe.com/api/v1
  baseurl_source: declared
  description: Render finished transcripts into downloadable files.
  name: Happy Scribe Exports API
  slug: happyscribe-exports-api
- baseURL: https://www.happyscribe.com/api/v1
  baseurl_source: declared
  description: Reusable glossaries and style guides attachable to orders.
  name: Happy Scribe Glossaries and Style Guides API
  slug: happyscribe-glossaries-and-style-guides-api
- baseURL: https://www.happyscribe.com/api/v1
  baseurl_source: declared
  description: Create and track transcription, subtitling, and translation orders.
  name: Happy Scribe Orders API
  slug: happyscribe-orders-api
- baseURL: https://www.happyscribe.com/api/v1
  baseurl_source: declared
  description: Manage members and roles within an organization.
  name: Happy Scribe Organization Memberships API
  slug: happyscribe-organization-memberships-api
- baseURL: https://www.happyscribe.com/api/v1
  baseurl_source: declared
  description: Organizations (workspaces) the authenticated user belongs to.
  name: Happy Scribe Organizations API
  slug: happyscribe-organizations-api
- baseURL: https://www.happyscribe.com/api/v1
  baseurl_source: declared
  description: List, retrieve, update, and delete transcriptions.
  name: Happy Scribe Transcriptions API
  slug: happyscribe-transcriptions-api
- baseURL: https://www.happyscribe.com/api/v1
  baseurl_source: declared
  description: Signed upload URLs for local media files.
  name: Happy Scribe Uploads API
  slug: happyscribe-uploads-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Happy Scribe Exports API
  slug: open-happyscribe-exports-api
- collection_type: open
  name: Happy Scribe Exports Glossaries and Style Guides API
  slug: open-happyscribe-glossaries-and-style-guides-api
- collection_type: open
  name: Happy Scribe Exports Orders API
  slug: open-happyscribe-orders-api
- collection_type: open
  name: Happy Scribe Exports Organization Memberships API
  slug: open-happyscribe-organization-memberships-api
- collection_type: open
  name: Happy Scribe Exports Organizations API
  slug: open-happyscribe-organizations-api
- collection_type: open
  name: Happy Scribe Exports Transcriptions API
  slug: open-happyscribe-transcriptions-api
- collection_type: open
  name: Happy Scribe Exports Uploads API
  slug: open-happyscribe-uploads-api
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
random_paper: 2
rate_limits:
- limit_count: 4
  name: Happyscribe Rate Limits
  slug: happyscribe-rate-limits
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
