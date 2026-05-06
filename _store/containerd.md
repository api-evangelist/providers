---
aid: containerd
name: Containerd
description: An industry-standard container runtime with an emphasis on simplicity, robustness and portability.
url: https://containerd.io/
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Container Runtime
  - CRI
  - Docker
  - gRPC
  - Kubernetes
  - OCI
created: '2025-01-01'
modified: '2026-03-18'
specificationVersion: '0.19'
type: Index
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
common:
  - type: Website
    url: https://containerd.io/
  - type: Documentation
    url: https://containerd.io/docs/
  - type: Getting Started
    url: https://containerd.io/docs/getting-started/
  - type: GitHub Organization
    url: https://github.com/containerd
  - type: GitHubRepository
    url: https://github.com/containerd/containerd
  - type: Change Log
    url: https://github.com/containerd/containerd/releases
  - type: Community
    url: https://cloud-native.slack.com/
  - type: CNCF Project
    url: https://www.cncf.io/projects/containerd/
  - type: License
    url: https://github.com/containerd/containerd/blob/main/LICENSE
  - type: JSON-LD
    url: json-ld/containerd-context.jsonld
  - type: JSONSchema
    url: json-schema/containerd-config-schema.json
  - type: JSONSchema
    url: json-schema/containerd-oci-runtime-spec-schema.json
  - type: Spectral
    url: rules/containerd-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/containerd-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
x-type: opensource
---
