---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.6
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 25
  human_in_the_loop: 18
  name: Namewhisper Ai Agentic Access
  operation_count: 44
  slug: namewhisper-ai-agentic-access
  summary_line: 44 operations · 25 acting · 18 human-in-the-loop
api_count: 3
apis:
- description: Public, anonymous remote MCP server (streamable-http, session header mcp-session-id) exposing 44 tools over ENS names - 19 free read tools for search, valuation, market activity, expiring names, wash-
  name: Name Whisper MCP Server
  slug: namewhisper-mcp-server
- description: 'The agent-to-agent surface: an anonymous A2A 0.3.0 JSON-RPC endpoint at https://namewhisper.ai/a2a whose agent card (served at both /.well-known/agent-card.json and the legacy /.well-known/agent.json)'
  name: Name Whisper A2A Agent
  slug: namewhisper-a2a-agent
- description: The REST twins of the MCP tools. The docs state "All MCP tools have equivalent REST endpoints under /api/*. The JSON shapes are the same" and the guide says to POST JSON bodies matching the MCP tool p
  name: Name Whisper REST API
  slug: namewhisper-rest-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://namewhisper.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://namewhisper.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://namewhisper.ai/guide
- group: docs
  title: ''
  type: APIReference
  url: https://namewhisper.ai/llms-full.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://namewhisper.ai/guide#fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://namewhisper.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://namewhisper.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://x.com/namewhisper_ai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/namewhisper_ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eggybug42069
- group: start
  title: ''
  type: X-MCPRegistryListing
  url: https://registry.modelcontextprotocol.io/v0/servers?search=namewhisper
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/a2a/namewhisper-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/namewhisper-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/mcp/namewhisper-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/namewhisper-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/llms/namewhisper-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/namewhisper-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/agentic-access/namewhisper-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/namewhisper-ai-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/well-known/namewhisper-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/namewhisper-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/well-known/namewhisper-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/namewhisper-ai-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/well-known/namewhisper-ai-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/namewhisper-ai-api-catalog.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/authentication/namewhisper-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/namewhisper-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/scopes/namewhisper-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/namewhisper-ai-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/conventions/namewhisper-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/namewhisper-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/conventions/namewhisper-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/namewhisper-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/errors/namewhisper-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/namewhisper-ai-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/rate-limits/namewhisper-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/namewhisper-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/plans/namewhisper-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/namewhisper-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/conformance/namewhisper-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/namewhisper-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/lifecycle/namewhisper-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/namewhisper-ai-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/changelog/namewhisper-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/namewhisper-ai-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/packages/namewhisper-ai-packages.yml
  title: ''
  type: Packages
  url: packages/namewhisper-ai-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/security/namewhisper-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/namewhisper-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/security/namewhisper-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/namewhisper-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://namewhisper.ai/.well-known/security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/namewhisper-ai/refs/heads/main/regulatory/namewhisper-ai-regulatory-posture.yml
  title: ''
  type: X-RegulatoryPosture
  url: regulatory/namewhisper-ai-regulatory-posture.yml
created: '2026-09-19'
description: 'Name Whisper is an ENS (Ethereum Name Service) intelligence layer built for AI agents: natural-language search across 3.5M indexed .eth names, three-track valuation, live market data, wallet portfolios, and non-custodial transaction building for registration, renewal, Seaport listings and offers, resolver records, NameWrapper operations and ERC-8004 / ENSIP-25 agent identity. Everything is exposed as a public, anonymous remote MCP server at https://namewhisper.ai/mcp (44 tools, streamable-http, on the MCP Registry as ai.namewhisper/ens-tools) and an A2A 0.3.0 agent at https://namewhisper.ai/a2a, described by an agent card, an MCP server card, RFC 8414 / 9728 auth metadata, an RFC 9727 api-catalog, an llms.txt and provider-published Agent Skills. Identity is opt-in ERC-8128 signed requests; x402 and MPP payments are wired but dormant. The service never holds keys - every mutating tool returns unsigned calldata for the caller''s wallet. No OpenAPI is published for the REST twins.'
image: https://namewhisper.ai/favicon-512.png
layout: provider
mcp_servers:
- description: 'Name Whisper operates a public, anonymous remote MCP server at https://namewhisper.ai/mcp (streamable-http, session header mcp-session-id) exposing 44 tools over ENS names: search, valuation, market d'
  name: NameWhisper MCP Server
  slug: namewhisper-mcp-server
modified: '2026-09-19'
name: NameWhisper
nav: Providers
network: true
overview: 'NameWhisper publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ENS, Ethereum, Web3, Domain Names, and AI Agents.


  NameWhisper''s developer surface includes documentation, getting-started guide, API reference, pricing, support, authentication, changelog, and 27 more developer resources.'
plans:
- name: Namewhisper Ai Plans Pricing
  plan_count: 1
  slug: namewhisper-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Namewhisper Ai Rate Limits
  slug: namewhisper-ai-rate-limits
scopes:
- name: Namewhisper Ai Scopes
  scope_count: 2
  slug: namewhisper-ai-scopes
  summary_line: 2 scopes · erc8128_signed_request
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 81.5
    operational_transparency: 50.0
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Namewhisper Ai Authentication
  slug: namewhisper-ai-authentication
  summary_line: none/erc8128-signed-request/oauth2-metadata · 4 schemes
- kind: domain-security
  name: Namewhisper Ai Domain Security
  slug: namewhisper-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Namewhisper Ai Vulnerability Disclosure
  slug: namewhisper-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: namewhisper-ai
tags:
- ENS
- Ethereum
- Web3
- Domain Names
- AI Agents
- MCP
- A2A
- Valuation
- NFT Marketplace
- Agent Identity
- Blockchain
website: https://namewhisper.ai/
---
