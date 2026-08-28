---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Car Api Agentic Access
  operation_count: 17
  slug: car-api-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 18
apis:
- description: The CarAPI VIN Decoder API decodes Vehicle Identification Numbers into structured vehicle attributes including year, make, model, trim, body type, engine, transmission, and other specifications. It re
  name: CarAPI VIN Decoder API
  slug: vin-decoder-api
- description: The CarAPI License Plate API decodes license plates into vehicle records for US, Canada, Australia, and other supported countries, returning year/make/model/trim and related specifications.
  name: CarAPI License Plate API
  slug: license-plate-api
- description: The CarAPI OBD-II Code API provides search and lookup across more than 9,000 OBD-II diagnostic trouble codes (DTCs) with code descriptions, used in vehicle diagnostics and automotive repair software.
  name: CarAPI OBD-II Code API
  slug: obd-code-api
- description: The CarAPI Power Sports API provides vehicle specifications for power sports categories such as motorcycles, ATVs, UTVs, and similar motor vehicles, following the same REST/JSON conventions as the mai
  name: CarAPI Power Sports API
  slug: power-sports-api
- description: The Account API from Car API (carapi.app) — 2 operation(s) for account.
  name: Car API (carapi.app) Account API
  slug: car-api-account-api
- description: The Auth API from Car API (carapi.app) — 1 operation(s) for auth.
  name: Car API (carapi.app) Auth API
  slug: car-api-auth-api
- description: The Bodies API from Car API (carapi.app) — 1 operation(s) for bodies.
  name: Car API (carapi.app) Bodies API
  slug: car-api-bodies-api
- description: The Colors (Exterior) API from Car API (carapi.app) — 1 operation(s) for colors (exterior).
  name: Car API (carapi.app) Colors (Exterior) API
  slug: car-api-colors-exterior-api
- description: The Colors (Interior) API from Car API (carapi.app) — 1 operation(s) for colors (interior).
  name: Car API (carapi.app) Colors (Interior) API
  slug: car-api-colors-interior-api
- description: The Data Feeds API from Car API (carapi.app) — 2 operation(s) for data feeds.
  name: Car API (carapi.app) Data Feeds API
  slug: car-api-data-feeds-api
- description: The Engines API from Car API (carapi.app) — 1 operation(s) for engines.
  name: Car API (carapi.app) Engines API
  slug: car-api-engines-api
- description: The Makes API from Car API (carapi.app) — 1 operation(s) for makes.
  name: Car API (carapi.app) Makes API
  slug: car-api-makes-api
- description: The Mileages API from Car API (carapi.app) — 1 operation(s) for mileages.
  name: Car API (carapi.app) Mileages API
  slug: car-api-mileages-api
- description: The Models API from Car API (carapi.app) — 1 operation(s) for models.
  name: Car API (carapi.app) Models API
  slug: car-api-models-api
- description: The Trims API from Car API (carapi.app) — 2 operation(s) for trims.
  name: Car API (carapi.app) Trims API
  slug: car-api-trims-api
- description: The Vehicle Attributes API from Car API (carapi.app) — 1 operation(s) for vehicle attributes.
  name: Car API (carapi.app) Vehicle Attributes API
  slug: car-api-vehicle-attributes-api
- description: The Vin Decoder API from Car API (carapi.app) — 1 operation(s) for vin decoder.
  name: Car API (carapi.app) Vin Decoder API
  slug: car-api-vin-decoder-api
- description: The Years API from Car API (carapi.app) — 1 operation(s) for years.
  name: Car API (carapi.app) Years API
  slug: car-api-years-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Car Account API
  slug: open-car-api-account-api
- collection_type: open
  name: Car Account Auth API
  slug: open-car-api-auth-api
- collection_type: open
  name: Car Authentication API
  slug: open-car-api-authentication-api
- collection_type: open
  name: Car Account Bodies API
  slug: open-car-api-bodies-api
- collection_type: open
  name: Car Account Colors (Exterior) API
  slug: open-car-api-colors-exterior-api
- collection_type: open
  name: Car Account Colors (Interior) API
  slug: open-car-api-colors-interior-api
- collection_type: open
  name: Car Account Data Feeds API
  slug: open-car-api-data-feeds-api
- collection_type: open
  name: Car Account Engines API
  slug: open-car-api-engines-api
- collection_type: open
  name: Car Account Makes API
  slug: open-car-api-makes-api
- collection_type: open
  name: Car Account Mileages API
  slug: open-car-api-mileages-api
