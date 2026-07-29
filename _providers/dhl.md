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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dhl Agentic Access
  operation_count: 4
  slug: dhl-agentic-access
  summary_line: 4 operations
api_count: 51
apis:
- description: Provides shipment status access across DHL Freight, DHL eCommerce, DHL Supply Chain, DHL Global Forwarding, and Post and Parcel Germany through a single unified tracking interface.
  name: Shipment Tracking Unified
  slug: shipment-tracking-unified
- description: Push-based variant of the Shipment Tracking Unified API that proactively sends updates on shipment status to subscribed consumers across DHL divisions.
  name: Shipment Tracking Unified Push
  slug: shipment-tracking-unified-push
- description: One-stop solution for shipping products including duty and tax calculations, shipping labels, manifests, and tracking for DHL eCommerce Americas customers.
  name: User Guide DHL eCommerce Americas
  slug: user-guide-dhl-ecommerce-americas
- description: Validates which additional services combine with DHL Freight products for European palletized road freight transport.
  name: Additional Services DHL Freight
  slug: additional-services-dhl-freight
- description: Access token generation endpoint for authenticating against DHL eCommerce Americas services.
  name: Authentication DHL eCommerce Americas
  slug: authentication-dhl-ecommerce-americas
- description: Provides authentication services for DHL Group freight operations across European road freight products.
  name: Authentication API DHL Freight
  slug: authentication-api-dhl-freight
- description: Authentication for business customers of Deutsche Post and Parcel Germany services.
  name: Authentication API Post Parcel Germany
  slug: authentication-api-post-parcel-germany
- description: Documents product updates, features, enhancements, and bug fixes for DHL eCommerce Americas APIs.
  name: Changelog DHL eCommerce Americas
  slug: changelog-dhl-ecommerce-americas
- description: Automatic postal data completion service for streamlined address entry across Post and Parcel Germany products.
  name: DATAFACTORY AUTOCOMPLETE 2.0
  slug: datafactory-autocomplete-20-post-parcel-germany
- description: Allows business customers to send PDF documents as physical mail shipments via Deutsche Post with tracking.
  name: Deutsche Post Hybrid Mail Shipments E-POST
  slug: deutsche-post-hybrid-mail-shipments-e-post-post-parcel-germany
- description: Creates labels for international mail, lightweight items, and merchandise shipments via Deutsche Post.
  name: Deutsche Post International
  slug: deutsche-post-international-post-parcel-germany
- description: Provides online postage purchase for domestic and international mail products from Deutsche Post.
  name: Deutsche Post INTERNETMARKE
  slug: deutsche-post-internetmarke-post-parcel-germany
- description: Electronic order management for Deutsche Post commercial and logistics processes.
  name: Deutsche Post Order Management AM
  slug: deutsche-post-order-management-am-post-parcel-germany
- description: Manages dialogue marketing print mailings including pricing, documents, and franking workflows.
  name: Deutsche Post Print-Mailing Dispatch Preparation
  slug: deutsche-post-print-mailing-dispatch-preparation-post-parcel-germany
- description: Plans dialogue marketing campaigns with target groups and recipient data for print mailings.
  name: Deutsche Post Print-Mailing Targeting
  slug: deutsche-post-print-mailing-targeting-post-parcel-germany
- description: Enables cross-border European shipments including Parcel Connect and return services across DHL eCommerce Europe.
  name: DHL eCommerce Europe eConnect
  slug: ecommerce-europe-econnect
- description: Beta features documentation for enhanced eCommerce European shipping capabilities ahead of general availability.
  name: DHL eCommerce Europe eConnect Beta
  slug: ecommerce-europe-econnect-beta
- description: Place pickup orders and query pickup locations and status details for DHL Parcel Germany.
  name: DHL Parcel DE Pickup
  slug: dhl-parcel-de-pickup
- description: Validates postnumbers to ensure deliverability of shipments to Deutsche Post and DHL parcel lockers.
  name: DHL Parcel DE Postnumber
  slug: dhl-parcel-de-postnumber
