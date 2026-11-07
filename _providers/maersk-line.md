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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Maersk Line Agentic Access
  operation_count: 20
  slug: maersk-line-agentic-access
  summary_line: 20 operations · 6 acting
api_count: 8
apis:
- description: Container Maintenance and Repair (M&R) API surfacing equipment-management events and repair workflow data for Maersk container assets.
  name: Maersk Container Maintenance and Repair API
  slug: maersk-container-maintenance-repair-api
- baseURL: https://api.maersk.com
  baseurl_source: spec
  description: Air freight bookings.
  name: Maersk AirBookings API
  slug: maersk-line-airbookings-api
- baseURL: https://api.maersk.com
  baseurl_source: spec
  description: Create and manage ocean shipment bookings.
  name: Maersk Bookings API
  slug: maersk-line-bookings-api
- baseURL: https://api.productmanagement.maersk.com
  baseurl_source: spec
  description: Supported container size and type combinations.
  name: Maersk Containers API
  slug: maersk-line-containers-api
- baseURL: https://api.maersk.com
  baseurl_source: spec
  description: Demurrage and detention charges and clocks.
  name: Maersk DemurrageDetention API
  slug: maersk-line-demurragedetention-api
- baseURL: https://api.productmanagement.maersk.com
  baseurl_source: spec
  description: Origin and destination port lookups.
  name: Maersk Locations API
  slug: maersk-line-locations-api
- baseURL: https://api.productmanagement.maersk.com
  baseurl_source: spec
  description: Product offers, prices, and surcharges.
  name: Maersk Offers API
  slug: maersk-line-offers-api
- baseURL: https://api.maersk.com
  baseurl_source: spec
  description: Sailing schedules and vessel routings.
  name: Maersk Schedules API
  slug: maersk-line-schedules-api
- baseURL: https://api.maersk.com
  baseurl_source: spec
  description: Container and shipment tracking events.
  name: Maersk Tracking API
  slug: maersk-line-tracking-api
- baseURL: https://api.maersk.com
  baseurl_source: spec
  description: Verified Gross Mass declarations.
  name: Maersk VGM API
  slug: maersk-line-vgm-api
- baseURL: https://api.maersk.com
  baseurl_source: spec
  description: Electronic bill of lading lifecycle.
  name: Maersk Bill of Lading API
  slug: maersk-line-bill-of-lading-api
artifact_total: 80
collections:
- collection_type: open
  name: Maersk Air Booking API
  slug: open-maersk-air-booking-api
- collection_type: open
  name: Maersk Bill of Lading API
  slug: open-maersk-bill-of-lading-api
- collection_type: open
  name: Maersk Import Demurrage and Detention API
  slug: open-maersk-demurrage-detention-api
- collection_type: open
  name: Maersk Air Booking AirBookings API
  slug: open-maersk-line-airbookings-api
- collection_type: open
  name: Maersk Air Booking AirBookings BillOfLading API
  slug: open-maersk-line-billoflading-api
- collection_type: open
  name: Maersk Air Booking AirBookings Bookings API
  slug: open-maersk-line-bookings-api
- collection_type: open
  name: Maersk Air Booking AirBookings Containers API
  slug: open-maersk-line-containers-api
- collection_type: open
  name: Maersk Air Booking AirBookings DemurrageDetention API
  slug: open-maersk-line-demurragedetention-api
- collection_type: open
  name: Maersk Air Booking AirBookings Locations API
  slug: open-maersk-line-locations-api
- collection_type: open
  name: Maersk Air Booking AirBookings Offers API
  slug: open-maersk-line-offers-api
- collection_type: open
  name: Maersk Air Booking AirBookings Schedules API
  slug: open-maersk-line-schedules-api
- collection_type: open
  name: Maersk Air Booking AirBookings Tracking API
  slug: open-maersk-line-tracking-api
- collection_type: open
  name: Maersk Air Booking AirBookings VGM API
  slug: open-maersk-line-vgm-api
- collection_type: open
  name: Maersk Ocean Booking API
  slug: open-maersk-ocean-booking-api
- collection_type: open
  name: Maersk Product Offers API
  slug: open-maersk-product-offers-api
- collection_type: open
  name: Maersk Schedules API
  slug: open-maersk-schedules-api
- collection_type: open
  name: Maersk Track and Trace API
  slug: open-maersk-track-and-trace-api
- collection_type: open
  name: Maersk Verified Gross Mass API
  slug: open-maersk-vgm-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/maersk/overview
- group: company
  title: ''
  type: Website
  url: https://www.maersk.com/
