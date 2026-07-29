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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Fusio Backend API provides a REST interface to configure and manage all aspects of a Fusio API management instance. It covers operations, routes, schemas, actions, connections, apps, users, and ma
  name: Fusio Backend API
  slug: fusio-backend-api
- description: The Fusio Consumer API is used by the developer portal application and enables third-party developers to request access tokens, manage their apps, and interact with protected API endpoints. It provide
  name: Fusio Consumer API
  slug: fusio-consumer-api
- description: The Fusio Worker API enables executing API action logic in multiple programming languages by forwarding requests to external worker processes. Workers are implemented in the target language (JavaScrip
  name: Fusio Worker API
  slug: fusio-worker-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fusio-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fusio-project.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fusio-project.org/docs/bootstrap
- group: company
  title: ''
  type: Blog
  url: https://www.fusio-project.org/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apioo/fusio/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apioo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apioo/fusio
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/eMrMgwsc6e
- group: other
  title: ''
  type: Marketplace
  url: https://www.fusio-project.org/marketplace
- group: build
  title: ''
  type: SDKs
  url: https://docs.fusio-project.org/docs/backend/development/sdk
created: '2026-03-16'
description: Fusio is an open source API management platform which helps to build and manage REST APIs. It provides capabilities for creating, managing, and documenting APIs with a built-in developer portal, marketplace, and support for multiple programming languages through worker processes.
features:
- description: Route and manage incoming API requests with built-in rate limiting and authentication.
  name: API Gateway
- description: Self-service developer portal for API consumers to register, browse APIs, and manage access tokens.
  name: Developer Portal
- description: Execute API action logic in JavaScript, Python, Java, PHP, and other languages through worker processes.
  name: Multi-Language Workers
- description: Browse and install pre-built API actions and adapters from the Fusio marketplace.
  name: Marketplace
- description: Define and manage API request and response schemas using TypeSchema format.
  name: Schema Management
- description: Built-in OAuth2 server for securing APIs with token-based authentication.
  name: OAuth2 Authentication
- description: Configure per-app and per-user rate limits to protect API resources.
  name: Rate Limiting
- description: Define webhook subscriptions to notify consumers of events.
  name: Webhook Support
finops:
- name: Fusio Finops
  service_category: API
  slug: fusio-finops
image: /assets/icons/fusio.png
integrations:
- description: Connect to MySQL and PostgreSQL databases as data sources for API endpoints.
  name: MySQL and PostgreSQL
- description: Use MongoDB as a NoSQL data source for API endpoints.
  name: MongoDB
- description: Integrate with Elasticsearch for search-powered API endpoints.
  name: Elasticsearch
- description: Use RabbitMQ for asynchronous message processing in API workflows.
  name: RabbitMQ
- description: Deploy Fusio and worker containers using Docker and Docker Compose.
  name: Docker
layout: provider
modified: '2026-04-18'
name: Fusio
nav: Providers
network: true
overview: 'Fusio publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Management, Open Source, and REST API.


  Fusio''s developer surface includes documentation, getting-started guide, engineering blog, changelog, support, and 5 more developer resources.'
plans:
- name: Fusio Plans Pricing
  plan_count: 3
  slug: fusio-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Fusio Rate Limits
  slug: fusio-rate-limits
score:
  band: emerging
  composite: 27.7
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fusio/refs/heads/main/screenshots/fusio-2026-06-20T181622.png
security:
- kind: domain-security
  name: Fusio Domain Security
  slug: fusio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fusio
tags:
- API Management
- Open Source
- REST API
use_cases:
- description: Build and publish API products with documentation, authentication, and developer onboarding.
  name: API Product Building
- description: Use Fusio as an API gateway in front of microservices for unified access control.
  name: Microservices Gateway
- description: Connect to databases and external APIs to build data integration endpoints.
  name: Data Integration
- description: Build API backends that execute logic in multiple languages without managing servers.
  name: Serverless API Backend
---
