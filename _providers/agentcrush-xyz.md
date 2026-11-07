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
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
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
  score: 10.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgentCrush is the protocol‑neutral market intelligence layer for the AI agent economy. This OpenAPI spec covers the free flat JSON endpoints designed for LLM/agent retrieval.
  name: AgentCrush Public API
  slug: agentcrush-public-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/agentcrush-xyz/plans/agentcrush-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentcrush-xyz-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agentcrush-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentcrush-xyz/conformance/agentcrush-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentcrush-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentcrush-xyz/llms/agentcrush-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcrush-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/agentcrush-xyz/a2a/agentcrush-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentcrush-xyz-a2a.yml
- group: build
  href: https://artifacts.apis.io/agentcrush-xyz/mcp/agentcrush-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentcrush-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentcrush-xyz/mcp/agentcrush-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentcrush-xyz-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentcrush-xyz/hosts/agentcrush-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcrush-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentcrush-xyz/vendors/agentcrush-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcrush-xyz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentcrush-xyz/security/agentcrush-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcrush-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentcrush.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://agentcrush.xyz/developers
- group: docs
  title: ''
  type: APIReference
  url: https://agentcrush.xyz/.well-known/mcp.json
- group: commercial
  title: ''
  type: Pricing
  url: https://agentcrush.xyz/pricing
- group: company
  title: ''
  type: Blog
  url: https://agentcrush.xyz/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcrush.xyz/terms
created: '2026-10-31'
description: AgentCrush provides a public, protocol‑neutral index of AI agents, offering rankings, ghost‑index snapshots, and market intelligence. It aggregates signals from GitHub, npm, PyPI, on‑chain x402 payments, and A2A/MCP activity to evaluate agent health, trust, and economic impact. The service is free for basic access and offers a paid Pro API for unlimited calls, with transparent pricing and open methodology.
image: https://agentcrush.xyz/api/og?title=The%20public%20record%20of%20AI%20agents&kicker=AGENTCRUSH&subtitle=Independent.%20Cross-protocol.%20Open%20methodology.
layout: provider
mcp_servers:
- description: Remote MCP server at agentcrush.xyz.
  name: AgentCrush MCP Server
  slug: agentcrush-xyz-mcp-yml
modified: '2026-10-31'
name: AgentCrush
nav: Providers
network: true
overview: 'AgentCrush is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Market Intelligence, Index, Rankings, and Open Data.


  AgentCrush''s developer surface includes documentation, API reference, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Agentcrush Xyz Plans Pricing
  plan_count: 1
  slug: agentcrush-xyz-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.3
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 19.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentcrush Xyz Domain Security
  slug: agentcrush-xyz-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: lookup-agent
  slug: agentcrush-xyz-lookup_agent
slug: agentcrush-xyz
tags:
- Artificial Intelligence
- Market Intelligence
- Index
- Rankings
- Open Data
website: https://agentcrush.xyz/
---
