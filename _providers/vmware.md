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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 22
  human_in_the_loop: 3
  name: Vmware Agentic Access
  operation_count: 49
  slug: vmware-agentic-access
  summary_line: 49 operations · 22 acting · 3 human-in-the-loop
api_count: 59
apis:
- description: Comprehensive SOAP-based API providing access to all vSphere management functionality including virtual machines, hosts, clusters, networking, and storage.
  name: vSphere Web Services API
  slug: vsphere-web-services-api
- description: HTTP and JSON based wire protocol as an alternative to SOAP and XML for vCenter Server 8.0 Update 1 and later, documented via OpenAPI 3.0 specification.
  name: Virtual Infrastructure JSON API
  slug: virtual-infrastructure-json-api
- description: API for managing NSX Federation with centralized configuration of multiple NSX deployments across sites.
  name: NSX-T Global Manager API
  slug: nsx-t-global-manager-api
- description: API for NSX Intelligence and Application Platform providing network traffic data collection, ingestion, and correlation capabilities.
  name: NSX Intelligence API
  slug: nsx-intelligence-api
- description: REST API for NSX Autonomous Edge providing network virtualization capabilities for edge deployments using a resource-oriented architecture with JSON encoding.
  name: NSX Autonomous Edge API
  slug: nsx-autonomous-edge-api
- description: API for managing enterprise-ready Kubernetes clusters.
  name: Tanzu Kubernetes Grid API
  slug: tanzu-kubernetes-grid-api
- description: API for unified endpoint management and digital workspace platform.
  name: Workspace ONE API
  slug: workspace-one-api
- description: API for managing the full VMware Cloud Foundation stack including SDDC Manager and Cloud Builder for automated lifecycle management of private cloud infrastructure.
  name: VMware Cloud Foundation API
  slug: vmware-cloud-foundation-api
- description: API for managing VMware Horizon virtual desktop and application delivery platform including pools, farms, desktops, and sessions.
  name: VMware Horizon Server API
  slug: vmware-horizon-server-api
- description: API for managing VMware vSAN software-defined storage including cluster configuration, disk management, health monitoring, and performance analytics.
  name: vSAN Management API
  slug: vsan-management-api
- description: REST API for VMware Aria Operations for Logs providing programmatic access to log data ingestion, querying, aggregation, and platform configuration.
  name: VMware Aria Operations for Logs API
  slug: vmware-aria-operations-for-logs-api
- description: API for network visibility, analytics, and troubleshooting providing access to application discovery, microsegmentation planning, and network flow analysis.
  name: VMware Aria Operations for Networks API
  slug: vmware-aria-operations-for-networks-api
- description: REST API for managing the lifecycle of VMware Aria suite products including deployment, upgrade, patching, and configuration management.
  name: VMware Aria Suite Lifecycle API
  slug: vmware-aria-suite-lifecycle-api
- description: REST API gateway for VMware Site Recovery Manager providing programmatic access to disaster recovery operations including protection groups, recovery plans, and replication management.
  name: VMware Site Recovery Manager API
  slug: vmware-site-recovery-manager-api
- description: REST API for VMware Live Cyber Recovery providing access to cloud file systems, protected sites, VMs, protection groups, and recovery plans for ransomware and disaster recovery.
  name: VMware Live Cyber Recovery API
  slug: vmware-live-cyber-recovery-api
- description: API for VMware Live Site Recovery providing disaster recovery as a service capabilities with automated recovery plan execution and testing.
  name: VMware Live Site Recovery API
  slug: vmware-live-site-recovery-api
- description: API for VMware vDefend lateral security platform providing network security segmentation, threat detection, network analysis, and malware prevention capabilities.
  name: VMware vDefend API
  slug: vmware-vdefend-api
- description: API for VMware Cloud Foundation operations management providing monitoring, analytics, and performance optimization for VCF deployments.
  name: VCF Operations API
  slug: vcf-operations-api
- description: API providing comprehensive access to VMware Horizon View data structures for managing virtual desktop infrastructure including desktop pools, sessions, and entitlements.
  name: VMware View API
  slug: vmware-view-api
- description: Comprehensive API reference for managing VMware Cloud on AWS infrastructure including SDDCs, organizations, subscriptions, and ESX host configurations.
  name: VMware Cloud on AWS API Reference
  slug: vmware-cloud-on-aws-api-reference
- description: API for managing logical networking in NSX for VMware Cloud on AWS customers including security policies, segments, and gateway configurations.
  name: NSX VMC Policy API
  slug: nsx-vmc-policy-api
- description: REST API for VMware Cloud Disaster Recovery providing access to cloud file systems, protected sites, protected VMs, protection groups, and Recovery SDDCs.
  name: VMware Cloud Disaster Recovery API
  slug: vmware-cloud-disaster-recovery-api
