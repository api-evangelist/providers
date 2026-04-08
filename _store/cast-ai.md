---
aid: cast-ai
url: https://raw.githubusercontent.com/api-evangelist/cast-ai/refs/heads/main/apis.yml
apis:
- aid: cast-ai:kubernetes-cost-optimization-api
  name: CAST AI Kubernetes Cost Optimization API
  tags:
  - Autoscaling
  - Clusters
  - Cost Optimization
  - Hibernation
  - Kubernetes
  - LLM
  - Metrics
  - Node Templates
  - Nodes
  - Policies
  - Pricing
  - Rebalancing
  - Security
  - Workloads
  humanURL: https://docs.cast.ai/docs/api
  properties:
  - url: https://docs.cast.ai/docs/api
    type: Documentation
  - url: openapi/cast-ai-kubernetes-cost-optimization-openapi.yml
    type: OpenAPI
  - url: https://api.cast.ai/v1/spec/
    type: Swagger
  - url: https://docs.cast.ai/docs/authentication
    type: Authentication
  - url: json-schema/cluster.json
    type: JSONSchema
  - url: json-schema/node.json
    type: JSONSchema
  - url: json-schema/node-template.json
    type: JSONSchema
  - url: json-schema/workload.json
    type: JSONSchema
  - url: json-schema/rebalancing-schedule.json
    type: JSONSchema
  - url: json-schema/cost-report.json
    type: JSONSchema
  - url: json-ld/cast-ai-context.jsonld
    type: JSONLD
  description: The CAST AI REST API provides comprehensive access to the Kubernetes cost optimization platform, including cluster management, autoscaling policies, node configuration and templates, workload optimization, scheduled rebalancing, cost reporting, security insights, hibernation schedules, and AI enabler functionality. The API uses API key authentication and is available at api.cast.ai.
name: CAST AI
tags:
- Autoscaling
- Cloud Infrastructure
- Cost Optimization
- DevOps
- Kubernetes
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/swagger-ui-n0PWZL5D.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CAST AI is a Kubernetes cost optimization and automation platform that provides APIs for managing clusters, autoscaling, node configuration, workload optimization, cost reporting, security insights, and more. The platform continuously monitors Kubernetes clusters and optimizes them for cost efficiency using autoscaling, spot instance automation, bin packing, and other techniques. Everything available in the console UI is also accessible via the REST API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