- collection_type: open
  name: Car Account Models API
  slug: open-car-api-models-api
- collection_type: open
  name: Car Account Trims API
  slug: open-car-api-trims-api
- collection_type: open
  name: Car Account Vehicle Attributes API
  slug: open-car-api-vehicle-attributes-api
- collection_type: open
  name: Car Authentication Vehicles API
  slug: open-car-api-vehicles-api
- collection_type: open
  name: Car Account Vin Decoder API
  slug: open-car-api-vin-decoder-api
- collection_type: open
  name: Car Account Years API
  slug: open-car-api-years-api
- collection_type: open
  name: CarAPI
  slug: open-carapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/car-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/car-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/car-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/car-api-team
- group: company
  title: ''
  type: Website
  url: https://carapi.app/
- group: docs
  title: ''
  type: Documentation
  url: https://carapi.app/docs
- group: other
  title: ''
  type: API
  url: https://carapi.app/api
- group: commercial
  title: ''
  type: Pricing
  url: https://carapi.app/pricing
- group: operate
  title: ''
  type: FAQ
  url: https://carapi.app/features/faq
- group: operate
  title: ''
  type: RateLimits
  url: https://carapi.app/docs/rate_limits/
- group: start
  title: ''
  type: Login
  url: https://carapi.app/login
- group: start
  title: ''
  type: Signup
  url: https://carapi.app/register
- group: operate
  title: ''
  type: Contact
  url: https://carapi.app/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carapi.app/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carapi.app/privacy-policy
created: '2024-07-11'
description: CarAPI is a developer-friendly vehicle API and database that provides programmatic access to automotive data including makes, models, trims, bodies, engines, mileage, VIN decoding, license plate decoding, OBD-II diagnostic codes, and power sports vehicle information. The platform follows a freemium model - its public vehicle dataset is available without an account, and paid plans unlock higher daily request limits and production use. The API is REST/JSON with JWT authentication and ships with OpenAPI, Swagger, ReDoc, and Postman documentation.
finops:
- name: Car Api Finops
  service_category: Automotive Data API
  slug: car-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/car-api.png
json_schemas:
- name: Exception
  property_count: 4
  slug: car-api-exception
- name: Make
  property_count: 2
  slug: car-api-make
- name: MakeModel
  property_count: 3
  slug: car-api-makemodel
- name: MakeModelTrim
  property_count: 9
  slug: car-api-makemodeltrim
- name: MakeModelTrimBody
  property_count: 18
  slug: car-api-makemodeltrimbody
- name: MakeModelTrimEngine
  property_count: 15
  slug: car-api-makemodeltrimengine
- name: MakeModelTrimExteriorColor
  property_count: 4
  slug: car-api-makemodeltrimexteriorcolor
- name: MakeModelTrimInteriorColor
  property_count: 4
  slug: car-api-makemodeltriminteriorcolor
- name: MakeModelTrimMileage
  property_count: 15
  slug: car-api-makemodeltrimmileage
- name: VehicleAttribute
  property_count: 0
  slug: car-api-vehicleattribute
- name: Year
  property_count: 0
  slug: car-api-year
json_structures:
- name: Car Api Structure
  property_count: 0
  slug: car-api-structure
layout: provider
modified: '2026-05-19'
name: Car API (carapi.app)
nav: Providers
network: true
overview: 'Car API (carapi.app) publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Bodies API, and 11 more. Tagged areas include Automobiles, Automotive Data, Cars, License Plate Decoder, and OBD-II.


  The Car API (carapi.app) catalog on APIs.io includes 1 Spectral governance ruleset.


  Car API (carapi.app)''s developer surface includes authentication, documentation, pricing, FAQ, signup flow, and 10 more developer resources.'
plans:
- name: Car Api Plans Pricing
  plan_count: 4
  slug: car-api-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Car Api Rate Limits
  slug: car-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Car API (carapi.app) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: car-api-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.9
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 9.8
    contract_quality: 58.9
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/car-api/refs/heads/main/screenshots/car-api-2026-06-20T173946.png
security:
- kind: authentication
  name: Car Api Authentication
  slug: car-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Car Api Domain Security
  slug: car-api-domain-security
  summary_line: TLSv1.3
slug: car-api
tags:
- Automobiles
- Automotive Data
- Cars
- License Plate Decoder
- OBD-II
- Power-Sports
- Vehicle API
- Vehicle Specifications
- Vehicles
- VIN Decoder
website: https://carapi.app/
---
