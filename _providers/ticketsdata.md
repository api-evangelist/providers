---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
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
  score: 22.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Unified API providing real-time event and ticketing data across major marketplaces. Documentation is at https://ticketsdata.com/docs.
  name: TicketsData API
  slug: ticketsdata-api-2
- baseURL: https://your-space.ticketsdata.com
  baseurl_source: declared
  description: 'TicketsData API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: TicketsData API
  slug: ticketsdata-api
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/ticketsdata/rate-limits/ticketsdata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ticketsdata-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ticketsdata/plans/ticketsdata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ticketsdata-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ticketsdata/rules/ticketsdata-rules.yml
  title: ''
  type: Spectral
  url: rules/ticketsdata-rules.yml
- group: design
  href: https://artifacts.apis.io/ticketsdata/json-ld/ticketsdata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ticketsdata-context.jsonld
- group: design
  href: https://artifacts.apis.io/ticketsdata/vocabulary/ticketsdata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ticketsdata-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ticketsdata/data-model/ticketsdata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ticketsdata-data-model.yml
- group: design
  href: https://artifacts.apis.io/ticketsdata/conventions/ticketsdata-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ticketsdata-conventions.yml
- group: design
  href: https://artifacts.apis.io/ticketsdata/conventions/ticketsdata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ticketsdata-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ticketsdata/authentication/ticketsdata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ticketsdata-authentication.yml
- group: design
  href: https://artifacts.apis.io/ticketsdata/conformance/ticketsdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ticketsdata-conformance.yml
- group: other
  href: https://artifacts.apis.io/ticketsdata/hosts/ticketsdata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ticketsdata-hosts.yml
- group: build
  href: https://artifacts.apis.io/ticketsdata/packages/ticketsdata-packages.yml
  title: ''
  type: SDKs
  url: packages/ticketsdata-packages.yml
- group: build
  href: https://artifacts.apis.io/ticketsdata/packages/ticketsdata-packages.yml
  title: ''
  type: Packages
  url: packages/ticketsdata-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ticketsdata.com/status
- group: start
  title: ''
  type: GettingStarted
  url: https://ticketsdata.com/blog/playoff-ticket-pricing-api-step-by-step-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ticketsdata
- group: auth
  href: https://artifacts.apis.io/ticketsdata/security/ticketsdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ticketsdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ticketsdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ticketsdata.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ticketsdata.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://ticketsdata.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ticketsdata.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ticketsdata.com/legal/privacy
coverage:
  checked: '2026-10-19'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://ticketsdata.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: TicketsData provides real-time event and ticketing data through a unified API that aggregates primary and resale marketplace listings. The platform offers clean JSON responses with seat maps, pricing, availability, and market intelligence across ten major ticket marketplaces. Users can access live event data, arbitrage insights, and pricing trends via a single endpoint, supporting high request volumes and enterprise-grade reliability. The service includes documentation, pricing details, and a free trial for developers to integrate ticket data into their applications.
image: https://ticketsdata.com/og-preview.png
json_schemas:
- name: GetEventsResponse
  property_count: 4
  slug: ticketsdata-get-events-response
- name: GetMatchResponse
  property_count: 10
  slug: ticketsdata-get-match-response
jsonld:
- class_count: 2
  name: Ticketsdata Context
  property_count: 11
  slug: ticketsdata-context
layout: provider
modified: '2026-10-19'
name: TicketsData
nav: Providers
network: true
overview: 'TicketsData is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Real-Time Data, and Market Intelligence.


  The TicketsData catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TicketsData''s developer surface includes authentication, getting-started guide, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Ticketsdata Plans Pricing
  plan_count: 4
  slug: ticketsdata-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Ticketsdata Rate Limits
  slug: ticketsdata-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: TicketsData API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ticketsdata-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 20.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 23.3
    developer_ergonomics: 42.9
    discoverability: 48.2
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
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
  name: Ticketsdata Authentication
  slug: ticketsdata-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ticketsdata Domain Security
  slug: ticketsdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ticketsdata
tags:
- Company
- Ticketing
- Real-Time Data
- Market Intelligence
website: https://ticketsdata.com/
---
