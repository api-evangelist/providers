---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 3
  name: Microsoft Azure Kubernetes Service Agentic Access
  operation_count: 24
  slug: microsoft-azure-kubernetes-service-agentic-access
  summary_line: 24 operations · 16 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: REST API for managing planned maintenance configurations, used to configure when updates can be deployed to an AKS managed cluster.
  name: Azure Kubernetes Service Maintenance Configurations API
  slug: azure-kubernetes-service-maintenance-configurations-api
- description: REST API for creating, updating, deleting, and managing node pool snapshots in AKS, including listing snapshots by resource group.
  name: Azure Kubernetes Service Snapshots API
  slug: azure-kubernetes-service-snapshots-api
- description: REST API for managing private endpoint connections for AKS clusters, enabling secure private network access to the cluster API server.
  name: Azure Kubernetes Service Private Endpoint Connections API
  slug: azure-kubernetes-service-private-endpoint-connections-api
- description: REST API for managing trusted access role bindings that give Azure services secure access to AKS API server using system-assigned managed identities.
  name: Azure Kubernetes Service Trusted Access Role Bindings API
  slug: azure-kubernetes-service-trusted-access-role-bindings-api
- description: Kubernetes API accessible via kubectl for cluster operations.
  name: Azure Kubernetes Service kubectl API
  slug: azure-kubernetes-service-kubectl-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: Operations for managing agent pools (node pools) within AKS clusters
  name: Azure Kubernetes Service Agent Pools API
  slug: microsoft-azure-kubernetes-service-agent-pools-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: Operations for managing AKS managed clusters
  name: Azure Kubernetes Service Managed Clusters API
  slug: microsoft-azure-kubernetes-service-managed-clusters-api
arazzos:
- description: Add a new agent (node) pool to an AKS cluster and poll until it finishes provisioning.
  name: Azure Kubernetes Service Add Node Pool and Poll
  slug: azure-kubernetes-service-add-node-pool-workflow
- description: Delete specific machines from an agent pool and poll until the operation completes.
  name: Azure Kubernetes Service Delete Node Pool Machines
  slug: azure-kubernetes-service-delete-machines-workflow
- description: Create a managed AKS cluster, poll until it is provisioned, then retrieve admin kubeconfig.
  name: Azure Kubernetes Service Provision Cluster and Fetch Credentials
  slug: azure-kubernetes-service-provision-cluster-workflow
- description: Trigger certificate rotation on a cluster, poll until provisioned, and refresh user credentials.
  name: Azure Kubernetes Service Rotate Cluster Certificates
  slug: azure-kubernetes-service-rotate-certificates-workflow
- description: Confirm a cluster is provisioned, then run a kubectl command against it via the AKS command runner.
  name: Azure Kubernetes Service Run Command on Cluster
  slug: azure-kubernetes-service-run-command-workflow
- description: Read an agent pool, change its node count, and poll until the scale operation completes.
  name: Azure Kubernetes Service Scale Node Pool
  slug: azure-kubernetes-service-scale-node-pool-workflow
- description: Start a stopped AKS cluster, poll until provisioned, then fetch user credentials.
  name: Azure Kubernetes Service Start Cluster
  slug: azure-kubernetes-service-start-cluster-workflow
- description: Stop a running AKS cluster and poll until the stop operation finishes provisioning.
  name: Azure Kubernetes Service Stop Cluster
  slug: azure-kubernetes-service-stop-cluster-workflow
- description: Discover an available Kubernetes version, upgrade the cluster, and poll until provisioned.
  name: Azure Kubernetes Service Upgrade Cluster Control Plane
  slug: azure-kubernetes-service-upgrade-cluster-workflow
- description: Discover the latest node image, trigger the node image upgrade, and poll until complete.
  name: Azure Kubernetes Service Upgrade Node Pool Image
  slug: azure-kubernetes-service-upgrade-node-image-workflow
artifact_total: 262
collections:
- collection_type: postman
  name: Azure Kubernetes Service REST API
  slug: postman-azure-kubernetes-service
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Kubernetes Service REST API
  slug: open-azure-kubernetes-service
- collection_type: open
  name: Azure Kubernetes Service REST Agent Pools API
  slug: open-microsoft-azure-kubernetes-service-agent-pools-api
