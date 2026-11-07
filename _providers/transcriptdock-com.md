---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 2
  name: Transcriptdock Com Agentic Access
  operation_count: 42
  slug: transcriptdock-com-agentic-access
  summary_line: 42 operations · 24 acting · 2 human-in-the-loop
api_count: 13
apis:
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The App API from transcriptdock-com — 1 operation(s) for app.
  name: transcriptdock-com App API
  slug: transcriptdock-com-app-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Batches API from transcriptdock-com — 2 operation(s) for batches.
  name: transcriptdock-com Batches API
  slug: transcriptdock-com-batches-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Capabilities API from transcriptdock-com — 1 operation(s) for capabilities.
  name: transcriptdock-com Capabilities API
  slug: transcriptdock-com-capabilities-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Jobs API from transcriptdock-com — 4 operation(s) for jobs.
  name: transcriptdock-com Jobs API
  slug: transcriptdock-com-jobs-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Language Discoveries API from transcriptdock-com — 2 operation(s) for language discoveries.
  name: transcriptdock-com Language Discoveries API
  slug: transcriptdock-com-language-discoveries-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Llms API from transcriptdock-com — 1 operation(s) for llms.
  name: transcriptdock-com Llms API
  slug: transcriptdock-com-llms-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Llms Full API from transcriptdock-com — 1 operation(s) for llms full.
  name: transcriptdock-com Llms Full API
  slug: transcriptdock-com-llms-full-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Transcripts API from transcriptdock-com — 1 operation(s) for transcripts.
  name: transcriptdock-com Transcripts API
  slug: transcriptdock-com-transcripts-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Uploads API from transcriptdock-com — 2 operation(s) for uploads.
  name: transcriptdock-com Uploads API
  slug: transcriptdock-com-uploads-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Usage API from transcriptdock-com — 1 operation(s) for usage.
  name: transcriptdock-com Usage API
  slug: transcriptdock-com-usage-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Video Discoveries API from transcriptdock-com — 2 operation(s) for video discoveries.
  name: transcriptdock-com Video Discoveries API
  slug: transcriptdock-com-video-discoveries-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Webhook Endpoints API from transcriptdock-com — 2 operation(s) for webhook endpoints.
  name: transcriptdock-com Webhook Endpoints API
  slug: transcriptdock-com-webhook-endpoints-api
- baseURL: https://transcriptdock.com
  baseurl_source: declared
  description: The Webhooks API from transcriptdock-com — 1 operation(s) for webhooks.
  name: transcriptdock-com Webhooks API
  slug: transcriptdock-com-webhooks-api
artifact_total: 39
common:
- group: auth
  href: https://artifacts.apis.io/transcriptdock-com/well-known/transcriptdock-com-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/transcriptdock-com-www-security.txt
- group: agent
  href: https://artifacts.apis.io/transcriptdock-com/agentic-access/transcriptdock-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transcriptdock-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/transcriptdock-com/rate-limits/transcriptdock-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/transcriptdock-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/transcriptdock-com/plans/transcriptdock-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/transcriptdock-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/transcriptdock-com/rules/transcriptdock-com-rules.yml
  title: ''
  type: Spectral
  url: rules/transcriptdock-com-rules.yml
- group: design
  href: https://artifacts.apis.io/transcriptdock-com/json-ld/transcriptdock-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/transcriptdock-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/transcriptdock-com/vocabulary/transcriptdock-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/transcriptdock-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/transcriptdock-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/transcriptdock-com/data-model/transcriptdock-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transcriptdock-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/transcriptdock-com/changelog/transcriptdock-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/transcriptdock-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/transcriptdock-com/conventions/transcriptdock-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/transcriptdock-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/transcriptdock-com/conventions/transcriptdock-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/transcriptdock-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.transcriptdock.com/docs/contact
- group: auth
  href: https://artifacts.apis.io/transcriptdock-com/authentication/transcriptdock-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transcriptdock-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/transcriptdock-com/conformance/transcriptdock-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transcriptdock-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/transcriptdock-com/llms/transcriptdock-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/transcriptdock-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/transcriptdock-com/well-known/transcriptdock-com-transcriptdock-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/transcriptdock-com-transcriptdock-security.txt
- group: auth
  href: https://artifacts.apis.io/transcriptdock-com/well-known/transcriptdock-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/transcriptdock-com-security.txt
- group: agent
  href: https://artifacts.apis.io/transcriptdock-com/well-known/transcriptdock-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/transcriptdock-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/transcriptdock-com/hosts/transcriptdock-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transcriptdock-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/transcriptdock-com/vendors/transcriptdock-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transcriptdock-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/transcriptdock-com/packages/transcriptdock-com-packages.yml
  title: ''
  type: SDKs
  url: packages/transcriptdock-com-packages.yml
