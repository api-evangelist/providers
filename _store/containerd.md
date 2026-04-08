---
aid: containerd
url: https://raw.githubusercontent.com/api-evangelist/containerd/refs/heads/main/apis.yml
apis:
- aid: containerd:containerd-grpc-api
  name: Containerd gRPC API
  description: Core gRPC API for managing the full container lifecycle including containers, images, content, snapshots, namespaces, tasks, leases, events, and plugins. Provides low-level access to all containerd functionality through Protocol Buffers service definitions.
  humanURL: https://github.com/containerd/containerd/tree/main/api
  properties:
  - type: Documentation
    url: https://containerd.io/docs/
  - type: Reference
    url: https://github.com/containerd/containerd/tree/main/api
  - type: JSONSchema
    url: json-schema/containerd-config-schema.json
  - type: JSONSchema
    url: json-schema/containerd-oci-runtime-spec-schema.json
  tags:
  - Container Runtime
  - gRPC
  - Lifecycle Management
- aid: containerd:containerd-cri-api
  name: Containerd CRI API
  description: Container Runtime Interface (CRI) implementation that enables Kubernetes to use containerd as its container runtime. Supports pod sandbox management, container lifecycle operations, image pulling, and streaming APIs for exec, attach, and port-forward.
  humanURL: https://github.com/containerd/containerd/tree/main/pkg/cri
  properties:
  - type: Documentation
    url: https://containerd.io/docs/
  - type: Reference
    url: https://github.com/containerd/containerd/tree/main/pkg/cri
  - type: JSONSchema
    url: json-schema/containerd-config-schema.json
  tags:
  - Container Runtime
  - CRI
  - Kubernetes
- aid: containerd:containerd-metrics-api
  name: Containerd Metrics API
  description: The containerd metrics plugin exposes a Prometheus-compatible HTTP endpoint for scraping runtime metrics. When enabled via the metrics.address configuration option in config.toml, it serves Prometheus text format metrics covering gRPC request counts, latency histograms, snapshot usage, content store statistics, and task lifecycle events.
  humanURL: https://containerd.io/docs/
  properties:
  - type: Documentation
    url: https://containerd.io/docs/
  - type: OpenAPI
    url: openapi/containerd-metrics-openapi.yml
  tags:
  - Metrics
  - Observability
  - Prometheus
- aid: containerd:containerd-nri-api
  name: Containerd NRI API
  description: The Node Resource Interface (NRI) is a framework for plugging extensions into OCI-compatible container runtimes. NRI plugins receive lifecycle event notifications and can make controlled modifications to container configurations before creation, enabling domain-specific resource management without modifying the runtime itself.
  humanURL: https://github.com/containerd/nri
  properties:
  - type: Documentation
    url: https://github.com/containerd/containerd/blob/main/docs/NRI.md
  - type: GitHubRepository
    url: https://github.com/containerd/nri
  tags:
  - Extensibility
  - Kubernetes
  - NRI
  - Plugins
name: Containerd
tags:
- Cloud Native
- Container Runtime
- CRI
- Docker
- gRPC
- Kubernetes
- OCI
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: An industry-standard container runtime with an emphasis on simplicity, robustness and portability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

