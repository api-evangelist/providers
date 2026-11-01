---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides access to weather forecasts, historical data, and climate analysis.
  name: Weather API
  slug: weather-api
- baseURL: https://my.meteoblue.com
  baseurl_source: declared
  description: 'Meteoblue API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Meteoblue API
  slug: meteoblue-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/meteoblue/rules/meteoblue-rules.yml
  title: ''
  type: Spectral
  url: rules/meteoblue-rules.yml
- group: design
  href: https://artifacts.apis.io/meteoblue/json-ld/meteoblue-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meteoblue-context.jsonld
- group: design
  href: https://artifacts.apis.io/meteoblue/vocabulary/meteoblue-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meteoblue-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/meteoblue/data-model/meteoblue-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meteoblue-data-model.yml
- group: design
  href: https://artifacts.apis.io/meteoblue/conformance/meteoblue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meteoblue-conformance.yml
- group: other
  href: https://artifacts.apis.io/meteoblue/hosts/meteoblue-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meteoblue-hosts.yml
- group: other
  href: https://artifacts.apis.io/meteoblue/vendors/meteoblue-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meteoblue-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://content.meteoblue.com/en/business-solutions/weather-apis/pricing
- group: start
  title: ''
  type: Login
  url: https://www.meteoblue.com/en/user/login/index
- group: company
  title: ''
  type: Blog
  url: https://www.meteoblue.com/en/blog/article/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meteoblue
- group: auth
  href: https://artifacts.apis.io/meteoblue/security/meteoblue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meteoblue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.meteoblue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.meteoblue.com/en/weather-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.meteoblue.com/en/weather-api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://content.meteoblue.com/en/about-us/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.meteoblue.com/en/user/contact/feedback
- group: operate
  title: ''
  type: Community
  url: https://community.meteoblue.com
coverage:
  checked: '2026-10-28'
  detail: Documentation is public but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://docs.meteoblue.com/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Meteoblue provides weather and climate data services, offering a range of APIs for forecasts, historical weather, climate analysis, and specialized data such as air quality, pollen, and aviation weather. Their platform delivers global coverage with customizable endpoints for developers, businesses, and researchers seeking accurate meteorological information.
image: https://static.meteoblue.com/assets/images/logo/meteoblue_tile_large.png
json_schemas:
- name: GetEnServerSearchQuery3Response
  property_count: 12
  slug: meteoblue-get-en-server-search-query3-response
- name: GetV1TimeModeDomainResponse
  property_count: 11
  slug: meteoblue-get-v1-time-mode-domain-response
- name: PostDatasetQueryRequest
  property_count: 5
  slug: meteoblue-post-dataset-query-request
jsonld:
- class_count: 3
  name: Meteoblue Context
  property_count: 26
  slug: meteoblue-context
layout: provider
modified: '2026-10-28'
name: Meteoblue
nav: Providers
network: true
overview: 'Meteoblue is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Climate, Data, API, and Forecast.


  The Meteoblue catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Meteoblue''s developer surface includes pricing, engineering blog, documentation, API reference, support, and 13 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Meteoblue API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: meteoblue-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 21.6
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Meteoblue Domain Security
  slug: meteoblue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meteoblue
tags:
- Weather
- Climate
- Data
- API
- Forecast
website: https://www.meteoblue.com/
---
