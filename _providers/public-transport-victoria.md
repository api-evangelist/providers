---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Public Transport Victoria Agentic Access
  operation_count: 26
  slug: public-transport-victoria-agentic-access
  summary_line: 26 operations
api_count: 1
apis:
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Departures API from Public Transport Victoria — 2 operation(s) for departures.
  name: Public Transport Victoria Departures API
  slug: public-transport-victoria-departures-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Directions API from Public Transport Victoria — 3 operation(s) for directions.
  name: Public Transport Victoria Directions API
  slug: public-transport-victoria-directions-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Disruptions API from Public Transport Victoria — 6 operation(s) for disruptions.
  name: Public Transport Victoria Disruptions API
  slug: public-transport-victoria-disruptions-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The FareEstimate API from Public Transport Victoria — 1 operation(s) for fareestimate.
  name: Public Transport Victoria Fare Estimate API
  slug: public-transport-victoria-fareestimate-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Outlets API from Public Transport Victoria — 2 operation(s) for outlets.
  name: Public Transport Victoria Outlets API
  slug: public-transport-victoria-outlets-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Patterns API from Public Transport Victoria — 1 operation(s) for patterns.
  name: Public Transport Victoria Patterns API
  slug: public-transport-victoria-patterns-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Routes API from Public Transport Victoria — 2 operation(s) for routes.
  name: Public Transport Victoria Routes API
  slug: public-transport-victoria-routes-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The RouteTypes API from Public Transport Victoria — 1 operation(s) for routetypes.
  name: Public Transport Victoria Route Types API
  slug: public-transport-victoria-routetypes-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Runs API from Public Transport Victoria — 4 operation(s) for runs.
  name: Public Transport Victoria Runs API
  slug: public-transport-victoria-runs-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Search API from Public Transport Victoria — 1 operation(s) for search.
  name: Public Transport Victoria Search API
  slug: public-transport-victoria-search-api
- baseURL: https://timetableapi.ptv.vic.gov.au
  baseurl_source: declared
  description: The Stops API from Public Transport Victoria — 3 operation(s) for stops.
  name: Public Transport Victoria Stops API
  slug: public-transport-victoria-stops-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/public-transport-victoria/agentic-access/public-transport-victoria-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/public-transport-victoria-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/public-transport-victoria/rules/public-transport-victoria-rules.yml
  title: ''
  type: Spectral
  url: rules/public-transport-victoria-rules.yml
- group: design
  href: https://artifacts.apis.io/public-transport-victoria/vocabulary/public-transport-victoria-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/public-transport-victoria-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/public-transport-victoria/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/public-transport-victoria/data-model/public-transport-victoria-data-model.yml
  title: ''
  type: DataModel
  url: data-model/public-transport-victoria-data-model.yml
- group: design
  href: https://artifacts.apis.io/public-transport-victoria/conventions/public-transport-victoria-conventions.yml
  title: ''
  type: Conventions
  url: conventions/public-transport-victoria-conventions.yml
- group: auth
  href: https://artifacts.apis.io/public-transport-victoria/authentication/public-transport-victoria-authentication.yml
  title: ''
  type: Authentication
  url: authentication/public-transport-victoria-authentication.yml
- group: operate
  href: https://artifacts.apis.io/public-transport-victoria/lifecycle/public-transport-victoria-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/public-transport-victoria-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/public-transport-victoria/lifecycle/public-transport-victoria-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/public-transport-victoria-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/public-transport-victoria/errors/public-transport-victoria-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/public-transport-victoria-problem-types.yml
- group: design
  href: https://artifacts.apis.io/public-transport-victoria/conformance/public-transport-victoria-conformance.yml
  title: ''
  type: Conformance
  url: conformance/public-transport-victoria-conformance.yml
- group: other
  href: https://artifacts.apis.io/public-transport-victoria/overlays/public-transport-victoria-timetable-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/public-transport-victoria-timetable-overlay.yaml
- group: other
  href: https://artifacts.apis.io/public-transport-victoria/hosts/public-transport-victoria-hosts.yml
  title: ''
  type: Hosts
  url: hosts/public-transport-victoria-hosts.yml
- group: other
  href: https://artifacts.apis.io/public-transport-victoria/vendors/public-transport-victoria-vendors.yml
  title: ''
  type: Vendors
  url: vendors/public-transport-victoria-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.developer.vic.gov.au/terms
- group: operate
  title: ''
  type: Support
  url: https://www.developer.vic.gov.au/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.developer.vic.gov.au/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://transport.vic.gov.au/news-and-resources/news
- group: start
  title: ''
  type: Login
  url: https://www.developer.vic.gov.au/sign-in
- group: auth
  href: https://artifacts.apis.io/public-transport-victoria/security/public-transport-victoria-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/public-transport-victoria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ptv.vic.gov.au/
- group: docs
  title: ''
  type: APIReference
  url: https://timetableapi.ptv.vic.gov.au/swagger/ui/index
- group: docs
  title: ''
  type: Documentation
  url: https://discover.data.vic.gov.au/dataset/ptv-timetable-api
created: '2026-10-22'
description: Public Transport Victoria (PTV) is the Victorian Government public transport authority in Australia, covering metropolitan and regional train, tram and bus services. It publishes the PTV Timetable API (Version 3, documented in Swagger), which provides scheduled timetable, route and stop data for all Victorian train, tram and bus services including Night Network, real-time data for metropolitan services where available, disruption information, stop facility information and myki ticket outlet data. Access requires a developer ID and key; the dataset is listed on DataVic under the Department of Transport. ptv.vic.gov.au now redirects to transport.vic.gov.au.
layout: provider
modified: '2026-10-22'
name: Public Transport Victoria
nav: Providers
network: true
overview: 'Public Transport Victoria publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Departures API, Directions API, Disruptions API, and 8 more. Tagged areas include Company, Public Transport, Government, Transit, and Timetables.


  The Public Transport Victoria catalog on APIs.io includes 1 Spectral governance ruleset.


  Public Transport Victoria''s developer surface includes authentication, support, API reference, documentation, and 19 more developer resources.'
plans:
- name: Public Transport Victoria Plans Pricing
  plan_count: 0
  slug: public-transport-victoria-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Public Transport Victoria Rate Limits
  slug: public-transport-victoria-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Public Transport Victoria API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: public-transport-victoria-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 41.9
    developer_ergonomics: 35.1
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Public Transport Victoria Authentication
  slug: public-transport-victoria-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Public Transport Victoria Domain Security
  slug: public-transport-victoria-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 4
skills:
- name: public-transport-victoria-check-disruptions
  slug: public-transport-victoria-check-disruptions
- name: public-transport-victoria-find-next-departures
  slug: public-transport-victoria-find-next-departures
- name: public-transport-victoria-plan-ticketing
  slug: public-transport-victoria-plan-ticketing
- name: public-transport-victoria-trace-a-service-run
  slug: public-transport-victoria-trace-a-service-run
slug: public-transport-victoria
tags:
- Company
- Public Transport
- Government
- Transit
- Timetables
- Australia
- Open Data
website: https://ptv.vic.gov.au/
---