- description: 'REST API for VMware Aria Automation Orchestrator enabling programmatic access to run and schedule workflows, retrieve workflow details and logs, browse inventories and plug-ins, and import and export '
  name: VMware Aria Automation Orchestrator API
  slug: vmware-aria-automation-orchestrator-api
- description: SaaS version of the VMware Aria Operations for Networks API providing cloud-hosted network visibility, analytics, and microsegmentation planning capabilities with token-based authentication.
  name: VMware Aria Operations for Networks SaaS API
  slug: vmware-aria-operations-for-networks-saas-api
- description: API for VCF Operations for Networks providing network visibility, analytics, and troubleshooting for VMware Cloud Foundation deployments.
  name: VCF Operations for Networks API
  slug: vcf-operations-for-networks-api
- description: RESTful API for VMware Avi Load Balancer providing programmatic access to application delivery services including virtual services, pools, service engines, analytics, and health monitoring.
  name: VMware Avi Load Balancer API
  slug: vmware-avi-load-balancer-api
- description: API for VMware Data Services Manager providing on-demand provisioning and automated management of PostgreSQL, MySQL, and Microsoft SQL Server databases in vSphere environments.
  name: VMware Data Services Manager API
  slug: vmware-data-services-manager-api
- description: Kubernetes API for VMware Data Services Manager enabling self-service consumption of supported data services through Kubernetes custom resources.
  name: VMware Data Services Manager Kubernetes API
  slug: vmware-data-services-manager-kubernetes-api
- description: API for VMware App Volumes providing programmatic access to real-time application delivery and lifecycle management for virtual desktops and published applications.
  name: App Volumes API
  slug: app-volumes-api
- description: API for VMware vSphere Kubernetes Service enabling management of Tanzu Kubernetes clusters on vSphere including cluster lifecycle, node pools, and infrastructure configuration.
  name: VMware vSphere Kubernetes Service API
  slug: vmware-vsphere-kubernetes-service-api
- description: API for SDDC Manager providing programmatic access to VMware Cloud Foundation workload domain lifecycle management, host commissioning, and infrastructure configuration.
  name: SDDC Manager API
  slug: sddc-manager-api
- description: API for VMware Cloud Foundation Installer providing automated infrastructure bringup and initial deployment of VCF components.
  name: VCF Installer API
  slug: vcf-installer-api
- description: REST API for VMware Cloud Foundation Operations Orchestrator providing workflow automation and orchestration capabilities for VCF infrastructure management.
  name: VCF Operations Orchestrator API
  slug: vcf-operations-orchestrator-api
- description: Modern RESTful API for VMware Cloud Director defined using OpenAPI standards providing cloud service delivery and multi-tenancy management capabilities.
  name: VMware Cloud Director OpenAPI
  slug: vmware-cloud-director-openapi
- description: XML-based API for VMware Cloud Director providing comprehensive cloud service provider capabilities including organization, VDC, vApp, and catalog management.
  name: VMware Cloud Director API
  slug: vmware-cloud-director-api
- description: API for VMware Identity Manager providing identity and access management capabilities including authentication, authorization, directory integration, and single sign-on.
  name: VMware Identity Manager API
  slug: vmware-identity-manager-api
- description: REST API for Operations for Applications providing access to metrics, dashboards, alerts, events, and integrations for full-stack observability and monitoring.
  name: Operations for Applications REST API
  slug: operations-for-applications-rest-api
- description: REST API for Data Management for VMware Tanzu providing database-as-a-service capabilities for provisioning and managing data services on Kubernetes.
  name: Data Management for VMware Tanzu REST API
  slug: data-management-for-vmware-tanzu-rest-api
- description: API for managing VMware Cloud Foundation deployments on Dell VxRail hyperconverged infrastructure including cluster expansion, lifecycle management, and VxRail-specific operations.
  name: VMware Cloud Foundation for VxRail API
  slug: vmware-cloud-foundation-for-vxrail-api
- description: API for VMware Cloud Foundation Usage Meter providing metering and usage reporting capabilities for VMware product consumption tracking by service providers.
  name: VCF Usage Meter API
  slug: vcf-usage-meter-api
- description: API for managing the lifecycle of virtual storage including first-class disks, storage policies, and virtual disk operations in vSphere environments.
  name: Virtual Storage Lifecycle Management API
  slug: virtual-storage-lifecycle-management-api
- description: API for VMware Private AI providing on-premises AI and machine learning infrastructure services for deploying and managing AI workloads within VMware environments.
  name: VMware Private AI Service API
  slug: vmware-private-ai-service-api
- description: REST API for VMware HCX enabling workload mobility, network extension, and disaster recovery across data centers and clouds with support for migration automation and service mesh management.
  name: VMware HCX API
  slug: vmware-hcx-api
