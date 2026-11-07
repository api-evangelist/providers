---
access_model:
  confidence: low
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
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
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
  score: 4.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: HumanMCP provides a personal server and federated network enabling creators to prove authorship of their works using cryptographic signatures.
  name: humanMCP API
  slug: humanmcp-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/humanmcp-net/llms/humanmcp-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/humanmcp-net-llms.txt
- group: other
  href: https://artifacts.apis.io/humanmcp-net/a2a/humanmcp-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/humanmcp-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/humanmcp-net/mcp/humanmcp-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/humanmcp-net-mcp.yml
- group: other
  href: https://artifacts.apis.io/humanmcp-net/hosts/humanmcp-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/humanmcp-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/humanmcp-net/vendors/humanmcp-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/humanmcp-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/humanmcp-net/security/humanmcp-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/humanmcp-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://humanmcp.net/
- group: docs
  title: ''
  type: APIReference
  url: https://kapoost.humanmcp.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kapoost
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is published; only an MCP JSON-RPC endpoint is available.
  evidence:
  - status: 404
    url: https://kapoost.humanmcp.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: humanMCP provides a personal server and federated network enabling creators to prove authorship of their works using cryptographic signatures. It offers a public REST API with OpenAPI 3.1, agent discovery via .well-known/agent.json, and supports AI-native discovery without platform lock‑in. The service is open‑source, CC‑BY licensed, and aims to give humans control over their digital creations while allowing agents to respect usage terms.
examples:
- key_count: 3
  name: Kapoost Tools List
  slug: kapoost-tools-list
image: https://avatars.githubusercontent.com/u/778613?v=4
layout: provider
mcp_servers:
- description: Remote MCP server at kapoost.humanmcp.net.
  name: humanmcp-net MCP Server
  slug: humanmcp-net-mcp-yml
modified: '2026-10-30'
name: humanmcp-net
nav: Providers
network: true
overview: 'humanmcp-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human, MCP, and OpenAPI.


  humanmcp-net''s developer surface includes API reference and 8 more developer resources.'
random_paper: 5
scopes:
- name: Humanmcp Net Scopes
  scope_count: 0
  slug: humanmcp-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 66.7
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/humanmcp-net/humanmcp-net-2026-11-03T133534.png
security:
- kind: authentication
  name: Humanmcp Net Authentication
  slug: humanmcp-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Humanmcp Net Domain Security
  slug: humanmcp-net-domain-security
  summary_line: TLSv1.3 · DMARC
slug: humanmcp-net
tags:
- Company
- Human
- MCP
- OpenAPI
website: https://humanmcp.net/
---