- collection_type: open
  name: Azure Kubernetes Service REST Agent Pools Managed Clusters API
  slug: open-microsoft-azure-kubernetes-service-managed-clusters-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/AKS/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/AKS/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/AKS/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/AKS/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/AKS/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-kubernetes-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-kubernetes-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-kubernetes-service-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-kubernetes-service-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-kubernetes-service/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-add-node-pool-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-delete-machines-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-provision-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-rotate-certificates-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-run-command-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-scale-node-pool-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-start-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-stop-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-upgrade-cluster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-kubernetes-service-upgrade-node-image-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-portal
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/aks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/topics/kubernetes/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/AKS
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-aks
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/azure/aks/concepts-security
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/aks/concepts-security#azure-policy
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/aks/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/kubernetes-service/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Azure/AKS/blob/master/CHANGELOG.md
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/azure/aks/release-tracker
- group: operate
  title: ''
  type: FAQ
  url: https://learn.microsoft.com/en-us/azure/aks/faq
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/modules/intro-to-azure-kubernetes-service/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/MicrosoftAzure
- group: design
  title: ''
  type: SpectralRules
  url: rules/azure-kubernetes-service-spectral-rules.yml
created: '2024-01-15'
description: Azure Kubernetes Service (AKS) simplifies deploying a managed Kubernetes cluster in Azure by offloading the operational overhead to Azure. As a hosted Kubernetes service, Azure handles critical tasks, like health monitoring and maintenance.
examples:
- key_count: 4
  name: Azure Kubernetes Service Agent Pool Available Versions Example
  slug: azure-kubernetes-service-agent-pool-available-versions-example
- key_count: 1
  name: Azure Kubernetes Service Agent Pool Delete Machines Parameter Example
  slug: azure-kubernetes-service-agent-pool-delete-machines-parameter-example
- key_count: 3
  name: Azure Kubernetes Service Agent Pool Example
  slug: azure-kubernetes-service-agent-pool-example
- key_count: 2
  name: Azure Kubernetes Service Agent Pool List Result Example
  slug: azure-kubernetes-service-agent-pool-list-result-example
- key_count: 35
  name: Azure Kubernetes Service Agent Pool Properties Example
  slug: azure-kubernetes-service-agent-pool-properties-example
- key_count: 4
  name: Azure Kubernetes Service Agent Pool Upgrade Profile Example
  slug: azure-kubernetes-service-agent-pool-upgrade-profile-example
- key_count: 3
  name: Azure Kubernetes Service Agent Pool Upgrade Settings Example
  slug: azure-kubernetes-service-agent-pool-upgrade-settings-example
- key_count: 1
  name: Azure Kubernetes Service Cloud Error Example
  slug: azure-kubernetes-service-cloud-error-example
- key_count: 1
  name: Azure Kubernetes Service Cluster Upgrade Settings Example
  slug: azure-kubernetes-service-cluster-upgrade-settings-example
- key_count: 2
  name: Azure Kubernetes Service Container Service Linux Profile Example
  slug: azure-kubernetes-service-container-service-linux-profile-example
- key_count: 10
  name: Azure Kubernetes Service Container Service Network Profile Example
  slug: azure-kubernetes-service-container-service-network-profile-example
- key_count: 1
  name: Azure Kubernetes Service Creation Data Example
  slug: azure-kubernetes-service-creation-data-example
- key_count: 1
  name: Azure Kubernetes Service Credential Results Example
  slug: azure-kubernetes-service-credential-results-example
- key_count: 2
  name: Azure Kubernetes Service Extended Location Example
  slug: azure-kubernetes-service-extended-location-example
- key_count: 7
  name: Azure Kubernetes Service Managed Cluster Aad Profile Example
  slug: azure-kubernetes-service-managed-cluster-aad-profile-example
- key_count: 2
  name: Azure Kubernetes Service Managed Cluster Addon Profile Example
  slug: azure-kubernetes-service-managed-cluster-addon-profile-example
- key_count: 35
  name: Azure Kubernetes Service Managed Cluster Agent Pool Profile Example
  slug: azure-kubernetes-service-managed-cluster-agent-pool-profile-example
- key_count: 7
  name: Azure Kubernetes Service Managed Cluster Api Server Access Profile Example
  slug: azure-kubernetes-service-managed-cluster-api-server-access-profile-example
- key_count: 19
  name: Azure Kubernetes Service Managed Cluster Auto Scaler Profile Example
  slug: azure-kubernetes-service-managed-cluster-auto-scaler-profile-example
- key_count: 2
  name: Azure Kubernetes Service Managed Cluster Auto Upgrade Profile Example
  slug: azure-kubernetes-service-managed-cluster-auto-upgrade-profile-example
- key_count: 1
  name: Azure Kubernetes Service Managed Cluster Azure Monitor Profile Example
  slug: azure-kubernetes-service-managed-cluster-azure-monitor-profile-example
- key_count: 6
  name: Azure Kubernetes Service Managed Cluster Example
  slug: azure-kubernetes-service-managed-cluster-example
- key_count: 4
  name: Azure Kubernetes Service Managed Cluster Identity Example
  slug: azure-kubernetes-service-managed-cluster-identity-example
- key_count: 1
  name: Azure Kubernetes Service Managed Cluster Ingress Profile Example
  slug: azure-kubernetes-service-managed-cluster-ingress-profile-example
