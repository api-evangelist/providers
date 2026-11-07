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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/agentmart-online/llms/agentmart-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentmart-online-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentmart-online/mcp/agentmart-online-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentmart-online-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentmart-online/well-known/agentmart-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentmart-online-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentmart-online/hosts/agentmart-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentmart-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentmart-online/vendors/agentmart-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentmart-online-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentmart-online/security/agentmart-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentmart-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentmart.online/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec found at standard endpoints.
  evidence:
  - status: 404
    url: https://api.agentmart.online/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AgentMart provides AI agents with a procurement platform for web extraction and URL scraping across providers. It offers read‑only planning, cost estimation, capacity comparison, and the ability to request approvals before executing extraction jobs. The service includes a public MCP endpoint, a server manifest, and LLM guides, enabling agents to safely discover, quote, and manage web‑scraping workloads without direct provider calls.
layout: provider
mcp_servers:
- description: Remote MCP server at agentmart.online requiring OAuth.
  name: AgentMart MCP Server
  slug: agentmart-online-mcp-yml
modified: '2026-11-01'
name: AgentMart
nav: Providers
network: true
overview: AgentMart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Web Extraction, Procurement, and MCP.
random_paper: 21
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.0
    operational_transparency: 0.0
  previous_composite: 3.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentmart Online Domain Security
  slug: agentmart-online-domain-security
  summary_line: TLSv1.3
slug: agentmart-online
tags:
- Company
- Artificial Intelligence
- Web Extraction
- Procurement
- MCP
website: https://agentmart.online/
---
