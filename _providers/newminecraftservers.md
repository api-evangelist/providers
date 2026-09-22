---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-09-21'
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
  description: 'Free, no-key read-only API for discovering published Minecraft servers and reading cached Minecraft service status. Five GET endpoints under /api/v1: server search/list, address lookup, server detail,'
  name: NewMinecraftServers API
  slug: newminecraftservers-api
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/agentic-access/newminecraftservers-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/newminecraftservers-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/plans/newminecraftservers-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/newminecraftservers-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/rules/newminecraftservers-rules.yml
  title: ''
  type: Spectral
  url: rules/newminecraftservers-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/json-ld/newminecraftservers-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/newminecraftservers-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/vocabulary/newminecraftservers-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/newminecraftservers-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/data-model/newminecraftservers-data-model.yml
  title: ''
  type: DataModel
  url: data-model/newminecraftservers-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/conventions/newminecraftservers-conventions.yml
  title: ''
  type: Conventions
  url: conventions/newminecraftservers-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/security/newminecraftservers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/newminecraftservers-domain-security.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/lifecycle/newminecraftservers-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/newminecraftservers-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/lifecycle/newminecraftservers-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/newminecraftservers-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/errors/newminecraftservers-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/newminecraftservers-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/conformance/newminecraftservers-conformance.yml
  title: ''
  type: Conformance
  url: conformance/newminecraftservers-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/llms/newminecraftservers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/newminecraftservers-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/packages/newminecraftservers-packages.yml
  title: ''
  type: SDKs
  url: packages/newminecraftservers-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/newminecraftservers/refs/heads/main/packages/newminecraftservers-packages.yml
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
overview: 'NewMinecraftServers publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Minecraft, Gaming, server-directory, Game Servers, and status-monitoring.


  The NewMinecraftServers catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NewMinecraftServers'' developer surface includes engineering blog and 21 more developer resources.'
plans:
- name: Newminecraftservers Plans Pricing
  plan_count: 1
  slug: newminecraftservers-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Newminecraftservers Rate Limits
  slug: newminecraftservers-rate-limits
rules:
- effective_rule_count: 56
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
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 65.2
    developer_ergonomics: 28.0
    discoverability: 70.4
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Newminecraftservers Domain Security
  slug: newminecraftservers-domain-security
  summary_line: TLSv1.3 · HSTS
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
