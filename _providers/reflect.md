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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Reflect Agentic Access
  operation_count: 3
  slug: reflect-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.reflect.run/v1
  baseurl_source: declared
  description: The Execution API from Reflect — 1 operation(s) for execution.
  name: Reflect Execution API
  slug: reflect-execution-api
- baseURL: https://api.reflect.run/v1
  baseurl_source: declared
  description: The Executions API from Reflect — 2 operation(s) for executions.
  name: Reflect Executions API
  slug: reflect-executions-api
- baseURL: https://api.reflect.run/v1
  baseurl_source: declared
  description: The Tests API from Reflect — 2 operation(s) for tests.
  name: Reflect Tests API
  slug: reflect-tests-api
artifact_total: 21
collections:
- collection_type: open
  name: Reflect Execution API
  slug: open-reflect-execution-api
- collection_type: open
  name: Reflect Execution Executions API
  slug: open-reflect-executions-api
- collection_type: open
  name: Reflect Execution Tests API
  slug: open-reflect-tests-api
- collection_type: open
  name: Reflect
  slug: open-reflect
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/reflect/overview
- group: operate
  href: https://artifacts.apis.io/reflect/rate-limits/reflect-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reflect-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/reflect/finops/reflect-finops.yml
  title: ''
  type: FinOps
  url: finops/reflect-finops.yml
- group: commercial
  href: https://artifacts.apis.io/reflect/plans/reflect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reflect-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/reflect/capabilities/reflect-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/reflect-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://reflect.run
- group: agent
  href: https://artifacts.apis.io/reflect/agentic-access/reflect-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reflect-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/reflect/security/reflect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reflect-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/reflect/authentication/reflect-authentication.yml
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
  href: https://artifacts.apis.io/reflect/openapi/_original/reflect-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/reflect-openapi.yml
- group: docs
  href: https://artifacts.apis.io/reflect/json-schema/reflect-test-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/reflect-test-schema.json
- group: docs
  href: https://artifacts.apis.io/reflect/json-schema/reflect-execution-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/reflect-execution-schema.json
- group: design
  href: https://artifacts.apis.io/reflect/json-structure/reflect-api-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/reflect-api-structure.json
- group: design
  href: https://artifacts.apis.io/reflect/json-ld/reflect-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/reflect-context.jsonld
- group: design
  href: https://artifacts.apis.io/reflect/rules/reflect-rules.yml
  title: ''
  type: SpectralRules
  url: rules/reflect-rules.yml
- group: design
  href: https://artifacts.apis.io/reflect/vocabulary/reflect-vocabulary.yml
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
- has_sources: true
  method: derived
  name: Reflect Finops
  primary_unit: ''
  service_category: ''
  slug: reflect-finops
  template: true
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
modified: '2026-09-16'
name: Reflect
nav: Providers
network: true
overview: 'Reflect publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Execution API, Executions API, and Tests API. Tagged areas include AI Testing, Artificial Intelligence, Automated Testing, CI/CD, and Developer Tools.


  The Reflect catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Reflect''s developer surface includes authentication, engineering blog, pricing, signup flow, getting-started guide, and 24 more developer resources.'
plans:
- name: Reflect Plans Pricing
  plan_count: 3
  slug: reflect-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Reflect Rate Limits
  slug: reflect-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Reflect — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: reflect-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Reflect API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: reflect-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 76.3
    contract_governance: 27.3
    contract_quality: 48.3
    developer_ergonomics: 36.9
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reflect/reflect-2026-06-20T192747.png
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
- Developer Tools
- End-to-End Testing
- QA
- Testing
website: https://reflect.run
---
