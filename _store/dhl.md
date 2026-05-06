---
aid: dhl
url: https://raw.githubusercontent.com/api-evangelist/dhl/refs/heads/main/apis.yml
name: DHL
description: DHL is a global logistics company that provides a wide range of services, including express delivery, freight transportation, supply chain solutions, and e-commerce services. As one of the largest logistics companies in the world, DHL operates in over 220 countries and territories, connecting businesses and individuals with seamless and reliable shipping solutions. The DHL API Developer Portal exposes APIs across the company's business divisions including DHL eCommerce, DHL Express, DHL Global Forwarding, DHL Freight, DHL Supply Chain, and Post and Parcel Germany.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Freight
  - Logistics
  - Shipping
  - eCommerce
  - Tracking
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: dhl:location-finder-unified
    name: Location Finder Unified
    humanURL: https://developer.dhl.com/api-reference/location-finder-unified
    tags:
      - Locations
      - Logistics
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/location-finder-unified
    description: Provides a single interface to discover all DHL locations that handle parcels and letters across multiple DHL divisions including Post and Parcel Germany, DHL Express, DHL eCommerce, and DHL Freight.
  - aid: dhl:shipment-tracking-unified
    name: Shipment Tracking Unified
    humanURL: https://developer.dhl.com/api-reference/shipment-tracking
    tags:
      - Tracking
      - Shipping
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/shipment-tracking
    description: Provides shipment status access across DHL Freight, DHL eCommerce, DHL Supply Chain, DHL Global Forwarding, and Post and Parcel Germany through a single unified tracking interface.
  - aid: dhl:shipment-tracking-unified-push
    name: Shipment Tracking Unified Push
    humanURL: https://developer.dhl.com/api-reference/shipment-tracking-unified-push
    tags:
      - Tracking
      - Push
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/shipment-tracking-unified-push
    description: Push-based variant of the Shipment Tracking Unified API that proactively sends updates on shipment status to subscribed consumers across DHL divisions.
  - aid: dhl:user-guide-dhl-ecommerce-americas
    name: User Guide DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/user-guide-dhl-ecommerce-americas
    tags:
      - eCommerce
      - Americas
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/user-guide-dhl-ecommerce-americas
    description: One-stop solution for shipping products including duty and tax calculations, shipping labels, manifests, and tracking for DHL eCommerce Americas customers.
  - aid: dhl:additional-services-dhl-freight
    name: Additional Services DHL Freight
    humanURL: https://developer.dhl.com/api-reference/additional-services-dhl-freight
    tags:
      - Freight
      - Services
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/additional-services-dhl-freight
    description: Validates which additional services combine with DHL Freight products for European palletized road freight transport.
  - aid: dhl:authentication-dhl-ecommerce-americas
    name: Authentication DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/authentication-dhl-ecommerce-americas
    tags:
      - Authentication
      - eCommerce
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/authentication-dhl-ecommerce-americas
    description: Access token generation endpoint for authenticating against DHL eCommerce Americas services.
  - aid: dhl:authentication-api-dhl-freight
    name: Authentication API DHL Freight
    humanURL: https://developer.dhl.com/api-reference/authentication-api-dhl-freight
    tags:
      - Authentication
      - Freight
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/authentication-api-dhl-freight
    description: Provides authentication services for DHL Group freight operations across European road freight products.
  - aid: dhl:authentication-api-post-parcel-germany
    name: Authentication API Post Parcel Germany
    humanURL: https://developer.dhl.com/api-reference/authentication-api-post-parcel-germany
    tags:
      - Authentication
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/authentication-api-post-parcel-germany
    description: Authentication for business customers of Deutsche Post and Parcel Germany services.
  - aid: dhl:changelog-dhl-ecommerce-americas
    name: Changelog DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/changelog-dhl-ecommerce-americas
    tags:
      - Changelog
      - eCommerce
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/changelog-dhl-ecommerce-americas
    description: Documents product updates, features, enhancements, and bug fixes for DHL eCommerce Americas APIs.
  - aid: dhl:datafactory-autocomplete-20-post-parcel-germany
    name: DATAFACTORY AUTOCOMPLETE 2.0
    humanURL: https://developer.dhl.com/api-reference/datafactory-autocomplete-20-post-parcel-germany
    tags:
      - Address
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/datafactory-autocomplete-20-post-parcel-germany
    description: Automatic postal data completion service for streamlined address entry across Post and Parcel Germany products.
  - aid: dhl:deutsche-post-hybrid-mail-shipments-e-post-post-parcel-germany
    name: Deutsche Post Hybrid Mail Shipments E-POST
    humanURL: https://developer.dhl.com/api-reference/deutsche-post-hybrid-mail-shipments-e-post-post-parcel-germany
    tags:
      - Mail
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/deutsche-post-hybrid-mail-shipments-e-post-post-parcel-germany
    description: Allows business customers to send PDF documents as physical mail shipments via Deutsche Post with tracking.
  - aid: dhl:deutsche-post-international-post-parcel-germany
    name: Deutsche Post International
    humanURL: https://developer.dhl.com/api-reference/deutsche-post-international-post-parcel-germany
    tags:
      - Mail
      - International
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/deutsche-post-international-post-parcel-germany
    description: Creates labels for international mail, lightweight items, and merchandise shipments via Deutsche Post.
  - aid: dhl:deutsche-post-internetmarke-post-parcel-germany
    name: Deutsche Post INTERNETMARKE
    humanURL: https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-parcel-germany
    tags:
      - Postage
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-parcel-germany
    description: Provides online postage purchase for domestic and international mail products from Deutsche Post.
  - aid: dhl:deutsche-post-order-management-am-post-parcel-germany
    name: Deutsche Post Order Management AM
    humanURL: https://developer.dhl.com/api-reference/deutsche-post-order-management-am-post-parcel-germany
    tags:
      - Orders
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/deutsche-post-order-management-am-post-parcel-germany
    description: Electronic order management for Deutsche Post commercial and logistics processes.
  - aid: dhl:deutsche-post-print-mailing-dispatch-preparation-post-parcel-germany
    name: Deutsche Post Print-Mailing Dispatch Preparation
    humanURL: https://developer.dhl.com/api-reference/deutsche-post-print-mailing-dispatch-preparation-post-parcel-germany
    tags:
      - Marketing
      - Mail
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/deutsche-post-print-mailing-dispatch-preparation-post-parcel-germany
    description: Manages dialogue marketing print mailings including pricing, documents, and franking workflows.
  - aid: dhl:deutsche-post-print-mailing-targeting-post-parcel-germany
    name: Deutsche Post Print-Mailing Targeting
    humanURL: https://developer.dhl.com/api-reference/deutsche-post-print-mailing-targeting-post-parcel-germany
    tags:
      - Marketing
      - Targeting
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/deutsche-post-print-mailing-targeting-post-parcel-germany
    description: Plans dialogue marketing campaigns with target groups and recipient data for print mailings.
  - aid: dhl:ecommerce-europe-econnect
    name: DHL eCommerce Europe eConnect
    humanURL: https://developer.dhl.com/api-reference/ecommerce-europe
    tags:
      - eCommerce
      - Europe
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/ecommerce-europe
    description: Enables cross-border European shipments including Parcel Connect and return services across DHL eCommerce Europe.
  - aid: dhl:ecommerce-europe-econnect-beta
    name: DHL eCommerce Europe eConnect Beta
    humanURL: https://developer.dhl.com/api-reference/dhl-ecommerce-europe-econnect-beta
    tags:
      - eCommerce
      - Beta
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dhl-ecommerce-europe-econnect-beta
    description: Beta features documentation for enhanced eCommerce European shipping capabilities ahead of general availability.
  - aid: dhl:dhl-parcel-de-pickup
    name: DHL Parcel DE Pickup
    humanURL: https://developer.dhl.com/api-reference/dhl-parcel-de-pickup-post-parcel-germany
    tags:
      - Pickup
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dhl-parcel-de-pickup-post-parcel-germany
    description: Place pickup orders and query pickup locations and status details for DHL Parcel Germany.
  - aid: dhl:dhl-parcel-de-postnumber
    name: DHL Parcel DE Postnumber
    humanURL: https://developer.dhl.com/api-reference/dhl-parcel-de-postnumber-post-parcel-germany
    tags:
      - Validation
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dhl-parcel-de-postnumber-post-parcel-germany
    description: Validates postnumbers to ensure deliverability of shipments to Deutsche Post and DHL parcel lockers.
  - aid: dhl:dhl-parcel-de-private-shipping
    name: DHL Parcel DE Private Shipping
    humanURL: https://developer.dhl.com/api-reference/dhl-parcel-de-private-shipping-post-parcel-germany
    tags:
      - Shipping
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dhl-parcel-de-private-shipping-post-parcel-germany
    description: API to create DHL private customer shipments for domestic and international destinations from Germany.
  - aid: dhl:dhl-parcel-de-returns
    name: DHL Parcel DE Returns
    humanURL: https://developer.dhl.com/api-reference/dhl-parcel-de-returns-post-parcel-germany
    tags:
      - Returns
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dhl-parcel-de-returns-post-parcel-germany
    description: Creation of return labels for end customers across European countries shipping back to DHL Parcel Germany.
  - aid: dhl:dhl-parcel-de-shipping
    name: DHL Parcel DE Shipping
    humanURL: https://developer.dhl.com/api-reference/parcel-de-shipping-post-parcel-germany-v2
    tags:
      - Shipping
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/parcel-de-shipping-post-parcel-germany-v2
    description: Designed for business customers of DHL Parcel Germany to manage and create shipment labels.
  - aid: dhl:dhl-parcel-de-tracking
    name: DHL Parcel DE Tracking
    humanURL: https://developer.dhl.com/api-reference/dhl-parcel-de-shipment-tracking-post-parcel-germany
    tags:
      - Tracking
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dhl-parcel-de-shipment-tracking-post-parcel-germany
    description: Allows DHL Parcel Germany customers to query the shipment status and history of shipments.
  - aid: dhl:dgf-document
    name: Document DHL Global Forwarding
    humanURL: https://developer.dhl.com/api-reference/dgf-document
    tags:
      - Documents
      - Forwarding
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dgf-document
    description: Downloads electronic documents from DHL Global Forwarding freight forwarding systems for air and ocean freight.
  - aid: dhl:duty-tax-dhl-ecommerce-americas
    name: Duty and Tax DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/duty-tax-dhl-ecommerce-americas
    tags:
      - Duty
      - Tax
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/duty-tax-dhl-ecommerce-americas
    description: Calculates duties and taxes for cross-border shipments processed through DHL eCommerce Americas.
  - aid: dhl:duty-and-tax-calculator
    name: Duty and Tax Calculator Unified
    humanURL: https://developer.dhl.com/api-reference/duty-and-tax-calculator
    tags:
      - Duty
      - Tax
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/duty-and-tax-calculator
    description: Carrier-agnostic duty and tax calculator that works with any global carrier; includes a 30-day free trial offering from DHL.
  - aid: dhl:ecommerce-uk
    name: DHL eCommerce UK
    humanURL: https://developer.dhl.com/api-reference/ecommerce-uk
    tags:
      - eCommerce
      - United Kingdom
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/ecommerce-uk
    description: Handles domestic and international parcel shipments originating from the United Kingdom through DHL eCommerce.
  - aid: dhl:parcel-eu
    name: Parcel EU BE LU NL
    humanURL: https://developer.dhl.com/api-reference/parcel-eu
    tags:
      - Parcel
      - Europe
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/parcel-eu
    description: Creates labels for shipments across Belgium, Luxembourg, and the Netherlands under DHL Parcel EU.
  - aid: dhl:pickup-cancellation-dhl-ecommerce-india-blue-dart
    name: Pickup Cancellation DHL eCommerce India
    humanURL: https://developer.dhl.com/api-reference/pickup-cancellation-dhl-ecommerce-india-blue-dart
    tags:
      - Pickup
      - India
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/pickup-cancellation-dhl-ecommerce-india-blue-dart
    description: Allows registered Blue Dart customers in India to cancel scheduled shipment pickups via DHL eCommerce India.
  - aid: dhl:price-quote-dhl-freight
    name: Price Quote DHL Freight
    humanURL: https://developer.dhl.com/api-reference/price-quote-dhl-freight
    tags:
      - Pricing
      - Freight
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/price-quote-dhl-freight
    description: Provides pricing for road freight shipments across Europe through DHL Freight.
  - aid: dhl:print-dhl-freight
    name: Print DHL Freight
    humanURL: https://developer.dhl.com/api-reference/print-dhl-freight
    tags:
      - Print
      - Freight
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/print-dhl-freight
    description: Creates barcode labels in GS1 or ANSIFACT formats and related shipment documents for DHL Freight.
  - aid: dhl:product-dhl-freight
    name: Product DHL Freight
    humanURL: https://developer.dhl.com/api-reference/product-dhl-freight
    tags:
      - Products
      - Freight
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/product-dhl-freight
    description: Determines available product codes for European road freight bookings through DHL Freight.
  - aid: dhl:product-and-sub-product-pickup-detail-dhl-ecommerce-india-blue-dart
    name: Product and Sub-Product Pickup Detail DHL eCommerce India
    humanURL: https://developer.dhl.com/api-reference/product-and-sub-product-pickup-detail-dhl-ecommerce-india-blue-dart
    tags:
      - Products
      - India
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/product-and-sub-product-pickup-detail-dhl-ecommerce-india-blue-dart
    description: Retrieves detailed pickup information and product or sub-product codes for Blue Dart in India.
  - aid: dhl:product-finder-dhl-ecommerce-americas
    name: Product Finder DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/product-finder-dhl-ecommerce-americas
    tags:
      - Products
      - Americas
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/product-finder-dhl-ecommerce-americas
    description: Obtains shipping products, rates, and delivery estimates for DHL eCommerce Americas shipments.
  - aid: dhl:products-api-post-parcel-germany
    name: Products API Post Parcel Germany
    humanURL: https://developer.dhl.com/api-reference/products-api-post-parcel-germany
    tags:
      - Products
      - Germany
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/products-api-post-parcel-germany
    description: Accesses Deutsche Post product portfolio for Internetmarke partners and integrated business customers.
  - aid: dhl:dgf-push-api
    name: Push API DHL Global Forwarding
    humanURL: https://developer.dhl.com/api-reference/dgf-push-api
    tags:
      - Push
      - Forwarding
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dgf-push-api
    description: Enables subscription-based push message delivery for DHL Global Forwarding freight shipments.
  - aid: dhl:references-dhl-ecommerce-americas
    name: References DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/references-dhl-ecommerce-americas
    tags:
      - Reference
      - eCommerce
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/references-dhl-ecommerce-americas
    description: Provides reference data for products, fields, and glossary information across DHL eCommerce Americas APIs.
  - aid: dhl:registration-pickup-dhl-ecommerce-india-blue-dart
    name: Registration for Pickup DHL eCommerce India
    humanURL: https://developer.dhl.com/api-reference/registration-pickup-dhl-ecommerce-india-blue-dart
    tags:
      - Pickup
      - India
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/registration-pickup-dhl-ecommerce-india-blue-dart
    description: Allows Blue Dart customers in India to schedule pickups for shipment orders through DHL eCommerce India.
  - aid: dhl:return-label-dhl-ecommerce-americas
    name: Return Label DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/return-label-dhl-ecommerce-americas
    tags:
      - Returns
      - Americas
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/return-label-dhl-ecommerce-americas
    description: Enables creation and retrieval of domestic return labels for shipments handled by DHL eCommerce Americas.
  - aid: dhl:shipment-booking-dhl-freight
    name: Shipment Booking DHL Freight
    humanURL: https://developer.dhl.com/api-reference/shipment-booking-dhl-freight
    tags:
      - Booking
      - Freight
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/shipment-booking-dhl-freight
    description: Creates European palletized road freight transport orders through DHL Freight.
  - aid: dhl:dgf-shipment-booking
    name: Shipment Booking DHL Global Forwarding
    humanURL: https://developer.dhl.com/api-reference/dgf-shipment-booking
    tags:
      - Booking
      - Forwarding
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dgf-shipment-booking
    description: Enables shipment and transport bookings for multiple freight types via DHL Global Forwarding.
  - aid: dhl:shipment-label-dhl-global-forwarding
    name: Shipment Label DHL Global Forwarding
    humanURL: https://developer.dhl.com/api-reference/shipment-label-dhl-global-forwarding
    tags:
      - Labels
      - Forwarding
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/shipment-label-dhl-global-forwarding
    description: Generates shipment labels for air and ocean freight handled by DHL Global Forwarding.
  - aid: dhl:dgf-shipment-status
    name: Shipment Status DHL Global Forwarding
    humanURL: https://developer.dhl.com/api-reference/dgf-shipment-status
    tags:
      - Status
      - Forwarding
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/dgf-shipment-status
    description: Provides access to the latest shipment event information for DHL Global Forwarding consignments.
  - aid: dhl:shipment-tracking-dhl-ecommerce-india-blue-dart
    name: Shipment Tracking DHL eCommerce India
    humanURL: https://developer.dhl.com/api-reference/shipment-tracking-dhl-ecommerce-india-blue-dart
    tags:
      - Tracking
      - India
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/shipment-tracking-dhl-ecommerce-india-blue-dart
    description: Delivers detailed shipment information and current status for Blue Dart shipments via DHL eCommerce India.
  - aid: dhl:shipment-tracking-v2-dhl-global-forwarding
    name: Shipment Tracking v2 DHL Global Forwarding
    humanURL: https://developer.dhl.com/api-reference/shipment-tracking-v2-dhl-global-forwarding
    tags:
      - Tracking
      - Forwarding
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/shipment-tracking-v2-dhl-global-forwarding
    description: Provides comprehensive tracking including emissions and routing data for DHL Global Forwarding shipments.
  - aid: dhl:time-table-dhl-freight
    name: Time Table DHL Freight
    humanURL: https://developer.dhl.com/api-reference/time-table-dhl-freight
    tags:
      - Schedule
      - Freight
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/time-table-dhl-freight
    description: Determines available product codes and projected delivery dates for DHL Freight European road shipments.
  - aid: dhl:tracking-dhl-ecommerce-americas
    name: Tracking DHL eCommerce Americas
    humanURL: https://developer.dhl.com/api-reference/tracking-dhl-ecommerce-americas
    tags:
      - Tracking
      - Americas
    properties:
      - type: Documentation
        url: https://developer.dhl.com/api-reference/tracking-dhl-ecommerce-americas
    description: Track single or multiple packages and manifest shipments handled by DHL eCommerce Americas.
common:
  - type: Documentation
    url: https://developer.dhl.com/
  - type: APICatalog
    url: https://developer.dhl.com/api-catalog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
