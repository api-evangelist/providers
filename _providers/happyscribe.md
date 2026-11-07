---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
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
artifact_total: 22
collections:
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
- group: other
  href: https://artifacts.apis.io/happyscribe/capabilities/happyscribe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/happyscribe-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/happyscribe/agentic-access/happyscribe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/happyscribe-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/happyscribe/authentication/happyscribe-authentication.yml
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
  href: https://artifacts.apis.io/happyscribe/plans/happyscribe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/happyscribe-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/happyscribe/rate-limits/happyscribe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/happyscribe-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/happyscribe/finops/happyscribe-finops.yml
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
- has_sources: true
  method: generated
  name: Happyscribe Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: happyscribe-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/happyscribe.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.happyscribe.com over HTTP.
  name: Happy Scribe MCP Server
  slug: happyscribe
modified: '2026-07-11'
name: Happy Scribe
nav: Providers
network: true
overview: 'Happy Scribe publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Exports API, Glossaries and Style Guides API, Orders API, and 4 more. Tagged areas include Audio Transcription, Transcription, Speech-to-Text, Subtitles, and Captions.


  The Happy Scribe catalog on APIs.io includes 1 Spectral governance ruleset.


  Happy Scribe''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Happyscribe Plans Pricing
  plan_count: 5
  slug: happyscribe-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Happyscribe Rate Limits
  slug: happyscribe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Happy Scribe API Rules
  rule_count: 64
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 3
  slug: happyscribe-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 53.6
    developer_ergonomics: 31.0
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 28.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/happyscribe/happyscribe-2026-07-25T220659.png
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
