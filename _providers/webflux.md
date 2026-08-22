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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.7
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: Reactive web framework providing annotated controllers, functional endpoints, dispatcher handler, and the full reactive request/response processing pipeline. Supports non-blocking I/O with Reactor Mon
  name: Spring WebFlux Core
  slug: spring-webflux-core
- description: Reactive, non-blocking HTTP client for consuming REST services and other APIs. Supports builder-based configuration, request/response filters, error handling, streaming, and bridging to blocking opera
  name: Spring WebFlux WebClient
  slug: spring-webflux-webclient
- description: 'Functional programming model for routing and request handling in WebFlux. RouterFunction and HandlerFunction provide a lightweight, lambda-based alternative to annotated controllers for defining HTTP '
  name: Spring WebFlux Router Functions
  slug: spring-webflux-router-functions
- description: Reactive WebSocket support for full-duplex, bidirectional communication in WebFlux applications. Provides WebSocketHandler, WebSocketSession, and integration with STOMP messaging protocol.
  name: Spring WebFlux WebSocket
  slug: spring-webflux-websocket
- description: Integration with RSocket binary protocol for reactive, message-driven communication between microservices. Supports request-response, request-stream, fire-and-forget, and channel interaction models.
  name: Spring WebFlux RSocket
  slug: spring-webflux-rsocket
- description: Project Reactor is the foundational reactive library powering Spring WebFlux. Provides Mono (0-1 element) and Flux (0-N element) publisher types implementing the Reactive Streams specification with co
  name: Reactor Core
  slug: reactor-core
- description: Declarative HTTP service interface client allowing annotation-based HTTP client definitions with @HttpExchange. Simplifies HTTP client creation with generated proxies backed by WebClient.
  name: Spring WebFlux HTTP Service Client
  slug: spring-webflux-http-service-client
- description: Testing support for WebFlux applications including WebTestClient for integration testing of server endpoints, controller tests, and end-to-end testing with a full Spring application context.
  name: Spring WebFlux Testing
  slug: spring-webflux-testing
artifact_total: 21
asyncapis:
- description: AsyncAPI specification describing WebSocket communication patterns for Spring WebFlux applications. Spring WebFlux provides reactive WebSocket support via WebSocketHandler and WebSocketSession, enabli
  name: Spring WebFlux WebSocket API
  slug: webflux-websocket-asyncapi
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/spring-projects/spring-framework/blob/main/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://spring.io/blog/category/engineering
- group: operate
  title: ''
  type: Support
  url: https://spring.io/support
- group: operate
  title: ''
  type: Community
  url: https://spring.io/community
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/spring-webflux
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spring-projects
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/springcentral
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/SpringSourceDev
- group: other
  title: ''
  type: Maven Repository
  url: https://mvnrepository.com/artifact/org.springframework/spring-webflux
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/spring-projects/spring-framework/releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-Versions
- group: design
  title: ''
  type: JSONLD
  url: json-ld/webflux-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/webflux-vocabulary.yml
created: '2024-01-01'
description: Spring WebFlux is a fully non-blocking, reactive-stack web framework built into Spring Framework 5.0+. It enables building highly scalable, asynchronous web applications using the Reactive Streams API with Project Reactor. WebFlux supports annotated controllers, functional routing endpoints, WebSocket communication, RSocket protocol, and a powerful reactive HTTP client (WebClient) for consuming APIs.
examples:
- key_count: 5
  name: Webflux Webclient Get Example
  slug: webflux-webclient-get-example
- key_count: 5
  name: Webflux Webclient Post Example
  slug: webflux-webclient-post-example
finops:
- name: Webflux Finops
  service_category: API
  slug: webflux-finops
image: https://spring.io/img/projects/spring-framework.svg
json_schemas:
- name: Spring WebFlux Router Function Configuration
  property_count: 3
  slug: webflux-router-function
- name: Spring WebFlux WebClient Request
  property_count: 10
  slug: webflux-webclient-request
- name: Spring WebFlux WebClient Response
  property_count: 6
  slug: webflux-webclient-response
json_structures:
- name: Webflux Webclient Request Structure
  property_count: 0
  slug: webflux-webclient-request-structure
jsonld:
- class_count: 0
  name: Webflux Context
  property_count: 24
  slug: webflux-context
layout: provider
modified: '2026-05-03'
name: Spring WebFlux
nav: Providers
network: true
overview: 'Spring WebFlux publishes 1 API on the [APIs.io](https://apis.io/) network: WebSocket. Tagged areas include Java, Microservices, Non-Blocking IO, Reactive Programming, and REST API.


  The Spring WebFlux catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Spring WebFlux''s developer surface includes engineering blog, support, Stack Overflow tag, YouTube channel, release notes, changelog, and 7 more developer resources.'
plans:
- name: Webflux Plans Pricing
  plan_count: 3
  slug: webflux-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Webflux Rate Limits
  slug: webflux-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Spring WebFlux API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: webflux-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Spring WebFlux API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: webflux-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.1
  delta: -6.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 64.4
    developer_ergonomics: 7.1
    discoverability: 55.6
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 39.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/webflux/refs/heads/main/screenshots/webflux-2026-06-20T201330.png
slug: webflux
tags:
- Java
- Microservices
- Non-Blocking IO
- Reactive Programming
- REST API
- Spring Boot
- Spring Framework
- WebFlux
---
