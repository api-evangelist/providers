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
  - rate-limits
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Render artifacts, read painted geometry, or edit Mermaid source with typed operations.
  name: Library API
  slug: library-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/agentic-mermaid-dev/rate-limits/agentic-mermaid-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentic-mermaid-dev-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/agentic-mermaid-dev/cli/agentic-mermaid-dev-cli.yml
  title: ''
  type: CLI
  url: cli/agentic-mermaid-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/agentic-mermaid-dev/changelog/agentic-mermaid-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentic-mermaid-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/agentic-mermaid-dev/lifecycle/agentic-mermaid-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentic-mermaid-dev-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/agentic-mermaid-dev/llms/agentic-mermaid-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentic-mermaid-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentic-mermaid-dev/mcp/agentic-mermaid-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentic-mermaid-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentic-mermaid-dev/hosts/agentic-mermaid-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentic-mermaid-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentic-mermaid-dev/vendors/agentic-mermaid-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentic-mermaid-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentic-mermaid-dev/packages/agentic-mermaid-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/agentic-mermaid-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/agentic-mermaid-dev/packages/agentic-mermaid-dev-packages.yml
  title: ''
  type: Packages
  url: packages/agentic-mermaid-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/agentic-mermaid-dev/security/agentic-mermaid-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentic-mermaid-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentic-mermaid.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentic-mermaid.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://agentic-mermaid.dev/demo/
coverage:
  checked: '2026-11-01'
  detail: Documentation provides a Library API but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://agentic-mermaid.dev/docs/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agentic Mermaid turns agent prompts into beautiful, verified Mermaid diagrams with deterministic layout, 16 styles, 20 palettes, and output options including SVG, PNG, ASCII, and Unicode. It offers a library, CLI, and MCP integration for typed edits and layout JSON for coordinate-aware tools.
image: https://agentic-mermaid.dev/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at agentic-mermaid.dev.
  name: Agentic Mermaid MCP Server
  slug: agentic-mermaid-dev-mcp-yml
modified: '2026-11-01'
name: Agentic Mermaid
nav: Providers
network: true
overview: 'Agentic Mermaid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Diagram Generation, Visualization, Mermaid, AI Agents, and CLI.


  Agentic Mermaid''s developer surface includes CLI, changelog, documentation, getting-started guide, and 10 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 6
  name: Agentic Mermaid Dev Rate Limits
  slug: agentic-mermaid-dev-rate-limits
scopes:
- name: Agentic Mermaid Dev Scopes
  scope_count: 0
  slug: agentic-mermaid-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 56.7
    operational_transparency: 47.4
  previous_composite: 19.1
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
security:
- kind: authentication
  name: Agentic Mermaid Dev Authentication
  slug: agentic-mermaid-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentic Mermaid Dev Domain Security
  slug: agentic-mermaid-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentic-mermaid-dev
tags:
- Diagram Generation
- Visualization
- Mermaid
- AI Agents
- CLI
website: https://agentic-mermaid.dev/
---
