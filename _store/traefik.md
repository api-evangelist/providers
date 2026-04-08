---
aid: traefik
url: https://raw.githubusercontent.com/api-evangelist/traefik/refs/heads/main/apis.yml
apis:
- aid: traefik:traefik
  name: Traefik Proxy
  description: Traefik is a leading modern reverse proxy and load balancer that makes deploying microservices easy with native support for Kubernetes, Docker, and automatic TLS certificate provisioning.
  humanURL: https://traefik.io/traefik/
  tags:
  - API Gateway
  - Kubernetes
  - Reverse Proxy
  properties:
  - type: Documentation
    url: https://doc.traefik.io/traefik/
  - type: Getting Started
    url: https://doc.traefik.io/traefik/getting-started/quick-start/
  - type: Reference
    url: https://doc.traefik.io/traefik/reference/static-configuration/cli/
  - type: Change Log
    url: https://github.com/traefik/traefik/blob/master/CHANGELOG.md
  - type: GitHubRepository
    url: https://github.com/traefik/traefik
- aid: traefik:traefik-api
  name: Traefik REST API
  description: The Traefik REST API exposes runtime configuration and state for all routers, services, middlewares, and entry points in a running Traefik instance. It provides read-only HTTP endpoints for inspecting HTTP, TCP, and UDP routing configuration, as well as version and overview statistics. The API must be enabled in static configuration and should be secured before use in production.
  humanURL: https://doc.traefik.io/traefik/operations/api/
  tags:
  - Configuration
  - Management
  - Observability
  - REST
  properties:
  - type: Documentation
    url: https://doc.traefik.io/traefik/operations/api/
  - type: Reference
    url: https://doc.traefik.io/traefik/operations/api/#endpoints
  - type: OpenAPI
    url: openapi/traefik-api-openapi.yml
- aid: traefik:traefik-ping
  name: Traefik Ping API
  description: The Traefik Ping API provides a simple health check endpoint at `/ping` that returns HTTP 200 with the body "OK" when the Traefik process is alive and ready. It is used for liveness probes in container orchestration environments and can be configured on a dedicated entry point.
  humanURL: https://doc.traefik.io/traefik/operations/ping/
  tags:
  - Health Check
  - Liveness
  - Monitoring
  - Operations
  properties:
  - type: Documentation
    url: https://doc.traefik.io/traefik/operations/ping/
- aid: traefik:traefik-dashboard
  name: Traefik Dashboard
  description: The Traefik Dashboard is a built-in web UI that provides a real-time visual overview of all configured routers, services, middlewares, and entry points. It is served from the same API handler as the REST API and can be accessed via the Traefik entry point or a custom route.
  humanURL: https://doc.traefik.io/traefik/operations/dashboard/
  tags:
  - Dashboard
  - Management
  - Observability
  - UI
  properties:
  - type: Documentation
    url: https://doc.traefik.io/traefik/operations/dashboard/
name: Traefik
tags:
- API Gateway
- Kubernetes
- Load Balancer
- Open Source
- Reverse Proxy
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Traefik is a modern open-source HTTP reverse proxy and load balancer that makes deploying microservices and API gateways easy with automatic service discovery, Let's Encrypt integration, and a rich middleware ecosystem.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

