---
aid: ternary
name: Ternary
description: Ternary is a multi-cloud FinOps platform providing cost visibility, anomaly detection, commitment management, forecasting, and Kubernetes cost allocation for cloud environments. Originally built for Google Cloud, Ternary now supports AWS, Azure, and other cloud providers through its Universal Spend Ledger, with a REST API for programmatic access to all platform capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Cost Management
  - Cost Optimization
  - FinOps
  - Google Cloud
  - Kubernetes
  - Multi-Cloud
url: https://raw.githubusercontent.com/api-evangelist/ternary/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: ternary:ternary-api
    name: Ternary API
    description: Ternary provides a REST API that exposes all platform capabilities programmatically. Customers can automate FinOps workflows, integrate cost data into CI/CD pipelines, trigger alerts based on spend thresholds, manage commitments, and generate reports. Authentication uses API keys generated from the platform.
    humanURL: https://ternary.app/
    tags:
      - Automation
      - Cloud Costs
      - Cost Management
      - FinOps
      - REST API
    properties:
      - type: Documentation
        url: https://docs.ternary.app/
      - type: API Reference
        url: https://docs.ternary.app/reference
      - type: Getting Started
        url: https://docs.ternary.app/docs/using-the-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ternary/refs/heads/main/openapi/ternary-openapi.yml
common:
  - type: Website
    url: https://ternary.app/
  - type: Documentation
    url: https://docs.ternary.app/
  - type: GCP Integration
    url: https://ternary.app/integrations/google-cloud-gcp/
  - type: Kubernetes
    url: https://ternary.app/integrations/kubernetes/
  - type: Blog
    url: https://ternary.app/blog/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/ternary/refs/heads/main/openapi/ternary-openapi.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ternary/refs/heads/main/vocabulary/ternary-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
