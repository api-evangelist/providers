---
aid: customs-brokerage
url: https://raw.githubusercontent.com/api-evangelist/customs-brokerage/refs/heads/main/apis.yml
apis:
- name: Customs Brokerage API
  description: Comprehensive API for customs brokerage services.
  baseURL: https://api.customsbroker.example.com/v1
  humanURL: https://customsbroker.example.com
  version: '1.0'
  tags:
  - Clearance
  - Customs
  - Declarations
  - Duties
  properties:
  - type: Documentation
    url: https://docs.customsbroker.example.com
  - type: OpenAPI
    url: https://api.customsbroker.example.com/openapi.json
  - type: Authentication
    url: https://docs.customsbroker.example.com/authentication
  - type: Pricing
    url: https://customsbroker.example.com/pricing
  - type: Support
    url: https://support.customsbroker.example.com
  - type: Status
    url: https://status.customsbroker.example.com
  - type: Terms of Service
    url: https://customsbroker.example.com/terms
  - type: Privacy Policy
    url: https://customsbroker.example.com/privacy
  endpoints:
  - name: Shipment Management
    description: Manage import/export shipments
    methods:
    - GET /shipments
    - POST /shipments
    - GET /shipments/{id}
    - PUT /shipments/{id}
    - DELETE /shipments/{id}
  - name: Customs Declarations
    description: Create and manage customs declarations
    methods:
    - GET /declarations
    - POST /declarations
    - GET /declarations/{id}
    - PUT /declarations/{id}
    - POST /declarations/{id}/submit
    - GET /declarations/{id}/status
  - name: Duty Calculations
    description: Calculate duties, taxes, and fees
    methods:
    - POST /calculations/duty
    - POST /calculations/tax
    - GET /calculations/{id}
    - POST /calculations/estimate
  - name: HS Code Lookup
    description: Search and validate Harmonized System codes
    methods:
    - GET /hscodes/search
    - GET /hscodes/{code}
    - POST /hscodes/classify
  - name: Document Management
    description: Upload and manage customs documents
    methods:
    - GET /documents
    - POST /documents/upload
    - GET /documents/{id}
    - DELETE /documents/{id}
    - GET /documents/{id}/download
  - name: Compliance Checks
    description: Validate compliance requirements
    methods:
    - POST /compliance/validate
    - GET /compliance/requirements
    - GET /compliance/sanctions-screening
    - POST /compliance/licenses/verify
  - name: Tracking
    description: Track shipment status and clearance progress
    methods:
    - GET /tracking/{shipmentId}
    - GET /tracking/{shipmentId}/timeline
    - POST /tracking/webhook
  - name: Tariff Information
    description: Access tariff rates and trade agreements
    methods:
    - GET /tariffs/rates
    - GET /tariffs/agreements
    - GET /tariffs/country/{countryCode}
  contact:
  - type: Email
    url: mailto:api@customsbroker.example.com
  - type: Support
    url: https://support.customsbroker.example.com/contact
name: Customs Brokerage
tags:
- Brokerage
- Compliance
- Customs
- Export
- Import
- Trade
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API for managing customs brokerage operations including clearance, declarations, duty calculations, and compliance documentation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

