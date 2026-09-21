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
api_count: 3
apis:
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://grokandmon.com/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 2.1.0, graded conformant on shape) a'
  name: GanjaMon AI A2A Agent
  slug: ganjamon-a2a-agent
- description: Remote Model Context Protocol server at https://grokandmon.com/mcp/v1 (also answers at /mcp; protocol version 2025-06-18, server version 1.0.0). initialize and tools/list answer anonymously with 22 to
  name: GanjaMon MCP Server
  slug: ganjamon-mcp-server
- description: 'The JSON REST origin under https://grokandmon.com/api/ that the website, the MCP tools and the ACP endpoints defer to for live data: sensor history, hourly aggregates, AI decision history, plant progr'
  name: Grok & Mon REST API
  slug: grokandmon-rest-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://grokandmon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://grokandmon.com/a2a.html
- group: commercial
  title: ''
  type: Pricing
  url: https://grokandmon.com/.well-known/x402-pricing.json
- group: other
  title: ''
  type: X
  url: https://x.com/ganjamonai
- group: other
  title: ''
  type: Telegram
  url: https://t.me/ganjamonai
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/a2a/grokandmon-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/grokandmon-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/mcp/grokandmon-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/grokandmon-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/well-known/grokandmon-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/grokandmon-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/llms/grokandmon-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grokandmon-com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/authentication/grokandmon-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grokandmon-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/conventions/grokandmon-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/grokandmon-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/errors/grokandmon-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/grokandmon-com-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/rate-limits/grokandmon-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/grokandmon-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/plans/grokandmon-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/grokandmon-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/conformance/grokandmon-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grokandmon-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/lifecycle/grokandmon-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/grokandmon-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/security/grokandmon-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grokandmon-com-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/grokandmon-com/refs/heads/main/regulatory/grokandmon-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/grokandmon-com-regulatory-posture.yml
created: '2026-09-19'
description: 'Grok & Mon operates GanjaMon AI, an autonomous ERC-8004 agent (agent #4 on Monad) that runs a real cannabis grow tent through IoT sensors and actuators, aggregates trading signals from nine on-chain and social sources, and sells its outputs to other agents. Its published surface is agent-native rather than REST-first: an A2A 0.3.0 agent card at /.well-known/agent-card.json with seven skills, a JSON-RPC endpoint at /a2a/v1, three ACP REST endpoints, a remote MCP server at /mcp/v1 listing 22 grow-tent tools, and an x402 pricing document quoting per-call USDC prices with a 100-request/day free tier. It publishes no OpenAPI, SDK, security.txt or status page, and its /api/* REST origin was unreachable (HTTP 530) when profiled.'
image: https://grokandmon.com/assets/GANJA_MON_brand_logo_powered_by_grok.png
layout: provider
mcp_servers:
- description: ''
  name: Grok & Mon MCP Server
  slug: grok-mon-mcp-server
- description: ''
  name: GanjaMon MCP endpoint (Streamable HTTP)
  slug: ganjamon-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Grok & Mon
nav: Providers
network: true
overview: 'Grok & Mon publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, A2A, MCP, x402, and Agentic Commerce.


  Grok & Mon''s developer surface includes documentation, pricing, authentication, and 15 more developer resources.'
plans:
- name: Grokandmon Com Plans Pricing
  plan_count: 18
  slug: grokandmon-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Grokandmon Com Rate Limits
  slug: grokandmon-com-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.2
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 74.1
    operational_transparency: 21.1
  previous_composite: 2.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Grokandmon Com Authentication
  slug: grokandmon-com-authentication
  summary_line: none/x402-payment/apiKey · 3 schemes
- kind: domain-security
  name: Grokandmon Com Domain Security
  slug: grokandmon-com-domain-security
  summary_line: TLSv1.3
slug: grokandmon-com
tags:
- AI Agents
- A2A
- MCP
- x402
- Agentic Commerce
- Cannabis
- IoT
- Cryptocurrency
- Monad
- Trading Signals
- Generative Art
website: https://grokandmon.com/
---
