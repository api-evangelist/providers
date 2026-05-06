---
aid: backstage
url: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/apis.yml
apis:
  - aid: backstage:catalog-api
    name: Backstage Catalog API
    tags:
      - Developer Portal
      - Entities
      - Software Catalog
    humanURL: https://backstage.io/docs/features/software-catalog/software-catalog-api/
    properties:
      - url: https://backstage.io/docs/features/software-catalog/software-catalog-api/
        type: Documentation
      - url: openapi/backstage-catalog-openapi.yml
        type: OpenAPI
    description: The Backstage Software Catalog REST API provides JSON-based endpoints for managing and querying catalog entities, locations, and related metadata. The catalog stores information about all software components, APIs, resources, systems, domains, groups, and users in an organization. Supports entity CRUD, filtering, full-text search, cursor-based pagination, faceted queries, location management, entity validation, and ancestry lookups.
  - aid: backstage:scaffolder-api
    name: Backstage Scaffolder API
    tags:
      - Developer Portal
      - Scaffolding
      - Software Templates
    humanURL: https://backstage.io/docs/features/software-templates/
    properties:
      - url: https://backstage.io/docs/features/software-templates/
        type: Documentation
      - url: openapi/backstage-scaffolder-openapi.yml
        type: OpenAPI
    description: The Backstage Scaffolder (Software Templates) REST API provides endpoints for creating, managing, and monitoring scaffolder tasks. It enables programmatic execution of software templates to bootstrap new projects, components, and other software assets. Supports task creation and cancellation, real-time event streaming, log retrieval, template parameter schema inspection, available action listing, and dry-run execution for template validation.
  - aid: backstage:auth-api
    name: Backstage Auth API
    tags:
      - Authentication
      - Developer Portal
      - OAuth
    humanURL: https://backstage.io/docs/auth/
    properties:
      - url: https://backstage.io/docs/auth/
        type: Documentation
      - url: openapi/backstage-auth-openapi.yml
        type: OpenAPI
    description: The Backstage Auth API provides endpoints for authenticating users and services with the Backstage backend. It supports multiple authentication providers (GitHub, Google, Okta, SAML, etc.) and handles OAuth flows, token issuance, token refresh, and session management. The Auth API is used by the Backstage frontend to initiate login flows and by backend plugins to verify caller identity via Backstage tokens.
  - aid: backstage:techdocs-api
    name: Backstage TechDocs API
    tags:
      - Developer Portal
      - Documentation
      - TechDocs
    humanURL: https://backstage.io/docs/features/techdocs/
    properties:
      - url: https://backstage.io/docs/features/techdocs/
        type: Documentation
      - url: openapi/backstage-techdocs-openapi.yml
        type: OpenAPI
    description: The Backstage TechDocs API provides endpoints for generating, publishing, and serving technical documentation for catalog entities. TechDocs uses MkDocs under the hood to render Markdown documentation into static HTML pages. The API supports fetching rendered documentation, syncing docs from external storage, retrieving metadata, and managing documentation lifecycle.
  - aid: backstage:search-api
    name: Backstage Search API
    tags:
      - Developer Portal
      - Discovery
      - Search
    humanURL: https://backstage.io/docs/features/search/
    properties:
      - url: https://backstage.io/docs/features/search/
        type: Documentation
      - url: openapi/backstage-search-openapi.yml
        type: OpenAPI
    description: The Backstage Search API provides endpoints for querying the Backstage search index. It enables full-text search across all indexed content including catalog entities, TechDocs pages, and any other content indexed by search collators. The API supports filtering by document type, pagination via cursors, and term-based queries.
  - aid: backstage:permissions-api
    name: Backstage Permissions API
    tags:
      - Authorization
      - Developer Portal
      - Permissions
    humanURL: https://backstage.io/docs/permissions/overview
    properties:
      - url: https://backstage.io/docs/permissions/overview
        type: Documentation
      - url: openapi/backstage-permissions-openapi.yml
        type: OpenAPI
    description: The Backstage Permissions API provides endpoints for evaluating and managing authorization decisions within Backstage. It enables plugins to check whether a given user or service has permission to perform a specific action. The framework supports policy-based authorization with conditional rules that can be applied to resources.
  - aid: backstage:events-system
    name: Backstage Events System
    tags:
      - Developer Portal
      - Events
      - Webhooks
    humanURL: https://backstage.io/docs/plugins/backends-and-plugins/
    properties:
      - url: https://backstage.io/docs/plugins/backends-and-plugins/
        type: Documentation
      - url: asyncapi/backstage-events-asyncapi.yml
        type: AsyncAPI
    description: The Backstage Events system provides a publish-subscribe mechanism for broadcasting and consuming events within a Backstage instance. It enables plugins to emit events when significant actions occur (such as catalog entity changes, scaffolder task completions, or permission policy updates) and allows other plugins or external systems to subscribe to those events via HTTP webhooks or the internal event bus.
