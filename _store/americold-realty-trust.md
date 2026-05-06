---
aid: americold-realty-trust
url: https://raw.githubusercontent.com/api-evangelist/americold-realty-trust/refs/heads/main/apis.yml
name: Americold Realty Trust
type: Index
image: https://www.americold.com/favicon.ico
tags:
  - Cold Storage
  - Logistics
  - Supply Chain
  - Warehousing
  - Real Estate
  - Temperature-Controlled
  - Cold Chain
  - EDI
  - 3PL
description: Americold Realty Trust is a global leader in temperature-controlled logistics, real estate, and value-added services, owning and operating one of the largest networks of cold storage warehouses in the world. The company serves food producers, retailers, and distributors with integrated logistics solutions, offering technology platforms such as i-3PL for customer-facing inventory and order visibility and EDI for system-to-system supply chain integration. While Americold provides customer-facing technology and integration capabilities, it does not currently publish a public developer-facing API portal with open OpenAPI documentation; integrations are established project-by-project through the Americold service desk and EDI onboarding process.
created: '2026-05-04'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: americold-i-3pl
    name: Americold i-3PL Platform
    humanURL: https://www.americold.com/technology-automation/i-3pl/
    baseURL: https://www.i-3pl.com/
    description: i-3PL is Americold's customer-facing digital supply chain platform offering real-time inventory tracking, order management, dock appointment scheduling, customizable alerts, and 40+ reporting tools across the Americold network. The platform supports integration with customer ERP systems for seamless data exchange but does not publish open public API documentation; programmatic integration is coordinated with the Americold Service Desk.
    tags:
      - Logistics
      - Supply Chain
      - Cold Storage
      - 3PL
      - Inventory
      - Reporting
    properties:
      - type: Portal
        url: https://www.i-3pl.com/login
      - type: Documentation
        url: https://www.americold.com/technology-automation/i-3pl/
      - type: Support
        url: https://www.americold.com/contact-us/
      - type: JSONSchema
        url: json-schema/americold-i-3pl-inventory-snapshot-schema.json
        title: i-3PL Inventory Snapshot Schema
      - type: JSONStructure
        url: json-structure/americold-i-3pl-inventory-snapshot-structure.json
        title: i-3PL Inventory Snapshot Structure
      - type: Example
        url: examples/americold-i-3pl-inventory-snapshot-example.json
        title: i-3PL Inventory Snapshot Example
  - aid: americold-edi
    name: Americold EDI
    humanURL: https://www.americold.com/technology-automation/edi-electronic-data-interchange/
    baseURL: https://www.americold.com/technology-automation/edi-electronic-data-interchange/
    description: Americold provides Electronic Data Interchange (EDI) capabilities for automated data exchange between Americold and depositor (customer) systems, supporting orders, inventory, shipments, and other supply chain transactions. The integration uses the X12 warehousing 900-series transaction sets common across third-party logistics providers (940 Warehouse Shipping Order, 943 Stock Transfer Shipment Advice, 944 Stock Transfer Receipt Advice, 945 Warehouse Shipping Advice, 947 Inventory Adjustment Advice, plus 856 ASN and 846 Inventory Inquiry).
    tags:
      - EDI
      - Integration
      - Supply Chain
      - X12
      - 3PL
      - AS2
    properties:
      - type: Documentation
        url: https://www.americold.com/technology-automation/edi-electronic-data-interchange/
      - type: Support
        url: https://www.americold.com/contact-us/
      - type: JSONSchema
        url: json-schema/americold-edi-warehouse-shipping-order-schema.json
        title: EDI Warehouse Shipping Order (940) Schema
      - type: JSONSchema
        url: json-schema/americold-edi-warehouse-shipping-advice-schema.json
        title: EDI Warehouse Shipping Advice (945) Schema
      - type: JSONStructure
        url: json-structure/americold-edi-warehouse-shipping-order-structure.json
        title: EDI Warehouse Shipping Order (940) Structure
      - type: JSONStructure
        url: json-structure/americold-edi-warehouse-shipping-advice-structure.json
        title: EDI Warehouse Shipping Advice (945) Structure
      - type: Example
        url: examples/americold-edi-warehouse-shipping-order-example.json
        title: EDI Warehouse Shipping Order (940) Example
      - type: Example
        url: examples/americold-edi-warehouse-shipping-advice-example.json
        title: EDI Warehouse Shipping Advice (945) Example
