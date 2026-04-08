---
aid: veritas-cluster
url: https://raw.githubusercontent.com/api-evangelist/veritas-cluster/refs/heads/main/apis.yml
apis:
- name: Veritas Cluster Server REST API
  description: RESTful API for managing cluster resources, service groups, and cluster configuration.
  baseURL: https://{vcs-management-server}:14150/api/v1
  humanURL: https://www.veritas.com/support/en_US/article.100040102
  tags:
  - Cluster Management
  - Resources
  - REST
  - Service Groups
  properties:
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/vcs/8.0/linux/productguides/html/vcs_rest_api/index.htm
  - type: X-openapi
    url: https://vcs-server:14150/api/docs/openapi.json
  - type: X-authentication
    url: https://sort.veritas.com/public/documents/vcs/8.0/linux/productguides/html/vcs_rest_api/ch02.htm
  contact:
  - FN: Veritas Support
    email: support@veritas.com
    X-twitter: VeritasTechLLC
- name: Veritas Cluster Server Python API
  description: Python SDK for programmatic cluster management and automation.
  baseURL: https://{vcs-management-server}:14150
  humanURL: https://www.veritas.com/support/en_US/article.100040102
  tags:
  - Automation
  - Python
  - Scripting
  - SDK
  properties:
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/vcs/8.0/linux/productguides/html/vcs_python_api/
  - type: X-sdk-python
    url: https://sort.veritas.com/public/documents/vcs/8.0/linux/productguides/html/vcs_python_api/ch01s02.htm
- name: Veritas Cluster Server Java API
  description: Java-based API for integrating VCS management into enterprise applications.
  humanURL: https://www.veritas.com/support/en_US/article.DOC5308
  tags:
  - Enterprise Integration
  - Java
  - SDK
  properties:
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/vcs/7.4/linux/productguides/html/vcs_java_api/
  - type: X-sdk-java
    url: https://sort.veritas.com/public/documents/vcs/7.4/linux/productguides/html/vcs_java_api/ch01s03.htm
- name: Veritas Cluster Server Command Line Interface
  description: Command-line tools for cluster administration and monitoring.
  humanURL: https://www.veritas.com/support/en_US/article.DOC5308
  tags:
  - Administration
  - CLI
  - Command Line
  - Monitoring
  properties:
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/vcs/8.0/linux/productguides/html/vcs_admin/index.htm
  - type: X-command-reference
    url: https://sort.veritas.com/public/documents/vcs/8.0/linux/productguides/html/vcs_command_reference/
- name: Veritas Cluster Server SNMP Agent
  description: SNMP-based monitoring interface for cluster health and status.
  humanURL: https://www.veritas.com/support/en_US/article.DOC5308
  tags:
  - Alerting
  - Monitoring
  - SNMP
  - Traps
  properties:
  - type: X-documentation
    url: https://sort.veritas.com/public/documents/vcs/8.0/linux/productguides/html/vcs_admin/ch22.htm
  - type: X-mib-files
    url: https://www.veritas.com/support/en_US/article.TECH95356
- name: Veritas InfoScale REST API
  description: REST API for InfoScale storage and cluster configuration and management operations, supporting storage provisioning, disk group management, and volume operations. Available in InfoScale 8.0 and 9.0.
  baseURL: https://{infoscale-rest-server}:14150/infoscale/api/2.0
  humanURL: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
  tags:
  - Cluster Management
  - InfoScale
  - REST
  - Storage Management
  - Volume Management
  properties:
  - type: X-documentation
    url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
  - type: X-supported-operations
    url: https://www.veritas.com/support/en_US/doc/79638609-149461849-0/v151832379-149461849
  - type: X-rest-server-configuration
    url: https://www.veritas.com/support/en_US/doc/79638609-149461849-0/v151837041-149461849
  - type: X-ha-configuration
    url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151835060-166315478
  - type: X-release-notes
    url: https://www.veritas.com/support/en_US/doc/109864724-166315456-0/v151831652-166315456
  - type: X-metrics
    url: https://{infoscale-rest-server}:14150/infoscale/api/2.0/metrics
- name: Veritas InfoScale Operations Manager Web Services API
  description: Web services API for InfoScale Operations Manager (VIOM) providing meta, query, update, and operations APIs for managing InfoScale objects over HTTPS. Supports management of hosts, clusters, LDEVs, and virtualization servers.
  baseURL: https://{management-server}:14161/vom/api
  humanURL: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/index
  tags:
  - Management
  - Monitoring
  - Operations Manager
  - REST
  - VIOM
  - Web Services
  properties:
  - type: X-documentation
    url: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/index
  - type: X-authentication
    url: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/viom_tot_v84306317-156079406
  - type: X-examples
    url: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/viom_tot_v96894970-156079406
  - type: X-supported-objects
    url: https://www.veritas.com/content/support/en_US/doc/132757515-132757518-0/br74_viom_tot_v96212267-132757518
  - type: X-blog
    url: https://vox.veritas.com/blog/storage-and-availability-management/increasing-flexibility-for-infoscale-environments-with-the-viom-api/881889
  - type: X-download
    url: https://www.veritas.com/support/en_US/downloads/detail.REL133180
  - type: X-installation-guide
    url: https://www.veritas.com/support/en_US/doc/120571566-156079382-0/index
- name: Veritas InfoScale for Kubernetes Environments
  description: InfoScale container support for Kubernetes and OpenShift, providing CSI-compliant storage drivers for dynamic and static provisioning, volume snapshots, and Prometheus metrics integration for monitoring.
  humanURL: https://www.veritas.com/support/en_US/doc/167166372-167166485-0/index
  tags:
  - Containers
  - CSI
  - Kubernetes
  - Monitoring
  - OpenShift
  - Prometheus
  - Storage Provisioning
  properties:
  - type: X-documentation
    url: https://www.veritas.com/support/en_US/doc/167166372-167166485-0/index
  - type: X-monitoring
    url: https://www.veritas.com/support/en_US/doc/167166372-167166485-0/v167165336-167166485
  - type: X-container-support
    url: https://www.veritas.com/support/en_US/doc/151215298-151215302-0/index
name: Veritas Cluster Server
tags:
- Clustering
- Containers
- Disaster Recovery
- Failover
- High Availability
- InfoScale
- Infrastructure Management
- Kubernetes
- Storage Management
- Veritas
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for managing and monitoring Veritas Cluster Server (VCS) and InfoScale infrastructure, providing high availability, disaster recovery, and storage management capabilities across on-premises and containerized environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

