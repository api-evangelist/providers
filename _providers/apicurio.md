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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 59
  human_in_the_loop: 1
  name: Apicurio Agentic Access
  operation_count: 115
  slug: apicurio-agentic-access
  summary_line: 115 operations · 59 acting · 1 human-in-the-loop
api_count: 23
apis:
- description: 'Apicurio Registry is a high-performance, runtime registry for schemas and API designs. It stores and manages OpenAPI, AsyncAPI, Avro, JSON Schema, Protobuf, and other artifact types, providing a REST '
  name: Apicurio Registry
  slug: apicurio-registry
- description: 'Apicurio Studio is a visual, zero-code API design tool for creating and editing OpenAPI and AsyncAPI specifications. Note: Apicurio Studio is deprecated in favor of the integrated design capabilities '
  name: Apicurio Studio
  slug: apicurio-studio
- description: Apicurio Data Models is a Java and TypeScript library for parsing, validating, and manipulating OpenAPI and AsyncAPI specification documents programmatically.
  name: Apicurio Data Models
  slug: apicurio-data-models
- description: Apicurio Codegen generates Java JAX-RS server stubs and client code from OpenAPI specifications, enabling design-first API development workflows.
  name: Apicurio Codegen
  slug: apicurio-codegen
- description: The Admin API from Apicurio — 17 operation(s) for admin.
  name: Apicurio Admin API
  slug: apicurio-admin-api
- description: The AI API from Apicurio — 1 operation(s) for ai.
  name: Apicurio AI API
  slug: apicurio-ai-api
- description: The Artifact rules API from Apicurio — 2 operation(s) for artifact rules.
  name: Apicurio Artifact rules API
  slug: apicurio-artifact-rules-api
- description: The Artifact Type API from Apicurio — 1 operation(s) for artifact type.
  name: Apicurio Artifact Type API
  slug: apicurio-artifact-type-api
- description: The Artifacts API from Apicurio — 9 operation(s) for artifacts.
  name: Apicurio Artifacts API
  slug: apicurio-artifacts-api
- description: The Branches API from Apicurio — 3 operation(s) for branches.
  name: Apicurio Branches API
  slug: apicurio-branches-api
- description: The Content API from Apicurio — 1 operation(s) for content.
  name: Apicurio Content API
  slug: apicurio-content-api
- description: The Contracts API from Apicurio — 16 operation(s) for contracts.
  name: Apicurio Contracts API
  slug: apicurio-contracts-api
- description: The GitOps API from Apicurio — 2 operation(s) for gitops.
  name: Apicurio GitOps API
  slug: apicurio-gitops-api
- description: The Global rules API from Apicurio — 2 operation(s) for global rules.
  name: Apicurio Global rules API
  slug: apicurio-global-rules-api
- description: The Group rules API from Apicurio — 2 operation(s) for group rules.
  name: Apicurio Group rules API
  slug: apicurio-group-rules-api
- description: The Groups API from Apicurio — 3 operation(s) for groups.
  name: Apicurio Groups API
  slug: apicurio-groups-api
- description: The KafkaSQL API from Apicurio — 1 operation(s) for kafkasql.
  name: Apicurio KafkaSQL API
  slug: apicurio-kafkasql-api
- description: The Metadata API from Apicurio — 2 operation(s) for metadata.
  name: Apicurio Metadata API
  slug: apicurio-metadata-api
- description: The Search API from Apicurio — 5 operation(s) for search.
  name: Apicurio Search API
  slug: apicurio-search-api
- description: The Snapshot API from Apicurio — 1 operation(s) for snapshot.
  name: Apicurio Snapshot API
  slug: apicurio-snapshot-api
- description: The System API from Apicurio — 2 operation(s) for system.
  name: Apicurio System API
  slug: apicurio-system-api
- description: The Users API from Apicurio — 1 operation(s) for users.
  name: Apicurio Users API
  slug: apicurio-users-api
- description: The Versions API from Apicurio — 11 operation(s) for versions.
  name: Apicurio Versions API
  slug: apicurio-versions-api
artifact_total: 32
collections:
- collection_type: open
  name: Apicurio Registry API
  slug: open-apicurio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apicurio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apicurio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apicurio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apicurio-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.apicur.io/blog/feed.xml
created: '2026-03-25'
description: Apicurio is an open source API and schema tooling platform maintained by Red Hat under the Apache 2.0 license. It includes Apicurio Registry (a high-performance schema and API design registry), Apicurio Studio (a visual API designer for OpenAPI and AsyncAPI), Apicurio Data Models (a data modeling library), Apicurio Codegen (Java code generation from OpenAPI), and Apicurito (an embedded API editor).
finops:
- name: Apicurio Finops
  service_category: API
  slug: apicurio-finops
graphqls:
- description: ''
  name: Apicurio GraphQL API
  slug: apicurio-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apicurio.png
layout: provider
modified: '2026-05-19'
name: Apicurio
nav: Providers
network: true
overview: 'Apicurio publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Admin API, AI API, Artifact rules API, and 16 more. Tagged areas include Apache License, API Design, API Registry, Avro, and AsyncAPI.


  Apicurio''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Apicurio Plans Pricing
  plan_count: 3
  slug: apicurio-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Apicurio Rate Limits
  slug: apicurio-rate-limits
scopes:
- name: Apicurio Scopes
  scope_count: 3
  slug: apicurio-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 33.9
  delta: -3.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.1
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apicurio/refs/heads/main/screenshots/apicurio-2026-06-20T172228.png
security:
- kind: authentication
  name: Apicurio Authentication
  slug: apicurio-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Apicurio Domain Security
  slug: apicurio-domain-security
  summary_line: TLSv1.3
slug: apicurio
tags:
- Apache License
- API Design
- API Registry
- Avro
- AsyncAPI
- Java
- Open Source
- OpenAPI
- Red Hat
- Schema Registry
---
