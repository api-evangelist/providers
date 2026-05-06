---
aid: berkshire-hathaway
name: Berkshire Hathaway
url: https://raw.githubusercontent.com/api-evangelist/berkshire-hathaway/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-19'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
description: Berkshire Hathaway is a multinational conglomerate holding company headquartered in Omaha, Nebraska. The company's diversified subsidiaries span insurance (GEICO, Berkshire Hathaway Specialty Insurance, National Indemnity), freight rail transportation (BNSF Railway), utilities and energy (Berkshire Hathaway Energy), manufacturing (Precision Castparts, Iscar), wholesale distribution (McLane Company), and services and retailing. BNSF Railway, one of North America's largest freight rail networks, operates a public API Center providing customer APIs for shipment tracking, pricing, scheduling, and waybill management.
tags:
  - Conglomerate
  - Energy
  - Finance
  - Freight Rail
  - Insurance
  - Investment
  - Manufacturing
  - Retail
  - Utilities
apis:
  - aid: berkshire-hathaway:bnsf-api
    name: BNSF Railway API
    tags:
      - Freight
      - Logistics
      - Rail
      - Shipment Tracking
      - Supply Chain
      - Transportation
    humanURL: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
    description: The BNSF API Center provides customer APIs for programmatic integration with BNSF Railway freight shipping operations. APIs enable real-time shipment tracing, intermodal hub operations, pricing and rate retrieval, transit schedule lookups, waybill management, and diagnostic testing. Authentication uses certificate-based mutual TLS (mTLS) for secure identity validation between customers and BNSF systems.
    properties:
      - type: Documentation
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/
      - type: GettingStarted
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/getting-started/
      - type: Console
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/developers-console/
      - type: APIReference
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/catalog/
      - type: Support
        url: https://www.bnsf.com/ship-with-bnsf/support-services/customer-api/support/
common:
  - type: Website
    url: https://www.berkshirehathaway.com
  - type: Features
    data:
      - name: BNSF Freight Rail Network
        description: BNSF Railway operates one of North America's largest freight rail networks, transporting consumer goods, agricultural products, industrial materials, coal, and intermodal containers across 32,500 route miles in 28 states and 3 Canadian provinces.
      - name: Insurance Operations
        description: Berkshire Hathaway's insurance operations include GEICO (auto insurance), Berkshire Hathaway Specialty Insurance, National Indemnity, General Re, and MedPro Group, providing insurance and reinsurance across personal and commercial lines.
      - name: Energy and Utilities
        description: Berkshire Hathaway Energy operates regulated electric and natural gas utilities, pipelines, and renewable energy facilities across the United States, United Kingdom, Canada, and Australia.
      - name: Manufacturing and Industrial
        description: Manufacturing subsidiaries include Precision Castparts (aerospace components), Iscar (cutting tools), Marmon Group (industrial products), and Lubrizol (specialty chemicals).
      - name: Wholesale Distribution
        description: McLane Company provides wholesale distribution of grocery and foodservice products to retail and restaurant customers across the United States.
  - type: UseCases
    data:
      - name: Freight Shipment Tracking
        description: Shippers and logistics providers integrate the BNSF API to display real-time freight tracking in their transportation management systems and customer-facing applications.
      - name: Freight Pricing and Scheduling
        description: Customers use the BNSF pricing and schedules APIs to obtain freight rates, compare transit times, and automate rate shopping in procurement and logistics workflows.
      - name: Waybill Submission
        description: Shippers submit bills of lading and retrieve waybill information programmatically through the BNSF Waybill Management API to reduce manual data entry and streamline freight documentation.
      - name: Intermodal Hub Operations
        description: Intermodal customers access container and trailer status, storage location, and driver pickup/delivery details at BNSF intermodal facilities through the Hub Operations API.
  - type: Integrations
    data:
      - name: Transportation Management Systems
        description: BNSF APIs integrate with TMS platforms used by shippers and third-party logistics providers to automate freight booking, tracking, and documentation within existing supply chain workflows.
      - name: Enterprise Resource Planning
        description: BNSF customer APIs enable direct integration with ERP and procurement systems to automate freight cost management, scheduling, and shipment visibility without manual portal access.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
