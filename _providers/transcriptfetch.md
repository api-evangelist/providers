---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://transcriptfetch.com
  baseurl_source: spec
  description: Service health and metadata
  name: TranscriptFetch System API
  phrasing_intents:
  - id: me
    intent: Check API key and credit balance (v1)
    question: Is my API key valid on the older v1 Transcriptfetch endpoint?
  - id: healthCheck
    intent: Check that the v1 API is up
    question: Is the v1 transcript API currently serving requests?
  - id: getApiV2Me
    intent: Check API key and credit balance (v2)
    question: How many transcript credits does my account have left on v2?
  - id: getApiV2Health
    intent: Check that the v2 API is up
    question: Is the v2 API healthy right now?
  phrasing_ops: 4
  slug: transcriptfetch-system-api
- baseURL: https://transcriptfetch.com
  baseurl_source: spec
  description: Transcript and video-list endpoints
  name: TranscriptFetch Transcripts API
  phrasing_intents:
  - id: fetchVideoTranscript
    intent: Get a transcript for one video (v1)
    question: How do I get the transcript of a YouTube video with the v1 endpoint?
  - id: fetchChannelVideos
    intent: List a YouTube channel's videos (v1)
    question: What are the newest uploads on a YouTube channel, using the v1 channel listing?
  - id: fetchPlaylistVideos
    intent: List a YouTube playlist's videos (v1)
    question: Which videos are in a YouTube playlist, using the older v1 playlist endpoint?
  - id: searchVideos
    intent: Search YouTube videos by keyword (v1)
    question: Can I search YouTube by keyword with the v1 search endpoint?
  - id: getTranscriptJob
    intent: Check an audio-transcription job (v1)
    question: Is my v1 audio transcription job still processing or completed?
  - id: fetchTranscriptsBatch
    intent: Fetch many transcripts at once (v1)
    question: How many videos can I transcribe in a single v1 batch request on my plan?
  - id: postApiV2TranscriptsVideo
    intent: Get a transcript for a video or podcast (v2)
    question: How do I transcribe a Spotify or Apple Podcasts episode with v2?
  - id: postApiV2TranscriptsChannel
    intent: List a channel, profile, show or feed's items (v2)
    question: Can I list the latest episodes of a podcast show or RSS feed with v2?
  phrasing_ops: 12
  slug: transcriptfetch-transcripts-api
artifact_total: 17
asyncapis:
- description: ''
  name: Transcriptfetch Webhooks
  slug: transcriptfetch-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://transcriptfetch.com/changelog/rss.xml
- group: other
  href: https://artifacts.apis.io/transcriptfetch/overlays/transcriptfetch-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/transcriptfetch-api-v2-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://transcriptfetch.com/mcp
- group: agent
  href: https://artifacts.apis.io/transcriptfetch/mcp/transcriptfetch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/transcriptfetch-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://transcriptfetch.com
- group: auth
  href: https://artifacts.apis.io/transcriptfetch/security/transcriptfetch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/transcriptfetch-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/transcriptfetch/security/transcriptfetch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/transcriptfetch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/transcriptfetch/security/transcriptfetch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transcriptfetch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/transcriptfetch/authentication/transcriptfetch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transcriptfetch-authentication.yml
- group: auth
  href: https://artifacts.apis.io/transcriptfetch/security/transcriptfetch-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/transcriptfetch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/transcriptfetch/well-known/transcriptfetch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/transcriptfetch-security.txt
- group: agent
  href: https://artifacts.apis.io/transcriptfetch/well-known/transcriptfetch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/transcriptfetch-well-known.yml
- group: build
  href: https://artifacts.apis.io/transcriptfetch/packages/transcriptfetch-packages.yml
  title: ''
  type: Packages
  url: packages/transcriptfetch-packages.yml
- group: build
  href: https://artifacts.apis.io/transcriptfetch/packages/transcriptfetch-packages.yml
  title: ''
  type: SDKs
  url: packages/transcriptfetch-packages.yml
- group: design
  href: https://artifacts.apis.io/transcriptfetch/conformance/transcriptfetch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transcriptfetch-conformance.yml
- group: design
  href: https://artifacts.apis.io/transcriptfetch/errors/transcriptfetch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/transcriptfetch-problem-types.yml
- group: design
  href: https://artifacts.apis.io/transcriptfetch/lifecycle/transcriptfetch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/transcriptfetch-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.transcriptfetch.com
- group: operate
  title: ''
  type: Deprecation
  url: https://transcriptfetch.com/docs/v1
- group: auth
  href: https://artifacts.apis.io/transcriptfetch/scopes/transcriptfetch-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/transcriptfetch-scopes.yml
