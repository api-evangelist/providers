---
name: Solaris Zones
description: API for managing Solaris Zones (containers) and virtualization on Oracle Solaris systems.
image: https://www.oracle.com/a/ocom/img/cb71-solaris.jpg
created: '2024'
modified: '2026-04-18'
url: https://docs.oracle.com/en/operating-systems/solaris.html
specificationVersion: '0.18'
apis:
  - name: Solaris Zones Management API
    description: Core API for creating, managing, and monitoring Solaris Zones.
    image: https://www.oracle.com/a/ocom/img/cb71-solaris.jpg
    humanURL: https://docs.oracle.com/cd/E88353_01/html/E37839/zones.html
    baseURL: https://solaris-host.example.com/api/v1
    tags:
      - Containers
      - Oracle
      - Solaris
      - Virtualization
      - Zones
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E88353_01/html/E37839/zones.html
      - type: OpenAPI
        url: openapi/solaris-zones-management-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: Zone Configuration API
    description: API endpoints for zone configuration and resource management.
    humanURL: https://docs.oracle.com/cd/E88353_01/html/E37839/zonecfg-1m.html
    baseURL: https://solaris-host.example.com/api/v1/zones
    tags:
      - Configuration
      - Networking
      - Resources
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E88353_01/html/E37839/zonecfg-1m.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E61040/
      - type: OpenAPI
        url: openapi/solaris-zone-configuration-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: Zone Administration API
    description: API for zone lifecycle management including install, boot, halt, and delete operations.
    humanURL: https://docs.oracle.com/cd/E88353_01/html/E37839/zoneadm-1m.html
    baseURL: https://solaris-host.example.com/api/v1/zones/admin
    tags:
      - Administration
      - Lifecycle
      - Management
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E88353_01/html/E37839/zoneadm-1m.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E61038/gqhar.html
      - type: OpenAPI
        url: openapi/solaris-zone-administration-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: Zone Monitoring API
    description: API for monitoring zone status, resource usage, and performance metrics.
    humanURL: https://docs.oracle.com/cd/E88353_01/html/E37839/zonestat-1.html
    baseURL: https://solaris-host.example.com/api/v1/zones/monitoring
    tags:
      - Metrics
      - Monitoring
      - Performance
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E88353_01/html/E37839/zonestat-1.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E61043/gklfb.html
      - type: OpenAPI
        url: openapi/solaris-zone-monitoring-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: RAD Zone Management REST API
    description: Remote Administration Daemon REST API for programmatic zone management via the com.oracle.solaris.rad.zonemgr module, supporting zone creation, configuration, migration, and lifecycle operations over HTTP/JSON.
    humanURL: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/rad-client/rest-api-reference.html
    baseURL: https://solaris-host.example.com/api/com.oracle.solaris.rad.zonemgr
    tags:
      - Management
      - RAD
      - Remote Administration
      - REST API
      - Zones
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/rad-client/rest-api-reference.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E68270/gpzpd.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E68270/gpzpv.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E88353_01/html/E76189/zonemgr-1-3rad.html
      - type: OpenAPI
        url: openapi/solaris-rad-zonemgr-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: Zones Monitoring Statistics API (libzonestat)
    description: The libzonestat.so.1 C library API used to retrieve and compute zone-related resource utilization information including physical memory, virtual memory, and CPU resources with sorting and filtering options.
    humanURL: https://docs.oracle.com/cd/E37838_01/html/E61043/
    baseURL: https://solaris-host.example.com/api/v1/zones/stats
    tags:
      - CPU
      - Libzonestat
      - Memory
      - Monitoring
      - Resource Utilization
      - Statistics
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E61043/
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E61043/gklfn.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E23824_01/html/821-1499/gloag.html
      - type: OpenAPI
        url: openapi/solaris-zone-stats-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: Oracle Solaris Kernel Zones API
    description: API for creating and managing Oracle Solaris Kernel Zones, which are non-global zones with their own kernel providing greater independence and enhanced security isolation.
    humanURL: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/kernel-zones/oracle-solaris-kernel-zones.html
    baseURL: https://solaris-host.example.com/api/v1/zones/kernel
    tags:
      - Isolation
      - Kernel Zones
      - Security
      - Virtualization
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/kernel-zones/oracle-solaris-kernel-zones.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E61041/gnzfn.html
      - type: OpenAPI
        url: openapi/solaris-kernel-zones-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: Oracle Solaris StatsStore and Analytics API
    description: REST API and web interface for accessing the Oracle Solaris 11.4 StatsStore, providing consolidated zone resource statistics, system performance data, and historical analytics via CLI, C, Python, and RAD interfaces.
    humanURL: https://docs.oracle.com/cd/E37838_01/html/E56520/index.html
    baseURL: https://solaris-host.example.com/api/v1/statsstore
    tags:
      - Analytics
      - Monitoring
      - Performance
      - REST API
      - StatsStore
      - Web Interface
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E56520/index.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E56520/sstoreintro.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E56520/ssids.html
      - type: OpenAPI
        url: openapi/solaris-statsstore-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
  - name: Oracle Solaris Unified Archives Zones API
    description: API for creating, deploying, and managing Unified Archives for zone system recovery, cloning, and migration across Oracle Solaris systems.
    humanURL: https://docs.oracle.com/cd/E37838_01/html/E60984/gmrlo.html
    baseURL: https://solaris-host.example.com/api/v1/zones/archives
    tags:
      - Backup
      - Cloning
      - Migration
      - Recovery
      - Unified Archives
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E60984/gmrlo.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E60984/gmwen.html
      - type: Documentation
        url: https://docs.oracle.com/cd/E37838_01/html/E61039/gpoiu.html
      - type: OpenAPI
        url: openapi/solaris-unified-archives-openapi.yml
    contact:
      - FN: Oracle Solaris Support
        email: solaris-support@oracle.com
        url: https://www.oracle.com/solaris/support/
