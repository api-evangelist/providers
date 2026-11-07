---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Aistoryhub Co Agentic Access
  operation_count: 40
  slug: aistoryhub-co-agentic-access
  summary_line: 40 operations · 23 acting
api_count: 1
apis:
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: The authenticated token's owner.
  name: AIStoryHub Account API
  slug: aistoryhub-co-account-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: AI generation and revision. Runs on your own BYOK provider key.
  name: AIStoryHub AI API
  slug: aistoryhub-co-ai-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: Chapters and scenes within a story.
  name: AIStoryHub Chapters API
  slug: aistoryhub-co-chapters-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: Durable memories (preference/feedback/context/reference) that persist across sessions.
  name: AIStoryHub Memory API
  slug: aistoryhub-co-memory-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: 'Story Rules: a reusable writing-instruction library, not tied to one story.'
  name: AIStoryHub Rules API
  slug: aistoryhub-co-rules-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: The prose-instruction skills catalog installable onto this connection.
  name: AIStoryHub Skills API
  slug: aistoryhub-co-skills-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: Stories owned by the token holder.
  name: AIStoryHub Stories API
  slug: aistoryhub-co-stories-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: 'Voiceprints: reusable 33-dial Style Lab voice profiles, and the one pinned to a story.'
  name: AIStoryHub Voice API
  slug: aistoryhub-co-voice-api
- baseURL: https://aistoryhub.co/api/v1
  baseurl_source: declared
  description: World-building entries (characters, locations, lore, etc.).
  name: AIStoryHub World API
  slug: aistoryhub-co-world-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/aistoryhub-co/agentic-access/aistoryhub-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aistoryhub-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aistoryhub-co/rules/aistoryhub-co-rules.yml
  title: ''
  type: Spectral
  url: rules/aistoryhub-co-rules.yml
- group: design
  href: https://artifacts.apis.io/aistoryhub-co/json-ld/aistoryhub-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aistoryhub-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/aistoryhub-co/vocabulary/aistoryhub-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aistoryhub-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aistoryhub-co/data-model/aistoryhub-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aistoryhub-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/aistoryhub-co/errors/aistoryhub-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aistoryhub-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aistoryhub-co/conformance/aistoryhub-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aistoryhub-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aistoryhub-co/llms/aistoryhub-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aistoryhub-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/aistoryhub-co/well-known/aistoryhub-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aistoryhub-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/aistoryhub-co/hosts/aistoryhub-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aistoryhub-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/aistoryhub-co/vendors/aistoryhub-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aistoryhub-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aistoryhub.co/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://aistoryhub.co/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aistoryhub.co/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://aistoryhub.co/press
- group: start
  title: ''
  type: Login
  url: https://aistoryhub.co/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AIStoryHub
- group: auth
  href: https://artifacts.apis.io/aistoryhub-co/authentication/aistoryhub-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aistoryhub-co-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aistoryhub-co/security/aistoryhub-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aistoryhub-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aistoryhub.co/
- group: docs
  title: ''
  type: Documentation
  url: https://aistoryhub.co/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://aistoryhub.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://aistoryhub.co/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aistoryhub.co/developers
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://aistoryhub.co/openapi.json
  - status: 401
    url: https://aistoryhub.co/mcp/v1
  - status: 200
    url: https://aistoryhub.co/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AIStoryHub provides a free AI-powered writing studio tailored for fiction writers. Users can create, edit, and refine stories with AI voiceprints that match their unique style. The platform offers features like story drafting, voiceprint training, and integration with popular AI models, all without requiring an API key to start. It includes a community, labs, pricing plans, and extensive documentation for developers.
image: https://aistoryhub.co/og-image-home.png
json_schemas:
- name: Memory
  property_count: 7
  slug: aistoryhub-co-memory
- name: Rule
  property_count: 9
  slug: aistoryhub-co-rule
- name: StoryCreate
  property_count: 11
  slug: aistoryhub-co-story-create
- name: Story
  property_count: 17
  slug: aistoryhub-co-story
- name: Voiceprint
  property_count: 9
  slug: aistoryhub-co-voiceprint
- name: WorldNode
  property_count: 9
  slug: aistoryhub-co-world-node
jsonld:
- class_count: 18
  name: Aistoryhub Co Context
  property_count: 88
  slug: aistoryhub-co-context
layout: provider
modified: '2026-11-01'
name: AIStoryHub
nav: Providers
network: true
overview: 'AIStoryHub publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, AI API, Chapters API, and 6 more. Tagged areas include Artificial Intelligence, Writing, Fiction, Platform, and Free.


  The AIStoryHub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIStoryHub''s developer surface includes authentication, documentation, pricing, engineering blog, and 20 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: AIStoryHub API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: aistoryhub-co-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 62.8
    developer_ergonomics: 22.6
    discoverability: 67.0
    operational_transparency: 10.5
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aistoryhub Co Authentication
  slug: aistoryhub-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aistoryhub Co Domain Security
  slug: aistoryhub-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aistoryhub-co
tags:
- Artificial Intelligence
- Writing
- Fiction
- Platform
- Free
website: https://aistoryhub.co/
---
