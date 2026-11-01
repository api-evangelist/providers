---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Gribstream Com Agentic Access
  operation_count: 13
  slug: gribstream-com-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- baseURL: https://gribstream.com
  baseurl_source: declared
  description: Token-scoped quota and access status.
  name: gribstream-com Account API
  slug: gribstream-com-account-api
- baseURL: https://gribstream.com
  baseurl_source: declared
  description: Free public dataset, parameter and selector discovery endpoints.
  name: gribstream-com Catalog API
  slug: gribstream-com-catalog-api
- baseURL: https://gribstream.com
  baseurl_source: declared
  description: Authenticated, metered native coordinate inventories.
  name: gribstream-com Grid coordinates API
  slug: gribstream-com-grid-coordinates-api
- baseURL: https://gribstream.com
  baseurl_source: declared
  description: Historical and forecast-run extraction endpoints.
  name: gribstream-com Weather data API
  slug: gribstream-com-weather-data-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/gribstream-com/agentic-access/gribstream-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gribstream-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/gribstream-com/rules/gribstream-com-rules.yml
  title: ''
  type: Spectral
  url: rules/gribstream-com-rules.yml
- group: design
  href: https://artifacts.apis.io/gribstream-com/json-ld/gribstream-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gribstream-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/gribstream-com/vocabulary/gribstream-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gribstream-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gribstream-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gribstream-com/data-model/gribstream-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gribstream-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/gribstream-com/errors/gribstream-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gribstream-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gribstream-com/conformance/gribstream-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gribstream-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gribstream-com/well-known/gribstream-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gribstream-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gribstream-com/hosts/gribstream-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gribstream-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/gribstream-com/packages/gribstream-com-packages.yml
  title: ''
  type: SDKs
  url: packages/gribstream-com-packages.yml
- group: build
  href: https://artifacts.apis.io/gribstream-com/packages/gribstream-com-packages.yml
  title: ''
  type: Packages
  url: packages/gribstream-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://gribstream.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GribStream
- group: auth
  href: https://artifacts.apis.io/gribstream-com/authentication/gribstream-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gribstream-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gribstream-com/security/gribstream-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gribstream-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gribstream.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gribstream.com/docs
- group: company
  title: ''
  type: Blog
  url: https://gribstream.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://gribstream.com/quickstart
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gribstream.com/tos.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gribstream.com/privacy_policy.html
created: '2026-10-30'
description: GribStream provides a live forecasts and historical weather API, offering access to global and regional forecast models, satellite and radar data, and atmospheric composition. Developers can query by coordinates, time ranges, and variables, integrating weather data into applications, AI tools, and databases. The service includes a Python client, MySQL-compatible endpoint, and extensive documentation for quick integration.
image: https://gribstream.com/favicon.ico
json_schemas:
- name: CatalogDataset
  property_count: 34
  slug: gribstream-com-catalog-dataset
- name: CatalogParameter
  property_count: 11
  slug: gribstream-com-catalog-parameter
- name: CatalogSharedParameter
  property_count: 17
  slug: gribstream-com-catalog-shared-parameter
- name: QuotaSnapshot
  property_count: 14
  slug: gribstream-com-quota-snapshot
- name: RunsPostRequest
  property_count: 14
  slug: gribstream-com-runs-post-request
- name: TimeseriesPostRequest
  property_count: 15
  slug: gribstream-com-timeseries-post-request
jsonld:
- class_count: 31
  name: Gribstream Com Context
  property_count: 151
  slug: gribstream-com-context
layout: provider
modified: '2026-10-30'
name: gribstream-com
nav: Providers
network: true
overview: 'gribstream-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Catalog API, Grid coordinates API, and 1 more. Tagged areas include Company, Weather, API, Forecast, and Data.


  The gribstream-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  gribstream-com''s developer surface includes authentication, documentation, engineering blog, getting-started guide, and 18 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: gribstream-com API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: gribstream-com-rules
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 70.9
    contract_quality: 61.3
    developer_ergonomics: 49.3
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gribstream Com Authentication
  slug: gribstream-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gribstream Com Domain Security
  slug: gribstream-com-domain-security
  summary_line: DMARC
skill_count: 1
skills:
- name: gribstream-com-get-latest-forecasts
  slug: gribstream-com-get-latest-forecasts
slug: gribstream-com
tags:
- Company
- Weather
- API
- Forecast
- Data
website: https://gribstream.com/
---
