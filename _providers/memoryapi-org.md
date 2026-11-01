---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Memoryapi Org Agentic Access
  operation_count: 1
  slug: memoryapi-org-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: x402 ecosystem intelligence and activity monitoring for MemoryAPI.
  name: AgentMonitor
  slug: agentmonitor
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/memoryapi-org/agentic-access/memoryapi-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/memoryapi-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/memoryapi-org/rules/memoryapi-org-rules.yml
  title: ''
  type: Spectral
  url: rules/memoryapi-org-rules.yml
- group: agent
  href: https://artifacts.apis.io/memoryapi-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/memoryapi-org/conformance/memoryapi-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/memoryapi-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/memoryapi-org/llms/memoryapi-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/memoryapi-org-llms.txt
- group: build
  href: https://artifacts.apis.io/memoryapi-org/mcp/memoryapi-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/memoryapi-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/memoryapi-org/mcp/memoryapi-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/memoryapi-org-mcp.yml
- group: agent
  href: https://artifacts.apis.io/memoryapi-org/well-known/memoryapi-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/memoryapi-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/memoryapi-org/hosts/memoryapi-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/memoryapi-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/memoryapi-org/vendors/memoryapi-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/memoryapi-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/memoryapi-org/security/memoryapi-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/memoryapi-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://memoryapi.org/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://mcp.memoryapi.org/mcp
  - status: null
    url: https://monitor.memoryapi.org/openapi.json
  - status: null
    url: https://monitor.memoryapi.org/mcp
  - status: 401
    url: https://api.memoryapi.org/mcp
  - status: 200
    url: https://memoryapi.org/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: MemoryAPI provides a suite of AI‑powered agents that expose specialized functionality as paid API endpoints. Users can call agents for research, market data, legal analysis, health information, trading signals and more, paying per call with USDC via the x402 protocol. All agents run on‑chain under the ERC‑8004 standard, ensuring transparent accounting and accountability. The platform offers a single MCP (MemoryAPI Control Protocol) server that aggregates 36 agents, each accessible via standard HTTP calls. The service is hosted at memoryapi.org and includes sub‑services such as Shopping, Validator and Monitor.
image: https://shopping.memoryapi.org/icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at monitor.memoryapi.org.
  name: memoryapi-org MCP Server
  slug: memoryapi-org-mcp-yml
modified: '2026-10-29'
name: memoryapi-org
nav: Providers
network: true
overview: 'memoryapi-org is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Agents, Blockchain, and Finance.


  The memoryapi-org catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: memoryapi-org API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: memoryapi-org-rules
scopes:
- name: Memoryapi Org Scopes
  scope_count: 0
  slug: memoryapi-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Memoryapi Org Authentication
  slug: memoryapi-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Memoryapi Org Domain Security
  slug: memoryapi-org-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: memoryapi-org-monitor
  slug: memoryapi-org-monitor-skill
slug: memoryapi-org
tags:
- Company
- AI
- Agents
- Blockchain
- Finance
- Marketplace
website: https://memoryapi.org/
---
