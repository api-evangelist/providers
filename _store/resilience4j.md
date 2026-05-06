---
aid: resilience4j
name: Resilience4j
description: Resilience4j is a lightweight fault tolerance library designed for Java 17+ and functional programming, providing higher-order functions to enhance functional interfaces with Circuit Breaker, Rate Limiter, Retry, Bulkhead, TimeLimiter, and Cache patterns. Designed as a replacement for Netflix Hystrix, it integrates with Spring Boot 2 and 3, Micronaut, RxJava, Spring Reactor, Micrometer, Prometheus, and Dropwizard Metrics. Used in production by Deutsche Telekom (400M+ requests/day), PlayStation Network, AOL, and Auto Trader Group.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bulkhead
  - Circuit Breaker
  - Fault Tolerance
  - Java
  - Microservices
  - Rate Limiter
  - Resilience
  - Retry
  - Spring Boot
  - Functional Programming
url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: resilience4j:resilience4j
    name: Resilience4j
    description: 'Resilience4j is a lightweight fault tolerance library for Java 17+ using functional programming patterns. It provides six core resilience patterns: Circuit Breaker (prevents cascading failures), Rate Limiter (controls throughput), Bulkhead (isolates resources), Retry (automatic retries with backoff), TimeLimiter (timeout handling), and Cache (result caching). Spring Boot Actuator integration exposes management endpoints for monitoring circuit breaker state, events, and metrics.'
    humanURL: https://resilience4j.readme.io/
    tags:
      - Bulkhead
      - Circuit Breaker
      - Fault Tolerance
      - Java
      - Microservices
      - Rate Limiter
      - Resilience
      - Retry
      - Spring Boot
      - Functional Programming
    properties:
      - type: Documentation
        url: https://resilience4j.readme.io/docs
      - type: GettingStarted
        url: https://resilience4j.readme.io/docs/getting-started
      - type: GitHub
        url: https://github.com/resilience4j/resilience4j
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-schema/circuit-breaker-configuration.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-schema/retry-configuration.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-schema/rate-limiter-configuration.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-schema/bulkhead-configuration.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-schema/time-limiter-configuration.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-structure/resilience4j-circuit-breaker-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-structure/resilience4j-retry-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/json-ld/resilience4j-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/resilience4j/refs/heads/main/vocabulary/resilience4j-vocabulary.yml
common:
  - type: Website
    url: https://resilience4j.readme.io/
  - type: Documentation
    url: https://resilience4j.readme.io/docs
  - type: GettingStarted
    url: https://resilience4j.readme.io/docs/getting-started
  - type: GitHub
    url: https://github.com/resilience4j/resilience4j
  - type: GitHubOrganization
    url: https://github.com/resilience4j
  - type: Releases
    url: https://github.com/resilience4j/resilience4j/releases
  - type: Issues
    url: https://github.com/resilience4j/resilience4j/issues
  - type: License
    url: https://github.com/resilience4j/resilience4j/blob/master/LICENSE.txt
  - type: MavenCentral
    url: https://search.maven.org/search?q=io.github.resilience4j
  - type: SpringBoot
    url: https://resilience4j.readme.io/docs/getting-started-3
  - type: Micronaut
    url: https://resilience4j.readme.io/docs/getting-started-4
  - type: SpringDemo
    url: https://github.com/resilience4j/resilience4j-spring-boot-demo
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
