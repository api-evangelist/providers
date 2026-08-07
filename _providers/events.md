---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 18
apis:
- description: CNCF-graduated specification (graduated January 25, 2024) for describing event data in a common way. Defines a payload envelope with required attributes id, source, specversion, and type, and optional
  name: CloudEvents
  slug: cloudevents
- description: 'Linux Foundation-hosted specification for event-driven APIs. Describes servers, channels, operations, messages, schemas, and protocol bindings for Kafka, AMQP, MQTT, NATS, WebSockets, HTTP, and more. '
  name: AsyncAPI
  slug: asyncapi
- description: Open-source distributed event streaming platform governed by the Apache Software Foundation. Described as used by "thousands of companies for high-performance data pipelines, streaming analytics, data
  name: Apache Kafka
  slug: apache-kafka
- description: Open-source distributed messaging and streaming platform built for the cloud. Top-10 Apache Software Foundation project (740+ contributors, current version 4.2). Multi-tenant by design (tenants, names
  name: Apache Pulsar
  slug: apache-pulsar
- description: CNCF incubating high-performance, lightweight messaging system designed for cloud, edge, and IoT. Supports pub/sub, request/reply, and queue groups over a text-based protocol. JetStream extends NATS w
  name: NATS
  slug: nats
- description: Kafka API-compatible streaming data platform written in C++ (no JVM, no ZooKeeper). Self-described as an "Agentic Data Plane and Data Streaming platform for real-time performance, AI innovation, and s
  name: Redpanda
  slug: redpanda
- description: Enterprise messaging middleware from IBM. Long the de facto standard for assured-once message delivery in regulated industries (banking, government). Exposes the MQI native API, JMS, AMQP 1.0, MQTT, a
  name: IBM MQ
  slug: ibm-mq
- description: AWS serverless event router. "EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications." Tw
  name: AWS EventBridge
  slug: aws-eventbridge
- description: Azure's "highly scalable and fully managed publish-subscribe service for message distribution." Supports both HTTP push/pull delivery and an MQTT v3.1.1 / v5.0 broker mode for IoT clients. Supports Cl
  name: Azure Event Grid
  slug: azure-event-grid
- description: 'Google Cloud''s asynchronous and scalable messaging service that decouples message producers from consumers with typical latencies around 100 ms. Uses per-message leasing (not partitions) for parallel '
  name: Google Cloud Pub/Sub
  slug: google-cloud-pubsub
- description: 'Commercial managed service from Confluent positioned as "the industry''s only fully managed data streaming platform." Built on the Kora cloud-native Kafka engine. Tiers: Basic, Standard, Enterprise, an'
  name: Confluent Cloud
  slug: confluent-cloud
- description: Central repository with a RESTful interface for registering and evolving schemas in Avro, JSON Schema, and Protobuf. Enforces compatibility rules (backward, forward, full, transitive) for Kafka topics
  name: Confluent Schema Registry
  slug: confluent-schema-registry
- description: Open-source schema and API artifact registry backed by Red Hat (Apache 2.0). Stores OpenAPI, AsyncAPI, Avro, JSON Schema, Protobuf, Kafka Connect schemas, GraphQL SDL, WSDL, and XSD. Configurable cont
  name: Apicurio Registry
  slug: apicurio-registry
- description: 'Managed ClickHouse-based SaaS for real-time analytics on event data. Ingests events via an HTTP Events API (up to 1,000 req/s) plus connectors for Kafka, S3, GCS, BigQuery, Snowflake, and PostgreSQL. '
  name: Tinybird
  slug: tinybird
- description: 'Streaming SQL database based on incremental view maintenance. Continually ingests CDC from Postgres, Kafka, and other sources, then keeps SQL views up to date with minimal recomputation. Materialized '
  name: Materialize
  slug: materialize
- description: 'OASIS standard messaging protocol for the Internet of Things. Lightweight publish/subscribe transport for remote, constrained devices. Current version is MQTT 5.0 (predecessors 3.1, 3.1.1). Three QoS '
  name: MQTT
  slug: mqtt
- description: Advanced Message Queuing Protocol. AMQP 1.0 is both an OASIS standard and an International Standard (ISO/IEC 19464). Wire-level binary protocol defining nodes, links, sessions, and frames. Mission per
  name: AMQP
  slug: amqp
- description: 'Simple (or Streaming) Text Oriented Messaging Protocol. Lightweight, text-based wire protocol for message-oriented middleware. Widely used as an alternative front-end on brokers like Apache ActiveMQ, '
  name: STOMP
  slug: stomp
artifact_total: 53
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/events-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://github.com/api-evangelist/events
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/events-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/events-context.jsonld
- group: other
  title: ''
  type: RelatedTopics
  url: ''
created: '2026-05-22'
description: Event-driven APIs catalog. Documents the landscape of brokers, streaming platforms, schema registries, and the specifications that standardize how events are described, transported, and stored. "Events" is the broader category that contains webhooks (HTTP callbacks) as one delivery surface, alongside message brokers, log-based streaming platforms, and managed pub/sub services. The catalog aligns around CloudEvents (CNCF graduated, v1.0.2) as the spec for the event payload envelope and AsyncAPI as the spec for the event API surface (channels, operations, messages, servers), and covers the major open-source brokers (Apache Kafka, Apache Pulsar, NATS, Redpanda, IBM MQ), cloud-native managed buses (AWS EventBridge, Azure Event Grid, Google Cloud Pub/Sub, Confluent Cloud), schema registries (Confluent Schema Registry, Apicurio Registry), and streaming-analytics SaaS (Tinybird, Materialize). Wire-level protocols included are MQTT (OASIS), AMQP (OASIS / ISO 19464), and STOMP.
examples:
- key_count: 17
  name: Events Event Source Descriptor Example
  slug: events-event-source-descriptor-example
- key_count: 13
  name: Events Event Subscription Descriptor Example
  slug: events-event-subscription-descriptor-example
- key_count: 8
  name: Events Github Pull Request Opened Cloudevent Example
  slug: events-github-pull-request-opened-cloudevent-example
- key_count: 8
  name: Events Kafka Binary Mode Cloudevent Example
  slug: events-kafka-binary-mode-cloudevent-example
- key_count: 8
  name: Events Mqtt Iot Telemetry Cloudevent Example
  slug: events-mqtt-iot-telemetry-cloudevent-example
- key_count: 9
  name: Events Order Placed Cloudevent Example
  slug: events-order-placed-cloudevent-example
- key_count: 8
  name: Events S3 Object Created Cloudevent Example
  slug: events-s3-object-created-cloudevent-example
features:
- description: Many-to-many fan-out where producers publish to a topic and any number of subscribers receive a copy. Core to MQTT, NATS, Google Pub/Sub, Kafka (consumer-group fan-out), and EventBridge.
  name: Pub Sub Messaging
- description: Point-to-point work distribution where each message is consumed by exactly one worker. Native to IBM MQ, RabbitMQ (AMQP 0-9-1), Pulsar shared subscriptions, and NATS queue groups.
  name: Queue Messaging
- description: Durable, ordered, partitioned commit log that consumers read by offset. Kafka and Redpanda are the canonical implementations; Pulsar and Pub/Sub Lite share many properties.
  name: Log Based Streaming
- description: Schema registries (Confluent, Apicurio) version event schemas and enforce compatibility rules so producers cannot break consumers.
  name: Schema Governance
- description: Standard required attributes (id, source, specversion, type) plus optional (datacontenttype, dataschema, subject, time) wrap any event payload, with bindings for HTTP, Kafka, AMQP, MQTT, NATS, WebSockets, JSON, Avro, and Protobuf.
  name: CloudEvents Envelope
- description: AsyncAPI documents describe the channels, operations, messages, and bindings of an event-driven API the way OpenAPI describes a REST API.
  name: AsyncAPI Description
graphqls:
- description: ''
  name: Events GraphQL API
  slug: events-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/events.png
integrations:
- description: Common envelope adopted across Azure Event Grid, Knative, GitHub Webhooks (via cloudevents-go binding), and most CNCF event-emitting projects.
  name: CloudEvents
- description: API description format used by Postman, Microcks, Apicurio, and numerous broker dashboards to render an event API surface.
  name: AsyncAPI
- description: De facto wire protocol; supported natively by Confluent Cloud, Redpanda, Aiven, and (via proxies) Azure Event Hubs and Pulsar.
  name: Kafka Protocol
- description: Native protocol for Azure Event Grid namespaces, AWS IoT Core, HiveMQ, EMQX, and Mosquitto.
  name: MQTT
- description: Confluent Schema Registry and Apicurio Registry plug into Kafka serializers/deserializers in every major language client.
  name: Schema Registry
json_schemas:
- name: CloudEvent
  property_count: 10
  slug: events-cloudevent
- name: Event Source
  property_count: 17
  slug: events-event-source
- name: Event Subscription
  property_count: 16
  slug: events-event-subscription
jsonld:
- class_count: 26
  name: Events Context
  property_count: 18
  slug: events-context
layout: provider
modified: '2026-05-22'
name: Events
nav: Providers
network: true
overview: 'Events publishes 18 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Events, Event-Driven, Event Streaming, Messaging, and Pub Sub.


  The Events catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Events'' developer surface includes developer portal and 4 more developer resources.'
random_paper: 96
rules:
- name: Events API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: events-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 17.7
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 20.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/events/refs/heads/main/screenshots/events-2026-06-20T180902.png
security:
- kind: domain-security
  name: Events Domain Security
  slug: events-domain-security
  summary_line: TLSv1.3 · HSTS
slug: events
solutions:
- description: Apache Kafka, Apache Pulsar, NATS, Redpanda Community Edition, and RabbitMQ cover most self-hosted deployments.
  name: Open Source Brokers
- description: AWS EventBridge, Azure Event Grid, and Google Cloud Pub/Sub provide serverless, pay-per-event delivery within their respective clouds.
  name: Managed Cloud Buses
- description: Confluent Cloud, Redpanda Cloud, Aiven for Kafka, and Tinybird offer fully managed Kafka or ClickHouse with their own consoles, APIs, and SLAs.
  name: Managed Streaming SaaS
- description: CloudEvents (envelope), AsyncAPI (API description), and JSON Schema / Avro / Protobuf (payload schema) compose into the standards layer that brokers and registries implement.
  name: Specification Stack
tags:
- Events
- Event-Driven
- Event Streaming
- Messaging
- Pub Sub
- Brokers
- CloudEvents
- AsyncAPI
- Topic
use_cases:
- description: Decoupling services so producers emit events without coupling to downstream consumers.
  name: Microservice Integration
- description: Replicating database changes (Postgres logical replication, MySQL binlog, MongoDB change streams) onto Kafka, Pulsar, or Materialize for downstream consumers.
  name: Change Data Capture
- description: Constrained devices publishing readings over MQTT or NATS to cloud gateways such as Azure Event Grid or AWS IoT Core.
  name: IoT Telemetry
- description: Streaming events into ClickHouse-, Pinot-, or Druid-based platforms (Tinybird, Materialize) to power user-facing dashboards with sub-second freshness.
  name: Real Time Analytics
- description: Storing every state change as an immutable event in a durable log (Kafka, Pulsar) so application state can be rebuilt by replay.
  name: Event Sourcing
- description: HTTP-based fan-out from a SaaS to subscriber URLs. The narrowest slice of the event landscape; covered in detail in the api-evangelist webhooks topic repo.
  name: Webhook Delivery
---
