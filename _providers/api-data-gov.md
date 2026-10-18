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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Api Data Gov Agentic Access
  operation_count: 25
  slug: api-data-gov-agentic-access
  summary_line: 25 operations · 1 acting
api_count: 2
apis:
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Dataset API from api.data.gov — 1 operation(s) for dataset.
  name: api.data.gov Dataset API
  slug: api-data-gov-dataset-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Harvest Jobs API from api.data.gov — 4 operation(s) for harvest jobs.
  name: api.data.gov Harvest Jobs API
  slug: api-data-gov-harvest-jobs-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Harvest Records API from api.data.gov — 7 operation(s) for harvest records.
  name: api.data.gov Harvest Records API
  slug: api-data-gov-harvest-records-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Harvest Sources API from api.data.gov — 1 operation(s) for harvest sources.
  name: api.data.gov Harvest Sources API
  slug: api-data-gov-harvest-sources-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Keywords API from api.data.gov — 1 operation(s) for keywords.
  name: api.data.gov Keywords API
  slug: api-data-gov-keywords-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Location API from api.data.gov — 1 operation(s) for location.
  name: api.data.gov Location API
  slug: api-data-gov-location-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Locations API from api.data.gov — 1 operation(s) for locations.
  name: api.data.gov Locations API
  slug: api-data-gov-locations-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Organizations API from api.data.gov — 4 operation(s) for organizations.
  name: api.data.gov Organizations API
  slug: api-data-gov-organizations-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Publishers API from api.data.gov — 1 operation(s) for publishers.
  name: api.data.gov Publishers API
  slug: api-data-gov-publishers-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Search API from api.data.gov — 1 operation(s) for search.
  name: api.data.gov Search API
  slug: api-data-gov-search-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Stats API from api.data.gov — 1 operation(s) for stats.
  name: api.data.gov Stats API
  slug: api-data-gov-stats-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Validate API from api.data.gov — 1 operation(s) for validate.
  name: api.data.gov Validate API
  slug: api-data-gov-validate-api
- baseURL: https://catalog.data.gov
  baseurl_source: declared
  description: The Open Search API from api.data.gov — 1 operation(s) for open search.
  name: api.data.gov Open Search API
  slug: api-data-gov-open-search-api
artifact_total: 30
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/agentic-access/api-data-gov-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/api-data-gov-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/rules/api-data-gov-rules.yml
  title: ''
  type: Spectral
  url: rules/api-data-gov-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/json-ld/api-data-gov-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/api-data-gov-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/vocabulary/api-data-gov-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/api-data-gov-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/data-model/api-data-gov-data-model.yml
  title: ''
  type: DataModel
  url: data-model/api-data-gov-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/errors/api-data-gov-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/api-data-gov-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/conformance/api-data-gov-conformance.yml
  title: ''
  type: Conformance
  url: conformance/api-data-gov-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/hosts/api-data-gov-hosts.yml
  title: ''
  type: Hosts
  url: hosts/api-data-gov-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/vendors/api-data-gov-vendors.yml
  title: ''
  type: Vendors
  url: vendors/api-data-gov-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://api.data.gov/signup/
- group: start
  title: ''
  type: DeveloperPortal
  url: http://api.agency.gov
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/api-data-gov/refs/heads/main/security/api-data-gov-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/api-data-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.data.gov
- group: docs
  title: ''
  type: Documentation
  url: https://api.data.gov/docs/developer-manual/
- group: docs
  title: ''
  type: APIReference
  url: https://api.data.gov/docs/developer-manual/
- group: operate
  title: ''
  type: Support
  url: https://api.data.gov/contact/
- group: operate
  title: ''
  type: RateLimits
  url: https://api.data.gov/docs/rate-limits/
- group: design
  title: ''
  type: Errors
  url: https://api.data.gov/docs/api-key/
created: '2026-10-13'
description: api.data.gov provides a free API management service for United States federal agencies, enabling them to share government data publicly in compliance with the Open Government Data Act. Hosted by GSA’s Technology Transformation Services, it aggregates over 450 APIs across 25 agencies, offering documentation, metrics, and support for developers and agency administrators. The platform aims to simplify data release, improve transparency, and foster innovation through accessible, well‑documented government datasets.
json_schemas:
- name: ErrorInfo
  property_count: 7
  slug: api-data-gov-error-info
- name: JobInfo
  property_count: 15
  slug: api-data-gov-job-info
- name: KeywordsResults
  property_count: 4
  slug: api-data-gov-keywords-results
- name: LocationsResults
  property_count: 3
  slug: api-data-gov-locations-results
- name: OrgInfo
  property_count: 10
  slug: api-data-gov-org-info
- name: OrganizationsResults
  property_count: 2
  slug: api-data-gov-organizations-results
- name: PublishersResults
  property_count: 2
  slug: api-data-gov-publishers-results
- name: RecordInfo
  property_count: 13
  slug: api-data-gov-record-info
- name: SearchResults
  property_count: 3
  slug: api-data-gov-search-results
- name: SourceInfo
  property_count: 11
  slug: api-data-gov-source-info
- name: StatsResult
  property_count: 3
  slug: api-data-gov-stats-result
- name: ValidatorInfo
  property_count: 4
  slug: api-data-gov-validator-info
jsonld:
- class_count: 28
  name: Api Data Gov Context
  property_count: 85
  slug: api-data-gov-context
layout: provider
modified: '2026-10-13'
name: api.data.gov
nav: Providers
network: true
overview: 'api.data.gov publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dataset API, Harvest Jobs API, Harvest Records API, and 10 more. Tagged areas include Company, Government, Data, and Open Data.


  The api.data.gov catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  api.data.gov''s developer surface includes signup flow, documentation, API reference, support, and 14 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 0
  name: Api Data Gov Rate Limits
  slug: api-data-gov-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: api.data.gov API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: api-data-gov-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 56.8
    developer_ergonomics: 31.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Api Data Gov Domain Security
  slug: api-data-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: api-data-gov
tags:
- Company
- Government
- Data
- Open Data
website: https://api.data.gov
---
