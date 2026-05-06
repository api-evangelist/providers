---
aid: beacon-roofing-supply
url: https://raw.githubusercontent.com/api-evangelist/beacon-roofing-supply/refs/heads/main/apis.yml
name: Beacon Roofing Supply
description: Beacon Roofing Supply (BECN) is one of the largest distributors of residential and non-residential roofing materials and complementary building products in North America. Beacon operates the Beacon PRO+ digital platform providing roofing contractors with real-time inventory, pricing, online ordering, delivery tracking, and account management. Beacon PRO+ offers a REST API and Swagger-documented integration layer for contractor management software, ERP systems, and roofing business applications. Beacon was acquired by QXO in 2025.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Construction
  - Distribution
  - Roofing
  - Building Materials
  - E-Commerce
access: 3rd-Party
created: '2026-03-23'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: beacon-roofing-supply:beacon-pro-plus
    name: Beacon PRO+ API
    description: The Beacon PRO+ API provides roofing contractors and integration partners with programmatic access to Beacon's product catalog, real-time inventory and pricing, order management, delivery tracking, account management, and manufacturer rebate tracking. The API is documented via Swagger UI and enables integrations with contractor management software like AccuLynx and JobNimbus.
    humanURL: https://beaconproplus.com/swagger/all_api/
    tags:
      - Construction
      - Roofing
      - Distribution
      - E-Commerce
      - Orders
    properties:
      - type: Documentation
        url: https://beaconproplus.com/swagger/all_api/
      - type: OpenAPI
        url: https://beaconproplus.com/swagger/all_api/
common:
  - type: Website
    url: https://www.becn.com/
  - type: Portal
    url: https://www.beaconproplus.com/
  - type: Documentation
    url: https://beaconproplus.com/swagger/all_api/
  - type: Support
    url: https://www.becn.com/contact-us
  - type: Features
    data:
      - name: Real-Time Inventory and Pricing
        description: Access live product inventory levels and pricing across Beacon locations for accurate contractor quoting.
      - name: Online Ordering
        description: Place, manage, and track roofing material orders programmatically through the Beacon PRO+ API.
      - name: Delivery Tracking
        description: Real-time delivery status updates and tracking for all Beacon material orders.
      - name: Account Management
        description: Manage contractor account details, billing, and payment information through the API.
      - name: Storm Tracking Alerts
        description: Receive storm event notifications to proactively reach out to customers in affected areas.
      - name: Rebate Tracking
        description: Track manufacturer rebate programs and earned rebates through the API.
  - type: UseCases
    data:
      - name: Contractor Management Software Integration
        description: Integrate Beacon PRO+ with AccuLynx, JobNimbus, or other contractor management platforms to enable in-app material ordering.
      - name: ERP Integration
        description: Connect enterprise ERP systems with Beacon ordering and inventory for automated procurement workflows.
      - name: Custom Ordering Portals
        description: Build custom ordering interfaces for roofing contractors that pull live Beacon pricing and inventory.
      - name: Delivery Logistics
        description: Integrate Beacon delivery tracking into construction project management and scheduling tools.
  - type: Integrations
    data:
      - name: AccuLynx
        description: Roofing contractor management software with native Beacon PRO+ integration for material ordering.
      - name: JobNimbus
        description: Contractor CRM and project management platform with Beacon PRO+ material order integration.
      - name: GAF
        description: Roofing manufacturer partnership enabling GAF product ordering through Beacon PRO+ e-commerce.
      - name: TrueCommerce EDI
        description: EDI integration service enabling electronic purchase orders, ASNs, and invoices with Beacon Roofing Supply.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
