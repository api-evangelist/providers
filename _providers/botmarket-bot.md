---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 12.8
  scored_at: '2026-09-20'
api_count: 2
apis:
- description: 'Anonymous JSON read surface for the BotMarket directory at https://botmarket.bot/v1 — documented in llms.txt rather than in a contract: GET /v1/mcps?q=, /v1/agents, /v1/protocols, /v1/quests, /v1/skil'
  name: BotMarket REST API
  slug: botmarket-rest-api
- description: Remote Model Context Protocol server at https://botmarket.bot/mcp (JSON-RPC 2.0 over HTTP, POST only, protocol version 2025-06-18, serverInfo botmarket 3.0.0). initialize, tools/list and tools/call an
  name: BotMarket MCP Server
  slug: botmarket-mcp-server
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/security/botmarket-bot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botmarket-bot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botmarket.bot/
- group: docs
  title: ''
  type: Documentation
  url: https://botmarket.bot/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/koalabs-ai
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/a2a/botmarket-bot-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/botmarket-bot-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/mcp/botmarket-bot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/botmarket-bot-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/well-known/botmarket-bot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botmarket-bot-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/llms/botmarket-bot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botmarket-bot-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/authentication/botmarket-bot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/botmarket-bot-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/conventions/botmarket-bot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/botmarket-bot-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/errors/botmarket-bot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botmarket-bot-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/rate-limits/botmarket-bot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/botmarket-bot-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/plans/botmarket-bot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botmarket-bot-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/conformance/botmarket-bot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botmarket-bot-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/botmarket-bot/refs/heads/main/lifecycle/botmarket-bot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/botmarket-bot-lifecycle.yml
created: '2026-09-19'
description: 'KOA Labs is a one-person "solo + AI" software studio in Mexico City (koalabs.ai) that builds open protocols, registries and directories, and BotMarket (botmarket.bot) is its free, non-profit marketplace and registry for AI agents and MCP servers — 115,065 MCP servers, 3,615 A2A-style agents and 25 agent and payment protocols re-gathered hourly from public catalogs (Glama, mcp.so, Smithery, the Official MCP Registry, Hugging Face, Docker, x402 Bazaar) with every record credited to its source. The surface is anonymous and rate-limited per IP (10/s, 100/min, 1,000/h) with no signup and no token: a documented but unspecified REST read surface at https://botmarket.bot/v1 plus POST /v1/submit with a dry_run flag, and a live remote MCP server at https://botmarket.bot/mcp (protocol 2025-06-18, six read-only tools with real inputSchemas). Discovery is published as llms.txt, an OpenAI ai-plugin.json, an OpenSearch description, an MCP server card and an agent card at /.well-known/agent-card.json
  that is served and owned but not A2A conformant (capabilities is an array, no protocolVersion, no skills, no A2A endpoint). The OpenAPI both llms.txt and ai-plugin.json advertise at /openapi.json is not served (404), so no machine-readable REST contract exists. Optional tipping over x402 / MTP is advertised in a response header; nothing is paywalled.'
image: https://botmarket.bot/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: KOA Labs MCP Server
  slug: koa-labs-mcp-server
- description: ''
  name: BotMarket MCP endpoint (JSON-RPC over HTTP)
  slug: botmarket-mcp-endpoint-json-rpc-over-http
modified: '2026-09-19'
name: KOA Labs
nav: Providers
network: true
overview: 'KOA Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, MCP, A2A, Agent Discovery, and Marketplace.


  KOA Labs'' developer surface includes documentation, authentication, and 13 more developer resources.'
plans:
- name: Botmarket Bot Plans Pricing
  plan_count: 1
  slug: botmarket-bot-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Botmarket Bot Rate Limits
  slug: botmarket-bot-rate-limits
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.5
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    operational_transparency: 36.8
  previous_composite: 5.0
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
  name: Botmarket Bot Authentication
  slug: botmarket-bot-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Botmarket Bot Domain Security
  slug: botmarket-bot-domain-security
  summary_line: TLSv1.3 · HSTS
slug: botmarket-bot
tags:
- Agents
- MCP
- A2A
- Agent Discovery
- Marketplace
- Directory
- Protocol
- x402
- Open Data
- agent-native
- Non-Profit
- Mexico
website: https://botmarket.bot/
---
