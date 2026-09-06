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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.3
  scored_at: '2026-09-05'
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
  slug: carsxe-specifications-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle market valuation — 2 operations (getMarketValue v1, getMarketValueV2) returning wholesale, retail and trade-in figures by VIN, with optional state, mileage and condition adjustment on v2.
  name: CarsXE Market Value API
  slug: carsxe-market-value-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: License plate decoding — 3 operations (decodePlate, decodeUsPlate, decodePlateV2) resolving a registration plate plus country/state to vehicle make, model, year and (where available) VIN, across 50+ c
  name: CarsXE Plate Decoder API
  slug: carsxe-plate-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Safety recall lookup — 6 operations covering single-VIN recalls, recalls by year/make/model, and the asynchronous Recalls Batch surface (submit up to 10,000 VINs, poll status, retrieve or download res
  name: CarsXE Recalls API
  slug: carsxe-recalls-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle history reporting — 1 operation (getVehicleHistory) returning title records, junk and salvage events, insurance records, odometer readings and brand history for a VIN.
  name: CarsXE History API
  slug: carsxe-history-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle imagery search — 1 operation (getVehicleImages) returning photo links, thumbnails, sources and dimensions filtered by make, model, year, trim, colour, angle, photo type and transparent-backgro
  name: CarsXE Images API
  slug: carsxe-images-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Image recognition — 2 operations (recognizePlate, vinOcr) that read a license plate or a VIN out of a supplied image URL or base64 payload, returning detected text, confidence scores and bounding boxe
  name: CarsXE Recognition API
  slug: carsxe-recognition-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Vehicle lookup without a VIN — 3 operations (getYearMakeModel, getYearMakeModelOptions, decodeObdCode) returning trims, features and option packages by year/make/model, dropdown population data, and O
  name: CarsXE Year Make Model API
  slug: carsxe-year-make-model-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: Encumbrance and theft screening — 1 operation (getLienTheft) returning active lien holders, theft reports and recovery status for a VIN, for lenders and pre-purchase due diligence.
  name: CarsXE Lien & Theft API
  slug: carsxe-lien-theft-api
- baseURL: https://api.carsxe.com
  baseurl_source: declared
  description: API key validation — 1 operation (validateKey) against /v1/auth/validate, the endpoint the CarsXE authentication guide documents for confirming that a key is present, valid and active before issuing p
  name: CarsXE Auth API
  slug: carsxe-auth-api
- description: 'Remote Model Context Protocol server exposing the CarsXE vehicle-data endpoints as 12 named agent tools over streamable HTTP, authenticated with an X-API-Key header or an OAuth 2.1 authorization code '
  name: CarsXE MCP Server
  slug: carsxe-mcp-server
artifact_total: 38
asyncapis:
- description: ''
  name: Carsxe Recalls Batch Webhooks
  slug: carsxe-recalls-batch-webhooks
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
- group: build
  title: ''
  type: Packages
  url: packages/carsxe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/carsxe-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/carsxe-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/carsxe-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/carsxe-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carsxe-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carsxe-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://carsxe.com/.well-known/api-catalog
- group: design
  title: ''
  type: Conventions
  url: conventions/carsxe-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/carsxe-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carsxe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://carsxe.com/trust
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
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carsxe-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: https://carsxe.com/docs/errors
- group: design
  title: ''
  type: DataModel
  url: data-model/carsxe-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/carsxe-examples.yml
- group: design
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
  title: ''
  type: Webhooks
  url: asyncapi/carsxe-recalls-batch-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/carsxe-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carsxe-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/carsxe-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/carsxe-finops.yml
- group: design
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
mcp_servers:
- description: ''
  name: CarsXE MCP Server
  slug: carsxe-mcp-server
modified: '2026-09-05'
name: CarsXE
nav: Providers
network: true
overview: 'CarsXE publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Specifications API, Market Value API, Plate Decoder API, and 7 more. Tagged areas include Automotive, Vehicles, VIN, Vehicle Data, and License Plate.


  The CarsXE catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  CarsXE''s developer surface includes CLI, authentication, code examples, sandbox, developer portal, documentation, API reference, and 40 more developer resources.'
plans:
- name: Carsxe Plans Pricing
  plan_count: 4
  slug: carsxe-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 39
  name: Carsxe Rate Limits
  slug: carsxe-rate-limits
score:
  band: exemplar
  composite: 74.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 74.0
    catalog_earned_first_party: 24.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 33.5
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 33.3
    contract_quality: 70.2
    developer_ergonomics: 80.4
    discoverability: 87.0
    governance: 33.3
    operational_transparency: 65.8
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/carsxe/refs/heads/main/screenshots/carsxe-2026-06-20T174021.png
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
- Model Context Protocol
- Agents
website: https://carsxe.com/
---
