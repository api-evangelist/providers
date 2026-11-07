---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP for Cursor, Claude Desktop, and Claude Code
  name: MCP
  slug: mcp
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/agentexec-dev/plans/agentexec-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentexec-dev-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/agentexec-dev/sandbox/agentexec-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agentexec-dev-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/agentexec-dev/authentication/agentexec-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentexec-dev-authentication.yml
- group: agent
  href: https://artifacts.apis.io/agentexec-dev/llms/agentexec-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentexec-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentexec-dev/a2a/agentexec-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentexec-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentexec-dev/mcp/agentexec-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentexec-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentexec-dev/well-known/agentexec-dev-x402-list-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentexec-dev-x402-list-security.txt
- group: agent
  href: https://artifacts.apis.io/agentexec-dev/well-known/agentexec-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentexec-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentexec-dev/hosts/agentexec-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentexec-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentexec-dev/vendors/agentexec-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentexec-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentexec-dev/packages/agentexec-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/agentexec-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/agentexec-dev/packages/agentexec-dev-packages.yml
  title: ''
  type: Packages
  url: packages/agentexec-dev-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.agentexec.dev`
- group: auth
  href: https://artifacts.apis.io/agentexec-dev/security/agentexec-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentexec-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentexec.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentexec.dev/docs/mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentexec.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentexec.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Har50
- group: start
  title: ''
  type: GettingStarted
  url: https://agentexec.dev/docs/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://agentexec.dev/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://agentexec.dev/#portal
- group: docs
  title: ''
  type: APIReference
  url: https://agentexec.dev/docs/mcp
coverage:
  checked: '2026-11-03'
  detail: Documentation is available but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found.
  evidence:
  - status: 200
    url: https://agentexec.dev/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AgentExec provides an on-chain execution gateway and WebMCP tool discovery platform for autonomous AI agents on Base Mainnet. It enables programmable money rails, allowing agents to manage treasuries, perform automated Tenderly dry‑runs, enforce time‑bounded session key permissions, and utilize HTTP 402 micro‑payment paywalls. The service offers documentation, a playground, and pricing details, targeting developers building AI‑driven automation on blockchain.
layout: provider
mcp_servers:
- description: Remote MCP server at api.agentexec.dev.
  name: AgentExec MCP Server
  slug: agentexec-dev-mcp-yml
modified: '2026-10-31'
name: AgentExec
nav: Providers
network: true
overview: 'AgentExec is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Blockchain, WebMCP, and Base.


  AgentExec''s developer surface includes sandbox, authentication, documentation, getting-started guide, pricing, signup flow, API reference, and 16 more developer resources.'
plans:
- name: Agentexec Dev Plans Pricing
  plan_count: 1
  slug: agentexec-dev-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Agentexec Dev Rate Limits
  slug: agentexec-dev-rate-limits
scopes:
- name: Agentexec Dev Scopes
  scope_count: 0
  slug: agentexec-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 61.7
    operational_transparency: 13.2
  previous_composite: 24.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentexec Dev Authentication
  slug: agentexec-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentexec Dev Domain Security
  slug: agentexec-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: agentexec-dev
tags:
- Artificial Intelligence
- Automation
- Blockchain
- WebMCP
- Base
- Finance
website: https://agentexec.dev/
---
