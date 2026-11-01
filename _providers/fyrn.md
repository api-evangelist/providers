---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API for Fyrn integration platform
  name: Fyrn REST API
  slug: fyrn-rest-api
- baseURL: https://api.fyrn.dev/api/v1
  baseurl_source: declared
  description: 'Fyrn API as documented publicly: 94 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Fyrn API
  slug: fyrn-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/fyrn/plans/fyrn-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fyrn-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fyrn/rules/fyrn-rules.yml
  title: ''
  type: Spectral
  url: rules/fyrn-rules.yml
- group: design
  href: https://artifacts.apis.io/fyrn/json-ld/fyrn-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fyrn-context.jsonld
- group: design
  href: https://artifacts.apis.io/fyrn/vocabulary/fyrn-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fyrn-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fyrn/data-model/fyrn-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fyrn-data-model.yml
- group: build
  href: https://artifacts.apis.io/fyrn/cli/fyrn-cli.yml
  title: ''
  type: CLI
  url: cli/fyrn-cli.yml
- group: auth
  href: https://artifacts.apis.io/fyrn/authentication/fyrn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fyrn-authentication.yml
- group: design
  href: https://artifacts.apis.io/fyrn/conformance/fyrn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fyrn-conformance.yml
- group: other
  href: https://artifacts.apis.io/fyrn/hosts/fyrn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fyrn-hosts.yml
- group: other
  href: https://artifacts.apis.io/fyrn/vendors/fyrn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fyrn-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fyrn/security/fyrn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fyrn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fyrn.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fyrn.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fyrn.ai/reference/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fyrn.ai/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://fyrn.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fyrn.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.fyrn.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fyrn.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fyrn.ai/privacy
coverage:
  checked: '2026-10-18'
  detail: Docs are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.fyrn.ai/reference/api-reference/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-17'
description: Fyrn is an AI‑first enterprise integration platform that enables users to describe integration workflows in natural language, automatically generating declarative YAML configurations that connect SaaS applications, databases, and services. The platform’s self‑healing runtime monitors API changes, auto‑fixes mappings, and ensures continuous operation without manual intervention. Featuring a CLI‑first developer experience, version‑controlled configurations, and robust security controls, Fyrn aims to simplify complex integrations for enterprises, reducing development time and operational overhead.
image: https://fyrn.ai/images/og-default.png
json_schemas:
- name: GetApiV1FlowsResponse
  property_count: 7
  slug: fyrn-get-api-v1-flows-response
- name: PostApiV1AiGenerateAdapterRequest
  property_count: 3
  slug: fyrn-post-api-v1-ai-generate-adapter-request
- name: PostApiV1AiGenerateFlowRequest
  property_count: 4
  slug: fyrn-post-api-v1-ai-generate-flow-request
- name: PostApiV1ConnectorsInstancesRequest
  property_count: 4
  slug: fyrn-post-api-v1-connectors-instances-request
- name: PostApiV1FlowsRequest
  property_count: 3
  slug: fyrn-post-api-v1-flows-request
- name: PutApiV1FlowsIdRequest
  property_count: 5
  slug: fyrn-put-api-v1-flows-id-request
jsonld:
- class_count: 19
  name: Fyrn Context
  property_count: 29
  slug: fyrn-context
layout: provider
modified: '2026-10-17'
name: Fyrn
nav: Providers
network: true
overview: 'Fyrn is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Artificial Intelligence, Automation, Enterprise, and Platform.


  The Fyrn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fyrn''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Fyrn Plans Pricing
  plan_count: 4
  slug: fyrn-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Fyrn API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: fyrn-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 26.3
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 41.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 23
      marker_coverage: 100.0
      total: 23
    mcp: derived
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
security:
- kind: authentication
  name: Fyrn Authentication
  slug: fyrn-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fyrn Domain Security
  slug: fyrn-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fyrn
tags:
- Integration
- Artificial Intelligence
- Automation
- Enterprise
- Platform
- Company
website: https://fyrn.ai/
---
