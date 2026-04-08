---
aid: vitess
url: https://raw.githubusercontent.com/api-evangelist/vitess/refs/heads/main/apis.yml
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
name: Vitess
tags:
- Cloud Native
- Database
- Distributed Systems
- Graduated
- MySQL
- Sharding
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Vitess is a CNCF graduated database clustering system for horizontal scaling of MySQL through generalized sharding. It provides MySQL protocol compatibility, automated resharding, query routing, and connection pooling, making it suitable for running large-scale MySQL deployments on Kubernetes or other container orchestration platforms.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

