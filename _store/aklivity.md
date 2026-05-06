---
aid: aklivity
name: Aklivity
description: Aklivity provides the Zilla multi-protocol edge and service proxy for event-driven architectures, enabling seamless integration between web apps, IoT clients, and microservices with Apache Kafka via declaratively defined, stateless APIs. Zilla supports HTTP, gRPC, MQTT, SSE, and WebSocket protocols, translating them to and from Kafka without custom code or connectors. The Zilla Platform adds enterprise governance, observability, and self-service access management for Kafka deployments.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Apache Kafka
  - Event-Driven
  - IoT
  - Kafka Proxy
  - Multi-Protocol
  - Real-Time
url: https://raw.githubusercontent.com/api-evangelist/aklivity/refs/heads/main/apis.yml
created: '2026-01-02'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: aklivity:zilla-gateway
    name: Zilla Gateway
    description: Zilla is a stateless, cloud-native multi-protocol edge and service proxy that enables seamless access to Apache Kafka through HTTP REST, gRPC, SSE, MQTT, and WebSocket protocols. Zilla eliminates the need for Kafka Connect, custom code, or separate MQTT brokers, translating client protocol requests directly to Kafka operations declaratively via YAML configuration or AsyncAPI specifications.
    humanURL: https://www.aklivity.io/
    tags:
      - API Gateway
      - Apache Kafka
      - Event-Driven
      - Kafka Proxy
      - Multi-Protocol
    properties:
      - type: Documentation
        url: https://docs.aklivity.io/zilla/latest/
      - type: GettingStarted
        url: https://docs.aklivity.io/zilla/latest/getting-started/quickstart/
      - type: GitHubRepository
        url: https://github.com/aklivity/zilla
      - type: AsyncAPI
        url: https://docs.aklivity.io/zilla/latest/concepts/config/
  - aid: aklivity:zilla-platform
    name: Zilla Platform
    description: The Zilla Platform adds an enterprise management layer on top of Zilla Gateway, providing API data products with versioning and rate limits, Kafka governance policies, a self-service developer portal with API key and certificate management, field-level encryption, PII classification, and unified observability across Kafka deployments.
    humanURL: https://www.aklivity.io/platform
    tags:
      - API Management
      - Developer Portal
      - Governance
      - Kafka Management
      - Observability
    properties:
      - type: Documentation
        url: https://docs.aklivity.io/
      - type: GettingStarted
        url: https://docs.aklivity.io/
  - aid: aklivity:zillabase
    name: ZillaBase
    description: ZillaBase is an event-driven backend framework for the next generation of web, mobile, and AI applications, built on top of Apache Kafka and Zilla to enable real-time, event-sourced application development.
    humanURL: https://github.com/aklivity/zillabase
    tags:
      - Backend Framework
      - Event-Driven
      - Real-Time
    properties:
      - type: Documentation
        url: https://docs.aklivity.io/
      - type: GitHubRepository
        url: https://github.com/aklivity/zillabase
common:
  - type: Website
    url: https://www.aklivity.io/
  - type: Documentation
    url: https://docs.aklivity.io/zilla/latest/
  - type: GettingStarted
    url: https://docs.aklivity.io/zilla/next/getting-started/quickstart/
  - type: GitHubOrganization
    url: https://github.com/aklivity
  - type: GitHubRepository
    url: https://github.com/aklivity/zilla
  - type: Pricing
    url: https://www.aklivity.io/pricing
  - type: Features
    data:
      - name: Multi-Protocol Kafka Access
        description: Translates HTTP REST, gRPC, MQTT, SSE, and WebSocket protocols directly to Kafka topics without custom code, connectors, or middleware.
      - name: Declarative Configuration
        description: Define gateways and protocol mappings via YAML configuration or AsyncAPI specifications, then deploy with Docker, Helm, or native binaries.
      - name: JWT Authentication and TLS
        description: Built-in JWT token validation, TLS termination, and Kafka SASL support for securing API access to Kafka clusters.
      - name: Schema Validation
        description: SIMD-optimized runtime schema validation for JSON, Avro, and Protobuf via Confluent Schema Registry or AWS Glue Schema Registry.
      - name: Observability
        description: Metrics and logs exported to Prometheus and OpenTelemetry for unified visibility across Kafka API traffic.
      - name: Kafka Governance
        description: Topic naming policies, runtime enforcement, schema compliance rules, and API data product versioning with rate limits via Zilla Platform.
      - name: Self-Service Developer Portal
        description: API key and certificate management self-service portal for Kafka consumers and producers via Zilla Platform.
      - name: Field-Level Encryption
        description: PII classification and field-level encryption for sensitive data in Kafka messages via Zilla Platform.
  - type: UseCases
    data:
      - name: HTTP to Kafka REST API
        description: Expose Kafka topics as REST API endpoints, allowing any HTTP client to produce and consume Kafka messages without Kafka client libraries.
      - name: IoT MQTT to Kafka
        description: Connect IoT devices using MQTT protocol directly to Kafka topics, eliminating the need for a separate MQTT broker.
      - name: gRPC to Kafka
        description: Route gRPC calls from microservices to Kafka topics for event-driven inter-service communication.
      - name: Kafka Self-Service Platform
        description: Platform teams build internal developer portals for Kafka access with governance, rate limiting, and self-service API key management.
      - name: Event-Driven Partner Integration
        description: Enterprises expose Kafka event streams to external partners via secured, rate-limited REST or SSE APIs.
      - name: Financial Services Data Distribution
        description: Financial institutions distribute real-time market data and trade events via secured Kafka API gateways.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Core integration — Zilla acts as a multi-protocol proxy in front of any Kafka cluster
      - name: AWS MSK
        description: Managed Streaming for Apache Kafka integration with AWS-native security
      - name: Confluent Schema Registry
        description: Schema validation and enforcement using Confluent Schema Registry
      - name: AWS Glue Schema Registry
        description: Schema validation using AWS Glue Schema Registry
      - name: Prometheus
        description: Metrics export for monitoring Zilla gateway performance
      - name: OpenTelemetry
        description: Distributed tracing and observability via OpenTelemetry
      - name: AWS Secrets Manager
        description: Secure credential management for Kafka and TLS configurations
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
