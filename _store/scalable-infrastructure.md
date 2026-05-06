---
name: Scalable Infrastructure
description: A subject-matter collection covering APIs, tools, and platforms for building and managing scalable cloud infrastructure. This topic encompasses compute, storage, networking, container orchestration, infrastructure as code (IaC), monitoring, and the major cloud providers (AWS, Azure, GCP, DigitalOcean) that power modern scalable systems.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Cloud Infrastructure
  - Compute
  - DevOps
  - Infrastructure as Code
  - Kubernetes
  - Networking
  - Scalability
  - Storage
apis:
  - name: AWS EC2 API
    description: Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud. The EC2 API manages instances, AMIs, security groups, VPCs, elastic IP addresses, placement groups, and auto-scaling groups. The most widely used compute API with a 31% global cloud market share.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://aws.amazon.com/ec2/
    baseUrl: https://ec2.amazonaws.com
    tags:
      - Amazon Web Services
      - Cloud
      - Compute
      - EC2
      - Infrastructure
      - Instances
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/ec2/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/amazonaws.com/ec2/2016-11-15/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/ec2/pricing/
      - type: Getting Started
        url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
      - type: SDK
        url: https://aws.amazon.com/developer/tools/
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - name: AWS VPC API
    description: Amazon Virtual Private Cloud (VPC) enables launching AWS resources in a logically isolated virtual network. The VPC API manages subnets, route tables, internet gateways, NAT gateways, VPC peering, PrivateLink, and network ACLs. Foundational networking for scalable AWS architectures.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://aws.amazon.com/vpc/
    baseUrl: https://ec2.amazonaws.com
    tags:
      - Amazon Web Services
      - Cloud
      - Infrastructure
      - Networking
      - Security
      - VPC
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/vpc/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/amazonaws.com/ec2/2016-11-15/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/vpc/pricing/
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - name: AWS EKS API
    description: Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service. The EKS API manages clusters, node groups, Fargate profiles, add-ons, identity providers, and access entries. Powers scalable containerized workloads on AWS with automatic Kubernetes control plane management.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://aws.amazon.com/eks/
    baseUrl: https://eks.amazonaws.com
    tags:
      - Amazon Web Services
      - Cloud
      - Containers
      - EKS
      - Kubernetes
      - Managed Service
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/eks/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/amazonaws.com/eks/2018-08-23/openapi.yaml
      - type: Pricing
        url: https://aws.amazon.com/eks/pricing/
      - type: Getting Started
        url: https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html
    contact:
      - type: Support
        url: https://aws.amazon.com/contact-us/
  - name: Google Compute Engine API
    description: Google Compute Engine provides virtual machines running in Google's infrastructure. The API manages instances, machine types, disks, snapshots, networks, firewall rules, and managed instance groups. Includes powerful autoscaler and load balancing integration. Google Cloud holds ~12% global cloud market share.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://cloud.google.com/compute
    baseUrl: https://compute.googleapis.com/compute/v1
    tags:
      - Cloud
      - Compute
      - Google Cloud
      - Infrastructure
      - Instances
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://cloud.google.com/compute/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/googleapis.com/compute/v1/openapi.yaml
      - type: Pricing
        url: https://cloud.google.com/compute/pricing
      - type: SDK
        url: https://cloud.google.com/sdk/docs
    contact:
      - type: Support
        url: https://cloud.google.com/support
  - name: Google Kubernetes Engine API
    description: Google Kubernetes Engine (GKE) is a managed, production-ready Kubernetes service with auto-upgrade, auto-repair, cluster autoscaling, Workload Identity, and Autopilot mode. The GKE API manages clusters, node pools, and operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://cloud.google.com/kubernetes-engine
    baseUrl: https://container.googleapis.com/v1
    tags:
      - Cloud
      - Containers
      - GKE
      - Google Cloud
      - Kubernetes
      - Managed Service
    properties:
      - type: Documentation
        url: https://cloud.google.com/kubernetes-engine/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/googleapis.com/container/v1/openapi.yaml
      - type: Pricing
        url: https://cloud.google.com/kubernetes-engine/pricing
    contact:
      - type: Support
        url: https://cloud.google.com/support
  - name: Azure Resource Manager API
    description: Azure Resource Manager (ARM) is the deployment and management service for Azure. The REST API provides a consistent way to create, update, delete, and manage Azure resources across all services including VMs, storage, networking, and databases. Microsoft Azure holds ~28% global cloud market share.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview
    baseUrl: https://management.azure.com
    tags:
      - Azure
      - Cloud
      - Infrastructure
      - Management
      - Microsoft
      - Resource Management
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/resources/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/resources/resource-manager/Microsoft.Resources/stable/2023-07-01/resources.json
      - type: SDK
        url: https://learn.microsoft.com/en-us/azure/developer/
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
  - name: Azure AKS API
    description: Azure Kubernetes Service (AKS) simplifies deploying, managing, and scaling containerized applications using Kubernetes. The AKS API manages clusters, agent pools, node pools, maintenance configurations, and trusted access bindings.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://learn.microsoft.com/en-us/azure/aks/
    baseUrl: https://management.azure.com
    tags:
      - AKS
      - Azure
      - Cloud
      - Containers
      - Kubernetes
      - Managed Service
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/aks/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2024-01-01/managedClusters.json
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
  - name: DigitalOcean API
    description: DigitalOcean's developer-friendly cloud platform API manages Droplets (VMs), Kubernetes clusters, databases, object storage (Spaces), load balancers, VPCs, firewalls, and app platform deployments. Known for simplicity, transparent pricing, and developer experience for digital-native applications.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanUrl: https://www.digitalocean.com/
    baseUrl: https://api.digitalocean.com/v2
    tags:
      - Cloud
      - Compute
      - Developer-Friendly
      - DigitalOcean
      - Infrastructure
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.digitalocean.com/reference/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/digitalocean/openapi/main/specification/DigitalOcean-public.v2.yaml
      - type: Pricing
        url: https://www.digitalocean.com/pricing
      - type: Getting Started
        url: https://docs.digitalocean.com/products/getting-started/
      - type: SDK
        url: https://github.com/digitalocean/doctl
    contact:
      - type: Support
        url: https://www.digitalocean.com/support/
      - type: Community
        url: https://www.digitalocean.com/community
  - name: Terraform Registry API
    description: The Terraform Registry API provides access to infrastructure-as-code (IaC) modules and providers. HashiCorp Terraform is the leading IaC tool for provisioning and managing cloud infrastructure in a declarative, version-controlled way. Critical to scalable infrastructure automation workflows.
    image: https://registry.terraform.io/images/logo/logo_vertical_dark.svg
    humanUrl: https://developer.hashicorp.com/terraform
    baseUrl: https://registry.terraform.io/v1
    tags:
      - Infrastructure as Code
      - IaC
      - Open Source
      - Provisioning
      - Terraform
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/terraform/docs
      - type: GitHub
        url: https://github.com/hashicorp/terraform
      - type: API Reference
        url: https://developer.hashicorp.com/terraform/cloud-docs/api-docs
      - type: Registry
        url: https://registry.terraform.io/
    contact:
      - type: Community
        url: https://discuss.hashicorp.com/c/terraform-core/
  - name: Pulumi Cloud API
    description: Pulumi is a modern infrastructure as code platform that uses general-purpose programming languages (TypeScript, Python, Go, C#, Java, YAML). The Pulumi Cloud API manages stacks, deployments, environments, and audit logs. Alternative to Terraform with full-language programming model.
    image: https://www.pulumi.com/logos/brand/avatar/logo-on-white.png
    humanUrl: https://www.pulumi.com/
    baseUrl: https://api.pulumi.com/api
    tags:
      - Cloud
      - Infrastructure as Code
      - IaC
      - Open Source
      - Provisioning
      - Pulumi
    properties:
      - type: Documentation
        url: https://www.pulumi.com/docs/
      - type: GitHub
        url: https://github.com/pulumi/pulumi
      - type: API Reference
        url: https://www.pulumi.com/docs/pulumi-cloud/cloud-rest-api/
      - type: Pricing
        url: https://www.pulumi.com/pricing/
    contact:
      - type: Community
        url: https://slack.pulumi.com/
      - type: GitHub Issues
        url: https://github.com/pulumi/pulumi/issues
common:
  - type: GitHub Organization
    url: https://github.com/hashicorp
  - type: CNCF Landscape
    url: https://landscape.cncf.io/card-mode?category=provisioning
  - type: Blog
    url: https://www.cncf.io/blog/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/json-schema/scalable-infrastructure-compute-instance-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/json-schema/scalable-infrastructure-kubernetes-cluster-schema.json
  - type: JSONLd
    url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/json-ld/scalable-infrastructure-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/vocabulary/scalable-infrastructure-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: kin@apievangelist.com
    url: https://apievangelist.com
include:
  - name: Scalability APIs
    url: https://raw.githubusercontent.com/api-evangelist/scalability/refs/heads/main/apis.yml
  - name: Scalable Architecture
    url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/refs/heads/main/apis.yml
---
