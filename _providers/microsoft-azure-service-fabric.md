---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Service Fabric Agentic Access
  operation_count: 7
  slug: microsoft-azure-service-fabric-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: 'Azure Resource Manager operations for Service Fabric clusters: create, update, delete, list clusters, cluster code versions and upgradable versions (Microsoft.ServiceFabric 2021-06-01).'
  name: Azure Service Fabric Clusters API
  slug: microsoft-azure-service-fabric-clusters-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Azure Service Fabric Operations API
  slug: microsoft-azure-service-fabric-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Azure Resource Manager operations for Service Fabric application types, application type versions, applications and services deployed to a classic cluster (Microsoft.ServiceFabric 2021-06-01).
  name: Azure Service Fabric Applications API
  slug: microsoft-azure-service-fabric-applications-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Application API from Azure Service Fabric — 19 operation(s) for application.
  name: Azure Service Fabric Application API
  slug: microsoft-azure-service-fabric-application-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ApplicationType API from Azure Service Fabric — 7 operation(s) for applicationtype.
  name: Azure Service Fabric Application Type API
  slug: microsoft-azure-service-fabric-applicationtype-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ApplicationTypes API from Azure Service Fabric — 2 operation(s) for applicationtypes.
  name: Azure Service Fabric Application Types API
  slug: microsoft-azure-service-fabric-applicationtypes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ApplicationTypeVersion API from Azure Service Fabric — 2 operation(s) for applicationtypeversion.
  name: Azure Service Fabric Application Type Version API
  slug: microsoft-azure-service-fabric-applicationtypeversion-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ApplicationTypeVersions API from Azure Service Fabric — 2 operation(s) for applicationtypeversions.
  name: Azure Service Fabric Application Type Versions API
  slug: microsoft-azure-service-fabric-applicationtypeversions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Chaos API from Azure Service Fabric — 5 operation(s) for chaos.
  name: Azure Service Fabric Chaos API
  slug: microsoft-azure-service-fabric-chaos-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Cluster API from Azure Service Fabric — 26 operation(s) for cluster.
  name: Azure Service Fabric Cluster API
  slug: microsoft-azure-service-fabric-cluster-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ClusterVersion API from Azure Service Fabric — 4 operation(s) for clusterversion.
  name: Azure Service Fabric Cluster Version API
  slug: microsoft-azure-service-fabric-clusterversion-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Code Package API from Azure Service Fabric — 4 operation(s) for code package.
  name: Azure Service Fabric Code Package API
  slug: microsoft-azure-service-fabric-code-package-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Compose Deployment API from Azure Service Fabric — 7 operation(s) for compose deployment.
  name: Azure Service Fabric Compose Deployment API
  slug: microsoft-azure-service-fabric-compose-deployment-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The EventsStore API from Azure Service Fabric — 13 operation(s) for eventsstore.
  name: Azure Service Fabric Events Store API
  slug: microsoft-azure-service-fabric-eventsstore-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Faults API from Azure Service Fabric — 10 operation(s) for faults.
  name: Azure Service Fabric Faults API
  slug: microsoft-azure-service-fabric-faults-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ImageStore API from Azure Service Fabric — 11 operation(s) for imagestore.
  name: Azure Service Fabric Image Store API
  slug: microsoft-azure-service-fabric-imagestore-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Infrastructure API from Azure Service Fabric — 2 operation(s) for infrastructure.
  name: Azure Service Fabric Infrastructure API
  slug: microsoft-azure-service-fabric-infrastructure-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ListUpgradableVersions API from Azure Service Fabric — 1 operation(s) for listupgradableversions.
  name: Azure Service Fabric List Upgradable Versions API
  slug: microsoft-azure-service-fabric-listupgradableversions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ManagedApplyMaintenanceWindow API from Azure Service Fabric — 1 operation(s) for managedapplymaintenancewindow.
  name: Azure Service Fabric Managed Apply Maintenance Window API
  slug: microsoft-azure-service-fabric-managedapplymaintenancewindow-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ManagedAzResiliencyStatus API from Azure Service Fabric — 1 operation(s) for managedazresiliencystatus.
  name: Azure Service Fabric Managed Az Resiliency Status API
  slug: microsoft-azure-service-fabric-managedazresiliencystatus-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ManagedClusters API from Azure Service Fabric — 3 operation(s) for managedclusters.
  name: Azure Service Fabric Managed Clusters API
  slug: microsoft-azure-service-fabric-managedclusters-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ManagedClusterVersion API from Azure Service Fabric — 4 operation(s) for managedclusterversion.
  name: Azure Service Fabric Managed Cluster Version API
  slug: microsoft-azure-service-fabric-managedclusterversion-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ManagedMaintenanceWindowStatus API from Azure Service Fabric — 1 operation(s) for managedmaintenancewindowstatus.
  name: Azure Service Fabric Managed Maintenance Window Status API
  slug: microsoft-azure-service-fabric-managedmaintenancewindowstatus-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ManagedVMSizes API from Azure Service Fabric — 2 operation(s) for managedvmsizes.
  name: Azure Service Fabric Managed VM Sizes API
  slug: microsoft-azure-service-fabric-managedvmsizes-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshApplications API from Azure Service Fabric — 3 operation(s) for meshapplications.
  name: Azure Service Fabric Mesh Applications API
  slug: microsoft-azure-service-fabric-meshapplications-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshCodePackages API from Azure Service Fabric — 1 operation(s) for meshcodepackages.
  name: Azure Service Fabric Mesh Code Packages API
  slug: microsoft-azure-service-fabric-meshcodepackages-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshGateways API from Azure Service Fabric — 2 operation(s) for meshgateways.
  name: Azure Service Fabric Mesh Gateways API
  slug: microsoft-azure-service-fabric-meshgateways-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshNetworks API from Azure Service Fabric — 2 operation(s) for meshnetworks.
  name: Azure Service Fabric Mesh Networks API
  slug: microsoft-azure-service-fabric-meshnetworks-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshSecrets API from Azure Service Fabric — 2 operation(s) for meshsecrets.
  name: Azure Service Fabric Mesh Secrets API
  slug: microsoft-azure-service-fabric-meshsecrets-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshSecretValues API from Azure Service Fabric — 3 operation(s) for meshsecretvalues.
  name: Azure Service Fabric Mesh Secret Values API
  slug: microsoft-azure-service-fabric-meshsecretvalues-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshServiceReplicas API from Azure Service Fabric — 2 operation(s) for meshservicereplicas.
  name: Azure Service Fabric Mesh Service Replicas API
  slug: microsoft-azure-service-fabric-meshservicereplicas-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshServices API from Azure Service Fabric — 2 operation(s) for meshservices.
  name: Azure Service Fabric Mesh Services API
  slug: microsoft-azure-service-fabric-meshservices-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MeshVolumes API from Azure Service Fabric — 2 operation(s) for meshvolumes.
  name: Azure Service Fabric Mesh Volumes API
  slug: microsoft-azure-service-fabric-meshvolumes-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Node API from Azure Service Fabric — 14 operation(s) for node.
  name: Azure Service Fabric Node API
  slug: microsoft-azure-service-fabric-node-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The NodeTypes API from Azure Service Fabric — 8 operation(s) for nodetypes.
  name: Azure Service Fabric Node Types API
  slug: microsoft-azure-service-fabric-nodetypes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The NodeTypeSkus API from Azure Service Fabric — 1 operation(s) for nodetypeskus.
  name: Azure Service Fabric Node Type Skus API
  slug: microsoft-azure-service-fabric-nodetypeskus-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Partition API from Azure Service Fabric — 17 operation(s) for partition.
  name: Azure Service Fabric Partition API
  slug: microsoft-azure-service-fabric-partition-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Property Management API from Azure Service Fabric — 6 operation(s) for property management.
  name: Azure Service Fabric Property Management API
  slug: microsoft-azure-service-fabric-property-management-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RepairManagement API from Azure Service Fabric — 7 operation(s) for repairmanagement.
  name: Azure Service Fabric Repair Management API
  slug: microsoft-azure-service-fabric-repairmanagement-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Replica API from Azure Service Fabric — 9 operation(s) for replica.
  name: Azure Service Fabric Replica API
  slug: microsoft-azure-service-fabric-replica-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Service API from Azure Service Fabric — 14 operation(s) for service.
  name: Azure Service Fabric Service API
  slug: microsoft-azure-service-fabric-service-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Service Package API from Azure Service Fabric — 5 operation(s) for service package.
  name: Azure Service Fabric Service Package API
  slug: microsoft-azure-service-fabric-service-package-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Services API from Azure Service Fabric — 3 operation(s) for services.
  name: Azure Service Fabric Services API
  slug: microsoft-azure-service-fabric-services-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ServiceType API from Azure Service Fabric — 5 operation(s) for servicetype.
  name: Azure Service Fabric Service Type API
  slug: microsoft-azure-service-fabric-servicetype-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Subscriptions API from Azure Service Fabric — 2 operation(s) for subscriptions.
  name: Azure Service Fabric Subscriptions API
  slug: microsoft-azure-service-fabric-subscriptions-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Backup Restore API from Azure Service Fabric — 29 operation(s) for backup restore.
  name: Azure Service Fabric Backup Restore API
  slug: microsoft-azure-service-fabric-backup-restore-api
