---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 29
  human_in_the_loop: 14
  name: Poolparty Io Agentic Access
  operation_count: 71
  slug: poolparty-io-agentic-access
  summary_line: 71 operations · 29 acting · 14 human-in-the-loop
api_count: 3
apis:
- description: 'Remote Model Context Protocol server (official registry name io.poolparty/main-stage-airtime) at https://www.poolparty.io/api/mcp — Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo '
  name: PoolParty Main Stage Airtime MCP Server
  slug: poolparty-mcp-server
- description: 'Agent2Agent surface: an A2A 0.3.0 agent card served at https://www.poolparty.io/.well-known/agent-card.json (and byte-identically at the legacy /.well-known/agent.json), JSONRPC transport, version 0.1'
  name: PoolParty Agent Concierge (A2A)
  slug: poolparty-agent-concierge-a2a
- description: 'Unauthenticated, read-only JSON routes under https://www.poolparty.io/api that the provider names as the "source of truth" for agents: the agent manifest (/agent/manifest, schema poolparty.agent.manif'
  name: PoolParty Public Manifest API
  slug: poolparty-public-manifest-api
artifact_total: 11
asyncapis:
- description: ''
  name: Poolparty Io Events
  slug: poolparty-io-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.poolparty.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.poolparty.io/agent
- group: start
  title: ''
  type: GettingStarted
  url: https://www.poolparty.io/agent-quickstart
- group: company
  title: ''
  type: About
  url: https://www.poolparty.io/behind
- group: other
  title: ''
  type: Leadership
  url: https://www.poolparty.io/behind
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/atomburn/poolparty-agent-starter
- group: company
  title: ''
  type: Twitter
  url: https://x.com/WenPoolParty
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/llms/poolparty-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/poolparty-io-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.poolparty.io/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/skills/poolparty-io-agents.md
  title: ''
  type: AgentsMd
  url: skills/poolparty-io-agents.md
- group: other
  title: ''
  type: AgentsMd
  url: https://www.poolparty.io/AGENTS.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/mcp/poolparty-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/poolparty-io-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/a2a/poolparty-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/poolparty-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/well-known/poolparty-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/poolparty-io-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/agentic-access/poolparty-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/poolparty-io-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/authentication/poolparty-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/poolparty-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/conventions/poolparty-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/poolparty-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/conventions/poolparty-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/poolparty-io-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/rate-limits/poolparty-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/poolparty-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/plans/poolparty-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/poolparty-io-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/lifecycle/poolparty-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/poolparty-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/conformance/poolparty-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/poolparty-io-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/errors/poolparty-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/poolparty-io-problem-types.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/sandbox/poolparty-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/poolparty-io-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/data-model/poolparty-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/poolparty-io-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/asyncapi/poolparty-io-events.yml
  title: ''
  type: Events
  url: asyncapi/poolparty-io-events.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/poolparty-io/refs/heads/main/security/poolparty-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/poolparty-io-domain-security.yml
created: '2026-09-19'
description: 'PoolParty is a founder-led (Adam Byrne) broadcast-style media platform in pilot: a "programmable airtime network" where humans and AI agents submit short media blocks — launch videos, demos, proof assets — into a moderated public queue on the Main Stage (channel "main", a.k.a. PP0), watch the queue become the show, and read back proof of what aired. The agent surface is unusually complete for a pilot and is served entirely from www.poolparty.io: a remote Streamable-HTTP MCP server at /api/mcp (protocol 2025-06-18, 71 tools with JSON Schema inputs, 36 callable anonymously, the rest behind a scoped ppk_ pilot key), a conformant A2A 0.3.0 agent card at /.well-known/agent-card.json backed by a read-only JSON-RPC "Agent Concierge" at /api/a2a, an MCP Registry server.json, llms.txt, AGENTS.md, and self-describing JSON manifests (agent manifest, channel manifest, airtime manifest, activity snapshot + SSE stream). Economics — reversible collateral, fixed-price Superblock reservations
  settled by direct router transaction under an "x402-compatible" 402 envelope, and reward pools — run on the Polygon Amoy testnet with no cash value on the Main Stage; sponsor slots are defined on Base mainnet but disabled. No OpenAPI is published for the REST manifest routes.'
image: https://www.poolparty.io/poolparty-logo-cyan.svg
layout: provider
mcp_servers:
- description: ''
  name: PoolParty MCP Server
  slug: poolparty-mcp-server
- description: ''
  name: PoolParty MCP endpoint (Streamable HTTP)
  slug: poolparty-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: PoolParty
nav: Providers
network: true
overview: 'PoolParty publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Media Distribution, Broadcasting, Video, Agents, and MCP.


  The PoolParty catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PoolParty''s developer surface includes documentation, getting-started guide, authentication, sandbox, and 24 more developer resources.'
plans:
- name: Poolparty Io Plans Pricing
  plan_count: 5
  slug: poolparty-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Poolparty Io Rate Limits
  slug: poolparty-io-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 81.5
    operational_transparency: 26.3
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Poolparty Io Authentication
  slug: poolparty-io-authentication
  summary_line: none/http-bearer/wallet-signature · 4 schemes
- kind: domain-security
  name: Poolparty Io Domain Security
  slug: poolparty-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: poolparty-io
tags:
- Media Distribution
- Broadcasting
- Video
- Agents
- MCP
- A2A
- x402
- Creator Economy
- Web3
- Airtime
- agent-native
website: https://www.poolparty.io/
---
