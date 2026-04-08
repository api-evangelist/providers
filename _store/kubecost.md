---
aid: kubecost
url: https://raw.githubusercontent.com/api-search/kubecost/refs/heads/main/apis.yml
apis:
- aid: kubecost:allocation-api
  name: Kubecost Allocation API
  tags:
  - Cost Allocation
  - Kubernetes
  - Monitoring
  humanURL: https://docs.kubecost.com/apis/monitoring-apis/api-allocation
  properties:
  - url: https://docs.kubecost.com/apis/monitoring-apis/api-allocation
    type: Documentation
  - url: openapi/kubecost-allocation-openapi.yml
    type: OpenAPI
  - url: json-schema/allocation.json
    type: JSONSchema
  - url: json-ld/kubecost-context.jsonld
    type: JSONLD
  description: The Allocation API retrieves cost allocation information for any Kubernetes concept, such as cost by namespace, label, deployment, service, and more. It is directly integrated with the Kubecost ETL caching layer and CSV pipeline so it can scale for large clusters.
- aid: kubecost:assets-api
  name: Kubecost Assets API
  tags:
  - Assets
  - Kubernetes
  - Monitoring
  humanURL: https://docs.kubecost.com/apis/monitoring-apis/assets-api
  properties:
  - url: https://docs.kubecost.com/apis/monitoring-apis/assets-api
    type: Documentation
  - url: openapi/kubecost-assets-openapi.yml
    type: OpenAPI
  - url: json-schema/asset.json
    type: JSONSchema
  - url: json-ld/kubecost-context.jsonld
    type: JSONLD
  description: The Assets API retrieves backing cost data broken down by individual Kubernetes assets in your cluster, such as nodes, disks, load balancers, and more. It also provides various aggregations of this data.
- aid: kubecost:cloud-cost-api
  name: Kubecost Cloud Cost API
  tags:
  - AWS
  - Azure
  - Cloud Cost
  - GCP
  - Monitoring
  humanURL: https://docs.kubecost.com/apis/monitoring-apis/cloud-cost-api
  properties:
  - url: https://docs.kubecost.com/apis/monitoring-apis/cloud-cost-api
    type: Documentation
  - url: openapi/kubecost-cloud-cost-openapi.yml
    type: OpenAPI
  - url: json-schema/cloud-cost.json
    type: JSONSchema
  - url: json-ld/kubecost-context.jsonld
    type: JSONLD
  description: The Cloud Cost API provides accurate cost information from your cloud service providers (CSPs), including AWS, Azure, and GCP. It offers multiple endpoints for querying, aggregating, and analyzing cloud costs.
- aid: kubecost:budget-api
  name: Kubecost Budget API
  tags:
  - Budget
  - Governance
  - Spending
  humanURL: https://docs.kubecost.com/apis/governance-apis/budget-api
  properties:
  - url: https://docs.kubecost.com/apis/governance-apis/budget-api
    type: Documentation
  - url: openapi/kubecost-budget-openapi.yml
    type: OpenAPI
  - url: json-schema/budget.json
    type: JSONSchema
  - url: json-schema/budget-action.json
    type: JSONSchema
  - url: json-ld/kubecost-context.jsonld
    type: JSONLD
  description: The Budget API allows you to create, update, and delete recurring budget rules to control your Kubernetes spending. Weekly and monthly budgets can be established on workloads to set limits on cost spend, with the option to configure alerts for reaching specified budget thresholds via email, Slack, or Microsoft Teams.
- aid: kubecost:forecast-api
  name: Kubecost Forecast API
  tags:
  - Cost Prediction
  - Forecast
  - Governance
  humanURL: https://docs.kubecost.com/apis/governance-apis/forecast-api
  properties:
  - url: https://docs.kubecost.com/apis/governance-apis/forecast-api
    type: Documentation
  - url: openapi/kubecost-forecast-openapi.yml
    type: OpenAPI
  - url: json-schema/forecast.json
    type: JSONSchema
  - url: json-ld/kubecost-context.jsonld
    type: JSONLD
  description: The Forecast API provides cost forecasting capabilities for Kubernetes workloads, allowing you to predict future spend based on historical cost data and trends.
- aid: kubecost:savings-api
  name: Kubecost Savings API
  tags:
  - Optimization
  - Right-Sizing
  - Savings
  humanURL: https://docs.kubecost.com/apis/savings-apis
  properties:
  - url: https://docs.kubecost.com/apis/savings-apis
    type: Documentation
  - url: openapi/kubecost-savings-openapi.yml
    type: OpenAPI
  - url: json-schema/savings-recommendation.json
    type: JSONSchema
  - url: json-ld/kubecost-context.jsonld
    type: JSONLD
  description: The Savings APIs provide cost optimization insights, including cluster-level potential savings estimates, recommendations for right-sizing clusters and containers, listing abandoned workloads, orphaned disks, and orphaned IP addresses.
name: Kubecost
tags:
- Cloud Cost
- Cost Monitoring
- Kubernetes
- Optimization
- Spending
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-13'
modified: '2026-04-07'
position: Consuming
description: Kubecost provides real-time cost monitoring and management for Kubernetes environments. Its APIs enable programmatic access to cost allocation data, asset costs, cloud provider spend, budget governance, cost forecasting, and savings recommendations for optimizing Kubernetes and cloud infrastructure spending.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

