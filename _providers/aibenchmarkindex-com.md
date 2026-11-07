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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 90
  human_in_the_loop: 10
  name: Aibenchmarkindex Com Agentic Access
  operation_count: 144
  slug: aibenchmarkindex-com-agentic-access
  summary_line: 144 operations · 90 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Admin API from AI Benchmark Index — 95 operation(s) for admin.
  name: AI Benchmark Index Admin API
  slug: aibenchmarkindex-com-admin-api
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Categories API from AI Benchmark Index — 1 operation(s) for categories.
  name: AI Benchmark Index Categories API
  slug: aibenchmarkindex-com-categories-api
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Listings API from AI Benchmark Index — 2 operation(s) for listings.
  name: AI Benchmark Index Listings API
  slug: aibenchmarkindex-com-listings-api
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Places API from AI Benchmark Index — 1 operation(s) for places.
  name: AI Benchmark Index Places API
  slug: aibenchmarkindex-com-places-api
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Product Categories API from AI Benchmark Index — 1 operation(s) for product categories.
  name: AI Benchmark Index Product Categories API
  slug: aibenchmarkindex-com-product-categories-api
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Products API from AI Benchmark Index — 2 operation(s) for products.
  name: AI Benchmark Index Products API
  slug: aibenchmarkindex-com-products-api
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Sources API from AI Benchmark Index — 1 operation(s) for sources.
  name: AI Benchmark Index Sources API
  slug: aibenchmarkindex-com-sources-api
- baseURL: https://aibenchmarkindex.com/api/v1
  baseurl_source: declared
  description: The Stats API from AI Benchmark Index — 1 operation(s) for stats.
  name: AI Benchmark Index Stats API
  slug: aibenchmarkindex-com-stats-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/aibenchmarkindex-com/agentic-access/aibenchmarkindex-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aibenchmarkindex-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aibenchmarkindex-com/rules/aibenchmarkindex-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aibenchmarkindex-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aibenchmarkindex-com/json-ld/aibenchmarkindex-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aibenchmarkindex-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aibenchmarkindex-com/vocabulary/aibenchmarkindex-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aibenchmarkindex-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aibenchmarkindex-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aibenchmarkindex-com/data-model/aibenchmarkindex-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aibenchmarkindex-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aibenchmarkindex-com/security/aibenchmarkindex-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aibenchmarkindex-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/aibenchmarkindex-com/errors/aibenchmarkindex-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aibenchmarkindex-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aibenchmarkindex-com/conformance/aibenchmarkindex-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aibenchmarkindex-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aibenchmarkindex-com/llms/aibenchmarkindex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aibenchmarkindex-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aibenchmarkindex-com/a2a/aibenchmarkindex-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aibenchmarkindex-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/aibenchmarkindex-com/mcp/aibenchmarkindex-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aibenchmarkindex-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aibenchmarkindex-com/mcp/aibenchmarkindex-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aibenchmarkindex-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aibenchmarkindex-com/well-known/aibenchmarkindex-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aibenchmarkindex-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aibenchmarkindex-com/well-known/aibenchmarkindex-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aibenchmarkindex-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aibenchmarkindex-com/hosts/aibenchmarkindex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aibenchmarkindex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aibenchmarkindex-com/vendors/aibenchmarkindex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aibenchmarkindex-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://aibenchmarkindex.com/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aibenchmarkindex.com/developers
- group: auth
  href: https://artifacts.apis.io/aibenchmarkindex-com/security/aibenchmarkindex-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aibenchmarkindex-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aibenchmarkindex-com/security/aibenchmarkindex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aibenchmarkindex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aibenchmarkindex.com/
- group: docs
  title: ''
  type: APIReference
  url: https://aibenchmarkindex.com/api/v1/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://aibenchmarkindex.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://aibenchmarkindex.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aibenchmarkindex.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aibenchmarkindex.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://aibenchmarkindex.com/guides/how-to-choose-an-ai-benchmark.md
created: '2026-11-01'
description: AI Benchmark Index provides an open, searchable catalog of AI benchmarks. It lists 270 benchmarks, allowing comparison of data licenses, scoring methods, and reported results. Users can explore benchmarks by region, access guides on selecting appropriate benchmarks, and view pricing and support information.
image: https://aibenchmarkindex.com/og
json_schemas:
- name: ListingItem
  property_count: 15
  slug: aibenchmarkindex-com-listing-item
- name: Listing
  property_count: 27
  slug: aibenchmarkindex-com-listing
- name: Page
  property_count: 5
  slug: aibenchmarkindex-com-page
- name: PlaceNode
  property_count: 7
  slug: aibenchmarkindex-com-place-node
- name: Product
  property_count: 19
  slug: aibenchmarkindex-com-product
- name: Stats
  property_count: 7
  slug: aibenchmarkindex-com-stats
jsonld:
- class_count: 11
  name: Aibenchmarkindex Com Context
  property_count: 65
  slug: aibenchmarkindex-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at aibenchmarkindex.com.
  name: AI Benchmark Index MCP Server
  slug: aibenchmarkindex-com-mcp-yml
modified: '2026-11-01'
name: AI Benchmark Index
nav: Providers
network: true
overview: 'AI Benchmark Index publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Categories API, Listings API, and 5 more. Tagged areas include Artificial Intelligence, Benchmarks, Data, Open, and Searchable.


  The AI Benchmark Index catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Benchmark Index''s developer surface includes documentation, API reference, pricing, support, getting-started guide, and 23 more developer resources.'
plans:
- name: Aibenchmarkindex Com Plans Pricing
  plan_count: 0
  slug: aibenchmarkindex-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Aibenchmarkindex Com Rate Limits
  slug: aibenchmarkindex-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AI Benchmark Index API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: aibenchmarkindex-com-rules
scopes:
- name: Aibenchmarkindex Com Scopes
  scope_count: 0
  slug: aibenchmarkindex-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 54.9
    developer_ergonomics: 27.9
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aibenchmarkindex Com Authentication
  slug: aibenchmarkindex-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aibenchmarkindex Com Domain Security
  slug: aibenchmarkindex-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aibenchmarkindex Com Vulnerability Disclosure
  slug: aibenchmarkindex-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: get-listing
  slug: aibenchmarkindex-com-get-listing
- name: get-stats
  slug: aibenchmarkindex-com-get-stats
- name: list-categories
  slug: aibenchmarkindex-com-list-categories
- name: list-places
  slug: aibenchmarkindex-com-list-places
- name: list-sources
  slug: aibenchmarkindex-com-list-sources
- name: search-listings
  slug: aibenchmarkindex-com-search-listings
slug: aibenchmarkindex-com
tags:
- Artificial Intelligence
- Benchmarks
- Data
- Open
- Searchable
- Index
website: https://aibenchmarkindex.com/
---
