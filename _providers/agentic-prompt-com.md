---
access_model:
  confidence: low
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
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/agentic-prompt-com/llms/agentic-prompt-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentic-prompt-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentic-prompt-com/mcp/agentic-prompt-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentic-prompt-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentic-prompt-com/hosts/agentic-prompt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentic-prompt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentic-prompt-com/vendors/agentic-prompt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentic-prompt-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentic-prompt-com/security/agentic-prompt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentic-prompt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentic-prompt.com/
- group: agent
  title: ''
  type: MCP
  url: https://agentic-prompt.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://agentic-prompt.com/openapi.json
  - status: 404
    url: https://agentic-prompt.com/openapi.yaml
  - status: 404
    url: https://agentic-prompt.com/swagger.json
  - status: 404
    url: https://agentic-prompt.com/v1/openapi.json
  - status: 404
    url: https://agentic-prompt.com/api-docs
  - status: 404
    url: https://agentic-prompt.com/docs
  - status: 404
    url: https://agentic-prompt.com/redoc
  - status: 404
    url: https://agentic-prompt.com/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agentic Prompt provides a free library of AI‑generated trading prompts designed for Claude and Robinhood’s MCP. Users can automate equity research, risk scoring, options execution, and portfolio management via a simple terminal command that connects Claude directly to Robinhood’s live trading server. The platform offers over 1,000 validated prompts across 15 categories, continuously updated weekly. It emphasizes privacy, includes a disclaimer, and is maintained by Kei Sakai.
image: https://agentic-prompt.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentic-prompt.com.
  name: Agentic Prompt MCP Server
  slug: agentic-prompt-com-mcp-yml
modified: '2026-11-01'
name: Agentic Prompt
nav: Providers
network: true
overview: Agentic Prompt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Trading, Prompts, Claude, and Robinhood.
plans:
- name: Agentic Prompt Com Plans Pricing
  plan_count: 0
  slug: agentic-prompt-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Agentic Prompt Com Rate Limits
  slug: agentic-prompt-com-rate-limits
scopes:
- name: Agentic Prompt Com Scopes
  scope_count: 0
  slug: agentic-prompt-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 4.6
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentic Prompt Com Authentication
  slug: agentic-prompt-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentic Prompt Com Domain Security
  slug: agentic-prompt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentic-prompt-com
tags:
- Artificial Intelligence
- Trading
- Prompts
- Claude
- Robinhood
website: https://agentic-prompt.com/
---