common:
  - type: Website
    url: https://www.americold.com
  - type: Portal
    url: https://www.i-3pl.com/login
  - type: TechnologyAutomation
    url: https://www.americold.com/technology-automation/
  - type: CustomerResources
    url: https://www.americold.com/customer-resources/
  - type: Contact
    url: https://www.americold.com/contact-us/
  - type: Careers
    url: https://www.americold.com/careers/
  - type: InvestorRelations
    url: https://ir.americold.com
  - type: PrivacyPolicy
    url: https://www.americold.com/privacy-policy/
  - type: TermsOfService
    url: https://www.americold.com/terms-of-use/
  - type: Features
    data:
      - name: Global Cold Storage Network
        description: Americold owns and operates one of the largest networks of temperature-controlled warehouses worldwide, with facilities across North America, Europe, Australia, New Zealand, and South America serving food producers, processors, distributors, and retailers.
      - name: i-3PL Customer Platform
        description: Customer-facing digital platform delivering real-time inventory tracking, order management, dock appointment scheduling, customizable alerts, and over 40 reporting tools across the Americold network from phone, tablet, or desktop.
      - name: EDI Supply Chain Integration
        description: Standards-based X12 EDI exchange of warehousing transactions (940/943/944/945/947) and shipping/inventory transactions (856, 846) between Americold's WMS/TMS/LMS/WES and depositor ERP systems for real-time supply chain visibility.
      - name: Lot-Level Traceability
        description: Item-lot granularity for receipts, holds, releases, and shipments enables food-safety traceability, recall readiness, and FSMA / HACCP compliance across the cold chain.
      - name: Multi-Temperature Zones
        description: Storage and handling across deep-frozen, frozen, refrigerated, cooler, and ambient temperature zones with documented temperature requirements and load-temperature recording on outbound shipments.
      - name: Value-Added Services
        description: Blast freezing, pick and pack, labeling and relabeling, repacking, kitting, staging, cross-dock, sloughing/tempering, plus light assembly and food processing services provided alongside storage.
  - type: UseCases
    data:
      - name: Cold Chain Outbound Fulfillment
        description: A depositor sends a 940 Warehouse Shipping Order to an Americold facility; Americold picks, stages, and ships product; a 945 Warehouse Shipping Advice returns to the depositor for ERP reconciliation.
      - name: Inventory Visibility for Food Manufacturers
        description: Frozen and refrigerated food manufacturers monitor on-hand, available, committed, and held inventory across Americold facilities using i-3PL snapshots, dashboards, and reports.
      - name: Dock Appointment Scheduling
        description: Carriers and depositor logistics teams book, modify, and cancel dock appointments at Americold facilities through i-3PL to optimize throughput and reduce dwell time.
      - name: Lot Traceability and Recall
        description: Quality assurance and food safety teams trace a lot from receipt through every shipment to support recalls and regulatory holds.
      - name: Stock Transfer Between Facilities
        description: Move inventory between Americold facilities using 943/944 transfer transactions to balance network inventory and meet regional demand.
      - name: ERP-to-WMS Integration
        description: Connect SAP, Oracle, NetSuite, Microsoft Dynamics, and other ERP systems to Americold's WMS through EDI and managed integration partners.
  - type: Integrations
    data:
      - name: SPS Commerce
        description: SPS Commerce provides pre-built EDI connections used by depositors and 3PL trading partners to exchange warehousing transaction sets with Americold over a managed network.
      - name: Stedi
        description: Stedi's API-first EDI platform is used by modern engineering teams to translate, validate, and exchange X12 warehouse transactions with Americold programmatically.
      - name: Cleo Integration Cloud
        description: Cleo provides AS2, SFTP, and API integration tooling commonly used to connect depositor ERP systems to 3PL warehouse partners like Americold.
      - name: SAP and Oracle ERP
        description: Americold integrates with leading enterprise ERP systems via EDI for orders, inventory, and shipping reconciliation across the depositor's order-to-cash and procure-to-pay processes.
      - name: Customer ERP Systems
        description: Americold can integrate its supply chain management systems (WMS, LMS, TMS, WES) with a customer's ERP system for seamless information flow.
  - type: JSON-LD
    url: https://raw.githubusercontent.com/api-evangelist/americold-realty-trust/refs/heads/main/json-ld/americold-realty-trust-context.jsonld
    title: Americold Realty Trust JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/americold-realty-trust/refs/heads/main/vocabulary/americold-realty-trust-vocabulary.yaml
    title: Americold Realty Trust Vocabulary
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
---
