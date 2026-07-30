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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: United States Postal Service Agentic Access
  operation_count: 12
  slug: united-states-postal-service-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 12
apis:
- description: Provides pricing for international USPS products based on shipment characteristics including destination country, weight, dimensions, and service class.
  name: USPS International Prices API
  slug: usps-international-prices-api
- description: Creates domestic shipping labels with barcodes in multiple formats and generates Shipping Services Files. Requires USPS Ship enrollment and Enterprise Payment Account.
  name: USPS Domestic Labels API
  slug: usps-domestic-labels-api
- description: Creates international shipping labels and generates required Shipping Services Files for customs compliance.
  name: USPS International Labels API
  slug: usps-international-labels-api
- description: Identifies drop-off facilities and destination entry points for various USPS services. Supports post office locator and drop-off location finder.
  name: USPS Locations API
  slug: usps-locations-api
- description: Provides delivery benchmarks showing expected transit times between origin and destination ZIP Codes for USPS mail classes.
  name: USPS Service Standards API
  slug: usps-service-standards-api
- description: Returns a comprehensive list of pricing, service standards, and shipping options for USPS products in a single API call, eliminating the need to query multiple APIs separately.
  name: USPS Shipping Options API
  slug: usps-shipping-options-api
- description: Links multiple domestic and international labels through a single electronic file number, creating Shipment Confirmation Acceptance Notice forms for batch shipping operations.
  name: USPS SCAN Forms API
  slug: usps-scan-forms-api
- description: Industry-standard OAuth 2.0 Client Credentials authentication protecting access to all USPS APIs. Returns Bearer Tokens used in the Authorization header for all USPS API calls.
  name: USPS OAuth API
  slug: usps-oauth-api
- description: Address validation and standardization operations
  name: United States Postal Service Addresses API
  slug: united-states-postal-service-addresses-api
- description: Schedule and manage USPS carrier pickup requests
  name: United States Postal Service Carrier Pickup API
  slug: united-states-postal-service-carrier-pickup-api
- description: Domestic postage pricing and rate calculation operations
  name: United States Postal Service Domestic Prices API
  slug: united-states-postal-service-domestic-prices-api
- description: Package tracking status and event operations
  name: United States Postal Service Tracking API
  slug: united-states-postal-service-tracking-api
artifact_total: 104
collections:
- collection_type: open
  name: USPS Addresses API
  slug: open-united-states-postal-service-addresses
- collection_type: open
  name: USPS Carrier Pickup API
  slug: open-united-states-postal-service-carrier-pickup
- collection_type: open
  name: USPS Domestic Prices API
  slug: open-united-states-postal-service-domestic-prices
- collection_type: open
  name: USPS Tracking API
  slug: open-united-states-postal-service-tracking
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-postal-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-postal-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-states-postal-service-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usps
- group: start
  title: ''
  type: Portal
  url: https://developers.usps.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.usps.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.usps.com/apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.usps.com/terms-and-conditions
- group: operate
  title: ''
  type: FAQ
  url: https://developers.usps.com/faq
- group: operate
  title: ''
  type: Support
  url: https://emailus.usps.com/s/web-tools-inquiry
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/USPS
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/USPS/api-examples
- group: design
  title: ''
  type: SpectralRules
  url: rules/united-states-postal-service-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/united-states-postal-service-vocabulary.yaml
created: 2024/01/01
description: The United States Postal Service (USPS) provides a modern REST API platform at developers.usps.com that gives ecommerce websites, shipping software, and logistics systems access to postal data and services. APIs cover address validation, package tracking, domestic and international shipping labels, pricing, carrier pickup scheduling, location finding, and Informed Delivery campaign management. The legacy Web Tools platform was retired January 25, 2026, with all functionality migrated to the new OAuth 2.0-secured API platform.
examples:
- key_count: 16
  name: Addresses Address Example
  slug: addresses-address-example
- key_count: 3
  name: Addresses City State Example
  slug: addresses-city-state-example
- key_count: 5
  name: Addresses Zip Code Result Example
  slug: addresses-zip-code-result-example
- key_count: 5
  name: Carrier Pickup Pickup Address Example
  slug: carrier-pickup-pickup-address-example
- key_count: 2
  name: Carrier Pickup Pickup Package Example
  slug: carrier-pickup-pickup-package-example
- key_count: 6
  name: Carrier Pickup Pickup Request Example
  slug: carrier-pickup-pickup-request-example
- key_count: 4
  name: Carrier Pickup Pickup Response Example
  slug: carrier-pickup-pickup-response-example
- key_count: 4
  name: Carrier Pickup Pickup Update Request Example
  slug: carrier-pickup-pickup-update-request-example
- key_count: 10
  name: Domestic Prices Base Rate Request Example
  slug: domestic-prices-base-rate-request-example