- group: design
  href: https://artifacts.apis.io/transcriptfetch/conventions/transcriptfetch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/transcriptfetch-conventions.yml
- group: design
  href: https://artifacts.apis.io/transcriptfetch/conventions/transcriptfetch-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/transcriptfetch-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://transcriptfetch.com/changelog
- group: operate
  href: https://artifacts.apis.io/transcriptfetch/changelog/transcriptfetch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/transcriptfetch-changelog.yml
- group: design
  href: https://artifacts.apis.io/transcriptfetch/data-model/transcriptfetch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transcriptfetch-data-model.yml
- group: design
  href: https://artifacts.apis.io/transcriptfetch/asyncapi/transcriptfetch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/transcriptfetch-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/transcriptfetch/plans/transcriptfetch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/transcriptfetch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/transcriptfetch/rate-limits/transcriptfetch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/transcriptfetch-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/transcriptfetch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://transcriptfetch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://transcriptfetch.com/blog
- group: operate
  title: ''
  type: Support
  url: https://transcriptfetch.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://transcriptfetch.com/help
- group: operate
  title: ''
  type: Roadmap
  url: https://transcriptfetch.com/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://transcriptfetch.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://transcriptfetch.com/legal
- group: start
  title: ''
  type: SignUp
  url: https://transcriptfetch.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://transcriptfetch.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TranscriptFetch
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/transcriptfetch
- group: start
  title: ''
  type: GettingStarted
  url: https://transcriptfetch.com/docs
created: '2026-09-09'
description: Social video & audio to text API for builders. Returns timestamped, structured JSON transcripts for YouTube, TikTok, Instagram, Spotify, Apple Podcasts, and direct media files — captions when available, AI audio transcription as fallback — plus YouTube channel/playlist/search discovery. Delivered via REST and a hosted MCP server for LLM pipelines, RAG, and agents.
finops:
- has_sources: true
  method: derived
  name: Transcriptfetch Finops
  primary_unit: credits
  service_category: ''
  slug: transcriptfetch-finops
  template: false
layout: provider
mcp_servers:
- description: ''
  name: TranscriptFetch MCP Server
  slug: mcp
modified: '2026-10-06'
name: TranscriptFetch
nav: Providers
network: true
overview: 'TranscriptFetch publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: System API and Transcripts API. Tagged areas include Transcripts, Speech-to-Text, Captions, YouTube, and TikTok.


  The TranscriptFetch catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  TranscriptFetch''s developer surface includes authentication, changelog, pricing, engineering blog, support, signup flow, getting-started guide, and 34 more developer resources.'
plans:
- name: Transcriptfetch Plans Pricing
  plan_count: 6
  slug: transcriptfetch-plans-pricing
- name: Transcriptfetch Price Estimates
  plan_count: 0
  slug: transcriptfetch-price-estimates
random_paper: 12
rate_limits:
- limit_count: 5
  name: Transcriptfetch Rate Limits
  slug: transcriptfetch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: TranscriptFetch API Rules
  rule_count: 54
  severity_counts:
    error: 50
    hint: 0
    info: 3
    warn: 1
  slug: transcriptfetch-rules
scopes:
- name: Transcriptfetch Scopes
  scope_count: 6
  slug: transcriptfetch-scopes
  summary_line: 6 scopes
score:
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 61.5
    catalog_earned_first_party: 24.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 60.6
    developer_ergonomics: 58.9
    discoverability: 63.3
    operational_transparency: 89.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/transcriptfetch/transcriptfetch-2026-10-11T131133.png
security:
- kind: authentication
  name: Transcriptfetch Authentication
  slug: transcriptfetch-authentication
  summary_line: http/oauth2 (MCP surface) · 2 schemes
- kind: domain-security
  name: Transcriptfetch Domain Security
  slug: transcriptfetch-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Transcriptfetch Vulnerability Disclosure
  slug: transcriptfetch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Transcriptfetch Trust Center
  slug: transcriptfetch-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: transcriptfetch-batch-transcripts
  slug: transcriptfetch-batch-transcripts
- name: transcriptfetch-get-transcript
  slug: transcriptfetch-get-transcript
- name: transcriptfetch-monitor-channel
  slug: transcriptfetch-monitor-channel
slug: transcriptfetch
tags:
- Transcripts
- Speech-to-Text
- Captions
- YouTube
- TikTok
- Instagram
- Podcasts
- MCP
- Llms.txt
- OpenAPI
- Transcription
- Video
- AI/LLM
- RAG
- Agents
- Developer Tools
- Media
- Content
- Spotify
- Apple Podcasts
website: https://transcriptfetch.com
---
