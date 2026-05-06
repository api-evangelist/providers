---
aid: vitess
name: Vitess
description: Vitess is a CNCF graduated database clustering system for horizontal scaling of MySQL through generalized sharding. It provides MySQL protocol compatibility, automated resharding, query routing, and connection pooling, making it suitable for running large-scale MySQL deployments on Kubernetes or other container orchestration platforms.
type: Index
url: https://vitess.io
tags:
  - Cloud Native
  - CNCF
  - Database
  - Distributed Systems
  - Graduated
  - MySQL
  - Sharding
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vitess:vtgate-api
    name: Vitess VTGate API
    description: VTGate is the stateless proxy that routes queries to the appropriate VTTablet instances. It exposes a MySQL-compatible interface and a gRPC API that clients use to interact with the Vitess cluster, handling query routing, scatter queries, and transaction management across shards.
    humanURL: https://vitess.io/docs/reference/programs/vtgate/
    properties:
      - type: Documentation
        url: https://vitess.io/docs/reference/programs/vtgate/
      - type: Reference
        url: https://vitess.io/docs/reference/query-serving/
    tags:
      - gRPC
      - MySQL
      - Proxy
      - Query Routing
      - SQL
  - aid: vitess:vtadmin-api
    name: Vitess VTAdmin API
    description: VTAdmin is the administrative web application and REST API for managing Vitess clusters. It provides endpoints for inspecting cluster topology, tablets, keyspaces, shards, schemas, and VReplication workflows, and serves as the backend for the VTAdmin web UI.
    humanURL: https://vitess.io/docs/reference/programs/vtadmin/
    properties:
      - type: Documentation
        url: https://vitess.io/docs/reference/programs/vtadmin/
      - type: Reference
        url: https://vitess.io/docs/reference/vtadmin/
      - type: OpenAPI
        url: openapi/vitess-vtadmin-openapi.yml
    tags:
      - Administration
      - Cluster Management
      - REST
      - Web UI
  - aid: vitess:vtctld-api
    name: Vitess VTCtld API
    description: VTCtld is the Vitess topology management daemon that exposes a gRPC and HTTP API for administrative operations on the cluster topology including creating and managing keyspaces, shards, tablets, and executing maintenance operations such as planned reparents and emergency reparents.
    humanURL: https://vitess.io/docs/reference/programs/vtctld/
    properties:
      - type: Documentation
        url: https://vitess.io/docs/reference/programs/vtctld/
      - type: Reference
        url: https://vitess.io/docs/reference/vtctl/
    tags:
      - Administration
      - Cluster Management
      - gRPC
      - Topology
  - aid: vitess:vreplication-api
    name: Vitess VReplication API
    description: VReplication is the Vitess framework for replicating and transforming data streams within and across Vitess clusters. It powers features such as MoveTables, Reshard, Materialize, and CreateLookupVindex and exposes workflow management commands through the VTCtl API for orchestrating data migrations and real-time replication workflows.
    humanURL: https://vitess.io/docs/reference/vreplication/
    properties:
      - type: Documentation
        url: https://vitess.io/docs/reference/vreplication/
      - type: Reference
        url: https://vitess.io/docs/reference/vreplication/vreplication/
    tags:
      - Data Migration
      - Replication
      - Streaming
      - Workflows
common:
  - type: JSONSchema
    url: json-schema/vitess-topology-schema.json
  - type: JSONLD
    url: json-ld/vitess-context.jsonld
  - type: JSONStructure
    url: json-structure/vitess-tablet-structure.json
  - type: OpenAPI
    url: openapi/vitess-vtadmin-openapi.yml
  - type: SpectralRules
    url: rules/vitess-rules.yml
  - type: Vocabulary
    url: vocabulary/vitess-vocabulary.yml
  - type: Website
    url: https://vitess.io
  - type: Documentation
    url: https://vitess.io/docs/
  - type: Getting Started
    url: https://vitess.io/docs/get-started/
  - type: GitHub Organization
    url: https://github.com/vitessio
  - type: GitHubRepository
    url: https://github.com/vitessio/vitess
  - type: Blog
    url: https://vitess.io/blog/
  - type: Community
    url: https://vitess.io/community/
  - type: Slack
    url: https://vitess.io/slack
  - type: Change Log
    url: https://github.com/vitessio/vitess/blob/main/changelog/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/vitess
  - type: Security
    url: https://github.com/vitessio/vitess/blob/main/SECURITY.md
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