- group: other
  href: https://artifacts.apis.io/maersk-line/capabilities/maersk-line-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/maersk-line-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/maersk-line/agentic-access/maersk-line-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/maersk-line-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/maersk-line/security/maersk-line-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/maersk-line-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/maersk-line/security/maersk-line-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maersk-line-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/maersk-line/authentication/maersk-line-authentication.yml
  title: ''
  type: Authentication
  url: authentication/maersk-line-authentication.yml
- group: auth
  href: https://artifacts.apis.io/maersk-line/scopes/maersk-line-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/maersk-line-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.maersk.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.maersk.com/api-catalogue
- group: operate
  title: ''
  type: Support
  url: https://developer.maersk.com/support/:tabName
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.maersk.com/support/getting-started-api
- group: auth
  title: ''
  type: Authentication
  url: https://developer.maersk.com/support/authorisation
- group: operate
  title: ''
  type: FAQ
  url: https://developer.maersk.com/support/faqs
- group: docs
  title: ''
  type: Documentation
  url: https://www.maersk.com/digital-services/data-integrations/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.maersk.com/digital-services/data-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://www.maersk.com/digital-services/data-integrations/solutions
- group: start
  title: ''
  type: Portal
  url: https://www.maersk.com
- group: company
  title: ''
  type: About
  url: https://www.maersk.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.maersk.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.maersk.com/insights
- group: docs
  title: ''
  type: Documentation
  url: https://www.maersk.com/local-information
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.maersk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maersk.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://www.maersk.com/career
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maersk-group
- group: other
  title: ''
  type: X
  url: https://twitter.com/Maersk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/MAERSK
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Maersk-Global
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MaerskTech
- group: other
  title: ''
  type: Standards
  url: https://dcsa.org
- group: docs
  title: ''
  type: Specification
  url: https://github.com/dcsaorg/DCSA-OpenAPI
- group: design
  href: https://artifacts.apis.io/maersk-line/rules/maersk-rules.yml
  title: ''
  type: SpectralRules
  url: rules/maersk-rules.yml
- group: design
  href: https://artifacts.apis.io/maersk-line/vocabulary/maersk-line-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/maersk-line-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/maersk-line/json-ld/maersk-line-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/maersk-line-context.jsonld
- group: commercial
  href: https://artifacts.apis.io/maersk-line/plans/maersk-line-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/maersk-line-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/maersk-line/rate-limits/maersk-line-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/maersk-line-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/maersk-line/finops/maersk-line-finops.yml
  title: ''
  type: FinOps
  url: finops/maersk-line-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: https://developer.maersk.com/support/authorisation
created: '2026-05-25'
description: A.P. Moller - Maersk is the Danish integrated container shipping and logistics company. Maersk operates one of the world's largest ocean fleets and a global network of warehouses, inland transport, customs services, and air-freight capacity through Maersk Air Cargo. The Maersk Developer Portal exposes a catalogue of APIs for Track and Trace, Ocean Booking (DCSA-aligned), Schedules, Product Offers and pricing, electronic Bills of Lading, Verified Gross Mass, Demurrage and Detention, Air Booking, VGM, and container Maintenance and Repair. Many of Maersk's APIs implement Digital Container Shipping Association (DCSA) interface standards so the same client can address multiple carriers.
examples:
- key_count: 9
  name: Maersk Booking Request Example
  slug: maersk-booking-request-example
- key_count: 11
  name: Maersk Product Offer Example
  slug: maersk-product-offer-example
- key_count: 3
  name: Maersk Tracking Shipment Example
  slug: maersk-tracking-shipment-example
- key_count: 2
  name: Maersk Vgm Submission Example
  slug: maersk-vgm-submission-example
features:
- description: Public Track and Trace API with neutralized container and shipment events.
  name: Container Tracking
- description: Create, retrieve, amend, and cancel bookings via the DCSA Booking 2.0 interface.
  name: Ocean Booking (DCSA)
- description: Point-to-point and commercial service schedules across the Maersk ocean network.
  name: Sailing Schedules
- description: Quote all-in ocean rates including base freight and surcharges.
  name: Product Offers and Pricing
- description: Issue and approve eBLs per the DCSA eBL 3.0 standard.
  name: Electronic Bills of Lading
- description: Submit SOLAS-mandated container weight declarations electronically.
  name: Verified Gross Mass (VGM)
- description: Surface accruing accessorial charges and remaining free-day clocks.
  name: Demurrage and Detention Visibility
- description: Book air freight via Maersk Air Cargo with product tiers including Pharma and Perishable.
  name: Air Cargo Bookings
- description: Surface equipment-management events and M&R workflow data.
  name: Container Maintenance and Repair
