---
aid: rook
url: https://raw.githubusercontent.com/api-evangelist/rook/refs/heads/main/apis.yml
apis:
- aid: rook:rook-ceph-crd-api
  name: Rook Ceph Custom Resource API
  description: Rook extends Kubernetes through Custom Resource Definitions (CRDs) to declaratively manage Ceph storage clusters. The CRD API includes resources for CephCluster, CephBlockPool, CephFilesystem, CephObjectStore, CephObjectStoreUser, and related storage primitives, enabling operators to configure and manage Ceph storage entirely through Kubernetes manifests.
  humanURL: https://rook.io/docs/rook/latest/CRDs/Cluster/ceph-cluster-crd/
  properties:
  - type: Documentation
    url: https://rook.io/docs/rook/latest/CRDs/Cluster/ceph-cluster-crd/
  - type: Reference
    url: https://rook.io/docs/rook/latest/CRDs/
  - type: JSONSchema
    url: json-schema/rook-ceph-cluster-schema.json
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
  tags:
  - CephFS
  - File Storage
  - Kubernetes
  - POSIX
  - Shared Filesystem
name: Rook
tags:
- Ceph
- Cloud Native
- Graduated
- Kubernetes
- Orchestration
- Storage
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Rook is a CNCF graduated cloud-native storage orchestrator for Kubernetes, providing the platform, framework, and support for distributed storage systems to natively integrate with cloud-native environments. It automates the deployment, configuration, provisioning, scaling, upgrading, and monitoring of storage systems, with primary support for Ceph.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

