---
aid: customs-computer-system
url: https://raw.githubusercontent.com/api-evangelist/customs-computer-system/refs/heads/main/apis.yml
apis:
- name: Customs Declaration API
  description: Submit and manage customs declarations for imports and exports.
  image: https://example.com/declaration-icon.png
  baseURL: https://api.customs.example.com/v1/declarations
  humanURL: https://customs-api.example.com/declarations
  tags:
  - Customs
  - Declarations
  - Export
  - Import
  - Trade
  properties:
  - type: X-OpenAPI
    url: https://api.customs.example.com/v1/declarations/openapi.json
  - type: X-Documentation
    url: https://docs.customs.example.com/declarations
  - type: X-Authentication
    url: https://docs.customs.example.com/auth
  - type: X-Pricing
    url: https://customs-api.example.com/pricing
  contact:
  - FN: API Support
    email: api-support@customs.example.com
    X-twitter: customsapi
- name: Tariff Classification API
  description: Query harmonized system codes and tariff rates.
  image: https://example.com/tariff-icon.png
  baseURL: https://api.customs.example.com/v1/tariffs
  humanURL: https://customs-api.example.com/tariffs
  tags:
  - Classification
  - Duties
  - HS Codes
  - Tariffs
  properties:
  - type: X-OpenAPI
    url: https://api.customs.example.com/v1/tariffs/openapi.json
  - type: X-Documentation
    url: https://docs.customs.example.com/tariffs
  - type: X-Rate-Limits
    url: https://docs.customs.example.com/rate-limits
  contact:
  - FN: API Support
    email: api-support@customs.example.com
- name: Customs Status Tracking API
  description: Track the status of customs declarations and clearances.
  image: https://example.com/tracking-icon.png
  baseURL: https://api.customs.example.com/v1/tracking
  humanURL: https://customs-api.example.com/tracking
  tags:
  - Clearance
  - Shipments
  - Status
  - Tracking
  properties:
  - type: X-OpenAPI
    url: https://api.customs.example.com/v1/tracking/openapi.json
  - type: X-Documentation
    url: https://docs.customs.example.com/tracking
  - type: X-Webhooks
    url: https://docs.customs.example.com/webhooks
  contact:
  - FN: API Support
    email: api-support@customs.example.com
- name: Trade Compliance API
  description: Verify trade compliance, sanctions, and restricted party screening.
  image: https://example.com/compliance-icon.png
  baseURL: https://api.customs.example.com/v1/compliance
  humanURL: https://customs-api.example.com/compliance
  tags:
  - Compliance
  - Regulations
  - Sanctions
  - Screening
  properties:
  - type: X-OpenAPI
    url: https://api.customs.example.com/v1/compliance/openapi.json
  - type: X-Documentation
    url: https://docs.customs.example.com/compliance
  - type: X-Terms-of-Service
    url: https://customs-api.example.com/terms
  contact:
  - FN: Compliance Team
    email: compliance@customs.example.com
name: Customs Computer System
tags:
- API
type: Contract
image: https://example.com/customs-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for interacting with customs computer systems for import/export declarations, tariff information, and trade compliance.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

