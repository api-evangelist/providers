---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Encarapi Com Agentic Access
  operation_count: 29
  slug: encarapi-com-agentic-access
  summary_line: 29 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: Business/Scale; trials get a daily preview of 100 lookups. Removed listings with their last known data, earlier versions of inspection reports and insurance records, and 6 months of change events.
  name: encarapi-com Archive API
  slug: encarapi-com-archive-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: Search & list vehicles
  name: encarapi-com Catalog API
  slug: encarapi-com-catalog-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: Filter facets & valid values
  name: encarapi-com Discovery API
  slug: encarapi-com-discovery-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: 'Business/Scale (and trials). Used excavators from 굴삭기나라 (direct-nara.co.kr), Korea''s dedicated construction-equipment marketplace: crawler and wheeled excavators, with maker, model, year, operating ho'
  name: encarapi-com Equipment API
  slug: encarapi-com-equipment-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: Lease-takeover (리스) and rental (렌트) listings - same shape and filters as /api/catalog, kept separate because these price by monthly payment, not a purchase price.
  name: encarapi-com Leasing API
  slug: encarapi-com-leasing-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: 'Business/Scale. Trials can test the change feed (last 7 days) and bulk lookups (1,000 ids per day), but not the full export. Hold a local copy of the catalog: one bulk export for the baseline, then in'
  name: encarapi-com Sync API
  slug: encarapi-com-sync-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: Downloadable make/model/badge lists (CSV). Fetch once, cache for a day, and drive your dropdowns from these - no offline mapping, no per-click facet calls.
  name: encarapi-com Taxonomy API
  slug: encarapi-com-taxonomy-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: 'Business/Scale (and trials). Encar''s truck, bus and special-vehicle marketplace (화물·특장·버스): cargo trucks (Porter, Bongo, Mighty, Xcient ...), wing bodies, dump and construction trucks, cranes, tankers'
  name: encarapi-com Trucks API
  slug: encarapi-com-trucks-api
- baseURL: https://api.encarapi.com
  baseurl_source: declared
  description: Per-vehicle detail, history & inspection
  name: encarapi-com Vehicle API
  slug: encarapi-com-vehicle-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/encarapi-com/agentic-access/encarapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/encarapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/encarapi-com/plans/encarapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/encarapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/encarapi-com/rules/encarapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/encarapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/encarapi-com/json-ld/encarapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/encarapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/encarapi-com/vocabulary/encarapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/encarapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/encarapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/encarapi-com/data-model/encarapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/encarapi-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/encarapi-com/authentication/encarapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/encarapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/encarapi-com/errors/encarapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/encarapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/encarapi-com/conformance/encarapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/encarapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/encarapi-com/llms/encarapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/encarapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/encarapi-com/mcp/encarapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/encarapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/encarapi-com/well-known/encarapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/encarapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/encarapi-com/hosts/encarapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/encarapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/encarapi-com/vendors/encarapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/encarapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/encarapi-com/packages/encarapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/encarapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/encarapi-com/packages/encarapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/encarapi-com-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.encarapi.com</code
- group: auth
  href: https://artifacts.apis.io/encarapi-com/security/encarapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/encarapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://encarapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.encarapi.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://api.encarapi.com/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://encarapi.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://t.me/innqtech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThatMojo
created: '2026-10-30'
description: EnCarAPI provides a REST API delivering Korean used-car market data from Encar, KB Chachacha, and K Car. Over 300,000 deduplicated vehicle listings, inspection reports, accident history, dealer information, and price history are available in real-time JSON responses. Plans start at €149/month with unlimited access to listings, photos, specifications, and market statistics, plus optional add‑ons for Chinese market data.
image: https://encarapi.com/en/opengraph-image?71c9c589b900c073
json_schemas:
- name: CatalogResponse
  property_count: 4
  slug: encarapi-com-catalog-response
- name: EnumsResponse
  property_count: 7
  slug: encarapi-com-enums-response
- name: InspectionResponse
  property_count: 10
  slug: encarapi-com-inspection-response
- name: ModelSearchResponse
  property_count: 2
  slug: encarapi-com-model-search-response
- name: RecordResponse
  property_count: 20
  slug: encarapi-com-record-response
jsonld:
- class_count: 11
  name: Encarapi Com Context
  property_count: 91
  slug: encarapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.encarapi.com.
  name: encarapi-com MCP Server
  slug: encarapi-com-mcp-yml
modified: '2026-10-30'
name: encarapi-com
nav: Providers
network: true
overview: 'encarapi-com publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Archive API, Catalog API, Discovery API, and 6 more. Tagged areas include Automotive, Data, Korean, and Cars.


  The encarapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  encarapi-com''s developer surface includes authentication, documentation, API reference, pricing, support, and 20 more developer resources.'
plans:
- name: Encarapi Com Plans Pricing
  plan_count: 3
  slug: encarapi-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: encarapi-com API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: encarapi-com-rules
scopes:
- name: Encarapi Com Scopes
  scope_count: 0
  slug: encarapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 36.8
    contract_governance: 19.7
    contract_quality: 64.8
    developer_ergonomics: 41.0
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/encarapi-com/encarapi-com-2026-11-03T131518.png
security:
- kind: authentication
  name: Encarapi Com Authentication
  slug: encarapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Encarapi Com Domain Security
  slug: encarapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: encarapi-com
tags:
- Automotive
- Data
- Korean
- Cars
website: https://encarapi.com/
---