- group: build
  href: https://artifacts.apis.io/transcriptdock-com/packages/transcriptdock-com-packages.yml
  title: ''
  type: Packages
  url: packages/transcriptdock-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.transcriptdock.com/docs/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://www.transcriptdock.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.transcriptdock.com/docs/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.transcriptdock.com/dashboard/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.transcriptdock.com/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://www.transcriptdock.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.transcriptdock.com/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TranscriptDock
- group: auth
  href: https://artifacts.apis.io/transcriptdock-com/security/transcriptdock-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/transcriptdock-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/transcriptdock-com/security/transcriptdock-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transcriptdock-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transcriptdock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.transcriptdock.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.transcriptdock.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.transcriptdock.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.transcriptdock.com/login
created: '2026-10-31'
description: Transcript Dock provides a public Video Transcript API for YouTube and TikTok, allowing developers to extract video captions with precise segment timing. The API returns captions in JSON, SRT, VTT, or plain text formats, and offers 50 free credits per month for testing. It aims to simplify integration of video transcripts into applications.
image: https://www.transcriptdock.com/og.jpg
json_schemas:
- name: GetV1CapabilitiesResponse
  property_count: 16
  slug: transcriptdock-com-get-v1-capabilities-response
- name: GetV1JobsIdResponse
  property_count: 9
  slug: transcriptdock-com-get-v1-jobs-id-response
- name: GetV1JobsResponse
  property_count: 9
  slug: transcriptdock-com-get-v1-jobs-response
- name: GetV1TranscriptsIdResponse
  property_count: 12
  slug: transcriptdock-com-get-v1-transcripts-id-response
- name: GetV1UsageResponse
  property_count: 9
  slug: transcriptdock-com-get-v1-usage-response
- name: GetV1VideoDiscoveriesIdResponse
  property_count: 11
  slug: transcriptdock-com-get-v1-video-discoveries-id-response
- name: PostV1BatchesRequest
  property_count: 3
  slug: transcriptdock-com-post-v1-batches-request
- name: PostV1JobsIdCancelResponse
  property_count: 9
  slug: transcriptdock-com-post-v1-jobs-id-cancel-response
- name: PostV1JobsIdRetryResponse
  property_count: 9
  slug: transcriptdock-com-post-v1-jobs-id-retry-response
- name: PostV1VideoDiscoveriesRequest
  property_count: 8
  slug: transcriptdock-com-post-v1-video-discoveries-request
- name: PostV1VideoDiscoveriesResponse
  property_count: 11
  slug: transcriptdock-com-post-v1-video-discoveries-response
jsonld:
- class_count: 27
  name: Transcriptdock Com Context
  property_count: 70
  slug: transcriptdock-com-context
layout: provider
modified: '2026-10-31'
name: transcriptdock-com
nav: Providers
network: true
overview: 'transcriptdock-com is listed with 13 APIs on the [APIs.io](https://apis.io/) network, including App API, Batches API, Capabilities API, and 10 more. Tagged areas include Company, Video, Transcript, YouTube, and TikTok.


  The transcriptdock-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  transcriptdock-com''s developer surface includes changelog, authentication, API reference, getting-started guide, documentation, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Transcriptdock Com Plans Pricing
  plan_count: 4
  slug: transcriptdock-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Transcriptdock Com Rate Limits
  slug: transcriptdock-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: transcriptdock-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: transcriptdock-com-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 44.5
    discoverability: 71.4
    operational_transparency: 55.3
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 93.8
      derived: 14
      marker_coverage: 87.5
      total: 16
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/transcriptdock-com/transcriptdock-com-2026-11-03T145031.png
security:
- kind: authentication
  name: Transcriptdock Com Authentication
  slug: transcriptdock-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Transcriptdock Com Domain Security
  slug: transcriptdock-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transcriptdock Com Vulnerability Disclosure
  slug: transcriptdock-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 7
skills:
- name: create-batch
  slug: create-batch
- name: create-job
  slug: create-job
- name: export-transcript
  slug: export-transcript
- name: get-batch
  slug: get-batch
- name: get-job
  slug: get-job
- name: get-transcript
  slug: get-transcript
- name: get-capabilities
  slug: transcriptdock-com-getCapabilities
slug: transcriptdock-com
tags:
- Company
- Video
- Transcript
- YouTube
- TikTok
website: https://transcriptdock.com/
---
