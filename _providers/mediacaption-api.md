---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.mediacaption.io/v1
  baseurl_source: declared
  description: Authenticated account credit balance endpoints.
  name: MediaCaption API Balance API
  slug: mediacaption-api-balance-api
- baseURL: https://api.mediacaption.io/v1
  baseurl_source: declared
  description: Async job status and item result endpoints.
  name: MediaCaption API Jobs API
  slug: mediacaption-api-jobs-api
- baseURL: https://api.mediacaption.io/v1
  baseurl_source: declared
  description: Retained transcript lookup endpoints.
  name: MediaCaption API Transcriptions API
  slug: mediacaption-api-transcriptions-api
- baseURL: https://api.mediacaption.io/v1
  baseurl_source: declared
  description: Synchronous and async public YouTube transcript endpoints.
  name: MediaCaption API Transcripts API
  slug: mediacaption-api-transcripts-api
- baseURL: https://api.mediacaption.io/v1
  baseurl_source: declared
  description: Multipart media upload and AI transcription endpoints.
  name: MediaCaption API Uploads API
  slug: mediacaption-api-uploads-api
- baseURL: https://api.mediacaption.io/v1
  baseurl_source: declared
  description: Authenticated account endpoints.
  name: MediaCaption API User API
  slug: mediacaption-api-user-api
- baseURL: https://api.mediacaption.io/v1
  baseurl_source: declared
  description: Job-level webhook event contracts.
  name: MediaCaption API Webhooks API
  slug: mediacaption-api-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Mediacaption Api Webhooks
  slug: mediacaption-api-webhooks
common:
- group: other
  href: https://artifacts.apis.io/mediacaption-api/overlays/mediacaption-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediacaption-api-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://mediacaption.io
- group: auth
  href: https://artifacts.apis.io/mediacaption-api/security/mediacaption-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mediacaption-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mediacaption-api/authentication/mediacaption-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mediacaption-api-authentication.yml
- group: agent
  href: https://artifacts.apis.io/mediacaption-api/well-known/mediacaption-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mediacaption-api-well-known.yml
- group: design
  href: https://artifacts.apis.io/mediacaption-api/asyncapi/mediacaption-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mediacaption-api-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/mediacaption-api/mcp/mediacaption-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mediacaption-api-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mediacaption-api/llms/mediacaption-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mediacaption-api-llms.txt
- group: design
  href: https://artifacts.apis.io/mediacaption-api/conformance/mediacaption-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mediacaption-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/mediacaption-api/errors/mediacaption-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mediacaption-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mediacaption-api/lifecycle/mediacaption-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mediacaption-api-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mediacaption-api/changelog/mediacaption-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mediacaption-api-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mediacaption.io/docs/changelog
- group: design
  href: https://artifacts.apis.io/mediacaption-api/conventions/mediacaption-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mediacaption-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/mediacaption-api/data-model/mediacaption-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mediacaption-api-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/mediacaption-api/plans/mediacaption-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mediacaption-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mediacaption-api/rate-limits/mediacaption-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mediacaption-api-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/mediacaption-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mediacaption.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.mediacaption.io/report
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mediacaption.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mediacaption.io/privacy
created: '2026-07-18'
description: A credit-billed REST API for retrieving public YouTube transcripts, with single and bulk transcript jobs, job-level webhooks, and AI transcription/translation capabilities. Backed by a public OpenAPI 3.1 contract with bearer/X-API-Key authentication.
finops:
- has_sources: true
  method: derived
  name: Mediacaption Api Finops
  primary_unit: credit pack
  service_category: ''
  slug: mediacaption-api-finops
  template: false
image: https://www.mediacaption.io/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: Media Caption ships no MCP server — no hosted endpoint, no stdio package, no MCP mention anywhere in the docs, and a web search finds only unaffiliated third-party YouTube-caption servers. This is a c
  name: MediaCaption API MCP Server
  slug: mediacaption-api-mcp-yml
modified: '2026-09-03'
name: MediaCaption API
nav: Providers
network: true
overview: 'MediaCaption API publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Jobs API, Transcriptions API, and 4 more. Tagged areas include YouTube, Transcription, Captions, Subtitles, and Video.


  The MediaCaption API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  MediaCaption API''s developer surface includes authentication, changelog, pricing, support, and 18 more developer resources.'
plans:
- name: Mediacaption Api Plans Pricing
  plan_count: 5
  slug: mediacaption-api-plans-pricing
- name: Mediacaption Api Price Estimates
  plan_count: 0
  slug: mediacaption-api-price-estimates
random_paper: 13
rate_limits:
- limit_count: 4
  name: Mediacaption Api Rate Limits
  slug: mediacaption-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: MediaCaption API API Rules
  rule_count: 68
  severity_counts:
    error: 65
    hint: 0
    info: 2
    warn: 1
  slug: mediacaption-api-rules
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 62.3
    developer_ergonomics: 47.0
    discoverability: 60.7
    operational_transparency: 55.3
  previous_composite: 56.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 85.7
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/mediacaption-api/mediacaption-api-2026-08-07T172332.png
security:
- kind: authentication
  name: Mediacaption Api Authentication
  slug: mediacaption-api-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mediacaption Api Domain Security
  slug: mediacaption-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: bulk-transcripts
  slug: mediacaption-api-bulk-transcripts
- name: fetch-youtube-transcript
  slug: mediacaption-api-fetch-youtube-transcript
- name: upload-and-transcribe
  slug: mediacaption-api-upload-and-transcribe
slug: mediacaption-api
tags:
- YouTube
- Transcription
- Captions
- Subtitles
- Video
- REST
- OpenAPI
- Webhook
- Speech-to-Text
- Media
- Developer Tools
website: https://mediacaption.io
---
