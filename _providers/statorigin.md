---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Statorigin Agentic Access
  operation_count: 17
  slug: statorigin-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- baseURL: https://statorigin.org/api/v1
  baseurl_source: declared
  description: Indicator definitions and time series
  name: StatOrigin Indicators API
  slug: statorigin-indicators-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: declared
  description: ISIC Rev.4 classification
  name: StatOrigin Industries API
  slug: statorigin-industries-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: declared
  description: Countries and supranational groupings
  name: StatOrigin Regions API
  slug: statorigin-regions-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: declared
  description: Full-text search
  name: StatOrigin Search API
  slug: statorigin-search-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: declared
  description: Publishing organisations and their documents
  name: StatOrigin Sources API
  slug: statorigin-sources-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: declared
  description: Data points with full provenance
  name: StatOrigin Statistics API
  slug: statorigin-statistics-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/statorigin/agentic-access/statorigin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/statorigin-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/statorigin/rules/statorigin-rules.yml
  title: ''
  type: Spectral
  url: rules/statorigin-rules.yml
- group: design
  href: https://artifacts.apis.io/statorigin/json-ld/statorigin-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/statorigin-context.jsonld
- group: design
  href: https://artifacts.apis.io/statorigin/vocabulary/statorigin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/statorigin-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/statorigin/data-model/statorigin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/statorigin-data-model.yml
- group: design
  href: https://artifacts.apis.io/statorigin/errors/statorigin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/statorigin-problem-types.yml
- group: design
  href: https://artifacts.apis.io/statorigin/conformance/statorigin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/statorigin-conformance.yml
- group: agent
  href: https://artifacts.apis.io/statorigin/llms/statorigin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/statorigin-llms.txt
- group: agent
  href: https://artifacts.apis.io/statorigin/well-known/statorigin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statorigin-well-known.yml
- group: other
  href: https://artifacts.apis.io/statorigin/hosts/statorigin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/statorigin-hosts.yml
- group: other
  href: https://artifacts.apis.io/statorigin/vendors/statorigin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/statorigin-vendors.yml
- group: auth
  href: https://artifacts.apis.io/statorigin/security/statorigin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statorigin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://statorigin.org
- group: docs
  title: ''
  type: Documentation
  url: https://statorigin.org/docs/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://statorigin.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://statorigin.org/privacy
- group: operate
  title: ''
  type: Support
  url: https://statorigin.org/about
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://statorigin.org/mcp
  - status: 200
    url: https://statorigin.org
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: StatOrigin provides free, sourced industry statistics via a REST API. It aggregates data from 157 primary publishers across 32 industries, offering over 232,938 verified statistics with full provenance and citation. The platform enables searching, comparing, and downloading data without authentication, supporting open data initiatives.
image: https://statorigin.org/og-default.png
json_schemas:
- name: Meta
  property_count: 6
  slug: statorigin-meta
- name: Statistic
  property_count: 23
  slug: statorigin-statistic
jsonld:
- class_count: 3
  name: Statorigin Context
  property_count: 30
  slug: statorigin-context
layout: provider
modified: '2026-10-14'
name: StatOrigin
nav: Providers
network: true
overview: 'StatOrigin publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Indicators API, Industries API, Regions API, and 3 more. Tagged areas include Company, Data, Statistics, OpenAPI, and Free.


  The StatOrigin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  StatOrigin''s developer surface includes documentation, support, and 15 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: StatOrigin API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: statorigin-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 58.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Statorigin Domain Security
  slug: statorigin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: statorigin
tags:
- Company
- Data
- Statistics
- OpenAPI
- Free
website: https://statorigin.org
---
