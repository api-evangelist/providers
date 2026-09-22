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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.3
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: 01Mind Net Agentic Access
  operation_count: 28
  slug: 01mind-net-agentic-access
  summary_line: 28 operations · 18 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://01mind.net
  baseurl_source: declared
  description: 'Agent-consumable REST API for the 01Mind superstore: purchase-and-collect execution of catalogue listings (document rendering, email send, legal research, reference packs) under x402 payment with EIP-'
  name: 01Mind Agent Superstore API
  slug: 01mind-agent-superstore-api
- description: Remote Model Context Protocol server at https://01mind.net/mcp (Streamable HTTP, POST only, protocol version 2025-06-18, serverInfo 01Mind 3.0.0). tools/list and initialize answer anonymously with thr
  name: 01Mind MCP Server
  slug: 01mind-mcp-server
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://01mind.net/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 3.0.0) advertising ten skills — document'
  name: 01Mind A2A Agent
  slug: 01mind-a2a-agent
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/agentic-access/01mind-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/01mind-net-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://01mind.net/
- group: docs
  title: ''
  type: Documentation
  url: https://01mind.net/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://01mind.net/catalogue
- group: commercial
  title: ''
  type: TermsOfService
  url: https://01mind.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://01mind.net/privacy
- group: operate
  title: ''
  type: Support
  url: https://01mind.net/contact
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/a2a/01mind-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/01mind-net-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/mcp/01mind-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/01mind-net-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/well-known/01mind-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/01mind-net-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/llms/01mind-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/01mind-net-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/authentication/01mind-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/01mind-net-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/conventions/01mind-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/01mind-net-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/errors/01mind-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/01mind-net-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/data-model/01mind-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/01mind-net-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/rate-limits/01mind-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/01mind-net-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/plans/01mind-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/01mind-net-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/sandbox/01mind-net-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/01mind-net-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/conformance/01mind-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/01mind-net-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/lifecycle/01mind-net-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/01mind-net-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/01mind-net/refs/heads/main/security/01mind-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/01mind-net-domain-security.yml
- group: other
  title: ''
  type: AITransparency
  url: https://01mind.net/terms
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://01mind.net/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://01mind.net/privacy
created: '2026-09-19'
description: '01Mind is a Melbourne, Australia software and intelligence-system maker (a registered business name of a sole trader, ABN 36 557 232 677) that runs an agent-facing "superstore" at 01mind.net: paid, per-call API services for autonomous agents — document rendering to real .docx/.xlsx files, plaintext email sending, live legal-research answers, AI-written compliance reference packs, agent-economy venue intelligence and an on-demand safe tool-generation engine (Charon) — settled in USDC on Base through the x402 protocol with no account required. The same catalogue is exposed three ways: a 28-operation OpenAPI 3.0.3 REST contract at https://01mind.net/openapi.json, a remote MCP server at https://01mind.net/mcp that answers an anonymous tools/list, and an A2A 0.3.0 agent card at /.well-known/agent-card.json declaring ten skills purchasable through the a2a-x402 payment extension.'
layout: provider
mcp_servers:
- description: ''
  name: 01Mind MCP Server
  slug: 01mind-mcp-server
- description: ''
  name: 01Mind MCP endpoint (Streamable HTTP)
  slug: 01mind-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: 01Mind
nav: Providers
network: true
overview: '01Mind publishes 1 API on the [APIs.io](https://apis.io/) network: Agent Superstore API. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  01Mind''s developer surface includes documentation, pricing, support, authentication, sandbox, and 20 more developer resources.'
plans:
- name: 01Mind Net Plans Pricing
  plan_count: 12
  slug: 01mind-net-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: 01Mind Net Rate Limits
  slug: 01mind-net-rate-limits
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 58.0
    catalog_earned_first_party: 20.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 45.9
    developer_ergonomics: 42.3
    discoverability: 70.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: 01Mind Net Authentication
  slug: 01mind-net-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: 01Mind Net Domain Security
  slug: 01mind-net-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 01mind-net
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Document Generation
- Email
- Legal Research
- Compliance
- Tool Generation
- agent-native
- Australia
website: https://01mind.net/
---
