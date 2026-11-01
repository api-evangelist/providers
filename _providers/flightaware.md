---
access_model:
  confidence: medium
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
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Flightaware Agentic Access
  operation_count: 69
  slug: flightaware-agentic-access
  summary_line: 69 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'AeroAPI is FlightAware''s query-based REST API for accessing aviation data on demand. It exposes 60+ endpoints across flights, airports, operators, alerts, history, and Foresight predictive analytics, '
  name: FlightAware AeroAPI
  slug: aeroapi
- description: Firehose is FlightAware's real-time streaming feed of global flight data, delivering ADS-B, radar, and ATC-derived position, status, and event messages over a persistent TLS connection for enterprise-
  name: FlightAware Firehose
  slug: firehose
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The airports API from FlightAware — 17 operation(s) for airports.
  name: FlightAware Airports API
  slug: flightaware-airports-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: AeroAPI alerting can be used to configure and receive real-time alerts on key flight events. With customizable alerting offered by our alert endpoints, AeroAPI empowers users to selectively pick vario
  name: FlightAware Alerts API
  slug: flightaware-alerts-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The flights API from FlightAware — 11 operation(s) for flights.
  name: FlightAware Flights API
  slug: flightaware-flights-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: 'Foresight endpoints provide access to FlightAware''s Foresight predictive models and predictions for key events. Our advanced machine learning (ML) models identify key influencing factors for a flight '
  name: FlightAware Foresight API
  slug: flightaware-foresight-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The history API from FlightAware — 5 operation(s) for history.
  name: FlightAware History API
  slug: flightaware-history-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The miscellaneous API from FlightAware — 6 operation(s) for miscellaneous.
  name: FlightAware Miscellaneous API
  slug: flightaware-miscellaneous-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The operators API from FlightAware — 8 operation(s) for operators.
  name: FlightAware Operators API
  slug: flightaware-operators-api
- baseURL: https://aeroapi.flightaware.com/aeroapi
  baseurl_source: declared
  description: The account surface of AeroAPI — GET /account/usage, added in AeroAPI 4.30.0. It reports the calling account's AeroAPI consumption over a requested period, and it is the only in-band signal a consumer
  name: FlightAware Account API
  slug: flightaware-account-api
artifact_total: 30
asyncapis:
- description: ''
  name: Flightaware Events
  slug: flightaware-events
collections:
- collection_type: open
  name: Aero airports API
  slug: open-flightaware-airports-api
- collection_type: open
  name: Aero airports alerts API
  slug: open-flightaware-alerts-api
- collection_type: open
  name: Aero airports flights API
  slug: open-flightaware-flights-api
- collection_type: open
  name: Aero airports foresight API
  slug: open-flightaware-foresight-api
- collection_type: open
  name: Aero airports history API
  slug: open-flightaware-history-api
- collection_type: open
  name: Aero airports miscellaneous API
  slug: open-flightaware-miscellaneous-api
- collection_type: open
  name: Aero airports operators API
  slug: open-flightaware-operators-api
- collection_type: open
  name: AeroAPI
  slug: open-flightaware
common:
- group: other
  href: https://artifacts.apis.io/flightaware/capabilities/flightaware-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/flightaware-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/flightaware/agentic-access/flightaware-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flightaware-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/flightaware/security/flightaware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flightaware-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/flightaware/authentication/flightaware-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flightaware-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flightaware
- group: company
  title: ''
  type: Website
  url: https://www.flightaware.com/
- group: other
  title: ''
  type: CommercialData
  url: https://www.flightaware.com/commercial/data/
- group: docs
  title: ''
  type: Documentation
  url: https://www.flightaware.com/aeroapi/portal/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flightaware.com/commercial/aeroapi/
- group: company
  title: ''
  type: Blog
  url: https://blog.flightaware.com/
- group: operate
  title: ''
  type: Support
  url: https://www.flightaware.com/about/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flightaware.com/about/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flightaware.com/about/termsofuse
- group: build
  title: ''
  type: GitHub
  url: https://github.com/flightaware
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.flightaware.com/aeroapi/portal/
- group: docs
  title: ''
  type: APIReference
  url: https://www.flightaware.com/aeroapi/portal/documentation
