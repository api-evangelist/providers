---
aid: webflux
url: https://raw.githubusercontent.com/api-evangelist/webflux/refs/heads/main/apis.yml
apis:
- name: Spring WebFlux Core API
  description: Reactive web framework for building non-blocking applications.
  image: https://spring.io/img/projects/spring-framework.svg
  humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux.html
  baseUrl: https://api.example.com/v1
  tags:
  - Microservices
  - Non-Blocking
  - Reactive
  - WebFlux
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html
  - type: OpenAPI
    url: https://api.example.com/v1/api-docs
  - type: Swagger UI
    url: https://api.example.com/swagger-ui.html
  - type: API Reference
    url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/package-summary.html
  - type: Getting Started
    url: https://spring.io/guides/gs/reactive-rest-service/
  - type: GitHub Repository
    url: https://github.com/spring-projects/spring-framework
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework/spring-webflux
- name: WebFlux Router Functions
  description: Functional routing and handler API for WebFlux.
  humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux-functional.html
  tags:
  - Functional Programming
  - Handlers
  - Routing
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-framework/reference/web/webflux-functional.html
  - type: Code Examples
    url: https://github.com/spring-projects/spring-framework/tree/main/spring-webflux/src/test/java/org/springframework/web/reactive/function
- name: WebFlux WebClient
  description: Reactive HTTP client for consuming REST services.
  humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux-webclient.html
  tags:
  - HTTP Client
  - Reactive
  - REST
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-framework/reference/web/webflux-webclient.html
  - type: API Reference
    url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.html
  - type: Tutorial
    url: https://www.baeldung.com/spring-5-webclient
- name: WebFlux WebSocket
  description: WebSocket support for reactive applications.
  humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux-websocket.html
  tags:
  - Bidirectional
  - Real-Time
  - WebSocket
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-framework/reference/web/webflux-websocket.html
  - type: Code Examples
    url: https://spring.io/guides/gs/messaging-stomp-websocket/
- name: Reactor Core
  description: Reactive library foundation for WebFlux.
  humanUrl: https://projectreactor.io/
  baseUrl: https://repo1.maven.org/maven2/io/projectreactor/reactor-core/
  tags:
  - Flux
  - Mono
  - Reactive Streams
  - Reactor
  properties:
  - type: Documentation
    url: https://projectreactor.io/docs/core/release/reference/
  - type: API Reference
    url: https://projectreactor.io/docs/core/release/api/
  - type: GitHub Repository
    url: https://github.com/reactor/reactor-core
  - type: Learning Materials
    url: https://projectreactor.io/learn
name: Spring WebFlux
tags:
- Java
- Microservices
- Non-Blocking IO
- Reactive Programming
- REST API
- Spring Framework
- WebFlux
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs and resources for Spring WebFlux reactive web framework.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

