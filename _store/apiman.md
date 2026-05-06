---
aid: apiman
name: Apiman
description: Apiman is an open source API management platform featuring a REST API, manager UI, and standalone developer portal with multi-tenancy, events, notifications, permissions, and approval workflows. It provides extensible API gateway capabilities through a simple Java plugin architecture with support for policies, plans, organizations, and client management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - API Management
  - Developer Portal
  - Java
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/apiman/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apiman:apiman
    name: Apiman
    description: Apiman is an open source API management platform with a developer portal, API gateway, and management UI supporting policies, plans, organizations, multi-tenancy, and extensible Java-based plugin architecture.
    humanURL: https://github.com/apiman/apiman
    baseURL: https://localhost:8080/apiman
    tags:
      - API Gateway
      - API Management
      - Developer Portal
      - Open Source
    properties:
      - type: Documentation
        url: https://www.apiman.io/api-manager/latest/index.html
      - type: GitHubRepository
        url: https://github.com/apiman/apiman
      - type: JSONSchema
        url: json-schema/apiman-api-schema.json
      - type: JSONSchema
        url: json-schema/apiman-plan-schema.json
      - type: JSON-LD
        url: json-ld/apiman-context.jsonld
common:
  - type: Website
    url: https://www.apiman.io
  - type: Documentation
    url: https://www.apiman.io/api-manager/latest/index.html
  - type: GitHubOrganization
    url: https://github.com/apiman
  - type: GitHubRepository
    url: https://github.com/apiman/apiman
  - type: Features
    data:
      - name: REST API Manager
        description: Full REST API for managing organizations, APIs, plans, clients, and policies programmatically.
      - name: API Gateway
        description: Extensible API gateway that enforces policies at runtime for authentication, rate limiting, and transformation.
      - name: Developer Portal
        description: Standalone developer portal for API discovery, documentation, and self-service subscription management.
      - name: Policy Engine
        description: Pluggable Java-based policy engine supporting rate limiting, quotas, IP whitelisting, authentication, and custom policies.
      - name: Multi-Tenancy
        description: Organization-based multi-tenancy allowing separate API management namespaces within a single platform.
      - name: Approval Workflows
        description: Configurable approval workflows for API subscriptions with notification and event support.
  - type: UseCases
    data:
      - name: On-Premise API Management
        description: Deploy Apiman on-premise to manage APIs across internal services with full control over infrastructure.
      - name: Developer Portal Hosting
        description: Provide developers with a self-service portal for discovering and subscribing to APIs.
      - name: API Policy Enforcement
        description: Enforce security, rate limiting, and transformation policies on API traffic through the gateway.
      - name: Multi-Team API Governance
        description: Use organizations and plans to provide isolated API management environments for multiple teams.
  - type: Solutions
    data:
      - name: Open Source
        description: Free, Apache-licensed API management platform deployable on any JVM-based infrastructure.
      - name: Vert.x Gateway
        description: High-performance async API gateway implementation using Eclipse Vert.x.
      - name: WildFly Overlay
        description: Apiman overlay for WildFly/EAP application server deployments.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