- description: API to create DHL private customer shipments for domestic and international destinations from Germany.
  name: DHL Parcel DE Private Shipping
  slug: dhl-parcel-de-private-shipping
- description: Creation of return labels for end customers across European countries shipping back to DHL Parcel Germany.
  name: DHL Parcel DE Returns
  slug: dhl-parcel-de-returns
- description: Designed for business customers of DHL Parcel Germany to manage and create shipment labels.
  name: DHL Parcel DE Shipping
  slug: dhl-parcel-de-shipping
- description: Allows DHL Parcel Germany customers to query the shipment status and history of shipments.
  name: DHL Parcel DE Tracking
  slug: dhl-parcel-de-tracking
- description: Downloads electronic documents from DHL Global Forwarding freight forwarding systems for air and ocean freight.
  name: Document DHL Global Forwarding
  slug: dgf-document
- description: Calculates duties and taxes for cross-border shipments processed through DHL eCommerce Americas.
  name: Duty and Tax DHL eCommerce Americas
  slug: duty-tax-dhl-ecommerce-americas
- description: Carrier-agnostic duty and tax calculator that works with any global carrier; includes a 30-day free trial offering from DHL.
  name: Duty and Tax Calculator Unified
  slug: duty-and-tax-calculator
- description: Handles domestic and international parcel shipments originating from the United Kingdom through DHL eCommerce.
  name: DHL eCommerce UK
  slug: ecommerce-uk
- description: Creates labels for shipments across Belgium, Luxembourg, and the Netherlands under DHL Parcel EU.
  name: Parcel EU BE LU NL
  slug: parcel-eu
- description: Allows registered Blue Dart customers in India to cancel scheduled shipment pickups via DHL eCommerce India.
  name: Pickup Cancellation DHL eCommerce India
  slug: pickup-cancellation-dhl-ecommerce-india-blue-dart
- description: Provides pricing for road freight shipments across Europe through DHL Freight.
  name: Price Quote DHL Freight
  slug: price-quote-dhl-freight
- description: Creates barcode labels in GS1 or ANSIFACT formats and related shipment documents for DHL Freight.
  name: Print DHL Freight
  slug: print-dhl-freight
- description: Determines available product codes for European road freight bookings through DHL Freight.
  name: Product DHL Freight
  slug: product-dhl-freight
- description: Retrieves detailed pickup information and product or sub-product codes for Blue Dart in India.
  name: Product and Sub-Product Pickup Detail DHL eCommerce India
  slug: product-and-sub-product-pickup-detail-dhl-ecommerce-india-blue-dart
- description: Obtains shipping products, rates, and delivery estimates for DHL eCommerce Americas shipments.
  name: Product Finder DHL eCommerce Americas
  slug: product-finder-dhl-ecommerce-americas
- description: Accesses Deutsche Post product portfolio for Internetmarke partners and integrated business customers.
  name: Products API Post Parcel Germany
  slug: products-api-post-parcel-germany
- description: Enables subscription-based push message delivery for DHL Global Forwarding freight shipments.
  name: Push API DHL Global Forwarding
  slug: dgf-push-api
- description: Provides reference data for products, fields, and glossary information across DHL eCommerce Americas APIs.
  name: References DHL eCommerce Americas
  slug: references-dhl-ecommerce-americas
- description: Allows Blue Dart customers in India to schedule pickups for shipment orders through DHL eCommerce India.
  name: Registration for Pickup DHL eCommerce India
  slug: registration-pickup-dhl-ecommerce-india-blue-dart
- description: Enables creation and retrieval of domestic return labels for shipments handled by DHL eCommerce Americas.
  name: Return Label DHL eCommerce Americas
  slug: return-label-dhl-ecommerce-americas
- description: Creates European palletized road freight transport orders through DHL Freight.
  name: Shipment Booking DHL Freight
  slug: shipment-booking-dhl-freight
