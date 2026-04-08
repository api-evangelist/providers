---
aid: gravitee
url: https://raw.githubusercontent.com/api-evangelist/gravitee/refs/heads/main/apis.yml
apis:
- aid: gravitee:gravitee
  name: Gravitee API Management
  description: Gravitee APIM is an open-source, flexible, and fast API management platform that helps organizations control, expose, and analyze their APIs with a full lifecycle management approach.
  humanURL: https://www.gravitee.io/
  tags:
  - API Gateway
  - API Management
  properties:
  - type: Documentation
    url: https://documentation.gravitee.io/
  - type: Getting Started
    url: https://documentation.gravitee.io/apim/getting-started
  - type: Change Log
    url: https://documentation.gravitee.io/apim/release-information/changelog
  - type: GitHubRepository
    url: https://github.com/gravitee-io/gravitee-api-management
  - type: JSON-LD Context
    url: json-ld/gravitee-context.jsonld
  - type: JSON Schema
    url: json-schema/gravitee-api-schema.json
  - type: JSON Schema
    url: json-schema/gravitee-plan-schema.json
- aid: gravitee:gravitee-management-api
  name: Gravitee Management API
  description: The Gravitee Management API provides a RESTful interface for programmatic administration of the Gravitee APIM platform. It exposes endpoints for creating and deploying APIs, managing plans, subscriptions, applications, users, and platform configuration. Two subcomponent versions (V1 and V2) cover both v2 and v4 API management operations.
  humanURL: https://documentation.gravitee.io/apim/configure-and-manage-the-platform/management-api
  baseURL: https://www.gravitee.io/
  tags:
  - Administration
  - Configuration
  - Management
  - REST API
  properties:
  - type: Documentation
    url: https://documentation.gravitee.io/apim/configure-and-manage-the-platform/management-api
  - type: Reference
    url: https://documentation.gravitee.io/apim/management-api-reference
  - type: GitHubRepository
    url: https://github.com/gravitee-io/gravitee-api-management
  - type: OpenAPI
    url: openapi/gravitee-management-api-openapi.yml
  - type: JSON-LD Context
    url: json-ld/gravitee-context.jsonld
  - type: JSON Schema
    url: json-schema/gravitee-api-schema.json
  - type: JSON Schema
    url: json-schema/gravitee-plan-schema.json
- aid: gravitee:gravitee-access-management-api
  name: Gravitee Access Management API
  description: The Gravitee Access Management (AM) API is a RESTful administration interface for the Gravitee AM identity and access management platform. It manages security domains, applications, users, roles, flows, and policies, and is secured using Bearer token authorization.
  humanURL: https://documentation.gravitee.io/am
  baseURL: https://www.gravitee.io/
  tags:
  - Access Management
  - Identity
  - OAuth2
  - REST API
  properties:
  - type: Documentation
    url: https://documentation.gravitee.io/am
  - type: Reference
    url: https://documentation.gravitee.io/am/reference/am-api-reference
  - type: Change Log
    url: https://documentation.gravitee.io/am/releases-and-changelog/release-notes
  - type: GitHubRepository
    url: https://github.com/gravitee-io/gravitee-api-management
  - type: OpenAPI
    url: openapi/gravitee-access-management-api-openapi.yml
  - type: JSON-LD Context
    url: json-ld/gravitee-context.jsonld
  - type: JSON Schema
    url: json-schema/gravitee-domain-schema.json
name: Gravitee
tags:
- API Gateway
- API Management
- GraphQL
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://www.gravitee.io/
  name: 'Gravitee: API Management Platform for APIs, Events & Agents'
  type: Website
  description: 'null'
- url: https://www.gravitee.io/partners
  name: Gravite API Management - Partners
  type: Partners
  description: 'null'
- url: https://www.gravitee.io/pricing
  name: API management pricing - Gravitee
  type: Pricing
  description: 'null'
created: '2025-01-08'
modified: '2026-04-07'
position: Consuming
description: Gravitee.io is an open-source API management platform offering an API gateway, developer portal, and API analytics with support for REST, GraphQL, WebSocket, gRPC, and event-driven APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

