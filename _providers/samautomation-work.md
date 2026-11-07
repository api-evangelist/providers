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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Unified AI video + image API with X-API-Key authentication; list models, create jobs, poll status, and retrieve media URLs.
  name: AI generation API
  slug: ai-generation-api
- description: 'samautomation-work API as documented publicly: 35 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: samautomation-work API
  slug: samautomation-work-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/samautomation-work/rate-limits/samautomation-work-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/samautomation-work-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/samautomation-work/plans/samautomation-work-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/samautomation-work-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/samautomation-work/rules/samautomation-work-rules.yml
  title: ''
  type: Spectral
  url: rules/samautomation-work-rules.yml
- group: design
  href: https://artifacts.apis.io/samautomation-work/json-ld/samautomation-work-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/samautomation-work-context.jsonld
- group: design
  href: https://artifacts.apis.io/samautomation-work/vocabulary/samautomation-work-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/samautomation-work-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/samautomation-work/data-model/samautomation-work-data-model.yml
  title: ''
  type: DataModel
  url: data-model/samautomation-work-data-model.yml
- group: operate
  href: https://artifacts.apis.io/samautomation-work/changelog/samautomation-work-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/samautomation-work-changelog.yml
- group: auth
  href: https://artifacts.apis.io/samautomation-work/authentication/samautomation-work-authentication.yml
  title: ''
  type: Authentication
  url: authentication/samautomation-work-authentication.yml
- group: design
  href: https://artifacts.apis.io/samautomation-work/errors/samautomation-work-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/samautomation-work-problem-types.yml
- group: design
  href: https://artifacts.apis.io/samautomation-work/conformance/samautomation-work-conformance.yml
  title: ''
  type: Conformance
  url: conformance/samautomation-work-conformance.yml
- group: agent
  href: https://artifacts.apis.io/samautomation-work/well-known/samautomation-work-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/samautomation-work-well-known.yml
- group: other
  href: https://artifacts.apis.io/samautomation-work/hosts/samautomation-work-hosts.yml
  title: ''
  type: Hosts
  url: hosts/samautomation-work-hosts.yml
- group: other
  href: https://artifacts.apis.io/samautomation-work/vendors/samautomation-work-vendors.yml
  title: ''
  type: Vendors
  url: vendors/samautomation-work-vendors.yml
- group: build
  href: https://artifacts.apis.io/samautomation-work/packages/samautomation-work-packages.yml
  title: ''
  type: SDKs
  url: packages/samautomation-work-packages.yml
- group: build
  href: https://artifacts.apis.io/samautomation-work/packages/samautomation-work-packages.yml
  title: ''
  type: Packages
  url: packages/samautomation-work-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://samautomation.work/changelog/
- group: auth
  href: https://artifacts.apis.io/samautomation-work/security/samautomation-work-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samautomation-work-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://samautomation.work/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://samautomation.work/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://samautomation.work/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://samautomation.work/api/ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://samautomation.work/docs/
- group: company
  title: ''
  type: Blog
  url: https://samautomation.work/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://samautomation.work/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://samautomation.work/subscriptions/plans/
- group: start
  title: ''
  type: SignUp
  url: https://samautomation.work/register/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://samautomation.work/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://samautomation.work/privacy/
coverage:
  checked: '2026-10-31'
  detail: API documentation lists a Base URL but no OpenAPI/Swagger/GraphQL spec was found (404 on common spec URLs).
  evidence:
  - status: 404
    url: https://samautomation.work/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: SamAutomation provides a JSON-to-video and AI video API that transforms structured JSON payloads into fully rendered MP4 videos. The platform offers mix, simple, and loop video generation, AI-powered video creation, auto-captioning in multiple languages, and a suite of tools for developers to integrate video automation into apps, workflows, and no‑code platforms.
image: https://jsontwovideo.s3.eu-west-3.amazonaws.com/blog/images/preview+image.jpg
json_schemas:
- name: PostApiAiGenerateRequest
  property_count: 7
  slug: samautomation-work-post-api-ai-generate-request
- name: PostApiAutocaptionsProcessRequest
  property_count: 5
  slug: samautomation-work-post-api-autocaptions-process-request
- name: PostApiFunctionVideoGenerationSimpleVideoRequest
  property_count: 2
  slug: samautomation-work-post-api-function-video-generation-simple-video-request
- name: PostRenderAdvancedVideoRequest
  property_count: 5
  slug: samautomation-work-post-render-advanced-video-request
- name: PostVideoGenerationLoopVideoRequest
  property_count: 6
  slug: samautomation-work-post-video-generation-loop-video-request
- name: PostVideoGenerationMixVideoRequest
  property_count: 5
  slug: samautomation-work-post-video-generation-mix-video-request
jsonld:
- class_count: 26
  name: Samautomation Work Context
  property_count: 46
  slug: samautomation-work-context
layout: provider
modified: '2026-10-31'
name: samautomation-work
nav: Providers
network: true
overview: 'samautomation-work is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Artificial Intelligence, JSON, Automation, and Media.


  The samautomation-work catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  samautomation-work''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Samautomation Work Plans Pricing
  plan_count: 3
  slug: samautomation-work-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Samautomation Work Rate Limits
  slug: samautomation-work-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: samautomation-work API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: samautomation-work-rules
scopes:
- name: Samautomation Work Scopes
  scope_count: 0
  slug: samautomation-work-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 39.3
    discoverability: 57.1
    operational_transparency: 42.1
  previous_composite: 51.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/samautomation-work/samautomation-work-2026-11-03T142652.png
security:
- kind: authentication
  name: Samautomation Work Authentication
  slug: samautomation-work-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Samautomation Work Domain Security
  slug: samautomation-work-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: samautomation-work
tags:
- Video
- Artificial Intelligence
- JSON
- Automation
- Media
website: https://samautomation.work/
---
