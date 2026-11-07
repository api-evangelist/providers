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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides JSON-RPC MCP endpoint with tools for Dubai real estate data.
  name: DXB Data MCP
  slug: dxb-data-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dxbdata-io/mcp/dxbdata-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dxbdata-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/dxbdata-io/hosts/dxbdata-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dxbdata-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dxbdata-io/vendors/dxbdata-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dxbdata-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dxbdata-io/security/dxbdata-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dxbdata-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dxbdata.io/
created: '2026-11-06'
description: DXB Data provides official Dubai real estate data for AI agents, including live sale prices, price per m2, and rental yields by area, sourced from the Dubai Land Department. The service offers an MCP endpoint for easy integration, a free tier with all tools, and a Pro/API tier with higher limits and priority support.
layout: provider
mcp_servers:
- description: Remote MCP server at dxbdata.io.
  name: DXB Data MCP Server
  slug: dxbdata-io-mcp-yml
modified: '2026-11-06'
name: DXB Data
nav: Providers
network: true
overview: DXB Data is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Artificial Intelligence, Data, Dubai, and MCP.
random_paper: 5
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.3
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dxbdata Io Domain Security
  slug: dxbdata-io-domain-security
  summary_line: TLSv1.3
slug: dxbdata-io
tags:
- Real Estate
- Artificial Intelligence
- Data
- Dubai
- MCP
website: https://dxbdata.io/
---
