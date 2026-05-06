---
aid: cloudzero
url: https://raw.githubusercontent.com/api-evangelist/cloudzero/refs/heads/main/apis.yml
name: CloudZero
created: '2026-01-02'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
x-type: company
tags:
  - Budgets
  - Cloud Cost Management
  - Cost Allocation
  - Cost Optimization
  - FinOps
  - Telemetry
  - Unit Economics
description: CloudZero is a cloud cost intelligence and FinOps platform that automates the collection, allocation, and analysis of infrastructure spend to uncover waste and improve unit economics. The CloudZero API V2 is REST-oriented, uses API key authentication, and exposes endpoints for querying billing costs and dimensions, managing insights and budgets, sending unit metric and allocation telemetry, and ingesting cost data from any source via the AnyCost framework.
apis:
  - aid: cloudzero:api
    name: CloudZero API
    description: The CloudZero API V2 enables you to automate the collection, allocation, and analysis of your infrastructure spend. It provides endpoints for querying billing costs and dimensions, managing insights and budgets, sending unit metric and allocation telemetry data, and ingesting cost data from any source via the AnyCost framework.
    humanURL: https://docs.cloudzero.com/reference/introduction
    baseURL: https://api.cloudzero.com
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
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
      - type: Spectral
        url: rules/cloudzero-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/cloud-cost-finops.yaml
  - aid: cloudzero:billing
    name: CloudZero Billing API
    description: The Billing API exposes cost and dimension data for analysis. Endpoints under /v2/billing return cost rows over a date range with selectable dimensions (account, service, region, custom dimension) and metrics (real_cost, billed_cost). Pagination uses page and page_size query parameters.
    humanURL: https://docs.cloudzero.com/reference/billing
    baseURL: https://api.cloudzero.com/v2/billing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Billing
      - Cost Reporting
      - Dimensions
    properties:
      - type: Documentation
        url: https://docs.cloudzero.com/reference/billing
  - aid: cloudzero:insights
    name: CloudZero Insights API
    description: The Insights API stores and surfaces actionable cost insights and recommendations. Endpoints under /v2/insights support listing, creating, updating, and deleting insight records, including assigned owners, severity, status, and estimated savings.
    humanURL: https://docs.cloudzero.com/reference/insights
    baseURL: https://api.cloudzero.com/v2/insights
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Cost Optimization
      - Insights
      - Recommendations
    properties:
      - type: Documentation
        url: https://docs.cloudzero.com/reference/insights
  - aid: cloudzero:budgets
    name: CloudZero Budgets API
    description: The Budgets API manages cost-and-usage budgets, alerts, thresholds, and actuals tracking. Endpoints under /v2/budgets list, create, update, and delete budgets and surface current consumption against limits.
    humanURL: https://docs.cloudzero.com/reference/budgets
    baseURL: https://api.cloudzero.com/v2/budgets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Alerts
      - Budgets
      - FinOps
    properties:
      - type: Documentation
        url: https://docs.cloudzero.com/reference/budgets
  - aid: cloudzero:allocation-telemetry
    name: CloudZero Allocation Telemetry API
    description: Allocation Telemetry sends, edits, and deletes allocation telemetry data for splitting cloud cost across custom allocation dimensions. Endpoints under /v1/telemetry/allocation/{stream_name} support sum, replace, and delete operations against a named telemetry stream.
    humanURL: https://docs.cloudzero.com/reference/allocation-telemetry
    baseURL: https://api.cloudzero.com/v1/telemetry/allocation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Allocation
      - Cost Splitting
      - Telemetry
    properties:
      - type: Documentation
        url: https://docs.cloudzero.com/reference/allocation-telemetry
  - aid: cloudzero:unit-metric-telemetry
    name: CloudZero Unit Metric Telemetry API
    description: Unit Metric Telemetry ingests business metrics that drive unit-economics calculations (cost per customer, cost per transaction, cost per tenant). Endpoints under /v1/telemetry/{stream_name} support submitting records, deleting, and replacing values for named streams.
    humanURL: https://docs.cloudzero.com/reference/unit-metric-telemetry
    baseURL: https://api.cloudzero.com/v1/telemetry
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Telemetry
      - Unit Economics
      - Unit Metrics
    properties:
      - type: Documentation
        url: https://docs.cloudzero.com/reference/unit-metric-telemetry
  - aid: cloudzero:anycost
    name: CloudZero AnyCost API
    description: AnyCost ingests cost data from any source using the AnyCost Stream Adaptor and Common Bill Format (CBF). Endpoints under /v2/connections/billing/anycost/{connection_id}/billing_drops accept uploads of normalized billing drops alongside native AWS, Azure, and GCP integrations.
    humanURL: https://docs.cloudzero.com/reference/anycost
    baseURL: https://api.cloudzero.com/v2/connections/billing/anycost
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - AnyCost
      - Billing Drop
      - CBF
      - Common Bill Format
      - Ingestion
    properties:
      - type: Documentation
        url: https://docs.cloudzero.com/reference/anycost
common:
  - type: Website
    url: https://www.cloudzero.com/
  - type: Portal
    url: https://app.cloudzero.com/
  - type: Documentation
    url: https://docs.cloudzero.com/
  - type: Pricing
    url: https://www.cloudzero.com/pricing/
  - type: Status
    url: https://status.cloudzero.com/
  - type: GitHub
    url: https://github.com/Cloudzero
  - type: Terms of Service
    url: https://www.cloudzero.com/terms-of-service/
  - type: Privacy
    url: https://www.cloudzero.com/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
