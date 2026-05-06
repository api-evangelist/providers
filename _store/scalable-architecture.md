---
name: Scalable Architecture
description: A subject-matter collection covering APIs, patterns, tools, and frameworks for building scalable system architecture. This topic encompasses microservices design, service mesh, event-driven architecture, CQRS, saga patterns, container orchestration, caching, message queuing, and observability patterns that enable distributed systems to scale reliably.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Cloud Architecture
  - Cloud Native
  - Distributed Systems
  - High Availability
  - Infrastructure
  - Microservices
  - Performance
  - Resilience
  - Scalability
  - Service Mesh
apis:
  - name: Istio Service Mesh API
    description: Istio is the leading open-source service mesh providing traffic management, security (mTLS), and observability for microservices. The Istio API includes VirtualService, DestinationRule, Gateway, and ServiceEntry custom resources for controlling service-to-service communication in Kubernetes. Graduated CNCF project.
    image: https://istio.io/latest/img/istio-whitelogo-bluebackground-framed.svg
    humanUrl: https://istio.io/
    baseUrl: https://api.istio.io
    tags:
      - CNCF
      - Kubernetes
      - Microservices
      - Observability
      - Security
      - Service Mesh
      - Traffic Management
    properties:
      - type: Documentation
        url: https://istio.io/latest/docs/
      - type: GitHub
        url: https://github.com/istio/istio
      - type: OpenAPI
        url: https://raw.githubusercontent.com/istio/api/master/networking/v1alpha3/virtual_service.proto
      - type: Changelog
        url: https://istio.io/latest/news/releases/
      - type: Getting Started
        url: https://istio.io/latest/docs/setup/getting-started/
    contact:
      - type: Slack
        url: https://slack.istio.io/
      - type: GitHub Issues
        url: https://github.com/istio/istio/issues
  - name: Linkerd API
    description: Linkerd is a lightweight, security-first service mesh for Kubernetes. Built on Rust-based micro-proxy (linkerd2-proxy), Linkerd provides automatic mTLS, observability with golden metrics (success rate, latency, throughput), and traffic management without the operational complexity of Istio. CNCF graduated project.
    image: https://linkerd.io/images/home/logo.svg
    humanUrl: https://linkerd.io/
    baseUrl: https://api.linkerd.io
    tags:
      - CNCF
      - Kubernetes
      - Microservices
      - mTLS
      - Observability
      - Security
      - Service Mesh
    properties:
      - type: Documentation
        url: https://linkerd.io/2.x/overview/
      - type: GitHub
        url: https://github.com/linkerd/linkerd2
      - type: Getting Started
        url: https://linkerd.io/2.x/getting-started/
    contact:
      - type: Slack
        url: https://slack.linkerd.io/
      - type: GitHub Issues
        url: https://github.com/linkerd/linkerd2/issues
  - name: Envoy Proxy Admin API
    description: Envoy is a high-performance, open-source edge and service proxy, and the underlying data plane for Istio, Linkerd, and most service meshes. The Envoy Admin API provides REST endpoints for configuration, statistics, health checks, cluster management, and runtime modification. CNCF graduated project.
    image: https://www.envoyproxy.io/img/envoy-logo.svg
    humanUrl: https://www.envoyproxy.io/
    baseUrl: https://envoy-admin.local:9901
    tags:
      - CNCF
      - Load Balancing
      - Open Source
      - Proxy
      - Service Mesh
      - Traffic Management
    properties:
      - type: Documentation
        url: https://www.envoyproxy.io/docs/envoy/latest/operations/admin
      - type: GitHub
        url: https://github.com/envoyproxy/envoy
      - type: OpenAPI
        url: https://www.envoyproxy.io/docs/envoy/latest/api-v3/api
    contact:
      - type: Slack
        url: https://envoyproxy.slack.com/
      - type: GitHub Issues
        url: https://github.com/envoyproxy/envoy/issues
  - name: Apache Kafka REST Proxy API
    description: The Confluent REST Proxy provides a RESTful interface to an Apache Kafka cluster, making it easy to produce and consume messages, view the state of the cluster, and perform administrative actions without using the native Kafka protocol. Central to event-driven scalable architectures.
    image: https://kafka.apache.org/images/apache-kafka.png
    humanUrl: https://kafka.apache.org/
    baseUrl: https://kafka-rest.example.com
    tags:
      - Apache Kafka
      - Event Streaming
      - Event-Driven
      - Message Broker
      - Microservices
      - Pub-Sub
    properties:
      - type: Documentation
        url: https://docs.confluent.io/platform/current/kafka-rest/api.html
      - type: GitHub
        url: https://github.com/confluentinc/kafka-rest
      - type: OpenAPI
        url: https://raw.githubusercontent.com/confluentinc/kafka-rest/master/api/v3/openapi.yaml
      - type: Getting Started
        url: https://kafka.apache.org/quickstart
    contact:
      - type: Community
        url: https://kafka.apache.org/contact
      - type: GitHub Issues
        url: https://github.com/apache/kafka/issues
  - name: Redis REST API (Redis Stack)
    description: Redis is an in-memory data structure store used as a cache, message broker, and streaming engine. Redis Stack provides REST API access via the RedisJSON and RediSearch modules. Used extensively in scalable architectures for caching, session management, real-time leaderboards, and pub/sub messaging.
    image: https://redis.io/images/redis-logo.svg
    humanUrl: https://redis.io/
    baseUrl: https://redis.example.com/redis
    tags:
      - Caching
      - Data Store
      - In-Memory
      - Message Broker
      - Open Source
      - Pub-Sub
      - Redis
    properties:
      - type: Documentation
        url: https://redis.io/docs/
      - type: GitHub
        url: https://github.com/redis/redis
      - type: API Reference
        url: https://redis.io/docs/data-types/
      - type: Pricing
        url: https://redis.io/pricing/
    contact:
      - type: Community
        url: https://redis.io/community/
      - type: GitHub Issues
        url: https://github.com/redis/redis/issues
  - name: RabbitMQ Management HTTP API
    description: RabbitMQ is a widely-deployed open-source message broker implementing AMQP, MQTT, STOMP, and other messaging protocols. The RabbitMQ Management HTTP API provides REST endpoints for managing exchanges, queues, bindings, users, and virtual hosts—critical for scalable event-driven microservice architectures.
    image: https://www.rabbitmq.com/img/logo-rabbitmq.svg
    humanUrl: https://www.rabbitmq.com/
    baseUrl: https://rabbitmq.example.com:15672/api
    tags:
      - AMQP
      - Event-Driven
      - Message Broker
      - Microservices
      - Open Source
      - RabbitMQ
    properties:
      - type: Documentation
        url: https://www.rabbitmq.com/management.html
      - type: GitHub
        url: https://github.com/rabbitmq/rabbitmq-server
      - type: OpenAPI
        url: https://raw.githubusercontent.com/rabbitmq/rabbitmq-server/main/deps/rabbitmq_management/priv/www/api/index.json
      - type: Getting Started
        url: https://www.rabbitmq.com/tutorials
    contact:
      - type: Community
        url: https://groups.google.com/g/rabbitmq-users
      - type: GitHub Issues
        url: https://github.com/rabbitmq/rabbitmq-server/issues
  - name: Kubernetes API
    description: The Kubernetes API is the foundation of the container orchestration ecosystem, providing REST endpoints for managing the full lifecycle of containerized workloads. Core to scalable architecture, Kubernetes manages Deployments, Services, Ingress, HPA, VPA, ConfigMaps, Secrets, and the entire cluster state. CNCF graduated project.
    image: https://kubernetes.io/images/favicon.png
    humanUrl: https://kubernetes.io/
    baseUrl: https://kubernetes.default.svc
    tags:
      - CNCF
      - Cloud Native
      - Containers
      - Kubernetes
      - Orchestration
      - Open Source
    properties:
      - type: Documentation
        url: https://kubernetes.io/docs/reference/
      - type: GitHub
        url: https://github.com/kubernetes/kubernetes
      - type: OpenAPI
        url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
      - type: Getting Started
        url: https://kubernetes.io/docs/tutorials/
      - type: Changelog
        url: https://kubernetes.io/releases/
    contact:
      - type: Slack
        url: https://slack.k8s.io/
      - type: GitHub Issues
        url: https://github.com/kubernetes/kubernetes/issues
  - name: Argo Workflows API
    description: Argo Workflows is a Kubernetes-native workflow engine for orchestrating parallel jobs. Used extensively in scalable data pipelines, CI/CD systems, and ML workflows. Provides a REST API for submitting, monitoring, and managing workflows and workflow templates. CNCF graduated project.
    image: https://argoproj.github.io/static/4f7f63c9de5b9a7bd1f28ea8d2cb06c9/argo-horizontal-color.png
    humanUrl: https://argoproj.github.io/argo-workflows/
    baseUrl: https://argo-server.example.com/api/v1
    tags:
      - CNCF
      - CI/CD
      - Kubernetes
      - Orchestration
      - Pipelines
      - Workflow
    properties:
      - type: Documentation
        url: https://argoproj.github.io/argo-workflows/
      - type: GitHub
        url: https://github.com/argoproj/argo-workflows
      - type: OpenAPI
        url: https://raw.githubusercontent.com/argoproj/argo-workflows/main/api/openapi-spec/swagger.json
      - type: Getting Started
        url: https://argoproj.github.io/argo-workflows/quick-start/
    contact:
      - type: Slack
        url: https://cloud-native.slack.com/archives/C01LWLS5M2X
      - type: GitHub Issues
        url: https://github.com/argoproj/argo-workflows/issues
common:
  - type: CNCF Landscape
    url: https://landscape.cncf.io/
  - type: GitHub Organization
    url: https://github.com/cncf
  - type: Blog
    url: https://www.cncf.io/blog/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/main/json-schema/scalable-architecture-microservice-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/main/json-schema/scalable-architecture-event-schema.json
  - type: JSONLd
    url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/main/json-ld/scalable-architecture-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scalable-architecture/main/vocabulary/scalable-architecture-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: kin@apievangelist.com
    url: https://apievangelist.com
include:
  - name: Scalability APIs
    url: https://raw.githubusercontent.com/api-evangelist/scalability/refs/heads/main/apis.yml
  - name: Scalable Infrastructure
    url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/refs/heads/main/apis.yml
---
