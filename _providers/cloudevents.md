---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cloudevents Agentic Access
  operation_count: 5
  slug: cloudevents-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 12
apis:
- description: The CloudEvents specification defines a set of metadata attributes that must be present in every event, including source, type, id, and specversion. It provides a vendor-neutral way to describe events
  name: CloudEvents Specification
  slug: cloudevents-spec
- description: The HTTP protocol binding defines how CloudEvents are transported using HTTP, including structured content mode where the entire event is in the HTTP body, and binary content mode where event attribut
  name: CloudEvents HTTP Protocol Binding
  slug: cloudevents-http-binding
- description: The Kafka protocol binding for CloudEvents defines how events are mapped to Apache Kafka messages. It specifies how CloudEvents attributes are encoded as Kafka message headers and how the event payloa
  name: CloudEvents Kafka Protocol Binding
  slug: cloudevents-kafka-binding
- description: The AMQP protocol binding for CloudEvents defines how events are mapped to OASIS AMQP 1.0 messages. In structured content mode, event attributes and data are placed in the AMQP message application dat
  name: CloudEvents AMQP Protocol Binding
  slug: cloudevents-amqp-binding
- description: The MQTT protocol binding for CloudEvents defines how events are mapped to MQTT 3.1.1 and MQTT 5.0 messages. It supports both structured and binary content modes for IoT and constrained device environ
  name: CloudEvents MQTT Protocol Binding
  slug: cloudevents-mqtt-binding
- description: The NATS protocol binding for CloudEvents defines how events are mapped to NATS messages. It enables CloudEvents to be produced and consumed over the NATS messaging system, supporting both publish/sub
  name: CloudEvents NATS Protocol Binding
  slug: cloudevents-nats-binding
- description: CloudEvents SQL (CESQL) is a v1.0 specification that defines a standardized query language for filtering and routing CloudEvents based on their attributes. It provides a SQL-like syntax for writing ev
  name: CloudEvents SQL (CESQL)
  slug: cloudevents-cesql
- description: 'The official Go SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Go applications. It supports all CloudEvents protocol bindings and content modes, and includes client '
  name: CloudEvents Go SDK
  slug: cloudevents-sdk-go
- description: The official JavaScript SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Node.js and browser environments. It supports structured and binary content modes over HTTP an
  name: CloudEvents JavaScript SDK
  slug: cloudevents-sdk-javascript
- description: The official Java SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Java applications. It includes support for HTTP, Kafka, and other transports, and integrates with po
  name: CloudEvents Java SDK
  slug: cloudevents-sdk-java
- description: The official Python SDK for CloudEvents provides libraries for producing and consuming CloudEvents in Python applications. It supports HTTP transport bindings and both structured and binary content mo
  name: CloudEvents Python SDK
  slug: cloudevents-sdk-python
- description: Operations for creating and managing event delivery subscriptions. Each subscription specifies a source of events, optional filter criteria, and a sink where matched events are delivered.
  name: CloudEvents Subscriptions API
  slug: cloudevents-subscriptions-api
artifact_total: 30
asyncapis:
- description: 'AsyncAPI definition for CloudEvents delivery over HTTP. This document describes the event-driven interface by which a CloudEvents-compatible broker pushes events to a subscriber''s HTTP sink endpoint. '
  name: CloudEvents HTTP Delivery
  slug: cloudevents-http-asyncapi
collections:
- collection_type: open
  name: CloudEvents Subscriptions API
  slug: open-cloudevents-subscriptions
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudevents-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudevents-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudevents.io
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cloudevents/spec
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md
- group: company
  title: ''
  type: Blog
  url: https://cloudevents.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudevents
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudevents/spec/blob/main/cloudevents/SDK.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/cloudevents/spec/releases
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cloudevents-event-schema.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cloudevents-subscriptions-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/cloudevents-http-asyncapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudevents-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudevents-rules.yml
created: '2026-03-16'
description: CloudEvents is a CNCF graduated specification for describing event data in a common way. It provides a consistent format for event metadata across services, platforms, and systems, enabling interoperability between event producers and consumers. The specification includes protocol bindings for HTTP, AMQP, Kafka, MQTT, and NATS, along with SDKs in multiple languages.
finops:
- name: Cloudevents Finops
  service_category: Open Source Specification
  slug: cloudevents-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudevents.png
json_schemas:
- name: Error
  property_count: 2
  slug: cloudevents-error
- name: CloudEvent
  property_count: 10
  slug: cloudevents-event
- name: Filter
  property_count: 3
  slug: cloudevents-filter
- name: ProtocolSettings
  property_count: 3
  slug: cloudevents-protocolsettings
- name: Subscription
  property_count: 8
  slug: cloudevents-subscription
- name: SubscriptionRequest
  property_count: 7
  slug: cloudevents-subscriptionrequest
json_structures:
- name: Cloudevents Structure
  property_count: 0
  slug: cloudevents-structure
jsonld:
- class_count: 4
  name: Cloudevents Context
  property_count: 27
  slug: cloudevents-context
layout: provider
modified: '2026-05-19'
name: CloudEvents
nav: Providers
network: true
overview: 'CloudEvents publishes 2 APIs on the [APIs.io](https://apis.io/) network: Specification and Subscriptions API. Tagged areas include Cloud Native, Events, Graduated, Interoperability, and Messaging.


  The CloudEvents catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  CloudEvents'' developer surface includes documentation, getting-started guide, engineering blog, changelog, and 10 more developer resources.'
plans:
- name: Cloudevents Plans Pricing
  plan_count: 1
  slug: cloudevents-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 1
  name: Cloudevents Rate Limits
  slug: cloudevents-rate-limits
rules:
- name: CloudEvents API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: cloudevents-asyncapi-spectral-rules
- name: CloudEvents API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cloudevents-jsonschema-spectral-rules
- name: CloudEvents API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 6
  slug: cloudevents-rules
score:
  band: developing
  composite: 42.4
  delta: -8.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 72.3
    developer_ergonomics: 28.3
    discoverability: 72.2
    governance: 41.7
    operational_transparency: 42.1
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudevents/refs/heads/main/screenshots/cloudevents-2026-06-20T174548.png
security:
- kind: domain-security
  name: Cloudevents Domain Security
  slug: cloudevents-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cloudevents
tags:
- Cloud Native
- Events
- Graduated
- Interoperability
- Messaging
- Specification
website: https://cloudevents.io
---
