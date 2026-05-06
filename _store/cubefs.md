---
aid: cubefs
url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/apis.yml
x-type: opensource
name: CubeFS
description: CubeFS is a CNCF graduated cloud-native distributed file system supporting POSIX, HDFS, and S3-compatible object storage protocols. It provides multi-tenancy, multi-AZ deployment, cross-region replication, and erasure coding for both hot and cold data tiers, and is widely used to back cloud-native AI training, big-data analytics, and container storage workloads.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - CNCF Graduated
  - Distributed File System
  - Kubernetes
  - Object Storage
  - POSIX
  - S3 Compatible
  - Storage
type: Index
specificationVersion: '0.19'
created: '2026-03-16'
modified: '2026-04-28'
apis:
  - aid: cubefs:cubefs-s3-api
    name: CubeFS S3-Compatible API
    description: CubeFS exposes an S3-compatible object storage interface through its ObjectNode component. AWS S3 SDKs work without modification for bucket management, object CRUD, multipart uploads, and access control.
    humanURL: https://cubefs.io/docs/master/user-guide/objectnode.html
    tags:
      - Compatible API
      - Object Storage
      - S3
    properties:
      - type: Documentation
        url: https://cubefs.io/docs/master/user-guide/objectnode.html
      - type: GitHubRepository
        url: https://github.com/cubefs/cubefs
      - type: OpenAPI
        url: openapi/cubefs-s3-api-openapi.yml
      - type: SpectralRules
        url: rules/cubefs-s3-rules.yml
  - aid: cubefs:cubefs-master-api
    name: CubeFS Master API
    description: The CubeFS Master API provides HTTP endpoints for cluster management including volume creation/deletion, data and meta partition management, data and meta node management, user/policy management, and cluster status monitoring. It is the control plane interface for administering CubeFS clusters.
    humanURL: https://cubefs.io/docs/master/dev-guide/master-api.html
    tags:
      - Admin API
      - Cluster Management
      - Control Plane
    properties:
      - type: Documentation
        url: https://cubefs.io/docs/master/dev-guide/master-api.html
      - type: GitHubRepository
        url: https://github.com/cubefs/cubefs
      - type: OpenAPI
        url: openapi/cubefs-master-api-openapi.yml
      - type: JSONSchema
        url: json-schema/cubefs-volume-schema.json
      - type: SpectralRules
        url: rules/cubefs-master-rules.yml
features:
  - name: Multi-Protocol Access
    description: Single backend serves POSIX (FUSE), HDFS, and S3-compatible clients.
  - name: Multi-Tenancy
    description: Tenant isolation by user, access key, and per-volume policies.
  - name: Multi-AZ Deployment
    description: Replication across availability zones with optional cross-zone partitions.
  - name: Erasure Coding
    description: Parity-coded storage to reduce overhead for cold data tiers.
  - name: Container Storage
    description: First-class CSI driver for Kubernetes persistent volumes.
  - name: Master Control Plane
    description: HTTP master API for volume, node, partition, and user management.
  - name: S3-Compatible ObjectNode
    description: ObjectNode gateway exposes standard S3 verbs to AWS SDK clients.
  - name: CNCF Graduated
    description: Project status, governance, and community managed under the CNCF.
useCases:
  - name: AI/ML Training Storage
    description: Large training datasets stored on CubeFS via POSIX or S3 access.
  - name: Big Data Analytics
    description: HDFS clients run analytics on CubeFS-backed datasets.
  - name: Cloud-Native Object Storage
    description: Apps use S3-compatible buckets backed by CubeFS without AWS dependency.
  - name: Kubernetes Persistent Volumes
    description: CubeFS CSI driver provides RWX persistent volumes to stateful workloads.
  - name: Multi-Region Storage
    description: Cross-region replication backs disaster recovery and locality strategies.
  - name: Hot/Cold Tiering
    description: Replicated tier for hot data and erasure-coded tier for cold data.
common:
  - type: JSON-LD
    url: json-ld/cubefs-context.jsonld
    name: CubeFS JSON-LD Context
    description: Linked-data context mapping CubeFS resources to standard vocabularies.
  - type: JSONSchema
    url: json-schema/cubefs-volume-schema.json
    name: CubeFS Volume JSON Schema
    description: JSON Schema for CubeFS volume, partition, node, and user data models.
  - type: Vocabulary
    url: vocabulary/cubefs-vocabulary.yml
    name: CubeFS Vocabulary
  - type: SpectralRules
    url: rules/cubefs-master-rules.yml
    name: CubeFS Master API Spectral Rules
  - type: SpectralRules
    url: rules/cubefs-s3-rules.yml
    name: CubeFS S3 API Spectral Rules
  - type: Website
    name: CubeFS Website
    description: Official CubeFS project website.
    url: https://cubefs.io/
  - type: Documentation
    name: CubeFS Documentation
    description: Official documentation for CubeFS.
    url: https://cubefs.io/docs/master/overview/introduction.html
  - type: GettingStarted
    name: CubeFS Quick Start
    description: Quick start guide for deploying CubeFS.
    url: https://cubefs.io/docs/master/quickstart/single-deploy.html
  - type: ChangeLog
    name: CubeFS Changelog
    description: Version history and changelog for CubeFS releases.
    url: https://github.com/cubefs/cubefs/blob/master/CHANGELOG.md
  - type: GitHubOrganization
    name: CubeFS GitHub Organization
    description: GitHub organization hosting all CubeFS source code.
    url: https://github.com/cubefs
  - type: GitHubRepository
    name: CubeFS GitHub Repository
    description: Main CubeFS source code repository.
    url: https://github.com/cubefs/cubefs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
