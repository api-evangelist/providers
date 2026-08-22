---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Carsxe Agentic Access
  operation_count: 5
  slug: carsxe-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 15
apis:
- description: VIN decoding and comprehensive vehicle specification lookup. Returns year, make, model, trim, engine, drivetrain, body style, and detailed feature and option data for a given North American VIN.
  name: CarsXE Vehicle Specifications API
  slug: vehicle-specifications-api
- description: Returns market value estimates (retail, wholesale, trade-in) for new and used vehicles by VIN, informed by millions of historical vehicle sales.
  name: CarsXE Vehicle Market Value API
  slug: vehicle-market-value-api
- description: Retrieves high-quality photos of vehicles by year, make, model (and optional trim / color / background-transparency options) for use in marketplaces, dealer sites, and comparison tools.
  name: CarsXE Vehicle Images API
  slug: vehicle-images-api
- description: OCR endpoint that extracts a VIN string from an image of a VIN plate, windshield, or document, enabling mobile-first vehicle-onboarding and inspection workflows.
  name: CarsXE VIN OCR API
  slug: vin-ocr-api
- description: Decodes vehicle information from a license plate plus state/province, returning make, model, year, and VIN where available.
  name: CarsXE Vehicle Plate Decoder API
  slug: vehicle-plate-decoder-api
- description: Image-to-text OCR for license plates. Paired with the Plate Decoder, enables full vehicle lookup starting from a plate image, supporting parking, access-control, law-enforcement, and valet use cases.
  name: CarsXE Vehicle Plate Recognition API
  slug: vehicle-plate-recognition-api
- description: Raw vehicle-history data endpoint returning title records, accident history, odometer readings, service history, and salvage/lemon flags for a given VIN.
  name: CarsXE Vehicle History API
  slug: vehicle-history-api
- description: Returns safety-recall and campaign data for a given VIN, sourced from manufacturer and NHTSA data, for use in inspection, compliance, and pre-purchase workflows.
  name: CarsXE Vehicle Recalls API
  slug: vehicle-recalls-api
- description: VIN decoding for non-US vehicles, returning make, model, year, and market-specific trim/spec data for international markets.
  name: CarsXE International VIN Decoder API
  slug: international-vin-decoder-api
- description: Matches an OBD-II diagnostic trouble code (DTC) to a human-readable vehicle fault description for use in service, maintenance, and connected-car applications.
  name: CarsXE OBD Codes Decoder API
  slug: obd-codes-decoder-api
- description: The Auth API from CarsXE — 1 operation(s) for auth.
  name: CarsXE Auth API
  slug: carsxe-auth-api
- description: The Market Value API from CarsXE — 1 operation(s) for market value.
  name: CarsXE Market Value API
  slug: carsxe-market-value-api
- description: The Plate API from CarsXE — 1 operation(s) for plate.
  name: CarsXE Plate API
  slug: carsxe-plate-api
- description: The Recalls API from CarsXE — 1 operation(s) for recalls.
  name: CarsXE Recalls API
  slug: carsxe-recalls-api
- description: The Specifications API from CarsXE — 1 operation(s) for specifications.
  name: CarsXE Specifications API
  slug: carsxe-specifications-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CarsXE Vehicle Data Auth API
  slug: open-carsxe-auth-api
- collection_type: open
  name: CarsXE Vehicle Data Auth Market Value API
  slug: open-carsxe-market-value-api
- collection_type: open
  name: CarsXE Vehicle Data Auth Plate API
  slug: open-carsxe-plate-api
- collection_type: open
  name: CarsXE Vehicle Data Auth Recalls API
  slug: open-carsxe-recalls-api
- collection_type: open
  name: CarsXE Vehicle Data Auth Specifications API
  slug: open-carsxe-specifications-api
- collection_type: open
  name: CarsXE Vehicle Data API
  slug: open-carsxe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carsxe-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/carsxe-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carsxe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carsxe-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carsxe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carsxe
- group: company
  title: ''
  type: Website
  url: https://api.carsxe.com/
- group: start
  title: ''
  type: Portal
  url: https://api.carsxe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.carsxe.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.carsxe.com/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://api.carsxe.com/docs/authentication
- group: design
  title: ''
  type: ErrorCodes
  url: https://api.carsxe.com/docs/errors
- group: commercial
  title: ''
  type: Pricing
  url: https://api.carsxe.com/pricing
- group: company
  title: ''
  type: About
  url: https://api.carsxe.com/about
- group: company
  title: ''
  type: Blog
  url: https://api.carsxe.com/blog
- group: operate
  title: ''
  type: Support
  url: https://api.carsxe.com/support
- group: operate
  title: ''
  type: Contact
  url: https://api.carsxe.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.carsxe.com/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://api.carsxe.com/login
- group: start
  title: ''
  type: Signup
  url: https://api.carsxe.com/register
created: '2025-02-24'
description: CarsXE is a comprehensive vehicle data API platform offering VIN decoding, vehicle specifications, market value estimates, vehicle history, vehicle imagery, license plate recognition, OBD fault-code decoding, international VIN decoding, and recall lookups. Designed for automotive marketplaces, dealerships, insurance, lending, fleet, and claims platforms that need programmatic access to rich, current vehicle data.
finops:
- name: Carsxe Finops
  service_category: API
  slug: carsxe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carsxe.png
jsonld:
- class_count: 0
  name: Carsxe Context
  property_count: 8
  slug: carsxe-context
layout: provider
modified: '2026-04-23'
name: CarsXE
nav: Providers
network: true
overview: 'CarsXE publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Market Value API, Plate API, and 2 more. Tagged areas include Automotive, Vehicles, VIN, Vehicle Data, and License Plate.


  The CarsXE catalog on APIs.io includes 1 JSON-LD context.


  CarsXE''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 13 more developer resources.'
plans:
- name: Carsxe Plans Pricing
  plan_count: 3
  slug: carsxe-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Carsxe Rate Limits
  slug: carsxe-rate-limits
score:
  band: developing
  composite: 42.3
  delta: -1.7
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carsxe/refs/heads/main/screenshots/carsxe-2026-06-20T174021.png
security:
- kind: authentication
  name: Carsxe Authentication
  slug: carsxe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Carsxe Domain Security
  slug: carsxe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carsxe Trust Center
  slug: carsxe-trust-center
  summary_line: SOC 2, ISO 27001
slug: carsxe
tags:
- Automotive
- Vehicles
- VIN
- Vehicle Data
- License Plate
- OCR
- Automobiles
website: https://api.carsxe.com/
---
