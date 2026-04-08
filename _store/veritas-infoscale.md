---
aid: veritas-infoscale
url: https://raw.githubusercontent.com/api-evangelist/veritas-infoscale/refs/heads/main/apis.yml
apis:
- name: Veritas InfoScale REST API
  description: REST API for managing InfoScale clusters, storage resources, and high availability configurations.
  image: https://www.veritas.com/content/dam/Veritas/images/logos/veritas-logo.svg
  humanURL: https://www.veritas.com/support/en_US/doc/infoscale
  baseURL: https://<infoscale-server>:14149/api/v1
  tags:
  - Availability
  - Clustering
  - Storage
  properties:
  - type: Documentation
    url: https://sort.veritas.com/documents/infoscale
  - type: OpenAPI
    url: https://<infoscale-server>:14149/api/v1/swagger.json
  - type: Authentication
    url: https://www.veritas.com/support/en_US/doc/infoscale/8.0/rest-api-guide
  contact:
  - FN: Veritas Support
    email: support@veritas.com
    url: https://www.veritas.com/support
- name: Veritas InfoScale Operations Manager API
  description: API for centralized monitoring and management of InfoScale environments.
  image: https://www.veritas.com/content/dam/Veritas/images/logos/veritas-logo.svg
  humanURL: https://www.veritas.com/support/en_US/doc/infoscale-operations-manager
  baseURL: https://<isom-server>:8443/api
  tags:
  - Management
  - Monitoring
  - Operations
  properties:
  - type: Documentation
    url: https://www.veritas.com/support/en_US/doc/infoscale-operations-manager/api-reference
  - type: API Reference
    url: https://sort.veritas.com/documents/isom
- name: Veritas Cluster Server (VCS) API
  description: API for managing VCS clusters, service groups, and resources within InfoScale.
  image: https://www.veritas.com/content/dam/Veritas/images/logos/veritas-logo.svg
  humanURL: https://www.veritas.com/support/en_US/doc/cluster-server
  baseURL: https://<vcs-server>:14149/vcs/api
  tags:
  - Clustering
  - Failover
  - High Availability
  properties:
  - type: Documentation
    url: https://sort.veritas.com/documents/vcs/api-guide
  - type: Command Line Reference
    url: https://www.veritas.com/support/en_US/doc/cluster-server/cli-reference
- name: Veritas Volume Manager (VxVM) API
  description: API for storage volume management, including volume creation, resizing, and snapshot operations.
  image: https://www.veritas.com/content/dam/Veritas/images/logos/veritas-logo.svg
  humanURL: https://www.veritas.com/support/en_US/doc/volume-manager
  baseURL: https://<server>:14149/vxvm/api
  tags:
  - Snapshots
  - Storage
  - Volumes
  properties:
  - type: Documentation
    url: https://sort.veritas.com/documents/vxvm
  - type: Administrator's Guide
    url: https://www.veritas.com/support/en_US/doc/volume-manager/admin-guide
name: Veritas InfoScale
tags:
- Clustering
- Data Management
- Disaster Recovery
- High Availability
- Storage Management
- Virtualization
type: Contract
image: https://www.veritas.com/content/dam/Veritas/images/logos/veritas-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Veritas InfoScale, an enterprise storage and availability management solution that provides high availability, disaster recovery, and storage management capabilities across physical, virtual, and cloud environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

