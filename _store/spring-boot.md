---
aid: spring-boot
url: https://raw.githubusercontent.com/api-evangelist/spring-boot/refs/heads/main/apis.yml
apis:
- name: Spring Boot Actuator API
  description: Production-ready features to help monitor and manage Spring Boot applications.
  image: https://spring.io/img/spring-boot-logo.png
  humanUrl: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
  baseUrl: http://localhost:8080/actuator
  tags:
  - Health Check
  - Management
  - Metrics
  - Monitoring
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/
  - type: OpenAPI
    url: openapi/spring-boot-actuator-openapi.yml
  - type: Health Endpoint
    url: http://localhost:8080/actuator/health
  - type: Metrics Endpoint
    url: http://localhost:8080/actuator/metrics
  - type: Info Endpoint
    url: http://localhost:8080/actuator/info
  - type: JSONSchema
    url: json-schema/spring-boot-application-properties.json
- name: Spring Boot REST API
  description: RESTful web services built with Spring Boot.
  humanUrl: https://spring.io/guides/gs/rest-service/
  baseUrl: http://localhost:8080/api
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
- name: Spring Data REST API
  description: Exposes Spring Data repositories as hypermedia-driven RESTful resources.
  humanUrl: https://spring.io/projects/spring-data-rest
  baseUrl: http://localhost:8080/
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
- name: Spring Boot Admin API
  description: Admin UI and monitoring tool for Spring Boot applications.
  humanUrl: https://github.com/codecentric/spring-boot-admin
  baseUrl: http://localhost:8080/admin
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
name: Spring Boot
tags:
- Framework
- Java
- Microservices
- REST API
- Spring
- Web Development
type: Contract
image: https://spring.io/img/spring-boot-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs and resources for Spring Boot framework.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

