---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Official Model Context Protocol server providing AI agents access to OP.GG game data for League of Legends, Teamfight Tactics, and Valorant over Streamable HTTP.
  name: OP.GG MCP Server
  slug: opgg-mcp-server
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://op.gg
- group: company
  title: ''
  type: About
  url: https://op.gg/lol/about
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opgg-mcp.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/opgginc/opgg-mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opgginc
- group: company
  title: ''
  type: Blog
  url: https://log.op.gg
- group: operate
  title: ''
  type: Support
  url: https://help.op.gg/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://op.gg/lol/policies/agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://op.gg/lol/policies/privacy
- group: build
  title: ''
  type: Packages
  url: packages/opgg-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opgg-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/opgg-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opgg-domain-security.yml
created: '2026-07-17'
description: OP.GG is the world's leading League of Legends statistics and performance tracking platform. Founded in Seoul, South Korea and launched in 2013, it grew from a LoL stats search engine into a global gaming platform serving tens of millions of monthly active users across games including League of Legends, Valorant, Teamfight Tactics, Overwatch 2, and PUBG. OP.GG surfaces summoner ranks, win rates, champion mastery, builds, tier lists, match history, and live meta trends. Its programmatic surface centers on an official, hosted Model Context Protocol (MCP) server that gives AI agents access to LoL, TFT, and Valorant game data, plus first-party AI-readable ai.json summoner/match snapshot endpoints advertised in its published llms.txt. OP.GG is backed by 500 Global, SBVA, DS Asset Management, Dunamu & Partners, and others.
image: https://op.gg/images/logo/logo.svg
layout: provider
mcp_servers:
- description: Official Model Context Protocol server that provides AI agents with access to OP.GG game data for League of Legends, Teamfight Tactics, and Valorant.
  name: OPGG MCP Server
  slug: opgg-mcp-server
modified: '2026-07-20'
name: OPGG
nav: Providers
network: true
overview: 'OPGG publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Esports, Game Data, and Analytics.


  OPGG''s developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.5
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opgg/refs/heads/main/screenshots/opgg-2026-08-07T190721.png
security:
- kind: domain-security
  name: Opgg Domain Security
  slug: opgg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opgg
tags:
- Company
- Gaming
- Esports
- Game Data
- Analytics
- League of Legends
- VALORANT
- Statistics
- MCP
website: https://op.gg
---
