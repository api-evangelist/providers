---
aid: solaris-zones
url: https://raw.githubusercontent.com/api-evangelist/solaris-zones/refs/heads/main/apis.yml
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
  - type: documentation
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
  - type: documentation
    url: https://docs.oracle.com/cd/E88353_01/html/E37839/zonecfg-1m.html
  - type: documentation
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
  - type: documentation
    url: https://docs.oracle.com/cd/E88353_01/html/E37839/zoneadm-1m.html
  - type: documentation
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
  - type: documentation
    url: https://docs.oracle.com/cd/E88353_01/html/E37839/zonestat-1.html
  - type: documentation
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
  - Rad
  - Remote-Administration
  - Rest-Api
  - Zones
  properties:
  - type: documentation
    url: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/rad-client/rest-api-reference.html
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E68270/gpzpd.html
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E68270/gpzpv.html
  - type: documentation
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
  - Cpu
  - Libzonestat
  - Memory
  - Monitoring
  - Resource-Utilization
  - Statistics
  properties:
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E61043/
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E61043/gklfn.html
  - type: documentation
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
  - Kernel-Zones
  - Security
  - Virtualization
  properties:
  - type: documentation
    url: https://docs.oracle.com/en/operating-systems/solaris/oracle-solaris/11.4/kernel-zones/oracle-solaris-kernel-zones.html
  - type: documentation
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
  - Rest-Api
  - Statsstore
  - Web-Interface
  properties:
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E56520/index.html
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E56520/sstoreintro.html
  - type: documentation
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
  - Unified-Archives
  properties:
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E60984/gmrlo.html
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E60984/gmwen.html
  - type: documentation
    url: https://docs.oracle.com/cd/E37838_01/html/E61039/gpoiu.html
  - type: OpenAPI
    url: openapi/solaris-unified-archives-openapi.yml
  contact:
  - FN: Oracle Solaris Support
    email: solaris-support@oracle.com
    url: https://www.oracle.com/solaris/support/
name: Solaris Zones
tags:
- Containers
- Kernel-Zones
- Operating-Systems
- Oracle
- Rad
- Resource-Management
- Solaris
- Statsstore
- Virtualization
- Zones
type: Contract
image: https://www.oracle.com/a/ocom/img/cb71-solaris.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API for managing Solaris Zones (containers) and virtualization on Oracle Solaris systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

