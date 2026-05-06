---
aid: vishay-intertechnology
name: Vishay Intertechnology
description: Vishay Intertechnology is one of the world's largest manufacturers of discrete semiconductors (diodes, rectifiers, MOSFETs, optoelectronics, selected ICs) and passive electronic components (resistors, inductors, capacitors). Vishay components are used in automotive, industrial, computing, consumer, telecommunications, military, aerospace, and medical applications. Component data is accessible via distributor APIs (Octopart/Nexar, DigiKey) and Vishay's own Parts Library (VPL) tool.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/vishay-intertechnology/refs/heads/main/apis.yml
tags:
  - Automotive
  - Capacitors
  - Diodes
  - Electronics
  - Industrial
  - MOSFETs
  - Manufacturing
  - Medical
  - Optoelectronics
  - Passive Components
  - Resistors
  - Semiconductors
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vishay-intertechnology:vishay-parts-data-via-octopart
    name: Vishay Parts Data via Octopart/Nexar API
    description: Access Vishay component data programmatically through the Octopart/Nexar API. Search for Vishay parts by part number or category, retrieve datasheets, specifications, pricing, and distributor inventory.
    humanURL: https://nexar.com/api
    tags:
      - Components
      - Search
      - Electronic Parts
      - Data
    properties:
      - type: Documentation
        url: https://nexar.com/api
      - type: ExternalAPI
        url: https://octopart.com/manufacturers/vishay
  - aid: vishay-intertechnology:vishay-parts-data-via-digikey
    name: Vishay Parts Data via DigiKey API
    description: Access Vishay component inventory, pricing, specifications, and datasheets through the DigiKey REST API. Enables integration of Vishay component data into BOM management and design tools.
    humanURL: https://developer.digikey.com/
    tags:
      - Components
      - Inventory
      - Electronic Parts
      - Data
    properties:
      - type: Documentation
        url: https://developer.digikey.com/
  - aid: vishay-intertechnology:vishay-parts-library
    name: Vishay Parts Library (VPL)
    description: The Vishay Parts Library (VPL) is a cross-reference resource that provides Vishay alternatives for industry reference designs, searchable by IC part number and manufacturer.
    humanURL: https://www.vishay.com/
    tags:
      - Parts Library
      - Cross-Reference
      - Electronic Parts
    properties:
      - type: Documentation
        url: https://www.vishay.com/
common:
  - type: Website
    url: https://www.vishay.com/
  - type: Documentation
    url: https://www.vishay.com/en/how/onlineliterature/online-libraries/
  - type: ProductCatalog
    url: https://www.vishay.com/en/product-selector/
  - type: JSONSchema
    url: json-schema/vishay-electronic-component-schema.json
  - type: JSON-LD
    url: json-ld/vishay-intertechnology-context.jsonld
  - type: Vocabulary
    url: vocabulary/vishay-intertechnology-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