- description: API for managing the lifecycle of VMware cloud provider environments including deployment, upgrade, and configuration of VMware products for service providers.
  name: VMware Cloud Provider Lifecycle Manager API
  slug: vmware-cloud-provider-lifecycle-manager-api
- description: Cluster management for compute resource grouping, DRS, and HA configuration
  name: VMware Clusters API
  slug: vmware-clusters-api
- description: Content library management for templates, ISOs, and OVF packages shared across vCenter instances
  name: VMware Content Library API
  slug: vmware-content-library-api
- description: Datacenter management for organizing vSphere inventory
  name: VMware Datacenters API
  slug: vmware-datacenters-api
- description: Datastore management including browsing, capacity monitoring, and storage configuration
  name: VMware Datastores API
  slug: vmware-datastores-api
- description: Inventory folder management for organizing vSphere objects
  name: VMware Folders API
  slug: vmware-folders-api
- description: ESXi host management including connection state, maintenance mode, and host configuration
  name: VMware Hosts API
  slug: vmware-hosts-api
- description: Virtual network management including standard and distributed port groups and network connectivity
  name: VMware Networks API
  slug: vmware-networks-api
- description: Resource pool management for allocating compute resources
  name: VMware Resource Pools API
  slug: vmware-resource-pools-api
- description: Authentication session management for the vSphere REST API
  name: VMware Session API
  slug: vmware-session-api
- description: VM storage policy management for defining storage requirements and compliance
  name: VMware Storage Policies API
  slug: vmware-storage-policies-api
- description: Tag and category management for organizing and classifying vSphere inventory objects
  name: VMware Tagging API
  slug: vmware-tagging-api
- description: Guest operating system operations including identity, networking, local filesystem, and process management via VMware Tools
  name: VMware VM Guest API
  slug: vmware-vm-guest-api
- description: Virtual machine hardware configuration including CPU, memory, disks, network adapters, CD-ROMs, and other virtual devices
  name: VMware VM Hardware API
  slug: vmware-vm-hardware-api
- description: Virtual machine power state operations including power on, power off, suspend, reset, and guest shutdown
  name: VMware VM Power API
  slug: vmware-vm-power-api
- description: Virtual machine lifecycle management including creation, power operations, cloning, migration, and configuration
  name: VMware VMs API
  slug: vmware-vms-api
artifact_total: 280
collections:
- collection_type: open
  name: VMware vSphere Automation REST API
  slug: open-vmware-vsphere-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vmware-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vmware-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vmware-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vmware
- group: start
  title: ''
  type: Portal
  url: https://developer.broadcom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.broadcom.com/us/en/vmware-cis.html
- group: build
  title: ''
  type: SDKs
  url: https://developer.broadcom.com/vmware-sdk-api
- group: build
  title: ''
  type: CodeExamples
  url: https://developer.broadcom.com/codesample
- group: build
  title: ''
  type: CLI
  url: https://developer.broadcom.com/powercli/latest/
- group: company
  title: ''
  type: Blog
  url: https://blogs.vmware.com/code/
- group: operate
  title: ''
  type: Support
  url: https://www.broadcom.com/support/vmware-services
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vmware
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vmware-samples
- group: start
  title: ''
  type: Login
  url: https://developer.broadcom.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadcom.com/company/legal/privacy/policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadcom.com/company/legal/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vmware-services.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.broadcom.com/products/software/vmware
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vmware-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vmware-virtual-machine-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/vmware-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vmware-vocabulary.yaml
created: '2024-01-01'
description: Collection of VMware APIs for cloud infrastructure, virtualization, and management solutions including vSphere, NSX, vCloud Director, Tanzu, and Aria operations.
examples:
- key_count: 6
  name: Vmware Attachtag Example
  slug: vmware-attachtag-example
- key_count: 6
  name: Vmware Createcontentlibrary Example
  slug: vmware-createcontentlibrary-example
- key_count: 6
  name: Vmware Createdatacenter Example
  slug: vmware-createdatacenter-example
- key_count: 6
  name: Vmware Createsession Example
  slug: vmware-createsession-example
- key_count: 6
  name: Vmware Createtag Example
  slug: vmware-createtag-example
- key_count: 6
  name: Vmware Createtagcategory Example
  slug: vmware-createtagcategory-example
- key_count: 6
  name: Vmware Createvm Example
  slug: vmware-createvm-example
- key_count: 6
  name: Vmware Createvmdisk Example
  slug: vmware-createvmdisk-example
- key_count: 6
  name: Vmware Createvmethernet Example
  slug: vmware-createvmethernet-example
- key_count: 6
  name: Vmware Getcluster Example
  slug: vmware-getcluster-example
- key_count: 6
  name: Vmware Getcontentlibrary Example
  slug: vmware-getcontentlibrary-example
- key_count: 6
  name: Vmware Getdatacenter Example
  slug: vmware-getdatacenter-example
- key_count: 6
  name: Vmware Getdatastore Example
  slug: vmware-getdatastore-example
