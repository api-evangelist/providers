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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Reflect Agentic Access
  operation_count: 3
  slug: reflect-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- description: The Execution API from Reflect — 1 operation(s) for execution.
  name: Reflect Execution API
  slug: reflect-execution-api
- description: The Executions API from Reflect — 2 operation(s) for executions.
  name: Reflect Executions API
  slug: reflect-executions-api
- description: The Tests API from Reflect — 2 operation(s) for tests.
  name: Reflect Tests API
  slug: reflect-tests-api
artifact_total: 18
collections:
- collection_type: open
  name: Reflect
  slug: open-reflect
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reflect-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reflect-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reflect-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://reflect.run/articles/index.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reflect
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reflect-app
- group: commercial
  title: ''
  type: Pricing
  url: https://reflect.run/pricing/
- group: other
  title: ''
  type: Articles
  url: https://reflect.run/articles/
- group: other
  title: ''
  type: Customers
  url: https://reflect.run/customers/
- group: start
  title: ''
  type: Login
  url: https://app.reflect.run/login
- group: start
  title: ''
  type: Signup
  url: https://app.reflect.run/registration
- group: company
  title: ''
  type: About
  url: https://reflect.run/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reflect.run/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reflect.run/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://reflect.run/docs/overview/quick-start/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/reflect-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/reflect-test-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/reflect-execution-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/reflect-api-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/reflect-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/reflect-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/reflect-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://reflect.run/llms.txt
created: '2024-11-13'
description: Reflect is an AI-powered automated end-to-end testing platform that enables teams to effortlessly create, execute, and troubleshoot automated browser tests. Reflect provides a no-code test recorder for capturing user workflows and a REST API for integrating test execution into CI/CD pipelines. Tests can be run against any environment using hostname and parameter overrides.
examples:
- key_count: 2
  name: Reflect List Tests Example
  slug: reflect-list-tests-example
- key_count: 2
  name: Reflect Run Test Example
  slug: reflect-run-test-example
finops:
- name: Reflect Finops
  service_category: API
  slug: reflect-finops
image: https://reflect.run/assets/logo.png
json_schemas:
- name: Reflect Test Execution
  property_count: 2
  slug: reflect-execution
- name: Reflect Test
  property_count: 4
  slug: reflect-test
json_structures:
- name: Reflect Api Structure
  property_count: 0
  slug: reflect-api-structure
jsonld:
- class_count: 6
  name: Reflect Context
  property_count: 7
  slug: reflect-context
layout: provider
modified: '2026-05-19'
name: Reflect
nav: Providers
network: true
overview: 'Reflect publishes 3 APIs on the [APIs.io](https://apis.io/) network: Execution API, Executions API, and Tests API. Tagged areas include AI Testing, Artificial Intelligence, Automated Testing, CI/CD, and End-to-End Testing.


  The Reflect catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Reflect''s developer surface includes authentication, engineering blog, pricing, signup flow, getting-started guide, and 18 more developer resources.'
plans:
- name: Reflect Plans Pricing
  plan_count: 3
  slug: reflect-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Reflect Rate Limits
  slug: reflect-rate-limits
rules:
- name: Reflect API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: reflect-jsonschema-spectral-rules
- name: Reflect API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: reflect-rules
score:
  band: strong
  composite: 56.4
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 57.4
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reflect/refs/heads/main/screenshots/reflect-2026-06-20T192747.png
security:
- kind: authentication
  name: Reflect Authentication
  slug: reflect-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reflect Domain Security
  slug: reflect-domain-security
  summary_line: TLSv1.3 · DMARC
slug: reflect
tags:
- AI Testing
- Artificial Intelligence
- Automated Testing
- CI/CD
- End-to-End Testing
- QA
- Testing
---
