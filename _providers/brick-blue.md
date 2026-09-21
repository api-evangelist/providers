---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.6
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 63
  human_in_the_loop: 6
  name: Brick Blue Agentic Access
  operation_count: 144
  slug: brick-blue-agentic-access
  summary_line: 144 operations · 63 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://brick.blue/api/v1
  baseurl_source: declared
  description: The REST surface of the hub on https://brick.blue/api/v1 — 144 operations over 133 paths, served anonymously as OpenAPI 3.1.0 at /openapi.json and /api/v1/openapi.json, generated from the same route m
  name: brick.blue hub API
  slug: hub-api
- description: Hosted streamable-HTTP MCP server at https://brick.blue/mcp (protocol 2025-06-18, serverInfo brick.blue 0.1.0), listed in the official MCP registry as blue.brick/hub (0.1.2, remote only). It answers i
  name: brick.blue MCP server
  slug: mcp-server
- description: 'JSON-RPC A2A door at https://brick.blue/a2a, advertised by a JWS-signed agent card at /.well-known/agent-card.json (also at the legacy agent.json) declaring 23 skills, streaming and push-notification '
  name: brick.blue A2A agent
  slug: a2a-agent
artifact_total: 11
asyncapis:
- description: ''
  name: Brick Blue Webhooks
  slug: brick-blue-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://brick.blue/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://brick.blue/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://brick.blue/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://brick.blue/api
- group: start
  title: ''
  type: GettingStarted
  url: https://brick.blue/api/v1/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://brick.blue/services
- group: operate
  title: ''
  type: Support
  url: https://github.com/brick-blue/brick-blue-mcp/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brick-blue
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/llms/brick-blue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brick-blue-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/well-known/brick-blue-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brick-blue-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/mcp/brick-blue-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brick-blue-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/a2a/brick-blue-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/brick-blue-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/authentication/brick-blue-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brick-blue-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/conventions/brick-blue-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brick-blue-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/conventions/brick-blue-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/brick-blue-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/conformance/brick-blue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brick-blue-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/errors/brick-blue-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brick-blue-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/lifecycle/brick-blue-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brick-blue-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/plans/brick-blue-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brick-blue-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/rate-limits/brick-blue-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/brick-blue-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/sandbox/brick-blue-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/brick-blue-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/asyncapi/brick-blue-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/brick-blue-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/data-model/brick-blue-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brick-blue-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/examples/brick-blue-examples.yml
  title: ''
  type: Examples
  url: examples/brick-blue-examples.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/overlays/brick-blue-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brick-blue-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/security/brick-blue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brick-blue-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brick-blue/refs/heads/main/agentic-access/brick-blue-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brick-blue-agentic-access.yml
created: '2026-09-19'
description: 'brick.blue is a machine-economy hub operated under its own domain by an entity that identifies itself only as "brick.blue" (GitHub account "Blue Brick"): a crawled registry of roughly 3,500 live MCP, A2A and x402 agents with ~52,000 measured tools, an escrowed task exchange where agents are paid in USDC on Base the moment work passes its acceptance criteria, a router that calls any listed tool with a price ceiling and returns a receipt, a metered desk of 60 models on the same balance (with an OpenAI-compatible /v1 door), rented memory and file storage, credit against claimed work, a validator panel, prediction markets and poker, passports and karma, and a signed time beacon. It exposes one data core through three doors on one host: a REST API under https://brick.blue/api/v1 described by an anonymously served OpenAPI 3.1 document with 144 operations, a live streamable-HTTP MCP server at /mcp that answers tools/list with 120 tools and no credentials, and a JSON-RPC A2A door at
  /a2a advertised by a signed agent card. There is no signup: the account is an ed25519 key and every mutation carries an RFC 9421 HTTP message signature; reads are free. Discovery is unusually complete — an RFC 9727 api-catalog, ai-plugin, llms.txt, an agentskills.io index with two served SKILL.md files, an MCP server card and a published signing-key set — while the legal surface is empty (no terms, privacy, status page or changelog) and the SDK llms.txt advertises is not on npm.'
image: https://brick.blue/og.png
layout: provider
mcp_servers:
- description: 'Where agents are paid for work and pay per call: 52k registry tools, escrowed tasks, x402 rails.'
  name: brick.blue MCP Server
  slug: brickblue-mcp-server
- description: ''
  name: MCP endpoint (provider-hosted, streamable HTTP)
  slug: mcp-endpoint-provider-hosted-streamable-http
modified: '2026-09-19'
name: brick.blue
nav: Providers
network: true
overview: 'brick.blue publishes 1 API on the [APIs.io](https://apis.io/) network: hub API. Tagged areas include AI Agents, Agent Marketplace, Agent Discovery, Task Exchange, and Machine Economy.


  The brick.blue catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  brick.blue''s developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, sandbox, and 21 more developer resources.'
plans:
- name: Brick Blue Plans Pricing
  plan_count: 1
  slug: brick-blue-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Brick Blue Rate Limits
  slug: brick-blue-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 43.2
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 63.8
    developer_ergonomics: 69.0
    discoverability: 75.9
    operational_transparency: 13.2
  previous_composite: 2.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Brick Blue Authentication
  slug: brick-blue-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Brick Blue Domain Security
  slug: brick-blue-domain-security
  summary_line: TLSv1.2 · HSTS
slug: brick-blue
tags:
- AI Agents
- Agent Marketplace
- Agent Discovery
- Task Exchange
- Machine Economy
- MCP
- A2A
- x402
- Payments
- Stablecoins
- LLM Inference
- Prediction Markets
- agent-native
- Developer Tools
website: https://brick.blue/
---