- key_count: 6
  name: Vmware Gethost Example
  slug: vmware-gethost-example
- key_count: 6
  name: Vmware Getsessioninfo Example
  slug: vmware-getsessioninfo-example
- key_count: 6
  name: Vmware Getvm Example
  slug: vmware-getvm-example
- key_count: 6
  name: Vmware Getvmcpu Example
  slug: vmware-getvmcpu-example
- key_count: 6
  name: Vmware Getvmguestidentity Example
  slug: vmware-getvmguestidentity-example
- key_count: 6
  name: Vmware Getvmguestnetworking Example
  slug: vmware-getvmguestnetworking-example
- key_count: 6
  name: Vmware Getvmhardware Example
  slug: vmware-getvmhardware-example
- key_count: 6
  name: Vmware Getvmmemory Example
  slug: vmware-getvmmemory-example
- key_count: 6
  name: Vmware Getvmpowerstate Example
  slug: vmware-getvmpowerstate-example
- key_count: 6
  name: Vmware Listclusters Example
  slug: vmware-listclusters-example
- key_count: 6
  name: Vmware Listcontentlibraries Example
  slug: vmware-listcontentlibraries-example
- key_count: 6
  name: Vmware Listdatacenters Example
  slug: vmware-listdatacenters-example
- key_count: 6
  name: Vmware Listdatastores Example
  slug: vmware-listdatastores-example
- key_count: 6
  name: Vmware Listfolders Example
  slug: vmware-listfolders-example
- key_count: 6
  name: Vmware Listhosts Example
  slug: vmware-listhosts-example
- key_count: 6
  name: Vmware Listnetworks Example
  slug: vmware-listnetworks-example
- key_count: 6
  name: Vmware Listresourcepools Example
  slug: vmware-listresourcepools-example
- key_count: 6
  name: Vmware Liststoragepolicies Example
  slug: vmware-liststoragepolicies-example
- key_count: 6
  name: Vmware Listtagcategories Example
  slug: vmware-listtagcategories-example
- key_count: 6
  name: Vmware Listtags Example
  slug: vmware-listtags-example
- key_count: 6
  name: Vmware Listvmdisks Example
  slug: vmware-listvmdisks-example
- key_count: 6
  name: Vmware Listvmethernet Example
  slug: vmware-listvmethernet-example
- key_count: 6
  name: Vmware Listvms Example
  slug: vmware-listvms-example
- key_count: 6
  name: Vmware Updatevmcpu Example
  slug: vmware-updatevmcpu-example
- key_count: 6
  name: Vmware Updatevmhardware Example
  slug: vmware-updatevmhardware-example
- key_count: 6
  name: Vmware Updatevmmemory Example
  slug: vmware-updatevmmemory-example
- key_count: 2
  name: Vmware Vsphere Cluster Info Example
  slug: vmware-vsphere-cluster-info-example
- key_count: 4
  name: Vmware Vsphere Cluster Summary Example
  slug: vmware-vsphere-cluster-summary-example
- key_count: 4
  name: Vmware Vsphere Cpu Info Example
  slug: vmware-vsphere-cpu-info-example
- key_count: 4
  name: Vmware Vsphere Cpu Update Spec Example
  slug: vmware-vsphere-cpu-update-spec-example
- key_count: 2
  name: Vmware Vsphere Datacenter Create Spec Example
  slug: vmware-vsphere-datacenter-create-spec-example
- key_count: 5
  name: Vmware Vsphere Datacenter Info Example
  slug: vmware-vsphere-datacenter-info-example
- key_count: 2
  name: Vmware Vsphere Datacenter Summary Example
  slug: vmware-vsphere-datacenter-summary-example
- key_count: 7
  name: Vmware Vsphere Datastore Info Example
  slug: vmware-vsphere-datastore-info-example
- key_count: 5
  name: Vmware Vsphere Datastore Summary Example
  slug: vmware-vsphere-datastore-summary-example
- key_count: 3
  name: Vmware Vsphere Disk Create Spec Example
  slug: vmware-vsphere-disk-create-spec-example
- key_count: 4
  name: Vmware Vsphere Disk Info Example
  slug: vmware-vsphere-disk-info-example
- key_count: 1
  name: Vmware Vsphere Disk Summary Example
  slug: vmware-vsphere-disk-summary-example
- key_count: 7
  name: Vmware Vsphere Ethernet Create Spec Example
  slug: vmware-vsphere-ethernet-create-spec-example
- key_count: 9
  name: Vmware Vsphere Ethernet Info Example
  slug: vmware-vsphere-ethernet-info-example
- key_count: 1
  name: Vmware Vsphere Ethernet Summary Example
  slug: vmware-vsphere-ethernet-summary-example
- key_count: 3
  name: Vmware Vsphere Folder Summary Example
  slug: vmware-vsphere-folder-summary-example