- group: start
  title: ''
  type: SignUp
  url: https://www.flightaware.com/account/join/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flightaware.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.flightaware.com/commercial/firehose/documentation/revisionhistory
- group: design
  href: https://artifacts.apis.io/flightaware/lifecycle/flightaware-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flightaware-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/flightaware/changelog/flightaware-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flightaware-changelog.yml
- group: design
  href: https://artifacts.apis.io/flightaware/conventions/flightaware-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flightaware-conventions.yml
- group: design
  href: https://artifacts.apis.io/flightaware/errors/flightaware-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flightaware-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flightaware/conformance/flightaware-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flightaware-conformance.yml
- group: design
  href: https://artifacts.apis.io/flightaware/data-model/flightaware-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flightaware-data-model.yml
- group: design
  href: https://artifacts.apis.io/flightaware/asyncapi/flightaware-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/flightaware-events.yml
- group: build
  href: https://artifacts.apis.io/flightaware/packages/flightaware-packages.yml
  title: ''
  type: Packages
  url: packages/flightaware-packages.yml
- group: agent
  href: https://artifacts.apis.io/flightaware/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/flightaware/llms/flightaware-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flightaware-llms.txt
- group: agent
  href: https://artifacts.apis.io/flightaware/mcp/flightaware-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/flightaware-mcp.yml
- group: other
  href: https://artifacts.apis.io/flightaware/wsdl/flightaware-flightxml2.wsdl
  title: ''
  type: WSDL
  url: wsdl/flightaware-flightxml2.wsdl
- group: other
  href: https://artifacts.apis.io/flightaware/wsdl/flightaware-flightxml3.wsdl
  title: ''
  type: WSDL
  url: wsdl/flightaware-flightxml3.wsdl
- group: operate
  href: https://artifacts.apis.io/flightaware/rate-limits/flightaware-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flightaware-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/flightaware/plans/flightaware-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flightaware-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/flightaware/finops/flightaware-finops.yml
  title: ''
  type: FinOps
  url: finops/flightaware-finops.yml
created: '2025-02-24'
description: FlightAware is a global flight tracking and data platform that provides real-time flight tracking, mapping, and predictive technology to both individual users and commercial aviation companies. The platform collects data from a variety of sources including air traffic control systems, radar, ADS-B, and satellite data, and exposes that data to developers and commercial customers through its AeroAPI query-based REST API and its Firehose streaming feed.
finops:
- has_sources: true
  method: derived
  name: Flightaware Finops
  primary_unit: monthly minimum fee
  service_category: ''
  slug: flightaware-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flightaware.png
layout: provider
modified: '2026-09-10'
name: FlightAware
nav: Providers
network: true
overview: 'FlightAware publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Airports API, Alerts API, Flights API, and 7 more. Tagged areas include Aviation, Flights, Flight Tracking, Mapping, and Radar.


  The FlightAware catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FlightAware''s developer surface includes authentication, documentation, pricing, engineering blog, support, GitHub presence, API reference, and 28 more developer resources.'
plans:
- name: Flightaware Plans Pricing
  plan_count: 5
  slug: flightaware-plans-pricing
- name: Flightaware Price Estimates
  plan_count: 0
  slug: flightaware-price-estimates
random_paper: 14
rate_limits:
- limit_count: 6
  name: Flightaware Rate Limits
  slug: flightaware-rate-limits
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 47.0
    discoverability: 57.1
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flightaware/flightaware-2026-10-11T185622.png
security:
- kind: authentication
  name: Flightaware Authentication
  slug: flightaware-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flightaware Domain Security
  slug: flightaware-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: Build an airport operations board with AeroAPI
  slug: flightaware-airport-operations-board
- name: Configure AeroAPI flight alerts (push webhooks)
  slug: flightaware-configure-flight-alerts
- name: Research historical flights with AeroAPI
  slug: flightaware-historical-flight-research
- name: Track a flight with AeroAPI
  slug: flightaware-track-a-flight
slug: flightaware
tags:
- Aviation
- Flights
- Flight Tracking
- Mapping
- Radar
- Satellite
- Traffic Control
website: https://www.flightaware.com/
---