- key_count: 2
  name: Azure Kubernetes Service Managed Cluster List Result Example
  slug: azure-kubernetes-service-managed-cluster-list-result-example
- key_count: 6
  name: Azure Kubernetes Service Managed Cluster Load Balancer Profile Example
  slug: azure-kubernetes-service-managed-cluster-load-balancer-profile-example
- key_count: 1
  name: Azure Kubernetes Service Managed Cluster Metrics Profile Example
  slug: azure-kubernetes-service-managed-cluster-metrics-profile-example
- key_count: 3
  name: Azure Kubernetes Service Managed Cluster Nat Gateway Profile Example
  slug: azure-kubernetes-service-managed-cluster-nat-gateway-profile-example
- key_count: 1
  name: Azure Kubernetes Service Managed Cluster Node Resource Group Profile Example
  slug: azure-kubernetes-service-managed-cluster-node-resource-group-profile-example
- key_count: 2
  name: Azure Kubernetes Service Managed Cluster Oidc Issuer Profile Example
  slug: azure-kubernetes-service-managed-cluster-oidc-issuer-profile-example
- key_count: 17
  name: Azure Kubernetes Service Managed Cluster Properties Example
  slug: azure-kubernetes-service-managed-cluster-properties-example
- key_count: 3
  name: Azure Kubernetes Service Managed Cluster Security Profile Example
  slug: azure-kubernetes-service-managed-cluster-security-profile-example
- key_count: 2
  name: Azure Kubernetes Service Managed Cluster Service Principal Profile Example
  slug: azure-kubernetes-service-managed-cluster-service-principal-profile-example
- key_count: 2
  name: Azure Kubernetes Service Managed Cluster Sku Example
  slug: azure-kubernetes-service-managed-cluster-sku-example
- key_count: 4
  name: Azure Kubernetes Service Managed Cluster Storage Profile Example
  slug: azure-kubernetes-service-managed-cluster-storage-profile-example
- key_count: 4
  name: Azure Kubernetes Service Managed Cluster Upgrade Profile Example
  slug: azure-kubernetes-service-managed-cluster-upgrade-profile-example
- key_count: 4
  name: Azure Kubernetes Service Managed Cluster Windows Profile Example
  slug: azure-kubernetes-service-managed-cluster-windows-profile-example
- key_count: 2
  name: Azure Kubernetes Service Managed Cluster Workload Auto Scaler Profile Example
  slug: azure-kubernetes-service-managed-cluster-workload-auto-scaler-profile-example
- key_count: 1
  name: Azure Kubernetes Service Power State Example
  slug: azure-kubernetes-service-power-state-example
- key_count: 3
  name: Azure Kubernetes Service Run Command Request Example
  slug: azure-kubernetes-service-run-command-request-example
- key_count: 2
  name: Azure Kubernetes Service Run Command Result Example
  slug: azure-kubernetes-service-run-command-result-example
- key_count: 2
  name: Azure Kubernetes Service Service Mesh Profile Example
  slug: azure-kubernetes-service-service-mesh-profile-example
- key_count: 6
  name: Azure Kubernetes Service System Data Example
  slug: azure-kubernetes-service-system-data-example
- key_count: 1
  name: Azure Kubernetes Service Tags Object Example
  slug: azure-kubernetes-service-tags-object-example
- key_count: 3
  name: Azure Kubernetes Service User Assigned Identity Example
  slug: azure-kubernetes-service-user-assigned-identity-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Abortlatestoperation Example
  slug: microsoft-azure-kubernetes-service-agentpools-abortlatestoperation-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Createorupdate Example
  slug: microsoft-azure-kubernetes-service-agentpools-createorupdate-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Delete Example
  slug: microsoft-azure-kubernetes-service-agentpools-delete-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Deletemachines Example
  slug: microsoft-azure-kubernetes-service-agentpools-deletemachines-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Get Example
  slug: microsoft-azure-kubernetes-service-agentpools-get-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Getavailableagentpoolversions Example
  slug: microsoft-azure-kubernetes-service-agentpools-getavailableagentpoolversions-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Getupgradeprofile Example
  slug: microsoft-azure-kubernetes-service-agentpools-getupgradeprofile-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools List Example
  slug: microsoft-azure-kubernetes-service-agentpools-list-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Agentpools Upgradenodeimageversion Example
  slug: microsoft-azure-kubernetes-service-agentpools-upgradenodeimageversion-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Abortlatestoperation Example
  slug: microsoft-azure-kubernetes-service-managedclusters-abortlatestoperation-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Createorupdate Example
  slug: microsoft-azure-kubernetes-service-managedclusters-createorupdate-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Delete Example
  slug: microsoft-azure-kubernetes-service-managedclusters-delete-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Get Example
  slug: microsoft-azure-kubernetes-service-managedclusters-get-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Getupgradeprofile Example
  slug: microsoft-azure-kubernetes-service-managedclusters-getupgradeprofile-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters List Example
  slug: microsoft-azure-kubernetes-service-managedclusters-list-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Listbyresourcegroup Example
  slug: microsoft-azure-kubernetes-service-managedclusters-listbyresourcegroup-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Listclusteradmincredentials Example
  slug: microsoft-azure-kubernetes-service-managedclusters-listclusteradmincredentials-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Listclustermonitoringusercredentials Example
  slug: microsoft-azure-kubernetes-service-managedclusters-listclustermonitoringusercredentials-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Listclusterusercredentials Example
  slug: microsoft-azure-kubernetes-service-managedclusters-listclusterusercredentials-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Rotateclustercertificates Example
  slug: microsoft-azure-kubernetes-service-managedclusters-rotateclustercertificates-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Runcommand Example
  slug: microsoft-azure-kubernetes-service-managedclusters-runcommand-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Start Example
  slug: microsoft-azure-kubernetes-service-managedclusters-start-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Stop Example
  slug: microsoft-azure-kubernetes-service-managedclusters-stop-example
