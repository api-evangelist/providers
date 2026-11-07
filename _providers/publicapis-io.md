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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP server providing tools to search and compare APIs.
  name: PublicAPIs.io MCP
  slug: publicapis-io-mcp
- baseURL: https://api.fynk.com/v1
  baseurl_source: declared
  description: 'publicapis-io API as documented publicly: 52 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: publicapis-io API
  slug: publicapis-io-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/publicapis-io/rules/publicapis-io-rules.yml
  title: ''
  type: Spectral
  url: rules/publicapis-io-rules.yml
- group: design
  href: https://artifacts.apis.io/publicapis-io/json-ld/publicapis-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/publicapis-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/publicapis-io/vocabulary/publicapis-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/publicapis-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/publicapis-io/data-model/publicapis-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/publicapis-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/publicapis-io/conformance/publicapis-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/publicapis-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/publicapis-io/llms/publicapis-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/publicapis-io-llms.txt
- group: build
  href: https://artifacts.apis.io/publicapis-io/mcp/publicapis-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/publicapis-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/publicapis-io/mcp/publicapis-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/publicapis-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/publicapis-io/hosts/publicapis-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/publicapis-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/publicapis-io/vendors/publicapis-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/publicapis-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://publicapis.io/category/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://publicapis.io/privacy.com-api
- group: company
  title: ''
  type: Newsroom
  url: https://publicapis.io/category/news
- group: docs
  title: ''
  type: Documentation
  url: https://dev.publicapis.io/
- group: auth
  href: https://artifacts.apis.io/publicapis-io/security/publicapis-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/publicapis-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://publicapis.io/
- group: company
  title: ''
  type: Blog
  url: https://publicapis.io/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://publicapis.io/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://publicapis.io/serpapi-web-search-api
created: '2026-10-31'
description: PublicAPIs.io is a curated directory of over 1,000 free public APIs, offering developers searchable listings, detailed descriptions, and direct links to API documentation and endpoints. The platform aggregates APIs across categories such as data, finance, AI, and more, providing a community-driven resource for discovering and accessing open APIs without registration barriers.
image: https://c1.tablecdn.com/pa/publicapis.png
json_schemas:
- name: GetApiAllTheXResponse
  property_count: 2
  slug: publicapis-io-get-api-all-the-xresponse
- name: GetApiCatalogListResponse
  property_count: 2
  slug: publicapis-io-get-api-catalog-list-response
- name: GetApiSpacecraftsResponse
  property_count: 1
  slug: publicapis-io-get-api-spacecrafts-response
- name: GetSeriesIdResponse
  property_count: 1
  slug: publicapis-io-get-series-id-response
- name: PostApiUrlSubmitRequest
  property_count: 4
  slug: publicapis-io-post-api-url-submit-request
- name: PostV1ContractsRequest
  property_count: 2
  slug: publicapis-io-post-v1-contracts-request
jsonld:
- class_count: 37
  name: Publicapis Io Context
  property_count: 17
  slug: publicapis-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at publicapis.io.
  name: publicapis-io MCP Server
  slug: publicapis-io-mcp-yml
modified: '2026-10-31'
name: publicapis-io
nav: Providers
network: true
overview: 'publicapis-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Directory, Public APIs, Developer Resources, and Open Data.


  The publicapis-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  publicapis-io''s developer surface includes documentation, engineering blog, API reference, and 16 more developer resources.'
plans:
- name: Publicapis Io Plans Pricing
  plan_count: 0
  slug: publicapis-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Publicapis Io Rate Limits
  slug: publicapis-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: publicapis-io API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: publicapis-io-rules
scopes:
- name: Publicapis Io Scopes
  scope_count: 0
  slug: publicapis-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 14.3
    discoverability: 65.8
    operational_transparency: 5.3
  previous_composite: 26.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/publicapis-io/publicapis-io-2026-11-03T141712.png
security:
- kind: authentication
  name: Publicapis Io Authentication
  slug: publicapis-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Publicapis Io Domain Security
  slug: publicapis-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: publicapis-io
tags:
- Company
- API Directory
- Public APIs
- Developer Resources
- Open Data
website: https://publicapis.io/
---
