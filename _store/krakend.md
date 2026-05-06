---
aid: krakend
name: KrakenD
description: KrakenD is a stateless, distributed, high-performance open-source API gateway written in Go, focused on API aggregation, transformation, and security with a declarative configuration approach.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Aggregation
  - API Gateway
  - Go
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/krakend/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: krakend:krakend
    name: KrakenD
    description: KrakenD Community Edition is an ultra-high performance API gateway that aggregates multiple service calls into a single endpoint, transforming and filtering responses with a declarative JSON configuration.
    humanURL: https://www.krakend.io/
    tags:
      - Aggregation
      - API Gateway
      - Go
    properties:
      - type: Documentation
        url: https://www.krakend.io/docs/overview/
      - type: Getting Started
        url: https://www.krakend.io/docs/overview/introduction/
      - type: Reference
        url: https://www.krakend.io/docs/configuration/structure/
      - type: Change Log
        url: https://github.com/krakend/krakend-ce/releases
      - type: GitHubRepository
        url: https://github.com/krakend/krakend-ce
      - type: JSONSchema
        url: json-schema/service-config.json
      - type: JSON-LD
        url: json-ld/krakend-context.jsonld
  - aid: krakend:krakend-service-api
    name: KrakenD Service API
    description: The KrakenD Service API exposes built-in operational endpoints on a running KrakenD gateway instance. It includes the health check endpoint at /__health (enabled by default), the debug endpoint at /__debug (enabled via configuration), and the extended metrics endpoint at /__stats for detailed runtime telemetry. These endpoints are used for monitoring, debugging, and health checking KrakenD deployments.
    humanURL: https://www.krakend.io/docs/service-settings/health/
    baseURL: http://localhost:8080
    tags:
      - Health Check
      - Monitoring
      - Observability
      - Operations
    properties:
      - type: Documentation
        url: https://www.krakend.io/docs/service-settings/health/
      - type: Reference
        url: https://www.krakend.io/docs/service-settings/debug-endpoint/
      - type: OpenAPI
        url: openapi/krakend-service-api-openapi.yml
  - aid: krakend:krakend-async-agent
    name: KrakenD Async Agent
    description: The KrakenD Async Agent enables event-driven API consumption by connecting KrakenD to message brokers and event queues such as AMQP, Kafka, and NATS. It allows KrakenD to consume messages from topics and queues and forward them to backend services without requiring an inbound HTTP request from a client.
    humanURL: https://www.krakend.io/docs/async/
    tags:
      - Async
      - Event-Driven
      - Kafka
      - Messaging
    properties:
      - type: Documentation
        url: https://www.krakend.io/docs/async/
      - type: Reference
        url: https://www.krakend.io/docs/async/amqp/
      - type: JSONSchema
        url: json-schema/async-agent.json
      - type: GitHubRepository
        url: https://github.com/krakend/krakend-ce
common:
  - type: Website
    url: https://www.krakend.io/
  - type: Documentation
    url: https://www.krakend.io/docs/
  - type: Getting Started
    url: https://www.krakend.io/docs/overview/introduction/
  - type: Blog
    url: https://www.krakend.io/blog/
  - type: Change Log
    url: https://github.com/krakend/krakend-ce/releases
  - type: GitHub Organization
    url: https://github.com/krakend
  - type: GitHubRepository
    url: https://github.com/krakend/krakend-ce
  - type: Community
    url: https://community.krakend.io/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/krakend
  - type: Issue Tracker
    url: https://github.com/krakend/krakend-ce/issues
  - type: Developer Tools
    url: https://designer.krakend.io/
  - type: JSONSchema
    url: json-schema/service-config.json
  - type: JSON-LD
    url: json-ld/krakend-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
