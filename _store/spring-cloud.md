---
aid: spring-cloud
url: https://raw.githubusercontent.com/api-evangelist/spring-cloud/refs/heads/main/apis.yml
apis:
- name: Spring Cloud Config
  description: Externalized configuration management backed by Git, providing server and client-side support for configuration in distributed systems.
  image: https://spring.io/img/projects/spring-cloud.svg
  humanURL: https://spring.io/projects/spring-cloud-config
  baseURL: http://localhost:8888
  tags:
  - Configuration
  - Distributed Config
  - Git
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-config/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-config
  - type: OpenAPI
    url: https://example.com/spring-cloud-config/openapi.json
  - type: JSONSchema
    url: json-schema/spring-cloud-config-properties.json
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
    X-twitter: springcloud
- name: Spring Cloud Netflix Eureka
  description: Service discovery using Netflix Eureka for registering and discovering microservices.
  image: https://spring.io/img/projects/spring-cloud.svg
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
  - type: API Endpoint
    url: http://localhost:8761/eureka/apps
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
- name: Spring Cloud Gateway
  description: Intelligent routing and filtering for microservices built on Spring WebFlux.
  image: https://spring.io/img/projects/spring-cloud.svg
  humanURL: https://spring.io/projects/spring-cloud-gateway
  baseURL: http://localhost:8080
  tags:
  - Api Gateway
  - Filtering
  - Load Balancing
  - Routing
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-gateway
  - type: Actuator Endpoints
    url: http://localhost:8080/actuator/gateway
  - type: OpenAPI
    url: openapi/spring-cloud-gateway-actuator-openapi.yml
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
- name: Spring Cloud Stream
  description: Framework for building event-driven microservices connected with shared messaging systems.
  image: https://spring.io/img/projects/spring-cloud.svg
  humanURL: https://spring.io/projects/spring-cloud-stream
  baseURL: https://spring.io/projects/spring-cloud-stream
  tags:
  - Event-Driven
  - Kafka
  - Messaging
  - Rabbitmq
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-stream/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-stream
  - type: Getting Started
    url: https://spring.io/guides/gs/spring-cloud-stream/
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
- name: Spring Cloud Sleuth
  description: Distributed tracing solution for Spring Cloud applications with support for Zipkin and other tracing systems.
  image: https://spring.io/img/projects/spring-cloud.svg
  humanURL: https://spring.io/projects/spring-cloud-sleuth
  baseURL: https://spring.io/projects/spring-cloud-sleuth
  tags:
  - Distributed Tracing
  - Observability
  - Tracing
  - Zipkin
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-sleuth/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-sleuth
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
- name: Spring Cloud Circuit Breaker
  description: Abstraction across different circuit breaker implementations like Resilience4J and Spring Retry.
  image: https://spring.io/img/projects/spring-cloud.svg
  humanURL: https://spring.io/projects/spring-cloud-circuitbreaker
  baseURL: https://spring.io/projects/spring-cloud-circuitbreaker
  tags:
  - Circuit Breaker
  - Fault Tolerance
  - Resilience
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-circuitbreaker/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-circuitbreaker
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
- name: Spring Cloud OpenFeign
  description: Declarative REST client with support for Spring MVC annotations and HttpMessageConverters.
  image: https://spring.io/img/projects/spring-cloud.svg
  humanURL: https://spring.io/projects/spring-cloud-openfeign
  baseURL: https://spring.io/projects/spring-cloud-openfeign
  tags:
  - Feign
  - Http
  - Rest Client
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-openfeign/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-openfeign
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
- name: Spring Cloud Kubernetes
  description: Integration with Kubernetes providing service discovery, configuration, and load balancing.
  image: https://spring.io/img/projects/spring-cloud.svg
  humanURL: https://spring.io/projects/spring-cloud-kubernetes
  baseURL: https://spring.io/projects/spring-cloud-kubernetes
  tags:
  - Container Orchestration
  - Kubernetes
  - Service Discovery
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-kubernetes/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-kubernetes
  contact:
  - FN: Spring Cloud Team
    email: spring-cloud@pivotal.io
name: Spring Cloud
tags:
- Cloud
- Distributed Systems
- Java
- Microservices
- Spring Framework
type: Contract
image: https://spring.io/img/spring-cloud.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs and services provided by Spring Cloud for building cloud-native applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

