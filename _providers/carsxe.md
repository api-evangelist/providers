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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 69.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Carsxe Agentic Access
  operation_count: 22
  slug: carsxe-agentic-access
  summary_line: 22 operations · 4 acting
api_count: 1
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
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: VIN decoding for North American and international vehicles — 2 operations (getVehicleSpecs, getInternationalVinDecoder) returning year, make, model, trim, engine, drivetrain, body style, dimensions, e
  name: CarsXE Specifications API
  phrasing_intents:
  - id: getVehicleSpecs
    intent: Decode a VIN into full vehicle specifications
    question: How do I decode a VIN into equipment, colors and warranty details?
  - id: getInternationalVinDecoder
    intent: Decode a non-US VIN
    question: Can I decode a VIN from a car built for the European or Asian market?
  phrasing_ops: 2
  slug: carsxe-specifications-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle market valuation — 2 operations (getMarketValue v1, getMarketValueV2) returning wholesale, retail and trade-in figures by VIN, with optional state, mileage and condition adjustment on v2.
  name: CarsXE Market Value API
  phrasing_intents:
  - id: getMarketValue
    intent: Get a vehicle's retail, trade-in and auction value
    question: What is the auction value of a car, alongside its retail and trade-in price?
  - id: getMarketValueV2
    intent: Get condition- and mileage-adjusted market values
    question: How much is my car worth wholesale given its mileage and condition?
  phrasing_ops: 2
  slug: carsxe-market-value-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Safety recall lookup — 6 operations covering single-VIN recalls, recalls by year/make/model, and the asynchronous Recalls Batch surface (submit up to 10,000 VINs, poll status, retrieve or download res
  name: CarsXE Recalls API
  phrasing_intents:
  - id: getVehicleRecalls
    intent: Check open safety recalls for a VIN
    question: Does my specific car have any open safety recalls?
  - id: getRecallsByYmm
    intent: Find recalls by year, make and model
    question: Can I look up recalls for a car model without knowing the VIN?
  - id: submitRecallsBatch
    intent: Submit a bulk batch of VINs for recall checks
    question: How do I check thousands of VINs for recalls in one go?
  - id: getRecallsBatchStatus
    intent: Check the progress of a bulk recall batch
    question: Is my bulk recall batch finished processing yet?
  - id: getRecallsBatchResults
    intent: Get per-VIN results of a completed recall batch
    question: Where do I get the per-VIN recall findings once a batch completes, as JSON?
  - id: downloadRecallsBatchResults
    intent: Download recall batch results as CSV
    question: Can I download a finished recall batch as a CSV spreadsheet?
  phrasing_ops: 6
  slug: carsxe-recalls-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle history reporting — 1 operation (getVehicleHistory) returning title records, junk and salvage events, insurance records, odometer readings and brand history for a VIN.
  name: CarsXE History API
  phrasing_intents:
  - id: getVehicleHistory
    intent: Get a vehicle history report by VIN
    question: Has this used car ever had a salvage or junk title?
  phrasing_ops: 1
  slug: carsxe-history-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle imagery search — 1 operation (getVehicleImages) returning photo links, thumbnails, sources and dimensions filtered by make, model, year, trim, colour, angle, photo type and transparent-backgro
  name: CarsXE Images API
  phrasing_intents:
  - id: getVehicleImages
    intent: Find photos of a vehicle by make and model
    question: Where can I get stock photos of a specific car make and model?
  phrasing_ops: 1
  slug: carsxe-images-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Image recognition — 2 operations (recognizePlate, vinOcr) that read a license plate or a VIN out of a supplied image URL or base64 payload, returning detected text, confidence scores and bounding boxe
  name: CarsXE Recognition API
  phrasing_intents:
  - id: recognizePlate
    intent: Read a license plate number from a car photo
    question: Can I read the license plate number from a photo of a car?
  - id: vinOcr
    intent: Extract a VIN from a photo
    question: Can I pull a VIN out of a picture of the dashboard or door sticker?
  phrasing_ops: 2
  slug: carsxe-recognition-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle lookup without a VIN — 3 operations (getYearMakeModel, getYearMakeModelOptions, decodeObdCode) returning trims, features and option packages by year/make/model, dropdown population data, and O
  name: CarsXE Year Make Model API
  phrasing_intents:
  - id: getYearMakeModel
    intent: Get vehicle data by year, make and model
    question: Can I get specs for a car when I only know its year, make and model?
  - id: getYearMakeModelOptions
    intent: Populate year, make, model and variant dropdowns
    question: How do I fill cascading year, make and model dropdowns in my car form?
  - id: decodeObdCode
    intent: Explain an OBD-II trouble code
    question: What does check engine code P0115 mean?
  phrasing_ops: 3
  slug: carsxe-year-make-model-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Encumbrance and theft screening — 1 operation (getLienTheft) returning active lien holders, theft reports and recovery status for a VIN, for lenders and pre-purchase due diligence.
  name: CarsXE Lien & Theft API
  phrasing_intents:
  - id: getLienTheft
    intent: Check a VIN for liens and theft records
    question: Is there an active lien on the car I'm about to buy?
  phrasing_ops: 1
  slug: carsxe-lien-theft-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: API key validation — 1 operation (validateKey) against /v1/auth/validate, the endpoint the CarsXE authentication guide documents for confirming that a key is present, valid and active before issuing p
  name: CarsXE Auth API
  phrasing_intents:
  - id: validateKey
    intent: Check that an API key is valid
    question: Is my CarsXE API key still valid?
  phrasing_ops: 1
  slug: carsxe-auth-api
- description: 'Remote Model Context Protocol server exposing the CarsXE vehicle-data endpoints as 12 named agent tools over streamable HTTP, authenticated with an X-API-Key header or an OAuth 2.1 authorization code '
  name: CarsXE MCP Server
  slug: carsxe-mcp-server
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Decode license plates into vehicle data
  name: CarsXE Plate Decoder API
  phrasing_intents:
  - id: decodePlate
    intent: Decode a license plate with the legacy v1 endpoint
    question: Does the older v1 plate decoder still work with legacy country codes like UK or IND?
  - id: decodeUsPlate
    intent: Look up a US vehicle and its VIN by plate
    question: How do I find the VIN of a US car from its license plate and state?
  - id: decodePlateV2
    intent: Decode a license plate from 60+ countries
    question: Can I decode a South African or Australian registration number into vehicle details?
  phrasing_ops: 3
  slug: carsxe-plate-decoder-api
artifact_total: 44
asyncapis:
- description: ''
  name: Carsxe Recalls Batch Webhooks
  slug: carsxe-recalls-batch-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/carsxe/overlays/carsxe-plate-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/carsxe-plate-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/carsxe/agentic-access/carsxe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carsxe-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/carsxe/packages/carsxe-packages.yml
  title: ''
  type: Packages
  url: packages/carsxe-packages.yml
- group: build
  href: https://artifacts.apis.io/carsxe/packages/carsxe-packages.yml
  title: ''
  type: SDKs
  url: packages/carsxe-packages.yml
- group: build
  href: https://artifacts.apis.io/carsxe/cli/carsxe-cli.yml
  title: ''
  type: CLI
  url: cli/carsxe-cli.yml
- group: agent
  href: https://artifacts.apis.io/carsxe/mcp/carsxe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carsxe-mcp.yml
- group: build
  href: https://artifacts.apis.io/carsxe/mcp/carsxe-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/carsxe-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/carsxe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/carsxe/llms/carsxe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carsxe-llms.txt
- group: agent
  href: https://artifacts.apis.io/carsxe/well-known/carsxe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carsxe-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://carsxe.com/.well-known/api-catalog
- group: design
  href: https://artifacts.apis.io/carsxe/conventions/carsxe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carsxe-conventions.yml
- group: design
  href: https://artifacts.apis.io/carsxe/conventions/carsxe-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/carsxe-conventions.yml
- group: design
  href: https://artifacts.apis.io/carsxe/conformance/carsxe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carsxe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://carsxe.com/trust
- group: auth
  href: https://artifacts.apis.io/carsxe/security/carsxe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/carsxe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/carsxe/security/carsxe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carsxe-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/carsxe/authentication/carsxe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carsxe-authentication.yml
- group: design
  href: https://artifacts.apis.io/carsxe/errors/carsxe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carsxe-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: https://carsxe.com/docs/errors
- group: design
  href: https://artifacts.apis.io/carsxe/data-model/carsxe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carsxe-data-model.yml
- group: build
  href: https://artifacts.apis.io/carsxe/examples/carsxe-examples.yml
  title: ''
  type: Examples
  url: examples/carsxe-examples.yml
- group: design
  href: https://artifacts.apis.io/carsxe/lifecycle/carsxe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/carsxe-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://carsxe.com/status
- group: operate
  title: ''
  type: Deprecation
  url: https://carsxe.com/docs/versioning
- group: design
  href: https://artifacts.apis.io/carsxe/asyncapi/carsxe-recalls-batch-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/carsxe-recalls-batch-webhooks.yml
- group: start
  href: https://artifacts.apis.io/carsxe/sandbox/carsxe-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/carsxe-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/carsxe/rate-limits/carsxe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/carsxe-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/carsxe/plans/carsxe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carsxe-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/carsxe/finops/carsxe-finops.yml
  title: ''
  type: FinOps
  url: finops/carsxe-finops.yml
- group: design
  href: https://artifacts.apis.io/carsxe/vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary.yml
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
  url: https://carsxe.com/
- group: start
  title: ''
  type: Portal
  url: https://carsxe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://carsxe.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://carsxe.com/docs/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://carsxe.com/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://carsxe.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://carsxe.com/pricing
- group: company
  title: ''
  type: About
  url: https://carsxe.com/about
- group: company
  title: ''
  type: Blog
  url: https://carsxe.com/blog
- group: operate
  title: ''
  type: Support
  url: https://carsxe.com/support
- group: operate
  title: ''
  type: Contact
  url: https://carsxe.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carsxe.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carsxe.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://carsxe.com/signin
- group: start
  title: ''
  type: SignUp
  url: https://carsxe.com/register
created: '2025-02-24'
description: CarsXE is a B2B vehicle data API platform operated by PiWaves, LLC, offering VIN decoding, vehicle specifications, market value estimates, vehicle history, vehicle imagery, license plate decoding and recognition, VIN OCR, OBD fault-code decoding, international VIN decoding, lien and theft screening, year/make/model lookup and single-VIN or 10,000-VIN batch recall checks. A single OpenAPI 3.1 contract covering 21 operations is published at api.carsxe.com/openapi.json, alongside a remote MCP server, an RFC 9727 api-catalog, an llms.txt index, first-party SDKs for eight languages, and a CLI. Designed for automotive marketplaces, dealerships, insurance, lending, fleet, parking and claims platforms that need programmatic access to rich, current vehicle data.
finops:
- has_sources: true
  method: derived
  name: Carsxe Finops
  primary_unit: subscription
  service_category: ''
  slug: carsxe-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carsxe.png
jsonld:
- class_count: 0
  name: Carsxe Context
  property_count: 8
  slug: carsxe-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.carsxe.com over HTTP requiring an API key; 12 tools listed.
  name: CarsXE MCP Server
  slug: carsxe
modified: '2026-09-05'
name: CarsXE
nav: Providers
network: true
overview: 'CarsXE publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Specifications API, Market Value API, Recalls API, and 18 more. Tagged areas include Automotive, Vehicles, VIN, Vehicle Data, and License Plate.


  The CarsXE catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CarsXE''s developer surface includes CLI, authentication, code examples, sandbox, developer portal, documentation, API reference, and 41 more developer resources.'
plans:
- name: Carsxe Plans Pricing
  plan_count: 4
  slug: carsxe-plans-pricing
- name: Carsxe Price Estimates
  plan_count: 0
  slug: carsxe-price-estimates
random_paper: 22
rate_limits:
- limit_count: 39
  name: Carsxe Rate Limits
  slug: carsxe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: CarsXE API Rules
  rule_count: 63
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 14
  slug: carsxe-rules
score:
  band: exemplar
  composite: 76.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 78.0
    catalog_earned_first_party: 24.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 67.2
    developer_ergonomics: 80.4
    discoverability: 85.0
    operational_transparency: 65.8
  previous_composite: 75.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 90.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/carsxe/carsxe-2026-06-20T174021.png
security:
- kind: authentication
  name: Carsxe Authentication
  slug: carsxe-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Carsxe Domain Security
  slug: carsxe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carsxe Trust Center
  slug: carsxe-trust-center
  summary_line: SOC 2 Type II, ISO 27001
skill_count: 5
skills:
- name: agent-onboarding
  slug: carsxe-agent-onboarding
- name: carsxe-bulk-recall-sweep
  slug: carsxe-bulk-recall-sweep
- name: carsxe-plate-photo-to-vehicle
  slug: carsxe-plate-photo-to-vehicle
- name: carsxe-vin-due-diligence
  slug: carsxe-vin-due-diligence
- name: carsxe-vin-ocr-intake
  slug: carsxe-vin-ocr-intake
slug: carsxe
tags:
- Automotive
- Vehicles
- VIN
- Vehicle Data
- License Plate
- OCR
- Automobiles
- Recalls
- Market Value
- Vehicle History
- MCP
- Agents
website: https://carsxe.com/
---
