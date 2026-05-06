---
aid: spring-cloud-gateway
name: Spring Cloud Gateway
description: Spring Cloud Gateway provides an intelligent, programmable router built on Spring WebFlux that serves as the entry point to microservice architectures. It offers routing, predicate evaluation, filter chaining, load balancing, circuit breaking, rate limiting, and runtime route management through an Actuator API.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://spring.io/projects/spring-cloud-gateway
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - API Gateway
  - Circuit Breaker
  - Load Balancing
  - Microservices
  - Rate Limiting
  - Routing
  - Spring
  - Spring WebFlux
apis:
  - aid: spring-cloud-gateway:spring-cloud-gateway-actuator
    name: Spring Cloud Gateway Actuator API
    description: Runtime management API for Spring Cloud Gateway exposing endpoints for retrieving, creating, updating, and deleting route definitions. Also provides access to global filters, route filter factories, route predicate factories, and cache refresh capabilities.
    humanURL: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#actuator-api
    baseURL: http://localhost:8080/actuator/gateway
    tags:
      - Actuator
      - API Gateway
      - Filters
      - Management
      - Monitoring
      - Routes
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#actuator-api
      - type: OpenAPI
        url: openapi/spring-cloud-gateway-actuator-openapi.yml
      - type: JSONSchema
        url: json-schema/spring-cloud-gateway-route-schema.json
      - type: JSONStructure
        url: json-structure/spring-cloud-gateway-route-structure.json
      - type: JSONLDContext
        url: json-ld/spring-cloud-gateway-context.jsonld
      - type: SpectralRules
        url: rules/spring-cloud-gateway-rules.yml
      - type: NaftikoCapability
        url: capabilities/api-gateway-management.yaml
  - aid: spring-cloud-gateway:spring-cloud-gateway-core
    name: Spring Cloud Gateway Core
    description: Core routing and filtering capabilities including predicate factories (Path, Host, Method, Header, Query, Cookie, Weight, RemoteAddr), gateway filter factories (AddRequestHeader, RewritePath, RequestRateLimiter, CircuitBreaker, Retry), and global filters for proxying requests to downstream services.
    humanURL: https://spring.io/projects/spring-cloud-gateway
    baseURL: http://localhost:8080
    tags:
      - API Gateway
      - Filtering
      - Load Balancing
      - Predicates
      - Routing
    properties:
      - type: Documentation
        url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
      - type: Getting Started
        url: https://spring.io/projects/spring-cloud-gateway#learn
      - type: GitHub
        url: https://github.com/spring-cloud/spring-cloud-gateway
      - type: Releases
        url: https://github.com/spring-cloud/spring-cloud-gateway/releases
common:
  - type: Website
    url: https://spring.io/projects/spring-cloud-gateway
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
  - type: GitHub
    url: https://github.com/spring-cloud/spring-cloud-gateway
  - type: GitHub Organization
    url: https://github.com/spring-cloud
  - type: Issues
    url: https://github.com/spring-cloud/spring-cloud-gateway/issues
  - type: Releases
    url: https://github.com/spring-cloud/spring-cloud-gateway/releases
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/spring-cloud-gateway
  - type: Maven Repository
    url: https://mvnrepository.com/artifact/org.springframework.cloud/spring-cloud-gateway-server
  - type: Vocabulary
    url: vocabulary/spring-cloud-gateway-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
