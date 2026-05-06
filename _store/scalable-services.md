---
aid: scalable-services
name: Scalable Services
description: A curated topic collection covering APIs, patterns, tools, and best practices for designing and operating scalable services. This includes cloud-native microservices, API gateways, load balancers, container orchestration, serverless platforms, service meshes, and the architectural patterns that enable services to scale horizontally and vertically. Relevant to platform engineers, cloud architects, and backend developers building high-traffic, distributed systems.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Cloud Native
  - Containers
  - Distributed Systems
  - High Availability
  - Kubernetes
  - Load Balancing
  - Microservices
  - Scalable Architecture
  - Serverless
  - Service Mesh
type: Index
created: '2025-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scalable-services:kubernetes
    name: Kubernetes API
    description: The Kubernetes API enables programmatic management of containerized workloads, including deployments, services, pods, config maps, and horizontal pod autoscalers. Core to running scalable microservices infrastructure.
    tags:
      - Containers
      - Kubernetes
      - Orchestration
      - Scalable Architecture
    humanURL: https://kubernetes.io/docs/reference/kubernetes-api/
    properties:
      - type: Documentation
        url: https://kubernetes.io/docs/reference/kubernetes-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
      - type: GettingStarted
        url: https://kubernetes.io/docs/home/
      - type: GitHub
        url: https://github.com/kubernetes/kubernetes
  - aid: scalable-services:envoy-admin
    name: Envoy Admin API
    description: Envoy Proxy's administration API for inspecting and modifying Envoy runtime configuration, stats, clusters, and listeners. Envoy is the foundational data plane for many service mesh and API gateway deployments.
    tags:
      - API Gateway
      - Load Balancing
      - Proxy
      - Service Mesh
    humanURL: https://www.envoyproxy.io/docs/envoy/latest/operations/admin
    properties:
      - type: Documentation
        url: https://www.envoyproxy.io/docs/envoy/latest/operations/admin
      - type: GitHub
        url: https://github.com/envoyproxy/envoy
  - aid: scalable-services:istio
    name: Istio API
    description: Istio's configuration APIs define traffic management, security policy, and observability for microservice meshes. Expressed as Kubernetes CRDs (VirtualService, DestinationRule, Gateway, etc.).
    tags:
      - Kubernetes
      - Microservices
      - Observability
      - Security
      - Service Mesh
    humanURL: https://istio.io/latest/docs/reference/config/
    properties:
      - type: Documentation
        url: https://istio.io/latest/docs/reference/config/
      - type: GitHub
        url: https://github.com/istio/istio
  - aid: scalable-services:aws-lambda
    name: AWS Lambda API
    description: Amazon Web Services Lambda API for creating, managing, invoking, and monitoring serverless functions. Core to event-driven, auto-scaling architectures.
    tags:
      - AWS
      - Cloud Native
      - Event Driven
      - Scalable Architecture
      - Serverless
    humanURL: https://docs.aws.amazon.com/lambda/latest/api/API_Operations.html
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/lambda/latest/api/API_Operations.html
  - aid: scalable-services:kong-admin
    name: Kong Admin API
    description: Kong Gateway's RESTful Admin API for managing services, routes, plugins, consumers, upstreams, and certificates. Kong is a widely deployed open-source API gateway for scalable API management.
    tags:
      - API Gateway
      - Load Balancing
      - Microservices
      - Plugins
    humanURL: https://docs.konghq.com/gateway/latest/admin-api/
    properties:
      - type: Documentation
        url: https://docs.konghq.com/gateway/latest/admin-api/
      - type: GitHub
        url: https://github.com/Kong/kong
  - aid: scalable-services:prometheus
    name: Prometheus HTTP API
    description: Prometheus exposes an HTTP API for querying metrics, metadata, and alerting rules. Essential for observability and autoscaling decisions in scalable service architectures.
    tags:
      - Alerts
      - Metrics
      - Monitoring
      - Observability
    humanURL: https://prometheus.io/docs/prometheus/latest/querying/api/
    properties:
      - type: Documentation
        url: https://prometheus.io/docs/prometheus/latest/querying/api/
      - type: GitHub
        url: https://github.com/prometheus/prometheus
  - aid: scalable-services:knative
    name: Knative API
    description: Knative provides Kubernetes-based platform APIs for deploying and scaling event-driven serverless workloads. Includes Knative Serving (scale-to-zero) and Knative Eventing (event sourcing and routing).
    tags:
      - Cloud Native
      - Event Driven
      - Kubernetes
      - Scalable Architecture
      - Serverless
    humanURL: https://knative.dev/docs/
    properties:
      - type: Documentation
        url: https://knative.dev/docs/
      - type: GitHub
        url: https://github.com/knative/serving
  - aid: scalable-services:grpc
    name: gRPC Reflection API
    description: gRPC server reflection provides information about publicly-accessible gRPC services on a server, enabling discovery and dynamic invocation. gRPC is widely used for high-performance inter-service communication in scalable microservice architectures.
    tags:
      - High Performance
      - Microservices
      - Protocol Buffers
      - RPC
    humanURL: https://grpc.io/docs/
    properties:
      - type: Documentation
        url: https://grpc.io/docs/
      - type: GitHub
        url: https://github.com/grpc/grpc
common:
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/architecture/
    name: Kubernetes Architecture Concepts
  - type: Guide
    url: https://microservices.io/patterns/index.html
    name: Microservices Patterns
  - type: Guide
    url: https://www.cncf.io/projects/
    name: CNCF Landscape Projects
  - type: Guide
    url: https://istio.io/latest/about/service-mesh/
    name: What is a Service Mesh?
  - type: Guide
    url: https://www.envoyproxy.io/learn/service-mesh
    name: Envoy Service Mesh Guide
  - type: JSONSchema
    url: https://github.com/api-evangelist/scalable-services/blob/main/json-schema/scalable-services-service-schema.json
    name: Scalable Service JSON Schema
  - type: JSONStructure
    url: https://github.com/api-evangelist/scalable-services/blob/main/json-structure/scalable-services-service-structure.json
    name: Scalable Service JSON Structure
  - type: JSONLDContext
    url: https://github.com/api-evangelist/scalable-services/blob/main/json-ld/scalable-services-context.jsonld
    name: Scalable Services JSON-LD Context
  - type: Vocabulary
    url: https://github.com/api-evangelist/scalable-services/blob/main/vocabulary/scalable-services-vocabulary.yml
    name: Scalable Services Vocabulary
  - type: Examples
    url: https://github.com/api-evangelist/scalable-services/blob/main/examples/scalable-services-kubernetes-hpa-example.json
    name: Kubernetes HPA Example
  - type: Examples
    url: https://github.com/api-evangelist/scalable-services/blob/main/examples/scalable-services-kong-plugin-example.json
    name: Kong Rate Limiting Plugin Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
