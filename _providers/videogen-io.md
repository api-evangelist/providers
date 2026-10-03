---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.9
  scored_at: '2026-10-03'
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
artifact_total: 25
asyncapis:
- description: ''
  name: Videogen Io Webhooks
  slug: videogen-io-webhooks
common:
- group: start
  title: ''
  type: SignUp
  url: https://app.videogen.io/signup?internalReferrerPath=%2F
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/agentic-access/videogen-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/videogen-io-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/rate-limits/videogen-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/videogen-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/plans/videogen-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/videogen-io-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/rules/videogen-io-rules.yml
  title: ''
  type: Spectral
  url: rules/videogen-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/json-ld/videogen-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/videogen-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/vocabulary/videogen-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/videogen-io-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/asyncapi/videogen-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/videogen-io-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/data-model/videogen-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/videogen-io-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/cli/videogen-io-cli.yml
  title: ''
  type: CLI
  url: cli/videogen-io-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/changelog/videogen-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/videogen-io-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/conventions/videogen-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/videogen-io-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/authentication/videogen-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/videogen-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/errors/videogen-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/videogen-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/conformance/videogen-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/videogen-io-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/llms/videogen-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/videogen-io-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/well-known/videogen-io-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/videogen-io-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/well-known/videogen-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/videogen-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/hosts/videogen-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/videogen-io-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/vendors/videogen-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/videogen-io-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/packages/videogen-io-packages.yml
  title: ''
  type: SDKs
  url: packages/videogen-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/packages/videogen-io-packages.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/videogen-io/refs/heads/main/security/videogen-io-domain-security.yml
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
overview: 'VideoGen publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Assistant API, Entities API, and 8 more. Tagged areas include Company, Artificial Intelligence, Video, Automation, and Platform.


  The VideoGen catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  VideoGen''s developer surface includes signup flow, CLI, changelog, authentication, documentation, pricing, engineering blog, and 28 more developer resources.'
plans:
- name: Videogen Io Plans Pricing
  plan_count: 3
  slug: videogen-io-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 19
  name: Videogen Io Rate Limits
  slug: videogen-io-rate-limits
rules:
- effective_rule_count: 56
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
  composite: 63.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 67.4
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Videogen Io Authentication
  slug: videogen-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Videogen Io Domain Security
  slug: videogen-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: videogen-io
tags:
- Company
- Artificial Intelligence
- Video
- Automation
- Platform
website: https://videogen.io
---
