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
  - sandbox
  trial: false
  try_now: false
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
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Kgninja Dev Agentic Access
  operation_count: 44
  slug: kgninja-dev-agentic-access
  summary_line: 44 operations · 6 acting
api_count: 1
apis:
- description: Remote Model Context Protocol server at https://agent-economy.kgninja.dev/mcp — stateless Streamable HTTP, POST only (GET returns 405), serverInfo dev.kgninja/agent-verification-utility 0.4.3, protoco
  name: Agent Verification Utility MCP Server
  slug: agent-verification-utility-mcp-server
- description: 'Agent2Agent (A2A) 1.0 surface: an agent card served from https://agent-economy.kgninja.dev/.well-known/agent-card.json (supportedInterfaces[] JSONRPC at https://agent-economy.kgninja.dev/a2a, protocol'
  name: Agent Verification Utility A2A Agent
  slug: agent-verification-utility-a2a-agent
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Synchronous A2A 1.0 JSON-RPC quote preparation
  name: KG-NINJA A2a API
  slug: kgninja-dev-a2a-api
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Free use-case selection and request validation before payment
  name: KG-NINJA Decision Support API
  slug: kgninja-dev-decision-support-api
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Machine-readable service discovery
  name: KG-NINJA Discovery API
  slug: kgninja-dev-discovery-api
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Goal-driven revenue measurement and improvement recommendations
  name: KG-NINJA Goals API
  slug: kgninja-dev-goals-api
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Stateless MCP Streamable HTTP transport
  name: KG-NINJA MCP API
  slug: kgninja-dev-mcp-api
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Availability and operational status
  name: KG-NINJA Operations API
  slug: kgninja-dev-operations-api
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Quote and paid verification operations
  name: KG-NINJA Purchase API
  slug: kgninja-dev-purchase-api
- baseURL: https://agent-economy.kgninja.dev/mcp
  baseurl_source: declared
  description: Optional anonymous, short-lived agent registration
  name: KG-NINJA Registration API
  slug: kgninja-dev-registration-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/kgninja-dev/capabilities/kgninja-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kgninja-dev-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/kgninja-dev/security/kgninja-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kgninja-dev-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/kgninja-dev/agentic-access/kgninja-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kgninja-dev-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kgninja-dev/authentication/kgninja-dev-authentication.yml
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
  href: https://artifacts.apis.io/kgninja-dev/a2a/kgninja-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kgninja-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/kgninja-dev/mcp/kgninja-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kgninja-dev-mcp.yml
- group: build
  href: https://artifacts.apis.io/kgninja-dev/mcp/kgninja-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kgninja-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/kgninja-dev/well-known/kgninja-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kgninja-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/kgninja-dev/well-known/kgninja-dev-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/kgninja-dev-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: https://agent-economy.kgninja.dev/robots.txt
- group: agent
  href: https://artifacts.apis.io/kgninja-dev/llms/kgninja-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kgninja-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agent-economy.kgninja.dev/llms.txt
- group: agent
  href: https://artifacts.apis.io/kgninja-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://agent-economy.kgninja.dev/.well-known/agent-skills/verify-json-evidence/SKILL.md
- group: design
  href: https://artifacts.apis.io/kgninja-dev/conventions/kgninja-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kgninja-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/kgninja-dev/conventions/kgninja-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kgninja-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/kgninja-dev/errors/kgninja-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kgninja-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kgninja-dev/data-model/kgninja-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kgninja-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/kgninja-dev/rate-limits/kgninja-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kgninja-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kgninja-dev/plans/kgninja-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kgninja-dev-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/kgninja-dev/sandbox/kgninja-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kgninja-dev-sandbox.yml
- group: design
  href: https://artifacts.apis.io/kgninja-dev/conformance/kgninja-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kgninja-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/kgninja-dev/lifecycle/kgninja-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kgninja-dev-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/kgninja-dev/overlays/kgninja-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kgninja-dev-openapi-overlay.yaml
created: '2026-09-19'
description: KG-NINJA is the operator identity (GitHub user KG-NINJA, Osaka; Cloudflare Wallet handle @kgninja) behind Agent Verification Utility at agent-economy.kgninja.dev, a Cloudflare Workers service (v0.4.3) that runs bounded deterministic checks (SHA-256 equality, JSON Pointer existence/equality/type) over caller-supplied inline JSON and returns an Ed25519-signed execution record, sold to agents per call for 10000 atomic USDC ($0.01) on Base through x402 v2 with no account, API key or OAuth. One origin exposes the product three ways — a 44-operation OpenAPI 3.1.0 contract at /openapi.json, a remote Streamable HTTP MCP server at /mcp answering an anonymous tools/list (five tools, one paid), and an A2A 1.0 agent card at /.well-known/agent-card.json with JSON-RPC at /a2a — plus an RFC 9727 API catalog, an MCP Registry server.json, a provider-published Agent Skill, a JWKS, an x402 manifest, llms.txt and Content-Signal. The apex kgninja.dev has no A record; the subdomain is its only web
  presence.
image: https://agent-economy.kgninja.dev/icon.svg
layout: provider
mcp_servers:
- description: KG-NINJA operates ONE remote MCP server at https://agent-economy.kgninja.dev/mcp — the same origin as its website, OpenAPI and A2A endpoint. It is stateless Streamable HTTP, POST only (GET returns 405
  name: KG-NINJA MCP Server
  slug: kgninja-dev-mcp-yml
modified: '2026-09-19'
name: KG-NINJA
nav: Providers
network: true
overview: 'KG-NINJA publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Decision Support API, Discovery API, and 7 more. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The KG-NINJA catalog on APIs.io includes 1 Spectral governance ruleset.


  KG-NINJA''s developer surface includes authentication, documentation, getting-started guide, API reference, FAQ, pricing, sandbox, and 24 more developer resources.'
plans:
- name: Kgninja Dev Plans Pricing
  plan_count: 1
  slug: kgninja-dev-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Kgninja Dev Rate Limits
  slug: kgninja-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: KG-NINJA API Rules
  rule_count: 53
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 4
  slug: kgninja-dev-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 46.9
    developer_ergonomics: 40.5
    discoverability: 75.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 8
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
screenshot: https://apis.io/screenshots/kgninja-dev/kgninja-dev-2026-10-11T110121.png
security:
- kind: authentication
  name: Kgninja Dev Authentication
  slug: kgninja-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kgninja Dev Domain Security
  slug: kgninja-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 1
skills:
- name: verify-json-evidence
  slug: kgninja-dev-verify-json-evidence
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
- Agent-Native
- Japan
website: https://agent-economy.kgninja.dev/
---
