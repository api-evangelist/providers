---
aid: apache-dubbo
name: Apache Dubbo
description: Apache Dubbo is a high-performance, Java-based open-source RPC framework that provides service discovery, traffic management, and observability capabilities for building enterprise-level microservices. It supports multiple protocols including Triple (gRPC-compatible), Dubbo, and REST, with SDKs for Java, Go, Node.js, Python, Rust, and Erlang.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Go
  - Java
  - Microservices
  - Open Source
  - RPC
  - Service Discovery
  - Service Mesh
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-dubbo/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-dubbo:apache-dubbo-admin
    name: Apache Dubbo Admin API
    description: The Dubbo Admin REST API provides service governance operations for managing services, instances, traffic rules, load balancing, route policies, and dynamic configuration in a Dubbo microservices cluster.
    humanURL: https://github.com/apache/dubbo-admin
    tags:
      - Admin
      - Governance
      - REST
      - Service Management
    properties:
      - type: Documentation
        url: https://dubbo.apache.org/en/overview/reference/admin/
      - type: OpenAPI
        url: openapi/apache-dubbo-admin-openapi-original.json
      - type: GitHubRepository
        url: https://github.com/apache/dubbo-admin
  - aid: apache-dubbo:apache-dubbo-java
    name: Apache Dubbo Java SDK
    description: The core Apache Dubbo Java framework providing RPC service definition, publishing, invocation, and service governance APIs for building enterprise microservices in Java and Spring Boot.
    humanURL: https://dubbo.apache.org/en/overview/mannual/java-sdk/
    tags:
      - Java
      - RPC
      - SDK
      - Spring Boot
    properties:
      - type: Documentation
        url: https://dubbo.apache.org/en/overview/mannual/java-sdk/
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.dubbo/dubbo
        title: Java SDK (Maven Central)
      - type: GitHubRepository
        url: https://github.com/apache/dubbo
  - aid: apache-dubbo:apache-dubbo-go
    name: Apache Dubbo Go SDK
    description: The Go implementation of Apache Dubbo, providing the same RPC framework capabilities including service discovery, traffic management, and Triple protocol support for Go-based microservices.
    humanURL: https://dubbo.apache.org/en/overview/mannual/golang-sdk/
    tags:
      - Go
      - Golang
      - RPC
      - SDK
    properties:
      - type: Documentation
        url: https://dubbo.apache.org/en/overview/mannual/golang-sdk/
      - type: GitHubRepository
        url: https://github.com/apache/dubbo-go
common:
  - type: GitHubOrganization
    url: https://github.com/apache
    title: Apache GitHub Organization
  - type: GitHubRepository
    url: https://github.com/apache/dubbo
    title: Apache Dubbo Java (Main Repo)
  - type: GitHubRepository
    url: https://github.com/apache/dubbo-go
    title: Apache Dubbo Go
  - type: GitHubRepository
    url: https://github.com/apache/dubbo-admin
    title: Apache Dubbo Admin
  - type: GitHubRepository
    url: https://github.com/apache/dubbo-kubernetes
    title: Apache Dubbo Kubernetes
  - type: Documentation
    url: https://dubbo.apache.org/en/overview/
  - type: GettingStarted
    url: https://dubbo.apache.org/en/overview/quickstart/
  - type: Blog
    url: https://dubbo.apache.org/en/blog/
  - type: ReleaseNotes
    url: https://github.com/apache/dubbo/releases
  - type: SpectralRules
    url: rules/apache-dubbo-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-dubbo-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/dubbo-service-governance.yaml
  - type: Features
    data:
      - name: Triple Protocol (gRPC Compatible)
        description: HTTP/2-based RPC protocol fully compatible with gRPC, supporting streaming communication and cross-language interoperability.
      - name: Service Discovery
        description: High-performance application-level service discovery supporting Nacos, Zookeeper, Kubernetes, Consul, Etcd, and Redis registries.
      - name: Traffic Management
        description: Advanced traffic control with conditional routing, tag routing, gray releases, and percentage-based traffic splitting.
      - name: Load Balancing
        description: Multiple load balancing strategies including weighted random, round-robin, least active, and consistent hashing.
      - name: Rate Limiting and Circuit Breaking
        description: Built-in rate limiting, circuit breaker, and service degradation capabilities for resilient microservices.
      - name: Observability
        description: Full-link tracing via OpenTelemetry, Prometheus metrics, Grafana dashboards, Zipkin, and SkyWalking integration.
      - name: Multi-Language SDK Support
        description: Official SDKs for Java, Go, Node.js, Python, Rust, and Erlang enabling polyglot microservices architectures.
      - name: Service Mesh Integration
        description: Native Istio integration with xDS protocol support for deploying Dubbo services in service mesh environments.
      - name: Dubbo Admin Console
        description: Visual cluster management UI for service governance, traffic rules, configuration, and monitoring.
      - name: Pixiu Gateway
        description: HTTP/gRPC gateway (Pixiu) enabling REST HTTP clients to access Dubbo backend services.
  - type: UseCases
    data:
      - name: Enterprise Microservices
        description: Build high-performance Java or Go microservices with RPC communication, service discovery, and traffic governance.
      - name: gRPC Migration
        description: Adopt the Triple protocol as a drop-in gRPC-compatible alternative with richer governance capabilities.
      - name: Cross-Language Service Communication
        description: Enable polyglot microservices with Java, Go, Node.js, Python, Rust, and Erlang services communicating via Dubbo protocols.
      - name: Service Mesh Deployment
        description: Run Dubbo services in Istio-managed service meshes using xDS protocol for sidecar-free or sidecar-based deployments.
      - name: Cloud-Native Kubernetes Deployment
        description: Deploy and manage Dubbo services on Kubernetes using the Dubbo Kubernetes operator and control plane.
      - name: API Gateway Integration
        description: Expose internal Dubbo RPC services as REST HTTP endpoints through the Pixiu API gateway.
  - type: Integrations
    data:
      - name: Nacos
        description: Service registry and configuration center integration for service discovery and dynamic configuration.
      - name: Zookeeper
        description: Apache Zookeeper integration for service registry and coordination.
      - name: Kubernetes
        description: Native Kubernetes service discovery and deployment orchestration support.
      - name: Istio
        description: Service mesh integration with Istio using xDS protocol for traffic management.
      - name: Prometheus
        description: Metrics export to Prometheus for monitoring Dubbo service performance.
      - name: Grafana
        description: Pre-built Grafana dashboards for visualizing Dubbo service metrics.
      - name: OpenTelemetry
        description: Distributed tracing via OpenTelemetry standard for end-to-end request tracking.
      - name: Zipkin
        description: Distributed tracing integration with Zipkin for request flow visualization.
      - name: SkyWalking
        description: Apache SkyWalking APM integration for distributed tracing and service performance monitoring.
      - name: Seata
        description: Apache Seata integration for distributed transaction management across Dubbo services.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
