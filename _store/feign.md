---
aid: feign
name: Feign
description: Feign (OpenFeign) is a declarative Java HTTP client binder inspired by Retrofit, JAX-RS, and WebSocket. It turns annotated interfaces into templated HTTP requests with pluggable encoders, decoders, error handlers, and HTTP transports. The OpenFeign organization maintains a large set of modules covering serialization (Jackson, Gson, Moshi, FastJSON2, JAXB, SAX, SOAP), HTTP transports (OkHttp, Apache HttpClient, Java 11 client, Ribbon), JAX-RS contracts, resilience (Hystrix), logging (SLF4J), form encoding, GraphQL, and metrics.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-27'
modified: '2026-04-28'
position: Consumer
tags:
  - HTTP Client
  - Java
  - JVM
  - Open Source
  - REST
  - SDKs
url: https://raw.githubusercontent.com/api-evangelist/feign/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: feign:feign-core
    name: Feign Core
    description: Feign Core is the base library that processes annotated Java interfaces into templated HTTP requests. It defines the contract, encoder, decoder, and client abstractions used across the entire OpenFeign ecosystem.
    humanURL: https://github.com/OpenFeign/feign
    tags:
      - HTTP Client
      - Java
      - Core
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign#readme
      - type: Getting Started
        url: https://github.com/OpenFeign/feign#basics
      - type: Source Code
        url: https://github.com/OpenFeign/feign
      - type: Maven Central
        url: https://central.sonatype.com/artifact/io.github.openfeign/feign-core
  - aid: feign:feign-jackson
    name: Feign Jackson
    description: Feign Jackson module provides Jackson-based JSON encoding and decoding for Feign-annotated client interfaces, the most common serialization choice in JVM applications.
    humanURL: https://github.com/OpenFeign/feign/tree/master/jackson
    tags:
      - JSON
      - Jackson
      - Serialization
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/jackson
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/jackson
  - aid: feign:feign-gson
    name: Feign Gson
    description: Feign Gson module provides Google Gson-based JSON encoding and decoding for Feign clients, useful in projects already standardized on Gson.
    humanURL: https://github.com/OpenFeign/feign/tree/master/gson
    tags:
      - JSON
      - Gson
      - Serialization
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/gson
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/gson
  - aid: feign:feign-okhttp
    name: Feign OkHttp
    description: Feign OkHttp module replaces the default JDK HTTP transport with Square's OkHttp client, adding HTTP/2, connection pooling, and modern transport features.
    humanURL: https://github.com/OpenFeign/feign/tree/master/okhttp
    tags:
      - HTTP Client
      - Transport
      - OkHttp
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/okhttp
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/okhttp
  - aid: feign:feign-httpclient
    name: Feign Apache HttpClient
    description: Feign Apache HttpClient module integrates Apache HttpComponents (HC5) as the underlying HTTP transport for Feign clients.
    humanURL: https://github.com/OpenFeign/feign/tree/master/httpclient
    tags:
      - HTTP Client
      - Transport
      - Apache
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/httpclient
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/httpclient
  - aid: feign:feign-java11
    name: Feign Java 11 HTTP
    description: Feign Java 11 HTTP module uses the JDK 11+ standard HttpClient as the transport, supporting HTTP/2 and asynchronous calls without external dependencies.
    humanURL: https://github.com/OpenFeign/feign/tree/master/java11
    tags:
      - HTTP Client
      - Transport
      - Java 11
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/java11
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/java11
  - aid: feign:feign-ribbon
    name: Feign Ribbon
    description: Feign Ribbon module integrates Netflix Ribbon for client-side load balancing across a list of HTTP servers.
    humanURL: https://github.com/OpenFeign/feign/tree/master/ribbon
    tags:
      - Load Balancing
      - Netflix
      - Resilience
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/ribbon
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/ribbon
  - aid: feign:feign-hystrix
    name: Feign Hystrix
    description: Feign Hystrix module wraps Feign client calls in Netflix Hystrix commands, adding circuit breaking, fallbacks, and bulkhead isolation.
    humanURL: https://github.com/OpenFeign/feign/tree/master/hystrix
    tags:
      - Resilience
      - Circuit Breaker
      - Netflix
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/hystrix
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/hystrix
  - aid: feign:feign-jaxrs
    name: Feign JAX-RS
    description: Feign JAX-RS modules let developers reuse JAX-RS 1.x, 2.x, 3.x, and 4.x annotations on Feign client interfaces instead of Feign's native annotation set.
    humanURL: https://github.com/OpenFeign/feign/tree/master/jaxrs
    tags:
      - JAX-RS
      - Annotations
      - Contracts
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/jaxrs
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/jaxrs
  - aid: feign:feign-slf4j
    name: Feign SLF4J
    description: Feign SLF4J module routes Feign request and response logging through the SLF4J facade, integrating with the host application's logging backend.
    humanURL: https://github.com/OpenFeign/feign/tree/master/slf4j
    tags:
      - Logging
      - Observability
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/slf4j
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/slf4j
  - aid: feign:feign-form
    name: Feign Form
    description: Feign Form module adds support for application/x-www-form-urlencoded and multipart/form-data request bodies, including file uploads.
    humanURL: https://github.com/OpenFeign/feign-form
    tags:
      - Forms
      - Multipart
      - File Upload
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign-form
      - type: Source Code
        url: https://github.com/OpenFeign/feign-form
  - aid: feign:feign-micrometer
    name: Feign Micrometer
    description: Feign Micrometer module exposes Feign client metrics (timings, counts, errors) through Micrometer for shipment to Prometheus, Datadog, and other monitoring backends.
    humanURL: https://github.com/OpenFeign/feign/tree/master/micrometer
    tags:
      - Metrics
      - Observability
      - Micrometer
    properties:
      - type: Documentation
        url: https://github.com/OpenFeign/feign/tree/master/micrometer
      - type: Source Code
        url: https://github.com/OpenFeign/feign/tree/master/micrometer
common:
  - type: Website
    url: https://github.com/OpenFeign/feign
  - type: Documentation
    url: https://github.com/OpenFeign/feign#readme
  - type: GitHub Organization
    url: https://github.com/OpenFeign
  - type: Issues
    url: https://github.com/OpenFeign/feign/issues
  - type: Releases
    url: https://github.com/OpenFeign/feign/releases
  - type: License
    url: https://github.com/OpenFeign/feign/blob/master/LICENSE
  - type: Maven Central
    url: https://central.sonatype.com/namespace/io.github.openfeign
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
