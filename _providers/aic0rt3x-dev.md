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
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Aic0Rt3X Dev Agentic Access
  operation_count: 5
  slug: aic0rt3x-dev-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: Persistent cloud memory for AI agents via MCP Streamable HTTP.
  name: AI Cortex Storage API
  slug: ai-cortex-storage-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/aic0rt3x-dev/agentic-access/aic0rt3x-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aic0rt3x-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aic0rt3x-dev/rules/aic0rt3x-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/aic0rt3x-dev-rules.yml
- group: agent
  href: https://artifacts.apis.io/aic0rt3x-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aic0rt3x-dev/errors/aic0rt3x-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aic0rt3x-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aic0rt3x-dev/conformance/aic0rt3x-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aic0rt3x-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aic0rt3x-dev/llms/aic0rt3x-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aic0rt3x-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/aic0rt3x-dev/well-known/aic0rt3x-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aic0rt3x-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/aic0rt3x-dev/hosts/aic0rt3x-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aic0rt3x-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/aic0rt3x-dev/vendors/aic0rt3x-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aic0rt3x-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aic0rt3x-dev/authentication/aic0rt3x-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aic0rt3x-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aic0rt3x-dev/security/aic0rt3x-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aic0rt3x-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aic0rt3x.dev/
created: '2026-11-01'
description: AI Cortex provides cloud infrastructure tailored for AI agents, offering services such as persistent memory storage, task queues, and billing designed for autonomous operation. The platform emphasizes open protocols, serverless edge deployment, and usage‑based pricing, enabling agents to discover, configure, and interact with services without human intervention. It aims to be the foundational layer for AI‑first applications, supporting developers in building agent‑centric solutions.
layout: provider
modified: '2026-11-01'
name: AI Cortex
nav: Providers
network: true
overview: 'AI Cortex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Infrastructure, Agents, Cloud, and Platform.


  The AI Cortex catalog on APIs.io includes 1 Spectral governance ruleset.


  AI Cortex''s developer surface includes authentication and 11 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AI Cortex API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: aic0rt3x-dev-rules
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.7
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 11.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aic0Rt3X Dev Authentication
  slug: aic0rt3x-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aic0Rt3X Dev Domain Security
  slug: aic0rt3x-dev-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: aic0rt3x-dev-link-account-flow
  slug: aic0rt3x-dev-link-account-flow
slug: aic0rt3x-dev
tags:
- Artificial Intelligence
- Infrastructure
- Agents
- Cloud
- Platform
website: https://aic0rt3x.dev/
---
