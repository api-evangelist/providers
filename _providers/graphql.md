---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphql
- group: start
  title: ''
  type: Portal
  url: https://graphql.org/
- group: docs
  title: ''
  type: Documentation
  url: https://graphql.org/learn/
- group: start
  title: ''
  type: GettingStarted
  url: https://graphql.org/learn/
- group: company
  title: ''
  type: Blog
  url: https://graphql.org/blog/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/graphql-request.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/graphql-response.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/graphql-error.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/graphql-introspection.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/graphql-context.jsonld
created: '2025-01-01'
description: GraphQL is a query language for APIs and a runtime for fulfilling those queries with existing data. Developed by Facebook in 2012 and open-sourced in 2015, GraphQL provides a complete and understandable description of the data in an API, gives clients the power to ask for exactly what they need, and enables powerful developer tools. It is maintained by the GraphQL Foundation under the Linux Foundation.
graphqls:
- description: ''
  name: GraphQL GraphQL API
  slug: graphql-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphql.png
json_schemas:
- name: GraphQL Error
  property_count: 4
  slug: graphql-error
- name: GraphQL Introspection Response
  property_count: 1
  slug: graphql-introspection
- name: GraphQL Request
  property_count: 4
  slug: graphql-request
- name: GraphQL Response
  property_count: 3
  slug: graphql-response
jsonld:
- class_count: 0
  name: Graphql Context
  property_count: 22
  slug: graphql-context
layout: provider
modified: '2026-03-16'
name: GraphQL
nav: Providers
network: true
overview: 'GraphQL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Fetching, GraphQL, Query Language, and Specification.


  The GraphQL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GraphQL''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, and 7 more developer resources.'
random_paper: 16
rules:
- effective_rule_count: 6
  extends: []
  name: GraphQL API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: graphql-jsonschema-spectral-rules
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 81.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 33.3
    discoverability: 48.1
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 15.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graphql/refs/heads/main/screenshots/graphql-2026-06-20T182329.png
security:
- kind: domain-security
  name: Graphql Domain Security
  slug: graphql-domain-security
  summary_line: TLSv1.3 · HSTS
slug: graphql
tags:
- Data Fetching
- GraphQL
- Query Language
- Specification
website: https://graphql.org/
---
