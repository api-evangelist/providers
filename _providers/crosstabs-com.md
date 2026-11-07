---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Crosstabs Com Agentic Access
  operation_count: 14
  slug: crosstabs-com-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://www.crosstabs.com
  baseurl_source: declared
  description: The Aggregate statistics API from Crosstabs — 4 operation(s) for aggregate statistics.
  name: Crosstabs Aggregate statistics API
  slug: crosstabs-com-aggregate-statistics-api
- baseURL: https://www.crosstabs.com
  baseurl_source: declared
  description: The Chi Square API from Crosstabs — 1 operation(s) for chi square.
  name: Crosstabs Chi Square API
  slug: crosstabs-com-chi-square-api
- baseURL: https://www.crosstabs.com
  baseurl_source: declared
  description: The Contingency API from Crosstabs — 1 operation(s) for contingency.
  name: Crosstabs Contingency API
  slug: crosstabs-com-contingency-api
- baseURL: https://www.crosstabs.com
  baseurl_source: declared
  description: The Fishers Exact API from Crosstabs — 1 operation(s) for fishers exact.
  name: Crosstabs Fishers Exact API
  slug: crosstabs-com-fishers-exact-api
- baseURL: https://www.crosstabs.com
  baseurl_source: declared
  description: The Odds Ratio API from Crosstabs — 1 operation(s) for odds ratio.
  name: Crosstabs Odds Ratio API
  slug: crosstabs-com-odds-ratio-api
- baseURL: https://www.crosstabs.com
  baseurl_source: declared
  description: The Operations API from Crosstabs — 1 operation(s) for operations.
  name: Crosstabs Operations API
  slug: crosstabs-com-operations-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/crosstabs-com/agentic-access/crosstabs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crosstabs-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crosstabs-com/rules/crosstabs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crosstabs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crosstabs-com/json-ld/crosstabs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crosstabs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crosstabs-com/vocabulary/crosstabs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crosstabs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crosstabs-com/data-model/crosstabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crosstabs-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/crosstabs-com/changelog/crosstabs-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crosstabs-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/crosstabs-com/errors/crosstabs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crosstabs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crosstabs-com/conformance/crosstabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crosstabs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crosstabs-com/llms/crosstabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crosstabs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/crosstabs-com/hosts/crosstabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crosstabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crosstabs-com/vendors/crosstabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crosstabs-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.crosstabs.com/status
- group: auth
  title: ''
  type: Security
  url: https://www.crosstabs.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.crosstabs.com/changelog
- group: auth
  href: https://artifacts.apis.io/crosstabs-com/security/crosstabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crosstabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crosstabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crosstabs.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.crosstabs.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.crosstabs.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.crosstabs.com/
- group: operate
  title: ''
  type: Support
  url: https://www.crosstabs.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crosstabs.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crosstabs.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crosstabs.com/terms
created: '2026-11-04'
description: Crosstabs provides a free, browser‑based alternative to SPSS, offering a suite of statistical tools, calculators, and an open Statistics API. Users can upload SPSS, Stata, SAS, R, Excel and other data formats, run over 115 statistical procedures, and export results to PowerPoint, Word, or Excel. The platform requires no installation, account, or API key, and supports multiple languages and open CORS for direct API calls.
image: https://www.crosstabs.com/opengraph-image
json_schemas:
- name: ChiSquareResponse
  property_count: 8
  slug: crosstabs-com-chi-square-response
- name: ContingencyResponse
  property_count: 17
  slug: crosstabs-com-contingency-response
- name: FisherResponse
  property_count: 5
  slug: crosstabs-com-fisher-response
- name: HealthReport
  property_count: 7
  slug: crosstabs-com-health-report
- name: OddsRatioResponse
  property_count: 6
  slug: crosstabs-com-odds-ratio-response
- name: TableRequest
  property_count: 1
  slug: crosstabs-com-table-request
jsonld:
- class_count: 8
  name: Crosstabs Com Context
  property_count: 36
  slug: crosstabs-com-context
layout: provider
modified: '2026-11-04'
name: Crosstabs
nav: Providers
network: true
overview: 'Crosstabs publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aggregate statistics API, Chi Square API, Contingency API, and 3 more. Tagged areas include Statistics, Data Analysis, Free Tools, OpenAPI, and Browser-Based.


  The Crosstabs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crosstabs'' developer surface includes changelog, documentation, API reference, getting-started guide, support, pricing, and 18 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Crosstabs API Rules
  rule_count: 53
  severity_counts:
    error: 45
    hint: 0
    info: 6
    warn: 2
  slug: crosstabs-com-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 55.7
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crosstabs Com Domain Security
  slug: crosstabs-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: crosstabs-com
tags:
- Statistics
- Data Analysis
- Free Tools
- OpenAPI
- Browser-Based
website: https://crosstabs.com/
---
