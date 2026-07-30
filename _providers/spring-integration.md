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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 2
  name: Spring Integration Agentic Access
  operation_count: 14
  slug: spring-integration-agentic-access
  summary_line: 14 operations · 5 acting · 2 human-in-the-loop
api_count: 10
apis:
- description: AMQP channel adapters and gateways for Spring Integration. Provides RabbitMQ message-driven and polling inbound adapters, outbound channel adapters, and request/reply gateways.
  name: Spring Integration AMQP Adapter
  slug: spring-integration-amqp
- description: Kafka channel adapters for Spring Integration. Provides message-driven inbound adapters, outbound channel adapters, and request/reply gateways for Apache Kafka integration.
  name: Spring Integration Kafka Adapter
  slug: spring-integration-kafka
- description: The Adapters API from Spring Integration — 2 operation(s) for adapters.
  name: Spring Integration Adapters API
  slug: spring-integration-adapters-api
- description: The Channels API from Spring Integration — 2 operation(s) for channels.
  name: Spring Integration Channels API
  slug: spring-integration-channels-api
- description: The Control API from Spring Integration — 1 operation(s) for control.
  name: Spring Integration Control API
  slug: spring-integration-control-api
- description: The Gateway API from Spring Integration — 2 operation(s) for gateway.
  name: Spring Integration Gateway API
  slug: spring-integration-gateway-api
- description: The Graph API from Spring Integration — 1 operation(s) for graph.
  name: Spring Integration Graph API
  slug: spring-integration-graph-api
- description: The Handlers API from Spring Integration — 2 operation(s) for handlers.
  name: Spring Integration Handlers API
  slug: spring-integration-handlers-api
- description: The History API from Spring Integration — 1 operation(s) for history.
  name: Spring Integration History API
  slug: spring-integration-history-api
- description: The Inbound Adapter API from Spring Integration — 1 operation(s) for inbound adapter.
  name: Spring Integration Inbound Adapter API
  slug: spring-integration-inbound-adapter-api
artifact_total: 24
collections:
- collection_type: open
  name: Spring Integration HTTP Inbound Gateway API
  slug: open-spring-integration-http
- collection_type: open
  name: Spring Integration Management API
  slug: open-spring-integration-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-integration-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-integration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-integration-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spring.io/projects/spring-integration
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spring.io/spring-integration/reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spring-projects/spring-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://spring.io/guides/gs/integration
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spring-integration
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework.integration
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-projects/spring-integration/releases
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog/category/integration
- group: build
  title: ''
  type: Sample Projects
  url: https://github.com/spring-projects/spring-integration-samples
created: '2026-03-27'
description: Spring Integration extends the Spring programming model to support enterprise integration patterns (EIP), providing lightweight messaging within Spring-based applications and integration with external systems via declarative adapters. It supports message channels, filters, transformers, routers, aggregators, and a wide range of inbound/outbound adapters for HTTP, JMS, AMQP, TCP, FTP, JDBC, email, and many more.
examples:
- key_count: 4
  name: Spring Integration Get Graph Example
  slug: spring-integration-get-graph-example
finops:
- name: Spring Integration Finops
  service_category: API
  slug: spring-integration-finops
image: https://spring.io/img/projects/spring-integration.svg
json_schemas:
- name: Spring Integration Message
  property_count: 2
  slug: spring-integration-message
json_structures:
- name: Spring Integration Channel Structure
  property_count: 0
  slug: spring-integration-channel-structure
jsonld:
- class_count: 3
  name: Spring Integration Context
  property_count: 21
  slug: spring-integration-context
layout: provider
modified: '2026-05-19'
name: Spring Integration
nav: Providers
network: true
overview: 'Spring Integration publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Adapters API, Channels API, Control API, and 5 more. Tagged areas include AMQP, Enterprise Integration, Event-Driven, Integration Patterns, and Java.


  The Spring Integration catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Integration''s developer surface includes documentation, getting-started guide, Stack Overflow tag, release notes, engineering blog, and 7 more developer resources.'
plans:
- name: Spring Integration Plans Pricing
  plan_count: 3
  slug: spring-integration-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Spring Integration Rate Limits
  slug: spring-integration-rate-limits
rules:
- name: Spring Integration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-integration-jsonschema-spectral-rules
- name: Spring Integration API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: spring-integration-rules
score:
  band: developing
  composite: 43.3
  delta: -7.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.8
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-integration/refs/heads/main/screenshots/spring-integration-2026-06-20T194414.png
security:
- kind: domain-security
  name: Spring Integration Domain Security
  slug: spring-integration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Integration Vulnerability Disclosure
  slug: spring-integration-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-integration
tags:
- AMQP
- Enterprise Integration
- Event-Driven
- Integration Patterns
- Java
- Messaging
- Spring
website: https://spring.io/projects/spring-integration
---
