---
aid: pure-storage
url: https://github.com/api-evangelist/pure-storage/blob/main/apis.yml
name: Pure Storage
type: Index
image: https://avatars.githubusercontent.com/u/8324560
tags:
  - Storage
  - Data Storage
  - Flash Storage
  - Enterprise Storage
  - Cloud Storage
  - Object Storage
  - File Storage
  - Block Storage
  - Kubernetes Storage
  - Infrastructure
description: Pure Storage is an American publicly traded technology company specializing in all-flash data storage hardware and software products. The company provides enterprise data storage platforms including FlashArray, FlashBlade, and Pure1 fleet management, along with Portworx for Kubernetes data services. Pure Storage offers REST APIs, SDKs, CRDs, and developer tooling that enable programmatic management of storage infrastructure and integration with automation workflows across block, file, and object storage.
created: '2026-05-04'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: pure-storage:flasharray-rest-api
    name: FlashArray REST API
    humanURL: https://code.purestorage.com/swagger
    description: REST API for managing Pure Storage FlashArray, the company's all-flash storage array platform. Provides programmatic control over arrays, volumes, hosts, snapshots, replication, protection groups, pods, and other storage resources.
    tags:
      - FlashArray
      - REST API
      - Block Storage
      - Storage Management
    properties:
      - type: APIReference
        url: https://code.purestorage.com/swagger
      - type: Documentation
        url: https://code.purestorage.com
      - type: OpenAPI
        url: openapi/flasharray-rest-api-openapi.yml
      - type: SDK
        url: https://pypi.org/project/py-pure-client/
        title: Python SDK (py-pure-client)
      - type: SDK
        url: https://github.com/PureStorage-OpenConnect/PureStorage.Pure1
        title: PowerShell Module
      - type: SDK
        url: https://github.com/PureStorage-OpenConnect/powershell-toolkit-3
        title: PowerShell Toolkit 3.x
      - type: SDK
        url: https://github.com/PureStorage-OpenConnect/rest-client
        title: Python REST 1.x Client (legacy)
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/ansible-playbook-examples
        title: Ansible Playbook Examples
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/python-scripts
        title: Python Sample Scripts
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/sqlserver-scripts
        title: SQL Server Scripts
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/oracle-scripts
        title: Oracle Scripts
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/VMware-Scripts
        title: VMware Scripts
      - type: Integrations
        url: https://github.com/PureStorage-OpenConnect/terraform-provider-flash
        title: Terraform Provider for FlashArray
      - type: Integrations
        url: https://github.com/PureStorage-OpenConnect/pure-fa-openmetrics-exporter
        title: FlashArray OpenMetrics Exporter
      - type: JSONSchema
        url: json-schema/flasharray-rest-api-array-schema.json
        title: Array Schema
      - type: JSONSchema
        url: json-schema/flasharray-rest-api-volume-schema.json
        title: Volume Schema
      - type: JSONSchema
        url: json-schema/flasharray-rest-api-host-schema.json
        title: Host Schema
      - type: JSONStructure
        url: json-structure/flasharray-rest-api-array-structure.json
        title: Array Structure
      - type: JSONStructure
        url: json-structure/flasharray-rest-api-volume-structure.json
        title: Volume Structure
      - type: JSON-LD
        url: json-ld/pure-storage-flasharray-rest-api-context.jsonld
        title: FlashArray JSON-LD Context
      - type: Example
        url: examples/flasharray-rest-api-volume-example.json
        title: Volume Example
      - type: Example
        url: examples/flasharray-rest-api-array-example.json
        title: Array Example
      - type: NaftikoCapability
        url: capabilities/shared/flasharray-rest-api.yaml
        title: FlashArray Shared Capability
  - aid: pure-storage:flashblade-rest-api
    name: FlashBlade REST API
    humanURL: https://code.purestorage.com/swagger
    description: REST API for managing Pure Storage FlashBlade, the unified fast file and object storage platform. Provides programmatic access to file systems, S3-compatible object stores, buckets, network configuration, policies, snapshots, and platform management.
    tags:
      - FlashBlade
      - REST API
      - Object Storage
      - File Storage
    properties:
      - type: APIReference
        url: https://code.purestorage.com/swagger
      - type: Documentation
        url: https://code.purestorage.com
      - type: OpenAPI
        url: openapi/flashblade-rest-api-openapi.yml
      - type: SDK
        url: https://pypi.org/project/py-pure-client/
        title: Python SDK (py-pure-client)
      - type: SDK
        url: https://github.com/PureStorage-OpenConnect/flashblade-powershell
        title: FlashBlade PowerShell Module
      - type: SDK
        url: https://github.com/purestorage/purity_fb_python_client
        title: Purity//FB Python Client (legacy)
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/ansible-playbook-examples
        title: Ansible Playbook Examples
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/python-scripts
        title: Python Sample Scripts
      - type: Integrations
        url: https://github.com/PureStorage-OpenConnect/pure-fb-openmetrics-exporter
        title: FlashBlade OpenMetrics Exporter
      - type: Tools
        url: https://github.com/PureStorage-OpenConnect/flashblade-mcp-server
        title: FlashBlade MCP Server
      - type: JSONSchema
        url: json-schema/flashblade-rest-api-file-system-schema.json
        title: File System Schema
      - type: JSONSchema
        url: json-schema/flashblade-rest-api-bucket-schema.json
        title: Bucket Schema
      - type: JSONSchema
        url: json-schema/flashblade-rest-api-array-schema.json
        title: Array Schema
      - type: JSONStructure
        url: json-structure/flashblade-rest-api-file-system-structure.json
        title: File System Structure
      - type: JSONStructure
        url: json-structure/flashblade-rest-api-bucket-structure.json
        title: Bucket Structure
      - type: JSON-LD
        url: json-ld/pure-storage-flashblade-rest-api-context.jsonld
        title: FlashBlade JSON-LD Context
      - type: Example
        url: examples/flashblade-rest-api-file-system-example.json
        title: File System Example
      - type: Example
        url: examples/flashblade-rest-api-bucket-example.json
        title: Bucket Example
      - type: NaftikoCapability
        url: capabilities/shared/flashblade-rest-api.yaml
        title: FlashBlade Shared Capability
  - aid: pure-storage:pure1-cloud-api
    name: Pure1 Public REST API
    humanURL: https://code.purestorage.com/swagger
    description: REST API for the Pure1 SaaS fleet management platform. Provides cross-array reporting, telemetry, capacity and performance metrics, alerts, audits, sustainability data, support contracts, and subscription information across the entire Pure Storage fleet.
    tags:
      - Pure1
      - Cloud
      - Fleet Management
      - Telemetry
      - REST API
    properties:
      - type: APIReference
        url: https://static.pure1.purestorage.com/api-swagger/index.html
      - type: Documentation
        url: https://support.purestorage.com/Pure1/Pure1_Manage/Pure1_Manage_-_REST_API/Pure1_Manage_-_REST_API__Reference
      - type: OpenAPI
        url: openapi/pure1-cloud-api-openapi.yml
      - type: SDK
        url: https://pypi.org/project/py-pure-client/
        title: Python SDK (py-pure-client)
      - type: SDK
        url: https://github.com/PureStorage-OpenConnect/PureStorage.Pure1
        title: Pure1 PowerShell Module
      - type: CodeExamples
        url: https://github.com/PureStorage-OpenConnect/python-scripts
        title: Pure1 Python Samples
      - type: JSONSchema
        url: json-schema/pure1-cloud-api-array-schema.json
        title: Array Schema
      - type: JSONSchema
        url: json-schema/pure1-cloud-api-metric-schema.json
        title: Metric Schema
      - type: JSONSchema
        url: json-schema/pure1-cloud-api-alert-schema.json
        title: Alert Schema
      - type: JSONStructure
        url: json-structure/pure1-cloud-api-array-structure.json
        title: Array Structure
      - type: JSON-LD
        url: json-ld/pure-storage-pure1-cloud-api-context.jsonld
        title: Pure1 JSON-LD Context
      - type: Example
        url: examples/pure1-cloud-api-array-example.json
        title: Array Example
      - type: NaftikoCapability
        url: capabilities/shared/pure1-cloud-api.yaml
        title: Pure1 Shared Capability
  - aid: pure-storage:portworx-kubernetes-api
    name: Portworx Kubernetes API
    humanURL: https://docs.portworx.com
    description: Kubernetes-native data services platform from Pure Storage. Portworx exposes its API surface through Custom Resource Definitions managed by the libopenstorage operator and the portworx/apis CRDs, enabling declarative management of storage clusters, storage nodes, diagnostics, and volume populators on Kubernetes.
    tags:
      - Portworx
      - Kubernetes
      - CRD
      - Data Services
      - Cloud Native
    properties:
      - type: Documentation
        url: https://docs.portworx.com
      - type: GitHubRepository
        url: https://github.com/libopenstorage/operator
      - type: GitHubRepository
        url: https://github.com/portworx/apis
      - type: KubernetesCRD
        url: crd/pure-storage-portworx-storagecluster.yaml
        title: StorageCluster CRD (core.libopenstorage.org/v1)
      - type: KubernetesCRD
        url: crd/pure-storage-portworx-storagenode.yaml
        title: StorageNode CRD (core.libopenstorage.org/v1)
      - type: KubernetesCRD
        url: crd/pure-storage-portworx-portworxdiag.yaml
        title: PortworxDiag CRD (portworx.io/v1)
      - type: KubernetesCRD
        url: crd/pure-storage-portworx-xcopyvolumepopulator.yaml
        title: PortworxXcopyVolumePopulator CRD (portworx.io/v1beta1)
      - type: SDK
        url: https://github.com/PureStorage-OpenConnect/fusion-python-sdk
        title: Pure Fusion Python SDK
      - type: Tools
        url: https://github.com/portworx/helm
        title: Portworx Helm Charts
      - type: Tools
        url: https://github.com/PureStorage-OpenConnect/px-deploy
        title: px-deploy
      - type: Integrations
        url: https://github.com/libopenstorage/stork
        title: Stork Storage Orchestration Runtime
      - type: Integrations
        url: https://github.com/portworx/kdmp
        title: Kubernetes Data Management Platform
