---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: United Airlines Agentic Access
  operation_count: 11
  slug: united-airlines-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 1
apis:
- description: United Airlines Flight Status API providing real-time flight status including estimated and actual departure and arrival times, gate information, delays, and flight tracking for United-operated flight
  name: United Airlines Flight Status API
  slug: united-airlines-flight-status-api
- baseURL: https://api.united.com/v1
  baseurl_source: declared
  description: Flight booking and reservation management
  name: United Airlines Booking API
  slug: united-airlines-booking-api
- baseURL: https://api.united.com/v1
  baseurl_source: declared
  description: Post-booking modifications, refunds, and ancillaries
  name: United Airlines Servicing API
  slug: united-airlines-servicing-api
- baseURL: https://api.united.com/v1
  baseurl_source: declared
  description: Flight search and pricing operations
  name: United Airlines Shopping API
  slug: united-airlines-shopping-api
- baseURL: https://api.united.com/v1
  baseurl_source: declared
  description: Flight status and schedule information
  name: United Airlines Status API
  slug: united-airlines-status-api
artifact_total: 25
collections:
- collection_type: open
  name: United Airlines NDC Booking API
  slug: open-united-airlines-booking-api
- collection_type: open
  name: United Airlines NDC Booking Servicing API
  slug: open-united-airlines-servicing-api
- collection_type: open
  name: United Airlines NDC Booking Shopping API
  slug: open-united-airlines-shopping-api
- collection_type: open
  name: United Airlines NDC Booking Status API
  slug: open-united-airlines-status-api
common:
- group: commercial
  href: https://artifacts.apis.io/united-airlines/plans/united-airlines-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/united-airlines-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/united-airlines/rate-limits/united-airlines-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/united-airlines-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/united-airlines/finops/united-airlines-finops.yml
  title: ''
  type: FinOps
  url: finops/united-airlines-finops.yml
- group: other
  href: https://artifacts.apis.io/united-airlines/capabilities/united-airlines-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/united-airlines-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/united-airlines/agentic-access/united-airlines-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/united-airlines-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/united-airlines/security/united-airlines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/united-airlines-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/united-airlines/authentication/united-airlines-authentication.yml
  title: ''
  type: Authentication
  url: authentication/united-airlines-authentication.yml
- group: auth
  href: https://artifacts.apis.io/united-airlines/scopes/united-airlines-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/united-airlines-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.united.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://united.business/NDC-corporate
- group: other
  title: ''
  type: NDC Capabilities
  url: https://united.business/NDC-capabilities
- group: operate
  title: ''
  type: Contact
  url: https://united.business/contact-form.html
- group: start
  title: ''
  type: IATA Developer Portal
  url: https://api.developer.iata.org/united-airlines-united-airlines-default/api/flight-status2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-airlines
- group: other
  title: ''
  type: X
  url: https://twitter.com/united
- group: other
  title: ''
  type: MileagePlus
  url: https://www.united.com/en/us/fly/mileageplus.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/openapi/united-airlines-ndc-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/rules/united-airlines-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-schema/united-airlines-booking-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-schema/united-airlines-flight-status-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-ld/united-airlines-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/vocabulary/united-airlines-vocabulary.yml
created: '2026-03-21'
description: United Airlines is a major American airline headquartered in Chicago, Illinois. It operates one of the largest route networks in the world with hubs in Chicago, Denver, Houston, Los Angeles, New York, San Francisco, and Washington, D.C. United provides NDC (New Distribution Capability) APIs for flight shopping, booking, and servicing, as well as corporate travel integration capabilities.
examples:
- key_count: 2
  name: United Airlines Createbooking Example
  slug: united-airlines-createBooking-example
- key_count: 2
  name: United Airlines Getflightstatus Example
  slug: united-airlines-getFlightStatus-example
- key_count: 2
  name: United Airlines Searchflightoffers Example
  slug: united-airlines-searchFlightOffers-example
finops:
- has_sources: true
  method: generated
  name: United Airlines Finops
  primary_unit: ''
  service_category: Travel
  slug: united-airlines-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-airlines.png
json_schemas:
- name: United Airlines Booking
  property_count: 8
  slug: united-airlines-booking
- name: United Airlines Flight Status
  property_count: 14
  slug: united-airlines-flight-status
json_structures:
- name: United Airlines Booking Structure
  property_count: 0
  slug: united-airlines-booking-structure
jsonld:
- class_count: 0
  name: United Airlines Context
  property_count: 41
  slug: united-airlines-context
layout: provider
modified: '2026-05-19'
name: United Airlines
nav: Providers
network: true
overview: 'United Airlines publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Booking API, Servicing API, Shopping API, and 2 more. Tagged areas include Airlines, Travel, Flight Booking, NDC, and Loyalty.


  The United Airlines catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United Airlines'' developer surface includes authentication and 21 more developer resources.'
plans:
- name: United Airlines Plans Pricing
  plan_count: 1
  slug: united-airlines-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: United Airlines Rate Limits
  slug: united-airlines-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: United Airlines — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: united-airlines-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: United Airlines API Rules
  rule_count: 15
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 9
  slug: united-airlines-rules
scopes:
- name: United Airlines Scopes
  scope_count: 2
  slug: united-airlines-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 27.3
    contract_quality: 56.9
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/united-airlines/united-airlines-2026-06-20T200049.png
security:
- kind: authentication
  name: United Airlines Authentication
  slug: united-airlines-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: United Airlines Domain Security
  slug: united-airlines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: united-airlines
tags:
- Airlines
- Travel
- Flight Booking
- NDC
- Loyalty
- Fortune 100
- Aviation
website: https://www.united.com
---