- key_count: 6
  name: Microsoft Azure Kubernetes Service Managedclusters Updatetags Example
  slug: microsoft-azure-kubernetes-service-managedclusters-updatetags-example
features:
- description: Create, update, delete, start, and stop AKS managed clusters with full lifecycle management.
  name: Managed Cluster Lifecycle
- description: Create and manage node pools with configurable VM sizes, scaling, and upgrade policies.
  name: Agent Pool Management
- description: Upgrade Kubernetes versions and node images with controlled rollout and upgrade profiles.
  name: Cluster Upgrades
- description: Retrieve admin, user, and monitoring credentials for cluster access and authentication.
  name: Credential Management
- description: Deploy private AKS clusters with private endpoint connections for secure API server access.
  name: Private Clusters
- description: Configure planned maintenance windows to control when updates are applied to clusters.
  name: Maintenance Windows
- description: Create and manage snapshots of node pools for backup and recovery scenarios.
  name: Node Pool Snapshots
- description: Grant Azure services secure access to AKS API server using managed identities and role bindings.
  name: Trusted Access
- description: Execute commands on cluster nodes remotely through the AKS API without direct SSH access.
  name: Run Commands
- description: Automatically scale node pools based on workload demands with configurable auto-scaler profiles.
  name: Auto-Scaling
finops:
- name: Azure Kubernetes Service Finops
  service_category: Container Platform
  slug: azure-kubernetes-service-finops
- name: Microsoft Azure Kubernetes Service Finops
  service_category: Compute / Container Orchestration
  slug: microsoft-azure-kubernetes-service-finops
image: https://azure.microsoft.com/images/aks-icon.png
integrations:
- description: Pull container images from Azure Container Registry with managed identity authentication.
  name: Azure Container Registry
- description: Monitor cluster health, performance, and logs with Azure Monitor and Container Insights.
  name: Azure Monitor
- description: Enforce organizational standards and compliance with Azure Policy for Kubernetes.
  name: Azure Policy
- description: Integrate with Azure AD for cluster authentication and role-based access control.
  name: Azure Active Directory
- description: Automate deployments to AKS using Azure Pipelines with native Kubernetes tasks.
  name: Azure DevOps
json_schemas:
- name: AgentPoolAvailableVersions
  property_count: 4
  slug: azure-kubernetes-service-agent-pool-available-versions
- name: AgentPoolDeleteMachinesParameter
  property_count: 1
  slug: azure-kubernetes-service-agent-pool-delete-machines-parameter
- name: AgentPoolListResult
  property_count: 2
  slug: azure-kubernetes-service-agent-pool-list-result
- name: AgentPoolProperties
  property_count: 35
  slug: azure-kubernetes-service-agent-pool-properties
- name: AgentPool
  property_count: 3
  slug: azure-kubernetes-service-agent-pool
- name: AgentPoolUpgradeProfile
  property_count: 4
  slug: azure-kubernetes-service-agent-pool-upgrade-profile
- name: AgentPoolUpgradeSettings
  property_count: 3
  slug: azure-kubernetes-service-agent-pool-upgrade-settings
- name: CloudError
  property_count: 1
  slug: azure-kubernetes-service-cloud-error
- name: Azure Kubernetes Service Managed Cluster
  property_count: 11
  slug: azure-kubernetes-service-cluster
- name: ClusterUpgradeSettings
  property_count: 1
  slug: azure-kubernetes-service-cluster-upgrade-settings
- name: ContainerServiceLinuxProfile
  property_count: 2
  slug: azure-kubernetes-service-container-service-linux-profile
- name: ContainerServiceNetworkProfile
  property_count: 10
  slug: azure-kubernetes-service-container-service-network-profile
- name: CreationData
  property_count: 1
  slug: azure-kubernetes-service-creation-data