common:
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/paas/api-platform/authentication.html
  - type: Support
    url: https://www.oracle.com/support/
  - type: Blog
    url: https://blogs.oracle.com/solaris/
  - type: Portal
    url: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/index.html
  - type: Resources
    url: https://www.oracle.com/solaris/technologies/solarisdeveloper.html
    title: Developer Resources
  - type: GitHubOrganization
    url: https://github.com/oracle/oraclesolaris-contrib
  - type: GettingStarted
    url: https://docs.oracle.com/cd/E37838_01/html/E61038/gitsf.html
  - type: Documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E61037/zonesoverview.html
    title: Virtual Environments Overview
  - type: Documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E61040/
    title: Zones Configuration Resources
  - type: Documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E68270/gpzpd.html
    title: RAD Client Guide
  - type: JSONLD
    url: json-ld/solaris-context.jsonld
  - type: JSONSchema
    url: json-schema/solaris-zone-schema.json
  - type: JSONSchema
    url: json-schema/solaris-zone-resource-schema.json
  - type: JSONSchema
    url: json-schema/solaris-zone-stats-schema.json
  - type: JSONSchema
    url: json-schema/solaris-zone-migration-schema.json
  - type: JSONSchema
    url: json-schema/solaris-zone-evacuation-schema.json
  - type: Features
    data:
      - name: Zone Isolation
        description: Hardware-enforced isolation between zones providing secure multi-tenant environments on a single physical system.
      - name: Live Migration
        description: Move running zones between physical systems without downtime using live migration capabilities.
      - name: Kernel Zones
        description: Non-global zones with their own independent kernel for enhanced security isolation and OS independence.
      - name: Unified Archives
        description: Create portable system archives for zone cloning, recovery, and migration across Solaris systems.
      - name: StatsStore Analytics
        description: Consolidated resource statistics and historical analytics for monitoring zone performance and capacity planning.
      - name: RAD Remote Administration
        description: RESTful remote administration daemon enabling programmatic zone management over HTTP/JSON.
      - name: Resource Capping
        description: Fine-grained CPU, memory, and swap resource controls with configurable caps per zone.
  - type: UseCases
    data:
      - name: Server Consolidation
        description: Consolidate multiple workloads onto a single physical system using zones for resource isolation and management.
      - name: Development and Testing
        description: Create isolated development and testing environments that mirror production without dedicated hardware.
      - name: Disaster Recovery
        description: Use Unified Archives and zone migration to implement disaster recovery workflows across Solaris systems.
      - name: Performance Monitoring
        description: Monitor zone resource utilization and system performance using StatsStore and zonestat APIs.
      - name: Automated Provisioning
        description: Programmatically create, configure, and deploy zones using RAD REST APIs for automated infrastructure provisioning.
  - type: Integrations
    data:
      - name: Oracle Enterprise Manager
        description: Manage Solaris Zones through Oracle Enterprise Manager for centralized infrastructure monitoring and control.
      - name: Ansible
        description: Automate zone provisioning and configuration management using Ansible playbooks with Oracle Solaris modules.
      - name: Puppet
        description: Configure and manage Solaris Zones infrastructure as code using Puppet modules for Oracle Solaris.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
  - FN: Oracle Corporation
    email: solaris-feedback@oracle.com
    url: https://www.oracle.com/solaris/
tags:
  - Containers
  - Kernel Zones
  - Operating Systems
  - Oracle
  - RAD
  - Resource Management
  - Solaris
  - StatsStore
  - Virtualization
  - Zones
---
