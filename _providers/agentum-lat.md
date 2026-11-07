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
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agentum Lat Agentic Access
  operation_count: 7
  slug: agentum-lat-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 2
apis:
- description: 'Agent2Agent (A2A) protocol surface of AGENTUM Business: an agent card at https://business.agentum.lat/.well-known/agent-card.json (A2A 1.0 shape — supportedInterfaces with protocolBinding JSONRPC and '
  name: AGENTUM Business A2A Agent
  slug: business-a2a-agent
- baseURL: https://business.agentum.lat
  baseurl_source: declared
  description: The Business Intelligence API from AGENTUM — 1 operation(s) for business intelligence.
  name: AGENTUM Business Intelligence API
  slug: agentum-lat-business-intelligence-api
- baseURL: https://business.agentum.lat
  baseurl_source: declared
  description: The Company Intelligence API from AGENTUM — 2 operation(s) for company intelligence.
  name: AGENTUM Company Intelligence API
  slug: agentum-lat-company-intelligence-api
- baseURL: https://business.agentum.lat
  baseurl_source: declared
  description: The Counterparty Verification API from AGENTUM — 1 operation(s) for counterparty verification.
  name: AGENTUM Counterparty Verification API
  slug: agentum-lat-counterparty-verification-api
- baseURL: https://business.agentum.lat
  baseurl_source: declared
  description: The Finance API from AGENTUM — 1 operation(s) for finance.
  name: AGENTUM Finance API
  slug: agentum-lat-finance-api
- baseURL: https://business.agentum.lat
  baseurl_source: declared
  description: The Verification API from AGENTUM — 2 operation(s) for verification.
  name: AGENTUM Verification API
  slug: agentum-lat-verification-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/agentum-lat/capabilities/agentum-lat-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agentum-lat-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/agentum-lat/overlays/agentum-lat-apis-brasil-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentum-lat-apis-brasil-overlay.yaml
- group: other
  href: https://artifacts.apis.io/agentum-lat/overlays/agentum-lat-business-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentum-lat-business-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/agentum-lat/agentic-access/agentum-lat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentum-lat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/agentum-lat/security/agentum-lat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentum-lat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentum-lat/security/agentum-lat-domain-security.yml
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
  href: https://artifacts.apis.io/agentum-lat/llms/agentum-lat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentum-lat-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agentum.lat/llms.txt
- group: agent
  href: https://artifacts.apis.io/agentum-lat/well-known/agentum-lat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentum-lat-well-known.yml
- group: auth
  href: https://artifacts.apis.io/agentum-lat/well-known/agentum-lat-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentum-lat-security.txt
- group: other
  href: https://artifacts.apis.io/agentum-lat/a2a/agentum-lat-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentum-lat-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentum-lat/mcp/agentum-lat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentum-lat-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/orionlabsai/agentum-mcp-server
- group: build
  href: https://artifacts.apis.io/agentum-lat/mcp/agentum-lat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentum-lat-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/agentum-lat/packages/agentum-lat-packages.yml
  title: ''
  type: Packages
  url: packages/agentum-lat-packages.yml
- group: build
  href: https://artifacts.apis.io/agentum-lat/packages/agentum-lat-packages.yml
  title: ''
  type: SDKs
  url: packages/agentum-lat-packages.yml
- group: auth
  href: https://artifacts.apis.io/agentum-lat/authentication/agentum-lat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentum-lat-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentum-lat/conventions/agentum-lat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentum-lat-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentum-lat/errors/agentum-lat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentum-lat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentum-lat/lifecycle/agentum-lat-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentum-lat-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/agentum-lat/rate-limits/agentum-lat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentum-lat-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentum-lat/plans/agentum-lat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentum-lat-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentum-lat/conformance/agentum-lat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentum-lat-conformance.yml
- group: design
  href: https://artifacts.apis.io/agentum-lat/data-model/agentum-lat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentum-lat-data-model.yml
- group: agent
  href: https://artifacts.apis.io/agentum-lat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agentum-lat/security/agentum-lat-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentum-lat-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'AGENTUM (AGENTUM LTDA, a software company in Sertãozinho, São Paulo, Brazil, registered September 2026) is a "payment agent" data provider: eleven HTTP endpoints sold per call over the x402 protocol — USDC on Base mainnet (eip155:8453) — with no account, no API key and no subscription; an agent pays inside the request and receives the result in the same round trip. Nine routes on agentum.lat cover Brazilian and global company and market data (CNPJ registration status, CEP address lookup, CPF check-digit validation, Banco Central Selic/CDI/commercial-dollar rates, ECB FX rates, World Bank indicators, EU VIES VAT validation, GLEIF LEI lookup and an AI-summarised business-intelligence report on a CNPJ), and three on business.agentum.lat (AGENTUM Business) add counterparty compliance checks against TCU, CEIS/CNEP, CNJ and CVM plus a consolidated preflight verdict. The same routes ship as eleven tools in the @agentum/mcp-server npm package (stdio, the caller''s own wallet pays),
  and AGENTUM Business is also an A2A 1.0 JSON-RPC agent with a card at business.agentum.lat/.well-known/agent-card.json. Partial OpenAPI 3.1 contracts, an llms.txt and an RFC 9116 security.txt are published; every paid route answers a genuine x402 v2 challenge with Bazaar discovery metadata and IETF RateLimit headers.'
finops:
- has_sources: true
  method: derived
  name: Agentum Lat Finops
  primary_unit: call
  service_category: ''
  slug: agentum-lat-finops
  template: false
image: https://agentum.lat/agentum-logo.png
layout: provider
mcp_servers:
- description: '(Portuguese) AGENTUM''s MCP server — exposes the eleven paid HTTP routes (nine on agentum.lat, two on business.agentum.lat) as MCP tools so any MCP-capable agent host can call them and pay per call in '
  name: AGENTUM MCP Server
  slug: agentum-mcp
modified: '2026-09-19'
name: AGENTUM
nav: Providers
network: true
overview: 'AGENTUM publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Business Intelligence API, Company Intelligence API, Counterparty Verification API, and 3 more. Tagged areas include Company, Business Intelligence, KYB, Company Data, and Compliance.


  The AGENTUM catalog on APIs.io includes 1 Spectral governance ruleset.


  AGENTUM''s developer surface includes documentation, pricing, authentication, and 27 more developer resources.'
plans:
- name: Agentum Lat Plans Pricing
  plan_count: 18
  slug: agentum-lat-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Agentum Lat Rate Limits
  slug: agentum-lat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: AGENTUM API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: agentum-lat-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 50.3
    developer_ergonomics: 29.2
    discoverability: 71.7
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 40.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agentum-lat/agentum-lat-2026-10-11T093100.png
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
skill_count: 5
skills:
- name: Fetch official Brazilian rates (Selic, CDI, commercial dollar)
  slug: agentum-lat-brazil-official-rates
- name: Pull a consolidated business-intelligence report on a CNPJ
  slug: agentum-lat-cnpj-business-report
- name: Validate a Brazilian address from a CEP
  slug: agentum-lat-validate-brazilian-address
- name: Verify a Brazilian counterparty before doing business
  slug: agentum-lat-verify-brazilian-counterparty
- name: AGENTUM x402 payment and rate-limit rules (shared)
  slug: agentum-lat-x402-payment-rules
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
