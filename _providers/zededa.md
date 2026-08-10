---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 179
  human_in_the_loop: 5
  name: Zededa Agentic Access
  operation_count: 421
  slug: zededa-agentic-access
  summary_line: 421 operations · 179 acting · 5 human-in-the-loop
api_count: 35
apis:
- description: The AppProfileService API from Zededa — 5 operation(s) for appprofileservice.
  name: Zededa AppProfileService API
  slug: zededa-appprofileservice-api
- description: The ArtifactManager API from Zededa — 4 operation(s) for artifactmanager.
  name: Zededa ArtifactManager API
  slug: zededa-artifactmanager-api
- description: The AssetGroupService API from Zededa — 3 operation(s) for assetgroupservice.
  name: Zededa AssetGroupService API
  slug: zededa-assetgroupservice-api
- description: The BulkJobOps API from Zededa — 14 operation(s) for bulkjobops.
  name: Zededa BulkJobOps API
  slug: zededa-bulkjobops-api
- description: The CertificateEnrollmentProfileConfiguration API from Zededa — 3 operation(s) for certificateenrollmentprofileconfiguration.
  name: Zededa CertificateEnrollmentProfileConfiguration API
  slug: zededa-certificateenrollmentprofileconfiguration-api
- description: The CloudDiagnostics API from Zededa — 8 operation(s) for clouddiagnostics.
  name: Zededa CloudDiagnostics API
  slug: zededa-clouddiagnostics-api
- description: APIs for managing cluster groups including creation, deletion, status monitoring, and manifest generation
  name: Zededa ClusterGroups API
  slug: zededa-clustergroups-api
- description: The ClusterStatus API from Zededa — 3 operation(s) for clusterstatus.
  name: Zededa ClusterStatus API
  slug: zededa-clusterstatus-api
- description: The DatastoreConfiguration API from Zededa — 4 operation(s) for datastoreconfiguration.
  name: Zededa DatastoreConfiguration API
  slug: zededa-datastoreconfiguration-api
- description: The EdgeApplicationConfiguration API from Zededa — 8 operation(s) for edgeapplicationconfiguration.
  name: Zededa EdgeApplicationConfiguration API
  slug: zededa-edgeapplicationconfiguration-api
- description: The EdgeApplicationInstanceConfiguration API from Zededa — 20 operation(s) for edgeapplicationinstanceconfiguration.
  name: Zededa EdgeApplicationInstanceConfiguration API
  slug: zededa-edgeapplicationinstanceconfiguration-api
- description: The EdgeApplicationInstanceStatus API from Zededa — 35 operation(s) for edgeapplicationinstancestatus.
  name: Zededa EdgeApplicationInstanceStatus API
  slug: zededa-edgeapplicationinstancestatus-api
- description: The EdgeDiagnostics API from Zededa — 12 operation(s) for edgediagnostics.
  name: Zededa EdgeDiagnostics API
  slug: zededa-edgediagnostics-api
- description: The EdgeNetworkConfiguration API from Zededa — 4 operation(s) for edgenetworkconfiguration.
  name: Zededa EdgeNetworkConfiguration API
  slug: zededa-edgenetworkconfiguration-api
- description: The EdgeNetworkInstanceConfiguration API from Zededa — 3 operation(s) for edgenetworkinstanceconfiguration.
  name: Zededa EdgeNetworkInstanceConfiguration API
  slug: zededa-edgenetworkinstanceconfiguration-api
- description: The EdgeNetworkInstanceStatus API from Zededa — 5 operation(s) for edgenetworkinstancestatus.
  name: Zededa EdgeNetworkInstanceStatus API
  slug: zededa-edgenetworkinstancestatus-api
- description: The EdgeNodeClusterConfiguration API from Zededa — 7 operation(s) for edgenodeclusterconfiguration.
  name: Zededa EdgeNodeClusterConfiguration API
  slug: zededa-edgenodeclusterconfiguration-api
- description: The EdgeNodeConfiguration API from Zededa — 23 operation(s) for edgenodeconfiguration.
  name: Zededa EdgeNodeConfiguration API
  slug: zededa-edgenodeconfiguration-api
- description: The EdgeNodeStatus API from Zededa — 13 operation(s) for edgenodestatus.
  name: Zededa EdgeNodeStatus API
  slug: zededa-edgenodestatus-api
- description: The EnterpriseEntitlementsReport API from Zededa — 8 operation(s) for enterpriseentitlementsreport.
  name: Zededa EnterpriseEntitlementsReport API
  slug: zededa-enterpriseentitlementsreport-api
- description: The HardwareModel API from Zededa — 20 operation(s) for hardwaremodel.
  name: Zededa HardwareModel API
  slug: zededa-hardwaremodel-api
- description: APIs for managing Helm charts in Kubernetes clusters. Provides operations for importing, creating, updating, deleting, and retrieving Helm charts from both global and enterprise-specific repositories.
  name: Zededa HelmChartManagement API
  slug: zededa-helmchartmanagement-api
- description: The IdentityAccessManagement API from Zededa — 38 operation(s) for identityaccessmanagement.
  name: Zededa IdentityAccessManagement API
  slug: zededa-identityaccessmanagement-api
