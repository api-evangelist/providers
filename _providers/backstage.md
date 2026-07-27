---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Backstage Agentic Access
  operation_count: 38
  slug: backstage-agentic-access
  summary_line: 38 operations · 14 acting
api_count: 13
apis:
- description: The Backstage Events system provides a publish-subscribe mechanism for broadcasting and consuming events within a Backstage instance. It enables plugins to emit events when significant actions occur (
  name: Backstage Events System
  slug: events-system
- description: Endpoints for listing available scaffolder actions.
  name: Backstage Actions API
  slug: backstage-actions-api
- description: The Authentication API from Backstage — 4 operation(s) for authentication.
  name: Backstage Authentication API
  slug: backstage-authentication-api
- description: The Authorization API from Backstage — 2 operation(s) for authorization.
  name: Backstage Authorization API
  slug: backstage-authorization-api
- description: The Documentation API from Backstage — 2 operation(s) for documentation.
  name: Backstage Documentation API
  slug: backstage-documentation-api
- description: Endpoints for managing and querying catalog entities.
  name: Backstage Entities API
  slug: backstage-entities-api
- description: Endpoints for managing catalog locations (entity sources).
  name: Backstage Locations API
  slug: backstage-locations-api
- description: The Metadata API from Backstage — 2 operation(s) for metadata.
  name: Backstage Metadata API
  slug: backstage-metadata-api
- description: The Search API from Backstage — 1 operation(s) for search.
  name: Backstage Search API
  slug: backstage-search-api
- description: The Sync API from Backstage — 1 operation(s) for sync.
  name: Backstage Sync API
  slug: backstage-sync-api
- description: Endpoints for creating and managing scaffolder tasks.
  name: Backstage Tasks API
  slug: backstage-tasks-api
- description: Endpoints for template metadata and parameter schemas.
  name: Backstage Templates API
  slug: backstage-templates-api
- description: The Token Verification API from Backstage — 1 operation(s) for token verification.
  name: Backstage Token Verification API
  slug: backstage-token-verification-api
artifact_total: 95
asyncapis:
- description: The Backstage Events system provides a publish-subscribe mechanism for broadcasting and consuming events within a Backstage instance. It enables plugins to emit events when significant actions occur (
  name: Backstage Events System
  slug: backstage-events-asyncapi
collections:
- collection_type: open
  name: Backstage Auth API
  slug: open-backstage-auth
- collection_type: open
  name: Backstage Catalog API
  slug: open-backstage-catalog
- collection_type: open
  name: Backstage Permissions API
  slug: open-backstage-permissions
- collection_type: open
  name: Backstage Scaffolder API
  slug: open-backstage-scaffolder
- collection_type: open
  name: Backstage Search API
  slug: open-backstage-search
- collection_type: open
  name: Backstage TechDocs API
  slug: open-backstage-techdocs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/backstage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/backstage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/backstage-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/backstage-from-spotify
- group: company
  title: ''
  type: Website
  url: https://backstage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://backstage.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://backstage.io/docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://backstage.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/backstage
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/backstage/backstage
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/backstage/backstage/releases
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/backstage-687207715902193673
- group: build
  title: ''
  type: Developer Tools
  url: https://backstage.io/plugins/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/backstage-entity-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/backstage-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/backstage-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/backstage-vocabulary.yaml
created: '2024-12-01'
description: Backstage is an open-source developer portal platform created by Spotify. It provides a centralized software catalog, software templates (scaffolder), TechDocs, and a plugin ecosystem for building customizable developer portals. Backstage helps organizations manage their software ecosystem by cataloging services, APIs, resources, and infrastructure, and provides tooling for creating new projects from templates.
examples:
- key_count: 3
  name: Auth Auth Response Example
  slug: auth-auth-response-example
- key_count: 1
  name: Auth Jwks Response Example
  slug: auth-jwks-response-example
- key_count: 6
  name: Backstage Entity Example
  slug: backstage-entity-example
- key_count: 6
  name: Catalog Entity Example
  slug: catalog-entity-example
- key_count: 10
  name: Catalog Entity Metadata Example
  slug: catalog-entity-metadata-example
- key_count: 2
  name: Catalog Entity Relation Example
  slug: catalog-entity-relation-example
- key_count: 3
  name: Catalog Location Example
  slug: catalog-location-example
- key_count: 3
  name: Permissions Conditional Request Example
  slug: permissions-conditional-request-example
- key_count: 4
  name: Permissions Permission Decision Example
  slug: permissions-permission-decision-example
- key_count: 2
  name: Permissions Permission Request Example
  slug: permissions-permission-request-example
- key_count: 3
  name: Scaffolder Action Example
  slug: scaffolder-action-example
- key_count: 7
  name: Scaffolder Task Example
  slug: scaffolder-task-example
- key_count: 3
  name: Search Search Document Example
  slug: search-search-document-example
- key_count: 4
  name: Search Search Result Example
  slug: search-search-result-example
- key_count: 4
  name: Search Search Result Set Example
  slug: search-search-result-set-example
- key_count: 5
  name: Techdocs Tech Docs Metadata Example
  slug: techdocs-tech-docs-metadata-example
features:
- description: Central inventory of all software components, APIs, resources, systems, domains, groups, and users.
  name: Software Catalog
- description: Bootstrap new projects, services, and components from customizable templates.
  name: Software Templates (Scaffolder)
- description: Render and serve MkDocs-based technical documentation alongside catalog entities.
  name: TechDocs
- description: Extensible plugin architecture with 100+ open-source plugins for CI/CD, monitoring, cloud, and more.
  name: Plugin Ecosystem
- description: Full-text search across catalog entities, TechDocs, and any other indexed content.
  name: Search
- description: Policy-based authorization with conditional rules for resource-level access control.
  name: Permissions Framework
- description: Model ownership, dependencies, and API consumption relationships between services.
  name: Entity Relations
finops:
- name: Backstage Finops
  service_category: Developer Tools
  slug: backstage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/backstage.png
integrations:
- description: Catalog ingestion from GitHub repos, GitHub Actions integration for CI/CD visibility.
  name: GitHub
- description: Show on-call information and incident status on catalog entity pages.
  name: PagerDuty
- description: Display Kubernetes workload status for catalog entities.
  name: Kubernetes
- description: Show metrics and alerts for services directly in the catalog.
  name: Prometheus
- description: Display security vulnerability information for catalog entities.
  name: Snyk
- description: Surface monitoring dashboards within Backstage.
  name: Datadog
json_schemas:
- name: AuthResponse
  property_count: 3
  slug: auth-auth-response
- name: JwksResponse
  property_count: 1
  slug: auth-jwks-response
- name: Backstage Catalog Entity
  property_count: 6
  slug: backstage-entity
- name: EntityMetadata
  property_count: 10
  slug: catalog-entity-metadata
- name: EntityRelation
  property_count: 2
  slug: catalog-entity-relation
- name: Entity
  property_count: 6
  slug: catalog-entity
- name: Location
  property_count: 3
  slug: catalog-location
- name: ConditionalRequest
  property_count: 3
  slug: permissions-conditional-request
- name: PermissionDecision
  property_count: 4
  slug: permissions-permission-decision
- name: PermissionRequest
  property_count: 2
  slug: permissions-permission-request
- name: Action
  property_count: 3
  slug: scaffolder-action
- name: Task
  property_count: 7
  slug: scaffolder-task
- name: SearchDocument
  property_count: 3
  slug: search-search-document
- name: SearchResult
  property_count: 4
  slug: search-search-result
- name: SearchResultSet
  property_count: 4
  slug: search-search-result-set
- name: TechDocsMetadata
  property_count: 5
  slug: techdocs-tech-docs-metadata
json_structures:
- name: Auth Auth Response Structure
  property_count: 3
  slug: auth-auth-response-structure
- name: Auth Jwks Response Structure
  property_count: 1
  slug: auth-jwks-response-structure
- name: Backstage Entity Structure
  property_count: 6
  slug: backstage-entity-structure
- name: Catalog Entity Metadata Structure
  property_count: 10
  slug: catalog-entity-metadata-structure
- name: Catalog Entity Relation Structure
  property_count: 2
  slug: catalog-entity-relation-structure
- name: Catalog Entity Structure
  property_count: 6
  slug: catalog-entity-structure
- name: Catalog Location Structure
  property_count: 3
  slug: catalog-location-structure
- name: Permissions Conditional Request Structure
  property_count: 3
  slug: permissions-conditional-request-structure
- name: Permissions Permission Decision Structure
  property_count: 4
  slug: permissions-permission-decision-structure
- name: Permissions Permission Request Structure
  property_count: 2
  slug: permissions-permission-request-structure
- name: Scaffolder Action Structure
  property_count: 3
  slug: scaffolder-action-structure
- name: Scaffolder Task Structure
  property_count: 7
  slug: scaffolder-task-structure
- name: Search Search Document Structure
  property_count: 3
  slug: search-search-document-structure
- name: Search Search Result Set Structure
  property_count: 4
  slug: search-search-result-set-structure
- name: Search Search Result Structure
  property_count: 4
  slug: search-search-result-structure
- name: Techdocs Tech Docs Metadata Structure
  property_count: 5
  slug: techdocs-tech-docs-metadata-structure
jsonld:
- class_count: 16
  name: Backstage Context
  property_count: 48
  slug: backstage-context
layout: provider
modified: '2026-04-21'
name: Backstage
nav: Providers
network: true
overview: 'Backstage publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Events System, Actions API, Authentication API, and 10 more. Tagged areas include Developer Portal, Internal Developer Platform, Software Catalog, and Open Source.


  The Backstage catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Backstage''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 12 more developer resources.'
plans:
- name: Backstage Plans Pricing
  plan_count: 4
  slug: backstage-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 6
  name: Backstage Rate Limits
  slug: backstage-rate-limits
rules:
- name: Backstage API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 6
  slug: backstage-asyncapi-spectral-rules
- name: Backstage API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: backstage-jsonschema-spectral-rules
- name: Backstage API Rules
  rule_count: 27
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 14
  slug: backstage-spectral-rules
score:
  band: developing
  composite: 58.4
  delta: 2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.2
    developer_ergonomics: 37.0
    discoverability: 75.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 56.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/backstage/refs/heads/main/screenshots/backstage-2026-06-20T172918.png
security:
- kind: authentication
  name: Backstage Authentication
  slug: backstage-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Backstage Domain Security
  slug: backstage-domain-security
  summary_line: TLSv1.3
slug: backstage
tags:
- Developer Portal
- Internal Developer Platform
- Software Catalog
- Open Source
use_cases:
- description: Build a unified portal for developers to discover services, read docs, and scaffold projects.
  name: Internal Developer Portal
- description: Maintain a complete, up-to-date inventory of all microservices, APIs, and infrastructure.
  name: Service Catalog
- description: Accelerate new developer onboarding with self-service project scaffolding and documentation.
  name: Developer Onboarding
- description: Track all internal and external APIs, their owners, and documentation in one place.
  name: API Governance
website: https://backstage.io/
---
