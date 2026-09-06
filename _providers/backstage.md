---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Backstage Agentic Access
  operation_count: 38
  slug: backstage-agentic-access
  summary_line: 38 operations · 14 acting
api_count: 6
apis:
- baseURL: https://{backstageHost}/api/events
  baseurl_source: declared
  description: The Backstage Events system provides a publish-subscribe mechanism for broadcasting and consuming events within a Backstage instance. It enables plugins to emit events when significant actions occur (
  name: Backstage Events System
  slug: events-system
- baseURL: https://{backstageHost}/api/scaffolder
  baseurl_source: declared
  description: Endpoints for listing available scaffolder actions.
  name: Backstage Actions API
  slug: backstage-actions-api
- baseURL: https://{backstageHost}/api/auth
  baseurl_source: declared
  description: The Authentication API from Backstage — 4 operation(s) for authentication.
  name: Backstage Authentication API
  slug: backstage-authentication-api
- baseURL: https://{backstageHost}/api/permission
  baseurl_source: declared
  description: The Authorization API from Backstage — 2 operation(s) for authorization.
  name: Backstage Authorization API
  slug: backstage-authorization-api
- baseURL: https://{backstageHost}/api/techdocs
  baseurl_source: declared
  description: The Documentation API from Backstage — 2 operation(s) for documentation.
  name: Backstage Documentation API
  slug: backstage-documentation-api
- baseURL: https://{backstageHost}/api/catalog
  baseurl_source: declared
  description: Endpoints for managing and querying catalog entities.
  name: Backstage Entities API
  slug: backstage-entities-api
- baseURL: https://{backstageHost}/api/catalog
  baseurl_source: declared
  description: Endpoints for managing catalog locations (entity sources).
  name: Backstage Locations API
  slug: backstage-locations-api
- baseURL: https://{backstageHost}/api/techdocs
  baseurl_source: declared
  description: The Metadata API from Backstage — 2 operation(s) for metadata.
  name: Backstage Metadata API
  slug: backstage-metadata-api
- baseURL: https://{backstageHost}/api/search
  baseurl_source: declared
  description: The Search API from Backstage — 1 operation(s) for search.
  name: Backstage Search API
  slug: backstage-search-api
- baseURL: https://{backstageHost}/api/techdocs
  baseurl_source: declared
  description: The Sync API from Backstage — 1 operation(s) for sync.
  name: Backstage Sync API
  slug: backstage-sync-api
- baseURL: https://{backstageHost}/api/scaffolder
  baseurl_source: declared
  description: Endpoints for creating and managing scaffolder tasks.
  name: Backstage Tasks API
  slug: backstage-tasks-api
- baseURL: https://{backstageHost}/api/scaffolder
  baseurl_source: declared
  description: Endpoints for template metadata and parameter schemas.
  name: Backstage Templates API
  slug: backstage-templates-api
- baseURL: https://{backstageHost}/api/auth
  baseurl_source: declared
  description: The Token Verification API from Backstage — 1 operation(s) for token verification.
  name: Backstage Token Verification API
  slug: backstage-token-verification-api
- baseURL: https://{backstageHost}/api/notifications
  baseurl_source: declared
  description: The Backstage Notifications API delivers user- and group-addressed notifications inside a Backstage portal. Plugins create notifications with a topic, severity and link; users list, read, mark and sav
  name: Backstage Notifications API
  slug: backstage-notifications-api
- baseURL: https://{backstageHost}/api/.backstage/dynamic-features
  baseurl_source: declared
  description: The Backstage dynamic feature service reports the dynamically loaded frontend and backend remotes present in a running Backstage instance. It is the introspection surface behind dynamic plugin loading
  name: Backstage Dynamic Feature Service API
  slug: backstage-dynamic-features-api
artifact_total: 114
asyncapis:
- description: The Backstage Events system provides a publish-subscribe mechanism for broadcasting and consuming events within a Backstage instance. It enables plugins to emit events when significant actions occur (
  name: Backstage Events System
  slug: backstage-events-asyncapi
- description: ''
  name: Backstage Webhooks
  slug: backstage-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Backstage Auth Actions API
  slug: open-backstage-actions-api
- collection_type: open
  name: Backstage Auth API
  slug: open-backstage-auth
- collection_type: open
  name: Backstage Auth Actions Authentication API
  slug: open-backstage-authentication-api
- collection_type: open
  name: Backstage Auth Actions Authorization API
  slug: open-backstage-authorization-api
- collection_type: open
  name: Backstage Catalog API
  slug: open-backstage-catalog
- collection_type: open
  name: Backstage Auth Actions Documentation API
  slug: open-backstage-documentation-api
- collection_type: open
  name: Backstage Auth Actions Entities API
  slug: open-backstage-entities-api
- collection_type: open
  name: Backstage Auth Actions Locations API
  slug: open-backstage-locations-api
- collection_type: open
  name: Backstage Auth Actions Metadata API
  slug: open-backstage-metadata-api
- collection_type: open
  name: Backstage Permissions API
  slug: open-backstage-permissions
- collection_type: open
  name: Backstage Scaffolder API
  slug: open-backstage-scaffolder
- collection_type: open
  name: Backstage Auth Actions Search API
  slug: open-backstage-search-api
- collection_type: open
  name: Backstage Search API
  slug: open-backstage-search
- collection_type: open
  name: Backstage Auth Actions Sync API
  slug: open-backstage-sync-api
- collection_type: open
  name: Backstage Auth Actions Tasks API
  slug: open-backstage-tasks-api
- collection_type: open
  name: Backstage TechDocs API
  slug: open-backstage-techdocs
- collection_type: open
  name: Backstage Auth Actions Templates API
  slug: open-backstage-templates-api
- collection_type: open
  name: Backstage Auth Actions Token Verification API
  slug: open-backstage-token-verification-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/backstage-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/backstage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/backstage-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/backstage-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/backstage-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/backstage-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/backstage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/backstage-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/backstage-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/backstage-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/backstage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/backstage-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/backstage-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/backstage-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/backstage-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/backstage-cli.yml
- group: design
  title: ''
  type: Components
  url: components/backstage-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/backstage-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/backstage-webhooks.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://backstage.io/docs/overview/roadmap/
- group: docs
  title: ''
  type: APIReference
  url: https://backstage.io/docs/features/software-catalog/software-catalog-api/
- group: operate
  title: ''
  type: Support
  url: https://backstage.io/docs/overview/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://backstage.io/docs/
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
mcp_servers:
- description: 'Backstage ships a first-party MCP server as the @backstage/plugin-mcp-actions-backend plugin. It exposes every action registered with the Backstage Actions Registry as an MCP tool over the Streamable '
  name: Backstage MCP Actions Backend
  slug: backstage-mcp-actions-backend
modified: '2026-09-04'
name: Backstage
nav: Providers
network: true
overview: 'Backstage publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Events System, Actions API, Authentication API, and 12 more. Tagged areas include Developer Portal, Internal Developer Platform, Software Catalog, Open-Source, and Platform Engineering.


  The Backstage catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Backstage''s developer surface includes sandbox, changelog, CLI, API reference, support, authentication, documentation, and 33 more developer resources.'
plans:
- name: Backstage Plans Pricing
  plan_count: 4
  slug: backstage-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Backstage Rate Limits
  slug: backstage-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Backstage API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 6
  slug: backstage-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Backstage API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: backstage-jsonschema-spectral-rules
- effective_rule_count: 68
  extends:
  - spectral:oas
  name: Backstage API Rules
  rule_count: 27
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 14
  slug: backstage-spectral-rules
scopes:
- name: Backstage Scopes
  scope_count: 0
  slug: backstage-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 47.0
    contract_quality: 63.3
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 47.0
    operational_transparency: 60.5
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- kind: vulnerability-disclosure
  name: Backstage Vulnerability Disclosure
  slug: backstage-vulnerability-disclosure
  summary_line: Hackerone
slug: backstage
tags:
- Developer Portal
- Internal Developer Platform
- Software Catalog
- Open-Source
- Platform Engineering
- Software Templates
- CNCF
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
