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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agentum Lat Agentic Access
  operation_count: 7
  slug: agentum-lat-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 3
apis:
- baseURL: https://agentum.lat
  baseurl_source: declared
  description: 'The agentum.lat host: nine pay-per-call routes — GET /verificar-cnpj (CNPJ registration status, Simples Nacional, address; $0.02), GET /taxas-brasil (Selic, CDI, commercial dollar from Banco Central S'
  name: AGENTUM APIs Brasil
  slug: apis-brasil
- baseURL: https://business.agentum.lat
  baseurl_source: declared
  description: 'The business.agentum.lat host ("AGENTUM Business", a separately deployed service with its own payout wallet): GET /preflight?q= (counterparty verdict for a CNPJ, a 20-character LEI or a company name —'
  name: AGENTUM Business API
  slug: business
- description: 'Agent2Agent (A2A) protocol surface of AGENTUM Business: an agent card at https://business.agentum.lat/.well-known/agent-card.json (A2A 1.0 shape — supportedInterfaces with protocolBinding JSONRPC and '
  name: AGENTUM Business A2A Agent
  slug: business-a2a-agent
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/agentic-access/agentum-lat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentum-lat-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/security/agentum-lat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentum-lat-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/security/agentum-lat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentum-lat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentum.lat/
- group: docs
  title: ''
  type: Documentation
  url: https://agentum.lat/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentum.lat/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orionlabsai
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/llms/agentum-lat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentum-lat-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agentum.lat/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/well-known/agentum-lat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentum-lat-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/well-known/agentum-lat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentum-lat-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/a2a/agentum-lat-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentum-lat-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/mcp/agentum-lat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentum-lat-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/orionlabsai/agentum-mcp-server
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/mcp/agentum-lat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentum-lat-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/packages/agentum-lat-packages.yml
  title: ''
  type: Packages
  url: packages/agentum-lat-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/packages/agentum-lat-packages.yml
  title: ''
  type: SDKs
  url: packages/agentum-lat-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/authentication/agentum-lat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentum-lat-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/conventions/agentum-lat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentum-lat-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/errors/agentum-lat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentum-lat-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/lifecycle/agentum-lat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentum-lat-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/rate-limits/agentum-lat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentum-lat-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/plans/agentum-lat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentum-lat-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/conformance/agentum-lat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentum-lat-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/data-model/agentum-lat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentum-lat-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentum-lat/refs/heads/main/security/agentum-lat-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentum-lat-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'AGENTUM (AGENTUM LTDA, a software company in Sertãozinho, São Paulo, Brazil, registered September 2026) is a "payment agent" data provider: eleven HTTP endpoints sold per call over the x402 protocol — USDC on Base mainnet (eip155:8453) — with no account, no API key and no subscription; an agent pays inside the request and receives the result in the same round trip. Nine routes on agentum.lat cover Brazilian and global company and market data (CNPJ registration status, CEP address lookup, CPF check-digit validation, Banco Central Selic/CDI/commercial-dollar rates, ECB FX rates, World Bank indicators, EU VIES VAT validation, GLEIF LEI lookup and an AI-summarised business-intelligence report on a CNPJ), and three on business.agentum.lat (AGENTUM Business) add counterparty compliance checks against TCU, CEIS/CNEP, CNJ and CVM plus a consolidated preflight verdict. The same routes ship as eleven tools in the @agentum/mcp-server npm package (stdio, the caller''s own wallet pays),
  and AGENTUM Business is also an A2A 1.0 JSON-RPC agent with a card at business.agentum.lat/.well-known/agent-card.json. Partial OpenAPI 3.1 contracts, an llms.txt and an RFC 9116 security.txt are published; every paid route answers a genuine x402 v2 challenge with Bazaar discovery metadata and IETF RateLimit headers.'
image: https://agentum.lat/agentum-logo.png
layout: provider
mcp_servers:
- description: '(Portuguese) AGENTUM''s MCP server — exposes the eleven paid HTTP routes (nine on agentum.lat, two on business.agentum.lat) as MCP tools so any MCP-capable agent host can call them and pay per call in '
  name: AGENTUM MCP Server
  slug: agentum-mcp-server
- description: ''
  name: MCP server source (GitHub)
  slug: mcp-server-source-github
modified: '2026-09-19'
name: AGENTUM
nav: Providers
network: true
overview: 'AGENTUM publishes 2 APIs on the [APIs.io](https://apis.io/) network: APIs Brasil and Business API. Tagged areas include Company, Business Intelligence, KYB, Company Data, and Compliance.


  AGENTUM''s developer surface includes documentation, pricing, authentication, and 24 more developer resources.'
plans:
- name: Agentum Lat Plans Pricing
  plan_count: 1
  slug: agentum-lat-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Agentum Lat Rate Limits
  slug: agentum-lat-rate-limits
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.0
    catalog_earned_first_party: 16.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 37.5
    discoverability: 81.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
  name: Agentum Lat Authentication
  slug: agentum-lat-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentum Lat Domain Security
  slug: agentum-lat-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Agentum Lat Vulnerability Disclosure
  slug: agentum-lat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentum-lat
tags:
- Company
- Business Intelligence
- KYB
- Company Data
- Compliance
- Brazil
- x402
- Agentic Commerce
- Exchange Rates
- Address Verification
- Economic Data
- MCP
- A2A
- Agents
website: https://agentum.lat/
---
