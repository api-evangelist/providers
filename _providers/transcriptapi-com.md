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
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Transcriptapi Com Agentic Access
  operation_count: 14
  slug: transcriptapi-com-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The auth API from transcriptapi-com — 1 operation(s) for auth.
  name: transcriptapi-com Auth API
  slug: transcriptapi-com-auth-api
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The Channels API from transcriptapi-com — 2 operation(s) for channels.
  name: transcriptapi-com Channels API
  slug: transcriptapi-com-channels-api
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The Health API from transcriptapi-com — 1 operation(s) for health.
  name: transcriptapi-com Health API
  slug: transcriptapi-com-health-api
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The Playlists API from transcriptapi-com — 1 operation(s) for playlists.
  name: transcriptapi-com Playlists API
  slug: transcriptapi-com-playlists-api
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The Public tools API from transcriptapi-com — 5 operation(s) for public tools.
  name: transcriptapi-com Public tools API
  slug: transcriptapi-com-public-tools-api
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The Search API from transcriptapi-com — 1 operation(s) for search.
  name: transcriptapi-com Search API
  slug: transcriptapi-com-search-api
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The Transcripts API from transcriptapi-com — 1 operation(s) for transcripts.
  name: transcriptapi-com Transcripts API
  slug: transcriptapi-com-transcripts-api
- baseURL: https://transcriptapi.com/api/v2/
  baseurl_source: declared
  description: The Webhooks API from transcriptapi-com — 1 operation(s) for webhooks.
  name: transcriptapi-com Webhooks API
  slug: transcriptapi-com-webhooks-api
artifact_total: 23
common:
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
- group: agent
  href: https://artifacts.apis.io/transcriptapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/transcriptapi-com/data-model/transcriptapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transcriptapi-com-data-model.yml
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
- group: start
  title: ''
  type: Login
  url: https://transcriptapi.com/login
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
- group: docs
  title: ''
  type: APIReference
  url: https://transcriptapi.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://transcriptapi.com/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://transcriptapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://transcriptapi.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://transcriptapi.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://transcriptapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transcriptapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transcriptapi.com/privacy
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
description: TranscriptAPI provides a RESTful YouTube transcript API with video search, channel browsing, playlist extraction, and MCP integration for AI agents like ChatGPT and Claude. It offers 100 free credits to start, paid plans from $5/month, processes over 15 million transcripts monthly, and includes comprehensive documentation, SDKs, and agent skills for developers.
image: https://transcriptapi.com/brand/youtube-transcript-api-og.png
json_schemas:
- name: ChannelRequest
  property_count: 2
  slug: transcriptapi-com-channel-request
- name: PlaylistRequest
  property_count: 2
  slug: transcriptapi-com-playlist-request
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
- class_count: 8
  name: Transcriptapi Com Context
  property_count: 13
  slug: transcriptapi-com-context
layout: provider
modified: '2026-10-31'
name: transcriptapi-com
nav: Providers
network: true
overview: 'transcriptapi-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Channels API, Health API, and 5 more. Tagged areas include YouTube, Transcripts, Video, API, and AI.


  The transcriptapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  transcriptapi-com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 18 more developer resources.'
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
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: transcriptapi-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: transcriptapi-com-rules
scopes:
- name: Transcriptapi Com Scopes
  scope_count: 0
  slug: transcriptapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 50.9
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Transcriptapi Com Authentication
  slug: transcriptapi-com-authentication
  summary_line: 0 schemes
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
- YouTube
- Transcripts
- Video
- API
- AI
website: https://transcriptapi.com/
---
