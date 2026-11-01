---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Flight Mcp Com Agentic Access
  operation_count: 6
  slug: flight-mcp-com-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://flight-mcp.com
  baseurl_source: declared
  description: The Flights API from flight-mcp-com — 2 operation(s) for flights.
  name: flight-mcp-com Flights API
  slug: flight-mcp-com-flights-api
- baseURL: https://flight-mcp.com
  baseurl_source: declared
  description: The Healthz API from flight-mcp-com — 1 operation(s) for healthz.
  name: flight-mcp-com Healthz API
  slug: flight-mcp-com-healthz-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/flight-mcp-com/agentic-access/flight-mcp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flight-mcp-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/flight-mcp-com/plans/flight-mcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flight-mcp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flight-mcp-com/rules/flight-mcp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/flight-mcp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/flight-mcp-com/json-ld/flight-mcp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flight-mcp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/flight-mcp-com/vocabulary/flight-mcp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flight-mcp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/flight-mcp-com/data-model/flight-mcp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flight-mcp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/flight-mcp-com/errors/flight-mcp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flight-mcp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flight-mcp-com/conformance/flight-mcp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flight-mcp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flight-mcp-com/llms/flight-mcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flight-mcp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/flight-mcp-com/hosts/flight-mcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flight-mcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/flight-mcp-com/vendors/flight-mcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flight-mcp-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://flight-mcp.com/playground
- group: start
  title: ''
  type: Login
  url: https://flight-mcp.com/sign-in
- group: auth
  href: https://artifacts.apis.io/flight-mcp-com/authentication/flight-mcp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flight-mcp-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/flight-mcp-com/security/flight-mcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flight-mcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flight-mcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://flight-mcp.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://flight-mcp.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flight-mcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flight-mcp.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://flight-mcp.com/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://flight-mcp.com/openapi.json
  - status: 401
    url: https://flight-mcp.com/mcp
  - status: 200
    url: https://flight-mcp.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Flight MCP provides a unified flight search API and MCP (Machine Call Protocol) contract, offering normalized flight offers across multiple providers. It supports both REST and MCP interfaces, includes caching mechanisms, tiered pricing plans, and a developer playground. The service is designed for integration into travel applications and AI agents, delivering reliable flight data with flexible usage options.
json_schemas:
- name: AnonymousFlightSearchInput
  property_count: 0
  slug: flight-mcp-com-anonymous-flight-search-input
- name: AnonymousFlightSearchResponse
  property_count: 6
  slug: flight-mcp-com-anonymous-flight-search-response
- name: FlightSearchInput
  property_count: 13
  slug: flight-mcp-com-flight-search-input
- name: FlightSearchResponse
  property_count: 5
  slug: flight-mcp-com-flight-search-response
jsonld:
- class_count: 8
  name: Flight Mcp Com Context
  property_count: 38
  slug: flight-mcp-com-context
layout: provider
modified: '2026-10-30'
name: flight-mcp-com
nav: Providers
network: true
overview: 'flight-mcp-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Flights API and Healthz API. Tagged areas include Travel, API, Flight, MCP, and Search.


  The flight-mcp-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  flight-mcp-com''s developer surface includes sandbox, authentication, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Flight Mcp Com Plans Pricing
  plan_count: 3
  slug: flight-mcp-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: flight-mcp-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: flight-mcp-com-rules
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 86.5
    catalog_earned_first_party: 0.0
    catalog_gap: 28.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 54.6
    developer_ergonomics: 33.3
    discoverability: 62.5
    operational_transparency: 0.0
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
  name: Flight Mcp Com Authentication
  slug: flight-mcp-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Flight Mcp Com Domain Security
  slug: flight-mcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flight-mcp-com
tags:
- Travel
- API
- Flight
- MCP
- Search
website: https://flight-mcp.com/
---
