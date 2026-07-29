---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Veritas Infoscale Agentic Access
  operation_count: 32
  slug: veritas-infoscale-agentic-access
  summary_line: 32 operations · 14 acting
api_count: 13
apis:
- description: REST API for centralized monitoring and management of InfoScale environments. Provides meta, query, update, and operational endpoints for managing clusters, service groups, hosts, storage, and extende
  name: Veritas InfoScale Operations Manager API
  slug: operations-manager-api
- description: 'API for managing VCS clusters, service groups, and resources within InfoScale. Provides operations for cluster node management, service group failover and failback, resource dependency configuration, '
  name: Veritas Cluster Server API
  slug: vcs-api
- description: API for storage volume management, including volume creation, resizing, mirroring, and snapshot operations. Manages disk groups, plexes, subdisks, and provides advanced storage features like thin prov
  name: Veritas Volume Manager API
  slug: vxvm-api
- description: Retrieve and manage cluster alerts
  name: Veritas InfoScale Alerts API
  slug: veritas-infoscale-alerts-api
- description: Cluster discovery and status operations
  name: Veritas InfoScale Clusters API
  slug: veritas-infoscale-clusters-api
- description: Manage Veritas Volume Manager disk groups
  name: Veritas InfoScale Disk Groups API
  slug: veritas-infoscale-disk-groups-api
- description: Manage physical disks and disk pools
  name: Veritas InfoScale Disks API
  slug: veritas-infoscale-disks-api
- description: Manage I/O fencing configuration
  name: Veritas InfoScale Fencing API
  slug: veritas-infoscale-fencing-api
- description: Monitor and manage asynchronous job operations
  name: Veritas InfoScale Jobs API
  slug: veritas-infoscale-jobs-api
- description: Manage cluster resources within service groups
  name: Veritas InfoScale Resources API
  slug: veritas-infoscale-resources-api
- description: Manage VCS service groups and their lifecycle
  name: Veritas InfoScale Service Groups API
  slug: veritas-infoscale-service-groups-api
- description: Manage cluster nodes and system status
  name: Veritas InfoScale Systems API
  slug: veritas-infoscale-systems-api
- description: Manage storage volumes
  name: Veritas InfoScale Volumes API
  slug: veritas-infoscale-volumes-api
artifact_total: 71
collections:
- collection_type: postman
  name: Veritas InfoScale REST Alerts API
  slug: postman-veritas-infoscale-alerts-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Clusters API
  slug: postman-veritas-infoscale-clusters-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Disk Groups API
  slug: postman-veritas-infoscale-disk-groups-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Disks API
  slug: postman-veritas-infoscale-disks-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Fencing API
  slug: postman-veritas-infoscale-fencing-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Jobs API
  slug: postman-veritas-infoscale-jobs-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Resources API
  slug: postman-veritas-infoscale-resources-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Service Groups API
  slug: postman-veritas-infoscale-service-groups-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Systems API
  slug: postman-veritas-infoscale-systems-api
- collection_type: postman
  name: Veritas InfoScale REST Alerts Volumes API
  slug: postman-veritas-infoscale-volumes-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/veritas-infoscale/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veritas-infoscale-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veritas-infoscale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veritas-infoscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veritas-infoscale-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://my.veritas.com
- group: operate
  title: ''
  type: Support
  url: https://www.veritas.com/support
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.veritas.com/support/en_US/dpp.InfoScaleStorageFoundation
- group: docs
  title: ''
  type: Documentation
  url: https://sort.veritas.com
- group: start
  title: ''
  type: GettingStarted
  url: https://sort.veritas.com/infoscale/intro
- group: learn
  title: ''
  type: Training
  url: https://www.veritas.com/support/training
- group: company
  title: ''
  type: Blog
  url: https://vox.veritas.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VeritasOS
- group: build
  title: InfoScale Ansible Playbooks
  type: GitHubRepository
  url: https://github.com/VeritasOS/infoscale_ansible
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veritas.com/company/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veritas.com/company/legal/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.veritas.com/form/requestacall
- group: commercial
  title: ''
  type: Pricing
  url: https://sort.veritas.com/license_calc
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.veritas.com/support/en_US/doc/infoscale
- group: design
  title: ''
  type: SpectralRules
  url: rules/veritas-infoscale-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/veritas-infoscale-vocabulary.yaml
created: '2025-03-14'
description: APIs for Veritas InfoScale, an enterprise storage and availability management solution that provides high availability, disaster recovery, and storage management capabilities across physical, virtual, and cloud environments.
examples:
- key_count: 7
  name: Rest Api Alert Example
  slug: rest-api-alert-example
- key_count: 8
  name: Rest Api Cluster Example
  slug: rest-api-cluster-example
- key_count: 8
  name: Rest Api Disk Group Example
  slug: rest-api-disk-group-example
- key_count: 9
  name: Rest Api Service Group Example
  slug: rest-api-service-group-example
- key_count: 8
  name: Rest Api System Example
  slug: rest-api-system-example
- key_count: 8
  name: Rest Api Volume Example
  slug: rest-api-volume-example
features:
- description: Provides application-aware clustering with automatic failover and failback to ensure continuous availability of mission-critical applications.
  name: High Availability Clustering
- description: Uses asynchronous event-based monitoring (IMF) to detect failures instantaneously, eliminating CPU overhead of legacy poll-based monitoring.
  name: Intelligent Monitoring Framework
- description: Software-defined storage services for volume management, thin provisioning, data migration, and multi-pathing across heterogeneous storage arrays.
  name: Storage Management
