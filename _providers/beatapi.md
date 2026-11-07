---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Beatapi Agentic Access
  operation_count: 50
  slug: beatapi-agentic-access
  summary_line: 50 operations · 30 acting
api_count: 1
apis:
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Read your account and balance, manage API keys and read payments with a personal access token.
  name: BeatAPI Account API
  slug: beatapi-account-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: 'Start here: one Search → Inspect → Run loop covers every BeatAPI capability — social media data, text, image, video and decision models, web search and workflows.'
  name: BeatAPI Capabilities API
  slug: beatapi-capabilities-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: The Decisions API from BeatAPI — 1 operation(s) for decisions.
  name: BeatAPI Decisions API
  slug: beatapi-decisions-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Create product ad video tasks from product images and duration.
  name: BeatAPI Ecommerce Video API
  slug: beatapi-ecommerce-video-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Discover versioned effects and create image or video effect tasks.
  name: BeatAPI Effects API
  slug: beatapi-effects-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Upload local assets and use the returned HTTPS URL as workflow input.
  name: BeatAPI Files API
  slug: beatapi-files-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Discover BeatAPI generation models and create image or video tasks.
  name: BeatAPI Generation API
  slug: beatapi-generation-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Create music video tasks from images, audio, and optional creative controls.
  name: BeatAPI Music Video API
  slug: beatapi-music-video-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Create and manage short-lived BeatAPI browser sessions for live AI video effects.
  name: BeatAPI Realtime Video API
  slug: beatapi-realtime-video-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: The Social Data API from BeatAPI — 1 operation(s) for social data.
  name: BeatAPI Social Data API
  slug: beatapi-social-data-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Poll task status and read output URLs.
  name: BeatAPI Tasks API
  slug: beatapi-tasks-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Discover enabled text models and call them through OpenAI, Anthropic, or Gemini-compatible request formats.
  name: BeatAPI Text API
  slug: beatapi-text-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Inspect task totals and account concurrency.
  name: BeatAPI Usage API
  slug: beatapi-usage-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Analyze uploaded videos with standard or deep multimodal reasoning.
  name: BeatAPI Video Analysis API
  slug: beatapi-video-analysis-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Search the web, read pages as Markdown or plain text, list the pages of a site and research a question.
  name: BeatAPI Web Search API
  slug: beatapi-web-search-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Manage optional completion callbacks.
  name: BeatAPI Webhooks API
  slug: beatapi-webhooks-api
- baseURL: https://api.beatapi.io
  baseurl_source: declared
  description: Discover the workflow IDs available for task creation.
  name: BeatAPI Workflows API
  slug: beatapi-workflows-api
artifact_total: 37
asyncapis:
- description: ''
  name: Beatapi Webhooks
  slug: beatapi-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/beatapi/agentic-access/beatapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beatapi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/beatapi/rules/beatapi-rules.yml
  title: ''
  type: Spectral
  url: rules/beatapi-rules.yml
- group: design
  href: https://artifacts.apis.io/beatapi/json-ld/beatapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beatapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/beatapi/vocabulary/beatapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beatapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/beatapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/beatapi/asyncapi/beatapi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/beatapi-webhooks.yml
- group: design
  href: https://artifacts.apis.io/beatapi/data-model/beatapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beatapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/beatapi/conventions/beatapi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/beatapi-conventions.yml
- group: design
  href: https://artifacts.apis.io/beatapi/conventions/beatapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beatapi-conventions.yml
- group: auth
  href: https://artifacts.apis.io/beatapi/authentication/beatapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beatapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/beatapi/errors/beatapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beatapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beatapi/conformance/beatapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beatapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beatapi/llms/beatapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beatapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/beatapi/well-known/beatapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beatapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/beatapi/hosts/beatapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beatapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/beatapi/vendors/beatapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beatapi-vendors.yml
- group: build
  href: https://artifacts.apis.io/beatapi/packages/beatapi-packages.yml
  title: ''
  type: SDKs
  url: packages/beatapi-packages.yml
- group: build
  href: https://artifacts.apis.io/beatapi/packages/beatapi-packages.yml
  title: ''
  type: Packages
  url: packages/beatapi-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beatapi.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beatapi.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://beatapi.io/pricing
- group: start
  title: ''
  type: Login
  url: https://beatapi.io/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BeatAPI
- group: start
  title: ''
  type: GettingStarted
  url: https://beatapi.io/dashboard/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://beatapi.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://beatapi.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beatapi.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.beatapi.io`.\n2
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beatapi.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/beatapi/security/beatapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beatapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beatapi.io
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://beatapi.io/openapi.json
  - status: null
    url: https://docs.beatapi.io/openapi.json
  - status: null
    url: https://docs.beatapi.io/mcp
  - status: 401
    url: https://beatapi.io/mcp
  - status: 200
    url: https://beatapi.io
  reason: partner-login
  state: gated
created: '2026-10-30'
description: BeatAPI is a unified API platform for AI agents, offering a single API key to access text, image, video models, social data, SEO data, and web search. It provides verified lower pricing for matched models and specifications, aiming to simplify integration for developers and enterprises. The service consolidates multiple AI capabilities into one cohesive endpoint, enhancing efficiency and reducing complexity for AI-driven applications.
image: https://beatapi.io/og/beatapi-home-social-card-v18.png
json_schemas:
- name: CapabilityContract
  property_count: 24
  slug: beatapi-capability-contract
- name: CapabilityRunRequest
  property_count: 9
  slug: beatapi-capability-run-request
- name: CapabilityRunResult
  property_count: 14
  slug: beatapi-capability-run-result
- name: CapabilitySearchPage
  property_count: 10
  slug: beatapi-capability-search-page
- name: ImageGenerationTaskCreateRequest
  property_count: 0
  slug: beatapi-image-generation-task-create-request
- name: VideoGenerationTaskCreateRequest
  property_count: 0
  slug: beatapi-video-generation-task-create-request
jsonld:
- class_count: 120
  name: Beatapi Context
  property_count: 235
  slug: beatapi-context
layout: provider
modified: '2026-10-30'
name: BeatAPI
nav: Providers
network: true
overview: 'BeatAPI publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Capabilities API, Decisions API, and 14 more. Tagged areas include Company, Artificial Intelligence, Platform, Unified API, and Data Integration.


  The BeatAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BeatAPI''s developer surface includes authentication, pricing, getting-started guide, changelog, engineering blog, documentation, API reference, and 24 more developer resources.'
plans:
- name: Beatapi Plans Pricing
  plan_count: 0
  slug: beatapi-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Beatapi Rate Limits
  slug: beatapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: BeatAPI API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 4
  slug: beatapi-rules
scopes:
- name: Beatapi Scopes
  scope_count: 0
  slug: beatapi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 71.6
    developer_ergonomics: 41.1
    discoverability: 75.0
    operational_transparency: 39.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 60.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: unknown
    skills: derived
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
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/beatapi/beatapi-2026-11-03T121650.png
security:
- kind: authentication
  name: Beatapi Authentication
  slug: beatapi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Beatapi Domain Security
  slug: beatapi-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: beatapi-effect-task-creation
  slug: beatapi-effect-task-creation
- name: beatapi-manage-account-api-keys
  slug: beatapi-manage-account-api-keys
- name: beatapi-manage-webhook-endpoints
  slug: beatapi-manage-webhook-endpoints
- name: beatapi-realtime-video-session
  slug: beatapi-realtime-video-session
- name: beatapi-webhook-receiver
  slug: beatapi-webhook-receiver
slug: beatapi
tags:
- Company
- Artificial Intelligence
- Platform
- Unified API
- Data Integration
website: https://beatapi.io
---
