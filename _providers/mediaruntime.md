---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Mediaruntime Agentic Access
  operation_count: 61
  slug: mediaruntime-agentic-access
  summary_line: 61 operations · 25 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'Submit asynchronous video, audio, and image jobs and receive canonical ZIP bundles through polling or signed terminal webhooks. One of the two products in the provider''s apis.json; its operations are '
  name: MediaRuntime Media API
  slug: media-api
- description: Configure sticker collections, discover enabled Hosted Packs, search stable sticker metadata, and resolve approved short-lived asset delivery URLs. One of the two products in the provider's apis.json;
  name: MediaRuntime Stickers API
  slug: stickers-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Public capability and contract discovery.
  name: MediaRuntime Discovery API
  slug: mediaruntime-discovery-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Redeem completed job output bundles.
  name: MediaRuntime Job Results API
  slug: mediaruntime-job-results-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Create, list, and inspect asynchronous media jobs.
  name: MediaRuntime Jobs API
  slug: mediaruntime-jobs-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Read analysis reports produced by requested presets.
  name: MediaRuntime Media Analysis API
  slug: mediaruntime-media-analysis-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: The four signed terminal webhook events MediaRuntime posts to an account's endpoint (job.completed, job.failed, job.partial, job.rejected); this document has no paths.
  name: MediaRuntime API
  slug: mediaruntime-mediaruntime-api-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Read a job's requested moderation verdict.
  name: MediaRuntime Moderation API
  slug: mediaruntime-moderation-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Manage immutable, account-scoped processing recipes.
  name: MediaRuntime Recipes API
  slug: mediaruntime-recipes-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Create a bounded public-sandbox session.
  name: MediaRuntime Sandbox API
  slug: mediaruntime-sandbox-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Optional upload targets for local media bytes.
  name: MediaRuntime Uploads API
  slug: mediaruntime-uploads-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Configure the account watermark logo.
  name: MediaRuntime Watermarks API
  slug: mediaruntime-watermarks-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Retry delivery of signed terminal events.
  name: MediaRuntime Webhooks API
  slug: mediaruntime-webhooks-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Browse MediaRuntime character packs and their public previews.
  name: MediaRuntime Marketplace API
  slug: mediaruntime-marketplace-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Configure which activated character packs each application exposes.
  name: MediaRuntime Sticker Collections API
  slug: mediaruntime-sticker-collections-api
- baseURL: https://mediaruntime.com
  baseurl_source: spec
  description: Search, inspect, and resolve collection-scoped hosted stickers.
  name: MediaRuntime Sticker Runtime API
  slug: mediaruntime-sticker-runtime-api
artifact_total: 46
asyncapis:
- description: ''
  name: Mediaruntime Webhooks
  slug: mediaruntime-webhooks
common:
- group: start
  title: ''
  type: Sandbox
  url: https://mediaruntime.com/sandbox
- group: agent
  href: https://artifacts.apis.io/mediaruntime/agentic-access/mediaruntime-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mediaruntime-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/rules/mediaruntime-rules.yml
  title: ''
  type: Spectral
  url: rules/mediaruntime-rules.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/json-ld/mediaruntime-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mediaruntime-context.jsonld
- group: design
  href: https://artifacts.apis.io/mediaruntime/vocabulary/mediaruntime-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mediaruntime-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mediaruntime/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/asyncapi/mediaruntime-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mediaruntime-webhooks.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/data-model/mediaruntime-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mediaruntime-data-model.yml
- group: build
  href: https://artifacts.apis.io/mediaruntime/cli/mediaruntime-cli.yml
  title: ''
  type: CLI
  url: cli/mediaruntime-cli.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/conventions/mediaruntime-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mediaruntime-conventions.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/conventions/mediaruntime-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mediaruntime-conventions.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/errors/mediaruntime-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mediaruntime-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mediaruntime/conformance/mediaruntime-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mediaruntime-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mediaruntime/llms/mediaruntime-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mediaruntime-llms.txt
- group: other
  href: https://artifacts.apis.io/mediaruntime/hosts/mediaruntime-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mediaruntime-hosts.yml
- group: other
  href: https://artifacts.apis.io/mediaruntime/vendors/mediaruntime-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mediaruntime-vendors.yml
- group: build
  href: https://artifacts.apis.io/mediaruntime/packages/mediaruntime-packages.yml
  title: ''
  type: SDKs
  url: packages/mediaruntime-packages.yml
- group: build
  href: https://artifacts.apis.io/mediaruntime/packages/mediaruntime-packages.yml
  title: ''
  type: Packages
  url: packages/mediaruntime-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ericel
- group: docs
  title: ''
  type: Documentation
  url: https://mediaruntime.com/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mediaruntime.com/en/docs/
- group: auth
  href: https://artifacts.apis.io/mediaruntime/authentication/mediaruntime-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mediaruntime-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mediaruntime/security/mediaruntime-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mediaruntime-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://mediaruntime.com/en/pricing/
- group: commercial
  href: https://artifacts.apis.io/mediaruntime/plans/mediaruntime-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mediaruntime-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/mediaruntime/capabilities/mediaruntime-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mediaruntime-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://mediaruntime.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mediaruntime.com/docs
- group: agent
  title: ''
  type: LLMsTxt
  url: https://mediaruntime.com/llms.txt
- group: other
  title: ''
  type: APIsJSON
  url: https://mediaruntime.com/apis.json
- group: docs
  title: ''
  type: OpenAPI
  url: https://mediaruntime.com/openapi.json
- group: start
  title: ''
  type: SignUp
  url: https://mediaruntime.com/account?signup=1
