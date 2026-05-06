---
aid: apollo-config
name: Apollo Config
description: Apollo is a reliable, open-source configuration management system suitable for microservice configuration management scenarios, providing centralized configuration management, real-time updates, versioning, and multi-environment support. Originally developed by Ctrip, now maintained by the apolloconfig community under Apache 2.0 license.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache 2.0
  - Configuration Management
  - Ctrip
  - Distributed Systems
  - Java
  - Microservices
  - Open Source
  - Real-Time Configuration
url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apollo-config:apollo-config
    name: Apollo Config
    description: Apollo is a reliable, open-source configuration management system suitable for microservice configuration management scenarios, providing centralized configuration management, real-time updates, versioning, and multi-environment support. The Open API provides programmatic access to app management, namespace management, configuration publishing, and release management including gray releases.
    humanURL: https://www.apolloconfig.com/
    tags:
      - Apache 2.0
      - Configuration Management
      - Distributed Systems
      - Java
      - Microservices
      - Open Source
      - Real-Time Configuration
    baseURL: http://localhost:8070
    properties:
      - type: Documentation
        url: https://www.apolloconfig.com/#/en/portal/apollo-open-api-platform
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/openapi/apollo-open-api.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/json-schema/apollo-open-api-app-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/json-schema/apollo-open-api-cluster-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/json-schema/apollo-open-api-namespace-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/json-schema/apollo-open-api-item-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/json-schema/apollo-open-api-release-schema.json
common:
  - type: Documentation
    url: https://www.apolloconfig.com/#/en/
  - type: GettingStarted
    url: https://www.apolloconfig.com/#/en/deployment/quick-start
  - type: GitHubRepository
    url: https://github.com/apolloconfig/apollo
  - type: GitHubOrganization
    url: https://github.com/apolloconfig
  - type: ReleaseNotes
    url: https://github.com/apolloconfig/apollo/releases
  - type: Support
    url: https://github.com/apolloconfig/apollo/issues
  - type: SDK
    url: https://github.com/apolloconfig/apollo-java
    title: Java SDK
  - type: SDK
    url: https://github.com/apolloconfig/apollo.net
    title: .NET SDK
  - type: SDK
    url: https://github.com/apolloconfig/agollo
    title: Go SDK
  - type: CodeExamples
    url: https://github.com/apolloconfig/apollo-demo-java
    title: Java Demo
  - type: CodeExamples
    url: https://github.com/apolloconfig/apollo-use-cases
    title: Use Cases
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/apollo-config/refs/heads/main/json-ld/apollo-config-open-api-context.jsonld
  - type: Features
    data:
      - name: Centralized Configuration Management
        description: Centralize configuration for all microservices in one place with real-time push updates.
      - name: Real-Time Configuration Updates
        description: Push configuration changes to all clients instantly without application restarts.
      - name: Multi-Environment Support
        description: Manage configurations across DEV, FAT, UAT, and PRO environments independently.
      - name: Versioning and History
        description: Track configuration changes with full version history and rollback capability.
      - name: Gray Release Support
        description: Gradually roll out configuration changes to a subset of instances.
      - name: Namespace Management
        description: Organize configurations into namespaces supporting properties, JSON, YAML, XML, and text formats.
      - name: Cluster Management
        description: Manage configuration at the cluster level for multi-cluster deployments.
      - name: Open API
        description: REST API for programmatic configuration management and automation.
      - name: Kubernetes Operator
        description: Kubernetes Operator for automated Apollo deployment in container environments.
      - name: Helm Chart Deployment
        description: Official Helm chart for Kubernetes deployments.
  - type: UseCases
    data:
      - name: Microservice Configuration
        description: Manage centralized configuration for distributed microservice architectures.
      - name: Multi-Environment Configuration
        description: Maintain separate configurations for development, testing, staging, and production.
      - name: Dynamic Configuration Updates
        description: Update application configuration at runtime without redeployment.
      - name: Configuration Audit
        description: Track who changed what configuration and when with full audit trail.
      - name: Kubernetes Configuration Management
        description: Manage configuration for containerized applications deployed on Kubernetes.
  - type: Integrations
    data:
      - name: Java
        description: Official Java client library via apollo-java SDK.
      - name: .NET
        description: Official .NET client library via apollo.net SDK.
      - name: Go
        description: Go client library via agollo SDK.
      - name: Kubernetes
        description: Apollo Operator and Helm chart for Kubernetes deployment.
      - name: Spring Boot
        description: Spring Boot integration via Java SDK for auto-configuration refresh.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
