---
aid: turbonomic
name: IBM Turbonomic
description: IBM Turbonomic is an Application Resource Management (ARM) platform that uses AI-powered automation to continuously analyze and optimize application performance and cloud costs across hybrid and multi-cloud environments. Turbonomic provides a comprehensive REST API enabling programmatic access to resource management data, workload actions, markets, policies, groups, templates, and topology information. The platform integrates with AWS, Azure, GCP, Kubernetes, VMware, and dozens of APM and ITSM tools.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.ibm.com/products/turbonomic
tags:
  - Application Resource Management
  - Cloud Cost Optimization
  - Cloud Management
  - Hybrid Cloud
  - IBM
  - Kubernetes
  - Multi-Cloud
  - Workload Optimization
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
apis:
  - aid: turbonomic:turbonomic-rest-api
    name: Turbonomic REST API
    description: The Turbonomic REST API provides programmatic access to the Turbonomic Application Resource Management platform. It enables automation of resource optimization actions, querying of entities (VMs, containers, applications, storage), management of markets and policies, retrieval of statistics and analytics, group management, template administration, and topology exploration across hybrid cloud environments. The API uses bearer token authentication obtained via a login endpoint.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.ibm.com/docs/en/tarm/8.19.3?topic=reference-turbonomic-rest-api-endpoints
    baseURL: https://{turbonomic_host}/api/v3
    tags:
      - Actions
      - Application Resource Management
      - Automation
      - Cloud Cost Optimization
      - Entities
      - Groups
      - Markets
      - Policies
      - Statistics
      - Topology
      - Workload Optimization
    properties:
      - type: Documentation
        url: https://www.ibm.com/docs/en/tarm/8.19.3?topic=reference-turbonomic-rest-api-endpoints
      - type: SwaggerUI
        url: https://try.turbonomic.io/apidoc/
      - type: GettingStarted
        url: https://www.ibm.com/docs/en/tarm/8.13.0?topic=reference-getting-started-turbonomic-rest-api
      - type: Reference
        url: https://www.ibm.com/docs/en/tarm/8.19.3?topic=reference-turbonomic-rest-api-endpoints
      - type: OpenAPI
        url: openapi/turbonomic-rest-api-openapi.yml
      - type: KubernetesCRD
        url: crd/charts.helm.k8s.io_xls.yaml
    features:
      - name: AI-Powered Actions
        description: Retrieve, approve, and execute resource optimization actions recommended by Turbonomic's AI engine across VMs, containers, and cloud resources.
      - name: Entity Management
        description: Query and manage entities including virtual machines, containers, applications, storage, and cloud services across hybrid environments.
      - name: Market Analytics
        description: Access Turbonomic markets to retrieve projected states, action impacts, and optimization scenarios for capacity planning.
      - name: Policy Management
        description: Create and manage automation policies that govern how Turbonomic executes optimization actions for different entity types and scopes.
      - name: Statistics and Reporting
        description: Retrieve historical and projected statistics for resource utilization, cost metrics, and performance data across the managed environment.
      - name: Group Management
        description: Create and manage logical groups of entities for scoped policy application, reporting, and workflow automation.
      - name: Template Management
        description: Define and manage resource templates used for workload placement and hardware refresh planning.
      - name: Topology Discovery
        description: Explore the topology of managed environments including supply chains, dependencies, and infrastructure relationships.
    useCases:
      - name: Automated Right-Sizing
        description: Automate VM and container right-sizing actions to eliminate waste and ensure application performance SLAs.
      - name: Cloud Cost Optimization
        description: Continuously identify and execute cost-saving actions across AWS, Azure, GCP, and hybrid cloud environments.
      - name: Kubernetes Resource Optimization
        description: Optimize container resource limits and requests in Kubernetes clusters to reduce costs and prevent out-of-memory issues.
      - name: ITSM Integration
        description: Integrate Turbonomic action recommendations with ITSM platforms like ServiceNow to route actions through change management workflows.
      - name: Capacity Planning
        description: Use market simulations and statistics APIs to plan infrastructure capacity for future workload demands.
    integrations:
      - name: AWS
        description: Cloud resource management and optimization for EC2, RDS, ECS, and EKS.
        url: https://aws.amazon.com/marketplace/pp/prodview-5r3k3snu4ttnm
      - name: Microsoft Azure
        description: Cloud resource management and optimization for Azure VMs and AKS.
        url: https://www.ibm.com/products/turbonomic
      - name: Google Cloud
        description: GCP compute and GKE container optimization.
        url: https://www.ibm.com/products/turbonomic
      - name: Kubernetes
        description: Native Kubernetes integration via kubeturbo for pod and container optimization.
        url: https://github.com/turbonomic/kubeturbo
      - name: VMware
        description: vSphere VM right-sizing and datacenter optimization.
        url: https://www.ibm.com/products/turbonomic
      - name: HashiCorp Terraform
        description: Infrastructure-as-code optimization for cloud-defined workloads.
        url: https://www.ibm.com/new/announcements/ibm-turbonomic-with-hashicorp-terraform
      - name: ServiceNow
        description: ITSM integration for action change management and approval workflows.
        url: https://www.ibm.com/products/turbonomic
      - name: IBM Kubecost
        description: Container cost visibility integrated with Kubernetes optimization actions.
        url: https://www.ibm.com/products/turbonomic
common:
  - type: Website
    url: https://www.ibm.com/products/turbonomic
  - type: Documentation
    url: https://www.ibm.com/docs/en/tarm/8.19.3
  - type: SwaggerUI
    url: https://try.turbonomic.io/apidoc/
  - type: GettingStarted
    url: https://www.ibm.com/docs/en/tarm/8.13.0?topic=reference-getting-started-turbonomic-rest-api
  - type: GitHub Organization
    url: https://github.com/turbonomic
  - type: Blog
    url: https://www.ibm.com/blog/turbonomic/
  - type: Pricing
    url: https://www.ibm.com/products/turbonomic/pricing
  - type: Marketplace
    url: https://aws.amazon.com/marketplace/pp/prodview-5r3k3snu4ttnm
  - type: Support
    url: https://www.ibm.com/mysupport/s/topic/0TO0z000000ZnCCGA0/turbonomic-application-resource-management
  - type: Community
    url: https://developer.ibm.com/components/turbonomic/
  - type: Terms of Service
    url: https://www.ibm.com/terms
  - type: Privacy Policy
    url: https://www.ibm.com/privacy
  - type: OpenAPI
    url: openapi/turbonomic-rest-api-openapi.yml
  - type: KubernetesCRD
    url: crd/charts.helm.k8s.io_xls.yaml
  - type: Vocabulary
    url: vocabulary/turbonomic-vocabulary.yml
  - type: JSON-LD
    url: json-ld/turbonomic-context.jsonld
  - type: JSONSchema
    url: json-schema/turbonomic-entity-schema.json
  - type: JSONSchema
    url: json-schema/turbonomic-action-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
