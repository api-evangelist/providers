---
aid: argus-enterprise
url: https://raw.githubusercontent.com/api-evangelist/argus-enterprise/refs/heads/main/apis.yml
apis:
- name: Argus Enterprise Core API
  description: Core REST API for the ARGUS Enterprise platform providing programmatic access to commercial real estate investment management capabilities including property data, portfolio management, cash flow projections, valuations, tenants, leases, and reporting.
  image: https://www.altusgroup.com/wp-content/uploads/argus-logo.png
  baseURL: https://api.argusenterprise.com/v1
  humanURL: https://www.argusenterprise.com/api
  properties:
  - type: Documentation
    url: https://docs.argusenterprise.com/api/v1
  - type: OpenAPI
    url: https://api.argusenterprise.com/v1/openapi.json
  - type: Authentication
    url: https://docs.argusenterprise.com/api/authentication
  - type: OpenAPI
    url: openapi/argus-enterprise-core-openapi.yml
  contact:
  - FN: Argus API Support
    email: api-support@argusenterprise.com
    url: https://support.argusenterprise.com
  tags:
  - Analytics
  - Data Management
  - Enterprise
  - Leases
  - Portfolios
  - Properties
  - Reporting
  - Valuations
- name: Argus Webhook API
  description: Webhook service for the ARGUS Enterprise platform enabling real-time event notifications for property changes, valuation updates, lease events, portfolio modifications, and report completions.
  image: https://www.altusgroup.com/wp-content/uploads/argus-logo.png
  baseURL: https://webhooks.argusenterprise.com/v1
  humanURL: https://www.argusenterprise.com/webhooks
  properties:
  - type: Documentation
    url: https://docs.argusenterprise.com/webhooks
  - type: Schema
    url: https://webhooks.argusenterprise.com/v1/schema
  - type: OpenAPI
    url: openapi/argus-enterprise-webhooks-openapi.yml
  tags:
  - Events
  - Real-Time
  - Webhooks
name: Argus Enterprise
tags:
- Business Intelligence
- Commercial Real Estate
- Enterprise Software
- Valuation
type: Contract
image: https://www.altusgroup.com/wp-content/uploads/argus-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and integration points for the ARGUS Enterprise commercial real estate investment management and valuation platform by Altus Group.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