- key_count: 5
  name: Vmware Vsphere Guest Identity Info Example
  slug: vmware-vsphere-guest-identity-info-example
- key_count: 3
  name: Vmware Vsphere Guest Networking Info Example
  slug: vmware-vsphere-guest-networking-info-example
- key_count: 3
  name: Vmware Vsphere Hardware Info Example
  slug: vmware-vsphere-hardware-info-example
- key_count: 2
  name: Vmware Vsphere Hardware Update Spec Example
  slug: vmware-vsphere-hardware-update-spec-example
- key_count: 3
  name: Vmware Vsphere Host Info Example
  slug: vmware-vsphere-host-info-example
- key_count: 4
  name: Vmware Vsphere Host Summary Example
  slug: vmware-vsphere-host-summary-example
- key_count: 4
  name: Vmware Vsphere Library Create Spec Example
  slug: vmware-vsphere-library-create-spec-example
- key_count: 9
  name: Vmware Vsphere Library Info Example
  slug: vmware-vsphere-library-info-example
- key_count: 4
  name: Vmware Vsphere Memory Info Example
  slug: vmware-vsphere-memory-info-example
- key_count: 2
  name: Vmware Vsphere Memory Update Spec Example
  slug: vmware-vsphere-memory-update-spec-example
- key_count: 3
  name: Vmware Vsphere Network Summary Example
  slug: vmware-vsphere-network-summary-example
- key_count: 2
  name: Vmware Vsphere Power Info Example
  slug: vmware-vsphere-power-info-example
- key_count: 2
  name: Vmware Vsphere Resource Pool Summary Example
  slug: vmware-vsphere-resource-pool-summary-example
- key_count: 3
  name: Vmware Vsphere Session Info Example
  slug: vmware-vsphere-session-info-example
- key_count: 3
  name: Vmware Vsphere Storage Policy Summary Example
  slug: vmware-vsphere-storage-policy-summary-example
- key_count: 2
  name: Vmware Vsphere Tag Association Spec Example
  slug: vmware-vsphere-tag-association-spec-example
- key_count: 4
  name: Vmware Vsphere Tag Category Create Spec Example
  slug: vmware-vsphere-tag-category-create-spec-example
- key_count: 3
  name: Vmware Vsphere Tag Create Spec Example
  slug: vmware-vsphere-tag-create-spec-example
- key_count: 7
  name: Vmware Vsphere Vm Create Spec Example
  slug: vmware-vsphere-vm-create-spec-example
- key_count: 11
  name: Vmware Vsphere Vm Info Example
  slug: vmware-vsphere-vm-info-example
- key_count: 5
  name: Vmware Vsphere Vm Summary Example
  slug: vmware-vsphere-vm-summary-example
features:
- description: Industry-leading server virtualization platform for running and managing virtual machines across data center infrastructure.
  name: vSphere Virtualization
- description: Software-defined networking and security platform with micro-segmentation, load balancing, and distributed firewall.
  name: NSX Networking
- description: Hyper-converged software-defined storage integrated with vSphere for simplified storage management and high availability.
  name: vSAN Storage
- description: Enterprise Kubernetes management for building, running, and managing modern containerized applications at scale.
  name: Tanzu Kubernetes
- description: AI-powered operations management for proactive performance optimization, capacity planning, and intelligent remediation.
  name: Aria Operations
- description: Virtual desktop and application delivery platform for secure remote work with published desktops and applications.
  name: Horizon VDI
- description: Integrated software stack for private and hybrid cloud with automated lifecycle management and consistent operations.
  name: Cloud Foundation
- description: Automated disaster recovery and business continuity with recovery plan orchestration and non-disruptive testing.
  name: Site Recovery
- description: On-premises AI infrastructure services for deploying and managing AI workloads within VMware environments.
  name: Private AI
finops:
- name: Vmware Finops
  service_category: Cloud Infrastructure / Virtualization
  slug: vmware-finops
image: /assets/icons/vmware.png
integrations:
- description: VMware Cloud on AWS provides a jointly engineered hybrid cloud service running vSphere on AWS bare-metal infrastructure.
  name: AWS
- description: Azure VMware Solution runs VMware workloads natively on Azure with full vSphere, vSAN, and NSX integration.
  name: Microsoft Azure
- description: Google Cloud VMware Engine provides a fully managed VMware environment on Google Cloud infrastructure.
  name: Google Cloud
- description: Jointly engineered hyperconverged infrastructure combining VCF with Dell PowerEdge servers for turnkey private cloud.
  name: Dell VxRail
- description: Native Kubernetes integration through Tanzu and vSphere with Kubernetes for container orchestration at enterprise scale.
  name: Kubernetes
- description: Official VMware Terraform provider for infrastructure-as-code automation of vSphere, NSX, and VCF resources.
  name: Terraform
