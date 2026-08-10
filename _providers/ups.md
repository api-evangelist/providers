---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Ups Agentic Access
  operation_count: 11
  slug: ups-agentic-access
  summary_line: 11 operations · 10 acting
api_count: 8
apis:
- description: Address validation and standardization
  name: UPS Address Validation API
  slug: ups-address-validation-api
- description: OAuth 2.0 token management
  name: UPS OAuth API
  slug: ups-oauth-api
- description: International paperless document management
  name: UPS Paperless Documents API
  slug: ups-paperless-documents-api
- description: Pickup scheduling and management
  name: UPS Pickup API
  slug: ups-pickup-api
- description: Shipping rates and service comparison
  name: UPS Rating API
  slug: ups-rating-api
- description: Shipment creation and label generation
  name: UPS Shipping API
  slug: ups-shipping-api
- description: Transit time and service schedules
  name: UPS Time In Transit API
  slug: ups-time-in-transit-api
- description: Package tracking and status
  name: UPS Tracking API
  slug: ups-tracking-api
artifact_total: 49
collections:
- collection_type: open
  name: UPS Shipping API
  slug: open-ups-shipping
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ups-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ups-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ups-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ups-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ups
- group: company
  title: ''
  type: Website
  url: https://www.ups.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ups.com
- group: other
  title: ''
  type: API Catalog
  url: https://developer.ups.com/catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ups.com/get-started
created: '2025-03-01'
description: UPS, or United Parcel Service, is a Fortune 500 global logistics company that specializes in package delivery and supply chain management services. UPS provides a comprehensive REST API platform with OAuth 2.0 authentication covering shipping, tracking, rating, address validation, pickup scheduling, paperless international documents, and time-in-transit estimation.
examples:
- key_count: 2
  name: Ups Shop Rates Example
  slug: ups-shop-rates-example
- key_count: 2
  name: Ups Track Shipment Example
  slug: ups-track-shipment-example
features:
- 'UPS: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- UPS Developer Kit APIs (Shipping, Tracking, Rating, Address Validation) require account; shipping rates per package/zone.
finops:
- name: Ups Finops
  service_category: Logistics / Shipping
  slug: ups-finops
graphqls:
- description: This GraphQL schema represents the UPS Developer Kit REST API surface — covering shipping, tracking, rating, address validation, pickup scheduling, and related logistics operations. UPS exposes its ca
  name: UPS GraphQL Schema
  slug: ups-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ups.png
json_schemas:
- name: Address
  property_count: 6
  slug: ups-address
- name: AddressValidationRequest
  property_count: 1
  slug: ups-addressvalidationrequest
- name: AddressValidationResponse
  property_count: 1
  slug: ups-addressvalidationresponse
- name: CancelPickupResponse
  property_count: 1
  slug: ups-cancelpickupresponse
- name: ErrorResponse
  property_count: 1
  slug: ups-errorresponse
- name: OAuthTokenResponse
  property_count: 6
  slug: ups-oauthtokenresponse
- name: PackageInfo
  property_count: 3
  slug: ups-packageinfo
- name: PaperlessDocumentRequest
  property_count: 1
  slug: ups-paperlessdocumentrequest
- name: PaperlessDocumentResponse
  property_count: 1
  slug: ups-paperlessdocumentresponse
- name: PickupRequest
  property_count: 1
  slug: ups-pickuprequest
- name: PickupResponse
  property_count: 1
  slug: ups-pickupresponse
- name: RateRequest
  property_count: 1
  slug: ups-raterequest
- name: RateResponse
  property_count: 1
  slug: ups-rateresponse
- name: ServiceCode
  property_count: 2
  slug: ups-servicecode
- name: UPS Shipment
  property_count: 7
  slug: ups-shipment
- name: ShipmentRequest
  property_count: 1
  slug: ups-shipmentrequest
- name: ShipmentResponse
  property_count: 1
  slug: ups-shipmentresponse
- name: ShipperInfo
  property_count: 5
  slug: ups-shipperinfo
- name: TimeInTransitRequest
  property_count: 13
  slug: ups-timeintransitrequest
- name: TimeInTransitResponse
  property_count: 3
  slug: ups-timeintransitresponse
- name: TrackResponse
  property_count: 1
  slug: ups-trackresponse
- name: VoidResponse
  property_count: 1
  slug: ups-voidresponse
json_structures:
- name: Ups Shipment Structure
  property_count: 0
  slug: ups-shipment-structure
- name: Ups Structure
  property_count: 0
  slug: ups-structure
jsonld:
- class_count: 4
  name: Ups Context
  property_count: 17
  slug: ups-context
layout: provider
modified: '2026-05-19'
name: UPS
nav: Providers
network: true
overview: 'UPS publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Address Validation API, OAuth API, Paperless Documents API, and 5 more. Tagged areas include Logistics, Shipping, Fortune 500, and Supply Chain.


  The UPS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UPS''s developer surface includes authentication, getting-started guide, and 7 more developer resources.'
plans:
- name: Ups Plans Pricing
  plan_count: 1
  slug: ups-plans-pricing
press:
- date: '2026-05-25'
  title: The Brilliant Ways UPS Uses Artificial Intelligence ...
  url: https://www.cbcommerce.eu/blog/2018/07/20/the-brilliant-ways-ups-uses-artificial-intelligence-machine-learning-and-big-data/?srsltid=AfmBOorrQQp7X1xM0zzx_HDJ98Vlb7BOUbH4JecNh0VQSBdOodiJ7iSI
- date: '2026-05-25'
  title: UPS Uses Artificial Intelligence For Pricing
  url: https://www.forbes.com/sites/stevebanker/2025/04/21/ups-uses-artificial-intelligence-for-pricing/
- date: '2026-05-25'
  title: UPS is improving careers and access to opportunity with ...
  url: https://about.ups.com/us/en/our-stories/innovation-driven/ups-is-improving-careers-and-access-to-opportunity-with-the-help.html
- date: '2026-05-25'
  title: UPS is teaming up with artificial intelligence to try and ...
  url: https://www.facebook.com/12news/posts/ups-is-teaming-up-with-artificial-intelligence-to-try-and-reduce-delivery-theft-/717383273756399/
- date: '2026-05-25'
  title: How UPS is using AI, from shipper pricing to customs ...
  url: https://www.supplychaindive.com/news/ups-ai-employee-upskilling-network-changes/816412/
random_paper: 112
rate_limits:
- limit_count: 1
  name: Ups Rate Limits
  slug: ups-rate-limits
rules:
- name: UPS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ups-jsonschema-spectral-rules
- name: UPS API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: ups-rules
scopes:
- name: Ups Scopes
  scope_count: 0
  slug: ups-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.9
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ups/refs/heads/main/screenshots/ups-2026-06-20T200507.png
security:
- kind: authentication
  name: Ups Authentication
  slug: ups-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ups Domain Security
  slug: ups-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ups
tags:
- Logistics
- Shipping
- Fortune 500
- Supply Chain
website: https://www.ups.com
---
