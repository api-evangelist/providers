---
aid: tyk
url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/apis.yml
apis:
- aid: tyk:tyk
  name: Tyk Gateway
  description: Tyk Gateway is a fast and scalable open-source API gateway that supports REST, GraphQL, gRPC, and async APIs with rate limiting, authentication, analytics, and a developer portal.
  humanURL: https://tyk.io/
  tags:
  - API Gateway
  - Open Source
  properties:
  - type: Documentation
    url: https://tyk.io/docs/
  - type: Getting Started
    url: https://tyk.io/docs/tyk-oss-gateway/
  - type: OpenAPI
    url: openapi/tyk-gateway-api-openapi.yml
  - type: Change Log
    url: https://tyk.io/docs/developer-support/release-notes/dashboard
  - type: GitHubRepository
    url: https://github.com/TykTechnologies/tyk
- aid: tyk:tyk-gateway-api
  name: Tyk Gateway API
  description: The Tyk Gateway API provides a RESTful interface for managing API definitions, keys, certificates, and health checks directly on a Tyk Gateway node. It is used to configure and operate the gateway programmatically in self-managed and open-source deployments.
  humanURL: https://tyk.io/docs/tyk-apis/
  baseURL: https://tyk.io/
  tags:
  - Administration
  - Gateway
  - Open Source
  - REST API
  properties:
  - type: Documentation
    url: https://tyk.io/docs/tyk-apis/
  - type: OpenAPI
    url: openapi/tyk-gateway-api-openapi.yml
  - type: GitHubRepository
    url: https://github.com/TykTechnologies/tyk
- aid: tyk:tyk-dashboard-api
  name: Tyk Dashboard API
  description: The Tyk Dashboard API is a superset of the Gateway API providing programmatic access to a centralized database of API definitions, keys, policies, users, and organizations. It is the primary integration point for managing multi-team Tyk deployments and is authenticated via an access credentials header.
  humanURL: https://tyk.io/docs/tyk-dashboard-api
  baseURL: https://tyk.io/
  tags:
  - Administration
  - Dashboard
  - Management
  - REST API
  properties:
  - type: Documentation
    url: https://tyk.io/docs/tyk-dashboard-api
  - type: OpenAPI
    url: openapi/tyk-dashboard-api-openapi.yml
  - type: Change Log
    url: https://tyk.io/docs/developer-support/release-notes/dashboard
  - type: GitHubRepository
    url: https://github.com/TykTechnologies/tyk-analytics
- aid: tyk:tyk-dashboard-admin-api
  name: Tyk Dashboard Admin API
  description: The Tyk Dashboard Admin API provides super-administrative access to the Tyk Dashboard, enabling management of organizations and system-level configuration. It is used for bootstrapping and managing multi-organization Tyk deployments.
  humanURL: https://tyk.io/docs/tyk-dashboard-api
  baseURL: https://tyk.io/
  tags:
  - Admin
  - Dashboard
  - Multi-Tenant
  - REST API
  properties:
  - type: Documentation
    url: https://tyk.io/docs/tyk-dashboard-api
  - type: OpenAPI
    url: openapi/tyk-dashboard-admin-api-openapi.yml
  - type: GitHubRepository
    url: https://github.com/TykTechnologies/tyk-analytics
- aid: tyk:tyk-mdcb-api
  name: Tyk MDCB API
  description: The Tyk Multi Data Centre Bridge (MDCB) API enables synchronization of API configurations, keys, and policies across geographically distributed Tyk Gateway clusters. It provides a control plane for managing multiple data center deployments from a single Tyk Dashboard.
  humanURL: https://tyk.io/docs/
  baseURL: https://tyk.io/
  tags:
  - MDCB
  - Multi-Data Center
  - REST API
  - Synchronization
  properties:
  - type: Documentation
    url: https://tyk.io/docs/
  - type: OpenAPI
    url: openapi/tyk-mdcb-api-openapi.yml
  - type: GitHubRepository
    url: https://github.com/TykTechnologies/tyk-sink
name: Tyk
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://tyk.io/
  name: API Management Platform & API Gateway | Tyk.io
  type: Website
  description: 'null'
- url: https://tyk.io/pricing/
  name: Pricing - Tyk API Management
  type: Pricing
  description: 'null'
- url: https://tyk.io/blog/
  name: Tyk API Expertise Blog - Tyk API Gateway and API Management
  type: Blog
  description: 'null'
- url: https://tyk.io/all-about-apis-podcast/
  name: All about apis podcast - Tyk API Management
  type: Podcast
  description: 'null'
- url: https://tyk.io/case-studies/
  name: Case Studies Archive - Tyk API Management
  type: CaseStudies
  description: 'null'
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Tyk is an open-source API gateway and management platform supporting REST, GraphQL, gRPC, and Async APIs with a developer portal, analytics, and flexible deployment across cloud, on-premise, and hybrid environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

