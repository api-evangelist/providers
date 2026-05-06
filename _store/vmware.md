---
aid: vmware
name: VMware
description: Collection of VMware APIs for cloud infrastructure, virtualization, and management solutions including vSphere, NSX, vCloud Director, Tanzu, and Aria operations.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Computing
  - Container Management
  - Hybrid Cloud
  - Infrastructure
  - Virtualization
created: '2024-01-01'
modified: '2026-04-18'
url: https://raw.githubusercontent.com/api-evangelist/vmware/refs/heads/main/apis.yml
specificationVersion: '0.19'
type: Index
apis:
  - aid: vmware:vsphere-api
    name: vSphere API
    description: API for managing VMware vSphere virtualization platform, including VMs, hosts, and datastores.
    image: https://www.vmware.com/content/dam/digitalmarketing/vmware/en/images/products/vsphere-icon.svg
    humanURL: https://developer.vmware.com/apis/vsphere-automation/latest/
    baseURL: https://{{vcenter}}/api
    tags:
      - Data Center
      - Hypervisor
      - Virtualization
      - VM Management
    properties:
      - type: Documentation
        url: https://developer.vmware.com/docs/vsphere-automation/latest/
      - type: OpenAPI
        url: openapi/vmware-vsphere-api-openapi.yml
      - type: OpenAPI
        url: https://developer.vmware.com/apis/vsphere-automation/latest/openapi/
      - type: Authentication
        url: https://developer.vmware.com/docs/vsphere-automation/latest/authentication/
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vsphere-automation-api/latest/
      - type: JSONSchema
        url: json-schema/vmware-virtual-machine-schema.json
      - type: JSONLD
        url: json-ld/vmware-vsphere-context.jsonld
    contact:
      - FN: VMware Developer Support
        email: developer@vmware.com
        url: https://developer.vmware.com/support
  - aid: vmware:vsphere-web-services-api
    name: vSphere Web Services API
    description: Comprehensive SOAP-based API providing access to all vSphere management functionality including virtual machines, hosts, clusters, networking, and storage.
    humanURL: https://developer.broadcom.com/xapis/vsphere-web-services-api/latest/
    baseURL: https://{{vcenter}}/sdk
    tags:
      - Data Center
      - SOAP
      - Virtualization
      - VM Management
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vsphere-web-services-api/latest/
      - type: SDK
        url: https://github.com/vmware/vsphere-automation-sdk-java
  - aid: vmware:virtual-infrastructure-json-api
    name: Virtual Infrastructure JSON API
    description: HTTP and JSON based wire protocol as an alternative to SOAP and XML for vCenter Server 8.0 Update 1 and later, documented via OpenAPI 3.0 specification.
    humanURL: https://developer.broadcom.com/xapis/virtual-infrastructure-json-api/latest/
    baseURL: https://{{vcenter}}/sdk/vim25/8.0.1.0
    tags:
      - JSON
      - REST
      - vCenter
      - Virtualization
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/virtual-infrastructure-json-api/latest/
  - aid: vmware:vcloud-director-api
    name: vCloud Director API
    description: API for VMware vCloud Director cloud service delivery platform.
    humanURL: https://developer.vmware.com/apis/vmware-cloud-director/latest/
    baseURL: https://{{vcd-host}}/api
    tags:
      - Cloud Management
      - Multi-Tenancy
      - Service Provider
    properties:
      - type: Documentation
        url: https://developer.vmware.com/docs/vmware-cloud-director/latest/
      - type: OpenAPI
        url: https://developer.vmware.com/apis/vmware-cloud-director/latest/openapi/
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-director-openapi/latest/
  - aid: vmware:nsx-t-data-center-api
    name: NSX-T Data Center API
    description: API for NSX-T network virtualization and security platform.
    humanURL: https://developer.vmware.com/apis/nsx-t/latest/
    baseURL: https://{{nsx-manager}}/api/v1
    tags:
      - Load Balancing
      - Micro-Segmentation
      - Network Virtualization
      - Security
    properties:
      - type: Documentation
        url: https://developer.vmware.com/docs/nsx-t/latest/
      - type: OpenAPI
        url: https://developer.vmware.com/apis/nsx-t/latest/openapi/
      - type: APIReference
        url: https://developer.broadcom.com/xapis/nsx-t-data-center-rest-api/latest/
  - aid: vmware:nsx-t-global-manager-api
    name: NSX-T Global Manager API
    description: API for managing NSX Federation with centralized configuration of multiple NSX deployments across sites.
    humanURL: https://developer.broadcom.com/xapis/nsx-t-data-center-global-manager-rest-api/latest/
    baseURL: https://{{global-manager}}/global-manager/api/v1
    tags:
      - Federation
      - Multi-Site
      - Network Virtualization
      - Security
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/nsx-t-data-center-global-manager-rest-api/latest/
  - aid: vmware:nsx-intelligence-api
    name: NSX Intelligence API
    description: API for NSX Intelligence and Application Platform providing network traffic data collection, ingestion, and correlation capabilities.
    humanURL: https://developer.broadcom.com/xapis/nsx-intelligence-and-application-platform-apis/latest/
    baseURL: https://{{nsx-manager}}/napp/api/v1
    tags:
      - Network Intelligence
      - Security Analytics
      - Traffic Analysis
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/nsx-intelligence-and-application-platform-apis/latest/
  - aid: vmware:nsx-autonomous-edge-api
    name: NSX Autonomous Edge API
    description: REST API for NSX Autonomous Edge providing network virtualization capabilities for edge deployments using a resource-oriented architecture with JSON encoding.
    humanURL: https://developer.broadcom.com/xapis/nsx-autonomous-edge-rest-api/latest/
    baseURL: https://{{nsx-edge}}/api/v1
    tags:
      - Edge Computing
      - Network Virtualization
      - SD-WAN
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/nsx-autonomous-edge-rest-api/latest/
  - aid: vmware:vrealize-automation-api
    name: vRealize Automation API
    description: API for automating IT service delivery and cloud infrastructure management.
    humanURL: https://developer.vmware.com/apis/vrealize-automation/latest/
    baseURL: https://{{vra-host}}/automation-api
    tags:
      - Automation
      - Infrastructure as Code
      - Orchestration
      - Self-Service
    properties:
      - type: Documentation
        url: https://developer.vmware.com/docs/vrealize-automation/latest/
      - type: OpenAPI
        url: https://developer.vmware.com/apis/vrealize-automation/latest/openapi/
      - type: CodeExamples
        url: https://github.com/vmware/vrealize-automation-samples
  - aid: vmware:vmware-cloud-on-aws-api
    name: VMware Cloud on AWS API
    description: API for managing VMware Cloud on AWS infrastructure.
    humanURL: https://developer.vmware.com/apis/vmc/latest/
    baseURL: https://vmc.vmware.com/vmc/api
    tags:
      - AWS
      - Cloud Services
      - Hybrid Cloud
      - SDDC
    properties:
      - type: Documentation
        url: https://developer.vmware.com/docs/vmc/latest/
      - type: OpenAPI
        url: https://developer.vmware.com/apis/vmc/latest/openapi/
      - type: GettingStarted
        url: https://developer.vmware.com/docs/vmc/latest/getting-started/
      - type: APIReference
        url: https://developer.broadcom.com/xapis/nsx-vmc-policy/latest/
  - aid: vmware:tanzu-kubernetes-grid-api
    name: Tanzu Kubernetes Grid API
    description: API for managing enterprise-ready Kubernetes clusters.
    humanURL: https://developer.vmware.com/apis/tanzu/
    baseURL: https://{{tkg-endpoint}}/api
    tags:
      - Cloud Native
      - Containers
      - DevOps
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.vmware.com/en/VMware-Tanzu-Kubernetes-Grid/index.html
      - type: CLI
        url: https://docs.vmware.com/en/VMware-Tanzu-Kubernetes-Grid/latest/vmware-tanzu-kubernetes-grid/cli-reference.html
  - aid: vmware:vrealize-operations-api
    name: vRealize Operations API
    description: API for IT operations management and performance monitoring.
    humanURL: https://developer.vmware.com/apis/vrealize-operations/latest/
    baseURL: https://{{vrops-host}}/suite-api/api
    tags:
      - Analytics
      - Monitoring
      - Operations
      - Performance
    properties:
      - type: Documentation
        url: https://developer.vmware.com/docs/vrealize-operations/latest/
      - type: OpenAPI
        url: https://developer.vmware.com/apis/vrealize-operations/latest/openapi/
  - aid: vmware:workspace-one-api
    name: Workspace ONE API
    description: API for unified endpoint management and digital workspace platform.
    humanURL: https://developer.vmware.com/apis/workspace-one/
    baseURL: https://{{ws1-host}}/api
    tags:
      - Endpoint Management
      - Enterprise Mobility
      - Identity
      - Mobile Device Management
    properties:
      - type: Documentation
        url: https://developer.vmware.com/docs/workspace-one/
      - type: APIReference
        url: https://developer.vmware.com/apis/workspace-one/latest/reference/
  - aid: vmware:vmware-cloud-foundation-api
    name: VMware Cloud Foundation API
    description: API for managing the full VMware Cloud Foundation stack including SDDC Manager and Cloud Builder for automated lifecycle management of private cloud infrastructure.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-foundation-api/latest/
    baseURL: https://{{sddc-manager}}/v1
    tags:
      - Cloud Foundation
      - Hyperconverged Infrastructure
      - Lifecycle Management
      - SDDC
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-foundation-api/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/administration-sdks-cli-and-tools/about-vmware-cloud-foundation-development/vcf-apis-and-scripts.html
      - type: SDK
        url: https://github.com/vmware/vcf-sdk-java
  - aid: vmware:vmware-horizon-server-api
    name: VMware Horizon Server API
    description: API for managing VMware Horizon virtual desktop and application delivery platform including pools, farms, desktops, and sessions.
    humanURL: https://developer.broadcom.com/xapis/vmware-horizon-server-api/latest/
    baseURL: https://{{horizon-server}}/rest
    tags:
      - Desktop Virtualization
      - Remote Access
      - VDI
      - Virtual Desktop
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-horizon-server-api/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/horizon.html
  - aid: vmware:vsan-management-api
    name: vSAN Management API
    description: API for managing VMware vSAN software-defined storage including cluster configuration, disk management, health monitoring, and performance analytics.
    humanURL: https://developer.broadcom.com/xapis/vsan-management-api/latest/
    baseURL: https://{{vcenter}}/vsanHealth
    tags:
      - Data Management
      - Hyper-Converged
      - Storage
      - vSAN
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vsan-management-api/latest/
  - aid: vmware:vmware-aria-operations-for-logs-api
    name: VMware Aria Operations for Logs API
    description: REST API for VMware Aria Operations for Logs providing programmatic access to log data ingestion, querying, aggregation, and platform configuration.
    humanURL: https://developer.broadcom.com/xapis/vrealize-log-insight-api/latest/
    baseURL: https://{{log-insight-host}}:9543/api/v2
    tags:
      - Analytics
      - Log Management
      - Monitoring
      - Observability
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vrealize-log-insight-api/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-operations-for-logs/8-18/developer-resources-for-vmware-aria-operations-for-logs-8-18/the-vrealize-log-insight-rest-api.html
  - aid: vmware:vmware-aria-operations-for-networks-api
    name: VMware Aria Operations for Networks API
    description: API for network visibility, analytics, and troubleshooting providing access to application discovery, microsegmentation planning, and network flow analysis.
    humanURL: https://developer.broadcom.com/xapis/vmware-aria-operations-for-networks-api/latest/
    baseURL: https://{{vrni-host}}/api/ni
    tags:
      - Microsegmentation
      - Network Analytics
      - Network Monitoring
      - Troubleshooting
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-aria-operations-for-networks-api/latest/
  - aid: vmware:vmware-aria-suite-lifecycle-api
    name: VMware Aria Suite Lifecycle API
    description: REST API for managing the lifecycle of VMware Aria suite products including deployment, upgrade, patching, and configuration management.
    humanURL: https://developer.broadcom.com/xapis/vmware-aria-suite-lifecycle-rest-api/latest/
    baseURL: https://{{lcm-host}}/lcm/api
    tags:
      - Automation
      - Configuration Management
      - Deployment
      - Lifecycle Management
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-aria-suite-lifecycle-rest-api/latest/
  - aid: vmware:vmware-site-recovery-manager-api
    name: VMware Site Recovery Manager API
    description: REST API gateway for VMware Site Recovery Manager providing programmatic access to disaster recovery operations including protection groups, recovery plans, and replication management.
    humanURL: https://developer.broadcom.com/xapis/vmware-site-recovery-manager-rest-api-gateway/latest/
    baseURL: https://{{srm-host}}/api
    tags:
      - Business Continuity
      - Disaster Recovery
      - Replication
      - Site Recovery
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-site-recovery-manager-rest-api-gateway/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery/site-recovery-manager/8-8/site-recovery-manager-administration-8-8/using-the-site-recovery-manager-rest-api-gateway.html
      - type: SDK
        url: https://developer.broadcom.com/sdks/site-recovery-manager-srm/latest
  - aid: vmware:vmware-live-cyber-recovery-api
    name: VMware Live Cyber Recovery API
    description: REST API for VMware Live Cyber Recovery providing access to cloud file systems, protected sites, VMs, protection groups, and recovery plans for ransomware and disaster recovery.
    humanURL: https://developer.broadcom.com/xapis/vmware-live-cyber-recovery-api/latest/
    baseURL: https://{{vcdr-orchestrator}}/api
    tags:
      - Cloud Recovery
      - Cyber Recovery
      - Data Protection
      - Ransomware Protection
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-live-cyber-recovery-api/latest/
      - type: SDK
        url: https://developer.broadcom.com/sdks/vmware-live-cyber-recovery-sdk/latest
  - aid: vmware:vmware-live-site-recovery-api
    name: VMware Live Site Recovery API
    description: API for VMware Live Site Recovery providing disaster recovery as a service capabilities with automated recovery plan execution and testing.
    humanURL: https://developer.broadcom.com/xapis/vmware-live-site-recovery-v1-api/latest/
    baseURL: https://{{vcdr-host}}/api/vcdr/v1
    tags:
      - Business Continuity
      - Disaster Recovery
      - DRaaS
      - Site Recovery
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-live-site-recovery-v1-api/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/live-recovery/live-site-recovery/9-0/how-do-i-protect-my-environment/using-the-site-recovery-manager-rest-api-gateway.html
  - aid: vmware:vmware-vdefend-api
    name: VMware vDefend API
    description: API for VMware vDefend lateral security platform providing network security segmentation, threat detection, network analysis, and malware prevention capabilities.
    humanURL: https://developer.broadcom.com/xapis/vmware-vdefend/latest/
    baseURL: https://{{nsx-manager}}/api/v1
    tags:
      - Firewall
      - Micro-Segmentation
      - Network Security
      - Threat Detection
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-vdefend/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/vdefend.html
  - aid: vmware:vcf-operations-api
    name: VCF Operations API
    description: API for VMware Cloud Foundation operations management providing monitoring, analytics, and performance optimization for VCF deployments.
    humanURL: https://developer.broadcom.com/xapis/vcf-operations-api/latest/
    baseURL: https://{{vrops-host}}/suite-api/api
    tags:
      - Analytics
      - Cloud Foundation
      - Monitoring
      - Operations Management
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vcf-operations-api/latest/
  - aid: vmware:vmware-view-api
    name: VMware View API
    description: API providing comprehensive access to VMware Horizon View data structures for managing virtual desktop infrastructure including desktop pools, sessions, and entitlements.
    humanURL: https://developer.broadcom.com/xapis/view-api/latest/
    baseURL: https://{{horizon-server}}/view-vlsi/rest
    tags:
      - Desktop Management
      - Horizon View
      - VDI
      - Virtual Desktop
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/view-api/latest/
  - aid: vmware:vmware-cloud-on-aws-api-reference
    name: VMware Cloud on AWS API Reference
    description: Comprehensive API reference for managing VMware Cloud on AWS infrastructure including SDDCs, organizations, subscriptions, and ESX host configurations.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-on-aws-api-reference/latest/
    baseURL: https://vmc.vmware.com/vmc/api
    tags:
      - AWS
      - Cloud Infrastructure
      - Hybrid Cloud
      - SDDC
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-on-aws-api-reference/latest/
  - aid: vmware:nsx-vmc-policy-api
    name: NSX VMC Policy API
    description: API for managing logical networking in NSX for VMware Cloud on AWS customers including security policies, segments, and gateway configurations.
    humanURL: https://developer.broadcom.com/xapis/nsx-vmc-policy/latest/
    baseURL: https://{{nsx-manager}}/policy/api/v1
    tags:
      - AWS
      - Network Virtualization
      - Security Policy
      - VMware Cloud
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/nsx-vmc-policy/latest/
  - aid: vmware:vmware-cloud-disaster-recovery-api
    name: VMware Cloud Disaster Recovery API
    description: REST API for VMware Cloud Disaster Recovery providing access to cloud file systems, protected sites, protected VMs, protection groups, and Recovery SDDCs.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-disaster-recovery-api-reference/latest/
    baseURL: https://{{vcdr-host}}/api
    tags:
      - Business Continuity
      - Cloud Recovery
      - Data Protection
      - Disaster Recovery
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-disaster-recovery-api-reference/latest/
  - aid: vmware:vmware-aria-automation-orchestrator-api
    name: VMware Aria Automation Orchestrator API
    description: REST API for VMware Aria Automation Orchestrator enabling programmatic access to run and schedule workflows, retrieve workflow details and logs, browse inventories and plug-ins, and import and export packages.
    humanURL: https://developer.broadcom.com/xapis/vrealize-orchestrator-api/latest/
    baseURL: https://{{vro-host}}/vco/api
    tags:
      - IT Automation
      - Orchestration
      - Plug-Ins
      - Workflow Automation
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vrealize-orchestrator-api/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-automation/all/developing-web-services-client-for-vco-all/using-the-orchestrator-rest-api.html
      - type: SDK
        url: https://techdocs.broadcom.com/us/en/vmware-cis/aria/aria-automation/all/vro-plug-in-development-all.html
  - aid: vmware:vmware-aria-operations-for-networks-saas-api
    name: VMware Aria Operations for Networks SaaS API
    description: SaaS version of the VMware Aria Operations for Networks API providing cloud-hosted network visibility, analytics, and microsegmentation planning capabilities with token-based authentication.
    humanURL: https://developer.broadcom.com/xapis/vmware-aria-operations-for-networks-saas-api/latest/
    baseURL: https://{{vrni-saas-host}}/api/ni
    tags:
      - Microsegmentation
      - Network Analytics
      - Network Monitoring
      - SaaS
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-aria-operations-for-networks-saas-api/latest/
  - aid: vmware:vcf-operations-for-networks-api
    name: VCF Operations for Networks API
    description: API for VCF Operations for Networks providing network visibility, analytics, and troubleshooting for VMware Cloud Foundation deployments.
    humanURL: https://developer.broadcom.com/xapis/vcf-operations-for-networks-api/latest/
    baseURL: https://{{vrni-host}}/api/ni
    tags:
      - Cloud Foundation
      - Network Analytics
      - Network Monitoring
      - Troubleshooting
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vcf-operations-for-networks-api/latest/
  - aid: vmware:vmware-avi-load-balancer-api
    name: VMware Avi Load Balancer API
    description: RESTful API for VMware Avi Load Balancer providing programmatic access to application delivery services including virtual services, pools, service engines, analytics, and health monitoring.
    humanURL: https://developer.broadcom.com/xapis/vmware-avi-load-balancer/latest/
    baseURL: https://{{avi-controller}}/api
    tags:
      - Analytics
      - Application Delivery
      - Load Balancing
      - Traffic Management
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-avi-load-balancer/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-security-load-balancing/avi-load-balancer.html
  - aid: vmware:vmware-data-services-manager-api
    name: VMware Data Services Manager API
    description: API for VMware Data Services Manager providing on-demand provisioning and automated management of PostgreSQL, MySQL, and Microsoft SQL Server databases in vSphere environments.
    humanURL: https://developer.broadcom.com/xapis/vmware-data-services-manager/latest/
    baseURL: https://{{dsm-host}}/api
    tags:
      - Data Services
      - Database Management
      - MySQL
      - PostgreSQL
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-data-services-manager/latest/
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/dsm/data-services-manager/2-1/access-the-vmware-data-services-manager-api.html
  - aid: vmware:vmware-data-services-manager-kubernetes-api
    name: VMware Data Services Manager Kubernetes API
    description: Kubernetes API for VMware Data Services Manager enabling self-service consumption of supported data services through Kubernetes custom resources.
    humanURL: https://developer.broadcom.com/xapis/vmware-data-services-manager-kubernetes-api/latest/all-api-ref.html
    baseURL: https://{{k8s-api}}/apis
    tags:
      - Data Services
      - Database Management
      - Kubernetes
      - Self-Service
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-data-services-manager-kubernetes-api/latest/all-api-ref.html
  - aid: vmware:app-volumes-api
    name: App Volumes API
    description: API for VMware App Volumes providing programmatic access to real-time application delivery and lifecycle management for virtual desktops and published applications.
    humanURL: https://developer.broadcom.com/xapis/app-volumes-api/latest/
    baseURL: https://{{app-volumes-manager}}/api
    tags:
      - Application Delivery
      - Application Management
      - Desktop Virtualization
      - VDI
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/app-volumes-api/latest/
  - aid: vmware:vmware-vsphere-kubernetes-service-api
    name: VMware vSphere Kubernetes Service API
    description: API for VMware vSphere Kubernetes Service enabling management of Tanzu Kubernetes clusters on vSphere including cluster lifecycle, node pools, and infrastructure configuration.
    humanURL: https://developer.broadcom.com/xapis/vmware-vsphere-kubernetes-service/latest/api-docs.html
    baseURL: https://{{vcenter}}/api
    tags:
      - Container Management
      - Kubernetes
      - Tanzu
      - vSphere
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-vsphere-kubernetes-service/latest/api-docs.html
  - aid: vmware:sddc-manager-api
    name: SDDC Manager API
    description: API for SDDC Manager providing programmatic access to VMware Cloud Foundation workload domain lifecycle management, host commissioning, and infrastructure configuration.
    humanURL: https://developer.broadcom.com/xapis/sddc-manager-api/latest/
    baseURL: https://{{sddc-manager}}/v1
    tags:
      - Cloud Foundation
      - Infrastructure
      - Lifecycle Management
      - SDDC
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/sddc-manager-api/latest/
  - aid: vmware:vcf-installer-api
    name: VCF Installer API
    description: API for VMware Cloud Foundation Installer providing automated infrastructure bringup and initial deployment of VCF components.
    humanURL: https://developer.broadcom.com/xapis/vcf-installer-api/latest/
    baseURL: https://{{cloud-builder}}/v1
    tags:
      - Automation
      - Cloud Foundation
      - Deployment
      - Installation
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vcf-installer-api/latest/
  - aid: vmware:vcf-operations-orchestrator-api
    name: VCF Operations Orchestrator API
    description: REST API for VMware Cloud Foundation Operations Orchestrator providing workflow automation and orchestration capabilities for VCF infrastructure management.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-foundation-operations-orchestrator-api/latest/
    baseURL: https://{{vro-host}}/vco/api
    tags:
      - Cloud Foundation
      - Operations
      - Orchestration
      - Workflow Automation
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-foundation-operations-orchestrator-api/latest/
  - aid: vmware:vmware-cloud-director-openapi
    name: VMware Cloud Director OpenAPI
    description: Modern RESTful API for VMware Cloud Director defined using OpenAPI standards providing cloud service delivery and multi-tenancy management capabilities.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-director-openapi/latest/
    baseURL: https://{{vcd-host}}/cloudapi
    tags:
      - Cloud Management
      - Multi-Tenancy
      - OpenAPI
      - Service Provider
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-director-openapi/latest/
      - type: GettingStarted
        url: https://techdocs.broadcom.com/us/en/vmware-cis/cloud-director/vmware-cloud-director/10-6/getting-started-with-vcloud-openapis-10-6.html
  - aid: vmware:vmware-cloud-director-api
    name: VMware Cloud Director API
    description: XML-based API for VMware Cloud Director providing comprehensive cloud service provider capabilities including organization, VDC, vApp, and catalog management.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-director-api/latest/
    baseURL: https://{{vcd-host}}/api
    tags:
      - Cloud Management
      - Multi-Tenancy
      - Service Provider
      - XML
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-director-api/latest/
  - aid: vmware:vmware-identity-manager-api
    name: VMware Identity Manager API
    description: API for VMware Identity Manager providing identity and access management capabilities including authentication, authorization, directory integration, and single sign-on.
    humanURL: https://developer.broadcom.com/xapis/vmware-identity-manager-api/latest/
    baseURL: https://{{idm-host}}/SAAS/jersey/manager/api
    tags:
      - Access Management
      - Authentication
      - Identity Management
      - Single Sign-On
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-identity-manager-api/latest/
  - aid: vmware:operations-for-applications-rest-api
    name: Operations for Applications REST API
    description: REST API for Operations for Applications providing access to metrics, dashboards, alerts, events, and integrations for full-stack observability and monitoring.
    humanURL: https://developer.broadcom.com/xapis/operations-for-applications-rest-api/latest/
    baseURL: https://{{wavefront-host}}/api/v2
    tags:
      - Dashboards
      - Metrics
      - Monitoring
      - Observability
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/operations-for-applications-rest-api/latest/
  - aid: vmware:data-management-for-vmware-tanzu-rest-api
    name: Data Management for VMware Tanzu REST API
    description: REST API for Data Management for VMware Tanzu providing database-as-a-service capabilities for provisioning and managing data services on Kubernetes.
    humanURL: https://developer.broadcom.com/xapis/data-management-for-vmware-tanzu-rest-api/latest/
    baseURL: https://{{tanzu-data-host}}/api
    tags:
      - Data Management
      - Database
      - Kubernetes
      - Tanzu
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/data-management-for-vmware-tanzu-rest-api/latest/
  - aid: vmware:vmware-cloud-foundation-for-vxrail-api
    name: VMware Cloud Foundation for VxRail API
    description: API for managing VMware Cloud Foundation deployments on Dell VxRail hyperconverged infrastructure including cluster expansion, lifecycle management, and VxRail-specific operations.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-foundation-for-vxrail-api/latest/
    baseURL: https://{{sddc-manager}}/v1
    tags:
      - Cloud Foundation
      - Dell
      - Hyperconverged Infrastructure
      - VxRail
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-foundation-for-vxrail-api/latest/
  - aid: vmware:vcf-usage-meter-api
    name: VCF Usage Meter API
    description: API for VMware Cloud Foundation Usage Meter providing metering and usage reporting capabilities for VMware product consumption tracking by service providers.
    humanURL: https://developer.broadcom.com/xapis/vcf-usage-meter-apis/latest/
    baseURL: https://{{usage-meter}}/api
    tags:
      - Billing
      - Reporting
      - Service Provider
      - Usage Metering
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vcf-usage-meter-apis/latest/
  - aid: vmware:virtual-storage-lifecycle-management-api
    name: Virtual Storage Lifecycle Management API
    description: API for managing the lifecycle of virtual storage including first-class disks, storage policies, and virtual disk operations in vSphere environments.
    humanURL: https://developer.broadcom.com/xapis/virtual-storage-lifecycle-management-api/latest/
    baseURL: https://{{vcenter}}/api
    tags:
      - Lifecycle Management
      - Storage
      - Storage Policy
      - Virtual Disk
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/virtual-storage-lifecycle-management-api/latest/
  - aid: vmware:vmware-private-ai-service-api
    name: VMware Private AI Service API
    description: API for VMware Private AI providing on-premises AI and machine learning infrastructure services for deploying and managing AI workloads within VMware environments.
    humanURL: https://developer.broadcom.com/xapis/vmware-private-ai-service-api/latest/
    baseURL: https://{{pai-host}}/api
    tags:
      - Artificial Intelligence
      - Infrastructure
      - Machine Learning
      - Private AI
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-private-ai-service-api/latest/
  - aid: vmware:vmware-hcx-api
    name: VMware HCX API
    description: REST API for VMware HCX enabling workload mobility, network extension, and disaster recovery across data centers and clouds with support for migration automation and service mesh management.
    humanURL: https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10.html
    baseURL: https://{{hcx-manager}}/hybridity/api
    tags:
      - Disaster Recovery
      - Hybrid Cloud
      - Network Extension
      - Workload Migration
    properties:
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10.html
  - aid: vmware:vmware-cloud-provider-lifecycle-manager-api
    name: VMware Cloud Provider Lifecycle Manager API
    description: API for managing the lifecycle of VMware cloud provider environments including deployment, upgrade, and configuration of VMware products for service providers.
    humanURL: https://developer.broadcom.com/xapis/vmware-cloud-provider-lifecycle-manager-api/latest/
    baseURL: https://{{vclm-host}}/api
    tags:
      - Cloud Provider
      - Deployment
      - Lifecycle Management
      - Service Provider
    properties:
      - type: APIReference
        url: https://developer.broadcom.com/xapis/vmware-cloud-provider-lifecycle-manager-api/latest/
