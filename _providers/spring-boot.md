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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Spring Boot Agentic Access
  operation_count: 21
  slug: spring-boot-agentic-access
  summary_line: 21 operations · 4 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: RESTful web services built with Spring Boot using Spring MVC or Spring WebFlux. Supports JSON, XML, and hypermedia responses with full content negotiation, validation, error handling, and CORS configu
  name: Spring Boot REST API
  slug: spring-boot-rest-api
- description: Exposes Spring Data repositories as hypermedia-driven RESTful resources automatically. Supports HAL, collection+json media types, sorting, pagination, projections, and custom event handlers.
  name: Spring Data REST API
  slug: spring-data-rest
- description: Admin UI and monitoring tool for Spring Boot applications providing registration, health monitoring, log level management, JMX bean access, and notification capabilities for multiple application insta
  name: Spring Boot Admin API
  slug: spring-boot-admin
- description: The Application API from Spring Boot — 3 operation(s) for application.
  name: Spring Boot Application API
  slug: spring-boot-application-api
- description: The Caches API from Spring Boot — 2 operation(s) for caches.
  name: Spring Boot Caches API
  slug: spring-boot-caches-api
- description: The Configuration API from Spring Boot — 1 operation(s) for configuration.
  name: Spring Boot Configuration API
  slug: spring-boot-configuration-api
- description: The Environment API from Spring Boot — 2 operation(s) for environment.
  name: Spring Boot Environment API
  slug: spring-boot-environment-api
- description: The Health API from Spring Boot — 2 operation(s) for health.
  name: Spring Boot Health API
  slug: spring-boot-health-api
- description: The Info API from Spring Boot — 1 operation(s) for info.
  name: Spring Boot Info API
  slug: spring-boot-info-api
- description: The JVM API from Spring Boot — 2 operation(s) for jvm.
  name: Spring Boot JVM API
  slug: spring-boot-jvm-api
- description: The Lifecycle API from Spring Boot — 1 operation(s) for lifecycle.
  name: Spring Boot Lifecycle API
  slug: spring-boot-lifecycle-api
- description: The Loggers API from Spring Boot — 2 operation(s) for loggers.
  name: Spring Boot Loggers API
  slug: spring-boot-loggers-api
- description: The Metrics API from Spring Boot — 3 operation(s) for metrics.
  name: Spring Boot Metrics API
  slug: spring-boot-metrics-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spring Boot Actuator API
  slug: open-spring-boot-actuator
- collection_type: open
  name: Spring Boot Actuator Application API
  slug: open-spring-boot-application-api
- collection_type: open
  name: Spring Boot Actuator Application Caches API
  slug: open-spring-boot-caches-api
- collection_type: open
  name: Spring Boot Actuator Application Configuration API
  slug: open-spring-boot-configuration-api
- collection_type: open
  name: Spring Boot Actuator Application Environment API
  slug: open-spring-boot-environment-api
- collection_type: open
  name: Spring Boot Actuator Application Health API
  slug: open-spring-boot-health-api
- collection_type: open
  name: Spring Boot Actuator Application Info API
  slug: open-spring-boot-info-api
- collection_type: open
  name: Spring Boot Actuator Application JVM API
  slug: open-spring-boot-jvm-api
- collection_type: open
  name: Spring Boot Actuator Application Lifecycle API
  slug: open-spring-boot-lifecycle-api
- collection_type: open
  name: Spring Boot Actuator Application Loggers API
  slug: open-spring-boot-loggers-api
- collection_type: open
  name: Spring Boot Actuator Application Metrics API
  slug: open-spring-boot-metrics-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/codecentric/spring-boot-admin/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spring-boot-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spring-boot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spring-boot-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spring.io/spring-boot/
- group: company
  title: ''
  type: Website
  url: https://spring.io/projects/spring-boot
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spring-projects/spring-boot
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spring-projects
- group: operate
  title: ''
  type: Issues
  url: https://github.com/spring-projects/spring-boot/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-projects/spring-boot/releases
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spring-boot
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog/category/spring-boot
- group: docs
  title: ''
  type: Guides
  url: https://spring.io/guides
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework.boot/spring-boot
- group: other
  title: ''
  type: Maven Central
  url: https://search.maven.org/artifact/org.springframework.boot/spring-boot
- group: other
  title: ''
  type: Spring Initializr
  url: https://start.spring.io/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spring-boot-vocabulary.yml
created: '2024-01-01'
description: Spring Boot is an open source Java-based framework used to create stand-alone, production-grade Spring-based applications with minimal configuration. It provides auto-configuration, embedded server support, opinionated defaults, and production-ready features including health checks, metrics, and externalized configuration management.
examples:
- key_count: 6
  name: Spring Boot Actuator Get Health Example
  slug: spring-boot-actuator-get-health-example
- key_count: 6
  name: Spring Boot Actuator Get Metrics Example
  slug: spring-boot-actuator-get-metrics-example
- key_count: 6
  name: Spring Boot Actuator Set Logger Example
  slug: spring-boot-actuator-set-logger-example
finops:
- name: Spring Boot Finops
  service_category: API
  slug: spring-boot-finops
image: https://spring.io/img/spring-boot-logo.png
json_schemas:
- name: Spring Boot Actuator Health Response
  property_count: 3
  slug: spring-boot-actuator-health
- name: Spring Boot Actuator Metric Response
  property_count: 5
  slug: spring-boot-actuator-metric
- name: Spring Boot Application Configuration
  property_count: 4
  slug: spring-boot-application-properties
json_structures:
- name: Spring Boot Actuator Structure
  property_count: 0
  slug: spring-boot-actuator-structure
jsonld:
- class_count: 12
  name: Spring Boot Context
  property_count: 13
  slug: spring-boot-context
layout: provider
modified: '2026-05-19'
name: Spring Boot
nav: Providers
network: true
overview: 'Spring Boot publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Application API, Caches API, Configuration API, and 7 more. Tagged areas include Auto-Configuration, Embedded Server, Framework, Java, and Microservices.


  The Spring Boot catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spring Boot''s developer surface includes documentation, GitHub presence, release notes, Stack Overflow tag, engineering blog, and 12 more developer resources.'
plans:
- name: Spring Boot Plans Pricing
  plan_count: 3
  slug: spring-boot-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Spring Boot Rate Limits
  slug: spring-boot-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Spring Boot API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: spring-boot-actuator-rules
- effective_rule_count: 5
  extends: []
  name: Spring Boot API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spring-boot-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.2
  delta: 2.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 69.7
    contract_quality: 55.0
    developer_ergonomics: 21.4
    discoverability: 72.2
    governance: 69.7
    operational_transparency: 26.3
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spring-boot/refs/heads/main/screenshots/spring-boot-2026-06-20T194406.png
security:
- kind: domain-security
  name: Spring Boot Domain Security
  slug: spring-boot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spring Boot Vulnerability Disclosure
  slug: spring-boot-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spring-boot
tags:
- Auto-Configuration
- Embedded Server
- Framework
- Java
- Microservices
- REST API
- Spring
- Web Development
website: https://spring.io/projects/spring-boot
---