artifact_total: 85
collections:
- collection_type: open
  name: Azure Service Fabric REST Clusters API
  slug: open-microsoft-azure-service-fabric-clusters-api
- collection_type: open
  name: Azure Service Fabric REST Clusters Operations API
  slug: open-microsoft-azure-service-fabric-operations-api
- collection_type: open
  name: Azure Service Fabric REST API
  slug: open-microsoft-azure-service-fabric
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/rules/microsoft-azure-service-fabric-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-service-fabric-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/json-ld/microsoft-azure-service-fabric-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-service-fabric-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/vocabulary/microsoft-azure-service-fabric-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-service-fabric-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/data-model/microsoft-azure-service-fabric-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-service-fabric-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/cli/microsoft-azure-service-fabric-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-service-fabric-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/conventions/microsoft-azure-service-fabric-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-service-fabric-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/lifecycle/microsoft-azure-service-fabric-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-service-fabric-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/errors/microsoft-azure-service-fabric-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-service-fabric-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/conformance/microsoft-azure-service-fabric-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-service-fabric-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/llms/microsoft-azure-service-fabric-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-service-fabric-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/well-known/microsoft-azure-service-fabric-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-service-fabric-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/well-known/microsoft-azure-service-fabric-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-service-fabric-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/hosts/microsoft-azure-service-fabric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-service-fabric-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/vendors/microsoft-azure-service-fabric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-service-fabric-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/packages/microsoft-azure-service-fabric-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-service-fabric-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/packages/microsoft-azure-service-fabric-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-service-fabric-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/azuredevcommunityblog
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/security/microsoft-azure-service-fabric-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-service-fabric-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/security/microsoft-azure-service-fabric-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-service-fabric-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/plans/microsoft-azure-service-fabric-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-service-fabric-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/rate-limits/microsoft-azure-service-fabric-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-service-fabric-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/finops/microsoft-azure-service-fabric-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-service-fabric-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/capabilities/microsoft-azure-service-fabric-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-service-fabric-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://microsoft.com
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/agentic-access/microsoft-azure-service-fabric-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-service-fabric-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/security/microsoft-azure-service-fabric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-service-fabric-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/authentication/microsoft-azure-service-fabric-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-service-fabric-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-service-fabric/scopes/microsoft-azure-service-fabric-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-service-fabric-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/service-fabric/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/service-fabric/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/service-fabric/service-fabric-quickstart-containers
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-service-fabric
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Service Fabric REST API provides management of microservices clusters, applications, and services. It supports creating and scaling clusters, deploying applications, managing partitions and replicas, and monitoring cluster health for distributed systems.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Service Fabric Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-service-fabric-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-service-fabric.png
json_schemas:
- name: ApplicationFetchHealthRequest
  property_count: 5
  slug: microsoft-azure-service-fabric-application-fetch-health-request
