---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Specmatic provides contract testing, intelligent service virtualization, and API mocking by transforming API specifications into executable contracts. It supports backward compatibility checking, API '
  name: Specmatic
  slug: specmatic
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/specmatic/plans/specmatic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/specmatic-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/specmatic/rate-limits/specmatic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/specmatic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/specmatic/finops/specmatic-finops.yml
  title: ''
  type: FinOps
  url: finops/specmatic-finops.yml
- group: auth
  href: https://artifacts.apis.io/specmatic/security/specmatic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/specmatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://specmatic.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.specmatic.io
- group: commercial
  title: ''
  type: Pricing
  url: https://specmatic.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://specmatic.io/specmatic-updates/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/specmatic/specmatic
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/specmatic
- group: operate
  title: ''
  type: ContactUs
  url: https://specmatic.io/contact-us/
- group: other
  title: ''
  type: CaseStudies
  url: https://specmatic.io/case-studies/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/specmatic/specmatic-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/specmatic/specmatic-python-extensions
- group: build
  title: ''
  type: Examples
  url: https://github.com/specmatic/specmatic-order-contracts
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/specmatic/specmatic-insights-build-reporter-github-action
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/specmatic/specmatic-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/specmatic/skills
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/specmatic/labs/blob/c381bc506e60db9e8c00fd593ec450381d4235e0/continuous-integration/.spectral.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/specmatic/specmatic-order-contracts/blob/2aa724db96914bf62e547fe971dda5785fba29d7/.spectral.yaml
created: '2025-01-25'
description: Specmatic is an AI-powered, no-code platform for API contract testing, service virtualization, and governance. It transforms API specifications (OpenAPI, AsyncAPI, gRPC, GraphQL, WSDL) into executable contracts for contract-driven development, enabling teams to ship APIs 10x faster with zero contract drift. Specmatic supports HTTP/REST, Kafka, JMS, SOAP, Redis, Google Pub/Sub, RabbitMQ, ActiveMQ, AWS SNS/SQS/EventBridge, IBM MQ, MQTT, WebSocket, and MCP protocols.
examples:
- key_count: 10
  name: Specmatic Contract Example
  slug: specmatic-contract-example
finops:
- has_sources: false
  method: generated
  name: Specmatic Finops
  primary_unit: request
  service_category: API
  slug: specmatic-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/specmatic.png
json_schemas:
- name: Specmatic Contract
  property_count: 10
  slug: specmatic-contract
json_structures:
- name: Specmatic Contract Structure
  property_count: 0
  slug: specmatic-contract-structure
jsonld:
- class_count: 9
  name: Specmatic Context
  property_count: 9
  slug: specmatic-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Specmatic
nav: Providers
network: true
overview: 'Specmatic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Contract Testing, API Governance, API Mocking, Backward Compatibility, and Contract-Driven Development.


  The Specmatic catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Specmatic''s developer surface includes documentation, pricing, engineering blog, GitHub presence, code examples, and 15 more developer resources.'
plans:
- name: Specmatic Plans Pricing
  plan_count: 3
  slug: specmatic-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Specmatic Rate Limits
  slug: specmatic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Specmatic — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: specmatic-jsonschema-spectral-rules
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Specmatic — labs rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: specmatic-labs-spectral-rules
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Specmatic — specmatic order contracts rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: specmatic-specmatic-order-contracts-spectral-rules
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 68.9
    catalog_earned_first_party: 8.0
    catalog_gap: 46.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 37.9
    contract_quality: 24.4
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 26.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/specmatic/specmatic-2026-06-20T194301.png
security:
- kind: domain-security
  name: Specmatic Domain Security
  slug: specmatic-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: debug-specmatic-failures
  slug: debug-specmatic-failures
- name: fix-openapi-spec
  slug: fix-openapi-spec
- name: specmatic-openapi-spec-extractor
  slug: specmatic-openapi-spec-extractor
slug: specmatic
tags:
- API Contract Testing
- API Governance
- API Mocking
- Backward Compatibility
- Contract-Driven Development
- Service Virtualization
website: https://specmatic.io
---
