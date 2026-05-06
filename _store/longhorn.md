---
aid: longhorn
name: Longhorn
description: Longhorn is a CNCF incubating lightweight, reliable, and easy-to-use distributed block storage system for Kubernetes. It creates a dedicated storage controller for each volume and replicates data across multiple nodes for high availability. Longhorn supports snapshots, backups to S3-compatible storage, disaster recovery, and recurring backup schedules.
url: https://longhorn.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backup
  - Block Storage
  - Cloud Native
  - Incubating
  - Kubernetes
  - Persistent Volumes
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
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
common:
  - type: JSON-LD
    url: json-ld/longhorn-context.jsonld
    name: Longhorn JSON-LD Context
    description: Linked data context mapping Longhorn resources to standard vocabularies.
  - type: JSONSchema
    url: json-schema/longhorn-volume-schema.json
    name: Longhorn Volume JSON Schema
    description: JSON Schema for Longhorn volume, replica, snapshot, node, and recurring job data models.
  - type: Website
    name: Longhorn Website
    description: Official Longhorn project website.
    url: https://longhorn.io/
  - type: Documentation
    name: Longhorn Documentation
    description: Official Longhorn documentation.
    url: https://longhorn.io/docs/
  - type: Getting Started
    name: Longhorn Quick Installation
    description: Quick installation guide for deploying Longhorn on Kubernetes.
    url: https://longhorn.io/docs/1.11.1/deploy/install/
  - type: Blog
    name: Longhorn Blog
    description: Official Longhorn blog with release announcements and articles.
    url: https://longhorn.io/blog/
  - type: Change Log
    name: Longhorn Releases
    description: Release history and changelogs for Longhorn.
    url: https://github.com/longhorn/longhorn/releases
  - type: GitHub Organization
    name: Longhorn GitHub Organization
    description: GitHub organization hosting all Longhorn source code.
    url: https://github.com/longhorn
  - type: GitHubRepository
    name: Longhorn GitHub Repository
    description: Main Longhorn source code repository.
    url: https://github.com/longhorn/longhorn
  - type: Community
    name: Longhorn Community
    description: Community resources including Slack, mailing lists, and discussions.
    url: https://longhorn.io/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
