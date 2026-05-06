---
name: AMQP
description: AMQP (Advanced Message Queuing Protocol) is an open standard for message-oriented middleware governed by OASIS and standardized as ISO/IEC 19464. AMQP 1.0 enables interoperable, asynchronous communication between applications across different platforms and vendors. It defines a wire-level protocol supporting reliable queuing, flexible routing, publish/subscribe, and request/reply messaging patterns. Major implementations include Apache ActiveMQ/Artemis, RabbitMQ, Azure Service Bus, Red Hat AMQ, and Apache Qpid.
url: https://www.amqp.org/
tags:
  - AMQP
  - Asynchronous
  - Message Queue
  - Messaging
  - Middleware
  - Open Standard
  - Publish Subscribe
created: '2025'
modified: '2026-04-19'
apis:
  - name: AMQP Messaging API
    description: AsyncAPI specification for AMQP messaging patterns including publish/subscribe, request/reply, and point-to-point messaging via exchanges, queues, and bindings.
    properties:
      - type: AsyncAPI
        url: asyncapi/amqp-messaging.yml
    tags:
      - AMQP
      - AsyncAPI
      - Messaging
      - Point to Point
      - Publish Subscribe
      - Request Reply
    humanURL: https://www.amqp.org/
common:
  - type: JSONSchema
    title: AMQP Message
    url: json-schema/amqp-message.json
    description: JSON Schema describing the structure of an AMQP message including properties, headers, and payload body.
  - type: JSONSchema
    title: AMQP Message Properties
    url: json-schema/amqp-message-properties.json
    description: JSON Schema describing the standard AMQP 0-9-1 Basic.Properties including content type, delivery mode, correlation ID, and reply-to.
  - type: JSONSchema
    title: AMQP Exchange
    url: json-schema/amqp-exchange.json
    description: JSON Schema describing an AMQP exchange with type, durability, auto-delete, and argument configuration.
  - type: JSONSchema
    title: AMQP Queue
    url: json-schema/amqp-queue.json
    description: JSON Schema describing an AMQP queue with support for TTL, dead-lettering, priority, and overflow policies.
  - type: JSONSchema
    title: AMQP Binding
    url: json-schema/amqp-binding.json
    description: JSON Schema describing an AMQP binding that links exchanges to queues or other exchanges using routing keys.
  - type: JSONLD
    title: AMQP JSON-LD Context
    url: json-ld/amqp-context.jsonld
    description: JSON-LD context mapping AMQP concepts (messages, exchanges, queues, bindings, channels) to linked data vocabularies including Schema.org and Dublin Core.
  - type: Portal
    url: https://www.amqp.org/
  - type: Documentation
    url: https://www.amqp.org/resources/specifications
  - type: GitHubOrganization
    url: https://github.com/amqp
  - type: GitHubOrganization
    url: https://github.com/apache
    title: Apache Qpid
  - type: Features
    data:
      - name: Reliable Messaging
        description: Guaranteed delivery with acknowledgment and persistence support.
      - name: Flexible Routing
        description: Exchange types (direct, fanout, topic, headers) for flexible message routing.
      - name: Publish/Subscribe
        description: Fan-out delivery to multiple consumers via topic and fanout exchanges.
      - name: Request/Reply
        description: Synchronous RPC patterns over asynchronous messaging infrastructure.
      - name: Transaction Support
        description: Transactional message publishing and acknowledgment for data consistency.
      - name: Security
        description: SASL authentication and TLS encryption for secure message transport.
      - name: Flow Control
        description: Credit-based flow control preventing consumer overload (AMQP 1.0).
      - name: Multi-Vendor Interoperability
        description: Wire-level protocol interoperability across different broker implementations.
  - type: UseCases
    data:
      - name: Microservices Communication
        description: Decoupled inter-service messaging in microservices architectures.
      - name: Event Streaming
        description: Event-driven architecture with durable, ordered event delivery.
      - name: Task Queues
        description: Distributed work queues for background job processing.
      - name: IoT Messaging
        description: Device-to-cloud and cloud-to-device messaging for IoT platforms.
      - name: Financial Messaging
        description: High-reliability financial transaction messaging with guaranteed delivery.
      - name: Log Aggregation
        description: Centralized log collection and routing from distributed systems.
  - type: Integrations
    data:
      - name: RabbitMQ
        description: Popular AMQP 0-9-1 compliant broker with extensive plugin ecosystem.
      - name: Apache ActiveMQ
        description: Java-based message broker supporting AMQP 1.0 and multiple protocols.
      - name: Azure Service Bus
        description: Microsoft's cloud messaging service with AMQP 1.0 support.
      - name: Apache Qpid
        description: AMQP 1.0 implementation with broker and client library support.
      - name: Red Hat AMQ
        description: Enterprise messaging platform based on ActiveMQ Artemis with AMQP 1.0.
      - name: Solace PubSub+
        description: Enterprise event broker supporting AMQP 1.0 among multiple protocols.
  - type: JSONStructure
    url: json-structure/amqp-message-structure.json
  - type: JSONStructure
    url: json-structure/amqp-exchange-structure.json
  - type: JSONStructure
    url: json-structure/amqp-queue-structure.json
  - type: SpectralRules
    url: rules/amqp-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amqp-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
