---
aid: spot
name: Spot
description: Spot by Flexera provides cloud infrastructure automation and optimization solutions. The platform includes Elastigroup for compute workload management across spot, reserved, and on-demand instances, Ocean for Kubernetes and container infrastructure automation, and Eco for cloud commitment management. The Spot API enables programmatic control over all platform capabilities including administration, compute groups, Kubernetes clusters, and cost optimization.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/spot/refs/heads/main/apis.yml
created: '2026-01-02'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Autoscaling
  - Cloud Infrastructure
  - Containers
  - Cost Optimization
  - FinOps
  - Kubernetes
  - Spot Instances
apis:
  - aid: spot:administration-api
    name: Spot Administration API
    description: The Spot Administration API provides endpoints for managing organizations, accounts, users, access policies, cloud credentials, subscriptions, and event notifications within the Spot by Flexera platform. It enables programmatic control over user permissions, account setup, and cloud provider credential linking for AWS, Azure, and GCP.
    humanURL: https://docs.spot.io/api/
    baseURL: https://api.spotinst.io
    tags:
      - Access Control
      - Accounts
      - Administration
      - Cloud Credentials
      - Organizations
      - Users
    properties:
      - type: Documentation
        url: https://docs.spot.io/api/
      - type: OpenAPI
        url: openapi/spot-administration-api-openapi.yml
      - type: JSONSchema
        url: json-schema/organization.json
      - type: JSONSchema
        url: json-schema/account.json
      - type: JSONSchema
        url: json-schema/user.json
      - type: JSONSchema
        url: json-schema/access-policy.json
      - type: JSONSchema
        url: json-schema/subscription.json
      - type: JSONLD
        url: json-ld/spot-context.jsonld
      - type: JSONLD
        url: json-ld/spot-administration-context.jsonld
  - aid: spot:elastigroup-api
    name: Spot Elastigroup API
    description: The Spot Elastigroup API enables programmatic management of Elastigroup compute groups across AWS, Azure, and GCP. Elastigroup simplifies and automates cloud infrastructure for scale-out applications, continuously analyzing resource usage and optimizing compute resources to ensure availability while leveraging the lowest-cost compute options including spot instances, reserved instances, and on-demand capacity.
    humanURL: https://docs.spot.io/api/
    baseURL: https://api.spotinst.io
    tags:
      - Autoscaling
      - AWS
      - Azure
      - Compute
      - Elastigroup
      - EMR
      - GCP
      - Spot Instances
    properties:
      - type: Documentation
        url: https://docs.spot.io/api/
      - type: OpenAPI
        url: openapi/spot-elastigroup-api-openapi.yml
      - type: JSONSchema
        url: json-schema/elastigroup.json
      - type: JSONLD
        url: json-ld/spot-context.jsonld
      - type: JSONLD
        url: json-ld/spot-elastigroup-context.jsonld
  - aid: spot:ocean-api
    name: Spot Ocean API
    description: The Spot Ocean API provides programmatic management of Ocean Kubernetes clusters across AWS EKS, Azure AKS, GCP GKE, and Amazon ECS. Ocean is a serverless Kubernetes infrastructure engine that automatically manages and optimizes cloud infrastructure for containers, handling node provisioning, scaling, and cost optimization with intelligent use of spot instances, reserved capacity, and on-demand resources.
    humanURL: https://docs.spot.io/api/
    baseURL: https://api.spotinst.io
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
    properties:
      - type: Documentation
        url: https://docs.spot.io/api/
      - type: OpenAPI
        url: openapi/spot-ocean-api-openapi.yml
      - type: JSONSchema
        url: json-schema/ocean-cluster.json
      - type: JSONSchema
        url: json-schema/virtual-node-group.json
      - type: JSONLD
        url: json-ld/spot-context.jsonld
      - type: JSONLD
        url: json-ld/spot-ocean-context.jsonld
  - aid: spot:eco-api
    name: Spot Eco API
    description: The Spot Eco API provides programmatic access to cloud commitment management and optimization across AWS, Azure, and GCP. Eco automates the purchase, management, and optimization of reserved instances, savings plans, and committed use discounts to maximize cloud cost savings while maintaining flexibility.
    humanURL: https://docs.spot.io/api/
    baseURL: https://api.spotinst.io
    tags:
      - AWS
      - Azure
      - Commitments
      - Cost Optimization
      - FinOps
      - GCP
      - Reserved Instances
      - Savings Plans
    properties:
      - type: Documentation
        url: https://docs.spot.io/api/
      - type: OpenAPI
        url: openapi/spot-eco-api-openapi.yml
      - type: JSONLD
        url: json-ld/spot-context.jsonld
      - type: JSONLD
        url: json-ld/spot-eco-context.jsonld
  - aid: spot:billing-engine-api
    name: Spot Billing Engine API
    description: The Spot Billing Engine API provides programmatic access to cloud billing management, cost allocation, and invoicing capabilities. Billing Engine streamlines multi-cloud invoicing with intelligent cost allocation, chargeback and showback reporting, and comprehensive billing analytics across AWS, Azure, and GCP accounts.
    humanURL: https://docs.spot.io/api/
    baseURL: https://api.spotinst.io
    tags:
      - Billing
      - Chargeback
      - Cost Allocation
      - Cost Intelligence
      - FinOps
      - Invoicing
    properties:
      - type: Documentation
        url: https://docs.spot.io/api/
      - type: OpenAPI
        url: openapi/spot-billing-engine-api-openapi.yml
      - type: JSONLD
        url: json-ld/spot-context.jsonld
      - type: JSONLD
        url: json-ld/spot-billing-engine-context.jsonld
