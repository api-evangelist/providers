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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
api_count: 62
apis:
- description: Access Keys allow users to authenticate and interact programmatically with the NVIDIA Run:ai API. Each access key consists of a client ID and secret that can be used to obtain authentication tokens. A
  name: NVIDIA Run:ai Access Keys API
  slug: runai-access-keys-api
- description: Access rules provide user authorization to system resources and entities. It is managed using Role-based access control (RBAC) which is a policy-neutral access control mechanism defined around roles a
  name: NVIDIA Run:ai Access rules API
  slug: runai-access-rules-api
- description: Information specific to the Administrator Command Line Interface.
  name: NVIDIA Run:ai Administrator Command Line Interface API
  slug: runai-administrator-command-line-interface-api
- description: AI Applications.
  name: NVIDIA Run:ai AI Applications API
  slug: runai-ai-applications-api
- description: '**DEPRECATED:** Applications have been renamed to Service Accounts. Please use the [Service Accounts](/latest/#tag/Service-Accounts) endpoints instead. Create and manage applications in the tenant.'
  name: NVIDIA Run:ai Applications API
  slug: runai-applications-api
- description: The audit log provides audit trail information for user activity, changes to business objects and other important information. For more information, see [Audit log](https://run-ai-docs.nvidia.com/saas
  name: NVIDIA Run:ai AuditLogs API
  slug: runai-auditlogs-api
- description: Use these endpoints to create, manage and delete NVIDIA Run:ai Kubernetes clusters.
  name: NVIDIA Run:ai Clusters API
  slug: runai-clusters-api
- description: A compute resource is a building block that represents compute resources such as GPUs, CPU cores, and CPU memory. The compute resources may consist of multiple physical resources, for example, 0.5 GPU
  name: NVIDIA Run:ai Compute API
  slug: runai-compute-api
- description: Use a ConfigMap as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai ConfigMap API
  slug: runai-configmap-api
- description: Credentials are used to unlock protected resources such as applications, containers, and other assets. For more information, see [Credentials](https://run-ai-docs.nvidia.com/saas/workloads-in-nvidia-r
  name: NVIDIA Run:ai Credentials API
  slug: runai-credentials-api
- description: Data source assets.
  name: NVIDIA Run:ai Datasources API
  slug: runai-datasources-api
- description: The Datavolumes API from NVIDIA Run:ai — 5 operation(s) for datavolumes.
  name: NVIDIA Run:ai Datavolumes API
  slug: runai-datavolumes-api
- description: Departments, in the hierarchy of resource allocation, are above Projects. A Department can contain multiple Projects, and has its own quotas. A Department's quota supersedes the total of the Project q
  name: NVIDIA Run:ai Departments API
  slug: runai-departments-api
- description: Distributed Training, is the ability to split the training of a model among multiple processors. It is often a necessity when multi-GPU training no longer applies; typically when you require more GPUs
  name: NVIDIA Run:ai Distributed API
  slug: runai-distributed-api
- description: Distributed inference enables running inference workloads across multiple pods, typically to scale model serving beyond a single container or node. This approach is useful when a single instance canno
  name: NVIDIA Run:ai Distributed Inferences API
  slug: runai-distributed-inferences-api
- description: An environment resource designates the container image, the image pull policy, working directory, security parameters, and others. It exposes all the necessary tools (open source, 3rd party, or custom
  name: NVIDIA Run:ai Environment API
  slug: runai-environment-api
- description: Workload events that occurred while the workload was running. Use to diagnose issue around workload scheduling.
  name: NVIDIA Run:ai Events API
  slug: runai-events-api
- description: Use Git as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai Git API
  slug: runai-git-api
- description: Use a HostPath as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai HostPath API
  slug: runai-hostpath-api
- description: The Idps API from NVIDIA Run:ai — 3 operation(s) for idps.
  name: NVIDIA Run:ai Idps API
  slug: runai-idps-api
- description: 'Inference workloads deploy trained models into a production environment to generate predictions from live data. These workloads are prioritized over Trainings and Workspaces during scheduling. NVIDIA '
  name: NVIDIA Run:ai Inferences API
  slug: runai-inferences-api
- description: Use to manage tenant logo files.
  name: NVIDIA Run:ai Logo API
  slug: runai-logo-api
- description: '"Me" returns the authenticated user''s permissions within the system. It provides a comprehensive view of access rules (roles, subjects and scope) assigned to the current user. For more information see'
  name: NVIDIA Run:ai Me API
  slug: runai-me-api
- description: The Network Topologies API enables administrators to reflect the hierarchical network topology connectivity of nodes in a data center, such as racks, blocks, and other organizational units, to improve
  name: NVIDIA Run:ai Network Topologies API
  slug: runai-network-topologies-api
- description: Use NFS as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai NFS API
  slug: runai-nfs-api
- description: 'Node pools assist in managing heterogeneous resources effectively. A node pool is a set of nodes grouped into a bucket of resources using a predefined (for example, GPU-Type) or administrator-defined '
  name: NVIDIA Run:ai NodePools API
  slug: runai-nodepools-api
- description: 'Nodes are worker machines in Kubernetes and may be either a virtual or a physical machine, depending on the cluster. Each Node is managed by the NVIDIA Run:ai control plane. For more information, see '
  name: NVIDIA Run:ai Nodes API
  slug: runai-nodes-api
- description: Use to manage notification state.
  name: NVIDIA Run:ai Notification State API
  slug: runai-notification-state-api
- description: Use to get notification types.
  name: NVIDIA Run:ai Notification Types API
  slug: runai-notification-types-api
- description: Notification Channels are the medium through which notifications are sent.
  name: NVIDIA Run:ai NotificationChannels API
  slug: runai-notificationchannels-api
- description: The NVIDIA NIM API provides endpoints to create and manage workloads that deploy NVIDIA Inference Microservices (NIM) through the NIM Operator. These workloads package optimized NVIDIA model servers a
  name: NVIDIA Run:ai NVIDIA NIM API
  slug: runai-nvidia-nim-api
- description: Org unit.
  name: NVIDIA Run:ai Org unit API
  slug: runai-org-unit-api
- description: The Permissions API from NVIDIA Run:ai — 2 operation(s) for permissions.
  name: NVIDIA Run:ai Permissions API
  slug: runai-permissions-api
- description: Retrieve data about workload pods from your NVIDIA Run:ai platform.
  name: NVIDIA Run:ai Pods API
  slug: runai-pods-api
- description: 'Policies allow administrators to impose restrictions and set default values for researcher workloads. Restrictions and default values can be placed on CPUs, GPUs, and other resources or entities. For '
  name: NVIDIA Run:ai Policy API
  slug: runai-policy-api
- description: Projects implement resource allocation policies and create segregation between different initiatives. It can represent a team, an individual, or an initiative that shares resources or has a specific r
  name: NVIDIA Run:ai Projects API
  slug: runai-projects-api
- description: Use a PVC as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai PVC API
  slug: runai-pvc-api
- description: Use an images registry to enable the listting of repositories and tags that can be used as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai Registry API
  slug: runai-registry-api
- description: The Reports API from NVIDIA Run:ai — 5 operation(s) for reports.
  name: NVIDIA Run:ai Reports API
  slug: runai-reports-api
- description: The Researcher Command Line Interface API from NVIDIA Run:ai — 9 operation(s) for researcher command line interface.
  name: NVIDIA Run:ai Researcher Command Line Interface API
  slug: runai-researcher-command-line-interface-api
- description: The Researcher Command Line Interface Deprecated API from NVIDIA Run:ai — 9 operation(s) for researcher command line interface deprecated.
  name: NVIDIA Run:ai Researcher Command Line Interface Deprecated API
  slug: runai-researcher-command-line-interface-deprecated-api
- description: Revisions are associated with an inference workload and represent a snapshot of its configuration. A revision is created on each change to the inference workload.
  name: NVIDIA Run:ai Revisions API
  slug: runai-revisions-api
- description: A role is a group of permissions that can be granted. Permissions are a set of actions that can be applied to entities. For more information, see [Roles](https://run-ai-docs.nvidia.com/saas/infrastruc
  name: NVIDIA Run:ai Roles API
  slug: runai-roles-api
- description: Use an S3 simple storage service as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai S3 API
  slug: runai-s3-api
- description: Use a credentials as a data source location for data sets that are relevant to the workload being submitted.
  name: NVIDIA Run:ai Secret API
  slug: runai-secret-api
- description: Service accounts enable programmatic access to the NVIDIA Run:ai API, allowing applications or automated systems to authenticate and interact securely. Each service account is associated with an acces
  name: NVIDIA Run:ai Service Accounts API
  slug: runai-service-accounts-api
- description: View and manage configuration settings for your organization.
  name: NVIDIA Run:ai Settings API
  slug: runai-settings-api
- description: The storage class configuration API enables administrators to define, manage, and customize how storage classes are used across the NVIDIA Run:ai platform. Through this API, you can configure access m
  name: NVIDIA Run:ai Storage Class Configuration API
  slug: runai-storage-class-configuration-api
- description: The Storage Classes API retrieves a list of available, pre-defined storage classes in the system.
  name: NVIDIA Run:ai Storage Classes API
  slug: runai-storage-classes-api
- description: Use to manage notifications subscriptions.
  name: NVIDIA Run:ai Subscriptions API
  slug: runai-subscriptions-api
- description: Templates are a pre-set configuration used to quickly configure and submit workloads using existing assets.
  name: NVIDIA Run:ai Template API
  slug: runai-template-api
- description: Manage tenant settings.
  name: NVIDIA Run:ai Tenant API
  slug: runai-tenant-api
- description: Use tokens to facilitate authentication to the NVIDIA Run:ai API. The API server must be configured to use the NVIDIA Run:ai identity service to validate authentication tokens.
  name: NVIDIA Run:ai Tokens API
  slug: runai-tokens-api
- description: Trainings are dedicated workloads that are specifically used for training models. They are by design preemptible workloads because they are used in unattended sessions where the scientists and researc
  name: NVIDIA Run:ai Trainings API
  slug: runai-trainings-api
- description: '**DEPRECATED:** User Applications have been renamed to Access Keys. Please use the [Access Keys](/latest/#tag/Access-Keys) endpoints instead. User Applications allow users to authenticate and interact'
  name: NVIDIA Run:ai User Applications API
  slug: runai-user-applications-api
- description: The Users API from NVIDIA Run:ai — 6 operation(s) for users.
  name: NVIDIA Run:ai Users API
  slug: runai-users-api
- description: Workload properties define the behavioral and scheduling characteristics of a workload submitted to the NVIDIA Run:ai platform. These properties such as type, category, and priority determine how work
  name: NVIDIA Run:ai Workload properties API
  slug: runai-workload-properties-api
- description: This set of endpoints manages workload templates used to define reusable workload configurations across various workload types in the NVIDIA Run:ai platform. Templates help standardize workload defini
  name: NVIDIA Run:ai Workload templates API
  slug: runai-workload-templates-api
- description: Workloads are both native platform workloads, Workspaces, Training and Inference, as well as workloads that originate from third-party ML frameworks, tools, or the broader Kubernetes ecosystems. For m
  name: NVIDIA Run:ai Workloads API
  slug: runai-workloads-api
- description: The Workloads batch API from NVIDIA Run:ai — 1 operation(s) for workloads batch.
  name: NVIDIA Run:ai Workloads batch API
  slug: runai-workloads-batch-api
- description: The Workloads V2 API allows you to create, retrieve, and delete workloads that originate from third-party ML frameworks, tools, or the broader Kubernetes ecosystem. These workloads are registered in t
  name: NVIDIA Run:ai Workloads V2 API
  slug: runai-workloads-v2-api
- description: A Workspace is a simplified tool for researchers to conduct experiments, build AI models, access standard MLOps tools, and collaborate with their peers. Workspaces abstract complex concepts related to
  name: NVIDIA Run:ai Workspaces API
  slug: runai-workspaces-api
artifact_total: 65
common:
- group: company
  title: ''
  type: Website
  url: https://www.nvidia.com/en-us/software/run-ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://run-ai-docs.nvidia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://run-ai-docs.nvidia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://run-ai-docs.nvidia.com/api/readme.md
- group: start
  title: ''
  type: GettingStarted
  url: https://run-ai-docs.nvidia.com/saas/getting-started/quick-starts.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/run-ai
- group: start
  title: ''
  type: Login
  url: https://app.run.ai/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/runai-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/runai-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/runai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/runai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/runai-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/runai-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/runai-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/runai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/runai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/runai-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/runai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/runai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/runai-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runai-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/runai-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nvidia.com/en-us/about-nvidia/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nvidia.com/en-us/about-nvidia/privacy-policy/
created: '2026-07-17'
description: NVIDIA Run:ai (formerly run.ai) is an AI operations and GPU orchestration platform for Kubernetes that pools, schedules, and governs GPU compute across clusters for training, fine-tuning, and inference workloads. It provides fractional GPU sharing, dynamic scheduling, quota and policy management, multi-tenant projects and departments, and workload lifecycle control across SaaS, self-hosted, and multi-tenant deployments. run.ai was founded in Israel, backed by Insight Partners and other investors, and acquired by NVIDIA in 2024; the product is now delivered as NVIDIA Run:ai. Its control-plane REST API exposes programmatic management of clusters, node pools, projects, departments, workloads (workspaces, trainings, inferences, distributed), assets, policies, permissions, service accounts, and audit logs, authenticated with bearer JWT access tokens obtained from client-credentials access keys.
image: https://avatars.githubusercontent.com/u/37841801?v=4
layout: provider
mcp_servers:
- description: ''
  name: runai-mcp.yml
  slug: runai-mcpyml
modified: '2026-07-21'
name: NVIDIA Run:ai
nav: Providers
network: true
overview: 'NVIDIA Run:ai publishes 62 APIs on the [APIs.io](https://apis.io/) network, including Access Keys API, Access rules API, Administrator Command Line Interface API, and 59 more. Tagged areas include Company, Artificial Intelligence, GPU, Machine Learning, and Kubernetes.


  NVIDIA Run:ai''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, and 20 more developer resources.'
random_paper: 67
score:
  band: developing
  composite: 48.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.9
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 48.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Runai Authentication
  slug: runai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runai Domain Security
  slug: runai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: runai
tags:
- Company
- Artificial Intelligence
- GPU
- Machine Learning
- Kubernetes
- Orchestration
- MLOps
- Compute
- Scheduling
- Infrastructure
website: https://www.nvidia.com/en-us/software/run-ai/
---
