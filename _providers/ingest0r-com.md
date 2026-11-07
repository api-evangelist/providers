---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ingest0R Com Agentic Access
  operation_count: 4
  slug: ingest0r-com-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: A live remote MCP server at https://api.ingest0r.com/mcp (streamable-http, JSON-RPC 2.0 over HTTP POST, protocol 2025-11-25, serverInfo cook-county-chicago-property-data 1.27.2) exposing five read-onl
  name: Cook County (Chicago) Property Records MCP Server
  slug: cook-county-property-records-mcp-server
- baseURL: https://api.ingest0r.com/mcp
  baseurl_source: declared
  description: The Comps API from ingest0r — 1 operation(s) for comps.
  name: ingest0r Comps API
  slug: ingest0r-com-comps-api
- baseURL: https://api.ingest0r.com/mcp
  baseurl_source: declared
  description: The Dossier API from ingest0r — 1 operation(s) for dossier.
  name: ingest0r Dossier API
  slug: ingest0r-com-dossier-api
- baseURL: https://api.ingest0r.com/mcp
  baseurl_source: declared
  description: The Parcel API from ingest0r — 1 operation(s) for parcel.
  name: ingest0r Parcel API
  slug: ingest0r-com-parcel-api
- baseURL: https://api.ingest0r.com/mcp
  baseurl_source: declared
  description: The Search API from ingest0r — 1 operation(s) for search.
  name: ingest0r Search API
  slug: ingest0r-com-search-api
arazzos:
- description: Resolve a street address to its parcel PIN, fetch the full property dossier, then fetch comparable sales and an implied value range.
  name: Cook County address to dossier and comps
  slug: ingest0r-com-address-to-valuation-workflow
artifact_total: 18
common:
- group: auth
  href: https://artifacts.apis.io/ingest0r-com/security/ingest0r-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ingest0r-com-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://api.ingest0r.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.ingest0r.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://api.ingest0r.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.ingest0r.com/changelog.json
- group: other
  href: https://artifacts.apis.io/ingest0r-com/a2a/ingest0r-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ingest0r-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ingest0r-com/mcp/ingest0r-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ingest0r-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/ingest0r-com/mcp/ingest0r-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ingest0r-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ingest0r-com/well-known/ingest0r-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ingest0r-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/ingest0r-com/well-known/ingest0r-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ingest0r-com-security.txt
- group: agent
  href: https://artifacts.apis.io/ingest0r-com/llms/ingest0r-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ingest0r-com-llms.txt
- group: build
  href: https://artifacts.apis.io/ingest0r-com/packages/ingest0r-com-packages.yml
  title: ''
  type: Packages
  url: packages/ingest0r-com-packages.yml
- group: other
  href: https://artifacts.apis.io/ingest0r-com/overlays/ingest0r-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ingest0r-com-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/ingest0r-com/conformance/ingest0r-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ingest0r-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/ingest0r-com/errors/ingest0r-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ingest0r-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ingest0r-com/lifecycle/ingest0r-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ingest0r-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ingest0r-com/lifecycle/ingest0r-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ingest0r-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/ingest0r-com/authentication/ingest0r-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ingest0r-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ingest0r-com/security/ingest0r-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ingest0r-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ingest0r-com/security/ingest0r-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ingest0r-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ingest0r-com/security/ingest0r-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ingest0r-com-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/ingest0r-com/sandbox/ingest0r-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ingest0r-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/ingest0r-com/conventions/ingest0r-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ingest0r-com-conventions.yml
- group: operate
  href: https://artifacts.apis.io/ingest0r-com/changelog/ingest0r-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ingest0r-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/ingest0r-com/data-model/ingest0r-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ingest0r-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/ingest0r-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/ingest0r-com/agentic-access/ingest0r-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ingest0r-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ingest0r-com/plans/ingest0r-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ingest0r-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ingest0r-com/rate-limits/ingest0r-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ingest0r-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ingest0r-com/arazzo/ingest0r-com-address-to-valuation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/ingest0r-com-address-to-valuation-workflow.yml
created: '2026-09-19'
description: 'ingest0r operates the Cook County (Chicago) property records API at api.ingest0r.com — a pay-per-call, agent-native REST API over Cook County, Illinois public records (~1.9M parcels, refreshed nightly) that resolves a street address to its parcel PIN, then returns parcel details, recorded sales and deed history, building permits linked to the PIN, property-tax assessment history and comparable-sales valuation as one joined answer. There is no signup and no API key: address search and a fixed sample are always free, the first 25 PIN-route calls per client per day return real data free, and past that the routes answer HTTP 402 and are settled per call in USDC on Base or Solana through the x402 protocol ($0.01, $0.03 and $0.10). The provider publishes an OpenAPI 3.1, an A2A agent card, a live streamable-HTTP MCP server with five tools, llms.txt, an x402 resource list, a machine-readable price card and changelog, and a security.txt — all on api.ingest0r.com. The operator identifies
  itself only as "independent" (the agent card''s provider.organization) with a personal contact address; the apex ingest0r.com has no DNS A record, so the API host is the website.'
finops:
- has_sources: true
  method: derived
  name: Ingest0R Com Finops
  primary_unit: call
  service_category: ''
  slug: ingest0r-com-finops
  template: false
image: https://api.ingest0r.com/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at api.ingest0r.com over HTTP; 5 tools listed.
  name: ingest0r MCP Server
  slug: cook-county-chicago-property-data
modified: '2026-09-19'
name: ingest0r
nav: Providers
network: true
overview: 'ingest0r publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Comps API, Dossier API, Parcel API, and 2 more. Tagged areas include Company, Real Estate, Property Records, Property Data, and Public Records.


  The ingest0r catalog on APIs.io includes 1 Spectral governance ruleset.


  ingest0r''s developer surface includes documentation, pricing, changelog, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Ingest0R Com Plans Pricing
  plan_count: 4
  slug: ingest0r-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Ingest0R Com Rate Limits
  slug: ingest0r-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: ingest0r API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: ingest0r-com-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 44.7
    contract_governance: 31.8
    contract_quality: 55.1
    developer_ergonomics: 29.2
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ingest0r-com/ingest0r-com-2026-10-11T105728.png
security:
- kind: authentication
  name: Ingest0R Com Authentication
  slug: ingest0r-com-authentication
  summary_line: none/payment · 2 schemes
- kind: domain-security
  name: Ingest0R Com Domain Security
  slug: ingest0r-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ingest0R Com Vulnerability Disclosure
  slug: ingest0r-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Resolve a Chicago address to its parcel and pull the full property dossier
  slug: ingest0r-com-address-to-dossier
- name: Get comparable sales and an implied value range for a Cook County property
  slug: ingest0r-com-comps-and-valuation
- name: Evaluate the Cook County property data for free before paying
  slug: ingest0r-com-evaluate-before-paying
slug: ingest0r-com
tags:
- Company
- Real Estate
- Property Records
- Property Data
- Public Records
- Open Data
- Government Data
- Geocoding
- Property Tax
- Building Permits
- Comparable Sales
- Valuation
- x402
- Agentic Commerce
- MCP
- A2A
- Agent-Native
- Chicago
- Illinois
- Land Parcels
website: https://api.ingest0r.com/
---