- group: start
  title: ''
  type: GettingStarted
  url: https://mediaruntime.com/docs#quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://mediaruntime.com/docs/operations.md
- group: operate
  title: ''
  type: RateLimits
  url: https://mediaruntime.com/docs/operations.md#rate-limits-and-retries
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@mediaruntime/node
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/mediaruntime/
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@mediaruntime/cli
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/ericel/mediaruntime-quickstarts
- group: docs
  title: ''
  type: Docs
  url: https://mediaruntime.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://mediaruntime.com/en/pricing/
- group: company
  title: ''
  type: Blog
  url: https://mediaruntime.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://mediaruntime.com/contact
- group: operate
  title: ''
  type: Support
  url: https://mediaruntime.com/contact
- group: commercial
  title: ''
  type: Legal
  url: https://mediaruntime.com/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mediaruntime.com/legal#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mediaruntime.com/legal#privacy
created: '2026-08-26'
description: MediaRuntime is an asynchronous media-processing API and hosted sticker runtime for server-side applications, served at https://mediaruntime.com/v1. It publishes two products in its apis.json. The Media API takes video, audio and image jobs (POST /v1/jobs) and returns canonical ZIP bundles through polling or signed terminal webhooks, with presets and account-scoped recipes, moderation verdicts, analysis reports, upload targets and watermarks. The Stickers API configures sticker collections, discovers enabled Hosted Packs, searches stable sticker metadata and resolves short-lived approved asset URLs. The OpenAPI 3.1 contract at https://mediaruntime.com/openapi.json describes 33 paths and 41 operations. Server requests authenticate with an X-API-Key workspace key, and a public sandbox session is available. Official tools are the @mediaruntime/node SDK and @mediaruntime/cli on npm, the mediaruntime Python SDK on PyPI, and a GitHub quickstarts repository.
finops:
- has_sources: true
  method: derived
  name: Mediaruntime Finops
  primary_unit: standard processing job/unit
  service_category: ''
  slug: mediaruntime-finops
  template: false
image: https://mediaruntime.com/og-image.png
json_schemas:
- name: ArchivedRecipeResponse
  property_count: 3
  slug: mediaruntime-archived-recipe-response
- name: CapabilitiesResponse
  property_count: 9
  slug: mediaruntime-capabilities-response
- name: CreateJobRequest
  property_count: 8
  slug: mediaruntime-create-job-request
- name: HostedRecipeListResponse
  property_count: 1
  slug: mediaruntime-hosted-recipe-list-response
- name: HostedRecipeResponse
  property_count: 8
  slug: mediaruntime-hosted-recipe-response
- name: JobListResponse
  property_count: 2
  slug: mediaruntime-job-list-response
- name: JobModerationInfo
  property_count: 10
  slug: mediaruntime-job-moderation-info
- name: JobReportResponse
  property_count: 4
  slug: mediaruntime-job-report-response
- name: JobResponse
  property_count: 7
  slug: mediaruntime-job-response
- name: JobStatusResponse
  property_count: 14
  slug: mediaruntime-job-status-response
- name: RecipeCreateRequest
  property_count: 3
  slug: mediaruntime-recipe-create-request
- name: RecipeVersionCreateRequest
  property_count: 3
  slug: mediaruntime-recipe-version-create-request
- name: SandboxSessionResponse
  property_count: 5
  slug: mediaruntime-sandbox-session-response
- name: UploadUrlRequest
  property_count: 2
  slug: mediaruntime-upload-url-request
- name: UploadUrlResponse
  property_count: 3
  slug: mediaruntime-upload-url-response
- name: WatermarkLogoConfirmRequest
  property_count: 4
  slug: mediaruntime-watermark-logo-confirm-request
- name: WatermarkLogoResponse
  property_count: 4
  slug: mediaruntime-watermark-logo-response
- name: WatermarkLogoUploadUrlRequest
  property_count: 1
  slug: mediaruntime-watermark-logo-upload-url-request
- name: WebhookRetryResponse
  property_count: 4
  slug: mediaruntime-webhook-retry-response
jsonld:
- class_count: 105
  name: Mediaruntime Context
  property_count: 302
  slug: mediaruntime-context
layout: provider
modified: '2026-09-16'
name: MediaRuntime
nav: Providers
network: true
overview: 'MediaRuntime publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Media API, Stickers API, Discovery API, and 13 more. Tagged areas include Media Processing, Video, Audio, Runtime, and Video Encoding.


  The MediaRuntime catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  MediaRuntime''s developer surface includes sandbox, CLI, documentation, API reference, authentication, pricing, signup flow, and 40 more developer resources.'
plans:
- name: Mediaruntime Plans Pricing
  plan_count: 3
  slug: mediaruntime-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: MediaRuntime API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 3
  slug: mediaruntime-rules
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 80.2
    developer_ergonomics: 73.2
    discoverability: 64.3
    operational_transparency: 6.6
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 92.9
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mediaruntime/mediaruntime-2026-09-02T150453.png
security:
- kind: authentication
  name: Mediaruntime Authentication
  slug: mediaruntime-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Mediaruntime Domain Security
  slug: mediaruntime-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: mediaruntime-create-and-enable-sticker-collection
  slug: mediaruntime-create-and-enable-sticker-collection
- name: mediaruntime-create-and-retrieve-job
  slug: mediaruntime-create-and-retrieve-job
- name: mediaruntime-fetch-sticker
  slug: mediaruntime-fetch-sticker
slug: mediaruntime
tags:
- Media Processing
- Video
- Audio
- Runtime
- Video Encoding
- Audio Processing
- Image Processing
- Content Moderation
- Media API
- Asynchronous Processing
website: https://mediaruntime.com
---
