---
aid: cubefs
url: https://raw.githubusercontent.com/api-evangelist/cubefs/refs/heads/main/apis.yml
apis:
- aid: cubefs:cubefs-s3-api
  name: CubeFS S3-Compatible API
  description: CubeFS provides an S3-compatible object storage interface through its ObjectNode component. This allows applications using AWS S3 SDKs to interact with CubeFS storage without modification, supporting standard S3 operations including bucket management, object CRUD, multipart uploads, and access control.
  humanURL: https://cubefs.io/docs/master/user-guide/objectnode.html
  properties:
  - type: Documentation
    url: https://cubefs.io/docs/master/user-guide/objectnode.html
  - type: GitHubRepository
    url: https://github.com/cubefs/cubefs
  - type: OpenAPI
    url: openapi/cubefs-s3-api-openapi.yml
  tags:
  - Compatible API
  - Object Storage
  - S3
- aid: cubefs:cubefs-master-api
  name: CubeFS Master API
  description: The CubeFS Master API provides HTTP endpoints for cluster management including volume creation and deletion, data partition management, metadata partition management, node management, and cluster status monitoring. It serves as the control plane interface for administering CubeFS clusters.
  humanURL: https://cubefs.io/docs/master/dev-guide/master-api.html
  properties:
  - type: Documentation
    url: https://cubefs.io/docs/master/dev-guide/master-api.html
  - type: GitHubRepository
    url: https://github.com/cubefs/cubefs
  - type: OpenAPI
    url: openapi/cubefs-master-api-openapi.yml
  - type: JSONSchema
    url: json-schema/cubefs-volume-schema.json
  tags:
  - Admin API
  - Cluster Management
  - Control Plane
name: CubeFS
tags:
- Cloud Native
- Distributed File System
- Graduated
- Kubernetes
- S3 Compatible
- Storage
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CubeFS is a CNCF graduated cloud-native distributed file system that supports multiple access protocols including POSIX, HDFS, and S3-compatible object storage. It provides multi-tenancy, multi-AZ deployment, and cross-region replication for large-scale storage needs. CubeFS is designed for both hot and cold data tiers with erasure coding support.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