- description: The ImageConfiguration API from Zededa — 9 operation(s) for imageconfiguration.
  name: Zededa ImageConfiguration API
  slug: zededa-imageconfiguration-api
- description: APIs for managing Kubernetes deployments
  name: Zededa KubernetesDeployments API
  slug: zededa-kubernetesdeployments-api
- description: APIs for managing GitOps configurations and continuous deployment from Git repositories to Kubernetes clusters
  name: Zededa KubernetesGitOps API
  slug: zededa-kubernetesgitops-api
- description: APIs for managing Kubernetes secrets including SSH keys, basic authentication credentials, and other sensitive data. Supports create, read, and list operations.
  name: Zededa KubernetesSecrets API
  slug: zededa-kubernetessecrets-api
- description: The PatchEnvelopeConfiguration API from Zededa — 4 operation(s) for patchenvelopeconfiguration.
  name: Zededa PatchEnvelopeConfiguration API
  slug: zededa-patchenvelopeconfiguration-api
- description: APIs for managing private Helm repositories and their authentication configurations
  name: Zededa PrivateHelmRepositories API
  slug: zededa-privatehelmrepositories-api
- description: The ProfileDeploymentService API from Zededa — 4 operation(s) for profiledeploymentservice.
  name: Zededa ProfileDeploymentService API
  slug: zededa-profiledeploymentservice-api
- description: The ResourceGroup API from Zededa — 11 operation(s) for resourcegroup.
  name: Zededa ResourceGroup API
  slug: zededa-resourcegroup-api
- description: The ResourceGroupStatus API from Zededa — 4 operation(s) for resourcegroupstatus.
  name: Zededa ResourceGroupStatus API
  slug: zededa-resourcegroupstatus-api
- description: The VolumeInstanceConfiguration API from Zededa — 3 operation(s) for volumeinstanceconfiguration.
  name: Zededa VolumeInstanceConfiguration API
  slug: zededa-volumeinstanceconfiguration-api
- description: The VolumeInstanceStatus API from Zededa — 6 operation(s) for volumeinstancestatus.
  name: Zededa VolumeInstanceStatus API
  slug: zededa-volumeinstancestatus-api
- description: APIs for managing ZKS (ZEDEDA Kubernetes Service) cluster instances including creation, management, node operations, and status monitoring
  name: Zededa ZKSClusterInstances API
  slug: zededa-zksclusterinstances-api
artifact_total: 40
common:
- group: docs
  title: ''
  type: APIReference
  url: https://zedcontrol.zededa.net/api/v1/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zededa.com/hc/en-us
- group: auth
  title: ''
  type: Authentication
  url: authentication/zededa-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/zededa-node_service-openapi.json
- group: design
  title: ''
  type: Conventions
  url: conventions/zededa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zededa-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zededa-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zededa-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zededa-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zededa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.zededa.com/
- group: build
  title: ''
  type: Packages
  url: packages/zededa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zededa-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zededa-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zededa-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zededa-node_service-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zededa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zededa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zededa-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZEDEDA
- group: operate
  title: ''
  type: Support
  url: https://help.zededa.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://zededa.com/resources/blog/
- group: start
  title: ''
  type: Login
  url: https://zedcontrol.gmwtus.zededa.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zededa.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zededa.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://zededa.com
created: '2026-07-17'
description: ZEDEDA is an edge intelligence platform that helps enterprises deploy, manage, and secure AI workloads and applications across thousands of distributed edge sites. Its ZedCloud control plane orchestrates EVE-OS edge nodes, edge applications, virtual networks, storage, and managed Kubernetes (ZKS) through a REST API served under https://zedcontrol.zededa.net/api. The API is grpc-gateway generated and published as ten Swagger 2.0 service specifications (App Profiles, Edge Applications, Diagnostics, Jobs, Kubernetes, Networks, Node Clusters, Edge Nodes, Storage, and IAM) totaling 421 operations, with an official Terraform provider for infrastructure-as-code. ZEDEDA was surfaced as a portfolio company of lux-capital and enriched by the API Evangelist pipeline.
image: https://avatars.githubusercontent.com/u/25070488?v=4
layout: provider
mcp_servers:
- description: ''
  name: zededa-mcp.yml
  slug: zededa-mcpyml
modified: '2026-07-21'
name: Zededa
nav: Providers
network: true
overview: 'Zededa publishes 35 APIs on the [APIs.io](https://apis.io/) network, including AppProfileService API, ArtifactManager API, AssetGroupService API, and 32 more. Tagged areas include Company, Edge Computing, Edge Intelligence, IoT, and Kubernetes.


  Zededa''s developer surface includes API reference, documentation, authentication, support, engineering blog, and 22 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.0
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Zededa Authentication
  slug: zededa-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Zededa Domain Security
  slug: zededa-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Zededa Trust Center
  slug: zededa-trust-center
  summary_line: ISO 27001, HIPAA, FedRAMP
slug: zededa
tags:
- Company
- Edge Computing
- Edge Intelligence
- IoT
- Kubernetes
- Device Management
- Orchestration
- AI at the Edge
website: https://zededa.com
---
