---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Newminecraftservers Agentic Access
  operation_count: 5
  slug: newminecraftservers-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://newminecraftservers.net/api/v1
  baseurl_source: declared
  description: Cached Minecraft authentication and Xbox service health.
  name: NewMinecraftServers Minecraft services API
  slug: newminecraftservers-minecraft-services-api
- baseURL: https://newminecraftservers.net/api/v1
  baseurl_source: declared
  description: Published Minecraft server listings and observed history.
  name: NewMinecraftServers Servers API
  slug: newminecraftservers-servers-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/newminecraftservers/rate-limits/newminecraftservers-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/newminecraftservers-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://newminecraftservers.net/minecraft-api
- group: agent
  href: https://artifacts.apis.io/newminecraftservers/agentic-access/newminecraftservers-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/newminecraftservers-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/newminecraftservers/plans/newminecraftservers-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/newminecraftservers-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/newminecraftservers/rules/newminecraftservers-rules.yml
  title: ''
  type: Spectral
  url: rules/newminecraftservers-rules.yml
- group: design
  href: https://artifacts.apis.io/newminecraftservers/json-ld/newminecraftservers-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/newminecraftservers-context.jsonld
- group: design
  href: https://artifacts.apis.io/newminecraftservers/vocabulary/newminecraftservers-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/newminecraftservers-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/newminecraftservers/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/newminecraftservers/data-model/newminecraftservers-data-model.yml
  title: ''
  type: DataModel
  url: data-model/newminecraftservers-data-model.yml
- group: design
  href: https://artifacts.apis.io/newminecraftservers/conventions/newminecraftservers-conventions.yml
  title: ''
  type: Conventions
  url: conventions/newminecraftservers-conventions.yml
- group: auth
  href: https://artifacts.apis.io/newminecraftservers/security/newminecraftservers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/newminecraftservers-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/newminecraftservers/lifecycle/newminecraftservers-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/newminecraftservers-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/newminecraftservers/lifecycle/newminecraftservers-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/newminecraftservers-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/newminecraftservers/errors/newminecraftservers-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/newminecraftservers-problem-types.yml
- group: design
  href: https://artifacts.apis.io/newminecraftservers/conformance/newminecraftservers-conformance.yml
  title: ''
  type: Conformance
  url: conformance/newminecraftservers-conformance.yml
- group: agent
  href: https://artifacts.apis.io/newminecraftservers/llms/newminecraftservers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/newminecraftservers-llms.txt
- group: build
  href: https://artifacts.apis.io/newminecraftservers/packages/newminecraftservers-packages.yml
  title: ''
  type: SDKs
  url: packages/newminecraftservers-packages.yml
- group: build
  href: https://artifacts.apis.io/newminecraftservers/packages/newminecraftservers-packages.yml
  title: ''
  type: Packages
  url: packages/newminecraftservers-packages.yml
- group: start
  title: ''
  type: Login
  url: https://newminecraftservers.net/login
- group: company
  title: ''
  type: Website
  url: https://newminecraftservers.net
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newminecraftservers.net/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newminecraftservers.net/terms
- group: company
  title: ''
  type: Blog
  url: https://newminecraftservers.net/posts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aarongainz
created: '2026-09-21'
description: NewMinecraftServers is a directory of new Minecraft servers for Java and Bedrock Edition, where every listing is checked automatically and shows the server IP, online state, players online, accepted versions and gamemodes. Alongside the public site it publishes a free, no-key read-only Public API (OpenAPI 3.0) for searching listed servers, looking one up by address, reading player-count history and reading cached Minecraft service status as JSON, plus a set of free browser tools and an open-source Paper companion plugin for server owners.
finops:
- has_sources: true
  method: derived
  name: Newminecraftservers Finops
  primary_unit: ''
  service_category: ''
  slug: newminecraftservers-finops
  template: true
image: https://newminecraftservers.net/og/index.png?v=1.82871
json_schemas:
- name: MinecraftStatusEnvelope
  property_count: 1
  slug: newminecraftservers-minecraft-status-envelope
- name: ServerDetailEnvelope
  property_count: 1
  slug: newminecraftservers-server-detail-envelope
- name: ServerHistoryEnvelope
  property_count: 1
  slug: newminecraftservers-server-history-envelope
- name: ServerListEnvelope
  property_count: 1
  slug: newminecraftservers-server-list-envelope
jsonld:
- class_count: 14
  name: Newminecraftservers Context
  property_count: 68
  slug: newminecraftservers-context
layout: provider
modified: '2026-09-21'
name: NewMinecraftServers
nav: Providers
network: true
overview: 'NewMinecraftServers publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Minecraft services API and Servers API. Tagged areas include Minecraft, Gaming, server-directory, Game Servers, and status-monitoring.


  The NewMinecraftServers catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NewMinecraftServers'' developer surface includes pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Newminecraftservers Plans Pricing
  plan_count: 1
  slug: newminecraftservers-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Newminecraftservers Rate Limits
  slug: newminecraftservers-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: NewMinecraftServers API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: newminecraftservers-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 67.8
    catalog_earned_first_party: 8.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 62.2
    developer_ergonomics: 18.5
    discoverability: 67.9
    operational_transparency: 10.5
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/newminecraftservers/newminecraftservers-2026-10-11T111538.png
security:
- kind: domain-security
  name: Newminecraftservers Domain Security
  slug: newminecraftservers-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: check-minecraft-status
  slug: check-minecraft-status
- name: find-minecraft-server
  slug: find-minecraft-server
slug: newminecraftservers
tags:
- Minecraft
- Gaming
- server-directory
- Game Servers
- status-monitoring
- Public APIs
- Read Only
- JSON
website: https://newminecraftservers.net
---