- name: ApplicationResourceList
  property_count: 2
  slug: microsoft-azure-service-fabric-application-resource-list
- name: ApplicationResource
  property_count: 9
  slug: microsoft-azure-service-fabric-application-resource
- name: ApplicationTypeResourceList
  property_count: 2
  slug: microsoft-azure-service-fabric-application-type-resource-list
- name: ApplicationTypeVersionResourceList
  property_count: 2
  slug: microsoft-azure-service-fabric-application-type-version-resource-list
- name: ApplicationTypeVersionResource
  property_count: 8
  slug: microsoft-azure-service-fabric-application-type-version-resource
- name: ApplicationUpdateDescription
  property_count: 5
  slug: microsoft-azure-service-fabric-application-update-description
- name: ChaosParameters
  property_count: 9
  slug: microsoft-azure-service-fabric-chaos-parameters
- name: ClusterCodeVersionsListResult
  property_count: 2
  slug: microsoft-azure-service-fabric-cluster-code-versions-list-result
- name: ClusterConfigurationUpgradeDescription
  property_count: 11
  slug: microsoft-azure-service-fabric-cluster-configuration-upgrade-description
- name: ClusterHealthPolicy
  property_count: 5
  slug: microsoft-azure-service-fabric-cluster-health-policy
- name: ClusterListResult
  property_count: 2
  slug: microsoft-azure-service-fabric-cluster-list-result
