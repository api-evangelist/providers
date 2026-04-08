---
aid: cloudzero
url: https://raw.githubusercontent.com/api-evangelist/cloudzero/refs/heads/main/apis.yml
apis:
- aid: cloudzero:api
  name: CloudZero API
  description: The CloudZero API V2 enables you to automate the collection, allocation, and analysis of your infrastructure spend. It provides endpoints for querying billing costs and dimensions, managing insights and budgets, sending unit metric and allocation telemetry data, and ingesting cost data from any source via the AnyCost framework.
  humanURL: https://docs.cloudzero.com/reference/introduction
  baseURL: https://api.cloudzero.com
  tags:
  - Billing
  - Budgets
  - Cloud Costs
  - Cost Allocation
  - FinOps
  - Insights
  - Telemetry
  - Unit Economics
  properties:
  - type: Documentation
    url: https://docs.cloudzero.com/reference/introduction
  - type: OpenAPI
    url: openapi/cloudzero-api-openapi.yml
  - type: Authorization
    url: https://docs.cloudzero.com/reference/authorization
  - type: JSONSchema
    url: json-schema/cloudzero-cost.json
  - type: JSONSchema
    url: json-schema/cloudzero-insight.json
  - type: JSONSchema
    url: json-schema/cloudzero-budget.json
  - type: JSONSchema
    url: json-schema/cloudzero-telemetry-record.json
  - type: JSONSchema
    url: json-schema/cloudzero-billing-drop.json
  - type: JSONLD
    url: json-ld/cloudzero-context.jsonld
name: CloudZero
tags:
- Budgets
- Cloud Cost Management
- Cost Allocation
- Cost Optimization
- FinOps
- Telemetry
- Unit Economics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-07'
position: Consumer
description: Automate the collection, allocation, and analysis of your infrastructure spend to uncover waste and improve unit economics.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

