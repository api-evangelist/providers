---
aid: spring-framework
name: Spring Framework
description: 'The Spring Framework provides a comprehensive programming and configuration model for modern Java-based enterprise applications on any kind of deployment platform. A key element of Spring is infrastructural support at the application level: Spring focuses on the "plumbing" of enterprise applications so that teams can focus on application-level business logic, without unnecessary ties to specific deployment environments. It includes modules for dependency injection, data access, web development, aspect-oriented programming, and more.'
type: Index
image: https://spring.io/img/spring-logo.svg
url: https://spring.io/projects/spring-framework
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - AOP
  - Dependency Injection
  - Enterprise
  - Framework
  - IoC
  - Java
  - Microservices
  - MVC
  - Spring Boot
apis:
  - aid: spring-framework:spring-initializr
    name: Spring Initializr API
    description: API for generating Spring Boot projects with customizable dependencies, build tool, language, and Java version. Provides metadata endpoints to discover available starters and configuration options.
    image: https://spring.io/img/spring-logo.svg
    humanURL: https://start.spring.io
    baseURL: https://start.spring.io
    tags:
      - Bootstrap
      - Code Generation
      - Configuration
      - Project Generation
    properties:
      - type: Documentation
        url: https://github.com/spring-io/start.spring.io
      - type: API Endpoint
        url: https://start.spring.io/
      - type: OpenAPI
        url: openapi/spring-initializr-openapi.yml
  - aid: spring-framework:spring-boot-actuator
    name: Spring Boot Actuator API
    description: Production-ready features for monitoring and managing Spring Boot applications. Exposes health checks, metrics, environment info, configuration properties, thread dumps, heap dumps, and logger configuration via HTTP endpoints.
    image: https://spring.io/img/spring-logo.svg
    humanURL: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
    baseURL: http://localhost:8080/actuator
    tags:
      - Health
      - Management
      - Metrics
      - Monitoring
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/
      - type: Reference
        url: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
  - aid: spring-framework:spring-mvc
    name: Spring MVC Web Framework
    description: Model-View-Controller web framework built on the Servlet API. Supports annotation-driven controllers, content negotiation, validation, data binding, file uploads, CORS, and exception handling in a flexible servlet container.
    image: https://spring.io/img/spring-logo.svg
    humanURL: https://docs.spring.io/spring-framework/docs/current/reference/html/web.html
    baseURL: http://localhost:8080
    tags:
      - Annotations
      - HTTP
      - MVC
      - REST
      - Web
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/docs/current/reference/html/web.html
      - type: API Reference
        url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/
      - type: Getting Started
        url: https://spring.io/guides/gs/serving-web-content/
  - aid: spring-framework:spring-webflux
    name: Spring WebFlux Reactive API
    description: Reactive-stack web framework for building non-blocking, event-driven web applications on top of Project Reactor. Supports annotated controllers and functional endpoints with reactive programming model.
    image: https://spring.io/img/spring-logo.svg
    humanURL: https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html
    baseURL: http://localhost:8080
    tags:
      - Non-Blocking
      - Reactive
      - Reactor
      - WebFlux
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html
      - type: API Reference
        url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/
      - type: Guide
        url: https://spring.io/guides/gs/reactive-rest-service/
common:
  - type: Website
    url: https://spring.io/projects/spring-framework
  - type: GitHub Organization
    url: https://github.com/spring-projects
  - type: GitHub Repository
    url: https://github.com/spring-projects/spring-framework
  - type: Blog
    url: https://spring.io/blog
  - type: Guides
    url: https://spring.io/guides
  - type: Quick Start
    url: https://spring.io/quickstart
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring
  - type: Twitter
    url: https://twitter.com/springcentral
  - type: YouTube
    url: https://www.youtube.com/user/SpringSourceDev
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework/spring-framework
  - type: Releases
    url: https://github.com/spring-projects/spring-framework/releases
  - type: Documentation
    url: https://docs.spring.io/spring-framework/docs/current/reference/html/
maintainers:
  - FN: VMware Broadcom Spring Team
    email: spring-projects@vmware.com
    url: https://spring.io/team
---
