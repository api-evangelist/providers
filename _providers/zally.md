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
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zally Agentic Access
  operation_count: 4
  slug: zally-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: The Api Violations API from Zally — 2 operation(s) for api violations.
  name: Zally Api Violations API
  slug: zally-api-violations-api
- description: The Review Statistics API from Zally — 1 operation(s) for review statistics.
  name: Zally Review Statistics API
  slug: zally-review-statistics-api
- description: The Supported Rules API from Zally — 1 operation(s) for supported rules.
  name: Zally Supported Rules API
  slug: zally-supported-rules-api
artifact_total: 52
collections:
- collection_type: postman
  name: Zally - Zalando's API Linter Api Violations API
  slug: postman-zally-api-violations-api
- collection_type: postman
  name: Zally - Zalando's API Linter Api Violations Review Statistics API
  slug: postman-zally-review-statistics-api
- collection_type: postman
  name: Zally - Zalando's API Linter Api Violations Supported Rules API
  slug: postman-zally-supported-rules-api
- collection_type: open
  name: Zally - Zalando's API Linter
  slug: open-zally-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zally/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zally-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zally-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zally-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://opensource.zalando.com/zally/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/zalando/zally#readme
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zalando/zally
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zalando
- group: commercial
  title: ''
  type: License
  url: https://github.com/zalando/zally/blob/main/LICENSE
- group: operate
  title: ''
  type: Issues
  url: https://github.com/zalando/zally/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/zalando/zally/releases
- group: build
  title: ''
  type: CLI
  url: https://github.com/zalando/zally/tree/main/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/zalando/zally/tree/main/web-ui
- group: docs
  title: ''
  type: Specification
  url: https://opensource.zalando.com/restful-api-guidelines/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/rules/zally-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/vocabulary/zally-vocabulary.yml
created: '2026-03-25'
description: Zally is an open source API linter from Zalando that validates OpenAPI 2 and 3 specifications against configurable rule sets for API design consistency. It exposes a REST API, command-line interface, and web UI for checking API designs against Zalando's RESTful API Guidelines or custom rule sets.
examples:
- key_count: 4
  name: Zally Api Linting Request Example
  slug: zally-api-linting-request-example
- key_count: 4
  name: Zally Api Linting Response Example
  slug: zally-api-linting-response-example
- key_count: 8
  name: Zally Api Review Statistics Response Example
  slug: zally-api-review-statistics-response-example
- key_count: 5
  name: Zally Api Rule Example
  slug: zally-api-rule-example
- key_count: 1
  name: Zally Api Supported Rules Response Example
  slug: zally-api-supported-rules-response-example
- key_count: 8
  name: Zally Api Violation Example
  slug: zally-api-violation-example
- key_count: 5
  name: Zally Api Violations Count Example
  slug: zally-api-violations-count-example
features:
- description: Validate OpenAPI 2/3 specifications against rule sets to enforce design consistency.
  name: API Linting
- description: Customize default Zalando RESTful API Guidelines rules or define custom rule sets.
  name: Configurable Rules
- description: REST API for programmatic access, CLI for local checking, and Web UI for visual review.
  name: Multiple Interfaces
- description: Use x-zally-ignore extension in specs to selectively bypass rules.
  name: Ignore Extension
- description: Rules categorized as MUST, SHOULD, COULD, MAY, and HINT for graduated enforcement.
  name: Rule Severity Levels
- description: Track linting requests and aggregate review statistics over time.
  name: Linting Statistics
finops:
- name: Zally Finops
  service_category: API
  slug: zally-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zally.png
integrations:
- description: Run Zally linting in GitHub Actions workflows on PRs.
  name: GitHub Actions
- description: Translate Zally rule sets to Spectral rulesets for OpenAPI 3 alignment.
  name: Spectral
- description: Default rule set ships with rules from Zalando's public API guidelines.
  name: Zalando RESTful API Guidelines
json_schemas:
- name: LintingRequest
  property_count: 4
  slug: zally-api-linting-request
- name: LintingResponse
  property_count: 4
  slug: zally-api-linting-response
- name: ReviewStatisticsResponse
  property_count: 8
  slug: zally-api-review-statistics-response
- name: Rule
  property_count: 5
  slug: zally-api-rule
- name: RuleType
  property_count: 0
  slug: zally-api-rule-type
- name: SupportedRulesResponse
  property_count: 1
  slug: zally-api-supported-rules-response
- name: Violation
  property_count: 8
  slug: zally-api-violation
- name: ViolationsCount
  property_count: 5
  slug: zally-api-violations-count
json_structures:
- name: Zally Api Linting Request Structure
  property_count: 4
  slug: zally-api-linting-request-structure
- name: Zally Api Linting Response Structure
  property_count: 4
  slug: zally-api-linting-response-structure
- name: Zally Api Review Statistics Response Structure
  property_count: 8
  slug: zally-api-review-statistics-response-structure
- name: Zally Api Rule Structure
  property_count: 5
  slug: zally-api-rule-structure
- name: Zally Api Rule Type Structure
  property_count: 0
  slug: zally-api-rule-type-structure
- name: Zally Api Supported Rules Response Structure
  property_count: 1
  slug: zally-api-supported-rules-response-structure
- name: Zally Api Violation Structure
  property_count: 8
  slug: zally-api-violation-structure
- name: Zally Api Violations Count Structure
  property_count: 5
  slug: zally-api-violations-count-structure
jsonld:
- class_count: 10
  name: Zally Context
  property_count: 29
  slug: zally-context
layout: provider
modified: '2026-05-19'
name: Zally
nav: Providers
network: true
overview: 'Zally publishes 3 APIs on the [APIs.io](https://apis.io/) network: Api Violations API, Review Statistics API, and Supported Rules API. Tagged areas include API Design, API Linting, API Quality, Open Source, and OpenAPI.


  The Zally catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Zally''s developer surface includes authentication, documentation, changelog, CLI, and 12 more developer resources.'
plans:
- name: Zally Plans Pricing
  plan_count: 3
  slug: zally-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Zally Rate Limits
  slug: zally-rate-limits
rules:
- name: Zally API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zally-jsonschema-spectral-rules
- name: Zally API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 13
  slug: zally-rules
score:
  band: strong
  composite: 56.5
  delta: -3.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 74.6
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 60.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zally/refs/heads/main/screenshots/zally-2026-06-20T201756.png
security:
- kind: authentication
  name: Zally Authentication
  slug: zally-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zally Domain Security
  slug: zally-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zally
tags:
- API Design
- API Linting
- API Quality
- Open Source
- OpenAPI
- Zalando
use_cases:
- description: Review OpenAPI specs in pull requests to enforce design standards before merge.
  name: API Design Review
- description: Enforce organizational API guidelines across teams via shared rule sets.
  name: API Governance
- description: Block API releases that violate critical MUST rules in CI/CD pipelines.
  name: API Quality Gate
- description: Encode an API style guide as executable rules and apply consistently.
  name: Style Guide Enforcement
website: https://opensource.zalando.com/zally/
---