- description: Volume replication (VVR) and file replication (VFR) for real-time data replication across sites with automated disaster recovery orchestration.
  name: Disaster Recovery
- description: Space-optimized snapshots for backup, data analytics, forensic discovery, and point-in-time recovery without impacting production workloads.
  name: Snapshot Management
- description: Native CSI driver providing persistent storage on DAS and SAN with data integrity using I/O fencing for Kubernetes and OpenShift environments.
  name: Kubernetes Integration
- description: Deployment on AWS, Azure, Google Cloud, and Oracle Cloud with solution templates and marketplace offerings for elastic scaling.
  name: Cloud Deployment
- description: Full REST API support for control plane operations enabling automation and integration with DevOps pipelines and orchestration tools.
  name: REST API Management
finops:
- name: Veritas Infoscale Finops
  service_category: Storage / High Availability
  slug: veritas-infoscale-finops
image: /assets/icons/veritas-infoscale.png
integrations:
- description: Deep integration with Oracle RAC and single-instance databases for storage management, availability, and disaster recovery.
  name: Oracle Database
- description: Certified integration with SAP HANA and SAP applications for high availability and disaster recovery in enterprise environments.
  name: SAP Applications
- description: High availability and storage management for SQL Server Always On availability groups and failover cluster instances.
  name: Microsoft SQL Server
- description: Integration with VMware vSphere and vSAN for virtualized application availability and storage management.
  name: VMware vSphere
- description: CSI driver integration for persistent storage provisioning and management in container orchestration platforms.
  name: Kubernetes and OpenShift
- description: Ansible modules for automated deployment, configuration, and management of InfoScale environments in DevOps pipelines.
  name: Ansible Automation
- description: SRDF MetroCluster support with Dell EMC PowerMax and vMAX arrays for storage replication and disaster recovery.
  name: Dell EMC Storage
- description: Cloud marketplace offerings and solution templates for deployment on Amazon Web Services and Microsoft Azure platforms.
  name: AWS and Azure
json_schemas:
- name: Alert
  property_count: 7
  slug: rest-api-alert
- name: Cluster
  property_count: 8
  slug: rest-api-cluster
- name: DiskGroup
  property_count: 8
  slug: rest-api-disk-group
- name: ServiceGroup
  property_count: 9
  slug: rest-api-service-group
- name: System
  property_count: 8
  slug: rest-api-system
- name: Volume
  property_count: 8
  slug: rest-api-volume
json_structures:
- name: Rest Api Cluster Structure
  property_count: 8
  slug: rest-api-cluster-structure
- name: Rest Api Disk Group Structure
  property_count: 8
  slug: rest-api-disk-group-structure
- name: Rest Api Service Group Structure
  property_count: 9
  slug: rest-api-service-group-structure
- name: Rest Api Volume Structure
  property_count: 8
  slug: rest-api-volume-structure
jsonld:
- class_count: 10
  name: Veritas Infoscale Rest Api Context
  property_count: 38
  slug: veritas-infoscale-rest-api-context
layout: provider
modified: '2026-05-19'
name: Veritas InfoScale
nav: Providers
network: true
overview: 'Veritas InfoScale publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Clusters API, Disk Groups API, and 7 more. Tagged areas include Clustering, Data Management, Disaster Recovery, High Availability, and Storage Management.


  The Veritas InfoScale catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Veritas InfoScale''s developer surface includes authentication, developer portal, support, documentation, getting-started guide, training material, engineering blog, and 14 more developer resources.'
plans:
- name: Veritas Infoscale Plans Pricing
  plan_count: 1
  slug: veritas-infoscale-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 1
  name: Veritas Infoscale Rate Limits
  slug: veritas-infoscale-rate-limits
rules:
- name: Veritas InfoScale API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: veritas-infoscale-jsonschema-spectral-rules
- name: Veritas InfoScale API Rules
  rule_count: 41
  severity_counts:
    error: 23
    hint: 0
    info: 6
    warn: 12
  slug: veritas-infoscale-spectral-rules
score:
  band: strong
  composite: 58.1
  delta: -8.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.3
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 66.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/veritas-infoscale/refs/heads/main/screenshots/veritas-infoscale-2026-06-20T200933.png
security:
- kind: authentication
  name: Veritas Infoscale Authentication
  slug: veritas-infoscale-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Veritas Infoscale Domain Security
  slug: veritas-infoscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Veritas Infoscale Vulnerability Disclosure
  slug: veritas-infoscale-vulnerability-disclosure
  summary_line: disclosure policy published
slug: veritas-infoscale
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
use_cases:
- description: Ensure zero-downtime for mission-critical applications like Oracle, SAP, and SQL Server with automatic failover and health monitoring.
  name: Application High Availability
- description: Automate cross-site replication and recovery orchestration to meet RPO and RTO requirements for business continuity planning.
  name: Disaster Recovery Automation
- description: Consolidate heterogeneous storage arrays into a unified software-defined storage layer with volume management.
  name: Storage Consolidation
- description: Migrate on-premises applications to cloud environments with consistent storage and availability management across hybrid infrastructure.
  name: Cloud Migration
- description: Provide enterprise-grade persistent storage for containerized applications on Kubernetes and OpenShift with CSI driver integration.
  name: Container Storage
- description: Protect databases with application-consistent snapshots, online data migration, and real-time replication without application downtime.
  name: Database Protection
website: https://my.veritas.com
---
