---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Transcriptapi Com Agentic Access
  operation_count: 13
  slug: transcriptapi-com-agentic-access
  summary_line: 13 operations
api_count: 1
apis:
- baseURL: https://transcriptapi.com
  baseurl_source: declared
  description: 'Size up a channel and pull everything it publishes: subscriber and video counts, uploads, Shorts, live streams, playlists, community posts, sections, and available tabs, from any @handle, URL, or chan'
  name: transcriptapi-com YouTube channel API
  slug: transcriptapi-com-youtube-channel-api
- baseURL: https://transcriptapi.com
  baseurl_source: declared
  description: 'Walk every video in a playlist, paginated: a full course, season, or collection, ready to process.'
  name: transcriptapi-com YouTube playlist API
  slug: transcriptapi-com-youtube-playlist-api
- baseURL: https://transcriptapi.com
  baseurl_source: declared
  description: 'Find the videos, channels, playlists, or movies worth processing: search a topic, then filter by popularity, upload date, or duration to build a work queue.'
  name: transcriptapi-com YouTube search API
  slug: transcriptapi-com-youtube-search-api
- baseURL: https://transcriptapi.com
  baseurl_source: declared
  description: Pull any video's transcript by URL or 11-character ID, with or without timestamps, as JSON or text. Check available languages first, then pull the exact track.
  name: transcriptapi-com YouTube transcript API
  slug: transcriptapi-com-youtube-transcript-api
- baseURL: https://transcriptapi.com
  baseurl_source: declared
  description: 'Get a video''s stats and context without transcribing: view and like counts, publish date, the full description with its links extracted, and related videos. Add include=details for duration, category,'
  name: transcriptapi-com YouTube video API
  slug: transcriptapi-com-youtube-video-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/transcriptapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/transcriptapi-com/agentic-access/transcriptapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transcriptapi-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-com/rules/transcriptapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/transcriptapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-com/json-ld/transcriptapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/transcriptapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/transcriptapi-com/vocabulary/transcriptapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/transcriptapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-com/data-model/transcriptapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transcriptapi-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/transcriptapi-com/authentication/transcriptapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transcriptapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-com/errors/transcriptapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/transcriptapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-com/conformance/transcriptapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transcriptapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/transcriptapi-com/llms/transcriptapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/transcriptapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/transcriptapi-com/well-known/transcriptapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/transcriptapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/transcriptapi-com/hosts/transcriptapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transcriptapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/transcriptapi-com/vendors/transcriptapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transcriptapi-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://transcriptapi.com/swagger
- group: auth
  href: https://artifacts.apis.io/transcriptapi-com/security/transcriptapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transcriptapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transcriptapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://transcriptapi.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://transcriptapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://transcriptapi.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://transcriptapi.com/docs/getting-started/python/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transcriptapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transcriptapi.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://transcriptapi.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://transcriptapi.com/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://transcriptapi.com/openapi.json
  - status: 401
    url: https://transcriptapi.com/mcp
  - status: 200
    url: https://transcriptapi.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: TranscriptAPI provides a YouTube Transcript API with search, channel and playlist capabilities. It offers REST endpoints to retrieve video transcripts, search across videos, browse channels, and extract playlists, supporting both standard API access and YouTube MCP integration. The service processes over 15 million transcripts monthly, serving a large developer community with reliable, low-latency responses.
image: https://transcriptapi.com/brand/youtube-transcript-api-og.png
json_schemas:
- name: APITranscriptResponseV2
  property_count: 6
  slug: transcriptapi-com-apitranscript-response-v2
- name: VideoInfoResponse
  property_count: 3
  slug: transcriptapi-com-app-api-v2-youtube-schemas-video-info-response
- name: VideoInfoResponse
  property_count: 13
  slug: transcriptapi-com-app-api-v2-youtube-schemas-youtube-video-info-response
- name: ChannelInfoResponse
  property_count: 13
  slug: transcriptapi-com-channel-info-response
- name: ChannelRequest
  property_count: 2
  slug: transcriptapi-com-channel-request
- name: PlaylistRequest
  property_count: 2
  slug: transcriptapi-com-playlist-request
- name: PlaylistVideosResponse
  property_count: 4
  slug: transcriptapi-com-playlist-videos-response
- name: SearchResponse
  property_count: 4
  slug: transcriptapi-com-search-response
- name: SubscribeRequest
  property_count: 2
  slug: transcriptapi-com-subscribe-request
- name: SummarizeRequest
  property_count: 2
  slug: transcriptapi-com-summarize-request
- name: TranscriptRequest
  property_count: 3
  slug: transcriptapi-com-transcript-request
- name: TranslateRequest
  property_count: 3
  slug: transcriptapi-com-translate-request
jsonld:
- class_count: 42
  name: Transcriptapi Com Context
  property_count: 106
  slug: transcriptapi-com-context
layout: provider
modified: '2026-10-31'
name: transcriptapi-com
nav: Providers
network: true
overview: 'transcriptapi-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including YouTube channel API, YouTube playlist API, YouTube search API, and 2 more. Tagged areas include Transcripts, YouTube API, Search, and Content Extraction.


  The transcriptapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  transcriptapi-com''s developer surface includes authentication, API reference, documentation, engineering blog, pricing, getting-started guide, signup flow, and 17 more developer resources.'
plans:
- name: Transcriptapi Com Plans Pricing
  plan_count: 0
  slug: transcriptapi-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Transcriptapi Com Rate Limits
  slug: transcriptapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: transcriptapi-com API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: transcriptapi-com-rules
scopes:
- name: Transcriptapi Com Scopes
  scope_count: 0
  slug: transcriptapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 65.4
    developer_ergonomics: 29.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 41.7
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/transcriptapi-com/transcriptapi-com-2026-11-03T145025.png
security:
- kind: authentication
  name: Transcriptapi Com Authentication
  slug: transcriptapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Transcriptapi Com Domain Security
  slug: transcriptapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-transcript
  slug: transcriptapi-com-get-transcript
slug: transcriptapi-com
tags:
- Transcripts
- YouTube API
- Search
- Content Extraction
website: https://transcriptapi.com/
---