- key_count: 5
  name: Domestic Prices Extra Service Rate Request Example
  slug: domestic-prices-extra-service-rate-request-example
- key_count: 1
  name: Domestic Prices Extra Service Rate Response Example
  slug: domestic-prices-extra-service-rate-response-example
- key_count: 1
  name: Domestic Prices Rate Response Example
  slug: domestic-prices-rate-response-example
- key_count: 8
  name: Domestic Prices Total Rate Request Example
  slug: domestic-prices-total-rate-request-example
- key_count: 1
  name: Domestic Prices Total Rate Response Example
  slug: domestic-prices-total-rate-response-example
- key_count: 1
  name: Tracking Multiple Tracking Request Example
  slug: tracking-multiple-tracking-request-example
- key_count: 1
  name: Tracking Multiple Tracking Result Example
  slug: tracking-multiple-tracking-result-example
- key_count: 11
  name: Tracking Tracking Event Example
  slug: tracking-tracking-event-example
- key_count: 2
  name: Tracking Tracking Result Example
  slug: tracking-tracking-result-example
features:
- description: Secure API access using industry-standard OAuth 2.0 Client Credentials flow with Bearer Token authentication.
  name: OAuth 2.0 Authentication
- description: All APIs follow RESTful conventions with JSON request and response bodies.
  name: RESTful Architecture
- description: Testing Environment for Mailers (TEM) at apis-tem.usps.com for safe API testing before going to production.
  name: Sandbox Testing Environment
- description: USPS Coding Accuracy Support System (CASS) compliant address validation and standardization.
  name: Address Standardization
- description: DPV confirmation codes ensure packages can be delivered to the validated address.
  name: Delivery Point Validation
- description: Live package tracking with scan events, timestamps, and location details from USPS systems.
  name: Real-Time Tracking
- description: Event-driven subscription APIs for tracking events, adjustments, and disputes delivered via webhooks.
  name: Webhook Subscriptions
- description: Support for bulk operations including multiple tracking lookups and SCAN Form generation.
  name: Batch Processing
finops:
- name: United States Postal Service Finops
  service_category: Postal / Shipping
  slug: united-states-postal-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-postal-service.png
integrations:
- description: USPS shipping integration available through Shopify Shipping for label generation and rate calculation.
  name: Shopify
- description: WooCommerce shipping plugins integrate USPS APIs for rate calculation and label printing.
  name: WooCommerce
- description: Adobe Commerce and Magento integrate USPS for shipping rate display and fulfillment.
  name: Magento
- description: ShipStation multi-carrier shipping platform integrates USPS APIs for ecommerce fulfillment.
  name: ShipStation
- description: EasyPost shipping API aggregator provides access to USPS services alongside other carriers.
  name: EasyPost
- description: Stamps.com and Pitney Bowes shipping platforms integrate USPS APIs for postage and label printing.
  name: Stamps.com
json_schemas:
- name: Address
  property_count: 16
  slug: addresses-address
- name: CityState
  property_count: 3
  slug: addresses-city-state
- name: ZIPCodeResult
  property_count: 5
  slug: addresses-zip-code-result
- name: PickupAddress
  property_count: 5
  slug: carrier-pickup-pickup-address
- name: PickupPackage
  property_count: 2
  slug: carrier-pickup-pickup-package
- name: PickupRequest
  property_count: 6
  slug: carrier-pickup-pickup-request
- name: PickupResponse
  property_count: 4
  slug: carrier-pickup-pickup-response
- name: PickupUpdateRequest
  property_count: 4
  slug: carrier-pickup-pickup-update-request
- name: BaseRateRequest
  property_count: 10
  slug: domestic-prices-base-rate-request
- name: ExtraServiceRateRequest
  property_count: 5
  slug: domestic-prices-extra-service-rate-request
- name: ExtraServiceRateResponse
  property_count: 1
  slug: domestic-prices-extra-service-rate-response
- name: RateResponse
  property_count: 1
  slug: domestic-prices-rate-response
- name: TotalRateRequest
  property_count: 8
  slug: domestic-prices-total-rate-request
- name: TotalRateResponse
  property_count: 1
  slug: domestic-prices-total-rate-response
- name: MultipleTrackingRequest
  property_count: 1
  slug: tracking-multiple-tracking-request
- name: MultipleTrackingResult
  property_count: 1
  slug: tracking-multiple-tracking-result
- name: TrackingEvent
  property_count: 11
  slug: tracking-tracking-event
- name: TrackingResult
  property_count: 2
  slug: tracking-tracking-result
json_structures:
- name: Addresses Address Structure
  property_count: 16
  slug: addresses-address-structure
- name: Addresses City State Structure
  property_count: 3
  slug: addresses-city-state-structure
