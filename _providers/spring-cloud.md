---
access_model:
  confidence: medium
  label: Enterprise · Open access
  onboarding: open
  pricing: enterprise
  public: true
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Spring Cloud Agentic Access
  operation_count: 9
  slug: spring-cloud-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 9
apis:
- description: Externalized configuration management backed by Git, providing server and client-side support for configuration in distributed systems with encryption, refresh, and multi-environment support.
  name: Spring Cloud Config
  slug: spring-cloud-config
- description: Service discovery using Netflix Eureka for registering and discovering microservices, providing self-registration, client-side discovery, heartbeat-based health checks, and zone-aware load balancing.
  name: Spring Cloud Netflix Eureka
  slug: spring-cloud-netflix-eureka
- description: Framework for building event-driven microservices connected with shared messaging systems including Apache Kafka and RabbitMQ with consumer groups and partitioning.
  name: Spring Cloud Stream
  slug: spring-cloud-stream
- description: Abstraction across different circuit breaker implementations including Resilience4J and Spring Retry, providing bulkhead, rate limiting, time limiting, and fallback patterns.
  name: Spring Cloud Circuit Breaker
  slug: spring-cloud-circuit-breaker
- description: Declarative REST client with support for Spring MVC annotations and HttpMessageConverters, providing load-balanced HTTP calls with Ribbon or Spring Cloud LoadBalancer integration.
  name: Spring Cloud OpenFeign
  slug: spring-cloud-openfeign
- description: Integration with Kubernetes providing service discovery via DNS and Kubernetes API, ConfigMap and Secret-backed property sources, and load balancing for Spring Boot applications deployed in Kubernetes
  name: Spring Cloud Kubernetes
  slug: spring-cloud-kubernetes
- description: The Filters API from Spring Cloud — 2 operation(s) for filters.
  name: Spring Cloud Filters API
  slug: spring-cloud-filters-api
- description: The Predicates API from Spring Cloud — 1 operation(s) for predicates.
  name: Spring Cloud Predicates API
  slug: spring-cloud-predicates-api
- description: The Routes API from Spring Cloud — 3 operation(s) for routes.
  name: Spring Cloud Routes API
  slug: spring-cloud-routes-api
artifact_total: 24
collections:
- collection_type: open
  name: Spring Cloud Gateway Actuator API
  slug: open-spring-cloud-gateway-actuator
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-cloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spring.io/projects/spring-cloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spring.io/spring-cloud/
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
  url: https://stackoverflow.com/questions/tagged/spring-cloud
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework.cloud
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spring-cloud-vocabulary.yml
created: '2024-01-15'
description: Spring Cloud provides tools for developers to quickly build some of the common patterns in distributed systems including configuration management, service discovery, circuit breakers, intelligent routing, micro-proxy, control bus, and distributed tracing. It builds on the Spring Boot approach to simplify microservice development and operations across cloud environments.
examples:
- key_count: 6
  name: Spring Cloud Circuit Breaker Example
  slug: spring-cloud-circuit-breaker-example
- key_count: 6
  name: Spring Cloud Eureka Registration Example
  slug: spring-cloud-eureka-registration-example
finops:
- name: Spring Cloud Finops
  service_category: Developer Tools
  slug: spring-cloud-finops
image: https://spring.io/img/spring-cloud.svg
json_schemas:
- name: Spring Cloud Configuration Properties
  property_count: 2
  slug: spring-cloud-config-properties
- name: Spring Cloud Service Instance
  property_count: 8
  slug: spring-cloud-service-instance
json_structures:
- name: Spring Cloud Service Registry Structure
  property_count: 0
  slug: spring-cloud-service-registry-structure
jsonld:
- class_count: 8
  name: Spring Cloud Context
  property_count: 9
  slug: spring-cloud-context
layout: provider
modified: '2026-05-19'
name: Spring Cloud
nav: Providers
network: true
overview: 'Spring Cloud publishes 3 APIs on the [APIs.io](https://apis.io/) network: Filters API, Predicates API, and Routes API. Tagged areas include Circuit Breaker, Cloud Native, Distributed Systems, Java, and Microservices.


  The Spring Cloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Cloud''s developer surface includes documentation, engineering blog, Stack Overflow tag, and 7 more developer resources.'
plans:
- name: Spring Cloud Plans Pricing
  plan_count: 1
  slug: spring-cloud-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 1
  name: Spring Cloud Rate Limits
  slug: spring-cloud-rate-limits
rules:
- name: Spring Cloud API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: spring-cloud-gateway-rules
- name: Spring Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-cloud-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.4
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.0
    developer_ergonomics: 10.9
    discoverability: 72.2
    governance: 31.3
    operational_transparency: 26.3
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-cloud/refs/heads/main/screenshots/spring-cloud-2026-06-20T194408.png
security:
- kind: domain-security
  name: Spring Cloud Domain Security
  slug: spring-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Cloud Vulnerability Disclosure
  slug: spring-cloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-cloud
tags:
- Circuit Breaker
- Cloud Native
- Distributed Systems
- Java
- Microservices
- Service Discovery
- Spring Framework
website: https://spring.io/projects/spring-cloud
---
