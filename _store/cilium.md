---
aid: cilium
url: https://raw.githubusercontent.com/api-evangelist/cilium/refs/heads/main/apis.yml
apis:
- aid: cilium:cilium-api
  name: Cilium API
  tags:
  - eBPF
  - Kubernetes
  - Networking
  - Security
  humanURL: https://docs.cilium.io/en/stable/api/
  baseURL: https://localhost/v1
  properties:
  - url: https://docs.cilium.io/en/stable/api/
    type: Documentation
  - url: https://github.com/cilium/cilium/blob/main/api/v1/openapi.yaml
    type: OpenAPI
  - url: openapi/cilium-api-openapi.yml
    type: OpenAPI
  - url: https://docs.cilium.io/en/stable/gettingstarted/
    type: Getting Started
  - url: https://github.com/cilium/cilium/releases
    type: Change Log
  description: The Cilium REST API provides access to Cilium daemon and agent endpoints for managing Kubernetes network policy, security, and connectivity. The API is served by the cilium-agent process over a local Unix domain socket and HTTP interface, and covers endpoints, identities, cluster nodes, and health status.
- aid: cilium:hubble-api
  name: Hubble API
  tags:
  - eBPF
  - Kubernetes
  - Networking
  - Observability
  humanURL: https://docs.cilium.io/en/stable/observability/hubble/index.html
  properties:
  - url: https://docs.cilium.io/en/stable/observability/hubble/index.html
    type: Documentation
  - url: https://docs.cilium.io/en/stable/internals/hubble/
    type: Reference
  - url: asyncapi/cilium-hubble-asyncapi.yml
    type: AsyncAPI
  - url: https://github.com/cilium/hubble
    type: GitHubRepository
  - url: https://github.com/cilium/hubble/releases
    type: Change Log
  description: The Hubble API is a gRPC-based observability API built on top of Cilium and eBPF that provides deep visibility into network flows, DNS queries, HTTP requests, and service communication within Kubernetes clusters. It exposes Observer and Peer gRPC services for querying flows, nodes, namespaces, and server status across single nodes or entire clusters via Hubble Relay.
- aid: cilium:tetragon-api
  name: Tetragon API
  tags:
  - eBPF
  - Kubernetes
  - Observability
  - Security
  humanURL: https://tetragon.io/docs/reference/grpc-api/
  properties:
  - url: https://tetragon.io/docs/reference/grpc-api/
    type: Documentation
  - url: https://tetragon.io/docs/
    type: Reference
  - url: https://github.com/cilium/tetragon
    type: GitHubRepository
  - url: https://tetragon.io/docs/getting-started/
    type: Getting Started
  - url: https://github.com/cilium/tetragon/releases
    type: Change Log
  description: The Tetragon gRPC API provides access to eBPF-based security observability and runtime enforcement capabilities. It enables querying of kernel-level events including process execution, file access, and network activity, and supports defining tracing policies via Kubernetes custom resources for real-time enforcement and event streaming.
- aid: cilium:cilium-operator-api
  name: Cilium Operator API
  tags:
  - eBPF
  - Kubernetes
  - Networking
  - Operations
  humanURL: https://docs.cilium.io/en/stable/internals/
  baseURL: https://localhost/v1
  properties:
  - url: https://docs.cilium.io/en/stable/internals/
    type: Documentation
  - url: https://github.com/cilium/cilium/blob/main/api/v1/operator/openapi.yaml
    type: OpenAPI
  - url: https://github.com/cilium/cilium/releases
    type: Change Log
  description: The Cilium Operator API provides a REST interface for the Cilium operator component, which handles cluster-wide tasks such as garbage collection of Cilium endpoints and identities, node IPAM management, and coordination of cluster mesh operations. It exposes health and status endpoints for operator lifecycle management in Kubernetes deployments.
- aid: cilium:hubble-relay-api
  name: Hubble Relay API
  tags:
  - gRPC
  - Kubernetes
  - Networking
  - Observability
  humanURL: https://docs.cilium.io/en/stable/observability/hubble/index.html
  properties:
  - url: https://docs.cilium.io/en/stable/observability/hubble/index.html
    type: Documentation
  - url: https://github.com/cilium/cilium/tree/main/api/v1/relay
    type: Reference
  - url: https://github.com/cilium/cilium
    type: GitHubRepository
  - url: https://github.com/cilium/cilium/releases
    type: Change Log
  description: The Hubble Relay API is a gRPC service that aggregates and relays network flow data from multiple Hubble agents running across Kubernetes cluster nodes. It provides a single cluster-wide endpoint for the Hubble Observer service, enabling centralized queries of flow data, DNS events, and HTTP metrics from all nodes through Hubble Relay without connecting to each node individually.
name: Cilium
tags:
- Cloud Native
- eBPF
- Kubernetes
- Networking
- Security
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Cilium is an open source, cloud native solution for providing, securing, and observing network connectivity between workloads, fueled by the revolutionary kernel technology eBPF. Cilium provides network security, load balancing, and observability for Kubernetes clusters.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

