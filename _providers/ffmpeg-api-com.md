---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ffmpeg Api Com Agentic Access
  operation_count: 2
  slug: ffmpeg-api-com-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.ffmpeg-api.com
  baseurl_source: declared
  description: For running FFmpeg tasks
  name: ffmpeg-api-com F Fmpeg API
  slug: ffmpeg-api-com-ffmpeg-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/ffmpeg-api-com/agentic-access/ffmpeg-api-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ffmpeg-api-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-api-com/rules/ffmpeg-api-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ffmpeg-api-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-api-com/vocabulary/ffmpeg-api-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ffmpeg-api-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/ffmpeg-api-com/authentication/ffmpeg-api-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ffmpeg-api-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/ffmpeg-api-com/lifecycle/ffmpeg-api-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ffmpeg-api-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-api-com/lifecycle/ffmpeg-api-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ffmpeg-api-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ffmpeg-api-com/conformance/ffmpeg-api-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ffmpeg-api-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ffmpeg-api-com/llms/ffmpeg-api-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ffmpeg-api-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ffmpeg-api-com/well-known/ffmpeg-api-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ffmpeg-api-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ffmpeg-api-com/hosts/ffmpeg-api-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ffmpeg-api-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ffmpeg-api-com/vendors/ffmpeg-api-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ffmpeg-api-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ffmpeg-api-com/security/ffmpeg-api-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ffmpeg-api-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ffmpeg-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ffmpeg-api.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ffmpeg-api.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://ffmpeg-api.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://ffmpeg-api.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ffmpeg-api.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ffmpeg-api.com/terms
created: '2026-10-30'
description: FFmpeg API provides a cloud-based service to process video and audio using FFmpeg via simple HTTP endpoints. Developers can upload media files, configure processing options, and retrieve results without managing FFmpeg installations. The platform offers file management, directory handling, and usage billing measured in GB‑seconds. It supports formats like MP4, WebM, GIF, and advanced filters, targeting rapid integration of media features into applications.
json_schemas:
- name: AsyncJobResponse
  property_count: 6
  slug: ffmpeg-api-com-async-job-response
- name: CompressVideoResponse
  property_count: 8
  slug: ffmpeg-api-com-compress-video-response
- name: EndlessLoopResponse
  property_count: 9
  slug: ffmpeg-api-com-endless-loop-response
- name: JobStatusResponse
  property_count: 14
  slug: ffmpeg-api-com-job-status-response
- name: SplitAudioSegmentsResponse
  property_count: 5
  slug: ffmpeg-api-com-split-audio-segments-response
- name: SplitVideoResponse
  property_count: 3
  slug: ffmpeg-api-com-split-video-response
jsonld:
- class_count: 13
  name: Ffmpeg Api Com Context
  property_count: 39
  slug: ffmpeg-api-com-context
layout: provider
modified: '2026-10-30'
name: ffmpeg-api-com
nav: Providers
network: true
overview: 'ffmpeg-api-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: F Fmpeg API. Tagged areas include Video, Audio, MediaProcessing, CloudAPI, and FFmpeg.


  The ffmpeg-api-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ffmpeg-api-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 0
  name: Ffmpeg Api Com Rate Limits
  slug: ffmpeg-api-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ffmpeg-api-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ffmpeg-api-com-rules
scopes:
- name: Ffmpeg Api Com Scopes
  scope_count: 0
  slug: ffmpeg-api-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 17.7
    developer_ergonomics: 40.5
    discoverability: 62.5
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
  name: Ffmpeg Api Com Authentication
  slug: ffmpeg-api-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ffmpeg Api Com Domain Security
  slug: ffmpeg-api-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: ffmpeg-api-com-merge-image-audio
  slug: ffmpeg-api-com-merge-image-audio
slug: ffmpeg-api-com
tags:
- Video
- Audio
- MediaProcessing
- CloudAPI
- FFmpeg
website: https://ffmpeg-api.com/
---