- name: Addresses Zip Code Result Structure
  property_count: 5
  slug: addresses-zip-code-result-structure
- name: Carrier Pickup Pickup Address Structure
  property_count: 5
  slug: carrier-pickup-pickup-address-structure
- name: Carrier Pickup Pickup Package Structure
  property_count: 2
  slug: carrier-pickup-pickup-package-structure
- name: Carrier Pickup Pickup Request Structure
  property_count: 6
  slug: carrier-pickup-pickup-request-structure
- name: Carrier Pickup Pickup Response Structure
  property_count: 4
  slug: carrier-pickup-pickup-response-structure
- name: Carrier Pickup Pickup Update Request Structure
  property_count: 4
  slug: carrier-pickup-pickup-update-request-structure
- name: Domestic Prices Base Rate Request Structure
  property_count: 10
  slug: domestic-prices-base-rate-request-structure
- name: Domestic Prices Extra Service Rate Request Structure
  property_count: 5
  slug: domestic-prices-extra-service-rate-request-structure
- name: Domestic Prices Extra Service Rate Response Structure
  property_count: 1
  slug: domestic-prices-extra-service-rate-response-structure
- name: Domestic Prices Rate Response Structure
  property_count: 1
  slug: domestic-prices-rate-response-structure
- name: Domestic Prices Total Rate Request Structure
  property_count: 8
  slug: domestic-prices-total-rate-request-structure
- name: Domestic Prices Total Rate Response Structure
  property_count: 1
  slug: domestic-prices-total-rate-response-structure
- name: Tracking Multiple Tracking Request Structure
  property_count: 1
  slug: tracking-multiple-tracking-request-structure
- name: Tracking Multiple Tracking Result Structure
  property_count: 1
  slug: tracking-multiple-tracking-result-structure
- name: Tracking Tracking Event Structure
  property_count: 11
  slug: tracking-tracking-event-structure
- name: Tracking Tracking Result Structure
  property_count: 2
  slug: tracking-tracking-result-structure
jsonld:
- class_count: 3
  name: United States Postal Service Addresses Context
  property_count: 16
  slug: united-states-postal-service-addresses-context
- class_count: 5
  name: United States Postal Service Carrier Context
  property_count: 17
  slug: united-states-postal-service-carrier-context
- class_count: 8
  name: United States Postal Service Domestic Context
  property_count: 19
  slug: united-states-postal-service-domestic-context
- class_count: 4
  name: United States Postal Service Tracking Context
  property_count: 18
  slug: united-states-postal-service-tracking-context
layout: provider
modified: '2026-05-19'
name: United States Postal Service
nav: Providers
network: true
overview: 'United States Postal Service publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Carrier Pickup API, Domestic Prices API, and 1 more. Tagged areas include Government, Postal Service, Shipping, Logistics, and Address Validation.


  The United States Postal Service catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  United States Postal Service''s developer surface includes authentication, developer portal, getting-started guide, documentation, FAQ, support, and 8 more developer resources.'
plans:
- name: United States Postal Service Plans Pricing
  plan_count: 2
  slug: united-states-postal-service-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 2
  name: United States Postal Service Rate Limits
  slug: united-states-postal-service-rate-limits
rules:
- name: United States Postal Service API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-postal-service-jsonschema-spectral-rules
- name: United States Postal Service API Rules
  rule_count: 39
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 23
  slug: united-states-postal-service-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: -7.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.3
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-postal-service/refs/heads/main/screenshots/united-states-postal-service-2026-06-20T200056.png
security:
- kind: authentication
  name: United States Postal Service Authentication
  slug: united-states-postal-service-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: United States Postal Service Domain Security
  slug: united-states-postal-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: united-states-postal-service
tags:
- Government
- Postal Service
- Shipping
- Logistics
- Address Validation
- Package Tracking
use_cases:
- description: Calculate shipping rates, generate labels, and provide package tracking directly within e-commerce checkout flows.
  name: E-Commerce Shipping Integration
- description: Validate and standardize customer addresses during checkout to reduce failed deliveries and return rates.
  name: Address Verification at Checkout
- description: Programmatically create domestic and international USPS shipping labels with barcodes for fulfillment operations.
  name: Shipping Label Generation
- description: Schedule and manage USPS carrier pickups automatically based on order fulfillment triggers.
  name: Carrier Pickup Automation
- description: Compare USPS service options and pricing to select the most cost-effective shipping method.
  name: Logistics Rate Shopping
- description: Display accurate expected delivery dates to customers using USPS service standards data.
  name: Delivery Time Estimation
- description: Help customers locate the nearest USPS facility for drop-offs or in-person services.
  name: Post Office Finder
- description: Enhance customer engagement by adding digital content to mail pieces viewed through Informed Delivery.
  name: Informed Delivery Campaigns
website: https://developers.usps.com/
---