name: Backstage
tags:
  - Developer Portal
  - Internal Developer Platform
  - Software Catalog
  - Open Source
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://backstage.io/
    name: Backstage Website
    type: Website
    description: 'null'
  - url: https://backstage.io/docs/
    name: Backstage Documentation
    type: Documentation
    description: 'null'
  - url: https://backstage.io/docs/getting-started/
    name: Backstage Getting Started
    type: Getting Started
    description: 'null'
  - url: https://backstage.io/blog/
    name: Backstage Blog
    type: Blog
    description: 'null'
  - url: https://github.com/backstage
    name: Backstage GitHub Organization
    type: GitHub Organization
    description: 'null'
  - url: https://github.com/backstage/backstage
    name: Backstage GitHub Repository
    type: GitHubRepository
    description: 'null'
  - url: https://github.com/backstage/backstage/releases
    name: Backstage Releases
    type: Change Log
    description: 'null'
  - url: https://discord.gg/backstage-687207715902193673
    name: Backstage Discord Community
    type: Community
    description: 'null'
  - url: https://backstage.io/plugins/
    name: Backstage Plugin Directory
    type: Developer Tools
    description: 'null'
  - type: JSONSchema
    url: json-schema/backstage-entity-schema.json
    name: Backstage Entity JSON Schema
    description: 'null'
  - type: JSON-LD
    url: json-ld/backstage-context.jsonld
    name: Backstage JSON-LD Context
    description: 'null'
  - type: SpectralRules
    url: rules/backstage-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/backstage-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/developer-portal.yaml
  - name: Features
    type: Features
    data:
      - name: Software Catalog
        description: Central inventory of all software components, APIs, resources, systems, domains, groups, and users.
      - name: Software Templates (Scaffolder)
        description: Bootstrap new projects, services, and components from customizable templates.
      - name: TechDocs
        description: Render and serve MkDocs-based technical documentation alongside catalog entities.
      - name: Plugin Ecosystem
        description: Extensible plugin architecture with 100+ open-source plugins for CI/CD, monitoring, cloud, and more.
      - name: Search
        description: Full-text search across catalog entities, TechDocs, and any other indexed content.
      - name: Permissions Framework
        description: Policy-based authorization with conditional rules for resource-level access control.
      - name: Entity Relations
        description: Model ownership, dependencies, and API consumption relationships between services.
  - name: UseCases
    type: UseCases
    data:
      - name: Internal Developer Portal
        description: Build a unified portal for developers to discover services, read docs, and scaffold projects.
      - name: Service Catalog
        description: Maintain a complete, up-to-date inventory of all microservices, APIs, and infrastructure.
      - name: Developer Onboarding
        description: Accelerate new developer onboarding with self-service project scaffolding and documentation.
      - name: API Governance
        description: Track all internal and external APIs, their owners, and documentation in one place.
  - name: Integrations
    type: Integrations
    data:
      - name: GitHub
        description: Catalog ingestion from GitHub repos, GitHub Actions integration for CI/CD visibility.
      - name: PagerDuty
        description: Show on-call information and incident status on catalog entity pages.
      - name: Kubernetes
        description: Display Kubernetes workload status for catalog entities.
      - name: Prometheus
        description: Show metrics and alerts for services directly in the catalog.
      - name: Snyk
        description: Display security vulnerability information for catalog entities.
      - name: Datadog
        description: Surface monitoring dashboards within Backstage.
created: '2024-12-01'
modified: '2026-04-21'
position: Consumer
description: Backstage is an open-source developer portal platform created by Spotify. It provides a centralized software catalog, software templates (scaffolder), TechDocs, and a plugin ecosystem for building customizable developer portals. Backstage helps organizations manage their software ecosystem by cataloging services, APIs, resources, and infrastructure, and provides tooling for creating new projects from templates.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
