---
aid: flexera
url: https://raw.githubusercontent.com/api-evangelist/spot/refs/heads/main/apis.yml
apis:
- aid: spot:administration-api
  name: Spot Administration API
  tags:
  - Access Control
  - Accounts
  - Administration
  - Cloud Credentials
  - Organizations
  - Users
  humanURL: https://docs.spot.io/api/
  baseURL: https://api.spotinst.io
  properties:
  - url: https://docs.spot.io/api/
    type: Documentation
  - url: openapi/spot-administration-api-openapi.yml
    type: OpenAPI
  - url: json-schema/organization.json
    type: JSONSchema
  - url: json-schema/account.json
    type: JSONSchema
  - url: json-schema/user.json
    type: JSONSchema
  - url: json-schema/access-policy.json
    type: JSONSchema
  - url: json-schema/subscription.json
    type: JSONSchema
  - url: json-ld/spot-context.jsonld
    type: JSONLD
  description: The Spot Administration API provides endpoints for managing organizations, accounts, users, access policies, cloud credentials, subscriptions, and event notifications within the Spot by Flexera platform. It enables programmatic control over user permissions, account setup, and cloud provider credential linking for AWS, Azure, and GCP.
- aid: spot:elastigroup-api
  name: Spot Elastigroup API
  tags:
  - Autoscaling
  - AWS
  - Azure
  - Compute
  - Elastigroup
  - EMR
  - GCP
  - Spot Instances
  humanURL: https://docs.spot.io/api/
  baseURL: https://api.spotinst.io
  properties:
  - url: https://docs.spot.io/api/
    type: Documentation
  - url: openapi/spot-elastigroup-api-openapi.yml
    type: OpenAPI
  - url: json-schema/elastigroup.json
    type: JSONSchema
  - url: json-ld/spot-context.jsonld
    type: JSONLD
  description: The Spot Elastigroup API enables programmatic management of Elastigroup compute groups across AWS, Azure, and GCP. Elastigroup simplifies and automates cloud infrastructure for scale-out applications, continuously analyzing resource usage and optimizing compute resources to ensure availability while leveraging the lowest-cost compute options including spot instances, reserved instances, and on-demand capacity.
- aid: spot:ocean-api
  name: Spot Ocean API
  tags:
  - AKS
  - Apache Spark
  - Autoscaling
  - Containers
  - ECS
  - EKS
  - GKE
  - Kubernetes
  - Ocean
  humanURL: https://docs.spot.io/api/
  baseURL: https://api.spotinst.io
  properties:
  - url: https://docs.spot.io/api/
    type: Documentation
  - url: openapi/spot-ocean-api-openapi.yml
    type: OpenAPI
  - url: json-schema/ocean-cluster.json
    type: JSONSchema
  - url: json-schema/virtual-node-group.json
    type: JSONSchema
  - url: json-ld/spot-context.jsonld
    type: JSONLD
  description: The Spot Ocean API provides programmatic management of Ocean Kubernetes clusters across AWS EKS, Azure AKS, GCP GKE, and Amazon ECS. Ocean is a serverless Kubernetes infrastructure engine that automatically manages and optimizes cloud infrastructure for containers, handling node provisioning, scaling, and cost optimization with intelligent use of spot instances, reserved capacity, and on-demand resources.
- aid: spot:eco-api
  name: Spot Eco API
  tags:
  - AWS
  - Azure
  - Commitments
  - Cost Optimization
  - FinOps
  - GCP
  - Reserved Instances
  - Savings Plans
  humanURL: https://docs.spot.io/api/
  baseURL: https://api.spotinst.io
  properties:
  - url: https://docs.spot.io/api/
    type: Documentation
  - url: openapi/spot-eco-api-openapi.yml
    type: OpenAPI
  - url: json-ld/spot-context.jsonld
    type: JSONLD
  description: The Spot Eco API provides programmatic access to cloud commitment management and optimization across AWS, Azure, and GCP. Eco automates the purchase, management, and optimization of reserved instances, savings plans, and committed use discounts to maximize cloud cost savings while maintaining flexibility.
- aid: spot:billing-engine-api
  name: Spot Billing Engine API
  tags:
  - Billing
  - Chargeback
  - Cost Allocation
  - Cost Intelligence
  - FinOps
  - Invoicing
  humanURL: https://docs.spot.io/api/
  baseURL: https://api.spotinst.io
  properties:
  - url: https://docs.spot.io/api/
    type: Documentation
  - url: openapi/spot-billing-engine-api-openapi.yml
    type: OpenAPI
  - url: json-ld/spot-context.jsonld
    type: JSONLD
  description: The Spot Billing Engine API provides programmatic access to cloud billing management, cost allocation, and invoicing capabilities. Billing Engine streamlines multi-cloud invoicing with intelligent cost allocation, chargeback and showback reporting, and comprehensive billing analytics across AWS, Azure, and GCP accounts.
name: Spot
tags:
- Autoscaling
- Cloud Infrastructure
- Containers
- Cost Optimization
- FinOps
- Kubernetes
- Spot Instances
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-02'
modified: '2026-04-07'
position: Consuming
description: Spot by Flexera provides cloud infrastructure automation and optimization solutions. The platform includes Elastigroup for compute workload management across spot, reserved, and on-demand instances, Ocean for Kubernetes and container infrastructure automation, and Eco for cloud commitment management. The Spot API enables programmatic control over all platform capabilities including administration, compute groups, Kubernetes clusters, and cost optimization.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

