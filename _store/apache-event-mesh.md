---
aid: apache-event-mesh
name: Apache EventMesh
description: Apache EventMesh is a dynamic event-driven application runtime used to decouple the application and backend middleware layer, providing a serverless platform for building distributed event-driven architectures with support for CloudEvents and multiple messaging protocols including HTTP, TCP, and gRPC.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - CloudEvents
  - Event-Driven
  - Messaging
  - Open Source
  - Pub-Sub
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/apache-event-mesh/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apache-event-mesh:eventmesh-admin-api
    name: Apache EventMesh Admin API
    description: HTTP endpoints for managing the EventMesh runtime including topic management, subscription management, event publishing via HTTP, client monitoring, and runtime metrics.
    humanURL: https://eventmesh.apache.org/docs/instruction/quickstart
    baseURL: http://localhost:10106
    tags:
      - Admin
      - CloudEvents
      - REST API
      - Topics
    properties:
      - type: Documentation
        url: https://eventmesh.apache.org/docs/introduction
      - type: OpenAPI
        url: openapi/eventmesh-admin.yml
      - type: JSONSchema
        url: json-schema/eventmesh-admin-cloud-event-schema.json
      - type: JSON-LD
        url: json-ld/apache-event-mesh-admin-context.jsonld
  - aid: apache-event-mesh:eventmesh-messaging-api
    name: Apache EventMesh Messaging API
    description: Event-driven messaging via TCP, HTTP, and gRPC protocols. Events follow the CloudEvents specification. Supports pub-sub, request-reply, and broadcast messaging patterns.
    humanURL: https://eventmesh.apache.org/docs/sdk-java/tcp-sdk-usage
    tags:
      - CloudEvents
      - Event-Driven
      - Messaging
      - Pub-Sub
    properties:
      - type: Documentation
        url: https://eventmesh.apache.org/docs/sdk-java/tcp-sdk-usage
      - type: AsyncAPI
        url: asyncapi/eventmesh-messaging.yml
common:
  - type: Documentation
    url: https://eventmesh.apache.org/docs/introduction
  - type: GettingStarted
    url: https://eventmesh.apache.org/docs/instruction/quickstart
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/eventmesh
  - type: Blog
    url: https://eventmesh.apache.org/blog
  - type: Support
    url: https://eventmesh.apache.org/community
  - type: SpectralRules
    url: rules/apache-event-mesh-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-event-mesh-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/eventmesh-event-streaming.yaml
  - type: Features
    data:
      - name: CloudEvents Support
        description: Native CloudEvents specification support for standardized event envelopes across all messaging protocols.
      - name: Multi-Protocol Messaging
        description: Support for HTTP, TCP, and gRPC messaging protocols enabling flexible client connectivity.
      - name: Pub-Sub Messaging
        description: Publish-subscribe messaging pattern with topic-based routing for event-driven architectures.
      - name: Request-Reply Pattern
        description: Synchronous request-reply messaging over asynchronous infrastructure for RPC-style interactions.
      - name: Event Store
        description: Durable event storage with replay capability for reliable event delivery and audit trails.
      - name: Workflow Orchestration
        description: Event-driven workflow engine for coordinating distributed business processes and sagas.
      - name: Multi-Runtime Support
        description: Pluggable connector model supporting Kafka, RocketMQ, Pulsar, and other messaging backends.
  - type: UseCases
    data:
      - name: Microservices Decoupling
        description: Decouple microservices through asynchronous event-driven communication reducing direct service dependencies.
      - name: Event Streaming Pipelines
        description: Build scalable event streaming pipelines with durable delivery and replay capabilities.
      - name: Distributed Workflows
        description: Orchestrate distributed business processes using event-driven saga and choreography patterns.
      - name: IoT Event Ingestion
        description: Ingest and process high-volume IoT device events through standardized CloudEvents format.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Kafka connector for event streaming with durable storage and consumer groups.
      - name: Apache RocketMQ
        description: RocketMQ connector for high-throughput message queueing and topic management.
      - name: Apache Pulsar
        description: Pulsar connector for multi-tenant event streaming with geo-replication.
      - name: Kubernetes
        description: Cloud-native deployment on Kubernetes with operator support for cluster management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
