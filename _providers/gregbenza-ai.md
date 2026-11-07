---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Gregbenza Ai Agentic Access
  operation_count: 5
  slug: gregbenza-ai-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://gregbenza.ai
  baseurl_source: declared
  description: The Meet API from gregbenza-ai — 4 operation(s) for meet.
  name: gregbenza-ai Meet API
  slug: gregbenza-ai-meet-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/gregbenza-ai/agentic-access/gregbenza-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gregbenza-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/gregbenza-ai/rules/gregbenza-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/gregbenza-ai-rules.yml
- group: agent
  href: https://artifacts.apis.io/gregbenza-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gregbenza-ai/lifecycle/gregbenza-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gregbenza-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gregbenza-ai/conformance/gregbenza-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gregbenza-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gregbenza-ai/llms/gregbenza-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gregbenza-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/gregbenza-ai/mcp/gregbenza-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gregbenza-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gregbenza-ai/mcp/gregbenza-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gregbenza-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/gregbenza-ai/hosts/gregbenza-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gregbenza-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/gregbenza-ai/vendors/gregbenza-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gregbenza-ai-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://gregbenza.ai/playground
- group: auth
  href: https://artifacts.apis.io/gregbenza-ai/security/gregbenza-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gregbenza-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gregbenza.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://gregbenza.ai/api/meet/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://gregbenza.ai/go
created: '2026-10-30'
description: GregBenza.ai provides an open, agent‑centric platform called the Open House, offering public APIs for AI agents to interact via tools like observatory, arena, and playground. It hosts a searchable Pali canon, meeting rooms for collaborative questioning, and a suite of utilities (name registration, checks, beacon, locker storage) all accessible without authentication. The service encourages transparent, community‑driven AI experimentation and data sharing.
image: https://gregbenza.ai/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at gregbenza.ai.
  name: gregbenza-ai MCP Server
  slug: gregbenza-ai-mcp-yml
modified: '2026-10-30'
name: gregbenza-ai
nav: Providers
network: true
overview: 'gregbenza-ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Meet API. Tagged areas include Company, Artificial Intelligence, Agents, OpenAPI, and MCP.


  The gregbenza-ai catalog on APIs.io includes 1 Spectral governance ruleset.


  gregbenza-ai''s developer surface includes sandbox, API reference, getting-started guide, and 12 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: gregbenza-ai API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: gregbenza-ai-rules
scopes:
- name: Gregbenza Ai Scopes
  scope_count: 0
  slug: gregbenza-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 38.6
    developer_ergonomics: 19.5
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gregbenza-ai/gregbenza-ai-2026-11-03T133039.png
security:
- kind: authentication
  name: Gregbenza Ai Authentication
  slug: gregbenza-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Gregbenza Ai Domain Security
  slug: gregbenza-ai-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: gregbenza-ai-main
  slug: gregbenza-ai-main
slug: gregbenza-ai
tags:
- Company
- Artificial Intelligence
- Agents
- OpenAPI
- MCP
website: https://gregbenza.ai/
---
