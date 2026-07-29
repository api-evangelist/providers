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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Swagger Codegen Agentic Access
  operation_count: 7
  slug: swagger-codegen-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 5
apis:
- description: The Swagger Codegen command-line interface for generating code artifacts locally. Available as a JAR file and Docker image. Supports the same generators as the online API with additional template cust
  name: Swagger Codegen CLI
  slug: swagger-codegen-cli
- description: Code generation endpoints for clients, servers, and documentation
  name: Swagger Codegen Generation API
  slug: swagger-codegen-generation-api
- description: Discover available generator languages and types
  name: Swagger Codegen Languages API
  slug: swagger-codegen-languages-api
- description: Retrieve per-language configuration options
  name: Swagger Codegen Options API
  slug: swagger-codegen-options-api
- description: Template rendering and intermediate model generation
  name: Swagger Codegen Utilities API
  slug: swagger-codegen-utilities-api
artifact_total: 18
collections:
- collection_type: open
  name: Swagger Generator API
  slug: open-swagger-generator
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swagger-codegen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swagger-codegen-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://swagger.io/tools/swagger-codegen/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/swagger-api/swagger-codegen/wiki
- group: company
  title: ''
  type: Website
  url: https://swagger.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swagger-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/swagger-api/swagger-codegen
- group: operate
  title: ''
  type: Issues
  url: https://github.com/swagger-api/swagger-codegen/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/swagger-api/swagger-codegen/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/swagger-api/swagger-codegen/blob/master/LICENSE
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/swaggerapi/swagger-codegen-cli-v3
- group: build
  title: ''
  type: Maven Plugin
  url: https://mvnrepository.com/artifact/io.swagger.codegen.v3/swagger-codegen-maven-plugin
- group: build
  title: ''
  type: Gradle Plugin
  url: https://plugins.gradle.org/plugin/org.hidetake.swagger.generator
created: '2026-03-16'
description: Swagger Codegen is an open-source template-driven code generation tool that automatically generates client libraries, server stubs, and API documentation from OpenAPI Specification definitions. It supports 40+ client languages and 20+ server frameworks. Available as a CLI, Docker image, Maven/Gradle plugin, and online REST API at generator3.swagger.io.
examples:
- key_count: 3
  name: Swagger Codegen Generate Python Client Example
  slug: swagger-codegen-generate-python-client-example
- key_count: 3
  name: Swagger Codegen List Languages Example
  slug: swagger-codegen-list-languages-example
finops:
- name: Swagger Codegen Finops
  service_category: API
  slug: swagger-codegen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swagger-codegen.png
json_schemas:
- name: Swagger Codegen Generation Request
  property_count: 6
  slug: swagger-codegen-generation-request
json_structures:
- name: Swagger Codegen Structure
  property_count: 0
  slug: swagger-codegen-structure
jsonld:
- class_count: 0
  name: Swagger Codegen Context
  property_count: 27
  slug: swagger-codegen-context
layout: provider
modified: '2026-05-19'
name: Swagger Codegen
nav: Providers
network: true
overview: 'Swagger Codegen publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Generation API, Languages API, Options API, and 1 more. Tagged areas include Client Libraries, Code Generation, Open Source, OpenAPI, and SDK.


  The Swagger Codegen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Swagger Codegen''s developer surface includes developer portal, documentation, release notes, and 10 more developer resources.'
plans:
- name: Swagger Codegen Plans Pricing
  plan_count: 3
  slug: swagger-codegen-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Swagger Codegen Rate Limits
  slug: swagger-codegen-rate-limits
rules:
- name: Swagger Codegen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swagger-codegen-jsonschema-spectral-rules
- name: Swagger Codegen API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: swagger-codegen-rules
score:
  band: developing
  composite: 46.9
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.0
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swagger-codegen/refs/heads/main/screenshots/swagger-codegen-2026-06-20T194753.png
security:
- kind: domain-security
  name: Swagger Codegen Domain Security
  slug: swagger-codegen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: swagger-codegen
tags:
- Client Libraries
- Code Generation
- Open Source
- OpenAPI
- SDK
website: https://swagger.io/
---
