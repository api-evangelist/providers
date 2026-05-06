---
aid: fusio
name: Fusio
description: Fusio is an open source API management platform which helps to build and manage REST APIs. It provides capabilities for creating, managing, and documenting APIs with a built-in developer portal, marketplace, and support for multiple programming languages through worker processes.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-16'
modified: '2026-04-18'
position: Consumer
tags:
  - API Management
  - Open Source
  - REST API
url: https://raw.githubusercontent.com/api-evangelist/fusio/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
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
      - type: APIReference
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
common:
  - type: Documentation
    url: https://docs.fusio-project.org/
  - type: GettingStarted
    url: https://docs.fusio-project.org/docs/bootstrap
  - type: Blog
    url: https://www.fusio-project.org/blog
  - type: ChangeLog
    url: https://github.com/apioo/fusio/blob/master/CHANGELOG.md
  - type: GitHubOrganization
    url: https://github.com/apioo
  - type: GitHubRepository
    url: https://github.com/apioo/fusio
  - type: Support
    url: https://discord.com/invite/eMrMgwsc6e
  - type: Marketplace
    url: https://www.fusio-project.org/marketplace
  - type: SDK
    url: https://docs.fusio-project.org/docs/backend/development/sdk
  - type: Features
    data:
      - name: API Gateway
        description: Route and manage incoming API requests with built-in rate limiting and authentication.
      - name: Developer Portal
        description: Self-service developer portal for API consumers to register, browse APIs, and manage access tokens.
      - name: Multi-Language Workers
        description: Execute API action logic in JavaScript, Python, Java, PHP, and other languages through worker processes.
      - name: Marketplace
        description: Browse and install pre-built API actions and adapters from the Fusio marketplace.
      - name: Schema Management
        description: Define and manage API request and response schemas using TypeSchema format.
      - name: OAuth2 Authentication
        description: Built-in OAuth2 server for securing APIs with token-based authentication.
      - name: Rate Limiting
        description: Configure per-app and per-user rate limits to protect API resources.
      - name: Webhook Support
        description: Define webhook subscriptions to notify consumers of events.
  - type: UseCases
    data:
      - name: API Product Building
        description: Build and publish API products with documentation, authentication, and developer onboarding.
      - name: Microservices Gateway
        description: Use Fusio as an API gateway in front of microservices for unified access control.
      - name: Data Integration
        description: Connect to databases and external APIs to build data integration endpoints.
      - name: Serverless API Backend
        description: Build API backends that execute logic in multiple languages without managing servers.
  - type: Integrations
    data:
      - name: MySQL and PostgreSQL
        description: Connect to MySQL and PostgreSQL databases as data sources for API endpoints.
      - name: MongoDB
        description: Use MongoDB as a NoSQL data source for API endpoints.
      - name: Elasticsearch
        description: Integrate with Elasticsearch for search-powered API endpoints.
      - name: RabbitMQ
        description: Use RabbitMQ for asynchronous message processing in API workflows.
      - name: Docker
        description: Deploy Fusio and worker containers using Docker and Docker Compose.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
