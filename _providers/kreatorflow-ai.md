---
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Kreatorflow Ai Agentic Access
  operation_count: 44
  slug: kreatorflow-ai-agentic-access
  summary_line: 44 operations · 28 acting
api_count: 1
apis:
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The Audio API from kreatorflow-ai — 2 operation(s) for audio.
  name: kreatorflow-ai Audio API
  slug: kreatorflow-ai-audio-api
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The Images API from kreatorflow-ai — 3 operation(s) for images.
  name: kreatorflow-ai Images API
  slug: kreatorflow-ai-images-api
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The Jobs API from kreatorflow-ai — 2 operation(s) for jobs.
  name: kreatorflow-ai Jobs API
  slug: kreatorflow-ai-jobs-api
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The Lip Sync API from kreatorflow-ai — 1 operation(s) for lip sync.
  name: kreatorflow-ai Lip Sync API
  slug: kreatorflow-ai-lip-sync-api
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The MCP API from kreatorflow-ai — 1 operation(s) for mcp.
  name: kreatorflow-ai MCP API
  slug: kreatorflow-ai-mcp-api
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The Models API from kreatorflow-ai — 1 operation(s) for models.
  name: kreatorflow-ai Models API
  slug: kreatorflow-ai-models-api
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The Uploads API from kreatorflow-ai — 4 operation(s) for uploads.
  name: kreatorflow-ai Uploads API
  slug: kreatorflow-ai-uploads-api
- baseURL: https://kreatorflow.ai
  baseurl_source: declared
  description: The Video API from kreatorflow-ai — 4 operation(s) for video.
  name: kreatorflow-ai Video API
  slug: kreatorflow-ai-video-api
artifact_total: 22
asyncapis:
- description: ''
  name: Kreatorflow Ai Webhooks
  slug: kreatorflow-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/kreatorflow-ai/agentic-access/kreatorflow-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kreatorflow-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/kreatorflow-ai/rate-limits/kreatorflow-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kreatorflow-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/rules/kreatorflow-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/kreatorflow-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/json-ld/kreatorflow-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kreatorflow-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/vocabulary/kreatorflow-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kreatorflow-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/asyncapi/kreatorflow-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/kreatorflow-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/data-model/kreatorflow-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kreatorflow-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/conventions/kreatorflow-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kreatorflow-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/conventions/kreatorflow-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kreatorflow-ai-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://kreatorflow.ai/acceptable-use
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/errors/kreatorflow-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kreatorflow-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kreatorflow-ai/conformance/kreatorflow-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kreatorflow-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kreatorflow-ai/llms/kreatorflow-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kreatorflow-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/kreatorflow-ai/well-known/kreatorflow-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kreatorflow-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/kreatorflow-ai/well-known/kreatorflow-ai-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kreatorflow-ai-developers-security.txt
- group: agent
  href: https://artifacts.apis.io/kreatorflow-ai/well-known/kreatorflow-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kreatorflow-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/kreatorflow-ai/hosts/kreatorflow-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kreatorflow-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/kreatorflow-ai/vendors/kreatorflow-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kreatorflow-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://kreatorflow.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kreatorflow.ai\
- group: auth
  href: https://artifacts.apis.io/kreatorflow-ai/authentication/kreatorflow-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kreatorflow-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/kreatorflow-ai/security/kreatorflow-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kreatorflow-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kreatorflow-ai/security/kreatorflow-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kreatorflow-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kreatorflow.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://kreatorflow.ai/developers
- group: docs
  title: ''
  type: APIReference
  url: https://kreatorflow.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://kreatorflow.ai/developers
- group: operate
  title: ''
  type: Support
  url: https://kreatorflow.ai/support/developer-api
- group: company
  title: ''
  type: Blog
  url: https://kreatorflow.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kreatorflow.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kreatorflow.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kreatorflow.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://kreatorflow.ai/openapi.json
  - status: null
    url: https://developers.kreatorflow.ai/openapi.json
  - status: 401
    url: https://kreatorflow.ai/api/mcp
  - status: 401
    url: https://developers.kreatorflow.ai/api/mcp
  - status: 200
    url: https://kreatorflow.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: KreatorFlow is an AI-powered platform that enables users to generate, edit, and enhance video, image, and voice content using BytePlus-powered models. It offers a suite of creative tools such as Seedance video generation, Seedream image creation, and TTS voice synthesis, all accessible via a unified REST API. Users can start for free with 25 credits, and the service provides flexible pricing, token‑based billing, and signed webhooks for integration. The platform also supports MCP connections to AI assistants like Claude and ChatGPT, positioning KreatorFlow as a comprehensive solution for AI‑driven media production.
image: https://kreatorflow.ai/brand/kreatorflow-share-v5.jpg
json_schemas:
- name: AudioRequest
  property_count: 14
  slug: kreatorflow-ai-audio-request
- name: CharacterRequest
  property_count: 16
  slug: kreatorflow-ai-character-request
- name: ImageRequest
  property_count: 16
  slug: kreatorflow-ai-image-request
- name: VideoEditRequest
  property_count: 23
  slug: kreatorflow-ai-video-edit-request
- name: VideoRequest
  property_count: 41
  slug: kreatorflow-ai-video-request
- name: VideoToolRequest
  property_count: 11
  slug: kreatorflow-ai-video-tool-request
jsonld:
- class_count: 18
  name: Kreatorflow Ai Context
  property_count: 109
  slug: kreatorflow-ai-context
layout: provider
modified: '2026-10-30'
name: kreatorflow-ai
nav: Providers
network: true
overview: 'kreatorflow-ai publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Images API, Jobs API, and 5 more. Tagged areas include AI, Video, Image, Voice, and API.


  The kreatorflow-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  kreatorflow-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 21
  name: Kreatorflow Ai Rate Limits
  slug: kreatorflow-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: kreatorflow-ai API Rules
  rule_count: 18
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 3
  slug: kreatorflow-ai-rules
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 72.8
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kreatorflow Ai Authentication
  slug: kreatorflow-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kreatorflow Ai Domain Security
  slug: kreatorflow-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kreatorflow Ai Vulnerability Disclosure
  slug: kreatorflow-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kreatorflow-ai
tags:
- AI
- Video
- Image
- Voice
- API
- Platform
website: https://kreatorflow.ai/
---