common:
  - type: Portal
    url: https://developer.broadcom.com/
  - type: Documentation
    url: https://techdocs.broadcom.com/us/en/vmware-cis.html
  - type: SDK
    url: https://developer.broadcom.com/vmware-sdk-api
  - type: CodeExamples
    url: https://developer.broadcom.com/codesample
  - type: CLI
    url: https://developer.broadcom.com/powercli/latest/
  - type: Blog
    url: https://blogs.vmware.com/code/
  - type: Support
    url: https://www.broadcom.com/support/vmware-services
  - type: GitHubOrganization
    url: https://github.com/vmware
  - type: GitHubRepository
    url: https://github.com/vmware-samples
  - type: Login
    url: https://developer.broadcom.com/
  - type: PrivacyPolicy
    url: https://www.broadcom.com/company/legal/privacy/policy
  - type: TermsOfService
    url: https://www.broadcom.com/company/legal/terms-of-use
  - type: StatusPage
    url: https://status.vmware-services.io/
  - type: Pricing
    url: https://www.broadcom.com/products/software/vmware
  - type: JSONLD
    url: json-ld/vmware-context.jsonld
  - type: JSONSchema
    url: json-schema/vmware-virtual-machine-schema.json
  - type: SpectralRules
    url: rules/vmware-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/vmware-vocabulary.yaml
  - type: Features
    url: https://www.vmware.com/products.html
    data:
      - name: vSphere Virtualization
        description: Industry-leading server virtualization platform for running and managing virtual machines across data center infrastructure.
      - name: NSX Networking
        description: Software-defined networking and security platform with micro-segmentation, load balancing, and distributed firewall.
      - name: vSAN Storage
        description: Hyper-converged software-defined storage integrated with vSphere for simplified storage management and high availability.
      - name: Tanzu Kubernetes
        description: Enterprise Kubernetes management for building, running, and managing modern containerized applications at scale.
      - name: Aria Operations
        description: AI-powered operations management for proactive performance optimization, capacity planning, and intelligent remediation.
      - name: Horizon VDI
        description: Virtual desktop and application delivery platform for secure remote work with published desktops and applications.
      - name: Cloud Foundation
        description: Integrated software stack for private and hybrid cloud with automated lifecycle management and consistent operations.
      - name: Site Recovery
        description: Automated disaster recovery and business continuity with recovery plan orchestration and non-disruptive testing.
      - name: Private AI
        description: On-premises AI infrastructure services for deploying and managing AI workloads within VMware environments.
  - type: UseCases
    url: https://www.vmware.com/solutions.html
    data:
      - name: Data Center Modernization
        description: Transform traditional data centers with software-defined compute, storage, and networking for improved agility and efficiency.
      - name: Hybrid Cloud Operations
        description: Extend on-premises infrastructure to public clouds with consistent management, security, and networking across environments.
      - name: Application Modernization
        description: Containerize existing applications and deploy new cloud-native workloads on Kubernetes with enterprise-grade management.
      - name: Disaster Recovery
        description: Protect business-critical workloads with automated failover, recovery plan testing, and ransomware protection.
      - name: Virtual Desktop Infrastructure
        description: Deliver secure virtual desktops and applications to remote workers with centralized management and endpoint security.
      - name: Network Security
        description: Implement zero-trust security with micro-segmentation, distributed firewall, and threat detection across the network.
  - type: Integrations
    url: https://www.vmware.com/partners.html
    data:
      - name: AWS
        description: VMware Cloud on AWS provides a jointly engineered hybrid cloud service running vSphere on AWS bare-metal infrastructure.
      - name: Microsoft Azure
        description: Azure VMware Solution runs VMware workloads natively on Azure with full vSphere, vSAN, and NSX integration.
      - name: Google Cloud
        description: Google Cloud VMware Engine provides a fully managed VMware environment on Google Cloud infrastructure.
      - name: Dell VxRail
        description: Jointly engineered hyperconverged infrastructure combining VCF with Dell PowerEdge servers for turnkey private cloud.
      - name: Kubernetes
        description: Native Kubernetes integration through Tanzu and vSphere with Kubernetes for container orchestration at enterprise scale.
      - name: Terraform
        description: Official VMware Terraform provider for infrastructure-as-code automation of vSphere, NSX, and VCF resources.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