common:
  - type: Website
    url: https://www.purestorage.com
  - type: DeveloperPortal
    url: https://code.purestorage.com
  - type: Documentation
    url: https://code.purestorage.com
  - type: APIReference
    url: https://code.purestorage.com/swagger
  - type: SDK
    url: https://github.com/PureStorage-OpenConnect/py-pure-client
    title: py-pure-client (Unified Python SDK)
  - type: Tools
    url: https://github.com/PureStorage-OpenConnect/swagger
    title: Swagger UI for FA / FB / Pure1
  - type: Tools
    url: https://github.com/PureStorage-OpenConnect/flashblade-mcp-server
    title: FlashBlade MCP Server
  - type: CLI
    url: https://github.com/PureStorage-OpenConnect/px-deploy
    title: px-deploy
  - type: Support
    url: https://support.purestorage.com
  - type: KnowledgeCenter
    url: https://supportcenter.purestorage.com
  - type: GitHubOrganization
    url: https://github.com/PureStorage-OpenConnect
  - type: GitHubOrganization
    url: https://github.com/purestorage
  - type: GitHubOrganization
    url: https://github.com/portworx
  - type: GitHubOrganization
    url: https://github.com/libopenstorage
  - type: Integrations
    url: https://galaxy.ansible.com/purestorage
    title: Ansible Galaxy Collections
  - type: SpectralRules
    url: rules/pure-storage-rules.yml
    title: Pure Storage Spectral Ruleset
  - type: Vocabulary
    url: vocabulary/pure-storage-vocabulary.yml
    title: Pure Storage Vocabulary
  - type: NaftikoCapability
    url: capabilities/storage-fleet-management.yaml
    title: Pure Storage Fleet Management Workflow
  - type: Features
    data:
      - name: All-Flash Storage
        description: Enterprise all-flash storage hardware (FlashArray, FlashBlade) with consistent low-latency performance.
      - name: Unified File and Object Storage
        description: FlashBlade provides scale-out file and S3-compatible object storage from a single platform.
      - name: Cross-Array Fleet Management
        description: Pure1 SaaS provides telemetry, analytics, alerting, and capacity planning across the entire Pure fleet.
      - name: Kubernetes Data Services
        description: Portworx delivers persistent storage, data protection, DR, and migration for Kubernetes workloads.
      - name: Active Cluster Replication
        description: Synchronous replication for zero-RPO active-active configurations across data centers.
      - name: Snapshot and Cloning
        description: Space-efficient snapshots and instant clones for backup, dev/test, and database refresh.
      - name: Sustainability Reporting
        description: Pure1 sustainability metrics expose energy, carbon, and efficiency data per array.
      - name: OAuth 2.0 Token Exchange
        description: All Pure Storage REST APIs authenticate via the OAuth 2.0 token-exchange flow with JWT subject tokens.
  - type: UseCases
    data:
      - name: Database Storage
        description: High-performance storage for SQL Server, Oracle, SAP HANA, PostgreSQL, and other database workloads.
      - name: VMware and Virtualization
        description: Storage backend for VMware vSphere, Hyper-V, KVM, and Nutanix virtualization platforms.
      - name: AI and Machine Learning Pipelines
        description: FlashBlade powers training datasets, vector search, embedding pipelines, and RAG architectures.
      - name: Backup and Disaster Recovery
        description: Snapshot-based backup, replication, and SafeMode immutable snapshots for ransomware recovery.
      - name: Cloud Block Storage
        description: Cloud Block Store extends Pure Storage to AWS, Azure, and other public clouds.
      - name: Container and Kubernetes Storage
        description: Portworx provides dynamic provisioning, snapshots, and DR for Kubernetes stateful workloads.
      - name: Fleet Capacity Planning
        description: Pure1 telemetry feeds capacity forecasting, performance analysis, and lifecycle management.
  - type: Integrations
    data:
      - name: VMware vSphere
        description: First-class integration with vSphere via vCenter plugins, vVols, and SRM workflows.
      - name: Ansible
        description: Official Ansible collections for FlashArray, FlashBlade, and Pure1 published on Ansible Galaxy.
      - name: Terraform
        description: Terraform providers for FlashArray and Cloud Block Store.
      - name: Kubernetes
        description: CSI drivers, the libopenstorage operator, Portworx, Stork, and the Pure Service Orchestrator (PSO).
      - name: OpenStack
        description: Cinder and Manila drivers for FlashArray and FlashBlade.
      - name: Splunk
        description: Splunk apps and TAs ingest Pure Storage telemetry for security and operations dashboards.
      - name: Prometheus / Grafana
        description: OpenMetrics exporters for FlashArray and FlashBlade feed Prometheus-based observability stacks.
      - name: ServiceNow / Jira
        description: Support and incident integrations through Pure1 alerts and webhooks.
  - type: Solutions
    data:
      - name: FlashArray
        description: All-flash block storage arrays for tier-1 enterprise workloads.
      - name: FlashBlade
        description: Unified fast file and object storage for unstructured data and modern analytics.
      - name: Pure1
        description: SaaS-based AI-driven fleet management, analytics, and support platform.
      - name: Portworx
        description: Kubernetes data services platform offering storage, DR, security, and migration.
      - name: Cloud Block Store
        description: FlashArray-as-a-service running natively on AWS and Azure.
      - name: Evergreen Storage
        description: Subscription model for non-disruptive controller and capacity upgrades.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
---
