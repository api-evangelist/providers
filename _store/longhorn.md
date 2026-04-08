---
aid: longhorn
url: https://raw.githubusercontent.com/api-evangelist/longhorn/refs/heads/main/apis.yml
apis:
- aid: longhorn:longhorn-api
  name: Longhorn Manager API
  description: The Longhorn Manager exposes a REST API for volume lifecycle management including creating, attaching, detaching, and deleting volumes. It also provides endpoints for snapshot management, backup operations, node management, engine image management, and system settings configuration. The API is used by the Longhorn UI and can be accessed directly for automation.
  humanURL: https://longhorn.io/docs/
  properties:
  - type: Documentation
    url: https://longhorn.io/docs/
  - type: GitHubRepository
    url: https://github.com/longhorn/longhorn
  - type: OpenAPI
    url: openapi/longhorn-manager-api-openapi.yml
  - type: JSONSchema
    url: json-schema/longhorn-volume-schema.json
  tags:
  - REST API
  - Snapshots
  - Volume Management
name: Longhorn
tags:
- Backup
- Block Storage
- Cloud Native
- Incubating
- Kubernetes
- Persistent Volumes
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Longhorn is a CNCF incubating lightweight, reliable, and easy-to-use distributed block storage system for Kubernetes. It creates a dedicated storage controller for each volume and replicates data across multiple nodes for high availability. Longhorn supports snapshots, backups to S3-compatible storage, disaster recovery, and recurring backup schedules.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

