---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
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
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Tourradar Agentic Access
  operation_count: 21
  slug: tourradar-agentic-access
  summary_line: 21 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.b2b.tourradar.com
  baseurl_source: declared
  description: The Bookings API from TourRadar — 5 operation(s) for bookings.
  name: TourRadar Bookings API
  slug: tourradar-bookings-api
- baseURL: https://api.b2b.tourradar.com
  baseurl_source: declared
  description: The Bulk API from TourRadar — 2 operation(s) for bulk.
  name: TourRadar Bulk API
  slug: tourradar-bulk-api
- baseURL: https://api.b2b.tourradar.com
  baseurl_source: declared
  description: The Operators API from TourRadar — 3 operation(s) for operators.
  name: TourRadar Operators API
  slug: tourradar-operators-api
- baseURL: https://api.b2b.tourradar.com
  baseurl_source: declared
  description: The Pricing & Availability API from TourRadar — 4 operation(s) for pricing & availability.
  name: TourRadar Pricing & Availability API
  slug: tourradar-pricing-availability-api
- baseURL: https://api.b2b.tourradar.com
  baseurl_source: declared
  description: The Taxonomy API from TourRadar — 4 operation(s) for taxonomy.
  name: TourRadar Taxonomy API
  slug: tourradar-taxonomy-api
- baseURL: https://api.b2b.tourradar.com
  baseurl_source: declared
  description: The Tours API from TourRadar — 2 operation(s) for tours.
  name: TourRadar Tours API
  slug: tourradar-tours-api
artifact_total: 21
common:
- group: other
  href: https://artifacts.apis.io/tourradar/capabilities/tourradar-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tourradar-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/tourradar/agentic-access/tourradar-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tourradar-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tourradar/rate-limits/tourradar-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tourradar-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tourradar/rules/tourradar-rules.yml
  title: ''
  type: Spectral
  url: rules/tourradar-rules.yml
- group: design
  href: https://artifacts.apis.io/tourradar/json-ld/tourradar-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tourradar-context.jsonld
- group: design
  href: https://artifacts.apis.io/tourradar/vocabulary/tourradar-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tourradar-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tourradar/data-model/tourradar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tourradar-data-model.yml
- group: design
  href: https://artifacts.apis.io/tourradar/conventions/tourradar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tourradar-conventions.yml
- group: start
  href: https://artifacts.apis.io/tourradar/sandbox/tourradar-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tourradar-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tourradar/errors/tourradar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tourradar-problem-types.yml
- group: other
  href: https://artifacts.apis.io/tourradar/hosts/tourradar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tourradar-hosts.yml
- group: other
  href: https://artifacts.apis.io/tourradar/vendors/tourradar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tourradar-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.tourradar.com/trust
- group: auth
  href: https://artifacts.apis.io/tourradar/security/tourradar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tourradar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tourradar.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.api.b2b.tourradar.com
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.api.b2b.tourradar.com/docs
- group: start
  title: ''
  type: Login
  url: https://dashboard.api.b2b.tourradar.com/signin
- group: operate
  title: ''
  type: Support
  url: https://customer.help.tourradar.com/wiki/spaces/CS/overview
- group: company
  title: ''
  type: Blog
  url: https://www.daystocome.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TourRadar
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tourradar.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tourradar.com/privacy
- group: company
  title: ''
  type: About
  url: https://www.tourradar.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sandbox.b2b.tourradar.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.tourradar.com/press
- group: operate
  title: ''
  type: Support
  url: https://support.tourradar.com/
- group: auth
  href: https://artifacts.apis.io/tourradar/authentication/tourradar-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tourradar-authentication.yml
- group: auth
  href: https://artifacts.apis.io/tourradar/scopes/tourradar-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tourradar-scopes.yml
- group: other
  href: https://artifacts.apis.io/tourradar/well-known/tourradar-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/tourradar-openid-configuration.json
- group: agent
  href: https://artifacts.apis.io/tourradar/well-known/tourradar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tourradar-well-known.yml
- group: auth
  href: https://artifacts.apis.io/tourradar/well-known/tourradar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tourradar-security.txt
- group: agent
  href: https://artifacts.apis.io/tourradar/llms/tourradar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tourradar-llms.txt
- group: design
  href: https://artifacts.apis.io/tourradar/conformance/tourradar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tourradar-conformance.yml
- group: design
  href: https://artifacts.apis.io/tourradar/components/tourradar-components.yml
  title: ''
  type: Components
  url: components/tourradar-components.yml
- group: auth
  href: https://artifacts.apis.io/tourradar/security/tourradar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tourradar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tourradar.com/.well-known/security.txt
created: '2026-07-17'
description: TourRadar is the world's largest online marketplace for multi-day organized adventures, connecting travelers with more than 50,000 tours, safaris, and river cruises from over 2,500 vetted operators worldwide. Headquartered in Vienna, Austria, the company also operates a B2B Distribution API that lets OTAs, airlines, GDSs, and travel agencies search tour content and book departures through a unified API, alongside embeddable booking widgets and an affiliate program (RISE) for creators and publishers.
image: https://cdn.tourradar.com/s3/content-pages/391/1200x630/j705A8.png
json_schemas:
- name: BookingInput
  property_count: 11
  slug: tourradar-booking-input
- name: BookingResponse
  property_count: 1
  slug: tourradar-booking-response
- name: Booking
  property_count: 30
  slug: tourradar-booking
- name: TourDeparturePrice
  property_count: 5
  slug: tourradar-tour-departure-price
- name: TourDeparture
  property_count: 8
  slug: tourradar-tour-departure
- name: Tour
  property_count: 29
  slug: tourradar-tour
jsonld:
- class_count: 67
  name: Tourradar Context
  property_count: 211
  slug: tourradar-context
layout: provider
modified: '2026-10-20'
name: TourRadar
nav: Providers
network: true
overview: 'TourRadar publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bookings API, Bulk API, Operators API, and 3 more. Tagged areas include Travel, Tours, Booking, Marketplace, and Adventure Travel.


  The TourRadar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TourRadar''s developer surface includes sandbox, documentation, support, engineering blog, API reference, authentication, and 31 more developer resources.'
plans:
- name: Tourradar Plans Pricing
  plan_count: 0
  slug: tourradar-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Tourradar Rate Limits
  slug: tourradar-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: TourRadar API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: tourradar-rules
scopes:
- name: Tourradar Scopes
  scope_count: 24
  slug: tourradar-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 70.0
    catalog_earned_first_party: 8.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 31.6
    contract_governance: 33.3
    contract_quality: 62.9
    developer_ergonomics: 29.8
    discoverability: 74.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 42.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tourradar/tourradar-2026-09-02T163955.png
security:
- kind: authentication
  name: Tourradar Authentication
  slug: tourradar-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Tourradar Domain Security
  slug: tourradar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tourradar Vulnerability Disclosure
  slug: tourradar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tourradar
tags:
- Travel
- Tours
- Booking
- Marketplace
- Adventure Travel
- Distribution
- Affiliates
website: https://www.tourradar.com
---
