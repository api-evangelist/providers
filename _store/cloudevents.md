---
aid: cloudevents
url: https://raw.githubusercontent.com/api-evangelist/cloudevents/refs/heads/main/apis.yml
apis:
- aid: cloudevents:cloudevents-spec
  name: CloudEvents Specification
  description: The CloudEvents specification defines a set of metadata attributes that must be present in every event, including source, type, id, and specversion. It provides a vendor-neutral way to describe events that enables consistent routing, filtering, and processing across different systems and cloud providers.
  humanURL: https://cloudevents.io/
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
  - type: Reference
    url: https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
  - type: GitHubRepository
    url: https://github.com/cloudevents/spec
  - type: Change Log
    url: https://github.com/cloudevents/spec/releases
  - type: JSONSchema
    url: json-schema/cloudevents-event-schema.json
  - type: AsyncAPI
    url: asyncapi/cloudevents-http-asyncapi.yml
  tags:
  - Events
  - Specification
  - Standards
- aid: cloudevents:cloudevents-http-binding
  name: CloudEvents HTTP Protocol Binding
  description: The HTTP protocol binding defines how CloudEvents are transported using HTTP, including structured content mode where the entire event is in the HTTP body, and binary content mode where event attributes are mapped to HTTP headers. This enables REST APIs to produce and consume standardized events.
  humanURL: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md
  - type: Reference
    url: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/http-protocol-binding.md
  tags:
  - HTTP
  - Protocol Binding
  - REST
- aid: cloudevents:cloudevents-kafka-binding
  name: CloudEvents Kafka Protocol Binding
  description: The Kafka protocol binding for CloudEvents defines how events are mapped to Apache Kafka messages. It specifies how CloudEvents attributes are encoded as Kafka message headers and how the event payload is placed in the Kafka message value, enabling standardized event interchange over Kafka topics.
  humanURL: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/kafka-protocol-binding.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/kafka-protocol-binding.md
  - type: Reference
    url: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/kafka-protocol-binding.md
  tags:
  - Kafka
  - Messaging
  - Protocol Binding
- aid: cloudevents:cloudevents-amqp-binding
  name: CloudEvents AMQP Protocol Binding
  description: The AMQP protocol binding for CloudEvents defines how events are mapped to OASIS AMQP 1.0 messages. In structured content mode, event attributes and data are placed in the AMQP message application data section; in binary content mode, event data is placed as-is with attributes mapped to AMQP message properties.
  humanURL: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/amqp-protocol-binding.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/amqp-protocol-binding.md
  - type: Reference
    url: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/amqp-protocol-binding.md
  tags:
  - AMQP
  - Messaging
  - Protocol Binding
- aid: cloudevents:cloudevents-mqtt-binding
  name: CloudEvents MQTT Protocol Binding
  description: The MQTT protocol binding for CloudEvents defines how events are mapped to MQTT 3.1.1 and MQTT 5.0 messages. It supports both structured and binary content modes for IoT and constrained device environments that use MQTT as their messaging protocol.
  humanURL: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/mqtt-protocol-binding.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/mqtt-protocol-binding.md
  tags:
  - IoT
  - MQTT
  - Protocol Binding
- aid: cloudevents:cloudevents-nats-binding
  name: CloudEvents NATS Protocol Binding
  description: The NATS protocol binding for CloudEvents defines how events are mapped to NATS messages. It enables CloudEvents to be produced and consumed over the NATS messaging system, supporting both publish/subscribe and request/reply patterns.
  humanURL: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/nats-protocol-binding.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/nats-protocol-binding.md
  tags:
  - Messaging
  - NATS
  - Protocol Binding
- aid: cloudevents:cloudevents-subscriptions
  name: CloudEvents Subscriptions API
  description: The CloudEvents Subscriptions API specification defines a standard REST API for managing subscriptions to event streams. It enables clients to create, list, update, and delete subscriptions with filter criteria, providing a vendor-neutral way to manage event delivery configurations across different event brokers and message systems.
  humanURL: https://github.com/cloudevents/spec/blob/main/subscriptions/spec.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/main/subscriptions/spec.md
  - type: OpenAPI
    url: openapi/cloudevents-subscriptions-openapi.yml
  tags:
  - REST
  - Specification
  - Subscriptions
- aid: cloudevents:cloudevents-cesql
  name: CloudEvents SQL (CESQL)
  description: CloudEvents SQL (CESQL) is a v1.0 specification that defines a standardized query language for filtering and routing CloudEvents based on their attributes. It provides a SQL-like syntax for writing event filter expressions that can be used across different event processing platforms and systems.
  humanURL: https://github.com/cloudevents/spec/blob/main/cesql/spec.md
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/spec/blob/main/cesql/spec.md
  tags:
  - Filtering
  - Specification
  - SQL
- aid: cloudevents:cloudevents-sdk-go
  name: CloudEvents Go SDK
  description: The official Go SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Go applications. It supports all CloudEvents protocol bindings and content modes, and includes client implementations for HTTP, Kafka, and other transports.
  humanURL: https://github.com/cloudevents/sdk-go
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://cloudevents.github.io/sdk-go/
  - type: GitHubRepository
    url: https://github.com/cloudevents/sdk-go
  tags:
  - Client Library
  - Go
  - SDK
- aid: cloudevents:cloudevents-sdk-javascript
  name: CloudEvents JavaScript SDK
  description: The official JavaScript SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Node.js and browser environments. It supports structured and binary content modes over HTTP and other transports.
  humanURL: https://github.com/cloudevents/sdk-javascript
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/sdk-javascript/blob/main/README.md
  - type: GitHubRepository
    url: https://github.com/cloudevents/sdk-javascript
  tags:
  - Client Library
  - JavaScript
  - SDK
- aid: cloudevents:cloudevents-sdk-java
  name: CloudEvents Java SDK
  description: The official Java SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Java applications. It includes support for HTTP, Kafka, and other transports, and integrates with popular Java frameworks.
  humanURL: https://github.com/cloudevents/sdk-java
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/sdk-java/blob/main/README.md
  - type: GitHubRepository
    url: https://github.com/cloudevents/sdk-java
  tags:
  - Client Library
  - Java
  - SDK
- aid: cloudevents:cloudevents-sdk-python
  name: CloudEvents Python SDK
  description: The official Python SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Python applications. It supports HTTP transport bindings and both structured and binary content modes.
  humanURL: https://github.com/cloudevents/sdk-python
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  properties:
  - type: Documentation
    url: https://github.com/cloudevents/sdk-python/blob/main/README.md
  - type: GitHubRepository
    url: https://github.com/cloudevents/sdk-python
  tags:
  - Client Library
  - Python
  - SDK
name: CloudEvents
tags:
- Cloud Native
- Events
- Graduated
- Interoperability
- Messaging
- Specification
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CloudEvents is a CNCF graduated specification for describing event data in a common way. It provides a consistent format for event metadata across services, platforms, and systems, enabling interoperability between event producers and consumers. The specification includes protocol bindings for HTTP, AMQP, Kafka, MQTT, and NATS, along with SDKs in multiple languages.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

