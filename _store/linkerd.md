---
aid: linkerd
name: Linkerd
description: Service mesh without the mess. Linkerd adds security, observability, and reliability to any Kubernetes cluster without the complexity of bloat of other meshes.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Kubernetes
  - mTLS
  - Observability
  - Security
  - Service Mesh
created: '2025-08-19'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/linkerd/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: linkerd:proxy-admin-api
    name: Linkerd Proxy Admin API
    description: The Linkerd proxy exposes an admin HTTP server on each meshed pod, providing health check endpoints, readiness probes, Prometheus-compatible metrics, and runtime diagnostic information. By default this server listens on port 4191.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://linkerd.io/2-edge/reference/proxy-configuration/
    baseURL: http://localhost:4191
    properties:
      - type: Documentation
        url: https://linkerd.io/2-edge/reference/proxy-configuration/
      - type: Reference
        url: https://linkerd.io/2-edge/reference/proxy-metrics/
      - type: OpenAPI
        url: openapi/linkerd-proxy-admin-openapi.yml
    tags:
      - Health Check
      - Metrics
      - Prometheus
      - Proxy
  - aid: linkerd:viz-metrics-api
    name: Linkerd Viz Metrics API
    description: The Linkerd Viz extension provides a metrics API that powers the linkerd viz CLI commands and the Linkerd dashboard. It queries Prometheus for golden metrics including request volume, success rate, and latency distributions for HTTP, HTTP/2, and gRPC traffic across meshed workloads.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://linkerd.io/2-edge/reference/cli/viz/
    properties:
      - type: Documentation
        url: https://linkerd.io/2-edge/reference/cli/viz/
      - type: OpenAPI
        url: openapi/linkerd-viz-metrics-openapi.yml
      - type: JSONSchema
        url: json-schema/stat-summary.json
      - type: JSONSchema
        url: json-schema/edge.json
      - type: JSONSchema
        url: json-schema/gateway.json
      - type: JSONLD
        url: json-ld/linkerd-context.jsonld
    tags:
      - Dashboard
      - Metrics
      - Observability
      - Statistics
  - aid: linkerd:tap-api
    name: Linkerd Tap API
    description: The Linkerd Tap API is a Kubernetes aggregated API server that provides real-time streaming access to requests flowing through the Linkerd service mesh. It allows live inspection of HTTP and gRPC traffic including headers, paths, response codes, and latency. Access is controlled via Kubernetes RBAC.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://linkerd.io/2-edge/reference/cli/viz/
    properties:
      - type: Documentation
        url: https://linkerd.io/2-edge/reference/cli/viz/
      - type: OpenAPI
        url: openapi/linkerd-tap-openapi.yml
      - type: JSONSchema
        url: json-schema/tap-event.json
      - type: JSONLD
        url: json-ld/linkerd-context.jsonld
    tags:
      - Debugging
      - Real-Time
      - Tap
      - Traffic Inspection
  - aid: linkerd:proxy-control-plane-api
    name: Linkerd Proxy Control Plane API
    description: The Linkerd Proxy Control Plane gRPC API defines the protobuf service contracts used by the data-plane proxy to communicate with the control plane. It includes the Destination API for service discovery and traffic policy, the Identity API for issuing mTLS certificates, and the Inbound API for per-port authorization and rate-limiting policies.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/linkerd/linkerd2-proxy-api
    tags:
      - Control Plane
      - gRPC
      - mTLS
      - Policy
    properties:
      - type: Documentation
        url: https://github.com/linkerd/linkerd2-proxy-api
      - type: Reference
        url: https://linkerd.io/2-edge/reference/authorization-policy/
      - type: GitHubRepository
        url: https://github.com/linkerd/linkerd2-proxy-api
      - type: JSONSchema
        url: json-schema/service-profile.json
  - aid: linkerd:multicluster-api
    name: Linkerd Multicluster API
    description: The Linkerd Multicluster extension provides Kubernetes CRDs and a gateway component that enables transparent, secure cross-cluster service communication. It uses mTLS to authenticate workloads across cluster boundaries within a unified trust domain, allowing services in different clusters to communicate as if they were local.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://linkerd.io/2-edge/features/multicluster/
    properties:
      - type: Documentation
        url: https://linkerd.io/2-edge/features/multicluster/
      - type: Reference
        url: https://linkerd.io/2-edge/reference/multicluster/
    tags:
      - Federation
      - Kubernetes
      - mTLS
      - Multicluster
common:
  - type: JSON-LD
    url: json-ld/linkerd-context.jsonld
  - type: JSONSchema
    url: json-schema/service-profile.json
  - type: Website
    url: https://linkerd.io/
  - type: Documentation
    url: https://linkerd.io/2.19/reference/
  - type: Getting Started
    url: https://linkerd.io/2.19/getting-started/
  - type: GitHub Organization
    url: https://github.com/linkerd
  - type: GitHubRepository
    url: https://github.com/linkerd/linkerd2
  - type: Blog
    url: https://linkerd.io/blog/
  - type: Change Log
    url: https://github.com/linkerd/linkerd2/blob/main/CHANGES.md
  - type: Community
    url: https://linkerd.io/community/get-involved/
  - type: Slack
    url: https://slack.linkerd.io/
  - type: Support
    url: https://linkerd.buoyant.io/
  - type: Releases
    url: https://github.com/linkerd/linkerd2/releases
  - type: Security
    url: https://github.com/linkerd/linkerd2/blob/main/SECURITY.md
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/linkerd
  - type: YouTube
    url: https://www.youtube.com/@Linkerd
  - type: Privacy Policy
    url: https://buoyant.io/privacy-policy
  - type: Terms of Service
    url: https://buoyant.io/terms-of-service
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
