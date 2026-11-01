---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cruise Itinerary Com Agentic Access
  operation_count: 24
  slug: cruise-itinerary-com-agentic-access
  summary_line: 24 operations · 1 acting
api_count: 1
apis:
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Bulk exports API from cruise-itinerary-com — 2 operation(s) for bulk exports.
  name: cruise-itinerary-com Bulk exports API
  slug: cruise-itinerary-com-bulk-exports-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Changes API from cruise-itinerary-com — 1 operation(s) for changes.
  name: cruise-itinerary-com Changes API
  slug: cruise-itinerary-com-changes-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Cruise Itinerary Data API API from cruise-itinerary-com — 0 operation(s) for cruise itinerary data api.
  name: cruise-itinerary-com Cruise Itinerary Data API
  slug: cruise-itinerary-com-cruise-itinerary-data-api-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Price index API from cruise-itinerary-com — 2 operation(s) for price index.
  name: cruise-itinerary-com Price index API
  slug: cruise-itinerary-com-price-index-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Reference data API from cruise-itinerary-com — 8 operation(s) for reference data.
  name: cruise-itinerary-com Reference data API
  slug: cruise-itinerary-com-reference-data-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Resolver API from cruise-itinerary-com — 1 operation(s) for resolver.
  name: cruise-itinerary-com Resolver API
  slug: cruise-itinerary-com-resolver-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Sailings API from cruise-itinerary-com — 4 operation(s) for sailings.
  name: cruise-itinerary-com Sailings API
  slug: cruise-itinerary-com-sailings-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Service API from cruise-itinerary-com — 2 operation(s) for service.
  name: cruise-itinerary-com Service API
  slug: cruise-itinerary-com-service-api
- baseURL: https://cruise-itinerary.com
  baseurl_source: declared
  description: The Ships and ports API from cruise-itinerary-com — 3 operation(s) for ships and ports.
  name: cruise-itinerary-com Ships and ports API
  slug: cruise-itinerary-com-ships-and-ports-api
artifact_total: 24
asyncapis:
- description: ''
  name: Cruise Itinerary Com Webhooks
  slug: cruise-itinerary-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/cruise-itinerary-com/agentic-access/cruise-itinerary-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cruise-itinerary-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cruise-itinerary-com/plans/cruise-itinerary-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cruise-itinerary-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cruise-itinerary-com/rules/cruise-itinerary-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cruise-itinerary-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cruise-itinerary-com/json-ld/cruise-itinerary-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cruise-itinerary-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cruise-itinerary-com/vocabulary/cruise-itinerary-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cruise-itinerary-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cruise-itinerary-com/asyncapi/cruise-itinerary-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cruise-itinerary-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cruise-itinerary-com/data-model/cruise-itinerary-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cruise-itinerary-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cruise-itinerary-com/errors/cruise-itinerary-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cruise-itinerary-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cruise-itinerary-com/conformance/cruise-itinerary-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cruise-itinerary-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cruise-itinerary-com/well-known/cruise-itinerary-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cruise-itinerary-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cruise-itinerary-com/hosts/cruise-itinerary-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cruise-itinerary-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cruise-itinerary-com/vendors/cruise-itinerary-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cruise-itinerary-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://cruise-itinerary.com/account/webhooks
- group: start
  title: ''
  type: Login
  url: https://cruise-itinerary.com/login
- group: auth
  href: https://artifacts.apis.io/cruise-itinerary-com/authentication/cruise-itinerary-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cruise-itinerary-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cruise-itinerary-com/security/cruise-itinerary-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cruise-itinerary-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cruise-itinerary.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cruise-itinerary.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cruise-itinerary.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cruise-itinerary.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cruise-itinerary.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://cruise-itinerary.com/openapi.json
  - status: 401
    url: https://cruise-itinerary.com/mcp
  - status: 200
    url: https://cruise-itinerary.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Cruise Itinerary provides a public API delivering weekly updated cruise schedule, fare, and port data from 35 cruise lines. Users can query ships, itineraries, ports, and pricing via a simple JSON endpoint. The service is operated by Agile Travel Group, Inc. (doing business as Cruiseable) and offers free API keys with rate limits. Documentation, pricing, and legal terms are openly available.
image: https://cruise-itinerary.com/assets/img/og.png?v=1791038565
json_schemas:
- name: ChangeEvent
  property_count: 14
  slug: cruise-itinerary-com-change-event
- name: Cruise
  property_count: 12
  slug: cruise-itinerary-com-cruise
- name: PortDayDetail
  property_count: 10
  slug: cruise-itinerary-com-port-day-detail
- name: PriceIndexPoint
  property_count: 14
  slug: cruise-itinerary-com-price-index-point
- name: SailingDetail
  property_count: 16
  slug: cruise-itinerary-com-sailing-detail
- name: Sailing
  property_count: 15
  slug: cruise-itinerary-com-sailing
jsonld:
- class_count: 26
  name: Cruise Itinerary Com Context
  property_count: 96
  slug: cruise-itinerary-com-context
layout: provider
modified: '2026-10-30'
name: cruise-itinerary-com
nav: Providers
network: true
overview: 'cruise-itinerary-com publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk exports API, Changes API, Cruise Itinerary Data API, and 6 more. Tagged areas include Company, Travel, Data, API, and Cruise.


  The cruise-itinerary-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  cruise-itinerary-com''s developer surface includes authentication, documentation, pricing, and 18 more developer resources.'
plans:
- name: Cruise Itinerary Com Plans Pricing
  plan_count: 5
  slug: cruise-itinerary-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Cruise Itinerary Com Rate Limits
  slug: cruise-itinerary-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: cruise-itinerary-com API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: cruise-itinerary-com-rules
scopes:
- name: Cruise Itinerary Com Scopes
  scope_count: 0
  slug: cruise-itinerary-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 72.1
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 7.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cruise Itinerary Com Authentication
  slug: cruise-itinerary-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cruise Itinerary Com Domain Security
  slug: cruise-itinerary-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cruise-itinerary-com
tags:
- Company
- Travel
- Data
- API
- Cruise
website: https://cruise-itinerary.com/
---