json_schemas:
- name: ClusterInfo
  property_count: 2
  slug: vmware-clusterinfo
- name: ClusterSummary
  property_count: 4
  slug: vmware-clustersummary
- name: CpuInfo
  property_count: 4
  slug: vmware-cpuinfo
- name: CpuUpdateSpec
  property_count: 4
  slug: vmware-cpuupdatespec
- name: DatacenterCreateSpec
  property_count: 2
  slug: vmware-datacentercreatespec
- name: DatacenterInfo
  property_count: 5
  slug: vmware-datacenterinfo
- name: DatacenterSummary
  property_count: 2
  slug: vmware-datacentersummary
- name: DatastoreInfo
  property_count: 7
  slug: vmware-datastoreinfo
- name: DatastoreSummary
  property_count: 5
  slug: vmware-datastoresummary
- name: DiskCreateSpec
  property_count: 3
  slug: vmware-diskcreatespec
- name: DiskInfo
  property_count: 4
  slug: vmware-diskinfo
- name: DiskSummary
  property_count: 1
  slug: vmware-disksummary
- name: EthernetCreateSpec
  property_count: 7
  slug: vmware-ethernetcreatespec
- name: EthernetInfo
  property_count: 9
  slug: vmware-ethernetinfo
- name: EthernetSummary
  property_count: 1
  slug: vmware-ethernetsummary
- name: FolderSummary
  property_count: 3
  slug: vmware-foldersummary
- name: GuestIdentityInfo
  property_count: 5
  slug: vmware-guestidentityinfo
- name: GuestNetworkingInfo
  property_count: 3
  slug: vmware-guestnetworkinginfo
- name: HardwareInfo
  property_count: 3
  slug: vmware-hardwareinfo
- name: HardwareUpdateSpec
  property_count: 2
  slug: vmware-hardwareupdatespec
- name: HostInfo
  property_count: 3
  slug: vmware-hostinfo
- name: HostSummary
  property_count: 4
  slug: vmware-hostsummary
- name: LibraryCreateSpec
  property_count: 4
  slug: vmware-librarycreatespec
- name: LibraryInfo
  property_count: 9
  slug: vmware-libraryinfo
- name: MemoryInfo
  property_count: 4
  slug: vmware-memoryinfo
- name: MemoryUpdateSpec
  property_count: 2
  slug: vmware-memoryupdatespec
- name: NetworkSummary
  property_count: 3
  slug: vmware-networksummary
- name: PowerInfo
  property_count: 2
  slug: vmware-powerinfo
- name: ResourcePoolSummary
  property_count: 2
  slug: vmware-resourcepoolsummary
- name: SessionInfo
  property_count: 3
  slug: vmware-sessioninfo
- name: StoragePolicySummary
  property_count: 3
  slug: vmware-storagepolicysummary
- name: TagAssociationSpec
  property_count: 2
  slug: vmware-tagassociationspec
- name: TagCategoryCreateSpec
  property_count: 4
  slug: vmware-tagcategorycreatespec
- name: TagCreateSpec
  property_count: 3
  slug: vmware-tagcreatespec
- name: VMware vSphere Virtual Machine
  property_count: 16
  slug: vmware-virtual-machine
- name: VMCreateSpec
  property_count: 9
  slug: vmware-vmcreatespec
- name: VMInfo
  property_count: 14
  slug: vmware-vminfo
- name: VMSummary
  property_count: 5
  slug: vmware-vmsummary
- name: ClusterInfo
  property_count: 2
  slug: vmware-vsphere-cluster-info
- name: ClusterSummary
  property_count: 4
  slug: vmware-vsphere-cluster-summary
- name: CpuInfo
  property_count: 4
  slug: vmware-vsphere-cpu-info
- name: CpuUpdateSpec
  property_count: 4
  slug: vmware-vsphere-cpu-update-spec
- name: DatacenterCreateSpec
  property_count: 2
  slug: vmware-vsphere-datacenter-create-spec
- name: DatacenterInfo
  property_count: 5
  slug: vmware-vsphere-datacenter-info
- name: DatacenterSummary
  property_count: 2
  slug: vmware-vsphere-datacenter-summary
- name: DatastoreInfo
  property_count: 7
  slug: vmware-vsphere-datastore-info
- name: DatastoreSummary
  property_count: 5
  slug: vmware-vsphere-datastore-summary
- name: DiskCreateSpec
  property_count: 3
  slug: vmware-vsphere-disk-create-spec
- name: DiskInfo
  property_count: 4
  slug: vmware-vsphere-disk-info
- name: DiskSummary
  property_count: 1
  slug: vmware-vsphere-disk-summary
- name: EthernetCreateSpec
  property_count: 7
  slug: vmware-vsphere-ethernet-create-spec
- name: EthernetInfo
  property_count: 9
  slug: vmware-vsphere-ethernet-info
