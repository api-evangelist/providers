---
aid: veritas-infoscale
name: Veritas InfoScale
description: APIs for Veritas InfoScale, an enterprise storage and availability management solution that provides high availability, disaster recovery, and storage management capabilities across physical, virtual, and cloud environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/veritas-infoscale/refs/heads/main/apis.yml
created: '2025-03-14'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Clustering
  - Data Management
  - Disaster Recovery
  - High Availability
  - Storage Management
  - Virtualization
apis:
  - aid: veritas-infoscale:rest-api
    name: Veritas InfoScale REST API
    description: REST API for managing InfoScale clusters, storage resources, and high availability configurations. Supports storage configuration and management operations including disk groups, volumes, and file systems, as well as cluster configuration and management operations including service groups, resources, and heartbeats.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
    baseURL: https://{infoscale-server}:14149/api/v1
    tags:
      - Availability
      - Clustering
      - Storage
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
      - type: OpenAPI
        url: openapi/veritas-infoscale-rest-api.yaml
      - type: Authentication
        url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151837041-166315478
      - type: JSONSchema
        url: json-schema/rest-api-cluster-schema.json
        title: Cluster Schema
      - type: JSONSchema
        url: json-schema/rest-api-service-group-schema.json
        title: Service Group Schema
      - type: JSONSchema
        url: json-schema/rest-api-disk-group-schema.json
        title: Disk Group Schema
      - type: JSONSchema
        url: json-schema/rest-api-volume-schema.json
        title: Volume Schema
      - type: JSONSchema
        url: json-schema/rest-api-system-schema.json
        title: System Schema
      - type: JSONSchema
        url: json-schema/rest-api-alert-schema.json
        title: Alert Schema
      - type: JSONStructure
        url: json-structure/rest-api-cluster-structure.json
        title: Cluster Structure
      - type: JSONStructure
        url: json-structure/rest-api-service-group-structure.json
        title: Service Group Structure
      - type: JSONStructure
        url: json-structure/rest-api-disk-group-structure.json
        title: Disk Group Structure
      - type: JSONStructure
        url: json-structure/rest-api-volume-structure.json
        title: Volume Structure
      - type: JSONLD
        url: json-ld/veritas-infoscale-rest-api-context.jsonld
      - type: Example
        url: examples/rest-api-cluster-example.json
        title: Cluster Example
      - type: Example
        url: examples/rest-api-service-group-example.json
        title: Service Group Example
      - type: Example
        url: examples/rest-api-disk-group-example.json
        title: Disk Group Example
      - type: Example
        url: examples/rest-api-volume-example.json
        title: Volume Example
      - type: Example
        url: examples/rest-api-system-example.json
        title: System Example
      - type: Example
        url: examples/rest-api-alert-example.json
        title: Alert Example
    contact:
      - FN: Veritas Support
        email: support@veritas.com
        url: https://www.veritas.com/support
  - aid: veritas-infoscale:operations-manager-api
    name: Veritas InfoScale Operations Manager API
    description: REST API for centralized monitoring and management of InfoScale environments. Provides meta, query, update, and operational endpoints for managing clusters, service groups, hosts, storage, and extended attributes across the entire InfoScale infrastructure.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/viom_tot_v96894970-156079406
    baseURL: https://{isom-server}:14161/vom/api
    tags:
      - Management
      - Monitoring
      - Operations
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/viom_tot_v96894970-156079406
      - type: APIReference
        url: https://sort.veritas.com/public/documents/vom/7.3/windowsandunix/productguides/html/viom_user/ch38.htm
  - aid: veritas-infoscale:vcs-api
    name: Veritas Cluster Server API
    description: API for managing VCS clusters, service groups, and resources within InfoScale. Provides operations for cluster node management, service group failover and failback, resource dependency configuration, and heartbeat monitoring.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
    baseURL: https://{vcs-server}:14149/vcs/api
    tags:
      - Clustering
      - Failover
      - High Availability
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
      - type: CLI
        url: https://www.veritas.com/support/en_US/doc/cluster-server/cli-reference
  - aid: veritas-infoscale:vxvm-api
    name: Veritas Volume Manager API
    description: API for storage volume management, including volume creation, resizing, mirroring, and snapshot operations. Manages disk groups, plexes, subdisks, and provides advanced storage features like thin provisioning, data migration, and volume replication.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
    baseURL: https://{server}:14149/vxvm/api
    tags:
      - Snapshots
      - Storage
      - Volumes
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
      - type: GettingStarted
        url: https://www.veritas.com/support/en_US/doc/volume-manager/admin-guide
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://my.veritas.com
  - type: Support
    url: https://www.veritas.com/support
  - type: KnowledgeCenter
    url: https://www.veritas.com/support/en_US/dpp.InfoScaleStorageFoundation
  - type: Documentation
    url: https://sort.veritas.com
  - type: GettingStarted
    url: https://sort.veritas.com/infoscale/intro
  - type: Training
    url: https://www.veritas.com/support/training
  - type: Blog
    url: https://vox.veritas.com
  - type: GitHubOrganization
    url: https://github.com/VeritasOS
  - type: GitHubRepository
    url: https://github.com/VeritasOS/infoscale_ansible
    title: InfoScale Ansible Playbooks
  - type: TermsOfService
    url: https://www.veritas.com/company/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.veritas.com/company/legal/privacy
  - type: Contact
    url: https://www.veritas.com/form/requestacall
  - type: Pricing
    url: https://sort.veritas.com/license_calc
  - type: ReleaseNotes
    url: https://www.veritas.com/support/en_US/doc/infoscale
  - type: SpectralRules
    url: rules/veritas-infoscale-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/infrastructure-management.yaml
    title: Infrastructure Management
  - type: Vocabulary
    url: vocabulary/veritas-infoscale-vocabulary.yaml
  - type: Features
    data:
      - name: High Availability Clustering
        description: Provides application-aware clustering with automatic failover and failback to ensure continuous availability of mission-critical applications.
      - name: Intelligent Monitoring Framework
        description: Uses asynchronous event-based monitoring (IMF) to detect failures instantaneously, eliminating CPU overhead of legacy poll-based monitoring.
      - name: Storage Management
        description: Software-defined storage services for volume management, thin provisioning, data migration, and multi-pathing across heterogeneous storage arrays.
      - name: Disaster Recovery
        description: Volume replication (VVR) and file replication (VFR) for real-time data replication across sites with automated disaster recovery orchestration.
      - name: Snapshot Management
        description: Space-optimized snapshots for backup, data analytics, forensic discovery, and point-in-time recovery without impacting production workloads.
      - name: Kubernetes Integration
        description: Native CSI driver providing persistent storage on DAS and SAN with data integrity using I/O fencing for Kubernetes and OpenShift environments.
      - name: Cloud Deployment
        description: Deployment on AWS, Azure, Google Cloud, and Oracle Cloud with solution templates and marketplace offerings for elastic scaling.
      - name: REST API Management
        description: Full REST API support for control plane operations enabling automation and integration with DevOps pipelines and orchestration tools.
  - type: UseCases
    data:
      - name: Application High Availability
        description: Ensure zero-downtime for mission-critical applications like Oracle, SAP, and SQL Server with automatic failover and health monitoring.
      - name: Disaster Recovery Automation
        description: Automate cross-site replication and recovery orchestration to meet RPO and RTO requirements for business continuity planning.
      - name: Storage Consolidation
        description: Consolidate heterogeneous storage arrays into a unified software-defined storage layer with volume management.
      - name: Cloud Migration
        description: Migrate on-premises applications to cloud environments with consistent storage and availability management across hybrid infrastructure.
      - name: Container Storage
        description: Provide enterprise-grade persistent storage for containerized applications on Kubernetes and OpenShift with CSI driver integration.
      - name: Database Protection
        description: Protect databases with application-consistent snapshots, online data migration, and real-time replication without application downtime.
  - type: Integrations
    data:
      - name: Oracle Database
        description: Deep integration with Oracle RAC and single-instance databases for storage management, availability, and disaster recovery.
      - name: SAP Applications
        description: Certified integration with SAP HANA and SAP applications for high availability and disaster recovery in enterprise environments.
      - name: Microsoft SQL Server
        description: High availability and storage management for SQL Server Always On availability groups and failover cluster instances.
      - name: VMware vSphere
        description: Integration with VMware vSphere and vSAN for virtualized application availability and storage management.
      - name: Kubernetes and OpenShift
        description: CSI driver integration for persistent storage provisioning and management in container orchestration platforms.
      - name: Ansible Automation
        description: Ansible modules for automated deployment, configuration, and management of InfoScale environments in DevOps pipelines.
      - name: Dell EMC Storage
        description: SRDF MetroCluster support with Dell EMC PowerMax and vMAX arrays for storage replication and disaster recovery.
      - name: AWS and Azure
        description: Cloud marketplace offerings and solution templates for deployment on Amazon Web Services and Microsoft Azure platforms.
---
