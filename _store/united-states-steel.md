---
aid: united-states-steel
name: United States Steel
url: https://raw.githubusercontent.com/api-evangelist/united-states-steel/refs/heads/main/apis.yml
description: United States Steel Corporation (U.S. Steel) is an integrated steel producer headquartered in Pittsburgh, Pennsylvania, with major production operations in the United States and Central Europe. The company serves customers in automotive, construction, container, energy, and industrial markets with advanced high-strength steels, coated products, hot-rolled and cold-rolled coils, electrical steel, and tubular products. U.S. Steel provides digital customer tools through the SteelTrack platform for order management, inventory tracking, shipment history, and certified test reporting.
modified: '2026-05-03'
tags:
  - Steel
  - Manufacturing
  - Automotive
  - Construction
  - Energy
  - Supply Chain
apis:
  - name: U.S. Steel SteelTrack API
    description: SteelTrack is U.S. Steel's internet-based customer platform providing order status reporting, inventory tracking, shipment history, material release, and physical and chemical test reporting. The API enables ERP and supply chain integration for steel order management and quality documentation.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.ussteel.com/about-us/doing-business-with-u.-s.-steel
    baseURL: https://steeltrack.ussteel.com/api
    tags:
      - Steel
      - Supply Chain
      - Order Management
      - Manufacturing
    properties:
      - type: Documentation
        url: https://www.ussteel.com/about-us/doing-business-with-u.-s.-steel
      - type: OpenAPI
        url: openapi/united-states-steel-steeltrack-openapi.yml
      - type: JSONSchema
        url: json-schema/steeltrack-order-schema.json
        title: Order Schema
      - type: JSONSchema
        url: json-schema/steeltrack-shipment-schema.json
        title: Shipment Schema
      - type: JSONStructure
        url: json-structure/steeltrack-order-structure.json
        title: Order Structure
      - type: JSON-LD
        url: json-ld/united-states-steel-steeltrack-context.jsonld
      - type: Example
        url: examples/steeltrack-order-example.json
        title: Order Example
    aid: united-states-steel:steeltrack-api
common:
  - type: Website
    url: https://www.ussteel.com
  - type: Portal
    url: https://www.ussteel.com/customers/solutions
  - type: Documentation
    url: https://www.ussteel.com/about-us/doing-business-with-u.-s.-steel
  - type: SpectralRules
    url: rules/united-states-steel-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/supply-chain-management.yaml
    title: Supply Chain Management
  - type: Vocabulary
    url: vocabulary/united-states-steel-vocabulary.yaml
  - type: Features
    data:
      - name: Order Status Reporting
        description: Customizable reports on order availability and status across all U.S. Steel facilities.
      - name: Inventory Tracking
        description: On-demand inventory reporting filterable by OP, customer, PO, and part number with flexible sorting.
      - name: Shipment History
        description: Load history searchable by order item, part number, and PO with optional coil-level detail.
      - name: Certified Test Reports
        description: Physical, mechanical, and chemical test reports with electronic certification signatures.
      - name: 24/7 Availability
        description: SteelTrack platform operates 24 hours a day, 7 days a week with console dashboard and workflow guidance.
      - name: Multi-Facility Coverage
        description: Consolidated view across all U.S. Steel production facilities including Gary Works, Mon Valley, and Big River Steel.
      - name: Real-Time Updates
        description: New and updated test report information relayed throughout the day to the Test Reports System.
  - type: UseCases
    data:
      - name: ERP Integration
        description: Integrate SteelTrack order and shipment data directly into customer ERP systems for automated procurement workflows.
      - name: Quality Documentation
        description: Automate retrieval of certified mill test reports for compliance, quality audits, and material traceability.
      - name: Supply Chain Visibility
        description: Track steel coil status from order placement through production and delivery for manufacturing planning.
      - name: Inventory Planning
        description: Monitor available inventory and in-transit material to optimize material release and production scheduling.
      - name: Automotive Supplier Compliance
        description: Access physical and chemical test data to meet automotive OEM supplier quality requirements (PPAP, IMDS).
      - name: Shipment Reconciliation
        description: Reconcile received shipments against orders using coil-level shipping data for accounts payable processing.
  - type: Integrations
    data:
      - name: SAP
        description: SteelTrack data integrates with SAP ERP for automated purchase order management and goods receipt processing.
      - name: Oracle ERP
        description: Order and inventory data connects to Oracle ERP Cloud for supply chain and procurement workflows.
      - name: EDI
        description: Electronic Data Interchange for standard steel industry transaction sets including orders, shipment notices, and invoices.
      - name: Nippon Steel
        description: Technology partnership with Nippon Steel Corporation following acquisition for shared manufacturing intelligence.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
