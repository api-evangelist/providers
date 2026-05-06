---
aid: rook
name: Rook
description: Rook is a CNCF graduated cloud-native storage orchestrator for Kubernetes, providing the platform, framework, and support for Ceph distributed storage systems to natively integrate with cloud-native environments. It automates the deployment, configuration, provisioning, scaling, upgrading, and monitoring of storage systems through Kubernetes operators and Custom Resource Definitions (CRDs), with primary support for Ceph block storage, shared filesystems, and S3-compatible object storage.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/rook/refs/heads/main/apis.yml
tags:
  - Block Storage
  - CNCF
  - Ceph
  - Cloud Native
  - File Storage
  - Graduated
  - Kubernetes
  - Object Storage
  - Orchestration
  - Storage
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rook:rook-ceph-crd-api
    name: Rook Ceph Custom Resource API
    description: Rook extends Kubernetes through Custom Resource Definitions (CRDs) to declaratively manage Ceph storage clusters. The CRD API includes resources for CephCluster, CephBlockPool, CephFilesystem, CephObjectStore, CephObjectStoreUser, CephNFS, CephRBDMirror, and related storage primitives, enabling operators to configure and manage Ceph storage entirely through Kubernetes manifests.
    humanURL: https://rook.io/docs/rook/latest/CRDs/Cluster/ceph-cluster-crd/
    properties:
      - type: Documentation
        url: https://rook.io/docs/rook/latest/CRDs/Cluster/ceph-cluster-crd/
      - type: Reference
        url: https://rook.io/docs/rook/latest/CRDs/
      - type: JSONSchema
        url: json-schema/rook-ceph-cluster-schema.json
      - type: JSONStructure
        url: json-structure/rook-ceph-cluster-structure.json
    tags:
      - Ceph
      - CRD
      - Declarative
      - Kubernetes
      - Storage
  - aid: rook:rook-ceph-object-storage-api
    name: Rook Ceph Object Storage API
    description: Rook provisions Ceph Object Storage gateways (RGW) that expose an S3-compatible and Swift-compatible object storage API. Applications can interact with Ceph Object Storage using standard S3 API clients, and Rook manages the lifecycle of the object store, buckets, and user credentials through Kubernetes CRDs.
    humanURL: https://rook.io/docs/rook/latest/CRDs/Object-Storage/ceph-object-store-crd/
    properties:
      - type: Documentation
        url: https://rook.io/docs/rook/latest/CRDs/Object-Storage/ceph-object-store-crd/
      - type: Reference
        url: https://rook.io/docs/rook/latest/CRDs/Object-Storage/
      - type: OpenAPI
        url: openapi/rook-ceph-object-storage-openapi.yml
      - type: JSONSchema
        url: json-schema/rook-ceph-object-store-schema.json
      - type: JSONStructure
        url: json-structure/rook-ceph-object-store-structure.json
    tags:
      - Ceph
      - Object Storage
      - S3
      - Storage
      - Swift
  - aid: rook:rook-ceph-block-storage-api
    name: Rook Ceph Block Storage API
    description: Rook provides Ceph block storage (RBD) through Kubernetes StorageClasses and PersistentVolumeClaims. The CephBlockPool CRD and associated StorageClass allow applications to dynamically provision block volumes backed by Ceph RADOS Block Device, supporting ReadWriteOnce access modes for stateful workloads.
    humanURL: https://rook.io/docs/rook/latest/CRDs/Block-Storage/ceph-block-pool-crd/
    properties:
      - type: Documentation
        url: https://rook.io/docs/rook/latest/CRDs/Block-Storage/ceph-block-pool-crd/
      - type: Reference
        url: https://rook.io/docs/rook/latest/CRDs/Block-Storage/
      - type: JSONSchema
        url: json-schema/rook-ceph-block-pool-schema.json
      - type: JSONStructure
        url: json-structure/rook-ceph-block-pool-structure.json
    tags:
      - Block Storage
      - Ceph
      - Kubernetes
      - PersistentVolume
      - RBD
  - aid: rook:rook-ceph-filesystem-api
    name: Rook Ceph Shared Filesystem API
    description: Rook manages CephFilesystem resources to provision shared POSIX-compliant file storage backed by CephFS. Multiple pods can simultaneously read and write to shared filesystem volumes, making it suitable for workloads requiring ReadWriteMany access, configured through the CephFilesystem CRD and a corresponding StorageClass.
    humanURL: https://rook.io/docs/rook/latest/CRDs/Shared-Filesystem/ceph-filesystem-crd/
    properties:
      - type: Documentation
        url: https://rook.io/docs/rook/latest/CRDs/Shared-Filesystem/ceph-filesystem-crd/
      - type: Reference
        url: https://rook.io/docs/rook/latest/CRDs/Shared-Filesystem/
      - type: JSONSchema
        url: json-schema/rook-ceph-filesystem-schema.json
      - type: JSONStructure
        url: json-structure/rook-ceph-filesystem-structure.json
    tags:
      - CephFS
      - File Storage
      - Kubernetes
      - POSIX
      - Shared Filesystem
common:
  - type: JSONSchema
    url: json-schema/rook-ceph-cluster-schema.json
  - type: JSONSchema
    url: json-schema/rook-ceph-block-pool-schema.json
  - type: JSONSchema
    url: json-schema/rook-ceph-filesystem-schema.json
  - type: JSONSchema
    url: json-schema/rook-ceph-object-store-schema.json
  - type: JSONStructure
    url: json-structure/rook-ceph-cluster-structure.json
  - type: JSON-LD
    url: json-ld/rook-context.jsonld
  - type: Vocabulary
    url: vocabulary/rook-vocabulary.yml
  - type: Rules
    url: rules/rook-spectral-rules.yml
  - type: Capabilities
    url: capabilities/storage-orchestration.yaml
  - type: Website
    url: https://rook.io
  - type: Documentation
    url: https://rook.io/docs/rook/latest/
  - type: Getting Started
    url: https://rook.io/docs/rook/latest/Getting-Started/quickstart/
  - type: GitHub Organization
    url: https://github.com/rook
  - type: GitHubRepository
    url: https://github.com/rook/rook
  - type: Blog
    url: https://blog.rook.io/
  - type: Community
    url: https://rook.io/community/
  - type: Slack
    url: https://slack.rook.io
  - type: Change Log
    url: https://github.com/rook/rook/blob/master/CHANGELOG.md
  - type: Security
    url: https://github.com/rook/rook/blob/master/SECURITY.md
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/rook
  - type: X
    url: https://twitter.com/rook_io
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
