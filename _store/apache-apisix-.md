---
aid: apache-apisix
url: https://raw.githubusercontent.com/api-evangelist/apache-apisix/refs/heads/main/apis.yml
apis:
- aid: apache-apisix:apache-apisix
  name: Apache APISIX
  description: Apache APISIX provides rich traffic management features including load balancing, dynamic upstream, canary release, circuit breaking, authentication, observability, and more.
  humanURL: https://apisix.apache.org/
  tags:
  - Apache
  - API Gateway
  - Cloud Native
  properties:
  - type: Documentation
    url: https://apisix.apache.org/docs/apisix/getting-started/
  - type: Getting Started
    url: https://apisix.apache.org/docs/apisix/getting-started/README/
  - type: GitHubRepository
    url: https://github.com/apache/apisix
  - type: Change Log
    url: https://github.com/apache/apisix/releases
- aid: apache-apisix:apache-apisix-admin-api
  name: Apache APISIX Admin API
  description: The Apache APISIX Admin API provides a RESTful interface to dynamically control and configure a running APISIX instance. It supports management of routes, services, upstreams, consumers, SSL certificates, global rules, plugin configurations, consumer groups, and secrets, and listens by default on port 9180 with API key authentication.
  humanURL: https://apisix.apache.org/docs/apisix/admin-api/
  tags:
  - Admin
  - Configuration
  - Management
  - REST
  properties:
  - type: Documentation
    url: https://apisix.apache.org/docs/apisix/admin-api/
  - type: OpenAPI
    url: openapi/apache-apisix-admin-api-openapi.yml
  - type: Authentication
    url: https://apisix.apache.org/docs/apisix/admin-api/#using-the-admin-api
- aid: apache-apisix:apache-apisix-control-api
  name: Apache APISIX Control API
  description: The Apache APISIX Control API provides internal status and health check endpoints for monitoring and introspecting a running APISIX instance. It listens by default on port 9090, is accessible only from localhost, and exposes endpoints for health checking, schema retrieval, and runtime diagnostics.
  humanURL: https://apisix.apache.org/docs/apisix/control-api/
  tags:
  - Control
  - Health Check
  - Monitoring
  - Observability
  properties:
  - type: Documentation
    url: https://apisix.apache.org/docs/apisix/control-api/
  - type: OpenAPI
    url: openapi/apache-apisix-control-api-openapi.yml
name: Apache APISIX
tags:
- Apache
- API Gateway
- Cloud Native
- Kubernetes
- Open Source
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://apisix.apache.org/docs/
  name: Documentation | Apache APISIX -- Cloud-Native API Gateway
  type: Documentation
  description: 'null'
- url: https://apisix.apache.org/blog/
  name: Blog | Apache APISIX -- Cloud-Native API Gateway
  type: Blog
  description: 'null'
- url: https://apisix.apache.org/help/
  name: Help | Apache APISIX -- Cloud-Native API Gateway
  type: Support
  description: 'null'
- url: https://apisix.apache.org/docs/general/events/
  name: Events calendar | Apache APISIX -- Cloud-Native API Gateway
  type: Events
  description: 'null'
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Apache APISIX is a dynamic, real-time, high-performance cloud-native API gateway built on NGINX and etcd, supporting Lua and multi-language plugins for traffic management, authentication, observability, and security.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

