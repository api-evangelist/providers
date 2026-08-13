---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: AsyncAPI specification for AMQP messaging patterns including publish/subscribe, request/reply, and point-to-point messaging via exchanges, queues, and bindings.
  name: AMQP Messaging API
  slug: amqp-messaging-api
artifact_total: 50
asyncapis:
- description: AsyncAPI specification for AMQP (Advanced Message Queuing Protocol) messaging patterns including publish/subscribe, request/reply, and point-to-point messaging. AMQP 0-9-1 defines exchanges, queues, a
  name: AMQP Messaging API
  slug: amqp-messaging
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amqp-domain-security.yml
- group: docs
  title: AMQP Message
  type: JSONSchema
  url: json-schema/amqp-message.json
- group: docs
  title: AMQP Message Properties
  type: JSONSchema
  url: json-schema/amqp-message-properties.json
- group: docs
  title: AMQP Exchange
  type: JSONSchema
  url: json-schema/amqp-exchange.json
- group: docs
  title: AMQP Queue
  type: JSONSchema
  url: json-schema/amqp-queue.json
- group: docs
  title: AMQP Binding
  type: JSONSchema
  url: json-schema/amqp-binding.json
- group: design
  title: AMQP JSON-LD Context
  type: JSONLD
  url: json-ld/amqp-context.jsonld
- group: start
  title: ''
  type: Portal
  url: https://www.amqp.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.amqp.org/resources/specifications
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amqp
- group: build
  title: Apache Qpid
  type: GitHubOrganization
  url: https://github.com/apache
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amqp-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amqp-exchange-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amqp-queue-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amqp-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amqp-vocabulary.yaml
created: '2025'
description: AMQP (Advanced Message Queuing Protocol) is an open standard for message-oriented middleware governed by OASIS and standardized as ISO/IEC 19464. AMQP 1.0 enables interoperable, asynchronous communication between applications across different platforms and vendors. It defines a wire-level protocol supporting reliable queuing, flexible routing, publish/subscribe, and request/reply messaging patterns. Major implementations include Apache ActiveMQ/Artemis, RabbitMQ, Azure Service Bus, Red Hat AMQ, and Apache Qpid.
examples:
- key_count: 5
  name: Amqp Binding Example
  slug: amqp-binding-example
- key_count: 6
  name: Amqp Exchange Example
  slug: amqp-exchange-example
- key_count: 7
  name: Amqp Message Example
  slug: amqp-message-example
- key_count: 14
  name: Amqp Message Properties Example
  slug: amqp-message-properties-example
- key_count: 5
  name: Amqp Queue Example
  slug: amqp-queue-example
features:
- description: Guaranteed delivery with acknowledgment and persistence support.
  name: Reliable Messaging
- description: Exchange types (direct, fanout, topic, headers) for flexible message routing.
  name: Flexible Routing
- description: Fan-out delivery to multiple consumers via topic and fanout exchanges.
  name: Publish/Subscribe
- description: Synchronous RPC patterns over asynchronous messaging infrastructure.
  name: Request/Reply
- description: Transactional message publishing and acknowledgment for data consistency.
  name: Transaction Support
- description: SASL authentication and TLS encryption for secure message transport.
  name: Security
- description: Credit-based flow control preventing consumer overload (AMQP 1.0).
  name: Flow Control
- description: Wire-level protocol interoperability across different broker implementations.
  name: Multi-Vendor Interoperability
finops:
- name: Amqp Finops
  service_category: API
  slug: amqp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amqp.png
integrations:
- description: Popular AMQP 0-9-1 compliant broker with extensive plugin ecosystem.
  name: RabbitMQ
- description: Java-based message broker supporting AMQP 1.0 and multiple protocols.
  name: Apache ActiveMQ
- description: Microsoft's cloud messaging service with AMQP 1.0 support.
  name: Azure Service Bus
- description: AMQP 1.0 implementation with broker and client library support.
  name: Apache Qpid
- description: Enterprise messaging platform based on ActiveMQ Artemis with AMQP 1.0.
  name: Red Hat AMQ
- description: Enterprise event broker supporting AMQP 1.0 among multiple protocols.
  name: Solace PubSub+
json_schemas:
- name: AMQP Binding
  property_count: 5
  slug: amqp-binding
- name: AMQP Exchange
  property_count: 6
  slug: amqp-exchange
- name: AMQP Message Properties
  property_count: 14
  slug: amqp-message-properties
- name: AMQP Message
  property_count: 7
  slug: amqp-message
- name: AMQP Queue
  property_count: 5
  slug: amqp-queue
json_structures:
- name: Amqp Binding Structure
  property_count: 5
  slug: amqp-binding-structure
- name: Amqp Exchange Structure
  property_count: 6
  slug: amqp-exchange-structure
- name: Amqp Message Properties Structure
  property_count: 14
  slug: amqp-message-properties-structure
- name: Amqp Message Structure
  property_count: 7
  slug: amqp-message-structure
- name: Amqp Queue Structure
  property_count: 5
  slug: amqp-queue-structure
jsonld:
- class_count: 1
  name: Amqp Amqp Binding Context
  property_count: 5
  slug: amqp-amqp-binding-context
- class_count: 1
  name: Amqp Amqp Exchange Context
  property_count: 6
  slug: amqp-amqp-exchange-context
- class_count: 1
  name: Amqp Amqp Message Context
  property_count: 7
  slug: amqp-amqp-message-context
- class_count: 1
  name: Amqp Amqp Message Properties Context
  property_count: 14
  slug: amqp-amqp-message-properties-context
- class_count: 1
  name: Amqp Amqp Queue Context
  property_count: 5
  slug: amqp-amqp-queue-context
- class_count: 0
  name: Amqp Context
  property_count: 9
  slug: amqp-context
layout: provider
modified: '2026-04-19'
name: AMQP
nav: Providers
network: true
overview: 'AMQP publishes 1 API on the [APIs.io](https://apis.io/) network: Messaging API. Tagged areas include AMQP, Asynchronous, Message Queue, Messaging, and Middleware.


  The AMQP catalog on APIs.io includes 1 event-driven AsyncAPI specification, 6 JSON-LD contexts, and 3 Spectral governance rulesets.


  AMQP''s developer surface includes developer portal, documentation, and 14 more developer resources.'
plans:
- name: Amqp Plans Pricing
  plan_count: 3
  slug: amqp-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Amqp Rate Limits
  slug: amqp-rate-limits
rules:
- name: AMQP API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 7
  slug: amqp-asyncapi-spectral-rules
- name: AMQP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amqp-jsonschema-spectral-rules
- name: AMQP API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: amqp-spectral-rules
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 59.3
    developer_ergonomics: 17.4
    discoverability: 66.7
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 38.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amqp/refs/heads/main/screenshots/amqp-2026-06-20T171940.png
security:
- kind: domain-security
  name: Amqp Domain Security
  slug: amqp-domain-security
  summary_line: TLSv1.3
slug: amqp
tags:
- AMQP
- Asynchronous
- Message Queue
- Messaging
- Middleware
- Open Standard
- Publish Subscribe
use_cases:
- description: Decoupled inter-service messaging in microservices architectures.
  name: Microservices Communication
- description: Event-driven architecture with durable, ordered event delivery.
  name: Event Streaming
- description: Distributed work queues for background job processing.
  name: Task Queues
- description: Device-to-cloud and cloud-to-device messaging for IoT platforms.
  name: IoT Messaging
- description: High-reliability financial transaction messaging with guaranteed delivery.
  name: Financial Messaging
- description: Centralized log collection and routing from distributed systems.
  name: Log Aggregation
website: https://www.amqp.org/
---
