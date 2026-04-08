---
aid: customs-procedures
url: https://raw.githubusercontent.com/api-evangelist/customs-procedures/refs/heads/main/apis.yml
apis:
- name: Customs Declaration API
  description: Submit and manage customs declarations for import and export shipments.
  image: https://example.com/declaration-api.png
  humanURL: https://customs.example.com/declaration-api
  baseURL: https://api.customs.example.com/v1/declarations
  tags:
  - Declarations
  - Export
  - Import
  - Submissions
  properties:
  - type: X-documentation
    url: https://docs.customs.example.com/declaration-api
  - type: X-openapi
    url: https://api.customs.example.com/declaration-api/openapi.json
  - type: X-postman-collection
    url: https://www.postman.com/customs/declaration-api
  - type: X-pricing
    url: https://customs.example.com/pricing/declaration-api
  contact:
  - FN: Customs API Support
    email: api-support@customs.example.com
    X-twitter: customs_api
- name: Tariff Classification API
  description: Look up HS codes, tariff rates, and duty calculations for imported goods.
  image: https://example.com/tariff-api.png
  humanURL: https://customs.example.com/tariff-api
  baseURL: https://api.customs.example.com/v1/tariffs
  tags:
  - Classification
  - Duties
  - Hs-Codes
  - Tariffs
  properties:
  - type: X-documentation
    url: https://docs.customs.example.com/tariff-api
  - type: X-openapi
    url: https://api.customs.example.com/tariff-api/openapi.json
  - type: X-postman-collection
    url: https://www.postman.com/customs/tariff-api
  - type: X-rate-limits
    url: https://customs.example.com/rate-limits
  contact:
  - FN: Tariff Support Team
    email: tariff-support@customs.example.com
- name: Trade Compliance API
  description: Verify licenses, sanctions, restricted parties, and trade compliance requirements.
  image: https://example.com/compliance-api.png
  humanURL: https://customs.example.com/compliance-api
  baseURL: https://api.customs.example.com/v1/compliance
  tags:
  - Compliance
  - Licenses
  - Sanctions
  - Screening
  properties:
  - type: X-documentation
    url: https://docs.customs.example.com/compliance-api
  - type: X-openapi
    url: https://api.customs.example.com/compliance-api/openapi.json
  - type: X-authentication
    url: https://docs.customs.example.com/authentication
  - type: X-status
    url: https://status.customs.example.com
  contact:
  - FN: Compliance Team
    email: compliance@customs.example.com
- name: Shipment Tracking API
  description: Track customs clearance status and shipment progress through customs procedures.
  image: https://example.com/tracking-api.png
  humanURL: https://customs.example.com/tracking-api
  baseURL: https://api.customs.example.com/v1/tracking
  tags:
  - Clearance
  - Shipments
  - Status
  - Tracking
  properties:
  - type: X-documentation
    url: https://docs.customs.example.com/tracking-api
  - type: X-openapi
    url: https://api.customs.example.com/tracking-api/openapi.json
  - type: X-webhooks
    url: https://docs.customs.example.com/webhooks
  contact:
  - FN: Tracking Support
    email: tracking@customs.example.com
- name: Customs Broker Integration API
  description: API for customs brokers to manage multiple clients and bulk declaration submissions.
  image: https://example.com/broker-api.png
  humanURL: https://customs.example.com/broker-api
  baseURL: https://api.customs.example.com/v1/broker
  tags:
  - Broker
  - Bulk-Operations
  - Multi-Client
  properties:
  - type: X-documentation
    url: https://docs.customs.example.com/broker-api
  - type: X-openapi
    url: https://api.customs.example.com/broker-api/openapi.json
  - type: X-authentication
    url: https://docs.customs.example.com/broker-authentication
  - type: X-terms-of-service
    url: https://customs.example.com/broker-terms
  contact:
  - FN: Broker Relations
    email: broker-support@customs.example.com
name: Customs Procedures
tags:
- Compliance
- Customs
- Declarations
- Export
- Import
- Tariffs
- Trade
type: Contract
image: https://example.com/customs-api-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs related to customs procedures, declarations, tariffs, and international trade compliance.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

