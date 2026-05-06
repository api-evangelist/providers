---
aid: trabex
name: Trabex
description: Trabex is a trade compliance platform that provides automated export compliance, shipment management, restricted party screening, and Automated Export System (AES) filing services. Trabex offers APIs for integrating trade compliance workflows including shipment data ingestion, export documentation generation, financial reporting, and ancillary compliance data to help organizations manage global trade risk.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Compliance
  - Export Control
  - Logistics
  - Restricted Party Screening
  - Shipment Management
  - Trade Compliance
url: https://raw.githubusercontent.com/api-evangelist/trabex/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trabex:trade-compliance
    name: Trabex Trade Compliance API
    description: The Trabex Trade Compliance API provides programmatic access to export compliance automation including shipment data submission, export documentation generation, Automated Export System (AES) filing, and restricted party screening. The API enables organizations to integrate compliance workflows into logistics and ERP systems, supporting single shipments, batch screening, and continuous compliance operations.
    humanURL: https://apidocs.trabex.io/
    baseURL: https://api.trabex.io
    tags:
      - AES Filing
      - Compliance
      - Export Control
      - Logistics
      - Restricted Party Screening
      - Shipment Management
      - Trade
    properties:
      - type: Documentation
        url: https://apidocs.trabex.io/
      - type: OpenAPI
        url: openapi/trabex-trade-compliance-openapi.yml
      - type: JSONSchema
        url: json-schema/trabex-shipment-schema.json
      - type: JSONStructure
        url: json-structure/trabex-shipment-structure.json
      - type: JSONLd
        url: json-ld/trabex-context.jsonld
      - type: SpectralRules
        url: rules/trabex-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/export-compliance.yaml
      - type: Vocabulary
        url: vocabulary/trabex-vocabulary.yml
      - type: Support
        url: https://support.trabex.io/support/home
common:
  - type: Website
    url: https://trabex.io
  - type: Documentation
    url: https://apidocs.trabex.io/
  - type: Support
    url: https://support.trabex.io/support/home
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
