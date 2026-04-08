---
aid: netflix-zuul
url: https://raw.githubusercontent.com/api-evangelist/netflix-zuul/refs/heads/main/apis.yml
apis:
- aid: netflix-zuul:netflix-zuul-gateway
  name: Netflix Zuul Gateway
  description: Netflix Zuul is an L7 application gateway built on Netty that provides dynamic routing, load balancing, authentication, monitoring, and resiliency for edge services. Zuul 3.x is the current release, supporting inbound, endpoint, and outbound filter pipelines for intercepting and modifying HTTP requests and responses at the edge.
  humanURL: https://github.com/Netflix/zuul
  tags:
  - API Gateway
  - Edge Service
  - Netty
  - Routing
  properties:
  - type: Documentation
    url: https://github.com/Netflix/zuul/wiki
  - type: Getting Started
    url: https://github.com/Netflix/zuul/wiki/Getting-Started-3.0
  - type: Reference
    url: https://github.com/Netflix/zuul/wiki/How-it-Works-3.0
  - type: GitHubRepository
    url: https://github.com/Netflix/zuul
  - type: Change Log
    url: https://github.com/Netflix/zuul/releases
  - type: Issue Tracker
    url: https://github.com/Netflix/zuul/issues
- aid: netflix-zuul:netflix-zuul-filters-api
  name: Netflix Zuul Filters API
  description: The Zuul Filters API provides the core extension point for building custom logic into the Zuul gateway pipeline. Developers implement inbound, endpoint, and outbound filters using synchronous or asynchronous base classes to handle authentication, routing, rate limiting, metrics, and response decoration.
  humanURL: https://github.com/Netflix/zuul/wiki/Filters
  tags:
  - Extension
  - Filters
  - Middleware
  - Routing
  properties:
  - type: Documentation
    url: https://github.com/Netflix/zuul/wiki/Filters
  - type: Reference
    url: https://github.com/Netflix/zuul/wiki/Writing-Filters
  - type: GitHubRepository
    url: https://github.com/Netflix/zuul
- aid: netflix-zuul:netflix-zuul-push-messaging
  name: Netflix Zuul Push Messaging
  description: Zuul Push Messaging enables server-to-client push communications over WebSockets and Server Sent Events (SSE). It provides a PushConnectionRegistry for managing connected clients and supports distributed deployments using external datastores such as Redis, Cassandra, or DynamoDB for multi-node clusters.
  humanURL: https://github.com/Netflix/zuul/wiki/Push-Messaging
  tags:
  - Push Messaging
  - Real Time
  - Server Sent Events
  - WebSocket
  properties:
  - type: Documentation
    url: https://github.com/Netflix/zuul/wiki/Push-Messaging
  - type: GitHubRepository
    url: https://github.com/Netflix/zuul
name: Netflix Zuul
tags:
- API Gateway
- Edge Service
- Netflix
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Netflix Zuul is an open-source L7 application gateway that provides dynamic routing, monitoring, resiliency, and security for edge services. Originally developed by Netflix, Zuul 2 uses Netty for non-blocking I/O and is commonly used as an API gateway and edge service.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

