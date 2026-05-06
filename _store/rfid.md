---
aid: rfid
name: RFID
description: Radio-Frequency Identification (RFID) is an automatic identification technology that uses radio waves to read and capture information stored on a tag attached to an object. RFID powers supply chain visibility, inventory management, asset tracking, access control, and contactless payments. The RFID ecosystem includes hardware vendors (Zebra, Impinj, Alien Technology), software platforms (ClearStream, TagMatiks, Jetstream), and open standards (GS1 EPCIS, EPC Tag Data Standard, ISO 18000 series).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - RFID
  - IoT
  - Supply Chain
  - Inventory Management
  - Asset Tracking
  - GS1
  - EPCIS
url: https://raw.githubusercontent.com/api-evangelist/rfid/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rfid:zebra-rfid-data-services
    name: Zebra Data Services for RFID
    description: Zebra Technologies provides cloud-based REST APIs for managing RFID readers, collecting tag data, and integrating RFID intelligence into enterprise applications. Cloud Connect for RFID enables remote reader management and data collection via REST API.
    humanURL: https://developer.zebra.com/data-services-rfid-developer-guide
    baseURL: https://api.zebra.com
    tags:
      - RFID
      - Asset Tracking
      - Inventory
      - Zebra
    properties:
      - type: Documentation
        url: https://developer.zebra.com/data-services-rfid-developer-guide
      - type: Portal
        url: https://developer.zebra.com/products/rfid
  - aid: rfid:clearstream-rfid-api
    name: ClearStream RFID REST API
    description: ClearStream provides a RESTful API for RFID and Bluetooth Beacon technology, giving developers full control of RFID readers and gateways to integrate tag data into existing applications and websites.
    humanURL: https://www.clearstreamrfid.com/software/integrate/api/
    tags:
      - RFID
      - Bluetooth Beacon
      - Asset Tracking
      - REST API
    properties:
      - type: Documentation
        url: https://www.clearstreamrfid.com/software/integrate/api/
  - aid: rfid:impinj-itemsense-api
    name: Impinj ItemSense RAIN RFID API
    description: Impinj provides APIs for RAIN RFID reader management and item location data, enabling real-time item-level inventory visibility in retail, healthcare, and manufacturing environments.
    humanURL: https://developer.impinj.com/
    tags:
      - RFID
      - RAIN RFID
      - Retail
      - Healthcare
      - Impinj
    properties:
      - type: Documentation
        url: https://developer.impinj.com/
  - aid: rfid:gs1-epcis-api
    name: GS1 EPCIS API
    description: The Electronic Product Code Information Services (EPCIS) is GS1's standard for sharing supply chain visibility data. EPCIS 2.0 supports REST/HTTP and JSON-LD for capturing and querying RFID events including Object, Aggregation, Transaction, Transformation, and Association events.
    humanURL: https://www.gs1.org/standards/epcis
    tags:
      - GS1
      - EPCIS
      - Supply Chain
      - EPC
      - Standard
    properties:
      - type: Documentation
        url: https://www.gs1.org/standards/epcis
features:
  - name: Tag Reading
    description: Reading and decoding EPC/ISO RFID tags at item, case, and pallet levels
  - name: Reader Management
    description: Remote configuration, firmware update, and monitoring of RFID fixed and handheld readers
  - name: Event Capture
    description: EPCIS-compliant event capture for object events, aggregation events, and transaction events
  - name: Inventory Visibility
    description: Real-time item-level inventory counts and location tracking
  - name: Supply Chain Traceability
    description: End-to-end product journey tracking from manufacture to point of sale
  - name: Access Control
    description: RFID-based employee and visitor access management
useCases:
  - name: Retail Inventory Management
    description: Automated cycle counting and real-time inventory accuracy with item-level RFID
  - name: Supply Chain Visibility
    description: Track products through manufacturing, distribution, and retail using EPCIS events
  - name: Asset Tracking
    description: Track tools, equipment, and IT assets in real time across facilities
  - name: Healthcare Asset Management
    description: Track medical equipment, surgical kits, and pharmaceutical inventory
  - name: Access Control
    description: RFID-based building access, parking management, and visitor management
common:
  - type: Website
    url: https://developer.zebra.com/products/rfid
  - type: Website
    url: https://www.clearstreamrfid.com/
  - type: Website
    url: https://www.gs1.org/standards/epcis
  - type: Standard
    url: https://www.gs1.org/standards/epc-rfid-epcis-id-keys/epc-rfid-tds/1-12
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