- name: EthernetSummary
  property_count: 1
  slug: vmware-vsphere-ethernet-summary
- name: FolderSummary
  property_count: 3
  slug: vmware-vsphere-folder-summary
- name: GuestIdentityInfo
  property_count: 5
  slug: vmware-vsphere-guest-identity-info
- name: GuestNetworkingInfo
  property_count: 3
  slug: vmware-vsphere-guest-networking-info
- name: HardwareInfo
  property_count: 3
  slug: vmware-vsphere-hardware-info
- name: HardwareUpdateSpec
  property_count: 2
  slug: vmware-vsphere-hardware-update-spec
- name: HostInfo
  property_count: 3
  slug: vmware-vsphere-host-info
- name: HostSummary
  property_count: 4
  slug: vmware-vsphere-host-summary
- name: LibraryCreateSpec
  property_count: 4
  slug: vmware-vsphere-library-create-spec
- name: LibraryInfo
  property_count: 9
  slug: vmware-vsphere-library-info
- name: MemoryInfo
  property_count: 4
  slug: vmware-vsphere-memory-info
- name: MemoryUpdateSpec
  property_count: 2
  slug: vmware-vsphere-memory-update-spec
- name: NetworkSummary
  property_count: 3
  slug: vmware-vsphere-network-summary
- name: PowerInfo
  property_count: 2
  slug: vmware-vsphere-power-info
- name: ResourcePoolSummary
  property_count: 2
  slug: vmware-vsphere-resource-pool-summary
- name: SessionInfo
  property_count: 3
  slug: vmware-vsphere-session-info
- name: StoragePolicySummary
  property_count: 3
  slug: vmware-vsphere-storage-policy-summary
- name: TagAssociationSpec
  property_count: 2
  slug: vmware-vsphere-tag-association-spec
- name: TagCategoryCreateSpec
  property_count: 4
  slug: vmware-vsphere-tag-category-create-spec
- name: TagCreateSpec
  property_count: 3
  slug: vmware-vsphere-tag-create-spec
- name: VMCreateSpec
  property_count: 7
  slug: vmware-vsphere-vm-create-spec
- name: VMInfo
  property_count: 11
  slug: vmware-vsphere-vm-info
- name: VMSummary
  property_count: 5
  slug: vmware-vsphere-vm-summary
json_structures:
- name: Vmware Structure
  property_count: 0
  slug: vmware-structure
- name: Vmware Vsphere Cluster Info Structure
  property_count: 2
  slug: vmware-vsphere-cluster-info-structure
- name: Vmware Vsphere Cluster Summary Structure
  property_count: 4
  slug: vmware-vsphere-cluster-summary-structure
- name: Vmware Vsphere Cpu Info Structure
  property_count: 4
  slug: vmware-vsphere-cpu-info-structure
- name: Vmware Vsphere Cpu Update Spec Structure
  property_count: 4
  slug: vmware-vsphere-cpu-update-spec-structure
- name: Vmware Vsphere Datacenter Create Spec Structure
  property_count: 2
  slug: vmware-vsphere-datacenter-create-spec-structure
- name: Vmware Vsphere Datacenter Info Structure
  property_count: 5
  slug: vmware-vsphere-datacenter-info-structure
- name: Vmware Vsphere Datacenter Summary Structure
  property_count: 2
  slug: vmware-vsphere-datacenter-summary-structure
- name: Vmware Vsphere Datastore Info Structure
  property_count: 7
  slug: vmware-vsphere-datastore-info-structure
- name: Vmware Vsphere Datastore Summary Structure
  property_count: 5
  slug: vmware-vsphere-datastore-summary-structure
- name: Vmware Vsphere Disk Create Spec Structure
  property_count: 3
  slug: vmware-vsphere-disk-create-spec-structure
- name: Vmware Vsphere Disk Info Structure
  property_count: 4
  slug: vmware-vsphere-disk-info-structure
- name: Vmware Vsphere Disk Summary Structure
  property_count: 1
  slug: vmware-vsphere-disk-summary-structure
- name: Vmware Vsphere Ethernet Create Spec Structure
  property_count: 7
  slug: vmware-vsphere-ethernet-create-spec-structure
- name: Vmware Vsphere Ethernet Info Structure
  property_count: 9
  slug: vmware-vsphere-ethernet-info-structure
- name: Vmware Vsphere Ethernet Summary Structure
  property_count: 1
  slug: vmware-vsphere-ethernet-summary-structure
- name: Vmware Vsphere Folder Summary Structure
  property_count: 3
  slug: vmware-vsphere-folder-summary-structure
- name: Vmware Vsphere Guest Identity Info Structure
  property_count: 5
  slug: vmware-vsphere-guest-identity-info-structure
- name: Vmware Vsphere Guest Networking Info Structure
  property_count: 3
  slug: vmware-vsphere-guest-networking-info-structure
