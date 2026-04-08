---
aid: etcd
url: https://raw.githubusercontent.com/api-evangelist/etcd/refs/heads/main/apis.yml
apis:
- aid: etcd:etcd-grpc-api
  name: etcd gRPC API
  description: The etcd v3 API is a gRPC-based interface providing key-value operations (put, get, delete, range), watch streams for change notifications, lease management for TTL-based keys, cluster membership management, maintenance operations including snapshots and defragmentation, and authentication and authorization controls.
  humanURL: https://etcd.io/docs/v3.5/learning/api/
  properties:
  - type: Documentation
    url: https://etcd.io/docs/v3.5/learning/api/
  - type: Reference
    url: https://etcd.io/docs/v3.5/learning/api_guarantees/
  - type: Authentication
    url: https://etcd.io/docs/v3.5/op-guide/authentication/
  - type: Getting Started
    url: https://etcd.io/docs/v3.5/dev-guide/interacting_v3/
  - type: Client Libraries
    url: https://etcd.io/docs/v3.5/integrations/
  tags:
  - Cluster Management
  - gRPC
  - Key-Value
  - Lease
  - Watch
- aid: etcd:etcd-http-api
  name: etcd HTTP Gateway API
  description: etcd provides an HTTP/JSON gateway that translates HTTP requests into gRPC calls, allowing clients without gRPC support to interact with etcd. The gateway supports the same operations as the gRPC API including key-value operations, watches, and cluster management through a RESTful interface.
  humanURL: https://etcd.io/docs/v3.5/dev-guide/api_grpc_gateway/
  properties:
  - type: Documentation
    url: https://etcd.io/docs/v3.5/dev-guide/api_grpc_gateway/
  - type: Reference
    url: https://etcd.io/docs/v3.5/dev-guide/api_grpc_gateway/
  - type: OpenAPI
    url: openapi/etcd-http-gateway-openapi.yml
  tags:
  - Gateway
  - gRPC
  - HTTP
  - REST
- aid: etcd:etcd-concurrency-api
  name: etcd Concurrency API
  description: The etcd concurrency API provides distributed primitives built on top of the core key-value store, including distributed mutexes (locks), leader election, and software transactional memory (STM). These primitives are used to coordinate between distributed processes and implement consensus patterns in clustered applications.
  humanURL: https://etcd.io/docs/v3.5/dev-guide/api_concurrency_reference_v3/
  properties:
  - type: Documentation
    url: https://etcd.io/docs/v3.5/dev-guide/api_concurrency_reference_v3/
  - type: Reference
    url: https://etcd.io/docs/v3.5/dev-guide/api_concurrency_reference_v3/
  tags:
  - Concurrency
  - Coordination
  - Distributed Locking
  - Leader Election
- aid: etcd:etcd-metrics-api
  name: etcd Metrics API
  description: etcd exposes a Prometheus-compatible metrics endpoint that provides operational insights into the etcd cluster, including request rates, latency histograms, disk I/O statistics, Raft state, and cluster health indicators. This endpoint is used for monitoring and alerting in production etcd deployments.
  humanURL: https://etcd.io/docs/v3.5/op-guide/monitoring/
  properties:
  - type: Documentation
    url: https://etcd.io/docs/v3.5/op-guide/monitoring/
  - type: Reference
    url: https://etcd.io/docs/v3.5/metrics/
  tags:
  - Metrics
  - Monitoring
  - Observability
  - Prometheus
- aid: etcd:etcd-v2-api
  name: etcd v2 HTTP API
  description: The original etcd v2 API exposed a RESTful HTTP interface for key-value operations using a hierarchical directory structure. This API has been deprecated in favor of the v3 gRPC API and was removed from the default etcd build in later versions. Existing users should migrate to the v3 API.
  humanURL: https://etcd.io/docs/v2.3/api/
  properties:
  - type: Documentation
    url: https://etcd.io/docs/v2.3/api/
  - type: Deprecation Notice
    url: https://etcd.io/docs/v3.5/op-guide/v2-migration/
  - type: Migration Guide
    url: https://etcd.io/docs/v3.5/op-guide/v2-migration/
  tags:
  - Deprecated
  - HTTP
  - Key-Value
  - REST
name: Etcd
tags:
- Cloud Native
- Consensus
- Distributed Systems
- Graduated
- Key-Value Store
- Kubernetes
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: etcd is a CNCF graduated distributed, reliable key-value store used as the backing store for all Kubernetes cluster data. It provides strong consistency guarantees using the Raft consensus algorithm, supporting watch operations, lease-based TTLs, and atomic compare-and-swap transactions. etcd is designed for high availability and stores critical configuration data for distributed systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

