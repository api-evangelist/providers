---
aid: vantage
url: https://raw.githubusercontent.com/api-evangelist/vantage/refs/heads/main/apis.yml
apis:
- aid: vantage:cost-management-api
  name: Vantage Cost Management API
  tags:
  - Anomaly Detection
  - Budgets
  - Cloud Costs
  - Cost Reports
  - Dashboards
  - FinOps
  humanURL: https://docs.vantage.sh/api
  properties:
  - url: https://vantage.readme.io/reference/general
    type: Documentation
  - url: openapi/vantage-cost-management-api-openapi.yml
    type: OpenAPI
  - url: https://api.vantage.sh/v2/oas_v3.json
    type: OpenAPI
  - url: https://api.vantage.sh/v2/swagger.json
    type: Swagger
  - url: json-schema/cost-report.json
    type: JSONSchema
  - url: json-schema/cost.json
    type: JSONSchema
  - url: json-schema/folder.json
    type: JSONSchema
  - url: json-schema/dashboard.json
    type: JSONSchema
  - url: json-schema/saved-filter.json
    type: JSONSchema
  - url: json-schema/workspace.json
    type: JSONSchema
  - url: json-schema/team.json
    type: JSONSchema
  - url: json-schema/access-grant.json
    type: JSONSchema
  - url: json-schema/budget-alert.json
    type: JSONSchema
  - url: json-schema/anomaly-alert.json
    type: JSONSchema
  - url: json-schema/recommendation.json
    type: JSONSchema
  - url: json-schema/segment.json
    type: JSONSchema
  - url: json-schema/integration.json
    type: JSONSchema
  - url: json-schema/managed-account.json
    type: JSONSchema
  - url: json-schema/cost-provider.json
    type: JSONSchema
  - url: json-schema/business-metric.json
    type: JSONSchema
  - url: json-schema/resource-report.json
    type: JSONSchema
  - url: json-schema/resource.json
    type: JSONSchema
  - url: json-schema/network-flow-report.json
    type: JSONSchema
  - url: json-schema/financial-commitment-report.json
    type: JSONSchema
  - url: json-schema/kubernetes-efficiency-report.json
    type: JSONSchema
  - url: json-ld/vantage-context.jsonld
    type: JSONLD
  description: The Vantage Cost Management API (v2) provides programmatic access to cloud cost data and enables automation of cost management workflows. Create and manage Cost Reports, Folders, Dashboards, Saved Filters, Teams, Budgets, Anomaly Alerts, Business Metrics, Network Flow Reports, Financial Commitment Reports, Resource Reports, Segments, Integrations, and more. Supports the Vantage Query Language (VQL) for filtering cost data across multiple cloud providers.
  baseURL: https://api.vantage.sh/v2
- aid: vantage:cloud-pricing-api
  name: Vantage Cloud Pricing API
  tags:
  - AWS
  - Azure
  - Cloud Pricing
  - GCP
  - Infrastructure Pricing
  humanURL: https://docs.vantage.sh/api
  properties:
  - url: https://vantage.readme.io/reference/general
    type: Documentation
  - url: openapi/vantage-cloud-pricing-api-openapi.yml
    type: OpenAPI
  - url: https://api.vantage.sh/v1/swagger.json
    type: Swagger
  - url: json-schema/provider.json
    type: JSONSchema
  - url: json-schema/service.json
    type: JSONSchema
  - url: json-schema/product.json
    type: JSONSchema
  - url: json-schema/price.json
    type: JSONSchema
  - url: json-ld/vantage-context.jsonld
    type: JSONLD
  description: The Vantage Cloud Pricing API (v1) provides programmatic access to cloud infrastructure pricing data across multiple providers including AWS, Azure, and GCP. Query providers, services, products, and prices to retrieve up-to-date pricing information for cloud infrastructure. The API is free for all registered Vantage users.
  baseURL: https://api.vantage.sh/v1
name: Vantage
tags:
- Budgets
- Cloud Pricing
- Cost Management
- Costs
- FinOps
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://www.vantage.sh/
  name: 'Vantage: Multi Cloud Cost Management & Optimization Tool'
  type: Website
  description: 'null'
- url: https://www.vantage.sh/integrations
  name: Integrations | Vantage
  type: Integrations
  description: 'null'
- url: https://docs.vantage.sh/
  name: Vantage Documentation - Vantage
  type: Documentation
  description: 'null'
- url: https://www.vantage.sh/blog
  name: Blog | Vantage
  type: Blog
  description: 'null'
- url: https://www.vantage.sh/pricing
  name: Pricing | Vantage
  type: Pricing
  description: 'null'
- url: https://www.vantage.sh/about
  name: About Vantage | Vantage
  type: About
  description: 'null'
- url: https://www.vantage.sh/vantage-partners
  name: Partners | Vantage
  type: Partners
  description: 'null'
- url: https://docs.vantage.sh/changelog
  name: Vantage Changelog - Vantage
  type: ChangeLog
  description: 'null'
- url: https://docs.vantage.sh/getting_started
  name: Quickstart - Vantage
  type: GettingStarted
  description: 'null'
created: '2026-01-02'
modified: '2026-04-07'
position: Consuming
description: Vantage is a cloud cost management platform designed for modern engineering teams to monitor, optimize, and control their cloud infrastructure spending across multiple providers. The platform helps companies identify immediate cost savings through features like automated purchasing of savings plans, cost recommendations, and Kubernetes rightsizing, while also preventing future cost overruns with anomaly detection, custom alerts, and budget tracking.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

