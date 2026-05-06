---
aid: american-axle-and-manufacturing
name: American Axle and Manufacturing
description: American Axle & Manufacturing (AAM), now operating as Dauch Corporation following the February 2026 acquisition of Dowlais Group (GKN Automotive and GKN Powder Metallurgy), is a global Tier 1 automotive supplier designing, engineering, and manufacturing driveline and metal forming technologies for electric, hybrid, and internal combustion vehicles. AAM operates an iSupplier Portal for supplier communication, EDI integration for forecasts and releases, and the Demand AAM aftermarket parts portal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - Manufacturing
  - Driveline
  - Automotive Supplier
  - EDI
  - Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/american-axle-and-manufacturing/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: american-axle-and-manufacturing:isupplier-portal
    name: AAM iSupplier Portal
    description: The AAM iSupplier Portal provides suppliers access to DELFORS forecasts, DELJIT releases, standard purchase orders, payment status, bulletins, specifications, manuals, PPAP documents, and ASN (Advanced Shipping Notification) transmission. EDI integration is required for all AAM suppliers, with EDI or portal-based ASN submission mandatory at time of shipment.
    humanURL: https://www.aam.com/suppliers/doing-business-with-aam
    baseURL: https://www.aam.com
    tags:
      - Supply Chain
      - EDI
      - Supplier Portal
      - Automotive
    properties:
      - type: Documentation
        url: https://www.aam.com/suppliers/doing-business-with-aam
      - type: Portal
        url: https://www.aam.com/suppliers/doing-business-with-aam/isupplier-faq
  - aid: american-axle-and-manufacturing:demand-aam
    name: Demand AAM Aftermarket Parts Portal
    description: Demand AAM provides access to genuine AAM OE replacement driveline parts for the aftermarket. The portal serves automotive parts distributors and repair shops with OE-quality driveline components.
    humanURL: https://www.demandaam.com/
    baseURL: https://www.demandaam.com
    tags:
      - Aftermarket
      - Parts
      - Automotive
    properties:
      - type: Documentation
        url: https://www.demandaam.com/
      - type: Portal
        url: https://www.demandaam.com/
common:
  - type: Website
    url: https://www.aam.com/
  - type: Portal
    url: https://www.aam.com/suppliers
  - type: Features
    data:
      - name: EDI Integration
        description: Electronic Data Interchange (EDI) integration required for all AAM suppliers, supporting DELFORS forecasts, DELJIT releases, and ASN transmission at time of shipment.
      - name: iSupplier Portal
        description: Web-based supplier portal providing access to forecasts, purchase orders, payment status, bulletins, specifications, PPAP documents, and ASN creation tools.
      - name: Advanced Shipping Notification
        description: Mandatory ASN submission via EDI or portal at time of shipment providing visibility of in-transit material to AAM manufacturing facilities.
      - name: Electric Vehicle Driveline Technology
        description: Next-generation electric drive units, eDrive systems, and driveline components for battery electric and hybrid vehicle platforms.
      - name: GKN Automotive Integration
        description: Following the February 2026 acquisition of Dowlais Group, AAM (now Dauch Corporation) integrates GKN Automotive's ePowertrain and driveline portfolio.
  - type: UseCases
    data:
      - name: Supplier Collaboration
        description: Tier 2 and Tier 3 suppliers access forecasts, purchase orders, and payment status through the iSupplier Portal for supply chain coordination.
      - name: Shipment Management
        description: Suppliers submit Advanced Shipping Notifications via EDI or portal to provide in-transit material visibility to AAM plants.
      - name: Aftermarket Parts Distribution
        description: Automotive parts distributors and repair shops source genuine OE driveline replacement parts through Demand AAM.
  - type: Integrations
    data:
      - name: EDI Systems
        description: ANSI X12 and EDIFACT EDI transaction sets for forecast (DELFORS), just-in-time releases (DELJIT), and Advanced Shipping Notifications.
      - name: GKN Automotive
        description: Integration of GKN Automotive's ePowertrain and sideshaft technology following Dauch Corporation acquisition of Dowlais Group.
      - name: GKN Powder Metallurgy
        description: Integration of GKN Powder Metallurgy's sintered components business following the Dowlais Group acquisition.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
