---
aid: cri-o
name: CRI-O
x-type: opensource
description: CRI-O is a CNCF graduated, lightweight container runtime built specifically for Kubernetes. It implements the Kubernetes Container Runtime Interface (CRI) gRPC API and uses any Open Container Initiative (OCI) compatible runtime, including runc and crun, as the underlying container executor. CRI-O integrates with the containers/image and containers/storage libraries, the conmon container monitor, and CNI plugins to deliver a minimal kubelet-facing runtime surface, while also exposing an HTTP status API and Prometheus metrics endpoint for operations and observability.
url: https://raw.githubusercontent.com/api-evangelist/cri-o/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache 2.0
  - CNCF
  - Cloud Native
  - conmon
  - Container Runtime
  - Containers
  - CRI
  - Go
  - Graduated
  - Kubernetes
  - OCI
  - Open Source
  - Prometheus
  - runc
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
type: Index
access: Public
position: Provider
apis:
  - aid: cri-o:cri-o-cri-grpc-api
    name: CRI-O CRI gRPC API
    description: CRI-O implements the Kubernetes Container Runtime Interface (CRI) gRPC API that the kubelet uses to manage pod sandboxes, containers, image lifecycle, and runtime status. The CRI gRPC API is served over a Unix domain socket (default /var/run/crio/crio.sock) and includes services for RuntimeService and ImageService as defined by the upstream CRI protobuf specification.
    humanURL: https://kubernetes.io/docs/concepts/architecture/cri/
    properties:
      - type: Documentation
        url: https://kubernetes.io/docs/concepts/architecture/cri/
      - type: Specification
        url: https://github.com/kubernetes/cri-api
      - type: GitHubRepository
        url: https://github.com/cri-o/cri-o
    tags:
      - CRI
      - gRPC
      - Kubelet
      - Kubernetes
  - aid: cri-o:cri-o-status-api
    name: CRI-O Status API
    description: The CRI-O Status API is an HTTP server exposed by the cri-o daemon for runtime introspection, container inspection, and lifecycle control. It provides /info and /config endpoints for daemon configuration, /containers/{id} for live container inspection, /pause/{id} and /unpause/{id} to control container execution, and /debug endpoints for golang debugging. As noted upstream, this API is not considered stable for production use.
    humanURL: https://github.com/cri-o/cri-o
    baseURL: http://localhost
    properties:
      - type: Documentation
        url: https://github.com/cri-o/cri-o
      - type: OpenAPI
        url: openapi/cri-o-status-openapi.yml
      - type: Rules
        url: rules/cri-o-status-rules.yml
      - type: Capabilities
        url: capabilities/cri-o-status-capabilities.yml
    tags:
      - Debugging
      - HTTP
      - Lifecycle
      - Status
  - aid: cri-o:cri-o-metrics-api
    name: CRI-O Metrics API
    description: The CRI-O metrics endpoint exposes Prometheus-compatible metrics for operation counts, container lifecycle, image pulls, and errors. It is enabled with the --enable-metrics flag and served on the configured port (default 9090) at the /metrics path. The endpoint can also be served over a Unix socket and secured with TLS for cluster-grade observability.
    humanURL: https://github.com/cri-o/cri-o/blob/main/docs/metrics.md
    baseURL: http://localhost:9090
    properties:
      - type: Documentation
        url: https://github.com/cri-o/cri-o/blob/main/docs/metrics.md
      - type: OpenAPI
        url: openapi/cri-o-metrics-openapi.yml
      - type: Rules
        url: rules/cri-o-metrics-rules.yml
      - type: Capabilities
        url: capabilities/cri-o-metrics-capabilities.yml
    tags:
      - Metrics
      - Monitoring
      - Observability
      - Prometheus
common:
  - type: Website
    url: https://cri-o.io/
  - type: Documentation
    url: https://github.com/cri-o/cri-o/tree/main/docs
  - type: GettingStarted
    url: https://github.com/cri-o/cri-o/blob/main/install.md
  - type: GitHubOrganization
    url: https://github.com/cri-o
  - type: GitHubRepository
    url: https://github.com/cri-o/cri-o
  - type: Blog
    url: https://cri-o.io/#blog
  - type: ChangeLog
    url: https://github.com/cri-o/cri-o/releases
  - type: Community
    url: https://github.com/cri-o/cri-o#getting-started
  - type: License
    url: https://github.com/cri-o/cri-o/blob/main/LICENSE
  - type: CNCF
    url: https://www.cncf.io/projects/cri-o/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
