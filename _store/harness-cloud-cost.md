---
aid: harness-cloud-cost
name: Harness Cloud Cost Management
description: Harness Cloud Cost Management (CCM) provides intelligent cloud cost optimization with AI-driven recommendations, customizable cost perspectives, budgets, anomaly detection, and chargeback / showback through cost categories. CCM ingests cost data from AWS, Azure, GCP, and Kubernetes clusters and exposes a REST API on the Harness platform for FinOps automation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Anomaly Detection
  - Budgets
  - Cloud Cost Management
  - FinOps
  - Kubernetes
  - Recommendations
url: https://raw.githubusercontent.com/api-evangelist/harness-cloud-cost/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: harness-cloud-cost:harness-cloud-cost
    name: Harness Cloud Cost Management API
    description: The Harness CCM API provides programmatic access to cloud cost data, perspectives, budgets, anomaly detection, AI-driven recommendations, cost categories (chargeback / showback), and cloud connector configuration across AWS, Azure, GCP, and Kubernetes.
    humanURL: https://www.harness.io/products/cloud-cost
    baseURL: https://app.harness.io
    tags:
      - Cloud Cost Management
      - FinOps
    properties:
      - type: Documentation
        url: https://developer.harness.io/docs/cloud-cost-management
      - type: Getting Started
        url: https://developer.harness.io/docs/cloud-cost-management/get-started/overview
      - type: API Reference
        url: https://apidocs.harness.io/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/harness-cloud-cost/refs/heads/main/openapi/harness-cloud-cost-openapi.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/harness-cloud-cost/refs/heads/main/rules/harness-cloud-cost-rules.yml
common:
  - type: Website
    url: https://www.harness.io/products/cloud-cost
  - type: Documentation
    url: https://developer.harness.io/docs/cloud-cost-management
  - type: API Reference
    url: https://apidocs.harness.io/
  - type: Pricing
    url: https://www.harness.io/pricing
  - type: Status
    url: https://status.harness.io
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
