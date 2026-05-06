---
aid: apache-cloudstack
name: Apache CloudStack
description: Apache CloudStack is an open-source cloud computing platform developed by the Apache Software Foundation for creating, managing, and deploying infrastructure cloud services. It provides a comprehensive IaaS platform supporting multiple hypervisors (KVM, VMware vSphere, XenServer) and a rich API for programmatic cloud resource management. CloudStack is used by service providers and enterprises to build public, private, and hybrid cloud environments with virtual machine management, networking, storage, and multi-tenancy features.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Cloud
  - IaaS
  - Infrastructure
  - Open Source
  - Virtualization
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-cloudstack/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-cloudstack:apache-cloudstack-api
    name: Apache CloudStack API
    description: The CloudStack API provides comprehensive REST endpoints for managing virtual machines, networks, storage volumes, accounts, domains, zones, and all cloud infrastructure resources using a query-parameter-based command dispatch pattern with HMAC-SHA1 authentication and asynchronous job support.
    humanURL: https://cloudstack.apache.org/api/
    baseURL: http://localhost:8080/client/api
    tags:
      - Cloud
      - IaaS
      - REST
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://cloudstack.apache.org/api/
      - type: OpenAPI
        url: openapi/apache-cloudstack-api-openapi.yaml
      - type: GettingStarted
        url: https://docs.cloudstack.apache.org/en/latest/installguide/
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/cloudstack
  - type: Documentation
    url: https://docs.cloudstack.apache.org/
  - type: GettingStarted
    url: https://docs.cloudstack.apache.org/en/latest/installguide/
  - type: Support
    url: https://cloudstack.apache.org/community/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: ChangeLog
    url: https://github.com/apache/cloudstack/releases
  - type: SpectralRules
    url: rules/apache-cloudstack-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-cloudstack-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/cloudstack-iaas-management.yaml
  - type: Features
    data:
      - name: Virtual Machine Management
        description: Full VM lifecycle management including deploy, start, stop, reboot, migrate, and destroy across multiple hypervisors.
      - name: Multi-Hypervisor Support
        description: Support for KVM, VMware vSphere, XenServer, and Hyper-V hypervisors within a single CloudStack deployment.
      - name: Network Management
        description: Advanced networking with isolated networks, shared networks, VLANs, VPNs, and software-defined networking.
      - name: Storage Management
        description: Primary and secondary storage management with volume snapshots, templates, and ISOs.
      - name: Multi-Tenancy
        description: Account and domain hierarchy for isolating resources between tenants, departments, and organizations.
      - name: Asynchronous API
        description: Long-running operations return async job IDs that can be polled for completion status.
      - name: Security Groups
        description: Stateful firewall rules for controlling inbound and outbound traffic to virtual machines.
      - name: Auto Scaling
        description: Automatic scaling of VM instances in response to load conditions using configurable policies.
      - name: REST API
        description: Comprehensive query-parameter-based REST API with HMAC-SHA1 authentication for programmatic cloud management.
      - name: CloudStack UI
        description: Web-based management console for administrators and users to manage cloud resources visually.
  - type: UseCases
    data:
      - name: Public Cloud Infrastructure
        description: Build and operate public IaaS clouds for service providers offering compute, storage, and networking.
      - name: Private Enterprise Cloud
        description: Deploy private clouds for enterprise organizations needing isolated, on-premises infrastructure.
      - name: Hybrid Cloud Orchestration
        description: Extend on-premises CloudStack clouds to public cloud providers for burst capacity and disaster recovery.
      - name: Managed Service Provider Hosting
        description: Host multi-tenant virtual server environments for managed service providers and resellers.
      - name: Development and Test Environments
        description: Provision self-service development and testing environments on demand for engineering teams.
  - type: Integrations
    data:
      - name: KVM
        description: KVM hypervisor support for Linux-based compute clusters in CloudStack zones.
      - name: VMware vSphere
        description: VMware vSphere integration for managing ESXi hosts and vCenter clusters via CloudStack.
      - name: Apache Cloudbridge
        description: Integration with Apache Cloudbridge for hybrid cloud connectivity between CloudStack and AWS.
      - name: Ceph
        description: Ceph distributed storage integration for primary storage in CloudStack deployments.
      - name: OpenDaylight
        description: OpenDaylight SDN controller integration for software-defined networking in CloudStack.
      - name: Terraform
        description: HashiCorp Terraform CloudStack provider for infrastructure-as-code provisioning.
      - name: Ansible
        description: Ansible CloudStack modules for automating VM provisioning and cloud management tasks.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
