---
aid: ch-robinson-worldwide
url: https://raw.githubusercontent.com/api-evangelist/ch-robinson-worldwide/refs/heads/main/apis.yml
name: C.H. Robinson
x-type: company
tags:
  - Freight
  - Logistics
  - Shipping
  - Supply Chain
  - Transportation
  - Transportation Management
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-23'
position: Consumer
description: C.H. Robinson is one of the world's largest third-party logistics (3PL) providers, offering global freight transportation, supply chain management, customs brokerage, and sourcing of fresh produce. Its Navisphere transportation management system provides end-to-end supply chain planning, purchase order management, execution, freight payment, and business intelligence. C.H. Robinson exposes APIs that allow shippers and carriers to integrate quoting, booking, tracking, documents, and payment workflows directly into their own TMS or ERP platforms.
apis:
  - aid: ch-robinson:carrier-api
    name: C.H. Robinson Carrier API
    tags:
      - Booking
      - Carriers
      - Documents
      - Loads
      - Payment
      - Visibility
    humanURL: https://developer.chrobinson.com/carrier
    baseURL: https://developer.chrobinson.com
    properties:
      - url: https://developer.chrobinson.com/carrier
        type: Documentation
      - url: https://www.chrobinson.com/en-us/carriers/api-connectivity/
        type: Overview
    description: The C.H. Robinson Carrier API enables carriers to find, offer, book, and auto-create loads directly from their own TMS, send visibility updates, upload documents for faster invoicing, and check payment status. The API is offered free to carriers to streamline integration with C.H. Robinson's logistics network.
  - aid: ch-robinson:shipper-navisphere-api
    name: C.H. Robinson Navisphere Shipper API
    tags:
      - Navisphere
      - Quoting
      - Shipments
      - Shippers
      - Tracking
      - TMS
    humanURL: https://www.chrobinson.com/en-us/technology/shipper-technology/navisphere/
    baseURL: https://developer.chrobinson.com
    properties:
      - url: https://developer.chrobinson.com/
        type: Documentation
      - url: https://www.chrobinson.com/en-us/technology/connectivity-integrations/
        type: Overview
    description: The Navisphere Shipper API integrates C.H. Robinson's global transportation management system into a shipper's TMS or ERP. Capabilities include real-time rate quoting, load tendering, shipment tracking and visibility, document exchange, freight audit and payment, and business intelligence access across multi-modal transportation (truckload, LTL, intermodal, ocean, air, customs).
common:
  - type: Website
    url: https://www.chrobinson.com
  - type: DeveloperPortal
    url: https://developer.chrobinson.com/
  - type: Documentation
    url: https://www.chrobinson.com/en-us/technology/connectivity-integrations/
  - type: Technology
    url: https://www.chrobinson.com/en-us/technology/
  - type: Navisphere
    url: https://www.chrobinson.com/en-us/technology/shipper-technology/navisphere/
  - type: CarrierPortal
    url: https://www.chrobinson.com/en-us/carriers/api-connectivity/
  - type: About
    url: https://www.chrobinson.com/en-us/about-us/
  - type: Careers
    url: https://jobs.chrobinson.com/
  - type: News
    url: https://www.chrobinson.com/en-us/newsroom/
  - type: Investors
    url: https://investor.chrobinson.com/
  - type: TermsOfService
    url: https://www.chrobinson.com/en-us/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.chrobinson.com/en-us/privacy-notice/
  - type: LinkedIn
    url: https://www.linkedin.com/company/c.h.-robinson/
  - type: X
    url: https://x.com/CHRobinsonInc
  - name: Features
    type: Features
    data:
      - name: Rate Quoting
      - name: Load Booking
      - name: Load Tendering
      - name: Shipment Tracking
      - name: Real-Time Visibility
      - name: Document Exchange
      - name: Payment Status
      - name: Freight Audit
      - name: Freight Payment
      - name: Business Intelligence
      - name: EDI
      - name: XML
      - name: API Connectivity
      - name: Carrier Onboarding
      - name: Load Matching
      - name: Capacity Search
      - name: Automated Booking
      - name: Tracking Webhooks
      - name: Proof of Delivery
      - name: Invoice Upload
  - name: UseCases
    type: UseCases
    data:
      - name: TMS Integration
      - name: Carrier Load Booking
      - name: Shipper Rate Shopping
      - name: Multi-Modal Transportation
      - name: Customs Brokerage
      - name: Global Forwarding
      - name: Produce Sourcing
      - name: Managed Transportation
      - name: Supply Chain Consulting
      - name: Fresh Produce Logistics
  - name: Integrations
    type: Integrations
    data:
      - name: Navisphere
      - name: Axele
      - name: Beyond Trucks
      - name: SmartHop
      - name: Geotab
      - name: SOS Trucking
      - name: SAP
      - name: Oracle
      - name: NetSuite
      - name: Microsoft Dynamics
      - name: Manhattan Associates
      - name: Blue Yonder
      - name: MercuryGate
      - name: Kuebix
  - name: Services
    type: Services
    data:
      - name: Truckload
      - name: Less Than Truckload
      - name: Intermodal
      - name: Ocean Freight
      - name: Air Freight
      - name: Customs Brokerage
      - name: Global Forwarding
      - name: Managed Services
      - name: Supply Chain Consulting
      - name: Robinson Fresh
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