- description: Enables shipment and transport bookings for multiple freight types via DHL Global Forwarding.
  name: Shipment Booking DHL Global Forwarding
  slug: dgf-shipment-booking
- description: Generates shipment labels for air and ocean freight handled by DHL Global Forwarding.
  name: Shipment Label DHL Global Forwarding
  slug: shipment-label-dhl-global-forwarding
- description: Provides access to the latest shipment event information for DHL Global Forwarding consignments.
  name: Shipment Status DHL Global Forwarding
  slug: dgf-shipment-status
- description: Delivers detailed shipment information and current status for Blue Dart shipments via DHL eCommerce India.
  name: Shipment Tracking DHL eCommerce India
  slug: shipment-tracking-dhl-ecommerce-india-blue-dart
- description: Provides comprehensive tracking including emissions and routing data for DHL Global Forwarding shipments.
  name: Shipment Tracking v2 DHL Global Forwarding
  slug: shipment-tracking-v2-dhl-global-forwarding
- description: Determines available product codes and projected delivery dates for DHL Freight European road shipments.
  name: Time Table DHL Freight
  slug: time-table-dhl-freight
- description: Track single or multiple packages and manifest shipments handled by DHL eCommerce Americas.
  name: Tracking DHL eCommerce Americas
  slug: tracking-dhl-ecommerce-americas
- description: The Find By Address API from DHL — 1 operation(s) for find by address.
  name: DHL Find By Address API
  slug: dhl-find-by-address-api
- description: The Find By Geo API from DHL — 1 operation(s) for find by geo.
  name: DHL Find By Geo API
  slug: dhl-find-by-geo-api
- description: The Find By Keyword Id API from DHL — 1 operation(s) for find by keyword id.
  name: DHL Find By Keyword Id API
  slug: dhl-find-by-keyword-id-api
- description: The Find By Location Id API from DHL — 1 operation(s) for find by location id.
  name: DHL Find By Location Id API
  slug: dhl-find-by-location-id-api
artifact_total: 59
collections:
- collection_type: open
  name: DHL Location Finder Unified API
  slug: open-dhl
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dhl-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dhl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dhl-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dhl
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dhl.com/
- group: other
  title: ''
  type: APICatalog
  url: https://developer.dhl.com/api-catalog
created: '2025-03-01'
description: DHL is a global logistics company that provides a wide range of services, including express delivery, freight transportation, supply chain solutions, and e-commerce services. As one of the largest logistics companies in the world, DHL operates in over 220 countries and territories, connecting businesses and individuals with seamless and reliable shipping solutions. The DHL API Developer Portal exposes APIs across the company's business divisions including DHL eCommerce, DHL Express, DHL Global Forwarding, DHL Freight, DHL Supply Chain, and Post and Parcel Germany.
finops:
- name: Dhl Finops
  service_category: API
  slug: dhl-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the DHL Express global shipping API. DHL Express provides express delivery services across more than 220 countries and territories. The DHL Unif
  name: DHL Express GraphQL Schema
  slug: dhl-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dhl.png
layout: provider
modified: '2026-05-19'
name: DHL
nav: Providers
network: true
overview: 'DHL publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Find By Address API, Find By Geo API, Find By Keyword Id API, and 1 more. Tagged areas include Freight, Logistics, Shipping, eCommerce, and Tracking.


  DHL''s developer surface includes authentication, documentation, and 4 more developer resources.'
plans:
- name: Dhl Plans Pricing
  plan_count: 3
  slug: dhl-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Dhl Rate Limits
  slug: dhl-rate-limits
score:
  band: thin
  composite: 37.7
  delta: 1.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.9
    developer_ergonomics: 19.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dhl/refs/heads/main/screenshots/dhl-2026-06-20T180001.png
security:
- kind: authentication
  name: Dhl Authentication
  slug: dhl-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dhl Domain Security
  slug: dhl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dhl
tags:
- Freight
- Logistics
- Shipping
- eCommerce
- Tracking
---
