---
name: Veritas Volume Manager
description: APIs for managing storage volumes, disk groups, and file systems using Veritas Volume Manager (VVM).
image: https://www.veritas.com/content/dam/veritas/images/logos/veritas-logo.svg
url: https://www.veritas.com/support/en_US/volume-manager
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.16'
tags:
  - Disaster Recovery
  - Enterprise Storage
  - File Systems
  - Storage
  - Volume Management
apis:
  - name: Veritas Volume Manager REST API
    description: RESTful API for managing storage volumes, disk groups, and storage operations.
    image: https://www.veritas.com/content/dam/veritas/images/logos/veritas-logo.svg
    humanURL: https://www.veritas.com/support/en_US/volume-manager
    baseURL: https://api.veritas.com/vvm/v1
    tags:
      - Disk Groups
      - Snapshots
      - Storage Pools
      - Volumes
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/article.DOC5555
      - type: OpenAPI
        url: https://api.veritas.com/vvm/v1/openapi.json
      - type: Authentication
        url: https://www.veritas.com/support/en_US/article.AUTH100
      - type: SDK
        url: https://www.veritas.com/support/en_US/downloads/sdks
      - type: RateLimits
        url: https://www.veritas.com/support/en_US/article.LIMITS100
    contact:
      - type: Support
        url: https://www.veritas.com/support/en_US/contact-support
      - type: Email
        url: mailto:support@veritas.com
      - type: Twitter
        url: https://twitter.com/Veritas
  - name: VxVM Command Line API
    description: Command-line interface and scripting API for Veritas Volume Manager operations.
    humanURL: https://www.veritas.com/support/en_US/article.VXVM100
    tags:
      - Administration
      - CLI
      - Scripting
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/article.CLI5555
      - type: APIReference
        url: https://www.veritas.com/support/en_US/article.CMDREF100
      - type: CodeExamples
        url: https://www.veritas.com/support/en_US/article.EXAMPLES100
  - name: Storage Foundation API
    description: Comprehensive API for Veritas Storage Foundation including volume management.
    humanURL: https://www.veritas.com/support/en_US/storage-foundation
    baseURL: https://api.veritas.com/sf/v1
    tags:
      - Enterprise
      - High Availability
      - Storage Foundation
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/article.SF5555
      - type: APIReference
        url: https://api.veritas.com/sf/v1/docs
  - name: Veritas InfoScale REST API
    description: REST API for InfoScale storage configuration and management operations including volume, disk group, and cluster management. The REST server is configured on cluster nodes and supports operations for storage provisioning, snapshots, replication, and high availability management.
    humanURL: https://www.veritas.com/support/en_US/doc/79638609-149461849-0/v151837041-149461849
    tags:
      - Cluster Management
      - High Availability
      - Infoscale
      - REST
      - Storage Configuration
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/79638609-149461849-0/v151837041-149461849
      - type: APIReference
        url: https://www.veritas.com/support/en_US/doc/79638609-149461849-0/v151832379-149461849
      - type: ReleaseNotes
        url: https://www.veritas.com/support/en_US/doc/109864724-166315456-0/index
  - name: Veritas InfoScale 9.0 REST API
    description: REST API support for InfoScale 9.0 providing storage configuration and management operations, including HA configuration for the REST server and expanded supported operations for enterprise storage management.
    humanURL: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
    tags:
      - Enterprise
      - Infoscale
      - REST
      - Storage Management
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151832379-166315478
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v151835060-166315478
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/79638609-166315478-0/v109543903-166315478
  - name: InfoScale Operations Manager Web Services API
    description: HTTPS-based Web Services API for Veritas InfoScale Operations Manager (VIOM) providing the ability to query discovered data, manage user-defined attributes, and perform operations on InfoScale objects. Supports Meta, Query, Update, and Operations API categories accessible via standard HTTPS clients including cURL.
    humanURL: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/index
    tags:
      - Management
      - Monitoring
      - Operations Manager
      - VIOM
      - Web Services
    properties:
      - type: Documentation
        url: https://sort.veritas.com/public/documents/vom/7.3/windowsandunix/productguides/html/viom_user/ch38.htm
      - type: GettingStarted
        url: https://sort.veritas.com/public/documents/vom/7.3/windowsandunix/productguides/html/viom_user/ch38s01.htm
      - type: Authentication
        url: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/viom_tot_v84306317-156079406
      - type: APIReference
        url: https://sort.veritas.com/public/documents/vom/7.3/windowsandunix/productguides/html/viom_user/ch38s05.htm
      - type: CodeExamples
        url: https://www.veritas.com/support/en_US/doc/120572053-156079406-0/viom_tot_v96894970-156079406
      - type: APIReference
        url: https://www.veritas.com/content/support/en_US/doc/132757515-132757518-0/br74_viom_tot_v96212267-132757518
  - name: InfoScale for Kubernetes API
    description: API for administering and monitoring InfoScale in Kubernetes and OpenShift container environments. Provides CSI driver integration for persistent storage, volume snapshots, and storage class management with enterprise data services for containerized applications.
    humanURL: https://www.veritas.com/support/en_US/doc/167166372-167166485-0/v167165336-167166485
    tags:
      - Cloud Native
      - Containers
      - CSI
      - Kubernetes
      - Openshift
    properties:
      - type: Documentation
        url: https://www.veritas.com/support/en_US/doc/167166372-167166485-0/v167165336-167166485
      - type: GettingStarted
        url: https://www.veritas.com/support/en_US/doc/161711084-161711096-0/index
      - type: Documentation
        url: https://www.veritas.com/support/en_US/downloads/detail.REL134671
common:
  - type: Portal
    url: https://my.veritas.com
  - type: GettingStarted
    url: https://www.veritas.com/support/en_US/article.GETSTART100
  - type: TermsOfService
    url: https://www.veritas.com/about/legal/license-agreements
  - type: PrivacyPolicy
    url: https://www.veritas.com/about/legal/privacy-policy
  - type: StatusPage
    url: https://status.veritas.com
  - type: ChangeLog
    url: https://www.veritas.com/support/en_US/article.CHANGELOG
  - type: Blog
    url: https://www.veritas.com/blogs
  - type: Support
    url: https://www.veritas.com/support/en_US/dpp.InfoScaleStorageFoundation
  - type: Features
    url: https://www.veritas.com/availability/infoscale
  - type: UseCases
    url: https://www.veritas.com/availability/infoscale
  - type: Integrations
    url: https://www.veritas.com/availability/infoscale
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
  - name: Veritas Technologies LLC
    email: api-support@veritas.com
    url: https://www.veritas.com
  - name: API Team
    email: api-team@veritas.com
include:
  - name: Volume Operations
    url: https://api.veritas.com/vvm/v1/apis/volumes.yaml
  - name: Disk Group Operations
    url: https://api.veritas.com/vvm/v1/apis/diskgroups.yaml
  - name: Snapshot Operations
    url: https://api.veritas.com/vvm/v1/apis/snapshots.yaml
---
