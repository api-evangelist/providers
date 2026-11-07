---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Flightpowers Com Agentic Access
  operation_count: 14
  slug: flightpowers-com-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 2
apis:
- baseURL: https://api.flightpowers.com
  baseurl_source: spec
  description: Key verification.
  name: flightpowers-com Account API
  slug: flightpowers-com-account-api
- baseURL: https://api.flightpowers.com
  baseurl_source: spec
  description: The Flights API from flightpowers-com — 2 operation(s) for flights.
  name: flightpowers-com Flights API
  slug: flightpowers-com-flights-api
- baseURL: https://api.flightpowers.com
  baseurl_source: spec
  description: The Hotels API from flightpowers-com — 4 operation(s) for hotels.
  name: flightpowers-com Hotels API
  slug: flightpowers-com-hotels-api
- description: The Verify API from flightpowers-com — 1 operation(s) for verify.
  name: flightpowers-com Verify API
  slug: flightpowers-com-verify-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/flightpowers-com/agentic-access/flightpowers-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flightpowers-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/flightpowers-com/plans/flightpowers-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flightpowers-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flightpowers-com/rules/flightpowers-com-rules.yml
  title: ''
  type: Spectral
  url: rules/flightpowers-com-rules.yml
- group: design
  href: https://artifacts.apis.io/flightpowers-com/json-ld/flightpowers-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flightpowers-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/flightpowers-com/vocabulary/flightpowers-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flightpowers-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/flightpowers-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/flightpowers-com/data-model/flightpowers-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flightpowers-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/flightpowers-com/authentication/flightpowers-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flightpowers-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/flightpowers-com/errors/flightpowers-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flightpowers-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flightpowers-com/conformance/flightpowers-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flightpowers-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flightpowers-com/llms/flightpowers-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flightpowers-com-llms.txt
- group: other
  href: https://artifacts.apis.io/flightpowers-com/hosts/flightpowers-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flightpowers-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/flightpowers-com/vendors/flightpowers-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flightpowers-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://flightpowers.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://flightpowers.com/changelog
- group: auth
  href: https://artifacts.apis.io/flightpowers-com/security/flightpowers-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flightpowers-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flightpowers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://flightpowers.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://flightpowers.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://flightpowers.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://flightpowers.com/contact
- group: company
  title: ''
  type: Blog
  url: https://flightpowers.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mtnrabi
- group: commercial
  title: ''
  type: Pricing
  url: https://flightpowers.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flightpowers.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flightpowers.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/mtnrabi/workspace/flightpowers
created: '2026-10-30'
description: FlightPowers provides live travel data APIs for flights and hotels, offering developers endpoint‑by‑endpoint documentation, pricing tiers, and integration guides. Founded by software engineer Matan Rabi, the service scrapes live Google Flights and Booking.com data to deliver up‑to‑date pricing, with free tier limits and paid plans for higher volume.
image: https://flightpowers.com/og/RmxpZ2h0UG93ZXJzOiB0cmF2ZWwgZGF0YSBBUEksIGxpdmUgZmxpZ2h0IGFuZCBob3RlbCBwcmljZXM.png
json_schemas:
- name: HotelByNameRequest
  property_count: 9
  slug: flightpowers-com-hotel-by-name-request
- name: HotelSearchRequest
  property_count: 10
  slug: flightpowers-com-hotel-search-request
- name: OnewayFlight
  property_count: 16
  slug: flightpowers-com-oneway-flight
- name: OnewayRequest
  property_count: 19
  slug: flightpowers-com-oneway-request
- name: RoundtripItinerary
  property_count: 22
  slug: flightpowers-com-roundtrip-itinerary
- name: RoundtripRequest
  property_count: 28
  slug: flightpowers-com-roundtrip-request
jsonld:
- class_count: 17
  name: Flightpowers Com Context
  property_count: 101
  slug: flightpowers-com-context
layout: provider
modified: '2026-10-30'
name: flightpowers-com
nav: Providers
network: true
overview: 'flightpowers-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Flights API, Hotels API, and 1 more. Tagged areas include Company, Travel, Data, Flights, and Hotels.


  The flightpowers-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  flightpowers-com''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 20 more developer resources.'
plans:
- name: Flightpowers Com Plans Pricing
  plan_count: 15
  slug: flightpowers-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: flightpowers-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: flightpowers-com-rules
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 58.0
    developer_ergonomics: 38.6
    discoverability: 64.3
    operational_transparency: 18.4
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/flightpowers-com/flightpowers-com-2026-11-03T132146.png
security:
- kind: authentication
  name: Flightpowers Com Authentication
  slug: flightpowers-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Flightpowers Com Domain Security
  slug: flightpowers-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: verify-key
  slug: flightpowers-com-verify-key
slug: flightpowers-com
tags:
- Company
- Travel
- Data
- Flights
- Hotels
website: https://flightpowers.com/
---
