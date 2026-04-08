---
aid: spring-cloud-gateway
url: https://raw.githubusercontent.com/api-evangelist/spring-cloud-gateway/refs/heads/main/apis.yml
apis:
- aid: spring-cloud-gateway:spring-cloud-gateway-api
  name: Spring Cloud Gateway API
  description: Intelligent API gateway built on Spring WebFlux offering routing, predicate and filter capabilities, load balancing, circuit breaking, and rate limiting for microservice architectures.
  humanURL: https://spring.io/projects/spring-cloud-gateway
  tags:
  - API Gateway
  - Routing
  - Spring WebFlux
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/
  - type: Getting Started
    url: https://spring.io/projects/spring-cloud-gateway#learn
  - type: Reference
    url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#gateway-starter
  - type: GitHubRepository
    url: https://github.com/spring-cloud/spring-cloud-gateway
  - type: Change Log
    url: https://github.com/spring-cloud/spring-cloud-gateway/releases
- aid: spring-cloud-gateway:spring-cloud-gateway-actuator-api
  name: Spring Cloud Gateway Actuator API
  description: The Spring Cloud Gateway Actuator API exposes HTTP endpoints for managing and monitoring gateway routes at runtime, including retrieving route definitions, creating and deleting routes, refreshing the route cache, and querying available filters and metrics.
  humanURL: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#actuator-api
  tags:
  - Actuator
  - Management
  - Monitoring
  - Routes
  properties:
  - type: Documentation
    url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#actuator-api
  - type: Reference
    url: https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#retrieving-route-filters
name: Spring Cloud Gateway
tags:
- API Gateway
- Microservices
- Routing
- Spring
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Spring Cloud Gateway provides an intelligent, programmable router built on Spring WebFlux that offers API gateway functionality for microservices including routing, filtering, load balancing, and rate limiting.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