- name: CredentialResults
  property_count: 1
  slug: azure-kubernetes-service-credential-results
- name: ExtendedLocation
  property_count: 2
  slug: azure-kubernetes-service-extended-location
- name: ManagedClusterAADProfile
  property_count: 7
  slug: azure-kubernetes-service-managed-cluster-aad-profile
- name: ManagedClusterAddonProfile
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-addon-profile
- name: ManagedClusterAgentPoolProfile
  property_count: 35
  slug: azure-kubernetes-service-managed-cluster-agent-pool-profile
- name: ManagedClusterAPIServerAccessProfile
  property_count: 7
  slug: azure-kubernetes-service-managed-cluster-api-server-access-profile
- name: ManagedClusterAutoScalerProfile
  property_count: 19
  slug: azure-kubernetes-service-managed-cluster-auto-scaler-profile
- name: ManagedClusterAutoUpgradeProfile
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-auto-upgrade-profile
- name: ManagedClusterAzureMonitorProfile
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-azure-monitor-profile
- name: ManagedClusterIdentity
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-identity
- name: ManagedClusterIngressProfile
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-ingress-profile
- name: ManagedClusterListResult
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-list-result
- name: ManagedClusterLoadBalancerProfile
  property_count: 6
  slug: azure-kubernetes-service-managed-cluster-load-balancer-profile
- name: ManagedClusterMetricsProfile
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-metrics-profile
- name: ManagedClusterNATGatewayProfile
  property_count: 3
  slug: azure-kubernetes-service-managed-cluster-nat-gateway-profile
- name: ManagedClusterNodeResourceGroupProfile
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-node-resource-group-profile
- name: ManagedClusterOIDCIssuerProfile
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-oidc-issuer-profile
- name: ManagedClusterProperties
  property_count: 17
  slug: azure-kubernetes-service-managed-cluster-properties
- name: ManagedCluster
  property_count: 6
  slug: azure-kubernetes-service-managed-cluster
- name: ManagedClusterSecurityProfile
  property_count: 3
  slug: azure-kubernetes-service-managed-cluster-security-profile
- name: ManagedClusterServicePrincipalProfile
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-service-principal-profile
- name: ManagedClusterSKU
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-sku
- name: ManagedClusterStorageProfile
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-storage-profile
- name: ManagedClusterUpgradeProfile
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-upgrade-profile
- name: ManagedClusterWindowsProfile
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-windows-profile
- name: ManagedClusterWorkloadAutoScalerProfile
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-workload-auto-scaler-profile
- name: PowerState
  property_count: 1
  slug: azure-kubernetes-service-power-state
- name: RunCommandRequest
  property_count: 3
  slug: azure-kubernetes-service-run-command-request
- name: RunCommandResult
  property_count: 2
  slug: azure-kubernetes-service-run-command-result
- name: ServiceMeshProfile
  property_count: 2
  slug: azure-kubernetes-service-service-mesh-profile
- name: SystemData
  property_count: 6
  slug: azure-kubernetes-service-system-data
- name: TagsObject
  property_count: 1
  slug: azure-kubernetes-service-tags-object
- name: UserAssignedIdentity
  property_count: 3
  slug: azure-kubernetes-service-user-assigned-identity
- name: AgentPool
  property_count: 4
  slug: microsoft-azure-kubernetes-service-agentpool
- name: AgentPoolAvailableVersions
  property_count: 4
  slug: microsoft-azure-kubernetes-service-agentpoolavailableversions
- name: AgentPoolDeleteMachinesParameter
  property_count: 1
  slug: microsoft-azure-kubernetes-service-agentpooldeletemachinesparameter
- name: AgentPoolListResult
  property_count: 2
  slug: microsoft-azure-kubernetes-service-agentpoollistresult
- name: AgentPoolProperties
  property_count: 38
  slug: microsoft-azure-kubernetes-service-agentpoolproperties
- name: AgentPoolUpgradeProfile
  property_count: 4
  slug: microsoft-azure-kubernetes-service-agentpoolupgradeprofile
- name: AgentPoolUpgradeSettings
  property_count: 3
  slug: microsoft-azure-kubernetes-service-agentpoolupgradesettings
- name: CloudError
  property_count: 1
  slug: microsoft-azure-kubernetes-service-clouderror
- name: ClusterUpgradeSettings
  property_count: 1
  slug: microsoft-azure-kubernetes-service-clusterupgradesettings
- name: ContainerServiceLinuxProfile
  property_count: 2
  slug: microsoft-azure-kubernetes-service-containerservicelinuxprofile
- name: ContainerServiceNetworkProfile
  property_count: 12
  slug: microsoft-azure-kubernetes-service-containerservicenetworkprofile
- name: CreationData
  property_count: 1
  slug: microsoft-azure-kubernetes-service-creationdata
