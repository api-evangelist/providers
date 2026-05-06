---
name: Spring Boot 3
description: Spring Boot 3 is the major release of the opinionated Spring application framework, now built on Spring Framework 6, requiring Java 17 baseline and Jakarta EE 10. It delivers native image support via GraalVM, improved observability with Micrometer tracing, and a modernized auto-configuration system. Spring Boot 3 simplifies the development of production-ready stand-alone Spring applications with embedded servers, health endpoints, and externalized configuration.
image: https://spring.io/img/spring-logo.svg
url: https://spring.io/projects/spring-boot
type: opensource
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Enterprise
  - Framework
  - Java
  - Microservices
  - REST API
  - Spring Boot
apis:
  - name: Spring Boot Actuator API
    description: Production-ready features for monitoring and managing Spring Boot 3 applications. Provides over 50 built-in endpoints exposing health status, metrics (Micrometer), environment properties, loggers, thread dumps, heap dumps, HTTP trace, and more via HTTP or JMX.
    humanURL: https://docs.spring.io/spring-boot/docs/3.2.x/reference/html/actuator.html
    baseURL: http://localhost:8080/actuator
    tags:
      - Health Check
      - Management
      - Metrics
      - Monitoring
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-boot/docs/3.2.x/reference/html/actuator.html
      - type: API Documentation
        url: https://docs.spring.io/spring-boot/docs/3.2.x/actuator-api/htmlsingle/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-boot
      - type: OpenAPI
        url: openapi/spring-boot-3-actuator-openapi.yml
      - type: Spectral Rules
        url: rules/spring-boot-3-rules.yml
  - name: Spring Boot Core Framework
    description: Core Spring Boot 3 framework providing auto-configuration, embedded server support (Tomcat, Jetty, Undertow), externalized configuration, profiles, and conditional bean registration.
    humanURL: https://docs.spring.io/spring-boot/docs/3.2.x/reference/html/
    baseURL: https://github.com/spring-projects/spring-boot
    tags:
      - Auto-Configuration
      - Embedded Server
      - Framework
      - Java
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-boot/docs/3.2.x/reference/html/
      - type: API Documentation
        url: https://docs.spring.io/spring-boot/docs/3.2.x/api/
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-boot
      - type: Getting Started
        url: https://spring.io/guides/gs/spring-boot/
      - type: Release Notes
        url: https://github.com/spring-projects/spring-boot/releases
      - type: Migration Guide
        url: https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide
      - type: Maven Central
        url: https://mvnrepository.com/artifact/org.springframework.boot/spring-boot
  - name: Spring Web MVC API
    description: Web MVC framework for building web applications and RESTful services with Spring Boot 3. Includes controllers, filters, interceptors, and content negotiation.
    humanURL: https://docs.spring.io/spring-framework/docs/6.1.x/reference/html/web.html
    baseURL: http://localhost:8080
    tags:
      - HTTP
      - MVC
      - REST
      - Web
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-framework/docs/6.1.x/reference/html/web.html
      - type: Tutorial
        url: https://spring.io/guides/gs/rest-service/
  - name: Spring Data REST API
    description: Automatically expose Spring Data repositories as hypermedia-driven REST resources using HAL. Integrates with Spring Data JPA, MongoDB, Neo4j, and other stores.
    humanURL: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
    baseURL: http://localhost:8080/api
    tags:
      - CRUD
      - Data
      - HAL
      - REST
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
      - type: API Documentation
        url: https://docs.spring.io/spring-data/rest/docs/current/api/
  - name: Spring Security API
    description: Security framework for authentication and authorization in Spring Boot 3 applications. Supports OAuth2, OIDC, SAML2, JWT, and method-level security.
    humanURL: https://docs.spring.io/spring-security/reference/
    baseURL: http://localhost:8080
    tags:
      - Authentication
      - Authorization
      - OAuth2
      - Security
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-security/reference/
      - type: API Documentation
        url: https://docs.spring.io/spring-security/site/docs/6.2.x/api/
      - type: OAuth2 Guide
        url: https://spring.io/guides/tutorials/spring-boot-oauth2/
maintainers:
  - name: VMware Tanzu (Broadcom)
    email: spring-team@vmware.com
    url: https://spring.io/team
common:
  - type: Getting Started
    url: https://spring.io/guides/gs/spring-boot/
  - type: GitHub Repository
    url: https://github.com/spring-projects/spring-boot
  - type: Release Notes
    url: https://github.com/spring-projects/spring-boot/releases
  - type: Migration Guide
    url: https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide
  - type: Community
    url: https://spring.io/community
  - type: Blog
    url: https://spring.io/blog
include:
  - name: Spring Framework
    url: https://spring.io/projects/spring-framework
  - name: Spring Cloud
    url: https://spring.io/projects/spring-cloud
  - name: Spring Data
    url: https://spring.io/projects/spring-data
---
