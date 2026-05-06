---
aid: bfe
name: BFE
description: BFE (Beyond Front End) is an open-source layer 7 load balancer developed by Baidu, providing advanced traffic routing, forwarding, and load balancing capabilities with support for HTTP, HTTPS, HTTP/2, WebSocket, TLS, and gRPC. BFE is a CNCF sandbox project licensed under Apache 2.0.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Load Balancer
  - Networking
  - Open Source
  - Traffic Management
  - CNCF
  - Baidu
url: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: bfe:bfe-management-api
    name: BFE Management API
    description: The BFE Management API provides internal monitoring metrics, configuration reload, and Go pprof profiling endpoints. This API should only be exposed on internal networks.
    humanURL: https://www.bfe-networks.net/en_us/operation/api/
    baseURL: http://localhost:8421
    tags:
      - Management
      - Monitoring
      - Configuration
      - Observability
    properties:
      - type: Documentation
        url: https://www.bfe-networks.net/en_us/operation/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/openapi/bfe-management-api.yaml
common:
  - type: Portal
    url: https://www.bfe-networks.net/en_us/
  - type: Documentation
    url: https://www.bfe-networks.net/en_us/
  - type: GitHubOrganization
    url: https://github.com/bfenetworks
  - type: GitHubRepository
    url: https://github.com/bfenetworks/bfe
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/vocabulary/bfe-vocabulary.yaml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/rules/bfe-spectral-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/bfe/refs/heads/main/capabilities/load-balancer-management.yaml
  - type: Features
    data:
      - name: Layer 7 Load Balancing
        description: Advanced HTTP/HTTPS/HTTP2 load balancing with pluggable algorithms.
      - name: Plugin Framework
        description: Extensible plugin system enabling custom traffic management logic.
      - name: Multi-tenancy
        description: Isolated configuration and routing per tenant.
      - name: Advanced Routing
        description: DSL-based routing rules for fine-grained traffic control.
      - name: Protocol Support
        description: HTTP, HTTPS, SPDY, HTTP/2, gRPC, WebSocket, TLS, FastCGI protocols.
      - name: Observability
        description: Built-in metrics, logging, and distributed tracing integration.
      - name: Dynamic Configuration
        description: Hot reload of routing and load balancing configuration without restart.
      - name: CNCF Sandbox
        description: Hosted as a CNCF sandbox project with active community governance.
  - type: UseCases
    data:
      - name: Enterprise API Gateway
        description: Route and load balance API traffic with per-tenant isolation.
      - name: Microservices Traffic Management
        description: Manage east-west and north-south traffic in microservices architectures.
      - name: TLS Termination
        description: Terminate TLS/HTTPS at the edge and forward to backend HTTP services.
      - name: A/B Testing
        description: Route fractions of traffic to canary deployments using routing rules.
      - name: DDoS Mitigation
        description: Use traffic management plugins to detect and mitigate DDoS attacks.
  - type: Integrations
    data:
      - name: Prometheus
        description: Export metrics to Prometheus for monitoring and alerting.
      - name: Kubernetes
        description: Deploy BFE as an ingress controller in Kubernetes clusters.
      - name: Docker
        description: Run BFE in Docker containers for containerized deployments.
      - name: Grafana
        description: Visualize BFE metrics in Grafana dashboards.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
