---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Transitland Agentic Access
  operation_count: 37
  slug: transitland-agentic-access
  summary_line: 37 operations · 9 acting
api_count: 2
apis:
- description: Flexible GraphQL query API over the Transitland datastore; available on Enterprise plans (introspection returns 401 without a key).
  name: Transitland GraphQL API
  slug: transitland-graphql-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: The Agencies API from TransitLand — 2 operation(s) for agencies.
  name: TransitLand Agencies API
  slug: transitland-agencies-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: The Feed Versions API from TransitLand — 4 operation(s) for feed versions.
  name: TransitLand Feed Versions API
  slug: transitland-feed-versions-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: The Feeds API from TransitLand — 4 operation(s) for feeds.
  name: TransitLand Feeds API
  slug: transitland-feeds-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: The Onestop Id API from TransitLand — 1 operation(s) for onestop id.
  name: TransitLand Onestop Id API
  slug: transitland-onestop-id-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: The Operators API from TransitLand — 2 operation(s) for operators.
  name: TransitLand Operators API
  slug: transitland-operators-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: The Routes API from TransitLand — 4 operation(s) for routes.
  name: TransitLand Routes API
  slug: transitland-routes-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: The Stops API from TransitLand — 3 operation(s) for stops.
  name: TransitLand Stops API
  slug: transitland-stops-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: Auto, pedestrian, and bicycle routing from Valhalla over OpenStreetMap.
  name: TransitLand Street routing API
  slug: transitland-street-routing-api
- baseURL: https://transit.land/api/v2/rest
  baseurl_source: declared
  description: Transit and walking itineraries from the Transitland Routing API.
  name: TransitLand Transit routing API
  slug: transitland-transit-routing-api
artifact_total: 23
common:
- group: design
  href: https://artifacts.apis.io/transitland/conventions/transitland-conventions.yml
  title: ''
  type: Conventions
  url: conventions/transitland-conventions.yml
- group: design
  href: https://artifacts.apis.io/transitland/lifecycle/transitland-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/transitland-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/transitland/agentic-access/transitland-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transitland-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/transitland/rate-limits/transitland-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/transitland-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/transitland/plans/transitland-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/transitland-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/transitland/rules/transitland-rules.yml
  title: ''
  type: Spectral
  url: rules/transitland-rules.yml
- group: design
  href: https://artifacts.apis.io/transitland/json-ld/transitland-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/transitland-context.jsonld
- group: design
  href: https://artifacts.apis.io/transitland/vocabulary/transitland-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/transitland-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/transitland/data-model/transitland-data-model.yml
  title: ''
  type: DataModel
  url: data-model/transitland-data-model.yml
- group: design
  href: https://artifacts.apis.io/transitland/errors/transitland-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/transitland-problem-types.yml
- group: design
  href: https://artifacts.apis.io/transitland/conformance/transitland-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transitland-conformance.yml
- group: agent
  href: https://artifacts.apis.io/transitland/llms/transitland-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/transitland-llms.txt
- group: agent
  href: https://artifacts.apis.io/transitland/well-known/transitland-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/transitland-well-known.yml
- group: other
  href: https://artifacts.apis.io/transitland/hosts/transitland-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transitland-hosts.yml
- group: other
  href: https://artifacts.apis.io/transitland/vendors/transitland-vendors.yml
  title: ''
  type: Vendors
  url: vendors/transitland-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.transit.land/
- group: company
  title: ''
  type: Newsroom
  url: https://www.transit.land/news/2015/11/05/citylab
- group: docs
  title: ''
  type: APIReference
  url: https://www.transit.land/llms.txt
- group: auth
  href: https://artifacts.apis.io/transitland/authentication/transitland-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transitland-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.transit.land
- group: auth
  href: https://artifacts.apis.io/transitland/security/transitland-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transitland-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.transit.land/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transitland
- group: commercial
  title: ''
  type: Pricing
  url: https://www.transit.land/plans-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.transit.land/terms
- group: start
  title: ''
  type: SignUp
  url: https://app.interline.io
created: '2026-05-28'
description: Transitland is an open, community-edited aggregation of public transit data from GTFS and GTFS Realtime feeds around the world, operated by Interline Technologies. It offers a REST API and a GraphQL API over agencies, routes, stops, trips, feeds and feed versions, real-time departures, plus the Interline Routing Platform for transit and street routing, isochrones and matrices.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transitland.png
json_schemas:
- name: ValhallaIsochroneRequest
  property_count: 17
  slug: transitland-valhalla-isochrone-request
- name: ValhallaMatrixRequest
  property_count: 16
  slug: transitland-valhalla-matrix-request
- name: ValhallaMatrixResponse
  property_count: 5
  slug: transitland-valhalla-matrix-response
- name: ValhallaRouteRequest
  property_count: 23
  slug: transitland-valhalla-route-request
- name: ValhallaTraceAttributesResponse
  property_count: 14
  slug: transitland-valhalla-trace-attributes-response
- name: ValhallaTraceRouteRequest
  property_count: 22
  slug: transitland-valhalla-trace-route-request
jsonld:
- class_count: 75
  name: Transitland Context
  property_count: 365
  slug: transitland-context
layout: provider
modified: '2026-10-19'
name: TransitLand
nav: Providers
network: true
overview: 'TransitLand publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agencies API, Feed Versions API, Feeds API, and 7 more. Tagged areas include Transportation, Public APIs, Transit, GTFS, and Open Data.


  The TransitLand catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TransitLand''s developer surface includes API reference, authentication, documentation, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Transitland Plans Pricing
  plan_count: 4
  slug: transitland-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Transitland Rate Limits
  slug: transitland-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: TransitLand API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: transitland-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 65.7
    developer_ergonomics: 20.2
    discoverability: 81.3
    operational_transparency: 31.6
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/transitland/transitland-2026-06-20T195546.png
security:
- kind: authentication
  name: Transitland Authentication
  slug: transitland-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Transitland Domain Security
  slug: transitland-domain-security
  summary_line: TLSv1.3 · DMARC
slug: transitland
tags:
- Transportation
- Public APIs
- Transit
- GTFS
- Open Data
- Routing
- Geospatial
website: https://www.transit.land
---
