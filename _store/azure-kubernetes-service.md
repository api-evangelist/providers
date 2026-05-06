---
name: Azure Kubernetes Service
description: Azure Kubernetes Service (AKS) simplifies deploying a managed Kubernetes cluster in Azure by offloading the operational overhead to Azure. As a hosted Kubernetes service, Azure handles critical tasks, like health monitoring and maintenance.
image: https://azure.microsoft.com/images/aks-icon.png
url: https://azure.microsoft.com/en-us/services/kubernetes-service/
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Azure
  - Cloud
  - Containers
  - DevOps
  - Kubernetes
  - Orchestration
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
      - type: JSONSchema
        url: json-schema/azure-kubernetes-service-cluster-schema.json
      - type: JSONLD
        url: json-ld/azure-kubernetes-service-context.jsonld
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/
      - type: RateLimits
        url: https://learn.microsoft.com/en-us/azure/aks/quotas-skus-regions
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
      - type: ChangeLog
        url: https://github.com/Azure/AKS/blob/master/CHANGELOG.md
      - type: ReleaseNotes
        url: https://learn.microsoft.com/en-us/azure/aks/release-tracker
      - type: SDK
        url: https://learn.microsoft.com/en-us/python/api/overview/azure/mgmt-containerservice-readme
        title: Python SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/javascript/api/overview/azure/container-service
        title: JavaScript SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/resourcemanager.containerservice-readme
        title: .NET SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/java/api/overview/azure/resourcemanager-containerservice-readme
        title: Java SDK
      - type: SDK
        url: https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/containerservice/armcontainerservice/v6
        title: Go SDK
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
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/aks/managed-clusters
      - type: OpenAPI
        url: openapi/azure-kubernetes-service-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-kubernetes-service-cluster-schema.json
      - type: JSONLD
        url: json-ld/azure-kubernetes-service-context.jsonld
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
      - type: GettingStarted
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
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/aks/agent-pools
      - type: OpenAPI
        url: openapi/azure-kubernetes-service-openapi.yml
      - type: JSONSchema
        url: json-schema/azure-kubernetes-service-cluster-schema.json
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/aks/concepts-identity
      - type: GettingStarted
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
      - type: APIReference
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
      - type: APIReference
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
      - type: APIReference
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
      - type: APIReference
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
      - type: APIReference
        url: https://kubernetes.io/docs/reference/kubernetes-api/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/aks/control-kubeconfig-access
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
  - type: CLI
    url: https://learn.microsoft.com/en-us/cli/azure/aks
  - type: StatusPage
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/topics/kubernetes/
  - type: GitHubRepository
    url: https://github.com/Azure/AKS
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/azure-aks
  - type: Security
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-security
  - type: Compliance
    url: https://learn.microsoft.com/en-us/azure/aks/concepts-security#azure-policy
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/aks/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/
  - type: SignUp
    url: https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account
  - type: Login
    url: https://portal.azure.com/
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: ChangeLog
    url: https://github.com/Azure/AKS/blob/master/CHANGELOG.md
  - type: ReleaseNotes
    url: https://learn.microsoft.com/en-us/azure/aks/release-tracker
  - type: FAQ
    url: https://learn.microsoft.com/en-us/azure/aks/faq
  - type: Training
    url: https://learn.microsoft.com/en-us/training/modules/intro-to-azure-kubernetes-service/
  - type: YouTube
    url: https://www.youtube.com/c/MicrosoftAzure
  - type: SpectralRules
    url: rules/azure-kubernetes-service-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/aks-rest.yaml
    title: AKS REST API Shared Definition
  - type: NaftikoCapability
    url: capabilities/cluster-management.yaml
    title: Cluster Management Workflow
  - type: Features
    data:
      - name: Managed Cluster Lifecycle
        description: Create, update, delete, start, and stop AKS managed clusters with full lifecycle management.
      - name: Agent Pool Management
        description: Create and manage node pools with configurable VM sizes, scaling, and upgrade policies.
      - name: Cluster Upgrades
        description: Upgrade Kubernetes versions and node images with controlled rollout and upgrade profiles.
      - name: Credential Management
        description: Retrieve admin, user, and monitoring credentials for cluster access and authentication.
      - name: Private Clusters
        description: Deploy private AKS clusters with private endpoint connections for secure API server access.
      - name: Maintenance Windows
        description: Configure planned maintenance windows to control when updates are applied to clusters.
      - name: Node Pool Snapshots
        description: Create and manage snapshots of node pools for backup and recovery scenarios.
      - name: Trusted Access
        description: Grant Azure services secure access to AKS API server using managed identities and role bindings.
      - name: Run Commands
        description: Execute commands on cluster nodes remotely through the AKS API without direct SSH access.
      - name: Auto-Scaling
        description: Automatically scale node pools based on workload demands with configurable auto-scaler profiles.
  - type: UseCases
    data:
      - name: Microservices Deployment
        description: Deploy and manage microservices architectures with container orchestration and service mesh capabilities.
      - name: CI/CD Pipelines
        description: Integrate AKS with Azure DevOps and GitHub Actions for automated build, test, and deployment workflows.
      - name: Hybrid Cloud
        description: Run Kubernetes workloads across on-premises and Azure environments with Azure Arc integration.
      - name: Machine Learning
        description: Deploy and scale ML model serving infrastructure using AKS with GPU-enabled node pools.
      - name: Edge Computing
        description: Deploy containerized workloads to edge locations using AKS Edge Essentials and Azure IoT.
  - type: Integrations
    data:
      - name: Azure Container Registry
        description: Pull container images from Azure Container Registry with managed identity authentication.
      - name: Azure Monitor
        description: Monitor cluster health, performance, and logs with Azure Monitor and Container Insights.
      - name: Azure Policy
        description: Enforce organizational standards and compliance with Azure Policy for Kubernetes.
      - name: Azure Active Directory
        description: Integrate with Azure AD for cluster authentication and role-based access control.
      - name: Azure DevOps
        description: Automate deployments to AKS using Azure Pipelines with native Kubernetes tasks.
include:
  - name: Azure Container Registry APIs
    url: https://apis.io/apis/azure-container-registry
  - name: Azure Monitor APIs
    url: https://apis.io/apis/azure-monitor
---
