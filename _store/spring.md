---
aid: spring
url: https://raw.githubusercontent.com/api-evangelist/spring/refs/heads/main/apis.yml
apis:
- name: Spring Boot
  description: API for building production-ready Spring applications.
  image: https://spring.io/img/projects/spring-boot.svg
  humanUrl: https://spring.io/projects/spring-boot
  baseUrl: https://api.spring.io/boot
  tags:
  - Framework
  - Java
  - Microservices
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-boot/docs/current/reference/html/
  - type: OpenAPI
    url: https://docs.spring.io/spring-boot/docs/current/actuator-api/openapi.yaml
  - type: GitHub
    url: https://github.com/spring-projects/spring-boot
  - type: Getting Started
    url: https://spring.io/guides/gs/spring-boot/
  contact:
  - type: Support
    url: https://spring.io/support
- name: Spring Data REST
  description: RESTful API exposure for Spring Data repositories.
  humanUrl: https://spring.io/projects/spring-data-rest
  baseUrl: https://api.spring.io/data/rest
  tags:
  - Crud
  - Data
  - Rest
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/
  - type: API Reference
    url: https://docs.spring.io/spring-data/rest/docs/current/api/
  - type: GitHub
    url: https://github.com/spring-projects/spring-data-rest
  - type: HAL Browser
    url: https://docs.spring.io/spring-data/rest/docs/current/reference/html/#tools.hal-explorer
- name: Spring Cloud Gateway
  description: API Gateway built on Spring Framework.
  humanUrl: https://spring.io/projects/spring-cloud-gateway
  baseUrl: https://api.spring.io/gateway
  tags:
  - Cloud
  - Gateway
  - Routing
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-gateway
  - type: Samples
    url: https://github.com/spring-cloud/spring-cloud-gateway/tree/main/spring-cloud-gateway-sample
- name: Spring Security OAuth
  description: OAuth2 and OpenID Connect support for Spring applications.
  humanUrl: https://spring.io/projects/spring-security-oauth
  baseUrl: https://api.spring.io/oauth
  tags:
  - Authentication
  - Oauth
  - Security
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html
  - type: GitHub
    url: https://github.com/spring-projects/spring-security
  - type: OAuth2 Guide
    url: https://spring.io/guides/tutorials/spring-boot-oauth2/
- name: Spring Initializr API
  description: API for generating Spring Boot projects.
  humanUrl: https://start.spring.io
  baseUrl: https://start.spring.io/api
  tags:
  - Bootstrap
  - Generator
  - Tooling
  properties:
  - type: API Documentation
    url: https://docs.spring.io/initializr/docs/current/reference/html/
  - type: OpenAPI
    url: https://start.spring.io/v3/api-docs
  - type: GitHub
    url: https://github.com/spring-io/initializr
  - type: Web Interface
    url: https://start.spring.io
name: Spring Framework APIs
tags:
- Cloud
- Enterprise
- Framework
- Java
- Microservices
- Rest
type: Contract
image: https://spring.io/img/spring-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs and resources for the Spring Framework ecosystem.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

