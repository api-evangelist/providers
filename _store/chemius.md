---
aid: chemius
name: Chemius
x-type: company
description: Chemius is a cloud-based chemical compliance platform that automates Safety Data Sheet (SDS), Technical Data Sheet (TDS), and regulatory label creation in 38+ languages for organizations handling chemical products. The platform exposes an API suite covering SDS, TDS, ADR transport documentation, ERP integration, labels, web shop product data, and PDF generation, and offers AI-assisted authoring through the Chemius AI SDS assistant. Chemius is hosted in DIN ISO/IEC 27001-certified German data centers and supports CLP 1272/2008, REACH 1907/2006, detergents, aerosols, and US OSHA / GHS regulatory frameworks.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chemius/refs/heads/main/apis.yml
tags:
  - ADR
  - AI
  - Chemicals
  - Chemists
  - Compliance
  - GHS
  - Hazard Communication
  - Labels
  - REACH
  - Regulatory
  - Research
  - Safety Data Sheets
  - SaaS
  - SDS
  - TDS
created: '2025-03-01'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chemius:sds-api
    name: Chemius Safety Data Sheet API
    description: Programmatic access to Chemius Safety Data Sheet (SDS) creation, retrieval, and version control. Supports multilingual SDS generation aligned with CLP 1272/2008, REACH 1907/2006, and GHS formats.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chemius.net/chemius-api/
    tags:
      - Compliance
      - SDS
      - Safety Data Sheets
    properties:
      - type: Documentation
        url: https://www.chemius.net/chemius-api/
  - aid: chemius:tds-api
    name: Chemius Technical Data Sheet API
    description: API for generating and retrieving Technical Data Sheets (TDS) for chemical products, including version control and translation.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chemius.net/chemius-api/
    tags:
      - Compliance
      - TDS
      - Technical Data Sheets
    properties:
      - type: Documentation
        url: https://www.chemius.net/chemius-api/
  - aid: chemius:adr-api
    name: Chemius ADR Transport API
    description: API for generating ADR (European Agreement concerning the International Carriage of Dangerous Goods by Road) transport documentation for chemical shipments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chemius.net/chemius-api/
    tags:
      - ADR
      - Transport
      - Compliance
    properties:
      - type: Documentation
        url: https://www.chemius.net/chemius-api/
  - aid: chemius:erp-api
    name: Chemius ERP Integration API
    description: API for integrating Chemius product, SDS, TDS, and label data with enterprise ERP systems for synchronized chemical product information.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chemius.net/chemius-api/
    tags:
      - ERP
      - Integration
    properties:
      - type: Documentation
        url: https://www.chemius.net/chemius-api/
  - aid: chemius:label-api
    name: Chemius Label API
    description: API for generating regulatory-compliant chemical product labels with QR codes, hazard pictograms, and multilingual content.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chemius.net/chemius-api/
    tags:
      - Labels
      - Compliance
      - GHS
    properties:
      - type: Documentation
        url: https://www.chemius.net/chemius-api/
  - aid: chemius:web-shop-api
    name: Chemius Web Shop API
    description: API exposing chemical product data, SDSs, and TDSs for embedding in e-commerce experiences and customer-facing web shops.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chemius.net/chemius-api/
    tags:
      - E-Commerce
      - Web Shop
    properties:
      - type: Documentation
        url: https://www.chemius.net/chemius-api/
  - aid: chemius:pdf-api
    name: Chemius PDF API
    description: API for rendering Chemius SDSs, TDSs, labels, and other compliance documents as PDF artifacts for distribution and archival.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.chemius.net/chemius-api/
    tags:
      - PDF
      - Documents
    properties:
      - type: Documentation
        url: https://www.chemius.net/chemius-api/
common:
  - type: Website
    url: https://www.chemius.net/
  - type: Documentation
    url: https://www.chemius.net/chemius-api/
  - type: Pricing
    url: https://www.chemius.net/pricing/
  - type: Contact
    url: https://www.chemius.net/contact/
  - type: JSONLD
    url: json-ld/chemius-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Automated SDS Authoring
      - name: Multilingual Output (38+ Languages)
      - name: Technical Data Sheets
      - name: Regulatory Labels with QR Codes
      - name: ADR Transport Documents
      - name: AI SDS Assistant
      - name: Version Control with Change Tracking
      - name: Real-Time Compliance Monitoring
      - name: UFI and Poison Centre Notifications
      - name: Regulatory Dashboard
      - name: ERP Integration
      - name: Web Shop Product Feeds
      - name: PDF Rendering
  - name: UseCases
    type: UseCases
    data:
      - name: SDS Authoring at Scale
      - name: Multilingual Chemical Compliance
      - name: Hazard Label Production
      - name: ADR Shipment Documentation
      - name: Poison Centre Notification Filing
      - name: ERP-Driven Chemical Product Catalogs
      - name: Customer-Facing SDS Portals
      - name: Regulatory Change Monitoring
  - name: Standards
    type: Standards
    data:
      - name: CLP 1272/2008
      - name: REACH 1907/2006
      - name: GHS
      - name: ADR
      - name: US OSHA Hazard Communication
      - name: UFI
      - name: ISO/IEC 27001
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