- name: CredentialResults
  property_count: 1
  slug: microsoft-azure-kubernetes-service-credentialresults
- name: ExtendedLocation
  property_count: 2
  slug: microsoft-azure-kubernetes-service-extendedlocation
- name: ManagedCluster
  property_count: 11
  slug: microsoft-azure-kubernetes-service-managedcluster
- name: ManagedClusterAADProfile
  property_count: 7
  slug: microsoft-azure-kubernetes-service-managedclusteraadprofile
- name: ManagedClusterAddonProfile
  property_count: 3
  slug: microsoft-azure-kubernetes-service-managedclusteraddonprofile
- name: ManagedClusterAgentPoolProfile
  property_count: 38
  slug: microsoft-azure-kubernetes-service-managedclusteragentpoolprofile
- name: ManagedClusterAPIServerAccessProfile
  property_count: 7
  slug: microsoft-azure-kubernetes-service-managedclusterapiserveraccessprofile
- name: ManagedClusterAutoScalerProfile
  property_count: 19
  slug: microsoft-azure-kubernetes-service-managedclusterautoscalerprofile
- name: ManagedClusterAutoUpgradeProfile
  property_count: 2
  slug: microsoft-azure-kubernetes-service-managedclusterautoupgradeprofile
- name: ManagedClusterAzureMonitorProfile
  property_count: 1
  slug: microsoft-azure-kubernetes-service-managedclusterazuremonitorprofile
- name: ManagedClusterIdentity
  property_count: 4
  slug: microsoft-azure-kubernetes-service-managedclusteridentity
- name: ManagedClusterIngressProfile
  property_count: 1
  slug: microsoft-azure-kubernetes-service-managedclusteringressprofile
- name: ManagedClusterListResult
  property_count: 2
  slug: microsoft-azure-kubernetes-service-managedclusterlistresult
- name: ManagedClusterLoadBalancerProfile
  property_count: 6
  slug: microsoft-azure-kubernetes-service-managedclusterloadbalancerprofile
- name: ManagedClusterMetricsProfile
  property_count: 1
  slug: microsoft-azure-kubernetes-service-managedclustermetricsprofile
- name: ManagedClusterNATGatewayProfile
  property_count: 3
  slug: microsoft-azure-kubernetes-service-managedclusternatgatewayprofile
- name: ManagedClusterNodeResourceGroupProfile
  property_count: 1
  slug: microsoft-azure-kubernetes-service-managedclusternoderesourcegroupprofile
- name: ManagedClusterOIDCIssuerProfile
  property_count: 2
  slug: microsoft-azure-kubernetes-service-managedclusteroidcissuerprofile
- name: ManagedClusterProperties
  property_count: 36
  slug: microsoft-azure-kubernetes-service-managedclusterproperties
- name: ManagedClusterSecurityProfile
  property_count: 3
  slug: microsoft-azure-kubernetes-service-managedclustersecurityprofile
- name: ManagedClusterServicePrincipalProfile
  property_count: 2
  slug: microsoft-azure-kubernetes-service-managedclusterserviceprincipalprofile
- name: ManagedClusterSKU
  property_count: 2
  slug: microsoft-azure-kubernetes-service-managedclustersku
- name: ManagedClusterStorageProfile
  property_count: 4
  slug: microsoft-azure-kubernetes-service-managedclusterstorageprofile
- name: ManagedClusterUpgradeProfile
  property_count: 4
  slug: microsoft-azure-kubernetes-service-managedclusterupgradeprofile
- name: ManagedClusterWindowsProfile
  property_count: 4
  slug: microsoft-azure-kubernetes-service-managedclusterwindowsprofile
- name: ManagedClusterWorkloadAutoScalerProfile
  property_count: 2
  slug: microsoft-azure-kubernetes-service-managedclusterworkloadautoscalerprofile
- name: PowerState
  property_count: 1
  slug: microsoft-azure-kubernetes-service-powerstate
- name: RunCommandRequest
  property_count: 3
  slug: microsoft-azure-kubernetes-service-runcommandrequest
- name: RunCommandResult
  property_count: 2
  slug: microsoft-azure-kubernetes-service-runcommandresult
- name: ServiceMeshProfile
  property_count: 2
  slug: microsoft-azure-kubernetes-service-servicemeshprofile
- name: SystemData
  property_count: 6
  slug: microsoft-azure-kubernetes-service-systemdata
- name: TagsObject
  property_count: 1
  slug: microsoft-azure-kubernetes-service-tagsobject
- name: UserAssignedIdentity
  property_count: 3
  slug: microsoft-azure-kubernetes-service-userassignedidentity
json_structures:
- name: Azure Kubernetes Service Agent Pool Available Versions Structure
  property_count: 4
  slug: azure-kubernetes-service-agent-pool-available-versions-structure
