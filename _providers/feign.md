---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 12
apis:
- description: Feign Core is the base library that processes annotated Java interfaces into templated HTTP requests. It defines the contract, encoder, decoder, and client abstractions used across the entire OpenFeig
  name: Feign Core
  slug: feign-core
- description: Feign Jackson module provides Jackson-based JSON encoding and decoding for Feign-annotated client interfaces, the most common serialization choice in JVM applications.
  name: Feign Jackson
  slug: feign-jackson
- description: Feign Gson module provides Google Gson-based JSON encoding and decoding for Feign clients, useful in projects already standardized on Gson.
  name: Feign Gson
  slug: feign-gson
- description: Feign OkHttp module replaces the default JDK HTTP transport with Square's OkHttp client, adding HTTP/2, connection pooling, and modern transport features.
  name: Feign OkHttp
  slug: feign-okhttp
- description: Feign Apache HttpClient module integrates Apache HttpComponents (HC5) as the underlying HTTP transport for Feign clients.
  name: Feign Apache HttpClient
  slug: feign-httpclient
- description: Feign Java 11 HTTP module uses the JDK 11+ standard HttpClient as the transport, supporting HTTP/2 and asynchronous calls without external dependencies.
  name: Feign Java 11 HTTP
  slug: feign-java11
- description: Feign Ribbon module integrates Netflix Ribbon for client-side load balancing across a list of HTTP servers.
  name: Feign Ribbon
  slug: feign-ribbon
- description: Feign Hystrix module wraps Feign client calls in Netflix Hystrix commands, adding circuit breaking, fallbacks, and bulkhead isolation.
  name: Feign Hystrix
  slug: feign-hystrix
- description: Feign JAX-RS modules let developers reuse JAX-RS 1.x, 2.x, 3.x, and 4.x annotations on Feign client interfaces instead of Feign's native annotation set.
  name: Feign JAX-RS
  slug: feign-jaxrs
- description: Feign SLF4J module routes Feign request and response logging through the SLF4J facade, integrating with the host application's logging backend.
  name: Feign SLF4J
  slug: feign-slf4j
- description: Feign Form module adds support for application/x-www-form-urlencoded and multipart/form-data request bodies, including file uploads.
  name: Feign Form
  slug: feign-form
- description: Feign Micrometer module exposes Feign client metrics (timings, counts, errors) through Micrometer for shipment to Prometheus, Datadog, and other monitoring backends.
  name: Feign Micrometer
  slug: feign-micrometer
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/OpenFeign/feign
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/OpenFeign/feign#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenFeign
- group: operate
  title: ''
  type: Issues
  url: https://github.com/OpenFeign/feign/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/OpenFeign/feign/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/OpenFeign/feign/blob/master/LICENSE
- group: other
  title: ''
  type: Maven Central
  url: https://central.sonatype.com/namespace/io.github.openfeign
created: '2026-03-27'
description: Feign (OpenFeign) is a declarative Java HTTP client binder inspired by Retrofit, JAX-RS, and WebSocket. It turns annotated interfaces into templated HTTP requests with pluggable encoders, decoders, error handlers, and HTTP transports. The OpenFeign organization maintains a large set of modules covering serialization (Jackson, Gson, Moshi, FastJSON2, JAXB, SAX, SOAP), HTTP transports (OkHttp, Apache HttpClient, Java 11 client, Ribbon), JAX-RS contracts, resilience (Hystrix), logging (SLF4J), form encoding, GraphQL, and metrics.
finops:
- name: Feign Finops
  service_category: API
  slug: feign-finops
graphqls:
- description: ''
  name: Feign GraphQL API
  slug: feign-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/feign.png
layout: provider
modified: '2026-04-28'
name: Feign
nav: Providers
network: true
overview: 'Feign publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include HTTP Client, Java, JVM, Open Source, and REST.


  Feign''s developer surface includes documentation, release notes, and 5 more developer resources.'
plans:
- name: Feign Plans Pricing
  plan_count: 3
  slug: feign-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Feign Rate Limits
  slug: feign-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 25.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/feign/refs/heads/main/screenshots/feign-2026-06-20T181136.png
slug: feign
tags:
- HTTP Client
- Java
- JVM
- Open Source
- REST
- SDKs
---
