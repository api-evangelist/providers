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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Blacklight provides read‑only MCP endpoint exposing wallet signals.
  name: Blacklight MCP
  slug: blacklight-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/blacklight-observer/llms/blacklight-observer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blacklight-observer-llms.txt
- group: agent
  href: https://artifacts.apis.io/blacklight-observer/mcp/blacklight-observer-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blacklight-observer-mcp.yml
- group: other
  href: https://artifacts.apis.io/blacklight-observer/hosts/blacklight-observer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blacklight-observer-hosts.yml
- group: auth
  href: https://artifacts.apis.io/blacklight-observer/security/blacklight-observer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blacklight-observer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blacklight.observer/
coverage:
  checked: '2026-11-02'
  detail: Only a read‑only MCP HTML page is available; no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://blacklight.observer/mcp.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Blacklight provides deep analytics on Polymarket and Hyperliquid wallet activity, revealing hidden trading flows and performance metrics. The platform offers historical insights into maker and taker behavior, enabling users to understand market dynamics without forecasting future trades.
layout: provider
mcp_servers:
- description: Remote MCP server at blacklight.observer.
  name: Blacklight MCP Server
  slug: blacklight-observer-mcp-yml
modified: '2026-11-02'
name: Blacklight
nav: Providers
network: true
overview: Blacklight is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Cryptocurrency, Analytics, Market Data, and Polymarket.
random_paper: 18
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blacklight Observer Domain Security
  slug: blacklight-observer-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: blacklight-observer
tags:
- Finance
- Cryptocurrency
- Analytics
- Market Data
- Polymarket
website: https://blacklight.observer/
---
