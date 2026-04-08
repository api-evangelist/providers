---
aid: spring-boot-3
url: https://raw.githubusercontent.com/api-evangelist/spring-boot-3/refs/heads/main/apis.yml
apis:
- name: Spring Boot Core API
  description: Core Spring Boot 3 framework APIs for application development.
  image: https://spring.io/img/spring-boot-logo.svg
  humanUrl: https://docs.spring.io/spring-boot/docs/3.0.x/reference/html/
  baseUrl: https://api.example.com/v3
  tags:
  - Framework
  - Java
  - Microservices
  - REST
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-boot/docs/3.0.x/reference/html/
  - type: API Documentation
    url: https://docs.spring.io/spring-boot/docs/3.0.x/api/
  - type: OpenAPI
    url: https://api.example.com/v3/api-docs
  - type: Swagger UI
    url: https://api.example.com/swagger-ui.html
  contact:
  - type: GitHub
    url: https://github.com/spring-projects/spring-boot
  - type: Support
    url: https://spring.io/support
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-boot
- name: Spring Boot Actuator API
  description: Production-ready features for monitoring and managing Spring Boot applications.
  humanUrl: https://docs.spring.io/spring-boot/docs/3.0.x/reference/html/actuator.html
  baseUrl: https://api.example.com/actuator
  tags:
  - Health Check
  - Management
  - Metrics
  - Monitoring
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-boot/docs/3.0.x/reference/html/actuator.html
  - type: API Documentation
    url: https://docs.spring.io/spring-boot/docs/3.0.x/actuator-api/htmlsingle/
  - type: Endpoints
    url: https://api.example.com/actuator
  endpoints:
  - path: /health
    description: Application health information
  - path: /metrics
    description: Application metrics
  - path: /info
    description: Application information
  - path: /env
    description: Environment properties
  - path: /loggers
    description: Logger configuration
- name: Spring Web MVC API
  description: Web MVC framework for building web applications and RESTful services.
  humanUrl: https://docs.spring.io/spring-framework/docs/6.0.x/reference/html/web.html
  baseUrl: https://api.example.com/api
  tags:
  - HTTP
  - MVC
  - REST
  - Web
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-framework/docs/6.0.x/reference/html/web.html
  - type: Tutorial
    url: https://spring.io/guides/gs/rest-service/
  - type: OpenAPI
    url: https://api.example.com/v3/api-docs
- name: Spring Data REST API
  description: Automatically expose Spring Data repositories as REST resources.
  humanUrl: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
  baseUrl: https://api.example.com/api
  tags:
  - CRUD
  - Data
  - Repository
  - REST
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
  - type: API Documentation
    url: https://docs.spring.io/spring-data/rest/docs/current/api/
  - type: HAL Browser
    url: https://api.example.com/browser/
- name: Spring Security API
  description: Security framework for authentication and authorization.
  humanUrl: https://docs.spring.io/spring-security/reference/
  baseUrl: https://api.example.com/api
  tags:
  - Authentication
  - Authorization
  - OAuth2
  - Security
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-security/reference/
  - type: API Documentation
    url: https://docs.spring.io/spring-security/site/docs/6.0.x/api/
  - type: OAuth2 Guide
    url: https://spring.io/guides/tutorials/spring-boot-oauth2/
name: Spring Boot 3
tags:
- Enterprise
- Framework
- Java
- Microservices
- REST API
- Spring Boot
type: Contract
image: https://spring.io/img/spring-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Comprehensive collection of Spring Boot 3 framework APIs and resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

