---
aid: spring-integration
name: Spring Integration
description: Spring Integration extends the Spring programming model to support enterprise integration patterns (EIP), providing lightweight messaging within Spring-based applications and integration with external systems via declarative adapters. It supports message channels, filters, transformers, routers, aggregators, and a wide range of inbound/outbound adapters for HTTP, JMS, AMQP, TCP, FTP, JDBC, email, and many more.
type: Index
image: https://spring.io/img/projects/spring-integration.svg
url: https://spring.io/projects/spring-integration
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - AMQP
  - Enterprise Integration
  - Event-Driven
  - Integration Patterns
  - Java
  - Messaging
  - Spring
apis:
  - aid: spring-integration:spring-integration-http
    name: Spring Integration HTTP Adapter API
    description: HTTP inbound and outbound channel adapters for Spring Integration. Provides HTTP request-response messaging, REST template integration, and configurable URL mapping for inbound HTTP gateways.
    humanURL: https://docs.spring.io/spring-integration/docs/current/reference/html/http.html
    baseURL: http://localhost:8080
    tags:
      - HTTP
      - Inbound
      - Messaging
      - Outbound
      - REST
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-integration/docs/current/reference/html/http.html
      - type: GitHub Repository
        url: https://github.com/spring-projects/spring-integration
      - type: OpenAPI
        url: openapi/spring-integration-http-openapi.yml
  - aid: spring-integration:spring-integration-management
    name: Spring Integration Management API
    description: Management and monitoring REST API for Spring Integration. Exposes channel statistics, handler metrics, component lifecycle control (start/stop), and message history configuration via HTTP endpoints.
    humanURL: https://docs.spring.io/spring-integration/docs/current/reference/html/management.html
    baseURL: http://localhost:8080/api
    tags:
      - Management
      - Messaging
      - Metrics
      - Monitoring
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-integration/docs/current/reference/html/management.html
      - type: OpenAPI
        url: openapi/spring-integration-management-openapi.yml
  - aid: spring-integration:spring-integration-amqp
    name: Spring Integration AMQP Adapter
    description: AMQP channel adapters and gateways for Spring Integration. Provides RabbitMQ message-driven and polling inbound adapters, outbound channel adapters, and request/reply gateways.
    humanURL: https://docs.spring.io/spring-integration/docs/current/reference/html/amqp.html
    tags:
      - AMQP
      - Messaging
      - RabbitMQ
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-integration/docs/current/reference/html/amqp.html
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.integration/spring-integration-amqp
  - aid: spring-integration:spring-integration-kafka
    name: Spring Integration Kafka Adapter
    description: Kafka channel adapters for Spring Integration. Provides message-driven inbound adapters, outbound channel adapters, and request/reply gateways for Apache Kafka integration.
    humanURL: https://docs.spring.io/spring-integration/docs/current/reference/html/kafka.html
    tags:
      - Event Streaming
      - Kafka
      - Messaging
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-integration/docs/current/reference/html/kafka.html
      - type: Maven Repository
        url: https://mvnrepository.com/artifact/org.springframework.integration/spring-integration-kafka
common:
  - type: Website
    url: https://spring.io/projects/spring-integration
  - type: Documentation
    url: https://docs.spring.io/spring-integration/reference/
  - type: GitHub Organization
    url: https://github.com/spring-projects/spring-integration
  - type: Getting Started
    url: https://spring.io/guides/gs/integration
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-integration
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework.integration
  - type: Releases
    url: https://github.com/spring-projects/spring-integration/releases
  - type: Blog
    url: https://spring.io/blog/category/integration
  - type: Sample Projects
    url: https://github.com/spring-projects/spring-integration-samples
maintainers:
  - FN: Spring Team
    email: spring-projects@vmware.com
    url: https://spring.io/team
---
