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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Maersk Line Agentic Access
  operation_count: 20
  slug: maersk-line-agentic-access
  summary_line: 20 operations · 6 acting
api_count: 11
apis:
- description: Container Maintenance and Repair (M&R) API surfacing equipment-management events and repair workflow data for Maersk container assets.
  name: Maersk Container Maintenance and Repair API
  slug: maersk-container-maintenance-repair-api
- description: Air freight bookings.
  name: Maersk AirBookings API
  slug: maersk-line-airbookings-api
- description: Electronic bill of lading lifecycle.
  name: Maersk BillOfLading API
  slug: maersk-line-billoflading-api
- description: Create and manage ocean shipment bookings.
  name: Maersk Bookings API
  slug: maersk-line-bookings-api
- description: Supported container size and type combinations.
  name: Maersk Containers API
  slug: maersk-line-containers-api
- description: Demurrage and detention charges and clocks.
  name: Maersk DemurrageDetention API
  slug: maersk-line-demurragedetention-api
- description: Origin and destination port lookups.
  name: Maersk Locations API
  slug: maersk-line-locations-api
- description: Product offers, prices, and surcharges.
  name: Maersk Offers API
  slug: maersk-line-offers-api
- description: Sailing schedules and vessel routings.
  name: Maersk Schedules API
  slug: maersk-line-schedules-api
- description: Container and shipment tracking events.
  name: Maersk Tracking API
  slug: maersk-line-tracking-api
- description: Verified Gross Mass declarations.
  name: Maersk VGM API
  slug: maersk-line-vgm-api
artifact_total: 81
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maersk-line-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maersk-line-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maersk-line-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maersk-line-authentication.yml
- group: auth
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
  title: ''
  type: SpectralRules
  url: rules/maersk-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/maersk-line-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/maersk-line-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/maersk-line-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maersk-line-rate-limits.yml
- group: commercial
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
- name: Maersk Line Finops
  service_category: Logistics and Shipping
  slug: maersk-line-finops
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
overview: 'Maersk publishes 10 APIs on the [APIs.io](https://apis.io/) network, including AirBookings API, BillOfLading API, Bookings API, and 7 more. Tagged areas include Shipping, Logistics, Container Shipping, Ocean Freight, and Air Freight.


  The Maersk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Maersk''s developer surface includes authentication, developer portal, documentation, support, getting-started guide, FAQ, engineering blog, and 29 more developer resources.'
plans:
- name: Maersk Line Plans Pricing
  plan_count: 5
  slug: maersk-line-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Maersk Line Rate Limits
  slug: maersk-line-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Maersk API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: maersk-line-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Maersk API Rules
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
  composite: 48.2
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 28.8
    contract_quality: 71.3
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maersk-line/refs/heads/main/screenshots/maersk-line-2026-06-20T184832.png
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
website: https://developer.maersk.com
---
