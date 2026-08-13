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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: REST API and tooling for Cucumber BDD framework supporting test-first development with Gherkin feature files, scenario definitions, and step implementations.
  name: Cucumber API
  slug: cucumber-api
- description: REST API for Pact Broker contract testing service, enabling consumer-driven contract testing where consumer tests define the API contract before providers implement it.
  name: Pact Broker API
  slug: pact-broker-api
- description: API design-first platform enabling teams to write API specifications before implementation, supporting test-first development with mock servers, contract testing, and API style guides.
  name: Stoplight API
  slug: stoplight-api
- description: Open-source cloud-native tool for API mocking and contract testing, supporting test-first development by generating mocks from OpenAPI, Postman, and gRPC specifications.
  name: Microcks API
  slug: microcks-api
- description: Command-line HTTP API testing framework that validates API implementations against API Blueprint or OpenAPI descriptions, enabling test-first API development.
  name: Dredd API
  slug: dredd-api
artifact_total: 35
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/cucumber/cucumber-js/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/test-first-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://en.wikipedia.org/wiki/Test-driven_development
- group: docs
  title: ''
  type: Documentation
  url: https://www.agilealliance.org/glossary/tdd/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/test-first-specification-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/test-first-contract-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/test-first-mock-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/test-first-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/test-first-vocabulary.yml
created: '2025'
description: A software development approach where tests are written before the implementation code, ensuring code quality and driving design decisions through test requirements. Test-first development is the foundational principle behind test-driven development (TDD) and behavior-driven development (BDD), where the specification of expected behavior is captured in executable tests before any production code is written.
examples:
- key_count: 6
  name: Test First Contract Example
  slug: test-first-contract-example
- key_count: 9
  name: Test First Mock Example
  slug: test-first-mock-example
- key_count: 11
  name: Test First Specification Example
  slug: test-first-specification-example
features:
- description: Write executable test specifications that define expected behavior before writing any production code.
  name: Specification Before Implementation
- description: Define the API contract through tests before the implementation exists, ensuring design clarity.
  name: API Contract Definition
- description: Use mock servers generated from specifications to enable parallel frontend and backend development.
  name: Mock-First Development
- description: Tests serve as up-to-date documentation of how the system is expected to behave.
  name: Living Documentation
- description: Discover design issues early by specifying tests before implementation reveals constraints.
  name: Fail Fast Feedback
- description: Let API consumers define their expectations as tests that the API provider must satisfy.
  name: Consumer-Driven Contracts
finops:
- name: Test First Finops
  service_category: API
  slug: test-first-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/test-first.png
integrations:
- description: Generate test-first stubs and mocks directly from OpenAPI specifications.
  name: OpenAPI
- description: Use Gherkin scenarios as the test-first specification for behavior-driven development.
  name: Cucumber
- description: Apply consumer-driven contract testing where consumer tests define provider expectations.
  name: Pact
- description: Use Stoplight Prism to mock APIs from OpenAPI specs enabling test-first development.
  name: Prism
json_schemas:
- name: TestFirstContract
  property_count: 6
  slug: test-first-contract
- name: MockServer
  property_count: 9
  slug: test-first-mock
- name: TestFirstSpecification
  property_count: 11
  slug: test-first-specification
json_structures:
- name: Test First Contract Structure
  property_count: 6
  slug: test-first-contract-structure
- name: Test First Mock Structure
  property_count: 9
  slug: test-first-mock-structure
- name: Test First Specification Structure
  property_count: 11
  slug: test-first-specification-structure
jsonld:
- class_count: 3
  name: Test First Context
  property_count: 37
  slug: test-first-context
layout: provider
modified: '2026-05-03'
name: Test First
nav: Providers
network: true
overview: 'Test First publishes 1 API on the [APIs.io](https://apis.io/) network: Pact Broker API. Tagged areas include Behavior-Driven Development, Best Practices, Methodology, Software Design, and Software Development.


  The Test First catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Test First''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Test First Plans Pricing
  plan_count: 3
  slug: test-first-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Test First Rate Limits
  slug: test-first-rate-limits
rules:
- name: Test First API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: test-first-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 45.2
    developer_ergonomics: 8.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 7.9
  previous_composite: 33.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/test-first/refs/heads/main/screenshots/test-first-2026-06-20T195144.png
security:
- kind: domain-security
  name: Test First Domain Security
  slug: test-first-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: test-first
tags:
- Behavior-Driven Development
- Best Practices
- Methodology
- Software Design
- Software Development
- Testing
use_cases:
- description: Write OpenAPI specifications and generate tests from them before building the implementation.
  name: API-First Design
- description: API consumers publish test expectations that API providers must verify in their CI pipelines.
  name: Consumer-Driven Contract Testing
- description: Use Gherkin feature files to define expected system behavior before writing implementation.
  name: Behavior-Driven Development
- description: Enable frontend and backend teams to develop in parallel using mock servers from specifications.
  name: Parallel Development
- description: Validate that API implementations comply with their published specifications using test-first assertions.
  name: Specification Compliance
website: https://en.wikipedia.org/wiki/Test-driven_development
---
