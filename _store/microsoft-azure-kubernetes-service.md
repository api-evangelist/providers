---
aid: microsoft-azure-kubernetes-service
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-kubernetes-service/refs/heads/main/apis.yml
apis:
- name: Azure Kubernetes Service REST API
  description: REST API for managing Azure Kubernetes Service clusters.
  image: https://azure.microsoft.com/images/aks-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/aks/
  baseURL: https://management.azure.com
  tags:
  - Containers
  - Kubernetes
  - Management
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/
  - type: OpenAPI
    url: openapi/azure-kubernetes-service-openapi.yml
  - type: OpenAPI
    url: https://github.com/Azure/azure-rest-api-specs/blob/main/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2023-10-01/managedClusters.json
  - type: Swagger
    url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/containerservice/resource-manager
  - type: JSONSchema
    url: json-schema/azure-kubernetes-service-cluster-schema.json
  - type: JSONLD
    url: json-ld/azure-kubernetes-service-context.jsonld
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/
  - type: SLA
    url: https://azure.microsoft.com/en-us/support/legal/sla/kubernetes-service/
  - type: Rate Limits
    url: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
  - type: Change Log
    url: https://github.com/Azure/AKS/blob/master/CHANGELOG.md
  - type: Release Notes
    url: https://learn.microsoft.com/en-us/azure/aks/release-tracker
  - type: SDK - Python
    url: https://learn.microsoft.com/en-us/python/api/overview/azure/mgmt-containerservice-readme
  - type: SDK - JavaScript
    url: https://learn.microsoft.com/en-us/javascript/api/overview/azure/container-service
  - type: SDK - .NET
    url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/resourcemanager.containerservice-readme
  - type: SDK - Java
    url: https://learn.microsoft.com/en-us/java/api/overview/azure/resourcemanager-containerservice-readme
  - type: SDK - Go
    url: https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/containerservice/armcontainerservice/v6
- name: Azure Kubernetes Service Managed Clusters API
  description: REST API for creating, updating, deleting, and managing AKS managed clusters including cluster configuration, upgrades, credentials, and run commands.
  image: https://azure.microsoft.com/images/aks-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/aks/managed-clusters
  baseURL: https://management.azure.com
  tags:
  - Clusters
  - Kubernetes
  - Management
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/
  - type: API Reference
    url: https://learn.microsoft.com/en-us/rest/api/aks/managed-clusters
  - type: OpenAPI
    url: openapi/azure-kubernetes-service-openapi.yml
  - type: OpenAPI
    url: https://github.com/Azure/azure-rest-api-specs/blob/main/specification/containerservice/resource-manager/Microsoft.ContainerService/aks/stable/2023-10-01/managedClusters.json
  - type: JSONSchema
    url: json-schema/azure-kubernetes-service-cluster-schema.json
  - type: JSONLD
    url: json-ld/azure-kubernetes-service-context.jsonld
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/
- name: Azure Kubernetes Service Agent Pools API
  description: REST API for creating, updating, deleting, and managing agent pools (node pools) within AKS managed clusters, including scaling and configuration.
  image: https://azure.microsoft.com/images/aks-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/aks/agent-pools
  baseURL: https://management.azure.com
  tags:
  - Agent Pools
  - Kubernetes
  - Node Pools
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/create-node-pools
  - type: API Reference
    url: https://learn.microsoft.com/en-us/rest/api/aks/agent-pools
  - type: OpenAPI
    url: openapi/azure-kubernetes-service-openapi.yml
  - type: JSONSchema
    url: json-schema/azure-kubernetes-service-cluster-schema.json
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/aks/create-node-pools
- name: Azure Kubernetes Service Maintenance Configurations API
  description: REST API for managing planned maintenance configurations, used to configure when updates can be deployed to an AKS managed cluster.
  image: https://azure.microsoft.com/images/aks-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/aks/maintenance-configurations
  baseURL: https://management.azure.com
  tags:
  - Configuration
  - Kubernetes
  - Maintenance
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/planned-maintenance
  - type: API Reference
    url: https://learn.microsoft.com/en-us/rest/api/aks/maintenance-configurations
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
- name: Azure Kubernetes Service Snapshots API
  description: REST API for creating, updating, deleting, and managing node pool snapshots in AKS, including listing snapshots by resource group.
  image: https://azure.microsoft.com/images/aks-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/aks/snapshots
  baseURL: https://management.azure.com
  tags:
  - Backup
  - Kubernetes
  - Snapshots
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/node-pool-snapshot
  - type: API Reference
    url: https://learn.microsoft.com/en-us/rest/api/aks/snapshots
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
- name: Azure Kubernetes Service Private Endpoint Connections API
  description: REST API for managing private endpoint connections for AKS clusters, enabling secure private network access to the cluster API server.
  image: https://azure.microsoft.com/images/aks-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/aks/private-endpoint-connections
  baseURL: https://management.azure.com
  tags:
  - Kubernetes
  - Networking
  - Private Endpoints
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/private-clusters
  - type: API Reference
    url: https://learn.microsoft.com/en-us/rest/api/aks/private-endpoint-connections
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
- name: Azure Kubernetes Service Trusted Access Role Bindings API
  description: REST API for managing trusted access role bindings that give Azure services secure access to AKS API server using system-assigned managed identities.
  image: https://azure.microsoft.com/images/aks-icon.png
  humanURL: https://learn.microsoft.com/en-us/rest/api/aks/trusted-access-role-bindings
  baseURL: https://management.azure.com
  tags:
  - Kubernetes
  - Security
  - Trusted Access
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/trusted-access-feature
  - type: API Reference
    url: https://learn.microsoft.com/en-us/rest/api/aks/trusted-access-role-bindings
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
- name: Azure Kubernetes Service kubectl API
  description: Kubernetes API accessible via kubectl for cluster operations.
  humanURL: https://kubernetes.io/docs/reference/
  baseURL: https://{cluster-name}.{region}.azmk8s.io
  tags:
  - Cluster Management
  - Kubectl
  - Kubernetes
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/kubernetes-walkthrough
  - type: API Reference
    url: https://kubernetes.io/docs/reference/kubernetes-api/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/aks/control-kubeconfig-access
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
name: Azure Kubernetes Service
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
type: Contract
image: https://azure.microsoft.com/images/aks-icon.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure Kubernetes Service (AKS) simplifies deploying a managed Kubernetes cluster in Azure by offloading the operational overhead to Azure. As a hosted Kubernetes service, Azure handles critical tasks, like health monitoring and maintenance.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

