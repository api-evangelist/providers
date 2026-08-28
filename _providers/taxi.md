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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Taxi Agentic Access
  operation_count: 11
  slug: taxi-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 8
apis:
- description: TaxiQL is a declarative query language for federated data retrieval across multiple APIs and data sources. Queries specify the desired data structure using semantic types and Taxi automatically discov
  name: TaxiQL Query API
  slug: taxiql-query-api
- description: Orbital is the companion data platform for Taxi that hosts TaxiQL queries, provides a schema registry, and executes federated data integrations across APIs, databases, and streams using Taxi annotatio
  name: Orbital Platform
  slug: orbital-platform
- description: Interactive web-based editor for writing Taxi schemas and TaxiQL queries with live diagram generation and query execution preview.
  name: Taxi Playground
  slug: taxi-playground
- description: Convert existing specs to Taxi format
  name: Taxi - Describe How Your APIs and Data Relate Conversion API
  slug: taxi-conversion-api
- description: TaxiQL query execution
  name: Taxi - Describe How Your APIs and Data Relate Queries API
  slug: taxi-queries-api
- description: Taxi schema management and compilation
  name: Taxi - Describe How Your APIs and Data Relate Schemas API
  slug: taxi-schemas-api
- description: Service registry operations
  name: Taxi - Describe How Your APIs and Data Relate Services API
  slug: taxi-services-api
- description: Type registry and discovery
  name: Taxi - Describe How Your APIs and Data Relate Types API
  slug: taxi-types-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Taxi Language Conversion API
  slug: open-taxi-conversion-api
- collection_type: open
  name: Taxi Language API
  slug: open-taxi-language
- collection_type: open
  name: Taxi Language Conversion Queries API
  slug: open-taxi-queries-api
- collection_type: open
  name: Taxi Language Conversion Schemas API
  slug: open-taxi-schemas-api
- collection_type: open
  name: Taxi Language Conversion Services API
  slug: open-taxi-services-api
- collection_type: open
  name: Taxi Language Conversion Types API
  slug: open-taxi-types-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taxi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taxi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taxi
- group: company
  title: ''
  type: Website
  url: https://taxilang.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taxilang.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/taxilang
- group: other
  title: ''
  type: Playground
  url: https://playground.taxilang.org
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/taxi-lang/shared_invite
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/taxi-language-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/taxi-schema-definition-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/taxi-schema-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/taxi-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/taxi-vocabulary.yml
created: '2026-01-05'
description: Taxi is an open-source language (Apache 2.0) for describing APIs, data models, and how data relates across an entire ecosystem. TaxiQL is a declarative query language that lets consumers define the data they want while Taxi handles orchestration across REST APIs, databases, Kafka topics, gRPC services, and S3 buckets. Taxi eliminates manual integration code by using semantic type annotations to automatically discover data paths and adapt to evolving API schemas.
examples:
- key_count: 2
  name: Taxi Compile Schema Example
  slug: taxi-compile-schema-example
- key_count: 2
  name: Taxi Execute Query Example
  slug: taxi-execute-query-example
finops:
- name: Taxi Finops
  service_category: Data Integration
  slug: taxi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taxi.png
json_schemas:
- name: Taxi Schema Definition
  property_count: 6
  slug: taxi-schema-definition
json_structures:
- name: Taxi Schema Structure
  property_count: 0
  slug: taxi-schema-structure
jsonld:
- class_count: 24
  name: Taxi Context
  property_count: 0
  slug: taxi-context
layout: provider
modified: '2026-05-19'
name: Taxi - Describe How Your APIs and Data Relate
nav: Providers
network: true
overview: 'Taxi - Describe How Your APIs and Data Relate publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Conversion API, Queries API, Schemas API, and 2 more. Tagged areas include API Description, Data Integration, Open-Source, Query Language, and Schema.


  The Taxi - Describe How Your APIs and Data Relate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Taxi - Describe How Your APIs and Data Relate''s developer surface includes documentation and 12 more developer resources.'
plans:
- name: Taxi Plans Pricing
  plan_count: 7
  slug: taxi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Taxi Rate Limits
  slug: taxi-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Taxi - Describe How Your APIs and Data Relate API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: taxi-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Taxi - Describe How Your APIs and Data Relate API Rules
  rule_count: 16
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 13
  slug: taxi-spectral-rules
score:
  band: thin
  composite: 31.5
  delta: -0.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 55.2
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taxi/refs/heads/main/screenshots/taxi-2026-06-20T194934.png
security:
- kind: domain-security
  name: Taxi Domain Security
  slug: taxi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taxi
tags:
- API Description
- Data Integration
- Open-Source
- Query Language
- Schema
- Semantic
website: https://taxilang.org/
---
