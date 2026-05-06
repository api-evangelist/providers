---
aid: circuit-breaker
url: https://raw.githubusercontent.com/api-evangelist/circuit-breaker/refs/heads/main/apis.yml
name: Circuit Breaker
tags:
  - Circuit Breaker
  - Distributed Systems
  - Fault Tolerance
  - Microservices
  - Patterns
  - Resilience
  - Stability
type: Topic
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-23'
position: Reference
specificationVersion: '0.19'
description: The Circuit Breaker is a stability pattern for distributed systems and API architectures that prevents cascading failure when a downstream service degrades. A breaker wraps a remote call and tracks failures against a threshold; when the threshold is exceeded the breaker "opens" and short-circuits subsequent calls (typically returning an error or fallback) without contacting the downstream service. After a cooldown the breaker enters a "half-open" probe state and either resets to "closed" on success or re-opens on failure. The pattern was popularized by Michael Nygard in *Release It!* and is now standard in resilient microservice and API gateway design.
apis: []
common:
  - type: Reference
    url: https://martinfowler.com/bliki/CircuitBreaker.html
  - type: Reference
    url: https://docs.microsoft.com/azure/architecture/patterns/circuit-breaker
  - type: Reference
    url: https://learn.microsoft.com/azure/architecture/patterns/retry
  - type: Book
    url: https://pragprog.com/titles/mnee2/release-it-second-edition/
  - type: JSON-LD
    url: json-ld/circuit-breaker-context.jsonld
  - type: JSONSchema
    url: json-schema/circuit-breaker-state-schema.json
  - type: JSONSchema
    url: json-schema/circuit-breaker-config-schema.json
implementations:
  - name: Resilience4j
    language: Java
    url: https://resilience4j.readme.io/docs/circuitbreaker
    description: Lightweight, functional fault-tolerance library for Java 8+ inspired by Hystrix; the de facto modern Java circuit breaker.
  - name: Hystrix
    language: Java
    url: https://github.com/Netflix/Hystrix
    description: Netflix's original circuit breaker library for the JVM. In maintenance mode since 2018; Resilience4j is the recommended successor.
  - name: Polly
    language: .NET
    url: https://www.pollydocs.org/strategies/circuit-breaker.html
    description: The .NET resilience library; provides classic and advanced (rate-of-failure) circuit breaker strategies.
  - name: opossum
    language: JavaScript / Node.js
    url: https://nodeshift.dev/opossum/
    description: Node.js circuit breaker with promise-based API, status events, and Hystrix-compatible metrics streams.
  - name: gobreaker
    language: Go
    url: https://github.com/sony/gobreaker
    description: Sony's Go circuit breaker implementing the classic Nygard state machine.
  - name: Hystrix-Go
    language: Go
    url: https://github.com/afex/hystrix-go
    description: Latency and fault tolerance library for Go services modelled on Netflix Hystrix.
  - name: pybreaker
    language: Python
    url: https://github.com/danielfm/pybreaker
    description: Python implementation of the circuit breaker pattern with optional Redis-backed shared state.
  - name: Failsafe
    language: Java
    url: https://failsafe.dev/circuit-breaker/
    description: Lightweight fault-tolerance library combining circuit breaker, retry, timeout, fallback, and rate-limiter policies.
  - name: Istio Outlier Detection
    language: Service Mesh
    url: https://istio.io/latest/docs/reference/config/networking/destination-rule/#OutlierDetection
    description: Envoy/Istio outlier detection ejects unhealthy upstream hosts from the load-balancing pool, providing circuit-breaker semantics at the mesh layer.
  - name: Envoy Circuit Breaking
    language: Service Mesh
    url: https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/circuit_breaking
    description: Envoy enforces concurrency-style circuit breakers (max connections, pending requests, retries) on every upstream cluster.
  - name: AWS App Mesh / Spring Cloud Circuit Breaker
    language: Framework
    url: https://docs.spring.io/spring-cloud-circuitbreaker/docs/current/reference/html/
    description: Spring Cloud abstraction over Resilience4j, Sentinel, and other breakers, used in many enterprise Java microservice stacks.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
