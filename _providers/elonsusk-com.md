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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Elonsusk Com Agentic Access
  operation_count: 23
  slug: elonsusk-com-agentic-access
  summary_line: 23 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'Agent2Agent protocol surface: an agent card served from https://a2a.elonsusk.com/.well-known/agent-card.json (and the legacy /.well-known/agent.json) declaring protocolVersion "1.0", JSONRPC transport'
  name: Sandbox Contractor Agent (A2A)
  slug: sandbox-contractor-agent-a2a
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The A2a API from Artem / A2A Sandbox — 1 operation(s) for a2a.
  name: Artem / A2A Sandbox A2a API
  slug: elonsusk-com-a2a-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The A2A Autonomous Trader Agent API from Artem / A2A Sandbox — 1 operation(s) for a2a autonomous trader agent.
  name: Artem / A2A Sandbox A2A Autonomous Trader Agent API
  slug: elonsusk-com-a2a-autonomous-trader-agent-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Health API from Artem / A2A Sandbox — 1 operation(s) for health.
  name: Artem / A2A Sandbox Health API
  slug: elonsusk-com-health-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Healthz API from Artem / A2A Sandbox — 1 operation(s) for healthz.
  name: Artem / A2A Sandbox Healthz API
  slug: elonsusk-com-healthz-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Healthz.earn.superteam API from Artem / A2A Sandbox — 1 operation(s) for healthz.earn.superteam.
  name: Artem / A2A Sandbox Healthz.earn.superteam API
  slug: elonsusk-com-healthz-earn-superteam-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Leads API from Artem / A2A Sandbox — 1 operation(s) for leads.
  name: Artem / A2A Sandbox Leads API
  slug: elonsusk-com-leads-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Metrics API from Artem / A2A Sandbox — 1 operation(s) for metrics.
  name: Artem / A2A Sandbox Metrics API
  slug: elonsusk-com-metrics-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Payments API from Artem / A2A Sandbox — 1 operation(s) for payments.
  name: Artem / A2A Sandbox Payments API
  slug: elonsusk-com-payments-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Showcase API from Artem / A2A Sandbox — 5 operation(s) for showcase.
  name: Artem / A2A Sandbox Showcase API
  slug: elonsusk-com-showcase-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The Tasks API from Artem / A2A Sandbox — 3 operation(s) for tasks.
  name: Artem / A2A Sandbox Tasks API
  slug: elonsusk-com-tasks-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The .well Known API from Artem / A2A Sandbox — 5 operation(s) for .well known.
  name: Artem / A2A Sandbox .well Known API
  slug: elonsusk-com-well-known-api
- baseURL: https://a2a.elonsusk.com/a2a
  baseurl_source: declared
  description: The X402 API from Artem / A2A Sandbox — 1 operation(s) for x402.
  name: Artem / A2A Sandbox X402 API
  slug: elonsusk-com-x402-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/elonsusk-com/overlays/elonsusk-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elonsusk-com-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/elonsusk-com/a2a/elonsusk-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/elonsusk-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/elonsusk-com/well-known/elonsusk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elonsusk-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/elonsusk-com/mcp/elonsusk-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elonsusk-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/elonsusk-com/llms/elonsusk-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elonsusk-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/elonsusk-com/authentication/elonsusk-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elonsusk-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/elonsusk-com/conventions/elonsusk-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elonsusk-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/elonsusk-com/errors/elonsusk-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elonsusk-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elonsusk-com/data-model/elonsusk-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elonsusk-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/elonsusk-com/rate-limits/elonsusk-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elonsusk-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/elonsusk-com/plans/elonsusk-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elonsusk-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/elonsusk-com/conformance/elonsusk-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elonsusk-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/elonsusk-com/lifecycle/elonsusk-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elonsusk-com-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/elonsusk-com/packages/elonsusk-com-packages.yml
  title: ''
  type: Packages
  url: packages/elonsusk-com-packages.yml
- group: agent
  href: https://artifacts.apis.io/elonsusk-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/elonsusk-com/agentic-access/elonsusk-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elonsusk-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/elonsusk-com/security/elonsusk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elonsusk-com-domain-security.yml
created: '2026-09-19'
description: 'Artem / A2A Sandbox is a one-operator agent-commerce sandbox that runs a paid "Sandbox Contractor Agent" at a2a.elonsusk.com: an Agent2Agent (A2A) JSON-RPC agent selling 28 skills — keyless developer utilities (JSON/YAML/CSV conversion, hashing incl. keccak256, base64/hex/base58, JWT decode, UUID, semver, epoch), on-chain data reads (EVM and Solana balances, ERC-20 metadata, gas price, transaction status, SPL supply) and security scans (MCP tool-manifest risk, EVM contract bytecode signals) — plus model-backed code review, code generation and inference sold quote-first. Every skill is payable per call over the x402 v2 HTTP payment protocol (HTTP 402 + PAYMENT-REQUIRED challenge, USDC on Base or Solana, from $0.001) at POST /x402/{skill}, or through a classic multi-chain crypto invoice (SOL, USDC, ETH, BTC) on the REST task API. The same FastAPI origin publishes an OpenAPI 3.1.0 contract at /openapi.json with Swagger UI at /docs, an A2A agent card at /.well-known/agent-card.json,
  an x402 discovery document at /.well-known/x402.json, and live health and revenue-metrics endpoints. The registrable domain elonsusk.com itself serves no website (TLS refused, HTTP 401); the a2a subdomain is the whole public surface.'
layout: provider
mcp_servers:
- description: No MCP server exists. https://a2a.elonsusk.com/mcp and /.well-known/mcp.json both return the app's real JSON 404, no MCP package is published in any registry, and neither the agent card nor the landin
  name: Artem / A2A Sandbox MCP Server
  slug: elonsusk-com-sandbox-contractor
modified: '2026-09-19'
name: Artem / A2A Sandbox
nav: Providers
network: true
overview: 'Artem / A2A Sandbox publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, A2A Autonomous Trader Agent API, Health API, and 10 more. Tagged areas include Agents, Agentic Commerce, A2A, x402, and Developer Tools.


  The Artem / A2A Sandbox catalog on APIs.io includes 1 Spectral governance ruleset.


  Artem / A2A Sandbox''s developer surface includes documentation, API reference, pricing, authentication, and 17 more developer resources.'
plans:
- name: Elonsusk Com Plans Pricing
  plan_count: 3
  slug: elonsusk-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Elonsusk Com Rate Limits
  slug: elonsusk-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Artem / A2A Sandbox API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: elonsusk-com-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 38.9
    developer_ergonomics: 22.0
    discoverability: 69.6
    operational_transparency: 0.0
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
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
screenshot: https://apis.io/screenshots/elonsusk-com/elonsusk-com-2026-10-11T185254.png
security:
- kind: authentication
  name: Elonsusk Com Authentication
  slug: elonsusk-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Elonsusk Com Domain Security
  slug: elonsusk-com-domain-security
  summary_line: TLSv1.2
skill_count: 3
skills:
- name: elonsusk-com-preflight-agent
  slug: elonsusk-com-preflight-agent
- name: elonsusk-com-quote-first-task
  slug: elonsusk-com-quote-first-task
- name: elonsusk-com-x402-pay-per-call
  slug: elonsusk-com-x402-pay-per-call
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
