---
aid: spring
name: Spring Framework
description: Spring is the leading open-source application framework for Java. The Spring ecosystem provides a comprehensive programming and configuration model for modern Java-based enterprise applications, covering web MVC, data access, security, messaging, cloud-native patterns, and AI integrations. Spring Boot enables rapid application development with embedded servers and auto-configuration. Spring is maintained by VMware and hosted under the Spring Projects GitHub organization.
image: https://spring.io/img/spring-logo.svg
url: https://spring.io
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - name: Spring Boot Actuator API
    description: The Spring Boot Actuator API provides production-ready endpoints for monitoring and managing Spring Boot applications. It exposes health checks, metrics, environment information, thread dumps, HTTP traces, and application info via REST endpoints. The Actuator API is OpenAPI-documented and follows standard HTTP REST conventions.
    image: https://spring.io/img/projects/spring-boot.svg
    humanUrl: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
    baseUrl: https://api.spring.io/boot/actuator
    tags:
      - Monitoring
      - Actuator
      - Operations
      - Spring Boot
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
      - type: OpenAPI
        url: openapi/spring-boot-actuator-openapi.yml
      - type: GitHub
        url: https://github.com/spring-projects/spring-boot
      - type: GettingStarted
        url: https://spring.io/guides/gs/spring-boot/
      - type: JSONSchema
        url: json-schema/spring-actuator-health-schema.json
      - type: SpectralRules
        url: rules/spring-rules.yml
      - type: Vocabulary
        url: vocabulary/spring-vocabulary.yml
    contact:
      - type: Support
        url: https://spring.io/support
  - name: Spring Initializr API
    description: The Spring Initializr REST API enables programmatic generation of Spring Boot project scaffolding. It provides endpoints for listing available dependencies, project types, and boot versions, as well as generating ready-to-use project archives in zip or tar.gz format. Used by IDEs (IntelliJ IDEA, Eclipse STS, VS Code) and CLI tools to bootstrap new Spring projects.
    humanUrl: https://start.spring.io
    baseUrl: https://start.spring.io
    tags:
      - Bootstrap
      - Code Generation
      - Developer Tools
      - Project Generator
    properties:
      - type: Documentation
        url: https://docs.spring.io/initializr/docs/current/reference/html/
      - type: OpenAPI
        url: openapi/spring-initializr-api-openapi.yml
      - type: OpenAPIUpstream
        url: https://start.spring.io/v3/api-docs
      - type: GitHub
        url: https://github.com/spring-io/initializr
      - type: WebInterface
        url: https://start.spring.io
      - type: JSONSchema
        url: json-schema/spring-boot-application-schema.json
      - type: JSONStructure
        url: json-structure/spring-boot-application-structure.json
      - type: JSONLD
        url: json-ld/spring-context.jsonld
  - name: Spring Data REST API
    description: Spring Data REST automatically exports Spring Data repository interfaces as RESTful hypermedia-driven APIs using HAL (Hypertext Application Language). It enables CRUD operations on domain entities through discoverable REST endpoints without writing controller code. The API supports HATEOAS linking, projections, validation, and event hooks.
    humanUrl: https://spring.io/projects/spring-data-rest
    baseUrl: https://api.spring.io/data/rest
    tags:
      - CRUD
      - Data
      - HATEOAS
      - Hypermedia
      - REST
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
      - type: APIReference
        url: https://docs.spring.io/spring-data/rest/docs/current/api/
      - type: GitHub
        url: https://github.com/spring-projects/spring-data-rest
      - type: HALBrowser
        url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/#tools.hal-explorer
  - name: Spring Cloud Gateway API
    description: Spring Cloud Gateway provides an API Gateway built on Spring WebFlux and Reactor. It offers route configuration, request/response filtering, load balancing, circuit breaking, rate limiting, and retry capabilities via a fluent Java DSL or YAML configuration. The Actuator endpoint exposes live route and filter information.
    humanUrl: https://spring.io/projects/spring-cloud-gateway
    baseUrl: https://api.spring.io/gateway
    tags:
      - API Gateway
      - Cloud
      - Load Balancing
      - Routing
      - Security
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-gateway
      - type: Samples
        url: https://github.com/spring-cloud/spring-cloud-gateway/tree/main/spring-cloud-gateway-sample
  - name: Spring Authorization Server API
    description: Spring Authorization Server provides a full OAuth 2.1 and OpenID Connect 1.0 authorization server implementation built on Spring Security. It supports authorization code flow, client credentials, device authorization, token introspection, and token revocation. Exposes standard OAuth 2 endpoints.
    humanUrl: https://spring.io/projects/spring-authorization-server
    baseUrl: https://api.spring.io/oauth
    tags:
      - Authorization
      - OAuth 2.0
      - OpenID Connect
      - Security
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-authorization-server/reference/
      - type: GitHub
        url: https://github.com/spring-projects/spring-authorization-server
      - type: OAuthGuide
        url: https://spring.io/guides/tutorials/spring-boot-oauth2/
  - name: Spring AI API
    description: Spring AI provides a Spring-friendly API and abstractions for building AI-powered applications. It offers a unified ChatClient API for interacting with AI models (OpenAI, Anthropic, Google Gemini, Ollama, and others), along with vector store integrations, prompt templates, output parsers, and function calling support. Follows portable, modular Spring design principles.
    humanUrl: https://spring.io/projects/spring-ai
    baseUrl: https://api.spring.io/ai
    tags:
      - AI
      - Chatbot
      - GenAI
      - LLM
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-ai/reference/
      - type: GitHub
        url: https://github.com/spring-projects/spring-ai
      - type: GettingStarted
        url: https://docs.spring.io/spring-ai/reference/getting-started.html
common:
  - type: Website
    url: https://spring.io
  - type: GitHub
    url: https://github.com/spring-projects
  - type: Documentation
    url: https://docs.spring.io
  - type: Blog
    url: https://spring.io/blog
  - type: Community
    url: https://spring.io/community
  - type: Guides
    url: https://spring.io/guides
  - type: Events
    url: https://spring.io/events
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework
  - type: Releases
    url: https://github.com/spring-projects/spring-framework/releases
maintainers:
  - name: Spring Team at VMware
    email: spring-team@vmware.com
    url: https://spring.io/team
tags:
  - AI
  - Cloud Native
  - Enterprise
  - Framework
  - Java
  - Microservices
  - Open Source
  - REST
  - Spring Boot
---
