---
aid: webflux
name: Spring WebFlux
description: Spring WebFlux is a fully non-blocking, reactive-stack web framework built into Spring Framework 5.0+. It enables building highly scalable, asynchronous web applications using the Reactive Streams API with Project Reactor. WebFlux supports annotated controllers, functional routing endpoints, WebSocket communication, RSocket protocol, and a powerful reactive HTTP client (WebClient) for consuming APIs.
image: https://spring.io/img/projects/spring-framework.svg
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/webflux/refs/heads/main/apis.yml
apis:
  - name: Spring WebFlux Core
    description: Reactive web framework providing annotated controllers, functional endpoints, dispatcher handler, and the full reactive request/response processing pipeline. Supports non-blocking I/O with Reactor Mono and Flux types.
    image: https://spring.io/img/projects/spring-framework.svg
    humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux.html
    baseUrl: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/
    tags:
      - Annotated Controllers
      - Dispatcher Handler
      - Functional Endpoints
      - Non-Blocking
      - Reactive
      - Spring Framework
      - WebFlux
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/reference/web/webflux.html
      - type: API Reference
        url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/package-summary.html
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-framework/tree/main/spring-webflux
      - type: Getting Started
        url: https://spring.io/guides/gs/reactive-rest-service/
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework/spring-webflux
  - name: Spring WebFlux WebClient
    description: Reactive, non-blocking HTTP client for consuming REST services and other APIs. Supports builder-based configuration, request/response filters, error handling, streaming, and bridging to blocking operations. Replaces the deprecated RestTemplate.
    image: https://spring.io/img/projects/spring-framework.svg
    humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux-webclient.html
    tags:
      - HTTP Client
      - Non-Blocking
      - Reactive
      - REST
      - WebClient
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/reference/web/webflux-webclient.html
      - type: API Reference
        url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/reactive/function/client/WebClient.html
      - type: Tutorial
        url: https://www.baeldung.com/spring-5-webclient
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-framework/tree/main/spring-webflux
      - type: JSONSchema
        url: json-schema/webflux-webclient-request-schema.json
      - type: JSONSchema
        url: json-schema/webflux-webclient-response-schema.json
      - type: JSONStructure
        url: json-structure/webflux-webclient-request-structure.json
  - name: Spring WebFlux Router Functions
    description: Functional programming model for routing and request handling in WebFlux. RouterFunction and HandlerFunction provide a lightweight, lambda-based alternative to annotated controllers for defining HTTP endpoints.
    humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux-functional.html
    tags:
      - Functional Programming
      - Handler Functions
      - Reactive
      - Router Functions
      - Routing
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/reference/web/webflux-functional.html
      - type: Code Examples
        url: https://github.com/spring-projects/spring-framework/tree/main/spring-webflux/src/test/java/org/springframework/web/reactive/function
      - type: JSONSchema
        url: json-schema/webflux-router-function-schema.json
  - name: Spring WebFlux WebSocket
    description: Reactive WebSocket support for full-duplex, bidirectional communication in WebFlux applications. Provides WebSocketHandler, WebSocketSession, and integration with STOMP messaging protocol.
    humanUrl: https://docs.spring.io/spring-framework/reference/web/webflux-websocket.html
    tags:
      - Bidirectional
      - Full Duplex
      - Messaging
      - Real-Time
      - WebSocket
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/reference/web/webflux-websocket.html
      - type: Code Examples
        url: https://spring.io/guides/gs/messaging-stomp-websocket/
      - type: AsyncAPI
        url: asyncapi/webflux-websocket-asyncapi.yml
  - name: Spring WebFlux RSocket
    description: Integration with RSocket binary protocol for reactive, message-driven communication between microservices. Supports request-response, request-stream, fire-and-forget, and channel interaction models.
    humanUrl: https://docs.spring.io/spring-framework/reference/rsocket.html
    tags:
      - Binary Protocol
      - Microservices
      - Reactive
      - RSocket
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/reference/rsocket.html
      - type: API Reference
        url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/messaging/rsocket/package-summary.html
  - name: Reactor Core
    description: Project Reactor is the foundational reactive library powering Spring WebFlux. Provides Mono (0-1 element) and Flux (0-N element) publisher types implementing the Reactive Streams specification with composable operators.
    humanUrl: https://projectreactor.io/
    baseUrl: https://repo1.maven.org/maven2/io/projectreactor/reactor-core/
    tags:
      - Flux
      - Mono
      - Project Reactor
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
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/io.projectreactor/reactor-core
  - name: Spring WebFlux HTTP Service Client
    description: Declarative HTTP service interface client allowing annotation-based HTTP client definitions with @HttpExchange. Simplifies HTTP client creation with generated proxies backed by WebClient.
    humanUrl: https://docs.spring.io/spring-framework/reference/integration/rest-clients.html#rest-http-interface
    tags:
      - Declarative
      - HTTP Client
      - HTTP Interface
      - Reactive
      - REST
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/reference/integration/rest-clients.html#rest-http-interface
  - name: Spring WebFlux Testing
    description: Testing support for WebFlux applications including WebTestClient for integration testing of server endpoints, controller tests, and end-to-end testing with a full Spring application context.
    humanUrl: https://docs.spring.io/spring-framework/reference/testing/webtestclient.html
    tags:
      - Integration Testing
      - Reactive Testing
      - Spring Boot Test
      - Testing
      - WebTestClient
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/reference/testing/webtestclient.html
      - type: API Reference
        url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/test/web/reactive/server/WebTestClient.html
common:
  - type: Blog
    url: https://spring.io/blog/category/engineering
  - type: Support
    url: https://spring.io/support
  - type: Community
    url: https://spring.io/community
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-webflux
  - type: GitHub Organization
    url: https://github.com/spring-projects
  - type: Twitter
    url: https://twitter.com/springcentral
  - type: YouTube
    url: https://www.youtube.com/user/SpringSourceDev
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework/spring-webflux
  - type: Releases
    url: https://github.com/spring-projects/spring-framework/releases
  - type: Changelog
    url: https://github.com/spring-projects/spring-framework/wiki/Spring-Framework-Versions
  - type: JSONLD
    url: json-ld/webflux-context.jsonld
  - type: Vocabulary
    url: vocabulary/webflux-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
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
