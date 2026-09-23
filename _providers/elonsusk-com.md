---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Elonsusk Com Agentic Access
  operation_count: 23
  slug: elonsusk-com-agentic-access
  summary_line: 23 operations · 6 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://a2a.elonsusk.com
  baseurl_source: declared
  description: The HTTP surface of the Sandbox Contractor Agent, published as an OpenAPI 3.1.0 document (FastAPI, info.title "A2A Autonomous Trader Agent", version 0.1.0) at https://a2a.elonsusk.com/openapi.json wit
  name: Sandbox Contractor Agent REST API
  slug: sandbox-contractor-agent-rest-api
- description: 'Agent2Agent protocol surface: an agent card served from https://a2a.elonsusk.com/.well-known/agent-card.json (and the legacy /.well-known/agent.json) declaring protocolVersion "1.0", JSONRPC transport'
  name: Sandbox Contractor Agent (A2A)
  slug: sandbox-contractor-agent-a2a
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://a2a.elonsusk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://a2a.elonsusk.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://a2a.elonsusk.com/redoc
- group: commercial
  title: ''
  type: Pricing
  url: https://a2a.elonsusk.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/a2a/elonsusk-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/elonsusk-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/well-known/elonsusk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elonsusk-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/mcp/elonsusk-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elonsusk-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/llms/elonsusk-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elonsusk-com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/authentication/elonsusk-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elonsusk-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/conventions/elonsusk-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elonsusk-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/errors/elonsusk-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elonsusk-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/data-model/elonsusk-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elonsusk-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/rate-limits/elonsusk-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elonsusk-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/plans/elonsusk-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elonsusk-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/conformance/elonsusk-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elonsusk-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/lifecycle/elonsusk-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elonsusk-com-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/packages/elonsusk-com-packages.yml
  title: ''
  type: Packages
  url: packages/elonsusk-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/agentic-access/elonsusk-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elonsusk-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elonsusk-com/refs/heads/main/security/elonsusk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elonsusk-com-domain-security.yml
created: '2026-09-19'
description: 'Artem / A2A Sandbox is a one-operator agent-commerce sandbox that runs a paid "Sandbox Contractor Agent" at a2a.elonsusk.com: an Agent2Agent (A2A) JSON-RPC agent selling 28 skills — keyless developer utilities (JSON/YAML/CSV conversion, hashing incl. keccak256, base64/hex/base58, JWT decode, UUID, semver, epoch), on-chain data reads (EVM and Solana balances, ERC-20 metadata, gas price, transaction status, SPL supply) and security scans (MCP tool-manifest risk, EVM contract bytecode signals) — plus model-backed code review, code generation and inference sold quote-first. Every skill is payable per call over the x402 v2 HTTP payment protocol (HTTP 402 + PAYMENT-REQUIRED challenge, USDC on Base or Solana, from $0.001) at POST /x402/{skill}, or through a classic multi-chain crypto invoice (SOL, USDC, ETH, BTC) on the REST task API. The same FastAPI origin publishes an OpenAPI 3.1.0 contract at /openapi.json with Swagger UI at /docs, an A2A agent card at /.well-known/agent-card.json,
  an x402 discovery document at /.well-known/x402.json, and live health and revenue-metrics endpoints. The registrable domain elonsusk.com itself serves no website (TLS refused, HTTP 401); the a2a subdomain is the whole public surface.'
layout: provider
mcp_servers:
- description: ''
  name: Artem / A2A Sandbox MCP Server
  slug: artem-a2a-sandbox-mcp-server
modified: '2026-09-19'
name: Artem / A2A Sandbox
nav: Providers
network: true
overview: 'Artem / A2A Sandbox publishes 1 API on the [APIs.io](https://apis.io/) network: Sandbox Contractor Agent REST API. Tagged areas include Agents, Agentic Commerce, A2A, x402, and Developer Tools.


  Artem / A2A Sandbox''s developer surface includes documentation, API reference, pricing, authentication, and 16 more developer resources.'
plans:
- name: Elonsusk Com Plans Pricing
  plan_count: 3
  slug: elonsusk-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Elonsusk Com Rate Limits
  slug: elonsusk-com-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 36.7
    developer_ergonomics: 30.4
    discoverability: 72.2
    operational_transparency: 0.0
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Elonsusk Com Authentication
  slug: elonsusk-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Elonsusk Com Domain Security
  slug: elonsusk-com-domain-security
  summary_line: TLSv1.2
slug: elonsusk-com
tags:
- Agents
- Agentic Commerce
- A2A
- x402
- Developer Tools
- Blockchain
- Solana
- Ethereum
- Security
- Code Review
- Code Generation
- Agent-Native
website: https://a2a.elonsusk.com/
---
