---
aid: tyk
name: Tyk
description: Tyk is an open-source API gateway and management platform supporting REST, GraphQL, gRPC, and Async APIs with a developer portal, analytics, and flexible deployment across cloud, on-premise, and hybrid environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - API Management
  - GraphQL
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/tyk/refs/heads/main/apis.yml
humanURL: https://tyk.io/
created: '2026-03-18'
modified: '2026-04-19'
specificationVersion: '0.19'
access: 3rd-Party
position: Consuming
apis:
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
      - type: JSONSchema
        url: json-schema/tyk-gateway-access-definition-schema.json
      - type: JSONLD
        url: json-ld/tyk-gateway-context.jsonld
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
      - type: ChangeLog
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
      - type: JSONSchema
        url: json-schema/tyk-mdcb-data-plane-config-schema.json
      - type: JSONLD
        url: json-ld/tyk-mdcb-context.jsonld
      - type: GitHubRepository
        url: https://github.com/TykTechnologies/tyk-sink
common:
  - type: Portal
    url: https://tyk.io/
  - type: Documentation
    url: https://tyk.io/docs/
  - type: GettingStarted
    url: https://tyk.io/docs/getting-started/
  - type: Authentication
    url: https://tyk.io/docs/basic-config-and-security/security/authentication-authorization/
  - type: Blog
    url: https://tyk.io/blog/
  - type: ChangeLog
    url: https://tyk.io/docs/developer-support/release-notes/dashboard
  - type: GitHubOrganization
    url: https://github.com/TykTechnologies
  - type: GitHubRepository
    url: https://github.com/TykTechnologies/tyk
  - type: Support
    url: https://community.tyk.io/
  - type: FAQ
    url: https://tyk.io/docs/frequently-asked-questions/
  - type: Pricing
    url: https://tyk.io/price-comparison/
  - type: CLI
    url: https://github.com/TykTechnologies/tyk-cli
  - type: SDK
    url: https://github.com/TykTechnologies/tyk
    title: Go Gateway SDK
  - type: SpectralRules
    url: rules/tyk-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/tyk-vocabulary.yaml
  - type: Features
    data:
      - name: API Gateway
        description: High-performance, open-source API gateway supporting REST, GraphQL, gRPC, TCP, and async APIs with low-latency request proxying.
      - name: Rate Limiting
        description: Configurable rate limiting and throttling policies to protect backend services from traffic spikes and abuse.
      - name: Authentication
        description: Multiple authentication methods including API keys, JWT, OAuth 2.0, mutual TLS, OpenID Connect, and basic auth.
      - name: Analytics and Monitoring
        description: Real-time API analytics, traffic monitoring, and detailed logging with export to multiple backend stores.
      - name: Developer Portal
        description: Customizable developer portal for API documentation, key management, and developer onboarding.
      - name: GraphQL Support
        description: Native GraphQL proxy and Universal Data Graph for federating REST and GraphQL APIs into a single graph endpoint.
      - name: API Versioning
        description: Built-in support for API versioning with URL, header, and query parameter-based version routing.
      - name: Policy Management
        description: Centralized access control policies for managing rate limits, quotas, and access rights across multiple APIs.
      - name: Multi Data Center
        description: MDCB enables synchronization of API configurations and keys across geographically distributed gateway clusters.
      - name: Plugin System
        description: Extensible middleware plugin system supporting Go, Python, JavaScript, Lua, and gRPC-based custom plugins.
      - name: AI Gateway
        description: Tyk AI Studio provides an AI gateway for managing, governing, and interacting with AI models across your organization.
  - type: UseCases
    data:
      - name: API Monetization
        description: Enable API-as-a-product strategies with tiered plans, usage tracking, and developer self-service through the portal.
      - name: Microservices Gateway
        description: Centralize traffic management, authentication, and observability for microservices architectures.
      - name: Multi-Cloud API Management
        description: Deploy gateways across cloud, on-premise, and hybrid environments with centralized management.
      - name: Legacy API Modernization
        description: Wrap legacy SOAP and XML APIs with modern REST or GraphQL interfaces using Tyk's transformation middleware.
      - name: Partner API Program
        description: Manage third-party developer access with fine-grained policies, quota management, and analytics per consumer.
      - name: AI API Management
        description: Govern and manage AI model APIs with rate limiting, access control, and usage analytics through Tyk AI Studio.
  - type: Integrations
    data:
      - name: Kubernetes
        description: Tyk Operator provides native Kubernetes integration for managing API definitions and policies as custom resources.
      - name: Terraform
        description: Infrastructure-as-code provider for managing Tyk configurations through Terraform.
      - name: Keycloak
        description: Integration with Keycloak for OAuth 2.0 and OpenID Connect authentication flows.
      - name: Auth0
        description: Support for Auth0 as an identity provider for JWT validation and OAuth 2.0 token management.
      - name: Prometheus
        description: Export gateway metrics to Prometheus for monitoring and alerting with Grafana dashboards.
      - name: OpenTelemetry
        description: Distributed tracing integration with OpenTelemetry for end-to-end request visibility.
      - name: Backstage
        description: Backstage plugin for viewing and managing Tyk API definitions from within the Backstage developer portal.
      - name: Jenkins
        description: CI/CD integration for automated API deployment and configuration updates through Jenkins pipelines.
      - name: Ansible
        description: Ansible playbooks for automated Tyk gateway and dashboard provisioning and configuration.
      - name: Helm Charts
        description: Official Helm charts for deploying Tyk components on Kubernetes clusters.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
