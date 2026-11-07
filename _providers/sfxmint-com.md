---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sfxmint Com Agentic Access
  operation_count: 9
  slug: sfxmint-com-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://sfxmint.com
  baseurl_source: declared
  description: Generating with an API key.
  name: SFXMint Generation API
  slug: sfxmint-com-generation-api
- baseURL: https://sfxmint.com
  baseurl_source: declared
  description: Keyless library endpoints.
  name: SFXMint Library API
  slug: sfxmint-com-library-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/sfxmint-com/agentic-access/sfxmint-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sfxmint-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sfxmint-com/plans/sfxmint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sfxmint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sfxmint-com/rules/sfxmint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sfxmint-com-rules.yml
- group: design
  href: https://artifacts.apis.io/sfxmint-com/json-ld/sfxmint-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sfxmint-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/sfxmint-com/vocabulary/sfxmint-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sfxmint-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sfxmint-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sfxmint-com/data-model/sfxmint-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sfxmint-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/sfxmint-com/cli/sfxmint-com-cli.yml
  title: ''
  type: CLI
  url: cli/sfxmint-com-cli.yml
- group: design
  href: https://artifacts.apis.io/sfxmint-com/errors/sfxmint-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sfxmint-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sfxmint-com/conformance/sfxmint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sfxmint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sfxmint-com/llms/sfxmint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sfxmint-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/sfxmint-com/mcp/sfxmint-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sfxmint-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/sfxmint-com/hosts/sfxmint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sfxmint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sfxmint-com/vendors/sfxmint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sfxmint-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sfxmint.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sfxmint.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://sfxmint.com/pricing
- group: start
  title: ''
  type: Login
  url: https://sfxmint.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flreey
- group: auth
  href: https://artifacts.apis.io/sfxmint-com/authentication/sfxmint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sfxmint-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sfxmint-com/security/sfxmint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sfxmint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sfxmint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sfxmint.com/api/docs
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://sfxmint.com/mcp
  - status: 200
    url: https://sfxmint.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: SFXMint provides a free library of CC0 sound effects for games and other media, offering WAV and MP3 downloads, ready‑made sound packs, an API for programmatic access, and an AI Studio that can generate missing sounds on demand. The service is open, requires no signup, and supports developers with a public API and MCP server for coding assistants.
image: https://sfxmint.com/og.png
json_schemas:
- name: OrderRequest
  property_count: 5
  slug: sfxmint-com-order-request
- name: RoleSound
  property_count: 21
  slug: sfxmint-com-role-sound
- name: SearchResult
  property_count: 20
  slug: sfxmint-com-search-result
- name: SoundDetail
  property_count: 18
  slug: sfxmint-com-sound-detail
- name: SoundSet
  property_count: 12
  slug: sfxmint-com-sound-set
- name: StructuredSearch
  property_count: 9
  slug: sfxmint-com-structured-search
jsonld:
- class_count: 13
  name: Sfxmint Com Context
  property_count: 77
  slug: sfxmint-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at sfxmint.com.
  name: SFXMint MCP Server
  slug: sfxmint-com-mcp-yml
modified: '2026-11-03'
name: SFXMint
nav: Providers
network: true
overview: 'SFXMint publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Generation API and Library API. Tagged areas include Sound Effects, CC0, AI Studio, Games, and Free.


  The SFXMint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SFXMint''s developer surface includes CLI, pricing, authentication, documentation, and 19 more developer resources.'
plans:
- name: Sfxmint Com Plans Pricing
  plan_count: 3
  slug: sfxmint-com-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: SFXMint API Rules
  rule_count: 61
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 2
  slug: sfxmint-com-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 64.7
    developer_ergonomics: 25.6
    discoverability: 65.0
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sfxmint Com Authentication
  slug: sfxmint-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sfxmint Com Domain Security
  slug: sfxmint-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: sfxmint-com-generation
  slug: sfxmint-com-generation
slug: sfxmint-com
tags:
- Sound Effects
- CC0
- AI Studio
- Games
- Free
website: https://sfxmint.com/
---
