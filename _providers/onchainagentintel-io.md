---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: quarter
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free, anonymous remote Model Context Protocol server at https://api.onchainagentintel.io/mcp (Streamable HTTP, protocol version 2025-06-18, serverInfo agent-zero-intel 1.8.0). tools/list answers witho
  name: Agent Zero MCP Server
  slug: agent-zero-mcp-server
- description: 'Agent2Agent surface: an agent card served from https://onchainagentintel.io/.well-known/agent-card.json (mirrored on www and api hosts) naming the JSON-RPC endpoint https://api.onchainagentintel.io/a2'
  name: Agent Zero A2A Agent
  slug: agent-zero-a2a-agent
- baseURL: https://api.onchainagentintel.io
  baseurl_source: declared
  description: Paid endpoints — settle with X-PAYMENT header per x402.
  name: Agent Zero Paid X402 API
  slug: onchainagentintel-io-paid-x402-api
- baseURL: https://api.onchainagentintel.io
  baseurl_source: declared
  description: Free endpoints — no payment, no auth.
  name: Agent Zero Public API
  slug: onchainagentintel-io-public-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/onchainagentintel-io/plans/onchainagentintel-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onchainagentintel-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/onchainagentintel-io/rate-limits/onchainagentintel-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onchainagentintel-io-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/onchainagentintel-io/overlays/onchainagentintel-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onchainagentintel-io-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: https://onchainagentintel.io/.agents/skills/onchain-agent-intel/SKILL.md
- group: auth
  href: https://artifacts.apis.io/onchainagentintel-io/security/onchainagentintel-io-domain-security.yml
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
  href: https://artifacts.apis.io/onchainagentintel-io/a2a/onchainagentintel-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/onchainagentintel-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/onchainagentintel-io/mcp/onchainagentintel-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/onchainagentintel-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/onchainagentintel-io/well-known/onchainagentintel-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onchainagentintel-io-well-known.yml
- group: agent
  href: https://artifacts.apis.io/onchainagentintel-io/llms/onchainagentintel-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onchainagentintel-io-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://onchainagentintel.io/llms.txt
- group: agent
  href: https://artifacts.apis.io/onchainagentintel-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/onchainagentintel-io/conformance/onchainagentintel-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onchainagentintel-io-conformance.yml
created: '2026-09-19'
description: 'Agent Zero (On-Chain Agent Intel, onchainagentintel.io) is an agent-native intelligence service for the ERC-8004 agent economy: it continuously indexes the ERC-8004 agents registered on Base and Ethereum, probes their advertised MCP, OpenAPI and .well-known endpoints for liveness, joins on-chain payment activity and ReputationRegistry rows, and scores each agent for buyer-POV readiness and trust. The intelligence is sold per call over the x402 protocol (USDC via EIP-3009 or native ETH, no accounts, no API keys) through a 25-operation OpenAPI 3.1 REST API at https://api.onchainagentintel.io, a free anonymous remote MCP server at /mcp, an A2A agent card at /.well-known/agent-card.json, an x402 Bazaar discovery manifest, an llms.txt and a published Agent Skill. It also sells Solidity security audits and ERC-8183 deliverable evaluations, and is itself ERC-8004 agentId 19353 on Base.'
finops:
- has_sources: true
  method: derived
  name: Onchainagentintel Io Finops
  primary_unit: call
  service_category: ''
  slug: onchainagentintel-io-finops
  template: false
image: https://onchainagentintel.io/logo.png
layout: provider
mcp_servers:
- description: Agent Zero operates a free, anonymous remote MCP server at https://api.onchainagentintel.io/mcp (Streamable HTTP; a GET or a POST without Accept text/event-stream returns 406 -32600 "Client must accep
  name: Agent Zero MCP Server
  slug: agent-zero-intel
modified: '2026-09-19'
name: Agent Zero
nav: Providers
network: true
overview: 'Agent Zero publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Paid X402 API, Public API, and 2 more. Tagged areas include Agents, Agent Intelligence, ERC-8004, x402, and Agentic Commerce.


  The Agent Zero catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Zero''s developer surface includes documentation, API reference, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Onchainagentintel Io Plans Pricing
  plan_count: 11
  slug: onchainagentintel-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Onchainagentintel Io Rate Limits
  slug: onchainagentintel-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Agent Zero API Rules
  rule_count: 58
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 4
  slug: onchainagentintel-io-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 51.3
    contract_governance: 31.8
    contract_quality: 52.8
    developer_ergonomics: 31.0
    discoverability: 75.0
    operational_transparency: 15.8
  previous_composite: 47.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/onchainagentintel-io/onchainagentintel-io-2026-10-11T111850.png
security:
- kind: authentication
  name: Onchainagentintel Io Authentication
  slug: onchainagentintel-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Onchainagentintel Io Domain Security
  slug: onchainagentintel-io-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: onchain-agent-intel
  slug: onchainagentintel-io-onchain-agent-intel
- name: Buy a 30-day flat-rate subscription and query intel with it
  slug: onchainagentintel-io-subscribe-and-query
- name: Vet a counterparty ERC-8004 agent before transacting
  slug: onchainagentintel-io-vet-counterparty-agent
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
- Agent-Native
website: https://onchainagentintel.io/
---
