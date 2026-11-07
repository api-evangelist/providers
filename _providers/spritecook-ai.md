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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Spritecook Ai Agentic Access
  operation_count: 21
  slug: spritecook-ai-agentic-access
  summary_line: 21 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.spritecook.ai
  baseurl_source: declared
  description: Credit balance.
  name: spritecook-ai Account API
  slug: spritecook-ai-account-api
- baseURL: https://api.spritecook.ai
  baseurl_source: declared
  description: Animate existing assets and characters.
  name: spritecook-ai Animation API
  slug: spritecook-ai-animation-api
- baseURL: https://api.spritecook.ai
  baseurl_source: declared
  description: Import, inspect, slice and clean up assets you own.
  name: spritecook-ai Assets API
  slug: spritecook-ai-assets-api
- baseURL: https://api.spritecook.ai
  baseurl_source: declared
  description: Models, workflows and options you can pass to generation calls.
  name: spritecook-ai Catalog API
  slug: spritecook-ai-catalog-api
- baseURL: https://api.spritecook.ai
  baseurl_source: declared
  description: Generate still assets, characters and tilesets.
  name: spritecook-ai Generation API
  slug: spritecook-ai-generation-api
- baseURL: https://api.spritecook.ai
  baseurl_source: declared
  description: Poll and cancel asynchronous jobs.
  name: spritecook-ai Jobs API
  slug: spritecook-ai-jobs-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/spritecook-ai/agentic-access/spritecook-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spritecook-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/spritecook-ai/rules/spritecook-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/spritecook-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/spritecook-ai/json-ld/spritecook-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/spritecook-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/spritecook-ai/vocabulary/spritecook-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spritecook-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/spritecook-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/spritecook-ai/data-model/spritecook-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spritecook-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/spritecook-ai/cli/spritecook-ai-cli.yml
  title: ''
  type: CLI
  url: cli/spritecook-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/spritecook-ai/authentication/spritecook-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spritecook-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/spritecook-ai/scopes/spritecook-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/spritecook-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/spritecook-ai/lifecycle/spritecook-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/spritecook-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/spritecook-ai/errors/spritecook-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spritecook-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spritecook-ai/conformance/spritecook-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spritecook-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spritecook-ai/llms/spritecook-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spritecook-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/spritecook-ai/well-known/spritecook-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spritecook-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/spritecook-ai/hosts/spritecook-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spritecook-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/spritecook-ai/vendors/spritecook-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spritecook-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/spritecook-ai/packages/spritecook-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/spritecook-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/spritecook-ai/packages/spritecook-ai-packages.yml
  title: ''
  type: Packages
  url: packages/spritecook-ai-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.spritecook.ai/press
- group: auth
  href: https://artifacts.apis.io/spritecook-ai/security/spritecook-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spritecook-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spritecook.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.spritecook.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.spritecook.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.spritecook.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.spritecook.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spritecook.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spritecook.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spritecook.ai/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.spritecook.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spritecook
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://spritecook.ai/openapi.json
  - status: null
    url: https://www.spritecook.ai/openapi.json
  - status: 401
    url: https://api.spritecook.ai/mcp
  - status: 200
    url: https://spritecook.ai/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: SpriteCook AI is a SaaS platform that leverages artificial intelligence to generate and animate pixel art and 2D game assets for developers. Users can create characters, items, and sprite sheets in a consistent style, with support for Unity, Godot, and other game engines. The service offers both single-image generation and batch asset packs, providing a fast, cost-effective alternative to hand‑crafted pixel art. By automating the art creation workflow, SpriteCook helps indie developers and studios accelerate prototyping and production while maintaining artistic coherence across game projects.
image: https://www.spritecook.ai/favicon_pad_hd.png
json_schemas:
- name: ApiAnimateRequest
  property_count: 19
  slug: spritecook-ai-api-animate-request
- name: ApiAssetInfo
  property_count: 26
  slug: spritecook-ai-api-asset-info
- name: ApiAssetMetadata
  property_count: 53
  slug: spritecook-ai-api-asset-metadata
- name: ApiGenerateRequest
  property_count: 24
  slug: spritecook-ai-api-generate-request
- name: ApiJobResponse
  property_count: 14
  slug: spritecook-ai-api-job-response
- name: ApiTilesetGenerateRequest
  property_count: 20
  slug: spritecook-ai-api-tileset-generate-request
jsonld:
- class_count: 25
  name: Spritecook Ai Context
  property_count: 167
  slug: spritecook-ai-context
layout: provider
modified: '2026-10-31'
name: spritecook-ai
nav: Providers
network: true
overview: 'spritecook-ai publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Animation API, Assets API, and 3 more. Tagged areas include Artificial Intelligence, Pixel Art, Game Development, Software-as-a-Service, and Graphics.


  The spritecook-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  spritecook-ai''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: spritecook-ai API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: spritecook-ai-rules
scopes:
- name: Spritecook Ai Scopes
  scope_count: 1
  slug: spritecook-ai-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 68.6
    developer_ergonomics: 48.1
    discoverability: 67.0
    operational_transparency: 2.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
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
screenshot: https://apis.io/screenshots/spritecook-ai/spritecook-ai-2026-11-03T143658.png
security:
- kind: authentication
  name: Spritecook Ai Authentication
  slug: spritecook-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Spritecook Ai Domain Security
  slug: spritecook-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: generate-animation
  slug: generate-animation
- name: generate-character
  slug: generate-character
- name: list-models
  slug: list-models
slug: spritecook-ai
tags:
- Artificial Intelligence
- Pixel Art
- Game Development
- Software-as-a-Service
- Graphics
website: https://spritecook.ai/
---