- name: Azure Kubernetes Service Agent Pool Delete Machines Parameter Structure
  property_count: 1
  slug: azure-kubernetes-service-agent-pool-delete-machines-parameter-structure
- name: Azure Kubernetes Service Agent Pool List Result Structure
  property_count: 2
  slug: azure-kubernetes-service-agent-pool-list-result-structure
- name: Azure Kubernetes Service Agent Pool Properties Structure
  property_count: 35
  slug: azure-kubernetes-service-agent-pool-properties-structure
- name: Azure Kubernetes Service Agent Pool Structure
  property_count: 3
  slug: azure-kubernetes-service-agent-pool-structure
- name: Azure Kubernetes Service Agent Pool Upgrade Profile Structure
  property_count: 4
  slug: azure-kubernetes-service-agent-pool-upgrade-profile-structure
- name: Azure Kubernetes Service Agent Pool Upgrade Settings Structure
  property_count: 3
  slug: azure-kubernetes-service-agent-pool-upgrade-settings-structure
- name: Azure Kubernetes Service Cloud Error Structure
  property_count: 1
  slug: azure-kubernetes-service-cloud-error-structure
- name: Azure Kubernetes Service Cluster Upgrade Settings Structure
  property_count: 1
  slug: azure-kubernetes-service-cluster-upgrade-settings-structure
- name: Azure Kubernetes Service Container Service Linux Profile Structure
  property_count: 2
  slug: azure-kubernetes-service-container-service-linux-profile-structure
- name: Azure Kubernetes Service Container Service Network Profile Structure
  property_count: 10
  slug: azure-kubernetes-service-container-service-network-profile-structure
- name: Azure Kubernetes Service Creation Data Structure
  property_count: 1
  slug: azure-kubernetes-service-creation-data-structure
- name: Azure Kubernetes Service Credential Results Structure
  property_count: 1
  slug: azure-kubernetes-service-credential-results-structure
- name: Azure Kubernetes Service Extended Location Structure
  property_count: 2
  slug: azure-kubernetes-service-extended-location-structure
- name: Azure Kubernetes Service Managed Cluster Aad Profile Structure
  property_count: 7
  slug: azure-kubernetes-service-managed-cluster-aad-profile-structure
- name: Azure Kubernetes Service Managed Cluster Addon Profile Structure
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-addon-profile-structure
- name: Azure Kubernetes Service Managed Cluster Agent Pool Profile Structure
  property_count: 35
  slug: azure-kubernetes-service-managed-cluster-agent-pool-profile-structure
- name: Azure Kubernetes Service Managed Cluster Api Server Access Profile Structure
  property_count: 7
  slug: azure-kubernetes-service-managed-cluster-api-server-access-profile-structure
- name: Azure Kubernetes Service Managed Cluster Auto Scaler Profile Structure
  property_count: 19
  slug: azure-kubernetes-service-managed-cluster-auto-scaler-profile-structure
- name: Azure Kubernetes Service Managed Cluster Auto Upgrade Profile Structure
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-auto-upgrade-profile-structure
- name: Azure Kubernetes Service Managed Cluster Azure Monitor Profile Structure
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-azure-monitor-profile-structure
- name: Azure Kubernetes Service Managed Cluster Identity Structure
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-identity-structure
- name: Azure Kubernetes Service Managed Cluster Ingress Profile Structure
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-ingress-profile-structure
- name: Azure Kubernetes Service Managed Cluster List Result Structure
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-list-result-structure
- name: Azure Kubernetes Service Managed Cluster Load Balancer Profile Structure
  property_count: 6
  slug: azure-kubernetes-service-managed-cluster-load-balancer-profile-structure
- name: Azure Kubernetes Service Managed Cluster Metrics Profile Structure
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-metrics-profile-structure
- name: Azure Kubernetes Service Managed Cluster Nat Gateway Profile Structure
  property_count: 3
  slug: azure-kubernetes-service-managed-cluster-nat-gateway-profile-structure
- name: Azure Kubernetes Service Managed Cluster Node Resource Group Profile Structure
  property_count: 1
  slug: azure-kubernetes-service-managed-cluster-node-resource-group-profile-structure
- name: Azure Kubernetes Service Managed Cluster Oidc Issuer Profile Structure
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-oidc-issuer-profile-structure
- name: Azure Kubernetes Service Managed Cluster Properties Structure
  property_count: 17
  slug: azure-kubernetes-service-managed-cluster-properties-structure
- name: Azure Kubernetes Service Managed Cluster Security Profile Structure
  property_count: 3
  slug: azure-kubernetes-service-managed-cluster-security-profile-structure
- name: Azure Kubernetes Service Managed Cluster Service Principal Profile Structure
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-service-principal-profile-structure
- name: Azure Kubernetes Service Managed Cluster Sku Structure
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-sku-structure
- name: Azure Kubernetes Service Managed Cluster Storage Profile Structure
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-storage-profile-structure
- name: Azure Kubernetes Service Managed Cluster Structure
  property_count: 6
  slug: azure-kubernetes-service-managed-cluster-structure
