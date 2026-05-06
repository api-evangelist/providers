---
aid: ambient-mesh
name: Ambient Mesh
description: Ambient Mesh is a sidecar-less service mesh architecture built on Istio that simplifies microservices communication, enhances zero-trust security, and improves observability without requiring sidecar proxy injection. It uses a shared per-node proxy (ztunnel) for zero-trust security and optional waypoint proxies for advanced Layer 7 policies, enabling seamless migration from sidecar-based meshes with zero downtime.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Service Mesh
  - Istio
  - Kubernetes
  - Zero Trust
  - Observability
  - Traffic Management
  - Microservices
url: https://raw.githubusercontent.com/api-evangelist/ambient-mesh/refs/heads/main/apis.yml
created: '2026-04-19'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: ambient-mesh:ambient-mesh
    name: Ambient Mesh
    description: Ambient Mesh provides a sidecar-less service mesh via the Kubernetes Gateway API and Istio ambient mode. It exposes configuration APIs for traffic management, security policies, resilience settings, and observability through standard Kubernetes CRDs including HTTPRoute, Gateway, AuthorizationPolicy, and WaypointProxy resources.
    humanURL: https://ambientmesh.io/
    baseURL: https://ambientmesh.io
    tags:
      - Service Mesh
      - Kubernetes
      - Istio
      - Zero Trust
    properties:
      - type: Documentation
        url: https://ambientmesh.io/docs/
      - type: GettingStarted
        url: https://ambientmesh.io/docs/quickstart/
      - type: APIReference
        url: https://ambientmesh.io/docs/
common:
  - type: Website
    url: https://ambientmesh.io/
  - type: Documentation
    url: https://ambientmesh.io/docs/
  - type: GettingStarted
    url: https://ambientmesh.io/docs/quickstart/
  - type: Blog
    url: https://ambientmesh.io/blog/
  - type: GitHubOrganization
    url: https://github.com/istio
  - type: GitHubRepository
    url: https://github.com/istio/istio
  - type: Features
    data:
      - name: Sidecar-Less Architecture
        description: Operates at the platform layer without sidecar proxy injection, reducing resource overhead and operational complexity while maintaining full service mesh capabilities.
      - name: Zero-Trust Security
        description: SPIFFE-based workload identity with automatic mutual TLS encryption between workloads, certificate management, and zero-trust network policies enforced by ztunnel.
      - name: Traffic Management
        description: Advanced traffic routing, load balancing, traffic splitting, mirroring, blue-green deployments, and gateway management via Kubernetes Gateway API HTTPRoute resources.
      - name: Resilience
        description: Zone-aware load balancing, circuit breaking, outlier detection, fault injection, timeouts, and retry budgets for high-availability workloads.
      - name: Observability
        description: Distributed tracing, performance metrics via Prometheus, Kiali observability console, and HTTP observability for traffic visualization and security verification.
      - name: Zero-Downtime Migration
        description: Free migration tooling for upgrading from sidecar-based architectures with automated workload analysis and risk mitigation for waypoint proxy requirements.
      - name: Waypoint Proxies
        description: Optional per-namespace or per-workload Layer 7 proxies that provide advanced policy enforcement without requiring per-pod sidecar containers.
  - type: UseCases
    data:
      - name: Microservices Security
        description: Enforce mutual TLS and zero-trust policies across microservices without modifying application code or injecting sidecar proxies.
      - name: Traffic Management
        description: Implement advanced traffic routing, A/B testing, canary deployments, and traffic mirroring across Kubernetes workloads.
      - name: Istio Migration
        description: Migrate existing Istio sidecar-based deployments to ambient mode with zero downtime using the free migration tooling.
      - name: Kubernetes Observability
        description: Gain full visibility into service-to-service communication with metrics, tracing, and traffic visualization via Kiali and Prometheus.
      - name: Multi-Cluster Networking
        description: Extend ambient mesh policies and security across multiple Kubernetes clusters for hybrid and multi-cloud architectures.
  - type: Integrations
    data:
      - name: Istio
        description: Ambient Mesh is built on Istio ambient mode, using its control plane and CRDs for configuration.
      - name: Kubernetes Gateway API
        description: Uses the standard Kubernetes Gateway API with HTTPRoute, Gateway, and GRPCRoute resources for traffic management.
      - name: Prometheus
        description: Integrates with Prometheus for metrics collection and monitoring of mesh traffic and performance.
      - name: Kiali
        description: Integrates with Kiali for service mesh observability, traffic visualization, and security verification.
      - name: Gloo Mesh
        description: Solo.io's Gloo Mesh provides enterprise-grade ambient mesh management for scaling across enterprise workloads.
      - name: OpenShift
        description: Red Hat OpenShift Service Mesh 3.x supports Istio ambient mode for OpenShift deployments.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