common:
  - type: GitHubOrganization
    url: https://github.com/spotinst
  - type: Documentation
    url: https://docs.spot.io/
  - type: APIReference
    url: https://docs.spot.io/api/
  - type: OpenAPI
    url: https://github.com/spotinst/openapi
  - type: Authentication
    url: https://docs.spot.io/administration/api/create-api-token
  - type: Blog
    url: https://spot.io/blog/
  - type: TermsOfService
    url: https://spot.io/terms-of-use/
  - type: Features
    data:
      - name: Elastigroup Compute Management
        description: Automated management of compute workloads across spot, reserved, and on-demand instances for optimal cost and availability.
      - name: Ocean Kubernetes Automation
        description: Serverless container infrastructure that automatically right-sizes and scales Kubernetes node pools using the lowest-cost compute.
      - name: Eco Commitment Optimization
        description: Automated purchase and management of reserved instances, savings plans, and committed use discounts across clouds.
      - name: Billing Engine
        description: Multi-cloud billing management with cost allocation, chargeback, showback, and invoicing analytics.
      - name: Multi-Cloud Support
        description: Unified management across AWS, Azure, and GCP with consistent APIs and optimization strategies.
      - name: Intelligent Autoscaling
        description: Predictive and reactive autoscaling that analyzes workload patterns to optimize resource provisioning.
      - name: Stateful Workload Management
        description: Support for stateful applications with persistent storage, ENI, and IP preservation during instance replacements.
  - type: UseCases
    data:
      - name: Cloud Cost Optimization
        description: Reduce cloud compute costs by up to 90% by leveraging spot instances with automated fallback to on-demand capacity.
      - name: Kubernetes Cost Management
        description: Optimize Kubernetes infrastructure costs with bin-packing, right-sizing, and intelligent node pool management.
      - name: FinOps Reporting
        description: Centralized cloud cost visibility with chargeback, showback, and commitment utilization reporting across teams.
      - name: Big Data Cost Reduction
        description: Run Apache Spark and EMR workloads on spot instances with automatic scaling and cost optimization.
      - name: Reserved Instance Management
        description: Automate the lifecycle of cloud commitments including purchasing, exchanging, and selling unused reservations.
      - name: Multi-Cloud Governance
        description: Unified access control, audit logging, and policy management across AWS, Azure, and GCP accounts.
  - type: Integrations
    data:
      - name: AWS
        description: Deep integration with EC2, EKS, ECS, EMR, Auto Scaling Groups, and Savings Plans for AWS workload optimization.
      - name: Azure
        description: Integration with Azure VMs, AKS, Virtual Machine Scale Sets, and Azure Reserved VM Instances.
      - name: Google Cloud
        description: Support for GCP Compute Engine, GKE, and Committed Use Discounts for Google Cloud optimization.
      - name: Kubernetes
        description: Native integration with EKS, AKS, GKE, and self-managed Kubernetes clusters through the Ocean controller.
      - name: Terraform
        description: Official Terraform provider for managing Elastigroup, Ocean, and Eco resources as infrastructure as code.
      - name: Jenkins
        description: Jenkins plugin for scaling CI/CD build agents dynamically using Elastigroup spot instances.
      - name: Ansible
        description: Ansible modules for automating Spot resource provisioning and configuration management.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