- description: APIs implement DCSA interface standards for portability across carriers.
  name: DCSA Alignment
- description: Client-credentials OAuth tokens layered over per-app Consumer-Key authentication.
  name: OAuth 2.0 with Consumer Keys
- description: Asynchronous push notifications for booking lifecycle events.
  name: Booking Status Webhooks
finops:
- has_sources: true
  method: generated
  name: Maersk Line Finops
  primary_unit: ''
  service_category: Logistics and Shipping
  slug: maersk-line-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maersk-line.png
integrations:
- description: Many Maersk customers integrate Maersk APIs with SAP TM.
  name: SAP Transportation Management
- description: OTM connectors consume Maersk shipment and booking events.
  name: Oracle Transportation Management
- description: Supply-chain planning platforms ingest tracking and schedule data.
  name: Blue Yonder
- description: Multi-carrier visibility platforms aggregate Maersk Track and Trace.
  name: project44
- description: Real-time supply-chain visibility platforms relay container milestones.
  name: FourKites
- description: Founding member; Maersk APIs implement DCSA Booking, Schedules, eBL, and Track and Trace interfaces.
  name: DCSA
- description: Legacy IFTSAI, IFTSTA, IFTMBF, and BAPLIE EDI flows interoperate with the API surface.
  name: EDI
json_schemas:
- name: Maersk Ocean Booking
  property_count: 10
  slug: maersk-booking
- name: Maersk Product Offer
  property_count: 11
  slug: maersk-product-offer
- name: Maersk Shipment
  property_count: 8
  slug: maersk-shipment
jsonld:
- class_count: 0
  name: Maersk Line Context
  property_count: 6
  slug: maersk-line-context
layout: provider
modified: '2026-05-25'
name: Maersk
nav: Providers
network: true
overview: 'Maersk publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including AirBookings API, Bookings API, Containers API, and 8 more. Tagged areas include Shipping, Logistics, Container Shipping, Ocean Freight, and Air Freight.


  The Maersk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Maersk''s developer surface includes authentication, developer portal, documentation, support, getting-started guide, FAQ, engineering blog, and 32 more developer resources.'
plans:
- name: Maersk Line Plans Pricing
  plan_count: 5
  slug: maersk-line-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Maersk Line Rate Limits
  slug: maersk-line-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Maersk — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: maersk-line-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Maersk — maersk rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 2
  slug: maersk-rules
scopes:
- name: Maersk Line Scopes
  scope_count: 4
  slug: maersk-line-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 0.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 27.3
    contract_quality: 65.5
    developer_ergonomics: 39.3
    discoverability: 62.5
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - denmark
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 70.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/maersk-line/maersk-line-2026-06-20T184832.png
security:
- kind: authentication
  name: Maersk Line Authentication
  slug: maersk-line-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Maersk Line Domain Security
  slug: maersk-line-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Maersk Line Vulnerability Disclosure
  slug: maersk-line-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: maersk-line
solutions:
- description: Container shipping across Maersk's global vessel network.
  name: Ocean Transport
- description: Maersk Air Cargo for time-sensitive shipments.
  name: Air Freight
- description: Global warehouse network with API-enabled inventory and outbound data.
  name: Warehousing and Distribution
- description: Managed end-to-end logistics with integrated transport, warehousing, customs, and finance.
  name: Supply Chain Management
- description: Customs brokerage and clearance integrated with shipment data.
  name: Customs Services
- description: Truck, rail, and barge transport for first- and last-mile movements.
  name: Inland Transport
- description: Reefer and pharma-grade transport for temperature-sensitive cargo.
  name: Cold Chain
- description: Break-bulk and out-of-gauge cargo for industrial projects.
  name: Project Logistics
tags:
- Shipping
- Logistics
- Container Shipping
- Ocean Freight
- Air Freight
- Supply Chain
- DCSA
- Maritime
- Freight
use_cases:
- description: Pipe container milestones into TMS and OMS platforms to give merchandisers, planners, and customers real-time shipment status.
  name: Supply Chain Visibility
- description: Embed real-time ocean and air quotes into freight-forwarder portals and marketplace platforms.
  name: Self-Service Quoting
- description: Trigger DCSA-compliant bookings from ERP procurement events and route them through Maersk's network.
  name: Automated Booking
- description: Programmatic VGM submission and eBL approvals eliminate manual filings.
  name: Compliance Automation
- description: Monitor D&D clocks across import containers and trigger dispatch workflows before free days expire.
  name: Penalty Avoidance
- description: Reconcile expected surcharges and accessorial charges against invoices using Product Offers and D&D data.
  name: Rate Audit and FinOps
website: https://www.maersk.com/
---
