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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 10
apis:
- description: Stoplight's flexible JSON/YAML linter for creating automated style guides, with baked-in support for OpenAPI v3.1, v3.0, v2.0, Arazzo v1.0, and AsyncAPI v2.x. Spectral is the de facto reference linter
  name: Spectral
  slug: spectral
- description: A Go-based, ultra-fast OpenAPI linter inspired by Spectral and fully compatible with existing Spectral rulesets. Vacuum tears through API specs at light speed, ships interactive HTML reports and a das
  name: Vacuum
  slug: vacuum
- description: Redocly's `lint` command identifies and reports problems in OpenAPI, AsyncAPI, Arazzo, or Open-RPC descriptions, helping teams "avoid bugs and make API or Arazzo descriptions more consistent." Rules a
  name: Redocly CLI
  slug: redocly-cli
- description: Optic catches breaking changes and applies lint rules to OpenAPI specs, generating OpenAPI from real traffic and keeping it accurate with automatic schema testing and patches. The project was archived
  name: Optic
  slug: optic
- description: Red Hat's open-source API/schema registry that stores and validates OpenAPI, AsyncAPI, JSON Schema, Avro, Protobuf, and GraphQL artifacts. While not a pure linter, Apicurio Registry performs content-r
  name: Apicurio Registry
  slug: apicurio-registry
- description: Snyk's TypeScript ruleset built on Optic CI that enforces consistency standards across OpenAPI specifications. Sweater Comb codifies the Snyk API Program's design rules so a growing federation of team
  name: Sweater Comb
  slug: sweater-comb
- description: Speakeasy's OpenAPI validator with 90+ built-in rules across six categories — SDK generation, spec correctness, best practices, security, schema validation, and Speakeasy-specific checks. The `speakea
  name: Speakeasy Linter
  slug: speakeasy
- description: Postman Spec Hub's governance engine applies linting rules to OpenAPI 2.0, 3.0, and 3.1 specifications, surfacing violations directly in the Issues tab below the spec editor. Enterprise teams can cust
  name: Postman API Governance
  slug: postman-api-governance
- description: Stoplight's API design IDE embeds Spectral natively, surfacing ruleset violations as real-time editor feedback as designers author OpenAPI and JSON Schema. Studio is the canonical reference for IDE-gr
  name: Stoplight Studio
  slug: stoplight-studio
- description: APIMetrics provides live-traffic API monitoring with a rule engine that evaluates JSON Schema and response-shape compliance on every production call. Unlike static linters, APIMetrics enforces contrac
  name: APIMetrics
  slug: apimetrics
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linting-domain-security.yml
- group: other
  title: ''
  type: Repository
  url: https://github.com/api-evangelist/linting
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: other
  title: ''
  type: Network
  url: https://github.com/api-evangelist/api-evangelist-network
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/linting/refs/heads/main/json-schema/linting-rule-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/linting/refs/heads/main/json-structure/linting-rule-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/linting/refs/heads/main/json-ld/linting-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/linting/refs/heads/main/vocabulary/linting-vocabulary.yml
- group: other
  title: ''
  type: RelatedRepository
  url: https://github.com/api-evangelist/spotlight-rules
- group: other
  title: ''
  type: RelatedRepository
  url: https://github.com/api-evangelist/spectral
- group: other
  title: ''
  type: RelatedRepository
  url: https://github.com/api-evangelist/vacuum
- group: other
  title: ''
  type: RelatedRepository
  url: https://github.com/api-evangelist/redocly
- group: other
  title: ''
  type: RelatedRepository
  url: https://github.com/api-evangelist/optic
- group: other
  title: ''
  type: RelatedRepository
  url: https://github.com/api-evangelist/stoplight
created: '2026-05-22'
description: API Linting is a topic index for the tools, rulesets, vocabularies, and practices that automate API style guide enforcement across OpenAPI, AsyncAPI, JSON Schema, and adjacent contract formats. The collection catalogs the major open-source and commercial linters in use across the industry — Spectral, Vacuum, Redocly CLI, Optic, Apicurio, sweater-comb, Speakeasy, and Postman API governance — alongside shared schemas, JSON-LD context, and a working vocabulary so linting concepts can be reasoned about consistently across tools.
examples:
- key_count: 14
  name: Linting Rule Normalized Example
  slug: linting-rule-normalized-example
graphqls:
- description: ''
  name: API Linting GraphQL API
  slug: linting-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/api-evangelist-logos/api-evangelist-logo-butterfly.png
json_schemas:
- name: Linting Rule
  property_count: 14
  slug: linting-rule
json_structures:
- name: Linting Rule Structure
  property_count: 14
  slug: linting-rule-structure
jsonld:
- class_count: 10
  name: Linting Context
  property_count: 18
  slug: linting-context
layout: provider
modified: '2026-05-22'
name: API Linting
nav: Providers
network: true
overview: 'API Linting publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, API Governance, API Linting, API Style Guide, and AsyncAPI.


  The API Linting catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 9
rules:
- name: API Linting API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: linting-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 20.8
    developer_ergonomics: 0.0
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 26.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linting/refs/heads/main/screenshots/linting-2026-06-20T184556.png
security:
- kind: domain-security
  name: Linting Domain Security
  slug: linting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linting
tags:
- API Design
- API Governance
- API Linting
- API Style Guide
- AsyncAPI
- JSON Schema
- Linting
- OpenAPI
- Quality Assurance
- Topic
---
