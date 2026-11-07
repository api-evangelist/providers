---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: AI Router provides an API for intelligent LLM routing, cost management, and analytics.
  name: AI Router API
  slug: ai-router-api
- baseURL: https://api.airouter.io
  baseurl_source: declared
  description: The AI Router API API from AI Router — 1 operation(s) for ai router api.
  name: AI Router AI Router API
  slug: airouter-ai-router-api-api
- baseURL: https://api.airouter.io
  baseurl_source: declared
  description: The Chat Completions API from AI Router — 1 operation(s) for chat completions.
  name: AI Router Chat Completions API
  slug: airouter-chat-completions-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/airouter/plans/airouter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airouter-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/airouter/rules/airouter-rules.yml
  title: ''
  type: Spectral
  url: rules/airouter-rules.yml
- group: design
  href: https://artifacts.apis.io/airouter/json-ld/airouter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/airouter-context.jsonld
- group: design
  href: https://artifacts.apis.io/airouter/vocabulary/airouter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/airouter-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/airouter/data-model/airouter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airouter-data-model.yml
- group: auth
  href: https://artifacts.apis.io/airouter/authentication/airouter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airouter-authentication.yml
- group: design
  href: https://artifacts.apis.io/airouter/conformance/airouter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airouter-conformance.yml
- group: agent
  href: https://artifacts.apis.io/airouter/well-known/airouter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airouter-well-known.yml
- group: other
  href: https://artifacts.apis.io/airouter/hosts/airouter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airouter-hosts.yml
- group: other
  href: https://artifacts.apis.io/airouter/vendors/airouter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airouter-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://airouter.io/playground
- group: company
  title: ''
  type: Newsroom
  url: https://airouter.io/news
- group: auth
  href: https://artifacts.apis.io/airouter/security/airouter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airouter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airouter.io/
- group: docs
  title: ''
  type: Documentation
  url: https://airouter.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://airouter.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://airouter.io/docs/quickstart/getting-started
- group: operate
  title: ''
  type: Support
  url: https://airouter.io/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airouter
- group: commercial
  title: ''
  type: Pricing
  url: https://airouter.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://airouter.io/auth/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airouter.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airouter.io/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/airouter/workspace
created: '2026-10-15'
description: AI Router provides intelligent LLM routing to control and reduce large language model costs while preserving quality. The platform dynamically selects optimal models per request, balancing latency, cost, and performance. It offers a playground, API, and detailed analytics for enterprises to manage AI spend at scale, with features like custom optimization, model selection, and cost monitoring.
finops:
- has_sources: true
  method: derived
  name: Airouter Finops
  primary_unit: seat
  service_category: ''
  slug: airouter-finops
  template: false
image: https://airouter.io/images/hero.png
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 5
  slug: airouter-post-v1-chat-completions-request
- name: PostV1V1IdRequest
  property_count: 5
  slug: airouter-post-v1-v1-id-request
jsonld:
- class_count: 2
  name: Airouter Context
  property_count: 7
  slug: airouter-context
layout: provider
modified: '2026-10-15'
name: AI Router
nav: Providers
network: true
overview: 'AI Router is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including AI Router API, Chat Completions API, and 1 more. Tagged areas include LLM Cost Optimization, Model Routing, Enterprise AI, and Privacy.


  The AI Router catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Router''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, pricing, and 17 more developer resources.'
plans:
- name: Airouter Plans Pricing
  plan_count: 4
  slug: airouter-plans-pricing
- name: Airouter Price Estimates
  plan_count: 0
  slug: airouter-price-estimates
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AI Router API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: airouter-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.0
    catalog_earned_first_party: 12.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 61.8
    contract_governance: 19.7
    contract_quality: 21.4
    developer_ergonomics: 34.5
    discoverability: 54.5
    operational_transparency: 2.6
  previous_composite: 42.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/airouter/airouter-2026-11-03T120528.png
security:
- kind: authentication
  name: Airouter Authentication
  slug: airouter-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Airouter Domain Security
  slug: airouter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airouter
tags:
- LLM Cost Optimization
- Model Routing
- Enterprise AI
- Privacy
website: https://airouter.io/
---