- name: Cluster
  property_count: 8
  slug: microsoft-azure-service-fabric-cluster
- name: ClusterUpdateParameters
  property_count: 2
  slug: microsoft-azure-service-fabric-cluster-update-parameters
- name: LongRunningOperationResult
  property_count: 6
  slug: microsoft-azure-service-fabric-long-running-operation-result
- name: ManagedCluster
  property_count: 3
  slug: microsoft-azure-service-fabric-managed-cluster
- name: ManagedMaintenanceWindowStatus
  property_count: 7
  slug: microsoft-azure-service-fabric-managed-maintenance-window-status
- name: NodeInfo
  property_count: 21
  slug: microsoft-azure-service-fabric-node-info
- name: OperationListResult
  property_count: 2
  slug: microsoft-azure-service-fabric-operation-list-result
- name: OperationList
  property_count: 2
  slug: microsoft-azure-service-fabric-operation-list
- name: RestartDeployedCodePackageRequest
  property_count: 5
  slug: microsoft-azure-service-fabric-restart-deployed-code-package-request
- name: RestartReplicaRequest
  property_count: 5
  slug: microsoft-azure-service-fabric-restart-replica-request
- name: ServiceResourceList
  property_count: 2
  slug: microsoft-azure-service-fabric-service-resource-list
- name: ServiceUpdateDescription
  property_count: 11
  slug: microsoft-azure-service-fabric-service-update-description
- name: UpgradableVersionPathResult
  property_count: 1
  slug: microsoft-azure-service-fabric-upgradable-version-path-result
jsonld:
- class_count: 120
  name: Microsoft Azure Service Fabric Context
  property_count: 216
  slug: microsoft-azure-service-fabric-context
layout: provider
modified: '2026-11-05'
name: Azure Service Fabric
nav: Providers
network: true
overview: 'Azure Service Fabric publishes 46 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clusters API, Operations API, Applications API, and 43 more. Tagged areas include Microservices, Distributed Systems, Containers, Container Orchestration, and Service Fabric.


  The Azure Service Fabric catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Service Fabric''s developer surface includes CLI, changelog, engineering blog, authentication, developer portal, pricing, documentation, and 36 more developer resources.'
plans:
- name: Microsoft Azure Service Fabric Plans Pricing
  plan_count: 6
  slug: microsoft-azure-service-fabric-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Microsoft Azure Service Fabric Rate Limits
  slug: microsoft-azure-service-fabric-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Azure Service Fabric API Rules
  rule_count: 52
  severity_counts:
    error: 35
    hint: 0
    info: 3
    warn: 14
  slug: microsoft-azure-service-fabric-rules
scopes:
- name: Microsoft Azure Service Fabric Scopes
  scope_count: 1
  slug: microsoft-azure-service-fabric-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 65.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.9
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 53.9
    developer_ergonomics: 61.9
    discoverability: 87.5
    operational_transparency: 52.6
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 47
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-service-fabric/microsoft-azure-service-fabric-2026-06-20T185437.png
security:
- kind: authentication
  name: Microsoft Azure Service Fabric Authentication
  slug: microsoft-azure-service-fabric-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Service Fabric Domain Security
  slug: microsoft-azure-service-fabric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Service Fabric Vulnerability Disclosure
  slug: microsoft-azure-service-fabric-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Service Fabric Trust Center
  slug: microsoft-azure-service-fabric-trust-center
  summary_line: GDPR
slug: microsoft-azure-service-fabric
tags:
- Microservices
- Distributed Systems
- Containers
- Container Orchestration
- Service Fabric
- Microsoft Azure
- Cluster Management
website: https://microsoft.com
---
