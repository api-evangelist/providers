---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hakuto 0209 Com Agentic Access
  operation_count: 16
  slug: hakuto-0209-com-agentic-access
  summary_line: 16 operations
api_count: 2
apis:
- description: Remote Model Context Protocol server at https://mcp.hakuto-0209.com/mcp (Streamable HTTP, POST only — GET returns 406 — protocol version 2025-06-18, serverInfo b612 0.1.0, hosted on Vercel). initializ
  name: b612 MCP Server
  slug: b612-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://mcp.hakuto-0209.com/.well-known/agent-card.json (protocolVersion 0.3, JSONRPC transport, version 0.1.0, provider.organization Hane'
  name: b612 A2A Agent
  slug: b612-a2a-agent
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://hakuto-0209.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.hakuto-0209.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hakuto-0209.com/legal/hakuto-company.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hakuto-0209.com/legal/hakuto-terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hakuto-0209.com/legal/hakuto-privacy.html
- group: operate
  title: ''
  type: Support
  url: https://hakuto-0209.com/#contact
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/a2a/hakuto-0209-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hakuto-0209-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/mcp/hakuto-0209-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hakuto-0209-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/well-known/hakuto-0209-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hakuto-0209-com-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/llms/hakuto-0209-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hakuto-0209-com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/authentication/hakuto-0209-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hakuto-0209-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/conventions/hakuto-0209-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hakuto-0209-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/errors/hakuto-0209-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hakuto-0209-com-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/rate-limits/hakuto-0209-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hakuto-0209-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/plans/hakuto-0209-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hakuto-0209-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/conformance/hakuto-0209-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hakuto-0209-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/lifecycle/hakuto-0209-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hakuto-0209-com-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/agentic-access/hakuto-0209-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hakuto-0209-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hakuto-0209-com/refs/heads/main/security/hakuto-0209-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hakuto-0209-com-domain-security.yml
- group: other
  title: ''
  type: AITransparency
  url: https://mcp.hakuto-0209.com/terms
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://mcp.hakuto-0209.com/terms
- group: other
  title: ''
  type: Subprocessors
  url: https://mcp.hakuto-0209.com/terms
created: '2026-09-19'
description: 'HaneruTo — trading as hakuto, brand B612 SHEEP — is a Japanese one-person, AI-assisted web and systems development studio founded in 2025 that also ships b612, a Japanese-market code-review agent for AI coding assistants: review checklists by target type, industry presets with mandatory Japanese legal checkpoints (景表法 / 特商法 / 薬機法 / インボイス / 電帳法 / 宅建業法 / 介護保険法), failure patterns and 31 deterministic detection rules — no LLM involved; the server has no input for customer source code. b612 is published two ways on mcp.hakuto-0209.com: a remote MCP server at /mcp (Streamable HTTP, protocol 2025-06-18, ten tools with real inputSchemas, anonymous tools/list, keyless principles/rules) and an A2A 0.3 agent whose EdDSA-signed card at /.well-known/agent-card.json declares six skills behind an x-b612-key licence header, with the signing key at /.well-known/jwks.json. No REST/OpenAPI surface, no SDK, no self-serve sign-up; agent access is a monthly flat-fee licence priced on contact.'
image: https://hakuto-0209.com/assets/og.png
layout: provider
mcp_servers:
- description: ''
  name: HaneruTo MCP Server
  slug: haneruto-mcp-server
- description: ''
  name: b612 MCP endpoint (Streamable HTTP)
  slug: b612-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: HaneruTo
nav: Providers
network: true
overview: 'HaneruTo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, MCP, A2A, Code Review, and Static Analysis.


  HaneruTo''s developer surface includes documentation, pricing, support, authentication, and 18 more developer resources.'
plans:
- name: Hakuto 0209 Com Plans Pricing
  plan_count: 2
  slug: hakuto-0209-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Hakuto 0209 Com Rate Limits
  slug: hakuto-0209-com-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hakuto 0209 Com Authentication
  slug: hakuto-0209-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hakuto 0209 Com Domain Security
  slug: hakuto-0209-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hakuto-0209-com
tags:
- Agents
- MCP
- A2A
- Code Review
- Static Analysis
- Developer Tools
- Compliance
- Web Development
- Japan
- Agent-Native
website: https://hakuto-0209.com/
---
