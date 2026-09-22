---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.9
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Kgninja Dev Agentic Access
  operation_count: 44
  slug: kgninja-dev-agentic-access
  summary_line: 44 operations · 6 acting
api_count: 3
apis:
- baseURL: https://agent-economy.kgninja.dev
  baseurl_source: declared
  description: 'REST contract for the Agent Verification Utility: a free precheck (POST /validate-request) that binds a verification request and an explicit spend policy into an unsigned receipt, a free quote (POST /'
  name: Agent Verification Utility API
  slug: agent-verification-utility-api
- description: Remote Model Context Protocol server at https://agent-economy.kgninja.dev/mcp — stateless Streamable HTTP, POST only (GET returns 405), serverInfo dev.kgninja/agent-verification-utility 0.4.3, protoco
  name: Agent Verification Utility MCP Server
  slug: agent-verification-utility-mcp-server
- description: 'Agent2Agent (A2A) 1.0 surface: an agent card served from https://agent-economy.kgninja.dev/.well-known/agent-card.json (supportedInterfaces[] JSONRPC at https://agent-economy.kgninja.dev/a2a, protocol'
  name: Agent Verification Utility A2A Agent
  slug: agent-verification-utility-a2a-agent
artifact_total: 10
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/security/kgninja-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kgninja-dev-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/agentic-access/kgninja-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kgninja-dev-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/authentication/kgninja-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kgninja-dev-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://agent-economy.kgninja.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agent-economy.kgninja.dev/docs/deterministic-json-verification
- group: start
  title: ''
  type: GettingStarted
  url: https://agent-economy.kgninja.dev/index.md
- group: docs
  title: ''
  type: APIReference
  url: https://agent-economy.kgninja.dev/openapi.json
- group: operate
  title: ''
  type: FAQ
  url: https://agent-economy.kgninja.dev/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://agent-economy.kgninja.dev/agent.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KG-NINJA
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/a2a/kgninja-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kgninja-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/mcp/kgninja-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kgninja-dev-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/mcp/kgninja-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kgninja-dev-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/well-known/kgninja-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kgninja-dev-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/well-known/kgninja-dev-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/kgninja-dev-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: https://agent-economy.kgninja.dev/robots.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/llms/kgninja-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kgninja-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agent-economy.kgninja.dev/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://agent-economy.kgninja.dev/.well-known/agent-skills/verify-json-evidence/SKILL.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/conventions/kgninja-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kgninja-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/conventions/kgninja-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kgninja-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/errors/kgninja-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kgninja-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/data-model/kgninja-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kgninja-dev-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/rate-limits/kgninja-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kgninja-dev-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/plans/kgninja-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kgninja-dev-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/sandbox/kgninja-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kgninja-dev-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/conformance/kgninja-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kgninja-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/lifecycle/kgninja-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kgninja-dev-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kgninja-dev/refs/heads/main/overlays/kgninja-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kgninja-dev-openapi-overlay.yaml
created: '2026-09-19'
description: KG-NINJA is the operator identity (GitHub user KG-NINJA, Osaka; Cloudflare Wallet handle @kgninja) behind Agent Verification Utility at agent-economy.kgninja.dev, a Cloudflare Workers service (v0.4.3) that runs bounded deterministic checks (SHA-256 equality, JSON Pointer existence/equality/type) over caller-supplied inline JSON and returns an Ed25519-signed execution record, sold to agents per call for 10000 atomic USDC ($0.01) on Base through x402 v2 with no account, API key or OAuth. One origin exposes the product three ways — a 44-operation OpenAPI 3.1.0 contract at /openapi.json, a remote Streamable HTTP MCP server at /mcp answering an anonymous tools/list (five tools, one paid), and an A2A 1.0 agent card at /.well-known/agent-card.json with JSON-RPC at /a2a — plus an RFC 9727 API catalog, an MCP Registry server.json, a provider-published Agent Skill, a JWKS, an x402 manifest, llms.txt and Content-Signal. The apex kgninja.dev has no A record; the subdomain is its only web
  presence.
image: https://agent-economy.kgninja.dev/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: KG-NINJA MCP Server
  slug: kg-ninja-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP)
  slug: mcp-endpoint-streamable-http
modified: '2026-09-19'
name: KG-NINJA
nav: Providers
network: true
overview: 'KG-NINJA publishes 1 API on the [APIs.io](https://apis.io/) network: Agent Verification Utility API. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  KG-NINJA''s developer surface includes authentication, documentation, getting-started guide, API reference, FAQ, pricing, sandbox, and 23 more developer resources.'
plans:
- name: Kgninja Dev Plans Pricing
  plan_count: 1
  slug: kgninja-dev-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Kgninja Dev Rate Limits
  slug: kgninja-dev-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 54.8
    discoverability: 81.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: first-party
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
  name: Kgninja Dev Authentication
  slug: kgninja-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kgninja Dev Domain Security
  slug: kgninja-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: kgninja-dev
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Verification
- JSON
- Cryptography
- Cloudflare Workers
- agent-native
- Japan
website: https://agent-economy.kgninja.dev/
---
