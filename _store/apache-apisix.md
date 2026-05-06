---
aid: apache-apisix
name: Apache APISIX
description: Apache APISIX is a dynamic, real-time, high-performance cloud-native API gateway built on NGINX and etcd, developed by the Apache Software Foundation. It supports Lua and multi-language plugins for traffic management, authentication, observability, and security. APISIX provides a RESTful Admin API for dynamic configuration of routes, upstreams, services, consumers, SSL certificates, and plugins, and a Control API for health monitoring and schema introspection.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - API Gateway
  - Cloud Native
  - Kubernetes
  - Lua
  - NGINX
  - Open Source
  - Traffic Management
url: https://raw.githubusercontent.com/api-evangelist/apache-apisix/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apache-apisix:apache-apisix-gateway
    name: Apache APISIX Gateway
    description: Apache APISIX provides rich traffic management features including load balancing, dynamic upstream configuration, canary releases, circuit breaking, authentication, observability plugins, and more. It is built on NGINX for high performance with etcd for distributed configuration.
    humanURL: https://apisix.apache.org/
    tags:
      - API Gateway
      - Apache
      - Cloud Native
    properties:
      - type: Documentation
        url: https://apisix.apache.org/docs/apisix/getting-started/
      - type: GettingStarted
        url: https://apisix.apache.org/docs/apisix/getting-started/README/
  - aid: apache-apisix:apache-apisix-admin-api
    name: Apache APISIX Admin API
    description: The Apache APISIX Admin API provides a RESTful interface to dynamically control and configure a running APISIX instance. It supports management of routes, services, upstreams, consumers, SSL certificates, global rules, plugin configurations, consumer groups, and secrets, and listens by default on port 9180 with API key authentication.
    humanURL: https://apisix.apache.org/docs/apisix/admin-api/
    tags:
      - Admin
      - Configuration
      - Management
      - REST
    properties:
      - type: Documentation
        url: https://apisix.apache.org/docs/apisix/admin-api/
      - type: OpenAPI
        url: openapi/apache-apisix-admin-api-openapi.yml
      - type: Authentication
        url: https://apisix.apache.org/docs/apisix/admin-api/#using-the-admin-api
  - aid: apache-apisix:apache-apisix-control-api
    name: Apache APISIX Control API
    description: The Apache APISIX Control API provides internal status and health check endpoints for monitoring and introspecting a running APISIX instance. It listens by default on port 9090, is accessible only from localhost, and exposes endpoints for health checking, schema retrieval, and runtime diagnostics.
    humanURL: https://apisix.apache.org/docs/apisix/control-api/
    tags:
      - Control
      - Health Check
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://apisix.apache.org/docs/apisix/control-api/
      - type: OpenAPI
        url: openapi/apache-apisix-control-api-openapi.yml
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/apisix
  - type: Documentation
    url: https://apisix.apache.org/docs/
  - type: GettingStarted
    url: https://apisix.apache.org/docs/apisix/getting-started/
  - type: Blog
    url: https://apisix.apache.org/blog/
  - type: ChangeLog
    url: https://github.com/apache/apisix/releases
  - type: Support
    url: https://apisix.apache.org/docs/general/community/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/apache-apisix
  - type: JSONSchema
    url: json-schema/route.json
  - type: JSONSchema
    url: json-schema/upstream.json
  - type: JSONSchema
    url: json-schema/service.json
  - type: JSONSchema
    url: json-schema/consumer.json
  - type: JSONSchema
    url: json-schema/ssl.json
  - type: JSONSchema
    url: json-schema/global-rule.json
  - type: JSONSchema
    url: json-schema/plugin-config.json
  - type: JSONSchema
    url: json-schema/consumer-group.json
  - type: JSONSchema
    url: json-schema/stream-route.json
  - type: JSONSchema
    url: json-schema/secret.json
  - type: JSONLD
    url: json-ld/apache-apisix-context.jsonld
  - type: SpectralRules
    url: rules/apache-apisix-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-apisix-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/apisix-gateway-config.yaml
  - type: Features
    data:
      - name: Dynamic Route Configuration
        description: Dynamically add, update, and delete routes without restarting via the Admin API and etcd-backed config.
      - name: Multi-Protocol Support
        description: Supports HTTP, HTTPS, HTTP/2, gRPC, TCP, UDP, and WebSocket protocols for diverse API types.
      - name: Plugin Ecosystem
        description: Rich plugin ecosystem for authentication (JWT, key-auth, OAuth2), rate limiting, transformations, and observability.
      - name: Multi-Language Plugin Support
        description: Plugins can be written in Lua, Go, Python, Java, and Node.js via the Plugin Runner architecture.
      - name: Load Balancing
        description: Supports round-robin, consistent hashing, EWMA, and least connections load balancing strategies.
      - name: Canary Releases
        description: Traffic splitting for canary deployments and A/B testing with percentage-based routing.
      - name: Circuit Breaking
        description: Built-in circuit breaker plugin for resilience and fault tolerance in upstream communication.
      - name: Kubernetes Integration
        description: Native Kubernetes ingress controller (APISIX Ingress) for Kubernetes-native API gateway deployments.
      - name: Observability
        description: Native integrations with Prometheus, Zipkin, SkyWalking, Datadog, and OpenTelemetry for metrics and tracing.
      - name: Service Discovery
        description: Dynamic service discovery via Kubernetes, Nacos, Consul, Eureka, and DNS for upstream resolution.
  - type: UseCases
    data:
      - name: API Gateway for Microservices
        description: Route and manage traffic to microservices with dynamic configuration and plugin-based policies.
      - name: Authentication and Authorization
        description: Apply JWT, key-auth, LDAP, OIDC, and OAuth2 plugins to protect APIs without changing upstream services.
      - name: Rate Limiting and Throttling
        description: Apply global or per-consumer rate limits to protect upstream services from traffic spikes.
      - name: Canary and Blue-Green Deployments
        description: Use traffic splitting to gradually roll out new API versions with percentage-based routing.
      - name: Kubernetes Ingress Controller
        description: Replace traditional ingress controllers with APISIX for rich API gateway features in Kubernetes.
      - name: API Observability
        description: Collect metrics, traces, and logs via native integrations with Prometheus, Zipkin, and SkyWalking.
  - type: Integrations
    data:
      - name: Kubernetes
        description: Native Kubernetes Ingress controller (APISIX Ingress Controller) for cloud-native deployments.
      - name: Prometheus
        description: Native Prometheus metrics exporter for monitoring route, consumer, and upstream metrics.
      - name: Zipkin and Jaeger
        description: Distributed tracing integration for request flow analysis across microservices.
      - name: OpenTelemetry
        description: OpenTelemetry plugin for standardized telemetry data export.
      - name: etcd
        description: etcd backend for distributed configuration storage and cluster synchronization.
      - name: Nacos and Consul
        description: Dynamic service discovery integrations for automatic upstream resolution.
      - name: HashiCorp Vault
        description: Secret management integration for storing API credentials and TLS certificates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
