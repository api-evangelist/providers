---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 30.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ablakunio Com Agentic Access
  operation_count: 5
  slug: ablakunio-com-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://www.ablakunio.com
  baseurl_source: declared
  description: Raktárkészlet
  name: Ablakunio – SM-UNIO Nyílászáró Kft. Inventory API
  slug: ablakunio-com-inventory-api
- baseURL: https://www.ablakunio.com
  baseurl_source: declared
  description: Ajánlatkérés / visszahívás
  name: Ablakunio – SM-UNIO Nyílászáró Kft. Lead API
  slug: ablakunio-com-lead-api
- baseURL: https://www.ablakunio.com
  baseurl_source: declared
  description: Model Context Protocol végpont AI-ágenseknek
  name: Ablakunio – SM-UNIO Nyílászáró Kft. MCP API
  slug: ablakunio-com-mcp-api
- baseURL: https://www.ablakunio.com
  baseurl_source: declared
  description: Egyedi méretű árbecslés
  name: Ablakunio – SM-UNIO Nyílászáró Kft. Pricing API
  slug: ablakunio-com-pricing-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/ablakunio-com/agentic-access/ablakunio-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ablakunio-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ablakunio-com/rules/ablakunio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ablakunio-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ablakunio-com/json-ld/ablakunio-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ablakunio-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ablakunio-com/vocabulary/ablakunio-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ablakunio-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ablakunio-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ablakunio-com/data-model/ablakunio-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ablakunio-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ablakunio-com/errors/ablakunio-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ablakunio-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ablakunio-com/conformance/ablakunio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ablakunio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ablakunio-com/llms/ablakunio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ablakunio-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ablakunio-com/a2a/ablakunio-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ablakunio-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/ablakunio-com/mcp/ablakunio-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ablakunio-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ablakunio-com/mcp/ablakunio-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ablakunio-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ablakunio-com/well-known/ablakunio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ablakunio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ablakunio-com/hosts/ablakunio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ablakunio-com-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ablakunio.com/blog
- group: auth
  href: https://artifacts.apis.io/ablakunio-com/security/ablakunio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ablakunio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ablakunio.com/
created: '2026-10-31'
description: Ablakunio – SM-UNIO Nyílászáró Kft. provides premium plastic windows, custom doors, and shading technology in Tiszafüred, Hungary. They offer a showroom, on‑site surveys, professional installation, and a genuine warranty. Their free price‑API delivers cost estimates for window sizes via a JSON‑RPC MCP endpoint, and an OpenAPI 3.1 REST description is publicly available without registration.
image: https://www.ablakunio.com/images/hero-bg.png
json_schemas:
- name: InventoryResponse
  property_count: 0
  slug: ablakunio-com-inventory-response
- name: LeadRequest
  property_count: 0
  slug: ablakunio-com-lead-request
- name: LeadResponse
  property_count: 0
  slug: ablakunio-com-lead-response
- name: PriceEstimateRequest
  property_count: 12
  slug: ablakunio-com-price-estimate-request
- name: PriceEstimateResponse
  property_count: 0
  slug: ablakunio-com-price-estimate-response
- name: StockCheckRequest
  property_count: 0
  slug: ablakunio-com-stock-check-request
- name: StockMatchesResponse
  property_count: 1
  slug: ablakunio-com-stock-matches-response
jsonld:
- class_count: 2
  name: Ablakunio Com Context
  property_count: 12
  slug: ablakunio-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.ablakunio.com.
  name: Ablakunio – SM-UNIO Nyílászáró Kft. MCP Server
  slug: ablakunio-com-mcp-yml
modified: '2026-10-31'
name: Ablakunio – SM-UNIO Nyílászáró Kft.
nav: Providers
network: true
overview: 'Ablakunio – SM-UNIO Nyílászáró Kft. publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Inventory API, Lead API, MCP API, and 1 more. Tagged areas include Windows, Doors, Construction, Hungary, and Pricing.


  The Ablakunio – SM-UNIO Nyílászáró Kft. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ablakunio – SM-UNIO Nyílászáró Kft.''s developer surface includes engineering blog and 16 more developer resources.'
plans:
- name: Ablakunio Com Plans Pricing
  plan_count: 0
  slug: ablakunio-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Ablakunio Com Rate Limits
  slug: ablakunio-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Ablakunio – SM-UNIO Nyílászáró Kft. API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: ablakunio-com-rules
scopes:
- name: Ablakunio Com Scopes
  scope_count: 0
  slug: ablakunio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 60.2
    developer_ergonomics: 3.0
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - hungary
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 25.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ablakunio Com Authentication
  slug: ablakunio-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ablakunio Com Domain Security
  slug: ablakunio-com-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: ablakunio-com-inventory-check
  slug: ablakunio-com-inventory-check
- name: price-estimate
  slug: ablakunio-com-price-estimate
slug: ablakunio-com
tags:
- Windows
- Doors
- Construction
- Hungary
- Pricing
website: https://www.ablakunio.com/
---
