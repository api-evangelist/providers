---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dataquoll Io Agentic Access
  operation_count: 29
  slug: dataquoll-io-agentic-access
  summary_line: 29 operations · 2 acting
api_count: 1
apis:
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: Every Australian address from G-NAF, matched exactly, with what is known about its point. One address per call, never a list.
  name: DataQuoll Addresses API
  slug: dataquoll-io-addresses-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: 'Industry calendars for NSW, VIC, QLD, WA, SA, TAS, ACT and NT: RDOs, public holidays, school holidays and shutdowns, verified against the official lists, with every source disagreement recorded.'
  name: DataQuoll Calendars API
  slug: dataquoll-io-calendars-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: Australian disaster declaration and DRFA funding-activation status by postcode and LGA. Reports declared-area status; the practitioner makes the billing/eligibility decision.
  name: DataQuoll Declarations API
  slug: dataquoll-io-declarations-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: Spatially clustered incident intelligence. Groups related incidents into events with boundary polygons, affected areas, and structured summaries.
  name: DataQuoll Events API
  slug: dataquoll-io-events-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: 'Emergency service facility locations from Geoscience Australia: where responders come from. A reference layer, not a feed.'
  name: DataQuoll Facilities API
  slug: dataquoll-io-facilities-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: River gauge observations against the Bureau of Meteorology flood classifications. Status reporting, not flood prediction, and not a substitute for official warnings.
  name: DataQuoll Gauges API
  slug: dataquoll-io-gauges-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: The Hazard history API from DataQuoll — 1 operation(s) for hazard history.
  name: DataQuoll Hazard history API
  slug: dataquoll-io-hazard-history-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: Emergency incident data
  name: DataQuoll Incidents API
  slug: dataquoll-io-incidents-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: API metadata and health
  name: DataQuoll Meta API
  slug: dataquoll-io-meta-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: Mobile network site records from the ACCC Mobile Infrastructure Report data release, a yearly snapshot. A location reference, not coverage.
  name: DataQuoll Mobile sites API
  slug: dataquoll-io-mobile-sites-api
- baseURL: https://dataquoll.io
  baseurl_source: declared
  description: 'Official documents from the publisher registry: media releases, news, alerts and notices, versioned and kept after the publisher deletes them. South Australia Police and Tasmania Police first.'
  name: DataQuoll Publications API
  slug: dataquoll-io-publications-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/dataquoll-io/agentic-access/dataquoll-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dataquoll-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dataquoll-io/plans/dataquoll-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataquoll-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dataquoll-io/rules/dataquoll-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dataquoll-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dataquoll-io/json-ld/dataquoll-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dataquoll-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dataquoll-io/vocabulary/dataquoll-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataquoll-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dataquoll-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dataquoll-io/data-model/dataquoll-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dataquoll-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/dataquoll-io/conventions/dataquoll-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dataquoll-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dataquoll-io/authentication/dataquoll-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dataquoll-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/dataquoll-io/errors/dataquoll-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dataquoll-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dataquoll-io/conformance/dataquoll-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataquoll-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataquoll-io/llms/dataquoll-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataquoll-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/dataquoll-io/well-known/dataquoll-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dataquoll-io-security.txt
- group: auth
  href: https://artifacts.apis.io/dataquoll-io/well-known/dataquoll-io-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dataquoll-io-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/dataquoll-io/well-known/dataquoll-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dataquoll-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dataquoll-io/hosts/dataquoll-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataquoll-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataquoll-io/vendors/dataquoll-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataquoll-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://dataquoll.io/security
- group: company
  title: ''
  type: Newsroom
  url: https://dataquoll.io/use-cases/media
- group: start
  title: ''
  type: Login
  url: https://dataquoll.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://dataquoll.io/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dataquoll.io\\\
- group: auth
  href: https://artifacts.apis.io/dataquoll-io/security/dataquoll-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dataquoll-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dataquoll-io/security/dataquoll-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataquoll-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dataquoll.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dataquoll.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dataquoll.io/api/v1/attribution
- group: start
  title: ''
  type: GettingStarted
  url: https://dataquoll.io/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JackDempsey9
- group: commercial
  title: ''
  type: Pricing
  url: https://dataquoll.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dataquoll.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dataquoll.io/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://dataquoll.io/openapi.json
  - status: null
    url: https://docs.dataquoll.io/openapi.json
  - status: 401
    url: https://dataquoll.io/api/mcp
  - status: 401
    url: https://docs.dataquoll.io/api/mcp
  - status: 200
    url: https://dataquoll.io/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DataQuoll is a data platform that aggregates scattered Australian public emergency and hazard data, normalises it into a consistent schema, and publishes it via a REST API. It covers incidents like fires, floods, storms, rescues, hazmat events, and disaster declarations, with historical archives back to 1840. The service provides live counts, maps, and industry calendars, enabling developers to integrate clean, machine‑readable data quickly for dashboards, automation, models, or products.
image: https://dataquoll.io/opengraph-image-12o0cb?59ddfaada03d40e0
json_schemas:
- name: EventFeature
  property_count: 4
  slug: dataquoll-io-event-feature
- name: Gauge
  property_count: 16
  slug: dataquoll-io-gauge
- name: HazardHistoryResult
  property_count: 7
  slug: dataquoll-io-hazard-history-result
- name: IncidentCollection
  property_count: 6
  slug: dataquoll-io-incident-collection
- name: IncidentFeature
  property_count: 4
  slug: dataquoll-io-incident-feature
- name: Publication
  property_count: 16
  slug: dataquoll-io-publication
jsonld:
- class_count: 26
  name: Dataquoll Io Context
  property_count: 126
  slug: dataquoll-io-context
layout: provider
modified: '2026-11-05'
name: DataQuoll
nav: Providers
network: true
overview: 'DataQuoll publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Calendars API, Declarations API, and 8 more. Tagged areas include Company, Data, Emergency, Australia, and Public Data.


  The DataQuoll catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DataQuoll''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, and 26 more developer resources.'
plans:
- name: Dataquoll Io Plans Pricing
  plan_count: 10
  slug: dataquoll-io-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: DataQuoll API Rules
  rule_count: 66
  severity_counts:
    error: 52
    hint: 0
    info: 7
    warn: 7
  slug: dataquoll-io-rules
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 61.5
    developer_ergonomics: 56.4
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dataquoll Io Authentication
  slug: dataquoll-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dataquoll Io Domain Security
  slug: dataquoll-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Dataquoll Io Vulnerability Disclosure
  slug: dataquoll-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-event
  slug: dataquoll-io-get-event
slug: dataquoll-io
tags:
- Company
- Data
- Emergency
- Australia
- Public Data
website: https://dataquoll.io/
---
