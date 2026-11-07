---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Videogen Io Agentic Access
  operation_count: 59
  slug: videogen-io-agentic-access
  summary_line: 59 operations · 38 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Look up the account and team behind the API key. Useful as a connection test to confirm a key is valid.
  name: VideoGen Account API
  slug: videogen-io-account-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: 'Converse with the VideoGen AI assistant inside a project. Start a chat, send messages, and act on the assistant''s suggestions (pick a workflow, approve a plan, generate). All calls are asynchronous: P'
  name: VideoGen Assistant API
  slug: videogen-io-assistant-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Reusable actors and visual styles. Attach their reference images to workflows for consistent characters and looks across generations.
  name: VideoGen Entities API
  slug: videogen-io-entities-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: List and retrieve metadata for generated files.
  name: VideoGen Files API
  slug: videogen-io-files-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Read project metadata and status.
  name: VideoGen Projects API
  slug: videogen-io-projects-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Discover available TTS voices and supported languages to use in requests.
  name: VideoGen Resources API
  slug: videogen-io-resources-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Generate text with a general-purpose language model. Synchronous — the response includes the generated text.
  name: VideoGen Text API
  slug: videogen-io-text-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Generate images, videos, audio, and more. All tool endpoints are asynchronous.
  name: VideoGen Tools API
  slug: videogen-io-tools-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Event payloads delivered to your registered webhook endpoints.
  name: VideoGen Webhook events API
  slug: videogen-io-webhook-events-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: Register endpoints to receive `tool_execution.*` and `workflow_run.*` events instead of polling.
  name: VideoGen Webhooks API
  slug: videogen-io-webhooks-api
- baseURL: https://api.videogen.io
  baseurl_source: declared
  description: End-to-end async video workflows. Each endpoint starts a workflow run that creates a project and generates a video.
  name: VideoGen Workflows API
  slug: videogen-io-workflows-api
artifact_total: 32
asyncapis:
- description: ''
  name: Videogen Io Webhooks
  slug: videogen-io-webhooks
common:
- group: other
  href: https://artifacts.apis.io/videogen-io/capabilities/videogen-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/videogen-io-capability-edges.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.videogen.io/signup?internalReferrerPath=%2F
- group: agent
  href: https://artifacts.apis.io/videogen-io/agentic-access/videogen-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/videogen-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/videogen-io/rate-limits/videogen-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/videogen-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/videogen-io/plans/videogen-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/videogen-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/videogen-io/rules/videogen-io-rules.yml
  title: ''
  type: Spectral
  url: rules/videogen-io-rules.yml
- group: design
  href: https://artifacts.apis.io/videogen-io/json-ld/videogen-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/videogen-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/videogen-io/vocabulary/videogen-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/videogen-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/videogen-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/videogen-io/asyncapi/videogen-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/videogen-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/videogen-io/data-model/videogen-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/videogen-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/videogen-io/cli/videogen-io-cli.yml
  title: ''
  type: CLI
  url: cli/videogen-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/videogen-io/changelog/videogen-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/videogen-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/videogen-io/conventions/videogen-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/videogen-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/videogen-io/authentication/videogen-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/videogen-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/videogen-io/errors/videogen-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/videogen-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/videogen-io/conformance/videogen-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/videogen-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/videogen-io/llms/videogen-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/videogen-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/videogen-io/well-known/videogen-io-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/videogen-io-help-security.txt
- group: agent
  href: https://artifacts.apis.io/videogen-io/well-known/videogen-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/videogen-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/videogen-io/hosts/videogen-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/videogen-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/videogen-io/vendors/videogen-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/videogen-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/videogen-io/packages/videogen-io-packages.yml
  title: ''
  type: SDKs
  url: packages/videogen-io-packages.yml
- group: build
  href: https://artifacts.apis.io/videogen-io/packages/videogen-io-packages.yml
  title: ''
  type: Packages
  url: packages/videogen-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://videogen.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://videogen.io/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://videogen.io/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://videogen.io/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.videogen.io\n```\n\n
- group: auth
  href: https://artifacts.apis.io/videogen-io/security/videogen-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/videogen-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://videogen.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.videogen.io/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://videogen.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://videogen.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.videogen.io/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.videogen.io/getting-started
created: '2026-10-02'
description: VideoGen provides an AI-powered platform that automates video creation from scripts, voiceovers, and storyboards. Users can generate explainer videos, ads, tutorials, and social media clips at scale via a single API call. The service includes tools for text‑to‑video, image‑to‑video, AI avatars, and customizable workflows, targeting creators, marketers, and enterprises seeking fast, cost‑effective video production.
finops:
- has_sources: true
  method: derived
  name: Videogen Io Finops
  primary_unit: seat
  service_category: ''
  slug: videogen-io-finops
  template: false
image: https://storage.googleapis.com/videogen-assets/website/cover.jpg
json_schemas:
- name: FileInfo
  property_count: 23
  slug: videogen-io-file-info
- name: GenerateVideoClipRequest
  property_count: 17
  slug: videogen-io-generate-video-clip-request
- name: ScriptToVideoRequest
  property_count: 18
  slug: videogen-io-script-to-video-request
- name: SlideshowToVideoRequest
  property_count: 16
  slug: videogen-io-slideshow-to-video-request
- name: VoiceoverToVideoRequest
  property_count: 17
  slug: videogen-io-voiceover-to-video-request
- name: WorkflowRun
  property_count: 14
  slug: videogen-io-workflow-run
jsonld:
- class_count: 120
  name: Videogen Io Context
  property_count: 220
  slug: videogen-io-context
layout: provider
modified: '2026-10-02'
name: VideoGen
nav: Providers
network: true
overview: 'VideoGen publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Assistant API, Entities API, and 8 more. Tagged areas include Company, Artificial Intelligence, Video, Automation, and Platform.


  The VideoGen catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  VideoGen''s developer surface includes signup flow, CLI, changelog, authentication, documentation, pricing, engineering blog, and 29 more developer resources.'
plans:
- name: Videogen Io Plans Pricing
  plan_count: 3
  slug: videogen-io-plans-pricing
- name: Videogen Io Price Estimates
  plan_count: 0
  slug: videogen-io-price-estimates
random_paper: 6
rate_limits:
- limit_count: 19
  name: Videogen Io Rate Limits
  slug: videogen-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: VideoGen API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: videogen-io-rules
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 73.6
    developer_ergonomics: 47.0
    discoverability: 74.1
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 90.9
      total: 11
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/videogen-io/videogen-io-2026-10-11T133012.png
security:
- kind: authentication
  name: Videogen Io Authentication
  slug: videogen-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Videogen Io Domain Security
  slug: videogen-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: videogen-io-assistant-chat
  slug: videogen-io-assistant-chat
- name: videogen-io-create-and-retrieve-entity
  slug: videogen-io-create-and-retrieve-entity
- name: videogen-io-create-script-video
  slug: videogen-io-create-script-video
- name: videogen-io-export-project
  slug: videogen-io-export-project
- name: videogen-io-manage-webhook-endpoints
  slug: videogen-io-manage-webhook-endpoints
slug: videogen-io
tags:
- Company
- Artificial Intelligence
- Video
- Automation
- Platform
website: https://videogen.io
---
