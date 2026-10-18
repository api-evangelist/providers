---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: REST API for Dealroom data
  name: Dealroom API
  slug: dealroom-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Composable single- and multi-metric aggregations across companies, universities, government bodies and NGOs, funding rounds, valuations, founders, investors, and entities of every type.
  name: Dealroom Aggregate API
  slug: dealroom-aggregate-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Company profiles — the `organization_subtype = company` subset of entities (excludes investors, universities, and gov/NGOs). Same response shape as the entity index, scoped to companies.
  name: Dealroom Companies API
  slug: dealroom-companies-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: API root discovery and functional namespaces.
  name: Dealroom Discovery API
  slug: dealroom-discovery-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Companies, investors, people, universities, and other organisations. Filter, sort, and paginate the unified entity index. The term `investor` refers to the investment firm; `fund` refers to the capita
  name: Dealroom Entities API
  slug: dealroom-entities-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Filter registry discovery and value lookup. Use `/reference/filters` to discover available filters per scope and `/reference/filters/:key/values` to look up valid values.
  name: Dealroom Filters API
  slug: dealroom-filters-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Founder profiles with company associations and education history. Subset of entities where `is_founder = true`.
  name: Dealroom Founders API
  slug: dealroom-founders-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: 'Funds — the capital vehicles investor firms raise (e.g. "Fund III", $200M, 2024). Browse/filter by manager, type, size, and vintage; each fund links to its manager (GP). Fund size (`amount`) converts '
  name: Dealroom Funds API
  slug: dealroom-funds-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Government bodies and NGOs — the `organization_subtype = gov_ngo` subset of entities.
  name: Dealroom Government & NGO API
  slug: dealroom-government-ngo-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Liveness probe (public, unauthenticated).
  name: Dealroom Health API
  slug: dealroom-health-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: 'Investor profiles (VCs, corporates, angels, family offices, governments). Subset of entities where `is_investor = true`. An investor is the firm that makes investments; the capital vehicles it raises '
  name: Dealroom Investors API
  slug: dealroom-investors-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Active job openings posted by companies, with hiring-trend signals.
  name: Dealroom Jobs API
  slug: dealroom-jobs-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Curated news articles about companies, funds, deals, sectors, and events.
  name: Dealroom News API
  slug: dealroom-news-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: The Notes API from Dealroom — 2 operation(s) for notes.
  name: Dealroom Notes API
  slug: dealroom-notes-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Person profiles (founders, executives, angels, and others). Subset of entities where `entity_type = 'person'`. Same response shape as founders, with company associations, education, and tags.
  name: Dealroom People API
  slug: dealroom-people-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Cross-resource fuzzy search across companies, investors, people, universities, and government & NGO bodies.
  name: Dealroom Search API
  slug: dealroom-search-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Funding rounds, equity events, debt, grants, exits, and other company-level financial events.
  name: Dealroom Transactions API
  slug: dealroom-transactions-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: University profiles — the `organization_subtype = university` subset of entities. The `university` sub-object carries alumni metrics.
  name: Dealroom Universities API
  slug: dealroom-universities-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Company valuation history, by `valued_date`.
  name: Dealroom Valuations API
  slug: dealroom-valuations-api
- baseURL: https://api.dealroom.app
  baseurl_source: declared
  description: Yearly entity metrics (employees, revenue, valuation).
  name: Dealroom Time Series API
  slug: dealroom-time-series-api
artifact_total: 33
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/rules/dealroom-rules.yml
  title: ''
  type: Spectral
  url: rules/dealroom-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/json-ld/dealroom-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dealroom-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/vocabulary/dealroom-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dealroom-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/conformance/dealroom-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealroom-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/rate-limits/dealroom-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dealroom-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/data-model/dealroom-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dealroom-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/changelog/dealroom-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dealroom-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/conventions/dealroom-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dealroom-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://dealroom.co/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/authentication/dealroom-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dealroom-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.dealroom.co/concepts/versioning.md#response-headers
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/lifecycle/dealroom-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dealroom-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/errors/dealroom-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dealroom-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/llms/dealroom-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealroom-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/a2a/dealroom-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dealroom-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/mcp/dealroom-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dealroom-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/well-known/dealroom-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealroom-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/well-known/dealroom-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealroom-docs-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/well-known/dealroom-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealroom-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/well-known/dealroom-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealroom-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/hosts/dealroom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealroom-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/vendors/dealroom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealroom-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dealroom.co/getting-started/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dealroom.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.dealroom.app/data/entities?sort=-launch_date&limit=1
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dealroom.co/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dealroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/security/dealroom-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dealroom-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dealroom/refs/heads/main/security/dealroom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealroom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealroom.co
created: '2026-10-14'
description: 'Dealroom is a company surfaced via the API Evangelist harvest backlog (source: tag-qc) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: EntityFundsResponse
  property_count: 3
  slug: dealroom-entity-funds-response
- name: EntityInvestmentsResponse
  property_count: 3
  slug: dealroom-entity-investments-response
- name: FilterSearchResponse
  property_count: 1
  slug: dealroom-filter-search-response
- name: FilterValuesResponse
  property_count: 2
  slug: dealroom-filter-values-response
- name: FiltersResponse
  property_count: 1
  slug: dealroom-filters-response
- name: SearchResponse
  property_count: 1
  slug: dealroom-search-response
jsonld:
- class_count: 120
  name: Dealroom Context
  property_count: 174
  slug: dealroom-context
layout: provider
mcp_servers:
- description: Remote MCP server at dealroomco-prod.main-kill-isr.mintlify.me.
  name: Dealroom MCP Server
  slug: dealroom-mcp-yml
modified: '2026-10-14'
name: Dealroom
nav: Providers
network: true
overview: 'Dealroom publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aggregate API, Companies API, Discovery API, and 17 more. Tagged areas include Company.


  The Dealroom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dealroom''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, and 25 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Dealroom Rate Limits
  slug: dealroom-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Dealroom API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: dealroom-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 58.8
    catalog_earned_first_party: 8.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 68.2
    developer_ergonomics: 50.0
    discoverability: 55.0
    operational_transparency: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Dealroom Authentication
  slug: dealroom-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dealroom Domain Security
  slug: dealroom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dealroom Vulnerability Disclosure
  slug: dealroom-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dealroom
tags:
- Company
website: https://dealroom.co
---
