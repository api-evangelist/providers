---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Australian Bureau Of Statistics Agentic Access
  operation_count: 6
  slug: australian-bureau-of-statistics-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: Servlet-based API (TSSearchServlet) for searching the ABS time series directory by catalogue number, table title, series ID and other parameters, returning XML listings of ABS time series spreadsheets
  name: ABS Time Series Directory API
  slug: abs-time-series-directory-api
- baseURL: https://data.api.abs.gov.au/rest
  baseurl_source: declared
  description: The Get Data API from Australian Bureau of Statistics — 2 operation(s) for get data.
  name: Australian Bureau of Statistics Get Data API
  slug: australian-bureau-of-statistics-get-data-api
- baseURL: https://data.api.abs.gov.au/rest
  baseurl_source: declared
  description: The Get Metadata API from Australian Bureau of Statistics — 4 operation(s) for get metadata.
  name: Australian Bureau of Statistics Get Metadata API
  slug: australian-bureau-of-statistics-get-metadata-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/australian-bureau-of-statistics/agentic-access/australian-bureau-of-statistics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/australian-bureau-of-statistics-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/australian-bureau-of-statistics/plans/australian-bureau-of-statistics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/australian-bureau-of-statistics-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/australian-bureau-of-statistics/rules/australian-bureau-of-statistics-rules.yml
  title: ''
  type: Spectral
  url: rules/australian-bureau-of-statistics-rules.yml
- group: design
  href: https://artifacts.apis.io/australian-bureau-of-statistics/json-ld/australian-bureau-of-statistics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/australian-bureau-of-statistics-context.jsonld
- group: design
  href: https://artifacts.apis.io/australian-bureau-of-statistics/vocabulary/australian-bureau-of-statistics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/australian-bureau-of-statistics-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/australian-bureau-of-statistics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/australian-bureau-of-statistics/changelog/australian-bureau-of-statistics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/australian-bureau-of-statistics-changelog.yml
- group: design
  href: https://artifacts.apis.io/australian-bureau-of-statistics/conventions/australian-bureau-of-statistics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/australian-bureau-of-statistics-conventions.yml
- group: design
  href: https://artifacts.apis.io/australian-bureau-of-statistics/lifecycle/australian-bureau-of-statistics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/australian-bureau-of-statistics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/australian-bureau-of-statistics/errors/australian-bureau-of-statistics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/australian-bureau-of-statistics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/australian-bureau-of-statistics/conformance/australian-bureau-of-statistics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/australian-bureau-of-statistics-conformance.yml
- group: other
  href: https://artifacts.apis.io/australian-bureau-of-statistics/overlays/australian-bureau-of-statistics-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/australian-bureau-of-statistics-data-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/australian-bureau-of-statistics/well-known/australian-bureau-of-statistics-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/australian-bureau-of-statistics-www-security.txt
- group: agent
  href: https://artifacts.apis.io/australian-bureau-of-statistics/well-known/australian-bureau-of-statistics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/australian-bureau-of-statistics-well-known.yml
- group: other
  href: https://artifacts.apis.io/australian-bureau-of-statistics/hosts/australian-bureau-of-statistics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/australian-bureau-of-statistics-hosts.yml
- group: other
  href: https://artifacts.apis.io/australian-bureau-of-statistics/vendors/australian-bureau-of-statistics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/australian-bureau-of-statistics-vendors.yml
- group: auth
  href: https://artifacts.apis.io/australian-bureau-of-statistics/authentication/australian-bureau-of-statistics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/australian-bureau-of-statistics-authentication.yml
- group: auth
  href: https://artifacts.apis.io/australian-bureau-of-statistics/security/australian-bureau-of-statistics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/australian-bureau-of-statistics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/australian-bureau-of-statistics/security/australian-bureau-of-statistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/australian-bureau-of-statistics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.abs.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.abs.gov.au/statistics/application-programming-interfaces-apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.abs.gov.au/statistics/application-programming-interfaces-apis/data-api-user-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://www.abs.gov.au/statistics/application-programming-interfaces-apis/data-api-user-guide/using-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.gov.au/assets/APIs/abs/DataAPI.openapi.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.abs.gov.au/statistics/application-programming-interfaces-apis/data-api-user-guide/updates
- group: operate
  title: ''
  type: Support
  url: https://www.abs.gov.au/about/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.abs.gov.au/system/files/documents/e229d9b19dd0be5a892fc9802c24fd74/ABS%20Indicator%20API%20Key%20Request%20Form.docx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abs.gov.au/about/data-services/application-programming-interfaces-apis/indicator-api/terms-use
- group: commercial
  title: ''
  type: Legal
  url: https://www.abs.gov.au/website-privacy-copyright-and-disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abs.gov.au/about/legislation-and-policy/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.abs.gov.au/about/legislation-and-policy/security-vulnerability-disclosure
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/absstats
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AustralianBureauOfStatistics
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ABSStats
created: '2026-10-22'
description: The Australian Bureau of Statistics (ABS) is Australia's national statistical agency, publishing official statistics on the economy, population, labour, health, industry and the Census. For developers it publishes the Data API, an SDMX 2.1-compliant REST service (data.api.abs.gov.au) returning ABS economic, social and Census data as XML, JSON or CSV; the Indicator API for headline economic indicators, which requires an API key requested from the ABS; a Time Series Directory API; and the ABS Data Explorer (dataexplorer.abs.gov.au) for browsing the same datasets without code.
image: https://www.abs.gov.au/themes/custom/abs_theme/images/abs-meta-image.png
json_schemas:
- name: File
  property_count: 0
  slug: australian-bureau-of-statistics-file
jsonld:
- class_count: 3
  name: Australian Bureau Of Statistics Context
  property_count: 0
  slug: australian-bureau-of-statistics-context
layout: provider
modified: '2026-10-22'
name: Australian Bureau of Statistics
nav: Providers
network: true
overview: 'Australian Bureau of Statistics publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Get Data API, Get Metadata API, and 1 more. Tagged areas include Company, Government, Statistics, Open Data, and SDMX.


  The Australian Bureau of Statistics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Australian Bureau of Statistics'' developer surface includes changelog, authentication, documentation, getting-started guide, API reference, support, signup flow, and 27 more developer resources.'
plans:
- name: Australian Bureau Of Statistics Plans Pricing
  plan_count: 1
  slug: australian-bureau-of-statistics-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Australian Bureau Of Statistics Rate Limits
  slug: australian-bureau-of-statistics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Australian Bureau of Statistics API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: australian-bureau-of-statistics-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.2
    catalog_earned_first_party: 8.0
    catalog_gap: 53.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 35.6
    contract_quality: 52.4
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Australian Bureau Of Statistics Authentication
  slug: australian-bureau-of-statistics-authentication
  summary_line: apiKey/none · 2 schemes
- kind: domain-security
  name: Australian Bureau Of Statistics Domain Security
  slug: australian-bureau-of-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Australian Bureau Of Statistics Vulnerability Disclosure
  slug: australian-bureau-of-statistics-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: fetch-structure-version
  slug: australian-bureau-of-statistics-fetch-structure-version
- name: get-economic-indicator
  slug: australian-bureau-of-statistics-get-economic-indicator
- name: query-sdmx-data
  slug: australian-bureau-of-statistics-query-sdmx-data
slug: australian-bureau-of-statistics
tags:
- Company
- Government
- Statistics
- Open Data
- SDMX
- Census
- Economic Indicators
- Australia
website: https://www.abs.gov.au/
---
