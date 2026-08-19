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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Core programmatic API for building message-driven microservice applications. Provides functional programming model with java.util.function.Function, Consumer and Supplier bindings, binding lifecycle m
  name: Spring Cloud Stream Core API
  slug: spring-cloud-stream-core
- description: Apache Kafka binder for Spring Cloud Stream providing Kafka producer and consumer binding configuration, Kafka Streams support, partitioning, transaction management, error handling, and dead-letter qu
  name: Spring Cloud Stream Kafka Binder
  slug: spring-cloud-stream-kafka-binder
- description: RabbitMQ binder for Spring Cloud Stream providing AMQP-based messaging with support for exchanges, queues, routing keys, dead-letter exchanges, consumer groups, and AMQP transaction management.
  name: Spring Cloud Stream RabbitMQ Binder
  slug: spring-cloud-stream-rabbitmq-binder
artifact_total: 14
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-cloud-stream-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-cloud-stream-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spring.io/projects/spring-cloud-stream
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spring.io/spring-cloud-stream/docs/current/reference/html/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spring-cloud/spring-cloud-stream
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spring-cloud
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog/category/cloud
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spring-cloud-stream
- group: operate
  title: ''
  type: Support
  url: https://spring.io/support
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spring-cloud-stream-vocabulary.yml
created: '2024-01-01'
description: Spring Cloud Stream is a framework for building event-driven microservices connected with shared messaging systems. It provides a flexible programming model built on established Spring idioms and best practices, including support for persistent pub/sub semantics, consumer groups, and stateful partitions with Apache Kafka and RabbitMQ binders.
examples:
- key_count: 5
  name: Spring Cloud Stream Kafka Binding Example
  slug: spring-cloud-stream-kafka-binding-example
- key_count: 4
  name: Spring Cloud Stream Rabbitmq Binding Example
  slug: spring-cloud-stream-rabbitmq-binding-example
finops:
- name: Spring Cloud Stream Finops
  service_category: API
  slug: spring-cloud-stream-finops
image: https://spring.io/img/projects/spring-cloud.svg
json_schemas:
- name: Spring Cloud Stream Binding Configuration
  property_count: 1
  slug: spring-cloud-stream-binding
json_structures:
- name: Spring Cloud Stream Binding Structure
  property_count: 0
  slug: spring-cloud-stream-binding-structure
jsonld:
- class_count: 7
  name: Spring Cloud Stream Context
  property_count: 9
  slug: spring-cloud-stream-context
layout: provider
modified: '2026-05-02'
name: Spring Cloud Stream
nav: Providers
network: true
overview: 'Spring Cloud Stream publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apache Kafka, AsyncAPI, Event-Driven, Java, and Messaging.


  The Spring Cloud Stream catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Spring Cloud Stream''s developer surface includes documentation, GitHub presence, engineering blog, Stack Overflow tag, support, and 5 more developer resources.'
plans:
- name: Spring Cloud Stream Plans Pricing
  plan_count: 3
  slug: spring-cloud-stream-plans-pricing
random_paper: 148
rate_limits:
- limit_count: 5
  name: Spring Cloud Stream Rate Limits
  slug: spring-cloud-stream-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Spring Cloud Stream API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: spring-cloud-stream-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.5
  delta: -6.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 19.7
    developer_ergonomics: 14.3
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 30.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-cloud-stream/refs/heads/main/screenshots/spring-cloud-stream-2026-06-20T194411.png
security:
- kind: domain-security
  name: Spring Cloud Stream Domain Security
  slug: spring-cloud-stream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Cloud Stream Vulnerability Disclosure
  slug: spring-cloud-stream-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-cloud-stream
tags:
- Apache Kafka
- AsyncAPI
- Event-Driven
- Java
- Messaging
- Microservices
- RabbitMQ
- Spring Framework
- Stream Processing
website: https://spring.io/projects/spring-cloud-stream
---