- name: Azure Kubernetes Service Managed Cluster Upgrade Profile Structure
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-upgrade-profile-structure
- name: Azure Kubernetes Service Managed Cluster Windows Profile Structure
  property_count: 4
  slug: azure-kubernetes-service-managed-cluster-windows-profile-structure
- name: Azure Kubernetes Service Managed Cluster Workload Auto Scaler Profile Structure
  property_count: 2
  slug: azure-kubernetes-service-managed-cluster-workload-auto-scaler-profile-structure
- name: Azure Kubernetes Service Power State Structure
  property_count: 1
  slug: azure-kubernetes-service-power-state-structure
- name: Azure Kubernetes Service Run Command Request Structure
  property_count: 3
  slug: azure-kubernetes-service-run-command-request-structure
- name: Azure Kubernetes Service Run Command Result Structure
  property_count: 2
  slug: azure-kubernetes-service-run-command-result-structure
- name: Azure Kubernetes Service Service Mesh Profile Structure
  property_count: 2
  slug: azure-kubernetes-service-service-mesh-profile-structure
- name: Azure Kubernetes Service System Data Structure
  property_count: 6
  slug: azure-kubernetes-service-system-data-structure
- name: Azure Kubernetes Service Tags Object Structure
  property_count: 1
  slug: azure-kubernetes-service-tags-object-structure
- name: Azure Kubernetes Service User Assigned Identity Structure
  property_count: 3
  slug: azure-kubernetes-service-user-assigned-identity-structure
- name: Microsoft Azure Kubernetes Service Structure
  property_count: 0
  slug: microsoft-azure-kubernetes-service-structure
jsonld:
- class_count: 0
  name: Azure Kubernetes Service Context
  property_count: 0
  slug: azure-kubernetes-service-context
layout: provider
modified: '2026-05-19'
name: Azure Kubernetes Service
nav: Providers
network: true
overview: 'Azure Kubernetes Service publishes 2 APIs on the [APIs.io](https://apis.io/) network: Agent Pools API and Managed Clusters API. Tagged areas include Azure, Cloud, Containers, DevOps, and Kubernetes.


  The Azure Kubernetes Service catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Azure Kubernetes Service''s developer surface includes authentication, developer portal, getting-started guide, CLI, support, engineering blog, Stack Overflow tag, and 36 more developer resources.'
plans:
- name: Azure Kubernetes Service Plans Pricing
  plan_count: 3
  slug: azure-kubernetes-service-plans-pricing
- name: Microsoft Azure Kubernetes Service Plans Pricing
  plan_count: 3
  slug: microsoft-azure-kubernetes-service-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 16
  name: Azure Kubernetes Service Rate Limits
  slug: azure-kubernetes-service-rate-limits
- limit_count: 8
  name: Microsoft Azure Kubernetes Service Rate Limits
  slug: microsoft-azure-kubernetes-service-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: Azure Kubernetes Service API Rules
  rule_count: 7
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 0
  slug: azure-kubernetes-service-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Azure Kubernetes Service API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-azure-kubernetes-service-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Azure Kubernetes Service API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: microsoft-azure-kubernetes-service-spectral-rules
scopes:
- name: Microsoft Azure Kubernetes Service Scopes
  scope_count: 1
  slug: microsoft-azure-kubernetes-service-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 54.5
    contract_quality: 63.9
    developer_ergonomics: 82.1
    discoverability: 75.9
    governance: 54.5
    operational_transparency: 55.3
  open_source:
    applies: true
    score: 100.0
  previous_composite: 70.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-kubernetes-service/refs/heads/main/screenshots/microsoft-azure-kubernetes-service-2026-06-20T185419.png
security:
- kind: authentication
  name: Microsoft Azure Kubernetes Service Authentication
  slug: microsoft-azure-kubernetes-service-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Kubernetes Service Domain Security
  slug: microsoft-azure-kubernetes-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-kubernetes-service
tags:
- Azure
- Cloud
- Containers
- DevOps
- Kubernetes
- Orchestration
use_cases:
- description: Deploy and manage microservices architectures with container orchestration and service mesh capabilities.
  name: Microservices Deployment
- description: Integrate AKS with Azure DevOps and GitHub Actions for automated build, test, and deployment workflows.
  name: CI/CD Pipelines
- description: Run Kubernetes workloads across on-premises and Azure environments with Azure Arc integration.
  name: Hybrid Cloud
- description: Deploy and scale ML model serving infrastructure using AKS with GPU-enabled node pools.
  name: Machine Learning
- description: Deploy containerized workloads to edge locations using AKS Edge Essentials and Azure IoT.
  name: Edge Computing
website: https://portal.azure.com/
---
