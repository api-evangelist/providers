---
aid: spring-boot
name: Spring Boot
description: Spring Boot is an open source Java-based framework used to create stand-alone, production-grade Spring-based applications with minimal configuration. It provides auto-configuration, embedded server support, opinionated defaults, and production-ready features including health checks, metrics, and externalized configuration management.
image: https://spring.io/img/spring-boot-logo.png
url: https://spring.io/projects/spring-boot
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Auto Configuration
  - Embedded Server
  - Framework
  - Java
  - Microservices
  - REST API
  - Spring
  - Web Development
apis:
  - aid: spring-boot:spring-boot-actuator
    name: Spring Boot Actuator API
    description: Production-ready management and monitoring endpoints for Spring Boot applications. Provides health checks, metrics, environment info, configuration properties, thread dumps, heap dumps, logger configuration, cache management, and graceful shutdown.
    image: https://spring.io/img/spring-boot-logo.png
    humanURL: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
    baseURL: http://localhost:8080/actuator
    tags:
      - Actuator
      - Health Check
      - Management
      - Metrics
      - Monitoring
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/
      - type: OpenAPI
        url: openapi/spring-boot-actuator-openapi.yml
      - type: JSONSchema
        url: json-schema/spring-boot-actuator-health-schema.json
      - type: JSONSchema
        url: json-schema/spring-boot-actuator-metric-schema.json
      - type: JSONStructure
        url: json-structure/spring-boot-actuator-structure.json
      - type: JSONLDContext
        url: json-ld/spring-boot-context.jsonld
      - type: SpectralRules
        url: rules/spring-boot-actuator-rules.yml
      - type: NaftikoCapability
        url: capabilities/application-monitoring.yaml
  - aid: spring-boot:spring-boot-rest-api
    name: Spring Boot REST API
    description: RESTful web services built with Spring Boot using Spring MVC or Spring WebFlux. Supports JSON, XML, and hypermedia responses with full content negotiation, validation, error handling, and CORS configuration.
    humanURL: https://spring.io/guides/gs/rest-service/
    baseURL: http://localhost:8080/api
    tags:
      - HTTP
      - JSON
      - REST
      - Web Services
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-boot/docs/current/reference/html/web.html
      - type: Getting Started Guide
        url: https://spring.io/guides/gs/rest-service/
      - type: Tutorial
        url: https://spring.io/guides/tutorials/rest/
  - aid: spring-boot:spring-data-rest
    name: Spring Data REST API
    description: Exposes Spring Data repositories as hypermedia-driven RESTful resources automatically. Supports HAL, collection+json media types, sorting, pagination, projections, and custom event handlers.
    humanURL: https://spring.io/projects/spring-data-rest
    baseURL: http://localhost:8080/
    tags:
      - Database
      - HATEOAS
      - Repository
      - REST
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
      - type: API Guide
        url: https://docs.spring.io/spring-data/rest/docs/current/api/
      - type: Getting Started
        url: https://spring.io/guides/gs/accessing-data-rest/
  - aid: spring-boot:spring-boot-admin
    name: Spring Boot Admin API
    description: Admin UI and monitoring tool for Spring Boot applications providing registration, health monitoring, log level management, JMX bean access, and notification capabilities for multiple application instances.
    humanURL: https://github.com/codecentric/spring-boot-admin
    baseURL: http://localhost:8080/admin
    tags:
      - Administration
      - Dashboard
      - Management
      - Monitoring
    properties:
      - type: Documentation
        url: https://codecentric.github.io/spring-boot-admin/current/
      - type: GitHub Repository
        url: https://github.com/codecentric/spring-boot-admin
      - type: Getting Started
        url: https://codecentric.github.io/spring-boot-admin/current/#getting-started
common:
  - type: Documentation
    url: https://docs.spring.io/spring-boot/
  - type: Website
    url: https://spring.io/projects/spring-boot
  - type: GitHub
    url: https://github.com/spring-projects/spring-boot
  - type: GitHub Organization
    url: https://github.com/spring-projects
  - type: Issues
    url: https://github.com/spring-projects/spring-boot/issues
  - type: Releases
    url: https://github.com/spring-projects/spring-boot/releases
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-boot
  - type: Blog
    url: https://spring.io/blog/category/spring-boot
  - type: Guides
    url: https://spring.io/guides
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework.boot/spring-boot
  - type: Maven Central
    url: https://search.maven.org/artifact/org.springframework.boot/spring-boot
  - type: Spring Initializr
    url: https://start.spring.io/
  - type: Vocabulary
    url: vocabulary/spring-boot-vocabulary.yml
maintainers:
  - FN: VMware Tanzu (Spring Team)
    email: spring-boot@vmware.com
    url: https://spring.io/team
include:
  - name: Spring Framework
    url: https://spring.io/projects/spring-framework
  - name: Spring Cloud
    url: https://spring.io/projects/spring-cloud
  - name: Spring Data
    url: https://spring.io/projects/spring-data
---
