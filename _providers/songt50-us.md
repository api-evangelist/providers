---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-09-20'
api_count: 6
apis:
- description: Agent2Agent agent at https://publicdata-agent.songt50.us — a JSON-RPC 2.0 endpoint at the host root (POST only) with an A2A 0.3.0 agent card at /.well-known/agent-card.json and the legacy /.well-known
  name: Korean Public Data Agent (A2A)
  slug: korean-public-data-agent
- description: Agent2Agent agent at https://news-agent.songt50.us — a JSON-RPC 2.0 endpoint at the host root (POST only) with an A2A 0.3.0 agent card at /.well-known/agent-card.json and /.well-known/agent.json. Five
  name: Korean News Agent (A2A)
  slug: korean-news-agent
- description: 'Model Context Protocol server io.github.SongT-50/korean-public-data-mcp (official MCP registry, active, 1.0.0, published 2026-03-08): six read-only tools over Korean government open data — check_busin'
  name: Korean Public Data MCP Server
  slug: korean-public-data-mcp
- description: 'Model Context Protocol server io.github.SongT-50/korean-news-mcp (official MCP registry, active, 1.0.0, published 2026-03-08): six read-only tools with no API key — korean_news (Naver/Google News by c'
  name: Korean News Hub MCP Server
  slug: korean-news-hub-mcp
- description: 'Model Context Protocol server io.github.SongT-50/korean-stock-mcp (official MCP registry, active, 1.0.0, published 2026-03-08): seven read-only tools over the data.go.kr Financial Services Commission '
  name: Korean Stock Market Data MCP Server
  slug: korean-stock-market-mcp
- description: 'Model Context Protocol server io.github.SongT-50/korean-agriculture-mcp (official MCP registry, active, 1.0.0, published 2026-03-08): six read-only tools over the data.go.kr national public wholesale-'
  name: Korean Agriculture Market Data MCP Server
  slug: korean-agriculture-market-mcp
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://songt50.us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SongT-50
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/SongT-50/korean-public-data-mcp
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/SongT-50
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCSHxaZHNDOrp0h0Ux8_6CVQ
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/a2a/songt50-us-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/songt50-us-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/mcp/songt50-us-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/songt50-us-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://registry.modelcontextprotocol.io/v0/servers?search=io.github.SongT-50
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/well-known/songt50-us-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/songt50-us-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/llms/songt50-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/songt50-us-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/packages/songt50-us-packages.yml
  title: ''
  type: Packages
  url: packages/songt50-us-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/conformance/songt50-us-conformance.yml
  title: ''
  type: Conformance
  url: conformance/songt50-us-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/lifecycle/songt50-us-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/songt50-us-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/authentication/songt50-us-authentication.yml
  title: ''
  type: Authentication
  url: authentication/songt50-us-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/conventions/songt50-us-conventions.yml
  title: ''
  type: Conventions
  url: conventions/songt50-us-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/errors/songt50-us-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/songt50-us-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/rate-limits/songt50-us-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/songt50-us-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/plans/songt50-us-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/songt50-us-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/regulatory/songt50-us-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/songt50-us-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/songt50-us/refs/heads/main/security/songt50-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/songt50-us-domain-security.yml
created: '2026-09-19'
description: sapjilcoding (삽질코딩, GitHub SongT-50) is a Korean independent maker — Song Tae-Eun, a Daejeon wholesale produce market director building AI tools for public data — that publishes two live Agent2Agent (A2A) agents on its own domain songt50.us and four open-source Model Context Protocol servers listed in the official MCP registry. The Korean Public Data Agent answers weather, air quality, apartment prices, Bank of Korea data and business-registration checks; the Korean News Agent searches Korean and global tech news. The MCP servers — Korean Public Data, Korean News Hub, Korean Stock Market Data and Korean Agriculture Market Data (25 tools, Python FastMCP, MIT) — wrap data.go.kr, AirKorea, Bank of Korea ECOS, KRX and the national wholesale-market auction feed. Every surface is read-only, anonymous and free; no OpenAPI or REST contract exists. On 2026-09-19 both A2A agents were live while all four hosted MCP endpoints were suspended (HTTP 503) and the apex site returned Cloudflare
  522.
image: https://raw.githubusercontent.com/SongT-50/korean-public-data-mcp/master/assets/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: sapjilcoding MCP Server
  slug: sapjilcoding-mcp-server
- description: ''
  name: Hosted Streamable HTTP endpoint (suspended when probed)
  slug: hosted-streamable-http-endpoint-suspended-when-probed
- description: ''
  name: server.json (MCP registry manifest)
  slug: serverjson-mcp-registry-manifest
- description: ''
  name: Hosted Streamable HTTP endpoint (suspended when probed)
  slug: hosted-streamable-http-endpoint-suspended-when-probed-2
- description: ''
  name: server.json (MCP registry manifest)
  slug: serverjson-mcp-registry-manifest-2
- description: ''
  name: Hosted Streamable HTTP endpoint (suspended when probed)
  slug: hosted-streamable-http-endpoint-suspended-when-probed-3
- description: ''
  name: server.json (MCP registry manifest)
  slug: serverjson-mcp-registry-manifest-3
- description: ''
  name: Hosted Streamable HTTP endpoint (suspended when probed)
  slug: hosted-streamable-http-endpoint-suspended-when-probed-4
- description: ''
  name: server.json (MCP registry manifest)
  slug: serverjson-mcp-registry-manifest-4
- description: ''
  name: Official MCP registry entries (four servers)
  slug: official-mcp-registry-entries-four-servers
modified: '2026-09-19'
name: sapjilcoding
nav: Providers
network: true
overview: 'sapjilcoding publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, A2A, MCP, Open Data, and Government Data.


  sapjilcoding''s developer surface includes documentation, YouTube channel, authentication, and 17 more developer resources.'
plans:
- name: Songt50 Us Plans Pricing
  plan_count: 3
  slug: songt50-us-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Songt50 Us Rate Limits
  slug: songt50-us-rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.9
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 74.1
    operational_transparency: 5.3
  previous_composite: 2.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Songt50 Us Authentication
  slug: songt50-us-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Songt50 Us Domain Security
  slug: songt50-us-domain-security
  summary_line: TLSv1.3
slug: songt50-us
tags:
- Agents
- A2A
- MCP
- Open Data
- Government Data
- News
- Weather
- Air Quality
- Real-Estate
- Economic Statistics
- Stock Market
- Agriculture
- South Korea
- agent-native
website: https://songt50.us/
---