- name: Vmware Vsphere Hardware Info Structure
  property_count: 3
  slug: vmware-vsphere-hardware-info-structure
- name: Vmware Vsphere Hardware Update Spec Structure
  property_count: 2
  slug: vmware-vsphere-hardware-update-spec-structure
- name: Vmware Vsphere Host Info Structure
  property_count: 3
  slug: vmware-vsphere-host-info-structure
- name: Vmware Vsphere Host Summary Structure
  property_count: 4
  slug: vmware-vsphere-host-summary-structure
- name: Vmware Vsphere Library Create Spec Structure
  property_count: 4
  slug: vmware-vsphere-library-create-spec-structure
- name: Vmware Vsphere Library Info Structure
  property_count: 9
  slug: vmware-vsphere-library-info-structure
- name: Vmware Vsphere Memory Info Structure
  property_count: 4
  slug: vmware-vsphere-memory-info-structure
- name: Vmware Vsphere Memory Update Spec Structure
  property_count: 2
  slug: vmware-vsphere-memory-update-spec-structure
- name: Vmware Vsphere Network Summary Structure
  property_count: 3
  slug: vmware-vsphere-network-summary-structure
- name: Vmware Vsphere Power Info Structure
  property_count: 2
  slug: vmware-vsphere-power-info-structure
- name: Vmware Vsphere Resource Pool Summary Structure
  property_count: 2
  slug: vmware-vsphere-resource-pool-summary-structure
- name: Vmware Vsphere Session Info Structure
  property_count: 3
  slug: vmware-vsphere-session-info-structure
- name: Vmware Vsphere Storage Policy Summary Structure
  property_count: 3
  slug: vmware-vsphere-storage-policy-summary-structure
- name: Vmware Vsphere Tag Association Spec Structure
  property_count: 2
  slug: vmware-vsphere-tag-association-spec-structure
- name: Vmware Vsphere Tag Category Create Spec Structure
  property_count: 4
  slug: vmware-vsphere-tag-category-create-spec-structure
- name: Vmware Vsphere Tag Create Spec Structure
  property_count: 3
  slug: vmware-vsphere-tag-create-spec-structure
- name: Vmware Vsphere Vm Create Spec Structure
  property_count: 7
  slug: vmware-vsphere-vm-create-spec-structure
- name: Vmware Vsphere Vm Info Structure
  property_count: 11
  slug: vmware-vsphere-vm-info-structure
- name: Vmware Vsphere Vm Summary Structure
  property_count: 5
  slug: vmware-vsphere-vm-summary-structure
jsonld:
- class_count: 0
  name: Vmware Context
  property_count: 12
  slug: vmware-context
- class_count: 0
  name: Vmware Vsphere Context
  property_count: 0
  slug: vmware-vsphere-context
layout: provider
modified: '2026-05-19'
name: VMware
nav: Providers
network: true
overview: 'VMware publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Content Library API, Datacenters API, and 12 more. Tagged areas include Cloud Computing, Container Management, Hybrid Cloud, Infrastructure, and Virtualization.


  The VMware catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  VMware''s developer surface includes authentication, developer portal, documentation, code examples, CLI, engineering blog, support, and 15 more developer resources.'
plans:
- name: Vmware Plans Pricing
  plan_count: 1
  slug: vmware-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 1
  name: Vmware Rate Limits
  slug: vmware-rate-limits
rules:
- name: VMware API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vmware-jsonschema-spectral-rules
- name: VMware API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 6
  slug: vmware-spectral-rules
score:
  band: strong
  composite: 63.4
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 70.8
    developer_ergonomics: 47.8
    discoverability: 55.0
    governance: 86.8
    operational_transparency: 42.1
  previous_composite: 63.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vmware/refs/heads/main/screenshots/vmware-2026-06-20T201116.png
security:
- kind: authentication
  name: Vmware Authentication
  slug: vmware-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Vmware Domain Security
  slug: vmware-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: vmware
tags:
- Cloud Computing
- Container Management
- Hybrid Cloud
- Infrastructure
- Virtualization
use_cases:
- description: Transform traditional data centers with software-defined compute, storage, and networking for improved agility and efficiency.
  name: Data Center Modernization
- description: Extend on-premises infrastructure to public clouds with consistent management, security, and networking across environments.
  name: Hybrid Cloud Operations
- description: Containerize existing applications and deploy new cloud-native workloads on Kubernetes with enterprise-grade management.
  name: Application Modernization
- description: Protect business-critical workloads with automated failover, recovery plan testing, and ransomware protection.
  name: Disaster Recovery
- description: Deliver secure virtual desktops and applications to remote workers with centralized management and endpoint security.
  name: Virtual Desktop Infrastructure
- description: Implement zero-trust security with micro-segmentation, distributed firewall, and threat detection across the network.
  name: Network Security
website: https://developer.broadcom.com/
---
