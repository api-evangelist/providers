---
aid: spring-cloud
name: Spring Cloud
description: Spring Cloud provides tools for developers to quickly build some of the common patterns in distributed systems including configuration management, service discovery, circuit breakers, intelligent routing, micro-proxy, control bus, and distributed tracing. It builds on the Spring Boot approach to simplify microservice development and operations across cloud environments.
image: https://spring.io/img/spring-cloud.svg
url: https://spring.io/projects/spring-cloud
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Circuit Breaker
  - Cloud Native
  - Distributed Systems
  - Java
  - Microservices
  - Service Discovery
  - Spring Framework
apis:
  - aid: spring-cloud:spring-cloud-config
    name: Spring Cloud Config
    description: Externalized configuration management backed by Git, providing server and client-side support for configuration in distributed systems with encryption, refresh, and multi-environment support.
    humanURL: https://spring.io/projects/spring-cloud-config
    baseURL: http://localhost:8888
    tags:
      - Configuration
      - Distributed Config
      - Git
      - Microservices
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-config/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-config
      - type: JSONSchema
        url: json-schema/spring-cloud-config-properties.json
  - aid: spring-cloud:spring-cloud-netflix-eureka
    name: Spring Cloud Netflix Eureka
    description: Service discovery using Netflix Eureka for registering and discovering microservices, providing self-registration, client-side discovery, heartbeat-based health checks, and zone-aware load balancing.
    humanURL: https://spring.io/projects/spring-cloud-netflix
    baseURL: http://localhost:8761
    tags:
      - Eureka
      - Registry
      - Service Discovery
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-netflix/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-netflix
  - aid: spring-cloud:spring-cloud-gateway
    name: Spring Cloud Gateway
    description: Intelligent routing and filtering for microservices built on Spring WebFlux with predicates, filters, load balancing, circuit breaking, and rate limiting.
    humanURL: https://spring.io/projects/spring-cloud-gateway
    baseURL: http://localhost:8080
    tags:
      - API Gateway
      - Filtering
      - Load Balancing
      - Routing
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-gateway
      - type: OpenAPI
        url: openapi/spring-cloud-gateway-actuator-openapi.yml
      - type: JSONSchema
        url: json-schema/spring-cloud-service-instance-schema.json
      - type: JSONStructure
        url: json-structure/spring-cloud-service-registry-structure.json
      - type: JSONLDContext
        url: json-ld/spring-cloud-context.jsonld
      - type: SpectralRules
        url: rules/spring-cloud-gateway-rules.yml
      - type: NaftikoCapability
        url: capabilities/microservice-platform.yaml
  - aid: spring-cloud:spring-cloud-stream
    name: Spring Cloud Stream
    description: Framework for building event-driven microservices connected with shared messaging systems including Apache Kafka and RabbitMQ with consumer groups and partitioning.
    humanURL: https://spring.io/projects/spring-cloud-stream
    baseURL: https://spring.io/projects/spring-cloud-stream
    tags:
      - Event-Driven
      - Kafka
      - Messaging
      - RabbitMQ
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-stream/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-stream
      - type: Getting Started
        url: https://spring.io/guides/gs/spring-cloud-stream/
  - aid: spring-cloud:spring-cloud-circuit-breaker
    name: Spring Cloud Circuit Breaker
    description: Abstraction across different circuit breaker implementations including Resilience4J and Spring Retry, providing bulkhead, rate limiting, time limiting, and fallback patterns.
    humanURL: https://spring.io/projects/spring-cloud-circuitbreaker
    baseURL: https://spring.io/projects/spring-cloud-circuitbreaker
    tags:
      - Circuit Breaker
      - Fault Tolerance
      - Resilience
      - Resilience4J
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-circuitbreaker/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-circuitbreaker
  - aid: spring-cloud:spring-cloud-openfeign
    name: Spring Cloud OpenFeign
    description: Declarative REST client with support for Spring MVC annotations and HttpMessageConverters, providing load-balanced HTTP calls with Ribbon or Spring Cloud LoadBalancer integration.
    humanURL: https://spring.io/projects/spring-cloud-openfeign
    baseURL: https://spring.io/projects/spring-cloud-openfeign
    tags:
      - Declarative Client
      - Feign
      - HTTP
      - REST Client
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-openfeign/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-openfeign
  - aid: spring-cloud:spring-cloud-kubernetes
    name: Spring Cloud Kubernetes
    description: Integration with Kubernetes providing service discovery via DNS and Kubernetes API, ConfigMap and Secret-backed property sources, and load balancing for Spring Boot applications deployed in Kubernetes clusters.
    humanURL: https://spring.io/projects/spring-cloud-kubernetes
    baseURL: https://spring.io/projects/spring-cloud-kubernetes
    tags:
      - ConfigMap
      - Container Orchestration
      - Kubernetes
      - Service Discovery
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-kubernetes/docs/current/reference/html/
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-kubernetes
common:
  - type: Website
    url: https://spring.io/projects/spring-cloud
  - type: Documentation
    url: https://docs.spring.io/spring-cloud/
  - type: GitHub Organization
    url: https://github.com/spring-cloud
  - type: Blog
    url: https://spring.io/blog/category/cloud
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-cloud
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework.cloud
  - type: Vocabulary
    url: vocabulary/spring-cloud-vocabulary.yml
maintainers:
  - FN: VMware Tanzu (Spring Team)
    email: support@vmware.com
    url: https://spring.io/team
include:
  - name: Spring Boot
    url: https://spring.io/projects/spring-boot
  - name: Spring Framework
    url: https://spring.io/projects/spring-framework
---
