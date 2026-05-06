---
aid: scaleops
name: ScaleOps
description: ScaleOps is an autonomous Kubernetes cost optimization and resource management platform that continuously manages cloud infrastructure resources in real-time based on actual workload behavior. ScaleOps eliminates the need for manual resource configuration by automatically right-sizing CPU, memory, and replica counts for containers and clusters. The platform integrates natively with AWS, GCP, Azure cost management tools and is deployed via a single Helm command. ScaleOps provides real-time, context-aware optimization for production Kubernetes environments without service disruption.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Azure
  - Cost Optimization
  - FinOps
  - GCP
  - Helm
  - Kubernetes
  - Resource Management
url: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scaleops:scaleops-platform-api
    name: ScaleOps Platform API
    description: The ScaleOps Platform API provides programmatic access to Kubernetes cost optimization features including workload resource recommendations, real-time optimization controls, cost monitoring dashboards, cluster configuration, and policy management. Installed via Helm chart into Kubernetes clusters.
    humanURL: https://scaleops.com/
    tags:
      - Automation
      - Cost Monitoring
      - FinOps
      - Kubernetes
      - Resource Optimization
      - Workloads
    properties:
      - type: Documentation
        url: https://docs.scaleops.com/
      - type: Getting Started
        url: https://docs.scaleops.com/
      - type: Helm Chart
        url: https://catalog.redhat.com/en/software/container-stacks/detail/66eaefc1fa4fb0aa5f835b90
common:
  - type: Website
    url: https://scaleops.com/
  - type: Documentation
    url: https://docs.scaleops.com/
  - type: GitHub
    url: https://github.com/scaleops-sh
  - type: Blog
    url: https://scaleops.com/blog/
  - type: Pricing
    url: https://scaleops.com/pricing/
  - type: Cost Monitoring
    url: https://scaleops.com/product/kubernetes-cost-monitoring/
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/vocabulary/scaleops-vocabulary.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/json-schema/scaleops-workload-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/scaleops/refs/heads/main/json-ld/scaleops-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
