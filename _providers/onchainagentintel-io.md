---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-09-21'
api_count: 1
apis:
- baseURL: https://api.onchainagentintel.io
  baseurl_source: declared
  description: REST API for ERC-8004 agent intelligence on Base and Ethereum. Free public operations (coverage stats, leaderboards, per-agent objective signals, capability and chain roll-ups, citable datasets, an em
  name: Agent Zero ERC-8004 Agent Intelligence API
  slug: agent-zero-erc-8004-agent-intelligence-api
- description: Free, anonymous remote Model Context Protocol server at https://api.onchainagentintel.io/mcp (Streamable HTTP, protocol version 2025-06-18, serverInfo agent-zero-intel 1.8.0). tools/list answers witho
  name: Agent Zero MCP Server
  slug: agent-zero-mcp-server
- description: 'Agent2Agent surface: an agent card served from https://onchainagentintel.io/.well-known/agent-card.json (mirrored on www and api hosts) naming the JSON-RPC endpoint https://api.onchainagentintel.io/a2'
  name: Agent Zero A2A Agent
  slug: agent-zero-a2a-agent
artifact_total: 9
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/onchainagentintel-io/refs/heads/main/security/onchainagentintel-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onchainagentintel-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onchainagentintel.io/
- group: docs
  title: ''
  type: Documentation
  url: https://onchainagentintel.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.onchainagentintel.io/v1/public/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://onchainagentintel.io/services
- group: company
  title: ''
  type: Blog
  url: https://onchainagentintel.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://onchainagentintel.io/feed.xml
- group: start
  title: ''
  type: Login
  url: https://app.onchainagentintel.io/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/onchainagentintel-io/refs/heads/main/a2a/onchainagentintel-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/onchainagentintel-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onchainagentintel-io/refs/heads/main/mcp/onchainagentintel-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/onchainagentintel-io-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onchainagentintel-io/refs/heads/main/well-known/onchainagentintel-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onchainagentintel-io-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onchainagentintel-io/refs/heads/main/llms/onchainagentintel-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onchainagentintel-io-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://onchainagentintel.io/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/onchainagentintel-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/onchainagentintel-io/refs/heads/main/conformance/onchainagentintel-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onchainagentintel-io-conformance.yml
created: '2026-09-19'
description: 'Agent Zero (On-Chain Agent Intel, onchainagentintel.io) is an agent-native intelligence service for the ERC-8004 agent economy: it continuously indexes the ERC-8004 agents registered on Base and Ethereum, probes their advertised MCP, OpenAPI and .well-known endpoints for liveness, joins on-chain payment activity and ReputationRegistry rows, and scores each agent for buyer-POV readiness and trust. The intelligence is sold per call over the x402 protocol (USDC via EIP-3009 or native ETH, no accounts, no API keys) through a 25-operation OpenAPI 3.1 REST API at https://api.onchainagentintel.io, a free anonymous remote MCP server at /mcp, an A2A agent card at /.well-known/agent-card.json, an x402 Bazaar discovery manifest, an llms.txt and a published Agent Skill. It also sells Solidity security audits and ERC-8183 deliverable evaluations, and is itself ERC-8004 agentId 19353 on Base.'
image: https://onchainagentintel.io/logo.png
layout: provider
mcp_servers:
- description: Agent Zero operates a free, anonymous remote MCP server at https://api.onchainagentintel.io/mcp (Streamable HTTP; a GET or a POST without Accept text/event-stream returns 406 -32600 "Client must accep
  name: Agent Zero MCP Server
  slug: agent-zero-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP)
  slug: mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Agent Zero
nav: Providers
network: true
overview: 'Agent Zero publishes 1 API on the [APIs.io](https://apis.io/) network: ERC-8004 Agent Intelligence API. Tagged areas include Agents, Agent Intelligence, ERC-8004, x402, and Agentic Commerce.


  Agent Zero''s developer surface includes documentation, API reference, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Onchainagentintel Io Plans Pricing
  plan_count: 5
  slug: onchainagentintel-io-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Onchainagentintel Io Rate Limits
  slug: onchainagentintel-io-rate-limits
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 50.4
    developer_ergonomics: 50.0
    discoverability: 75.9
    operational_transparency: 15.8
  previous_composite: 44.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Onchainagentintel Io Authentication
  slug: onchainagentintel-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Onchainagentintel Io Domain Security
  slug: onchainagentintel-io-domain-security
  summary_line: TLSv1.3
slug: onchainagentintel-io
tags:
- Agents
- Agent Intelligence
- ERC-8004
- x402
- Agentic Commerce
- Blockchain
- Ethereum
- Base
- Web3
- MCP
- A2A
- Smart Contracts
- Security Audits
- agent-native
website: https://onchainagentintel.io/
---
