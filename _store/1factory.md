---
aid: 1factory
url: https://raw.githubusercontent.com/api-evangelist/1factory/refs/heads/main/apis.yml
name: 1Factory
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Data Collection
  - Manufacturing
  - Monitoring
  - Quality
description: 1Factory is a leading provider of quality management software solutions for manufacturing companies. The platform helps businesses streamline their operations, improve efficiency, and ensure product quality at every stage of the production process. Features include real-time monitoring, automated data collection, advanced analytics, and integration with ERP and PLM systems via a REST API.
created: '2025-02-08'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: 1factory:1factory
    name: 1Factory API
    tags:
      - Manufacturing
      - Quality
      - Inspections
    humanURL: https://www.1factory.com/api-doc/index.html
    baseURL: https://www.1factory.com/api/v1
    properties:
      - url: https://www.1factory.com/api-doc/index.html
        type: Documentation
      - url: openapi/1factory-openapi.json
        type: OpenAPI
      - url: json-schema/1factory-part-master-schema.json
        type: JSONSchema
      - url: json-schema/1factory-inspection-schema.json
        type: JSONSchema
      - url: json-schema/1factory-plan-schema.json
        type: JSONSchema
      - url: json-schema/1factory-fai-schema.json
        type: JSONSchema
      - url: json-schema/1factory-capa-schema.json
        type: JSONSchema
      - url: json-schema/1factory-ncr-schema.json
        type: JSONSchema
      - url: json-schema/1factory-complaint-schema.json
        type: JSONSchema
      - url: json-schema/1factory-supplier-schema.json
        type: JSONSchema
    description: This API allows you to create and query a number of objects in your 1Factory account. The API accepts and returns request and response bodies as JSON, using UTF-8 encoding. Supports part master management, manufacturing and receiving inspections, supplier quality, first article inspections (FAI), and quality management system records (NCRs, CAPAs, complaints).
common:
  - type: Website
    url: https://www.1factory.com/
  - type: Documentation
    url: https://www.1factory.com/api-doc/index.html
  - type: Security
    url: https://www.1factory.com/technical-overview.html
  - type: Support
    url: https://1factoryhelp.zendesk.com/hc/en-us
  - type: TermsOfService
    url: https://www.1factory.com/resources/TOS%20May%2020%202021.pdf
  - type: RateLimits
    url: https://www.1factory.com/api-doc/index.html
    data:
      - name: Minute Limit
        description: 60 requests per minute
      - name: Daily Limit
        description: 1000 requests per day
  - type: SpectralRules
    url: rules/1factory-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/1factory-quality-management.yaml
  - type: Vocabulary
    url: vocabulary/1factory-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/1factory-context.jsonld
  - type: Features
    data:
      - name: Manufacturing Quality Control
        description: Factory floor quality control, inspection planning, and statistical process control (SPC)
      - name: Quality Management System (QMS)
        description: Document control, training management, audits, and compliance workflows
      - name: Supplier Quality Management
        description: Vendor oversight, incoming inspection management, and supplier corrective actions
      - name: First Article Inspection (FAI)
        description: Automated drawing ballooning and AS9102-compliant first article inspection
      - name: Real-Time Analytics
        description: Real-time quality analytics and audit-ready reporting dashboards
      - name: CMM Data Integration
        description: Automatic import of CMM measurement data with SPC analysis
      - name: ERP/PLM Integration
        description: API-based integration with ERP and PLM systems for part and work order sync
  - type: UseCases
    data:
      - name: Manufacturing Inspection
        description: Create and track manufacturing inspections with measurement data and SPC analysis
      - name: Supplier Qualification
        description: Manage supplier certifications, conduct receiving inspections, and track supplier CAPAs
      - name: Non-Conformance Management
        description: Log, track, and resolve non-conformances, CAPAs, and customer complaints
      - name: First Article Inspection
        description: Conduct and document AS9102 first article inspections for aerospace and defense
      - name: ERP Data Sync
        description: Synchronize part master data, work orders, and inspection results with ERP systems
  - type: Integrations
    data:
      - name: ERP Systems
        description: Sync part master data, work orders, and inspection records with ERP platforms
      - name: PLM Systems
        description: Connect with PLM systems for design-to-manufacturing quality continuity
      - name: CMM Equipment
        description: Auto-import measurement data from CMM equipment directly into inspections
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
