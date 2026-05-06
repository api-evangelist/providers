---
aid: opencost
name: OpenCost
description: An open source CNCF specification and reference implementation for real-time cost monitoring of Kubernetes infrastructure and cloud spending, enabling teams to measure, allocate, and optimize cloud costs across workloads.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Cost Management
  - CNCF
  - FinOps
  - Kubernetes
  - Observability
url: https://raw.githubusercontent.com/api-evangelist/opencost/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: opencost:opencost-api
    name: OpenCost API
    description: The OpenCost REST API exposes real-time and historical reporting of Kubernetes workload costs and underlying cloud infrastructure spend, including allocation, asset, and cloud cost endpoints.
    humanURL: https://www.opencost.io/docs/integrations/api
    baseURL: http://localhost:9003
    tags:
      - Kubernetes
      - FinOps
      - Cost Allocation
    properties:
      - type: Documentation
        url: https://www.opencost.io/docs/integrations/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/opencost/refs/heads/main/openapi/opencost-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/opencost/refs/heads/main/json-schema/opencost-allocation-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/opencost/refs/heads/main/json-schema/opencost-asset-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/opencost/refs/heads/main/json-schema/opencost-cloudcost-schema.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/opencost/refs/heads/main/json-ld/opencost-context.jsonld
common:
  - type: Website
    url: https://opencost.io/
  - type: Documentation
    url: https://www.opencost.io/docs/
  - type: GitHubOrganization
    url: https://github.com/opencost/opencost
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
