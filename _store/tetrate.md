---
aid: tetrate
url: https://raw.githubusercontent.com/api-evangelist/tetrate/refs/heads/main/apis.yml
apis:
- aid: tetrate:tsb-platform-api
  name: Tetrate Service Bridge Platform API
  description: The Tetrate Service Bridge (TSB) Platform API provides programmatic management of the TSB control plane, including organizations, tenants, workspaces, and cluster onboarding. It exposes REST and gRPC endpoints for configuring the global service mesh management plane across multi-cluster and multi-cloud environments.
  humanURL: https://docs.tetrate.io/service-bridge/latest/refs/tsb/v2/
  baseURL: https://docs.tetrate.io/
  tags:
  - Management Plane
  - Multi-Cluster
  - REST
  - Service Mesh
  properties:
  - type: Documentation
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/v2/
  - type: Reference
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/v2/
- aid: tetrate:tsb-gateway-api
  name: Tetrate Service Bridge Gateway API
  description: The TSB Gateway API manages ingress and egress gateway configuration for services in a Tetrate Service Bridge environment. It provides resources for defining gateway groups, IngressGateway, EgressGateway, and Tier1Gateway objects that control traffic entering and leaving the mesh across clusters.
  humanURL: https://docs.tetrate.io/service-bridge/latest/refs/tsb/gateway/v2/
  baseURL: https://docs.tetrate.io/
  tags:
  - Egress
  - Gateway
  - Ingress
  - Traffic Management
  properties:
  - type: Documentation
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/gateway/v2/
  - type: Reference
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/gateway/v2/
- aid: tetrate:tsb-traffic-api
  name: Tetrate Service Bridge Traffic API
  description: The TSB Traffic API provides configuration resources for managing service-to-service traffic within a Tetrate Service Bridge workspace. It supports traffic groups, TrafficSetting, and ServiceRoute objects that control load balancing, failover, retries, and routing rules for workloads in the mesh.
  humanURL: https://docs.tetrate.io/service-bridge/latest/refs/tsb/traffic/v2/
  baseURL: https://docs.tetrate.io/
  tags:
  - Load Balancing
  - Routing
  - Service Mesh
  - Traffic Management
  properties:
  - type: Documentation
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/traffic/v2/
  - type: Reference
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/traffic/v2/
- aid: tetrate:tsb-security-api
  name: Tetrate Service Bridge Security API
  description: The TSB Security API provides configuration resources for enforcing security policies in a Tetrate Service Bridge environment. It includes security groups, SecuritySetting, and ServiceSecuritySetting objects for controlling mutual TLS, authorization policies, and access control between workloads across the mesh.
  humanURL: https://docs.tetrate.io/service-bridge/latest/refs/tsb/security/v2/
  baseURL: https://docs.tetrate.io/
  tags:
  - Authorization
  - mTLS
  - Security
  - Service Mesh
  properties:
  - type: Documentation
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/security/v2/
  - type: Reference
    url: https://docs.tetrate.io/service-bridge/latest/refs/tsb/security/v2/
- aid: tetrate:tsb-observability-api
  name: Tetrate Service Bridge Observability API
  description: The TSB Observability API exposes metrics, topology, and service observability data for workloads managed by Tetrate Service Bridge. It provides access to service-level metrics, traffic telemetry, and distributed tracing information collected across mesh clusters, enabling monitoring and troubleshooting of distributed applications.
  humanURL: https://docs.tetrate.io/service-bridge/latest/refs/
  baseURL: https://docs.tetrate.io/
  tags:
  - Metrics
  - Observability
  - Telemetry
  - Tracing
  properties:
  - type: Documentation
    url: https://docs.tetrate.io/service-bridge/latest/refs/
name: Tetrate
tags:
- Enterprise
- Envoy
- Istio
- Kubernetes
- Service Mesh
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Tetrate is an enterprise service mesh company that provides Tetrate Service Bridge (TSB), a multi-cluster, multi-cloud service mesh management platform built on Istio and Envoy Proxy. Tetrate offers management APIs for traffic, security, and observability across distributed microservice environments, as well as Tetrate Istio Distro, a vetted upstream Istio distribution with FIPS-verified builds.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

