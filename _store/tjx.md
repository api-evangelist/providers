---
aid: tjx
name: TJX Companies
description: The TJX Companies, Inc. is an American multinational off-price department store corporation headquartered in Framingham, Massachusetts, ranked No. 80 on the 2024 Fortune 500 list. Operating over 4,800 stores across nine countries and three continents under brands including T.J. Maxx, Marshalls, HomeGoods, Sierra, HomeSense (US), and Winners, HomeSense, Marshalls (Canada), TJX provides supplier and vendor integration through EDI and web-based portal platforms. Supplier connectivity is handled via Oracle iSupplier, SupplierOne, and the DiCentral ASN Vendor Portal, supporting purchase orders, advanced shipping notices, invoicing, and payment tracking.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Retail
  - Off-Price
  - Fortune 100
  - Supply Chain
  - EDI
created: '2024-11-27'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tjx/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tjx:tjx-isupplier
    name: TJX Oracle iSupplier Portal
    description: The TJX Oracle iSupplier portal allows not-for-resale suppliers to manage purchase orders, track invoices, monitor payment status, and handle deduction disputes. Suppliers can access real-time account activity and submit invoices electronically via integration with Transcepta. Available to approved TJX suppliers via login credentials.
    humanURL: https://www.mytjx.com/mytjx/supplier.html
    tags:
      - Supplier Portal
      - Oracle
      - Invoicing
      - Purchase Orders
    properties:
      - type: Documentation
        url: https://www.tjx.com/mytjx/supplier/files/iSupplier-User-Guide-EN.pdf
  - aid: tjx:tjx-edi
    name: TJX EDI Integration
    description: TJX Companies requires EDI compliance for all resale vendors, supporting purchase orders (850), purchase order acknowledgements (855), advanced shipping notices (856), invoices (810), motor carrier load tender (204), response to load tender (990), and transportation carrier shipment status (214). Integration is available through approved EDI service providers including SPS Commerce, DiCentral, Zenbridge, and others.
    humanURL: https://www.spscommerce.com/network/find-a-partner/view/the-tjx-companies-inc/
    tags:
      - EDI
      - Supply Chain
      - Vendors
    properties:
      - type: Documentation
        url: https://www.spscommerce.com/network/find-a-partner/view/the-tjx-companies-inc/
  - aid: tjx:tjx-asn-vendor-portal
    name: TJX ASN Vendor Portal
    description: The TJX Companies LLC Advanced Shipping Notice (ASN) Vendor Portal powered by DiCentral allows resale vendors to create and submit advance shipping notices, manage compliance requirements, and handle electronic transaction processing for shipments to TJX distribution centers.
    humanURL: https://diweb.dicentral.com/tjx/SignUp/GetStarted.aspx
    tags:
      - ASN
      - Shipping
      - Vendors
      - DiCentral
    properties:
      - type: Documentation
        url: https://diweb.dicentral.com/tjx/SignUp/GetStarted.aspx
  - aid: tjx:tjx-supplierone
    name: TJX SupplierOne Diversity Portal
    description: The TJX SupplierOne portal enables diverse supplier registration, certification tracking, and quarterly Tier II program reporting. Suppliers can complete vendor applications, provide business documentation and certifications, and participate in TJX's supplier diversity program.
    humanURL: https://tjx.supplierone.co/
    tags:
      - Supplier Diversity
      - Vendors
      - Registration
    properties:
      - type: Documentation
        url: https://tjx.supplierone.co/
common:
  - type: Website
    url: https://www.tjx.com/
  - type: Documentation
    url: https://www.tjx.com/mytjx/supplier/supplier.html
  - type: Portal
    url: https://www.mytjx.com/mytjx/supplier.html
  - type: GitHubOrganization
    url: https://github.com/TJX
  - type: Features
    data:
      - name: Oracle iSupplier Portal
        description: Web-based supplier self-service for invoice tracking, payment status, deduction management, and purchase order visibility.
      - name: EDI Vendor Integration
        description: Electronic Data Interchange compliance for purchase orders (850), ASNs (856), invoices (810), and related transactions for resale suppliers.
      - name: ASN Vendor Portal
        description: DiCentral-powered portal for creating and submitting advance shipping notices and managing compliance.
      - name: SupplierOne Diversity Registration
        description: Supplier diversity portal for diverse supplier registration, certification, and Tier II reporting.
      - name: Transcepta Electronic Invoicing
        description: Digital invoice submission via Transcepta integration, reducing paperwork and expediting payment cycles.
      - name: Multi-Brand Vendor Support
        description: Vendor integration covering all TJX banners including T.J. Maxx, Marshalls, HomeGoods, Sierra, HomeSense, Winners, and TK Maxx.
  - type: UseCases
    data:
      - name: Supplier Invoice Submission
        description: Suppliers electronically submit invoices through iSupplier or Transcepta and track payment status in real time.
      - name: Purchase Order Management
        description: Suppliers receive and acknowledge purchase orders from TJX banners via EDI 850/855 transactions.
      - name: Advance Shipping Notice
        description: Vendors create and submit ASNs (EDI 856) to notify TJX distribution centers of incoming shipments.
      - name: Deduction Dispute Automation
        description: Suppliers manage and dispute payment deductions through the Oracle iSupplier portal.
      - name: Supplier Diversity Reporting
        description: Diverse suppliers register, maintain certifications, and submit quarterly Tier II reports through SupplierOne.
      - name: EDI Compliance Onboarding
        description: New vendors establish EDI connectivity via approved service providers and complete TJX's testing requirements.
  - type: Integrations
    data:
      - name: SPS Commerce
        description: EDI integration and compliance platform for TJX vendor connectivity.
      - name: DiCentral
        description: ASN Vendor Portal and EDI integration provider powering TJX's vendor shipping notice system.
      - name: Zenbridge
        description: EDI integration platform supporting TJX vendor compliance requirements.
      - name: Pipe17
        description: Order management and EDI integration connector for TJX Companies.
      - name: Transcepta
        description: Electronic invoicing platform for TJX supplier invoice submission.
      - name: Oracle iSupplier
        description: Oracle-based supplier portal for invoice management and purchase order tracking.
      - name: Cleo
        description: EDI integration solution for TJX trading partner compliance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
