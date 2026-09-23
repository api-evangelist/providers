---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.7
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Babyblueviper Com Agentic Access
  operation_count: 187
  slug: babyblueviper-com-agentic-access
  summary_line: 187 operations · 63 acting
api_count: 1
apis:
- baseURL: https://api.babyblueviper.com
  baseurl_source: declared
  description: 'REST API on api.babyblueviper.com (FastAPI, OpenAPI 3.1.0, version 1.13.0, 174 paths / 187 operations): pre-action review verdicts, signed proofs, witnessing, the public verdict ledger and conformance'
  name: invinoveritas API
  slug: invinoveritas-api
- description: 'Remote MCP server (streamable HTTP, protocol 2025-06-18) at https://api.babyblueviper.com/mcp exposing 31 tools with inputSchema, pricing and annotations: review, reason, decision, signals, markets_ac'
  name: invinoveritas MCP Server
  slug: invinoveritas-mcp-server
- description: A2A agent "invinoveritas-reasoning-agent" (protocolVersion 0.3.0, JSONRPC transport) at https://api.babyblueviper.com/a2a with 15 skills mirroring the MCP tools. The agent card is served at both the c
  name: invinoveritas A2A Agent
  slug: invinoveritas-a2a-agent
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/agentic-access/babyblueviper-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/babyblueviper-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/security/babyblueviper-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/babyblueviper-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://babyblueviper.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.babyblueviper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.babyblueviper.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.babyblueviper.com/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://api.babyblueviper.com/install
- group: commercial
  title: ''
  type: Pricing
  url: https://api.babyblueviper.com/billing/plans
- group: operate
  title: ''
  type: Roadmap
  url: https://api.babyblueviper.com/roadmap
- group: operate
  title: ''
  type: Support
  url: https://github.com/babyblueviper1/invinoveritas/issues
- group: company
  title: ''
  type: Blog
  url: https://www.babyblueviper.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.babyblueviper.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/babyblueviper1
- group: build
  title: ''
  type: GitHub
  url: https://github.com/babyblueviper1/invinoveritas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.babyblueviper.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.babyblueviper.com/privacy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/changelog/babyblueviper-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/babyblueviper-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/babyblueviper1/invinoveritas/releases
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/a2a/babyblueviper-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/babyblueviper-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/mcp/babyblueviper-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/babyblueviper-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/mcp/babyblueviper-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/babyblueviper-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/llms/babyblueviper-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/babyblueviper-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/well-known/babyblueviper-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/babyblueviper-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/well-known/babyblueviper-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/babyblueviper-com-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/packages/babyblueviper-com-packages.yml
  title: ''
  type: Packages
  url: packages/babyblueviper-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/packages/babyblueviper-com-packages.yml
  title: ''
  type: SDKs
  url: packages/babyblueviper-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/cli/babyblueviper-com-cli.yml
  title: ''
  type: CLI
  url: cli/babyblueviper-com-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/authentication/babyblueviper-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/babyblueviper-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/scopes/babyblueviper-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/babyblueviper-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/conventions/babyblueviper-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/babyblueviper-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/errors/babyblueviper-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/babyblueviper-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/lifecycle/babyblueviper-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/babyblueviper-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/conformance/babyblueviper-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/babyblueviper-com-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/plans/babyblueviper-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/babyblueviper-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/rate-limits/babyblueviper-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/babyblueviper-com-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/sandbox/babyblueviper-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/babyblueviper-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/data-model/babyblueviper-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/babyblueviper-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/babyblueviper-com/refs/heads/main/overlays/babyblueviper-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/babyblueviper-com-openapi-overlay.yaml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://api.babyblueviper.com/privacy
created: '2026-09-19'
description: 'invinoveritas, published by Baby Blue Viper, is a verification layer for autonomous agents: a neutral, model-agnostic verdict before an irreversible action (POST /review), a schnorr-signed portable proof after (POST /prove), and a public, Nostr- and Bitcoin-anchored track record (GET /ledger) that anyone can recompute against the published key. It is exposed as a REST API (OpenAPI 3.1, 187 operations on api.babyblueviper.com), a remote MCP server with 31 tools at /mcp (OAuth 2.1 metadata, anonymous tools/list), and an A2A agent with a conformant 0.3.0 agent card. Paid calls settle per call in Bitcoin Lightning sats (Bearer credits or L402), USDC via x402 on Base, or by card through Stripe governance subscriptions; /verify-proof and /ledger are free.'
image: https://api.babyblueviper.com/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: invinoveritas MCP Server
  slug: invinoveritas-mcp-server
- description: ''
  name: Live remote MCP endpoint (streamable HTTP)
  slug: live-remote-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: invinoveritas
nav: Providers
network: true
overview: 'invinoveritas publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Agent Verification, Agent Governance, MCP, and A2A.


  invinoveritas'' developer surface includes documentation, API reference, getting-started guide, pricing, support, engineering blog, GitHub presence, and 33 more developer resources.'
plans:
- name: Babyblueviper Com Plans Pricing
  plan_count: 6
  slug: babyblueviper-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Babyblueviper Com Rate Limits
  slug: babyblueviper-com-rate-limits
scopes:
- name: Babyblueviper Com Scopes
  scope_count: 1
  slug: babyblueviper-com-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 47.0
    developer_ergonomics: 85.7
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Babyblueviper Com Authentication
  slug: babyblueviper-com-authentication
  summary_line: http-bearer/l402/x402/oauth2 · 4 schemes
- kind: domain-security
  name: Babyblueviper Com Domain Security
  slug: babyblueviper-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: babyblueviper-com
tags:
- AI Agents
- Agent Verification
- Agent Governance
- MCP
- A2A
- Bitcoin Lightning
- x402
- Trading
- Cryptographic Proofs
- Agent Marketplace
website: https://babyblueviper.com/
---
