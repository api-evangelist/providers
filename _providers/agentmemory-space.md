---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/agentmemory-space/plans/agentmemory-space-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentmemory-space-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agentmemory-space/llms/agentmemory-space-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentmemory-space-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentmemory-space/well-known/agentmemory-space-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentmemory-space-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentmemory-space/hosts/agentmemory-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentmemory-space-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentmemory-space/vendors/agentmemory-space-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentmemory-space-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentmemory.space/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentmemory.space/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentmemory.space/pricing/
- group: auth
  href: https://artifacts.apis.io/agentmemory-space/security/agentmemory-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentmemory-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentmemory.space/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: no-response
    url: https://api.agentmemory.space/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agentmemory provides a persistent memory layer for AI coding agents, enabling teams to capture, retrieve, and govern agent session data across workflows. The platform supports Claude Code, Codex, Cursor, and OpenAI agents, offering features like hybrid recall, review before share, and memory actions. It includes a marketplace for memory packs, pricing plans for teams, and integrates with MCP tools to ensure secure, governed memory for AI-driven development.
image: https://agentmemory.space/assets/agentmemory-workspace.svg
layout: provider
modified: '2026-11-01'
name: Agentmemory
nav: Providers
network: true
overview: 'Agentmemory is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Platform, Team, and Agents.


  Agentmemory''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Agentmemory Space Plans Pricing
  plan_count: 3
  slug: agentmemory-space-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 17.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentmemory Space Domain Security
  slug: agentmemory-space-domain-security
  summary_line: TLSv1.3
slug: agentmemory-space
tags:
- Artificial Intelligence
- Memory
- Platform
- Team
- Agents
website: https://agentmemory.space/
---
