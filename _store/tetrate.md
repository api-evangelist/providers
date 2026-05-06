---
aid: tetrate
name: Tetrate
description: Tetrate is an enterprise service mesh company that provides Tetrate Service Bridge (TSB), a multi-cluster, multi-cloud service mesh management platform built on Istio and Envoy Proxy. Tetrate offers management APIs for traffic, security, and observability across distributed microservice environments, as well as Tetrate Istio Distro (TID), a vetted upstream Istio distribution with FIPS-verified builds. TSB exposes a REST management plane API for programmatic control of organizations, tenants, workspaces, clusters, applications, gateways, traffic routing, and security policies.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise
  - Envoy
  - Istio
  - Kubernetes
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/tetrate/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tetrate:tsb-rest-api
    name: Tetrate Service Bridge REST API
    description: The Tetrate Service Bridge (TSB) REST API provides programmatic management of the TSB control plane, including organizations, tenants, workspaces, cluster onboarding, application and API lifecycle management, gateway groups, traffic settings, and security policies. Authentication supports HTTP Basic and JWT token via x-tetrate-token header. The API base path is /v2 on port 8443.
    humanURL: https://docs.tetrate.io/service-bridge/reference/rest-api/guide
    baseURL: https://tsbhost:8443/v2
    tags:
      - Management Plane
      - Multi-Cluster
      - REST
      - Service Mesh
    properties:
      - type: Documentation
        url: https://docs.tetrate.io/service-bridge/reference/rest-api/guide
      - type: OpenAPI
        url: openapi/tetrate-service-bridge-openapi.yml
      - type: JSONSchema
        url: json-schema/tsb-resource-schema.json
      - type: JSONStructure
        url: json-structure/tsb-resource-structure.json
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
common:
  - type: Website
    url: https://tetrate.io/
  - type: Documentation
    url: https://docs.tetrate.io/
  - type: Getting Started
    url: https://docs.tetrate.io/service-bridge/latest/quickstart/
  - type: Blog
    url: https://tetrate.io/blog/
  - type: GitHub Organization
    url: https://github.com/tetrateio
  - type: GitHubRepository
    url: https://github.com/tetrateio/tetrate
  - type: Change Log
    url: https://docs.tetrate.io/service-bridge/latest/release-notes/
  - type: Support
    url: https://tetrate.io/contact/
  - type: Pricing
    url: https://tetrate.io/tetrate-service-bridge/
  - type: Community
    url: https://tetrate.io/community/
  - type: OpenAPI
    url: openapi/tetrate-service-bridge-openapi.yml
  - type: JSONSchema
    url: json-schema/tsb-resource-schema.json
  - type: JSONStructure
    url: json-structure/tsb-resource-structure.json
  - type: JSON-LD
    url: json-ld/tetrate-context.jsonld
  - type: Vocabulary
    url: vocabulary/tetrate-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
