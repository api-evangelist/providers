---
aid: perfectscale
name: PerfectScale
description: PerfectScale is a Kubernetes cost optimization platform providing autonomous scaling and resource rightsizing.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FinOps
  - Kubernetes
  - Cost Optimization
url: https://raw.githubusercontent.com/api-evangelist/perfectscale/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: perfectscale:perfectscale
    name: PerfectScale Public API
    description: PerfectScale provides a public API for managing Kubernetes cost optimization, cluster monitoring, workload metrics, and automation audit logs.
    humanURL: https://www.perfectscale.io/
    baseURL: https://api.app.perfectscale.io/public/v1
    tags:
      - FinOps
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.perfectscale.io/api/public-api.md
      - type: Getting Started
        url: https://docs.perfectscale.io/
      - type: OpenAPI
        url: openapi/perfectscale-perfectscale-openapi.yml
common:
  - type: Website
    url: https://www.perfectscale.io/
  - type: Documentation
    url: https://docs.perfectscale.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
