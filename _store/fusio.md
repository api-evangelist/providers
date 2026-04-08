---
aid: fusio
url: https://raw.githubusercontent.com/api-evangelist/fusio/refs/heads/main/apis.yml
apis:
- aid: fusio:fusio
  name: Fusio
  tags:
  - API Management
  - Open Source
  - REST API
  humanURL: https://www.fusio-project.org/
  properties:
  - url: https://docs.fusio-project.org/
    type: Documentation
  - type: Getting Started
    url: https://docs.fusio-project.org/docs/bootstrap
  - type: GitHubRepository
    url: https://github.com/apioo/fusio
  - type: Change Log
    url: https://github.com/apioo/fusio/blob/master/CHANGELOG.md
  description: Fusio is an open source API management platform which helps to build and manage REST APIs.
- aid: fusio:fusio-backend-api
  name: Fusio Backend API
  description: The Fusio Backend API provides a REST interface to configure and manage all aspects of a Fusio API management instance. It covers operations, routes, schemas, actions, connections, apps, users, and marketplace resources used by the Fusio backend application.
  humanURL: https://docs.fusio-project.org/docs/use_cases/api_product/
  baseURL: https://www.fusio-project.org/
  tags:
  - Backend
  - Configuration
  - Management
  - REST API
  properties:
  - type: Documentation
    url: https://docs.fusio-project.org/docs/use_cases/api_product/
  - type: GitHubRepository
    url: https://github.com/apioo/fusio
- aid: fusio:fusio-consumer-api
  name: Fusio Consumer API
  description: The Fusio Consumer API is used by the developer portal application and enables third-party developers to request access tokens, manage their apps, and interact with protected API endpoints. It provides the authentication and user management layer for API consumers.
  humanURL: https://docs.fusio-project.org/docs/backend/consumer/user/
  baseURL: https://www.fusio-project.org/
  tags:
  - Authentication
  - Consumer
  - Developer Portal
  - REST API
  properties:
  - type: Documentation
    url: https://docs.fusio-project.org/docs/backend/consumer/user/
  - type: Reference
    url: https://docs.fusio-project.org/docs/backend/consumer/app
  - type: GitHubRepository
    url: https://github.com/apioo/fusio
- aid: fusio:fusio-worker-api
  name: Fusio Worker API
  description: The Fusio Worker API enables executing API action logic in multiple programming languages by forwarding requests to external worker processes. Workers are implemented in the target language (JavaScript, Python, Java, PHP, etc.) and communicate with the Fusio core via a simple REST interface, enabling serverless deployments.
  humanURL: https://docs.fusio-project.org/docs/concepts/worker_api
  baseURL: https://www.fusio-project.org/
  tags:
  - Multi-Language
  - REST API
  - Serverless
  - Worker
  properties:
  - type: Documentation
    url: https://docs.fusio-project.org/docs/concepts/worker_api
  - type: GitHubRepository
    url: https://github.com/apioo/fusio-worker-php
name: Fusio
tags:
- API Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Fusio is an open source API management platform which helps to build and manage REST APIs. Fusio provides capabilities for creating, managing, and documenting APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

