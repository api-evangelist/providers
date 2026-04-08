---
aid: spring-framework
url: https://raw.githubusercontent.com/api-evangelist/spring-framework/refs/heads/main/apis.yml
apis:
- name: Spring Framework Documentation API
  description: Official Spring Framework documentation and API reference.
  image: https://spring.io/img/spring-logo.svg
  humanURL: https://docs.spring.io/spring-framework/docs/current/reference/html/
  baseURL: https://docs.spring.io/spring-framework/docs/current/
  tags:
  - Documentation
  - Guides
  - Reference
  properties:
  - type: x-documentation
    url: https://docs.spring.io/spring-framework/docs/current/reference/html/
  - type: x-javadoc
    url: https://docs.spring.io/spring-framework/docs/current/javadoc-api/
  - type: x-github
    url: https://github.com/spring-projects/spring-framework
- name: Spring Initializr API
  description: API for generating Spring Boot projects with customizable dependencies and configurations.
  image: https://spring.io/img/spring-logo.svg
  humanURL: https://start.spring.io
  baseURL: https://start.spring.io/
  tags:
  - Bootstrap
  - Configuration
  - Project Generation
  properties:
  - type: x-api-endpoint
    url: https://start.spring.io/
  - type: x-documentation
    url: https://github.com/spring-io/start.spring.io
  - type: x-openapi
    url: https://start.spring.io/v2-schema.json
- name: Spring Boot Actuator API
  description: Production-ready features for monitoring and managing Spring Boot applications.
  image: https://spring.io/img/spring-logo.svg
  humanURL: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
  baseURL: http://localhost:8080/actuator
  tags:
  - Health
  - Management
  - Metrics
  - Monitoring
  properties:
  - type: x-documentation
    url: https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html
  - type: x-endpoints
    url: https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/
name: Spring Framework
tags:
- Dependency Injection
- Enterprise
- Framework
- IoC
- Java
- Microservices
- MVC
- Spring Boot
type: Contract
image: https://spring.io/img/spring-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Spring Framework provides a comprehensive programming and configuration model for modern Java-based enterprise applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

