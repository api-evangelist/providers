---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-09-16'
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
artifact_total: 13
asyncapis:
- description: ''
  name: Mediacaption Api Webhooks
  slug: mediacaption-api-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/overlays/mediacaption-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediacaption-api-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://mediacaption.io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/security/mediacaption-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mediacaption-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/authentication/mediacaption-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mediacaption-api-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/well-known/mediacaption-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mediacaption-api-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/asyncapi/mediacaption-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mediacaption-api-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/mcp/mediacaption-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mediacaption-api-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/llms/mediacaption-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mediacaption-api-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/conformance/mediacaption-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mediacaption-api-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/errors/mediacaption-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mediacaption-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/lifecycle/mediacaption-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mediacaption-api-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/changelog/mediacaption-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mediacaption-api-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mediacaption.io/docs/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/conventions/mediacaption-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mediacaption-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/data-model/mediacaption-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mediacaption-api-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/plans/mediacaption-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mediacaption-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/rate-limits/mediacaption-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mediacaption-api-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/skills/_index.yml
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
image: https://www.mediacaption.io/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: Media Caption ships no MCP server — no hosted endpoint, no stdio package, no MCP mention anywhere in the docs, and a web search finds only unaffiliated third-party YouTube-caption servers. This is a c
  name: MediaCaption API MCP Server
  slug: mediacaption-api-mcp-server
modified: '2026-09-03'
name: MediaCaption API
nav: Providers
network: true
overview: 'MediaCaption API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Jobs API, Transcriptions API, and 4 more. Tagged areas include YouTube, Transcription, Captions, Subtitles, and Video.


  The MediaCaption API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MediaCaption API''s developer surface includes authentication, changelog, pricing, support, and 18 more developer resources.'
plans:
- name: Mediacaption Api Plans Pricing
  plan_count: 2
  slug: mediacaption-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Mediacaption Api Rate Limits
  slug: mediacaption-api-rate-limits
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.0
    catalog_earned_first_party: 20.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 63.7
    developer_ergonomics: 47.0
    discoverability: 63.0
    operational_transparency: 55.3
  previous_composite: 48.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/mediacaption-api/refs/heads/main/screenshots/mediacaption-api-2026-08-07T172332.png
security:
- kind: authentication
  name: Mediacaption Api Authentication
  slug: mediacaption-api-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mediacaption Api Domain Security
  slug: mediacaption-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
