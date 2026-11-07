---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Carhunt Fr Agentic Access
  operation_count: 12
  slug: carhunt-fr-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api-pro.carhunt.fr
  baseurl_source: declared
  description: The Analyses API from CarHunt — 2 operation(s) for analyses.
  name: CarHunt Analyses API
  slug: carhunt-fr-analyses-api
- baseURL: https://api-pro.carhunt.fr
  baseurl_source: declared
  description: The Compte API from CarHunt — 1 operation(s) for compte.
  name: CarHunt Compte API
  slug: carhunt-fr-compte-api
- baseURL: https://api-pro.carhunt.fr
  baseurl_source: declared
  description: The Marché API from CarHunt — 1 operation(s) for marché.
  name: CarHunt Marché API
  slug: carhunt-fr-march-api
- baseURL: https://api-pro.carhunt.fr
  baseurl_source: declared
  description: The Recherche API from CarHunt — 3 operation(s) for recherche.
  name: CarHunt Recherche API
  slug: carhunt-fr-recherche-api
- baseURL: https://api-pro.carhunt.fr
  baseurl_source: declared
  description: The Synchronisation API from CarHunt — 1 operation(s) for synchronisation.
  name: CarHunt Synchronisation API
  slug: carhunt-fr-synchronisation-api
- baseURL: https://api-pro.carhunt.fr
  baseurl_source: declared
  description: The Watchlists API from CarHunt — 2 operation(s) for watchlists.
  name: CarHunt Watchlists API
  slug: carhunt-fr-watchlists-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/carhunt-fr/agentic-access/carhunt-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carhunt-fr-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/carhunt-fr/plans/carhunt-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carhunt-fr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/carhunt-fr/rules/carhunt-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/carhunt-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/carhunt-fr/json-ld/carhunt-fr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carhunt-fr-context.jsonld
- group: design
  href: https://artifacts.apis.io/carhunt-fr/vocabulary/carhunt-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carhunt-fr-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/carhunt-fr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/carhunt-fr/data-model/carhunt-fr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carhunt-fr-data-model.yml
- group: design
  href: https://artifacts.apis.io/carhunt-fr/errors/carhunt-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carhunt-fr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carhunt-fr/conformance/carhunt-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carhunt-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carhunt-fr/llms/carhunt-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carhunt-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/carhunt-fr/mcp/carhunt-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carhunt-fr-mcp.yml
- group: agent
  href: https://artifacts.apis.io/carhunt-fr/well-known/carhunt-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carhunt-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/carhunt-fr/hosts/carhunt-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carhunt-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/carhunt-fr/vendors/carhunt-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carhunt-fr-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://carhunt.fr/pricing
- group: start
  title: ''
  type: Login
  url: https://carhunt.fr/login
- group: company
  title: ''
  type: Blog
  url: https://blog.carhunt.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.carhunt.fr/
- group: docs
  title: ''
  type: APIReference
  url: https://api-pro.carhunt.fr/docs
- group: auth
  href: https://artifacts.apis.io/carhunt-fr/security/carhunt-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carhunt-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carhunt.fr/
created: '2026-11-03'
description: 'carhunt-fr is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://carhunt.fr/og-image-radar.jpg
json_schemas:
- name: EstimateIn
  property_count: 9
  slug: carhunt-fr-estimate-in
- name: EstimateOut
  property_count: 20
  slug: carhunt-fr-estimate-out
- name: ListingAnalysisOut
  property_count: 7
  slug: carhunt-fr-listing-analysis-out
- name: UsageOut
  property_count: 7
  slug: carhunt-fr-usage-out
- name: WatchlistIn
  property_count: 16
  slug: carhunt-fr-watchlist-in
- name: WatchlistPatch
  property_count: 17
  slug: carhunt-fr-watchlist-patch
jsonld:
- class_count: 18
  name: Carhunt Fr Context
  property_count: 85
  slug: carhunt-fr-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.carhunt.fr.
  name: CarHunt MCP Server
  slug: carhunt-fr-mcp-yml
modified: '2026-11-03'
name: CarHunt
nav: Providers
network: true
overview: 'CarHunt publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analyses API, Compte API, Marché API, and 3 more. Tagged areas include Company.


  The CarHunt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CarHunt''s developer surface includes pricing, engineering blog, documentation, API reference, and 17 more developer resources.'
plans:
- name: Carhunt Fr Plans Pricing
  plan_count: 6
  slug: carhunt-fr-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: CarHunt API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: carhunt-fr-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 60.3
    developer_ergonomics: 11.3
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carhunt Fr Domain Security
  slug: carhunt-fr-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: carhunt-fr-watchlist-management
  slug: carhunt-fr-watchlist-management
slug: carhunt-fr
tags:
- Company
website: https://carhunt.fr/
---
