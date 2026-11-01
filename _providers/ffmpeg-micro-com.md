---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Ffmpeg Micro Com Agentic Access
  operation_count: 21
  slug: ffmpeg-micro-com-agentic-access
  summary_line: 21 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.ffmpeg-micro.com
  baseurl_source: declared
  description: The Blueprints API from ffmpeg-micro-com — 3 operation(s) for blueprints.
  name: ffmpeg-micro-com Blueprints API
  slug: ffmpeg-micro-com-blueprints-api
- baseURL: https://api.ffmpeg-micro.com
  baseurl_source: declared
  description: The Ffprobe API from ffmpeg-micro-com — 1 operation(s) for ffprobe.
  name: ffmpeg-micro-com Ffprobe API
  slug: ffmpeg-micro-com-ffprobe-api
- baseURL: https://api.ffmpeg-micro.com
  baseurl_source: declared
  description: The Generate API from ffmpeg-micro-com — 6 operation(s) for generate.
  name: ffmpeg-micro-com Generate API
  slug: ffmpeg-micro-com-generate-api
- baseURL: https://api.ffmpeg-micro.com
  baseurl_source: declared
  description: The Transcodes API from ffmpeg-micro-com — 4 operation(s) for transcodes.
  name: ffmpeg-micro-com Transcodes API
  slug: ffmpeg-micro-com-transcodes-api
- baseURL: https://api.ffmpeg-micro.com
  baseurl_source: declared
  description: The Transcribe API from ffmpeg-micro-com — 3 operation(s) for transcribe.
  name: ffmpeg-micro-com Transcribe API
  slug: ffmpeg-micro-com-transcribe-api
- baseURL: https://api.ffmpeg-micro.com
  baseurl_source: declared
  description: The Transcribes API from ffmpeg-micro-com — 1 operation(s) for transcribes.
  name: ffmpeg-micro-com Transcribes API
  slug: ffmpeg-micro-com-transcribes-api
- baseURL: https://api.ffmpeg-micro.com
  baseurl_source: declared
  description: The Upload API from ffmpeg-micro-com — 2 operation(s) for upload.
  name: ffmpeg-micro-com Upload API
  slug: ffmpeg-micro-com-upload-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/ffmpeg-micro-com/agentic-access/ffmpeg-micro-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ffmpeg-micro-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ffmpeg-micro-com/plans/ffmpeg-micro-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ffmpeg-micro-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-micro-com/rules/ffmpeg-micro-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ffmpeg-micro-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-micro-com/json-ld/ffmpeg-micro-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ffmpeg-micro-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ffmpeg-micro-com/vocabulary/ffmpeg-micro-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ffmpeg-micro-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ffmpeg-micro-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-micro-com/data-model/ffmpeg-micro-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ffmpeg-micro-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ffmpeg-micro-com/authentication/ffmpeg-micro-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ffmpeg-micro-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-micro-com/errors/ffmpeg-micro-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ffmpeg-micro-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-micro-com/conformance/ffmpeg-micro-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ffmpeg-micro-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ffmpeg-micro-com/llms/ffmpeg-micro-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ffmpeg-micro-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ffmpeg-micro-com/well-known/ffmpeg-micro-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ffmpeg-micro-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ffmpeg-micro-com/hosts/ffmpeg-micro-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ffmpeg-micro-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ffmpeg-micro-com/vendors/ffmpeg-micro-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ffmpeg-micro-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/ffmpeg-micro-com/packages/ffmpeg-micro-com-packages.yml
  title: ''
  type: SDKs
  url: packages/ffmpeg-micro-com-packages.yml
- group: build
  href: https://artifacts.apis.io/ffmpeg-micro-com/packages/ffmpeg-micro-com-packages.yml
  title: ''
  type: Packages
  url: packages/ffmpeg-micro-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ffmpeg-micro.com/legal/terms
- group: start
  title: ''
  type: Sandbox
  url: https://www.ffmpeg-micro.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ffmpeg-micro.com/legal/privacy
- group: auth
  href: https://artifacts.apis.io/ffmpeg-micro-com/security/ffmpeg-micro-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ffmpeg-micro-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ffmpeg-micro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ffmpeg-micro.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ffmpeg-micro.com/auth/signup
- group: operate
  title: ''
  type: Support
  url: https://www.ffmpeg-micro.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.ffmpeg-micro.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ffmpeg-micro
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ffmpeg-micro.com/pricing
created: '2026-10-30'
description: FFmpeg Micro provides a hosted REST API that brings the power of FFmpeg video processing to developers at scale. Users can upload media, transcode to various formats, add captions, and generate short-form video content without managing any servers or installing FFmpeg themselves. The service integrates with popular automation platforms such as n8n, Make, and Zapier, and offers a simple HTTP interface with pay‑per‑use pricing. It targets content creators, marketers, and developers who need to automate video creation, editing, and repurposing workflows.
image: https://www.ffmpeg-micro.com/og-image.jpg
json_schemas:
- name: CreateTranscodeRequest
  property_count: 5
  slug: ffmpeg-micro-com-create-transcode-request
- name: CreateTranscribeRequest
  property_count: 3
  slug: ffmpeg-micro-com-create-transcribe-request
- name: GenerateImageRequest
  property_count: 5
  slug: ffmpeg-micro-com-generate-image-request
- name: MediaMetadata
  property_count: 10
  slug: ffmpeg-micro-com-media-metadata
- name: Transcode
  property_count: 22
  slug: ffmpeg-micro-com-transcode
- name: Transcribe
  property_count: 19
  slug: ffmpeg-micro-com-transcribe
jsonld:
- class_count: 26
  name: Ffmpeg Micro Com Context
  property_count: 75
  slug: ffmpeg-micro-com-context
layout: provider
modified: '2026-10-30'
name: ffmpeg-micro-com
nav: Providers
network: true
overview: 'ffmpeg-micro-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Blueprints API, Ffprobe API, Generate API, and 4 more. Tagged areas include Video, API, Automation, FFmpeg, and Cloud.


  The ffmpeg-micro-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ffmpeg-micro-com''s developer surface includes authentication, sandbox, documentation, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Ffmpeg Micro Com Plans Pricing
  plan_count: 3
  slug: ffmpeg-micro-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Ffmpeg Micro Com Rate Limits
  slug: ffmpeg-micro-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ffmpeg-micro-com API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: ffmpeg-micro-com-rules
scopes:
- name: Ffmpeg Micro Com Scopes
  scope_count: 0
  slug: ffmpeg-micro-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 85.8
    catalog_earned_first_party: 0.0
    catalog_gap: 29.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 70.9
    contract_quality: 58.2
    developer_ergonomics: 68.3
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ffmpeg Micro Com Authentication
  slug: ffmpeg-micro-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ffmpeg Micro Com Domain Security
  slug: ffmpeg-micro-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ffmpeg-micro-com
tags:
- Video
- API
- Automation
- FFmpeg
- Cloud
- MediaProcessing
website: https://ffmpeg-micro.com/
---
