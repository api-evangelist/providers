---
aid: kong
name: Kong
description: Kong Gateway is the world's most popular open-source API gateway, built on NGINX and Lua, offering a plugin ecosystem for authentication, rate limiting, observability, and traffic management at any scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Lua
  - NGINX
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/kong/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-18'
specificationVersion: '0.19'
apis:
  - aid: kong:kong
    name: Kong Gateway
    description: Kong Gateway is an open-source, lightweight API gateway optimized for microservices, delivering unparalleled latency performance and scalability through a rich plugin ecosystem.
    humanURL: https://konghq.com/products/kong-gateway
    tags:
      - API Gateway
      - Open Source
    properties:
      - type: Documentation
        url: https://developer.konghq.com/gateway/
      - type: GettingStarted
        url: https://docs.konghq.com/gateway/latest/get-started/
      - type: ChangeLog
        url: https://developer.konghq.com/gateway/changelog/
      - type: GitHubRepository
        url: https://github.com/Kong/kong
  - aid: kong:kong-admin-api
    name: Kong Gateway Admin API
    description: The Kong Gateway Admin API provides a RESTful interface for configuring and managing Kong Gateway instances, including services, routes, plugins, consumers, and certificates. It is used by operators to configure the gateway programmatically or via decK declarative configuration.
    humanURL: https://developer.konghq.com/admin-api/
    baseURL: https://konghq.com/
    tags:
      - Admin API
      - Configuration
      - Gateway
      - REST API
    properties:
      - type: Documentation
        url: https://developer.konghq.com/admin-api/
      - type: OpenAPI
        url: openapi/kong-gateway-admin-api.yml
      - type: JSONSchema
        url: json-schema/kong-service-schema.json
      - type: JSONLD
        url: json-ld/kong-context.jsonld
      - type: GitHubRepository
        url: https://github.com/Kong/kong
  - aid: kong:kong-konnect-api
    name: Kong Konnect API
    description: The Kong Konnect API provides a programmatic interface for managing the Konnect cloud platform, including control planes, API products, teams, system accounts, and developer portal configuration. It is used to automate Konnect operations and integrate with CI/CD pipelines.
    humanURL: https://developer.konghq.com/konnect-api/
    baseURL: https://konghq.com/
    tags:
      - Cloud
      - Konnect
      - Management
      - REST API
    properties:
      - type: Documentation
        url: https://developer.konghq.com/konnect-api/
      - type: APIReference
        url: https://developer.konghq.com/api/
      - type: Authentication
        url: https://developer.konghq.com/konnect-api/
      - type: GitHubRepository
        url: https://github.com/Kong/kong
  - aid: kong:kong-mesh
    name: Kong Mesh
    description: Kong Mesh is an enterprise-grade service mesh built on top of Kuma and Envoy, providing universal service mesh capabilities across Kubernetes and virtual machine environments. It supports mTLS, traffic policies, service discovery, observability, and multi-zone deployments.
    humanURL: https://developer.konghq.com/mesh/
    baseURL: https://konghq.com/
    tags:
      - Envoy
      - Kubernetes
      - mTLS
      - Service Mesh
    properties:
      - type: Documentation
        url: https://developer.konghq.com/mesh/
      - type: ChangeLog
        url: https://developer.konghq.com/mesh/changelog/
      - type: GettingStarted
        url: https://developer.konghq.com/mesh/
  - aid: kong:kong-insomnia
    name: Kong Insomnia
    description: Kong Insomnia is an open-source API development platform for designing, debugging, and testing APIs. It supports REST, GraphQL, gRPC, and WebSocket protocols and provides collections, environments, mock servers, and OpenAPI spec editing for developers.
    humanURL: https://developer.konghq.com/insomnia/
    baseURL: https://konghq.com/
    tags:
      - API Client
      - Developer Tools
      - Open Source
      - Testing
    properties:
      - type: Documentation
        url: https://developer.konghq.com/insomnia/
      - type: GitHubRepository
        url: https://github.com/Kong/insomnia
common:
  - type: Documentation
    url: https://developer.konghq.com/
  - type: GettingStarted
    url: https://docs.konghq.com/gateway/latest/get-started/
  - type: Blog
    url: https://konghq.com/blog
  - type: ChangeLog
    url: https://developer.konghq.com/gateway/changelog/
  - type: GitHubOrganization
    url: https://github.com/Kong
  - type: GitHubRepository
    url: https://github.com/Kong/kong
  - type: SDK
    url: https://github.com/Kong/sdk-konnect-go
    name: Kong Konnect Go SDK
  - type: CLI
    url: https://github.com/Kong/kongctl
    name: Kong Developer CLI
  - type: Support
    url: https://discuss.konghq.com/
  - type: JSONSchema
    url: json-schema/kong-service-schema.json
  - type: JSONLD
    url: json-ld/kong-context.jsonld
  - type: Features
    data:
      - name: Plugin Ecosystem
        description: Extensible plugin architecture for authentication, rate limiting, logging, transformations, and custom business logic.
      - name: Service and Route Management
        description: Define upstream services and routing rules to direct client requests to the correct backend services.
      - name: Consumer Management
        description: Create and manage API consumers with per-consumer authentication credentials and plugin configurations.
      - name: Load Balancing
        description: Built-in upstream load balancing with health checks, circuit breaking, and weighted target distribution.
      - name: TLS Certificate Management
        description: Manage TLS certificates and SNI mappings for secure HTTPS traffic termination at the gateway.
      - name: Declarative Configuration
        description: Configure Kong Gateway declaratively using decK or the Admin API for infrastructure-as-code workflows.
      - name: Kong Konnect Cloud Platform
        description: Centralized cloud control plane for managing multiple Kong Gateway instances, teams, and API products.
      - name: Service Mesh with Kong Mesh
        description: Enterprise service mesh built on Kuma and Envoy for mTLS, traffic policies, and multi-zone deployments.
  - type: UseCases
    data:
      - name: API Gateway for Microservices
        description: Route, secure, and observe traffic to microservices with authentication, rate limiting, and request transformations.
      - name: Multi-Cloud API Management
        description: Manage APIs across hybrid and multi-cloud environments with centralized control through Kong Konnect.
      - name: Zero-Trust Security
        description: Implement zero-trust security with mTLS, OAuth2, JWT validation, and API key authentication at the gateway layer.
      - name: API Lifecycle Management
        description: Manage the full API lifecycle from design with Insomnia to deployment and monitoring with Kong Gateway.
      - name: Rate Limiting and Traffic Control
        description: Protect backend services with configurable rate limiting, request size limits, and traffic shaping policies.
  - type: Integrations
    data:
      - name: Kubernetes
        description: Deploy Kong Gateway as a Kubernetes Ingress Controller with CRD-based configuration for cloud-native environments.
      - name: Prometheus and Grafana
        description: Export gateway metrics to Prometheus and visualize API performance and health in Grafana dashboards.
      - name: OpenTelemetry
        description: Distributed tracing integration with OpenTelemetry for end-to-end request visibility across services.
      - name: HashiCorp Vault
        description: Secrets management integration for storing and retrieving API keys, certificates, and credentials.
      - name: Datadog
        description: Send gateway logs, metrics, and traces to Datadog for comprehensive API monitoring and alerting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
