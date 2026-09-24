---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 87
  human_in_the_loop: 1
  name: Macaroonnetwork Com Agentic Access
  operation_count: 120
  slug: macaroonnetwork-com-agentic-access
  summary_line: 120 operations · 87 acting · 1 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.macaroonnetwork.com
  baseurl_source: declared
  description: 'The REST surface behind the marketplace: anonymous discovery (GET /listings, /listings/search?intent=, /api/public/services, /api/public/taxonomy, /api/public/mcp-servers, /api/public/sources, /api/ro'
  name: Macaroon Network Agent Services API
  slug: agent-services-api
- description: The network router MCP server — a live Streamable HTTP endpoint at https://api.macaroonnetwork.com/mcp (serverInfo macaroon-network 0.3.0, protocol 2025-06-18) answering initialize and tools/list anon
  name: Macaroon Network MCP Server
  slug: mcp-server
- description: A free, read-only Streamable HTTP MCP server at https://api.macaroonnetwork.com/mcp-faith-evidence-v1/mcp/ (serverInfo macaroon-bible-evidence 0.3.0) exposing eleven bounded tools over pinned Berean S
  name: Macaroon Bible Evidence MCP Server
  slug: bible-evidence-mcp
- description: An Agent2Agent 0.3.0 endpoint at https://api.macaroonnetwork.com/a2a (JSON-RPC; message/send, tasks/get and tasks/cancel implemented) described by a conformant agent card served from both /.well-known
  name: Macaroon Network A2A Agent
  slug: a2a-agent
artifact_total: 14
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/security/macaroonnetwork-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/macaroonnetwork-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/security/macaroonnetwork-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/macaroonnetwork-com-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/agentic-access/macaroonnetwork-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/macaroonnetwork-com-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://macaroonnetwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://macaroonnetwork.com/listings
- group: docs
  title: ''
  type: APIReference
  url: https://api.macaroonnetwork.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://macaroonnetwork.com/
- group: auth
  title: ''
  type: Authentication
  url: https://macaroonnetwork.com/auth.md
- group: commercial
  title: ''
  type: Pricing
  url: https://macaroonnetwork.com/services
- group: commercial
  title: ''
  type: TermsOfService
  url: https://macaroonnetwork.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://macaroonnetwork.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@macaroonnetwork.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kevmoz/macaroonnetwork-mcp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/a2a/macaroonnetwork-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/macaroonnetwork-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/mcp/macaroonnetwork-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/macaroonnetwork-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/well-known/macaroonnetwork-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/macaroonnetwork-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/well-known/macaroonnetwork-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/macaroonnetwork-com-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/well-known/macaroonnetwork-com-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/macaroonnetwork-com-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/llms/macaroonnetwork-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/macaroonnetwork-com-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/llms/macaroonnetwork-com-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/macaroonnetwork-com-api-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/authentication/macaroonnetwork-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/macaroonnetwork-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/conventions/macaroonnetwork-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/macaroonnetwork-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/errors/macaroonnetwork-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/macaroonnetwork-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/data-model/macaroonnetwork-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/macaroonnetwork-com-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/rate-limits/macaroonnetwork-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/macaroonnetwork-com-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/plans/macaroonnetwork-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/macaroonnetwork-com-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/conformance/macaroonnetwork-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/macaroonnetwork-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/lifecycle/macaroonnetwork-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/macaroonnetwork-com-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/macaroonnetwork-com/refs/heads/main/packages/macaroonnetwork-com-packages.yml
  title: ''
  type: Packages
  url: packages/macaroonnetwork-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://macaroonnetwork.com/.well-known/security.txt
- group: other
  title: ''
  type: AITransparency
  url: https://macaroonnetwork.com/terms
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://macaroonnetwork.com/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://macaroonnetwork.com/privacy
created: '2026-09-19'
description: 'Macaroon Network is a UK-operated marketplace where autonomous AI agents discover, pay for and execute live-data and scientific-computing capabilities. Seventy-nine sale-ready listings — UK company and haulage checks, sanctions/PEP screening, VAT/IBAN/LEI validation, domain trust, government, health, weather and CVE lookups, source-labelled Bible evidence, and Polymathica/VortX scientific solvers — are sold pay-per-call in USDC on Base over x402 v2 (HTTP 402 + PAYMENT-REQUIRED, retried with PAYMENT-SIGNATURE), with settlement gated on a falsifiable acceptance predicate evaluated against the real response. The surface is agent-native by construction: an OpenAPI 3.1 contract at api.macaroonnetwork.com/openapi.json, a conformant A2A 0.3.0 agent card, two live Streamable HTTP MCP servers (the network router and a free read-only Bible Evidence server, both in the official MCP registry), an RFC 9727 api-catalog, RFC 9728 protected-resource metadata, an RFC 9116 security.txt, llms.txt,
  an x402 discovery document and a JSON agent-capabilities catalogue. Human products (Faith Evidence Pro, Logistics Compliance Pro, ebooks) are sold by PayPal subscription.'
image: https://macaroonnetwork.com/og-cover.png
layout: provider
mcp_servers:
- description: ''
  name: Macaroon Network MCP Server
  slug: macaroon-network-mcp-server
- description: ''
  name: Remote endpoint (Streamable HTTP)
  slug: remote-endpoint-streamable-http
- description: ''
  name: Macaroon Network MCP Server
  slug: macaroon-network-mcp-server-2
- description: ''
  name: Remote endpoint (Streamable HTTP)
  slug: remote-endpoint-streamable-http-2
modified: '2026-09-19'
name: Macaroon Network
nav: Providers
network: true
overview: 'Macaroon Network publishes 1 API on the [APIs.io](https://apis.io/) network: Agent Services API. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  Macaroon Network''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, support, GitHub presence, and 27 more developer resources.'
plans:
- name: Macaroonnetwork Com Plans Pricing
  plan_count: 4
  slug: macaroonnetwork-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Macaroonnetwork Com Rate Limits
  slug: macaroonnetwork-com-rate-limits
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 41.3
    developer_ergonomics: 47.0
    discoverability: 81.5
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Macaroonnetwork Com Authentication
  slug: macaroonnetwork-com-authentication
  summary_line: none/x402-payment · 3 schemes
- kind: domain-security
  name: Macaroonnetwork Com Domain Security
  slug: macaroonnetwork-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Macaroonnetwork Com Vulnerability Disclosure
  slug: macaroonnetwork-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: macaroonnetwork-com
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Data Marketplace
- Compliance
- Sanctions Screening
- Company Data
- Scientific Computing
- Bible
- United Kingdom
- Agent-Native
website: https://macaroonnetwork.com/
---
