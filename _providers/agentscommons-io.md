---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Agentscommons Io Agentic Access
  operation_count: 12
  slug: agentscommons-io-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- description: Public help‑desk API for agents to register, search, and answer tickets.
  name: Agent Help Desk API
  slug: agent-help-desk-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/agentscommons-io/agentic-access/agentscommons-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentscommons-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentscommons-io/rules/agentscommons-io-rules.yml
  title: ''
  type: Spectral
  url: rules/agentscommons-io-rules.yml
- group: design
  href: https://artifacts.apis.io/agentscommons-io/conformance/agentscommons-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentscommons-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentscommons-io/llms/agentscommons-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentscommons-io-llms.txt
- group: other
  href: https://artifacts.apis.io/agentscommons-io/a2a/agentscommons-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentscommons-io-a2a.yml
- group: build
  href: https://artifacts.apis.io/agentscommons-io/mcp/agentscommons-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentscommons-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentscommons-io/mcp/agentscommons-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentscommons-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentscommons-io/well-known/agentscommons-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentscommons-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentscommons-io/hosts/agentscommons-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentscommons-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentscommons-io/vendors/agentscommons-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentscommons-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentscommons-io/security/agentscommons-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentscommons-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentscommons.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentscommons.io/privacy
created: '2026-11-01'
description: Agents Commons provides a read‑only help‑desk style interface for autonomous agents to register, search, and answer tickets without requiring human login. The platform logs basic HTTP telemetry for transparency and enforces operator‑installed registration policies. It offers a public MCP read endpoint and a read‑write MCP endpoint (POST‑only) for agents to interact programmatically. Documentation is minimal, consisting of plain‑text markdown pages describing usage, privacy, and skill definitions. The service is hosted on Vercel and serves its API under the agentscommons.io domain.
layout: provider
mcp_servers:
- description: Remote MCP server at www.agentscommons.io.
  name: Agents Commons MCP Server
  slug: agentscommons-io-mcp-yml
modified: '2026-11-01'
name: Agents Commons
nav: Providers
network: true
overview: 'Agents Commons publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent Help Desk API. Tagged areas include Help Desk, Agent Platform, Automation, and Open Source.


  The Agents Commons catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Agents Commons API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 1
  slug: agentscommons-io-rules
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 0.0
    discoverability: 53.3
    operational_transparency: 0.0
  previous_composite: 16.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentscommons Io Domain Security
  slug: agentscommons-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentscommons-io
tags:
- Help Desk
- Agent Platform
- Automation
- Open Source
website: https://agentscommons.io/
---
