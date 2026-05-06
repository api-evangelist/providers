---
aid: north-cloud
name: North.Cloud
description: North.Cloud delivers real-time savings, automated FinOps, and dynamic optimization across AWS and GCP. The platform's public API enables programmatic ingestion and retrieval of cost unit data so teams can integrate unit economics, allocation, and chargeback reporting into their own systems.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FinOps
  - Cloud Cost Management
  - AWS
  - GCP
  - Cost Optimization
  - Cost Units
created: '2026-01-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/north-cloud/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: north-cloud:north-cloud
    name: North.Cloud Public API
    description: Programmatic access to push and retrieve cost unit data for FinOps and cloud cost optimization workflows across AWS and GCP.
    humanURL: https://www.north.cloud/
    baseURL: https://api.north.cloud
    tags:
      - FinOps
      - Cost Units
      - Cloud Cost
    properties:
      - type: Documentation
        url: https://docs.north.cloud/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/north-cloud/refs/heads/main/openapi/north-cloud-openapi.yml
common:
  - type: Website
    url: https://www.north.cloud/
  - type: Documentation
    url: https://docs.north.cloud/
  - type: Application
    url: https://app.north.cloud/
  - type: Security
    url: https://docs.north.cloud/security
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
