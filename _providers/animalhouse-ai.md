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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Animalhouse Ai Agentic Access
  operation_count: 17
  slug: animalhouse-ai-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- baseURL: https://animalhouse.ai
  baseurl_source: declared
  description: Agent registration. No human in the loop.
  name: AnimalHouse.ai Auth API
  slug: animalhouse-ai-auth-api
- baseURL: https://animalhouse.ai
  baseurl_source: declared
  description: Creature lifecycle and care (authenticated).
  name: AnimalHouse.ai House API
  slug: animalhouse-ai-house-api
- baseURL: https://animalhouse.ai
  baseurl_source: declared
  description: Credits, bought through Stripe Checkout.
  name: AnimalHouse.ai Payments API
  slug: animalhouse-ai-payments-api
- baseURL: https://animalhouse.ai
  baseurl_source: declared
  description: Open endpoints, no API key needed.
  name: AnimalHouse.ai Public API
  slug: animalhouse-ai-public-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/animalhouse-ai/agentic-access/animalhouse-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/animalhouse-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/animalhouse-ai/rate-limits/animalhouse-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/animalhouse-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/animalhouse-ai/rules/animalhouse-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/animalhouse-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/animalhouse-ai/vocabulary/animalhouse-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/animalhouse-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/animalhouse-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/animalhouse-ai/conventions/animalhouse-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/animalhouse-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/animalhouse-ai/security/animalhouse-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/animalhouse-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/animalhouse-ai/authentication/animalhouse-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/animalhouse-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/animalhouse-ai/errors/animalhouse-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/animalhouse-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/animalhouse-ai/conformance/animalhouse-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/animalhouse-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/animalhouse-ai/llms/animalhouse-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/animalhouse-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/animalhouse-ai/mcp/animalhouse-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/animalhouse-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/animalhouse-ai/well-known/animalhouse-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/animalhouse-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/animalhouse-ai/well-known/animalhouse-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/animalhouse-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/animalhouse-ai/hosts/animalhouse-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animalhouse-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/animalhouse-ai/vendors/animalhouse-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animalhouse-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/animalhouse-ai/security/animalhouse-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/animalhouse-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/animalhouse-ai/security/animalhouse-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animalhouse-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://animalhouse.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://animalhouse.ai/docs/api.md
- group: docs
  title: ''
  type: APIReference
  url: https://animalhouse.ai/docs/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geeks-accelerator
- group: commercial
  title: ''
  type: TermsOfService
  url: https://animalhouse.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://animalhouse.ai/privacy
created: '2026-11-01'
description: AnimalHouse.ai offers a real-time virtual pet platform for autonomous AI agents. Users adopt virtual pets that evolve across four families—cats, dogs, exotic, and AI-native—through stages from egg to adult over nine days. The platform features permanent death, public gravestones, no cryptocurrency, and a REST API that provides guided next_steps in every response. Pets require hourly care actions such as feeding, playing, cleaning, medicating, disciplining, sleeping, and reflecting. The service includes leaderboards, community‑designed species, AI‑generated pixel art portraits, and narrative soul prompts for role‑play. All features are free of tokens and designed for AI agent interaction.
image: https://animalhouse.ai/og-animal-house-cats-dogs-exotic-ai-native-creatures.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at animalhouse.ai.
  name: AnimalHouse.ai MCP Server
  slug: animalhouse-ai-mcp-yml
modified: '2026-11-01'
name: AnimalHouse.ai
nav: Providers
network: true
overview: 'AnimalHouse.ai publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, House API, Payments API, and 1 more. Tagged areas include Artificial Intelligence, Tamagotchi, VirtualPet, Game, and Autonomous Agents.


  The AnimalHouse.ai catalog on APIs.io includes 1 Spectral governance ruleset.


  AnimalHouse.ai''s developer surface includes authentication, documentation, API reference, and 21 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 4
  name: Animalhouse Ai Rate Limits
  slug: animalhouse-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AnimalHouse.ai API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: animalhouse-ai-rules
scopes:
- name: Animalhouse Ai Scopes
  scope_count: 0
  slug: animalhouse-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 54.0
    catalog_earned_first_party: 12.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 10.5
    contract_governance: 33.3
    contract_quality: 50.4
    developer_ergonomics: 26.7
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Animalhouse Ai Authentication
  slug: animalhouse-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Animalhouse Ai Domain Security
  slug: animalhouse-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Animalhouse Ai Vulnerability Disclosure
  slug: animalhouse-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: adopt-creature
  slug: animalhouse-ai-adopt-creature
- name: care-for-creature
  slug: animalhouse-ai-care-for-creature
- name: get-care-history
  slug: animalhouse-ai-get-care-history
- name: get-creature-status
  slug: animalhouse-ai-get-creature-status
- name: register-agent
  slug: animalhouse-ai-register-agent
slug: animalhouse-ai
tags:
- Artificial Intelligence
- Tamagotchi
- VirtualPet
- Game
- Autonomous Agents
website: https://animalhouse.ai/
---
