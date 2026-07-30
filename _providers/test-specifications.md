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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: The OpenAPI Specification (OAS) is the de-facto standard for describing RESTful APIs. OpenAPI documents serve as machine-readable test specifications that tools such as Dredd, Schemathesis, and Postma
  name: OpenAPI Initiative
  slug: openapi-initiative
- description: AsyncAPI is an open specification standard for event-driven and message-based APIs. AsyncAPI documents define the channels, messages, and schemas of asynchronous interfaces, providing a test specifica
  name: AsyncAPI Initiative
  slug: asyncapi-initiative
- description: JSON Schema provides a vocabulary for annotating and validating JSON documents. Used extensively as the payload specification layer in test specifications, JSON Schema enables both human-readable docu
  name: JSON Schema
  slug: json-schema
- description: Gherkin is a plain-text language used to write behavior-driven test specifications in Given-When-Then format. Cucumber and Karate consume Gherkin feature files as executable test specifications that b
  name: Gherkin / Cucumber BDD
  slug: gherkin-cucumber-bdd
- description: 'Pact is a consumer-driven contract testing tool where consumers write test specifications (pacts) that define what responses they expect from provider APIs. Providers then verify their implementation '
  name: Pact Contract Testing
  slug: pact-contract-testing
- description: Swagger Editor is an open-source web-based editor for designing OpenAPI specifications that double as test specifications. It provides real-time validation, mock server generation, and exportable spec
  name: Swagger Editor
  slug: swagger-editor
- description: 'Optic is a developer tool that uses API specifications as the source of truth for testing. It tracks specification changes, generates changelog diffs, and validates live traffic against OpenAPI specs '
  name: Optic API
  slug: optic-api
- description: Spectral is an open-source JSON/YAML linter and specification validator. It evaluates OpenAPI, AsyncAPI, and custom specification documents against rulesets, serving as a static test specification com
  name: Spectral
  slug: spectral
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/test-specifications-domain-security.yml
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/api-evangelist/test-specifications
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/json-schema/test-specifications-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/json-structure/test-specifications-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/json-ld/test-specifications-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/test-specifications/main/vocabulary/test-specifications-vocabulary.yml
created: '2025'
description: Documentation that defines the requirements, procedures, and expected outcomes for testing software systems and APIs. Test specifications establish the criteria that implementations must satisfy, bridging the gap between product requirements and executable test cases. They include test plans, test case definitions, acceptance criteria, and conformance requirements. Effective use of this practice reduces bugs in production, supports contract testing, and enables a culture of quality-driven development aligned with OpenAPI, AsyncAPI, and JSON Schema standards.
examples:
- key_count: 11
  name: Test Specification Openapi Example
  slug: test-specification-openapi-example
finops:
- name: Test Specifications Finops
  service_category: API
  slug: test-specifications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/test-specifications.png
json_schemas:
- name: Test Specification
  property_count: 11
  slug: test-specifications
json_structures:
- name: Test Specifications Structure
  property_count: 0
  slug: test-specifications-structure
jsonld:
- class_count: 13
  name: Test Specifications Context
  property_count: 8
  slug: test-specifications-context
layout: provider
modified: '2026-05-03'
name: Test Specifications
nav: Providers
network: true
overview: 'Test Specifications publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Acceptance Testing, Contract Testing, Documentation, OpenAPI, and Quality Assurance.


  The Test Specifications catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Test Specifications Plans Pricing
  plan_count: 3
  slug: test-specifications-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Test Specifications Rate Limits
  slug: test-specifications-rate-limits
rules:
- name: Test Specifications API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: test-specifications-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.8
  delta: -4.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 36.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/test-specifications/refs/heads/main/screenshots/test-specifications-2026-06-20T195154.png
security:
- kind: domain-security
  name: Test Specifications Domain Security
  slug: test-specifications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: test-specifications
tags:
- Acceptance Testing
- Contract Testing
- Documentation
- OpenAPI
- Quality Assurance
- Testing
website: https://en.wikipedia.org/wiki/Test_specification
---
