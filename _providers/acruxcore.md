---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: The AcruxCore REST API provides endpoints for authentication, prompts, versions, gateway, tracing, tools, and evaluation.
  name: Acrux Core API
  slug: acrux-core-api
- baseURL: https://api.acruxcore.com
  baseurl_source: declared
  description: The Account API from Acrux Core — 1 operation(s) for account.
  name: Acrux Core Account API
  slug: acruxcore-account-api
- baseURL: https://api.acruxcore.com
  baseurl_source: declared
  description: The Acrux Core API API from Acrux Core — 2 operation(s) for acrux core api.
  name: Acrux Core Acrux Core API
  slug: acruxcore-acrux-core-api-api
- baseURL: https://api.acruxcore.com
  baseurl_source: declared
  description: The Prompts API from Acrux Core — 6 operation(s) for prompts.
  name: Acrux Core Prompts API
  slug: acruxcore-prompts-api
- baseURL: https://api.acruxcore.com
  baseurl_source: declared
  description: The Tools API from Acrux Core — 5 operation(s) for tools.
  name: Acrux Core Tools API
  slug: acruxcore-tools-api
- baseURL: https://api.acruxcore.com
  baseurl_source: declared
  description: The Traces API from Acrux Core — 4 operation(s) for traces.
  name: Acrux Core Traces API
  slug: acruxcore-traces-api
artifact_total: 20
common:
- group: operate
  href: https://artifacts.apis.io/acruxcore/rate-limits/acruxcore-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/acruxcore-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/acruxcore/plans/acruxcore-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acruxcore-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/acruxcore/rules/acruxcore-rules.yml
  title: ''
  type: Spectral
  url: rules/acruxcore-rules.yml
- group: design
  href: https://artifacts.apis.io/acruxcore/json-ld/acruxcore-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/acruxcore-context.jsonld
- group: design
  href: https://artifacts.apis.io/acruxcore/vocabulary/acruxcore-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/acruxcore-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/acruxcore/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/acruxcore/data-model/acruxcore-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acruxcore-data-model.yml
- group: auth
  href: https://artifacts.apis.io/acruxcore/authentication/acruxcore-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acruxcore-authentication.yml
- group: design
  href: https://artifacts.apis.io/acruxcore/conformance/acruxcore-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acruxcore-conformance.yml
- group: agent
  href: https://artifacts.apis.io/acruxcore/llms/acruxcore-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acruxcore-llms.txt
- group: agent
  href: https://artifacts.apis.io/acruxcore/well-known/acruxcore-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/acruxcore-well-known.yml
- group: other
  href: https://artifacts.apis.io/acruxcore/hosts/acruxcore-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acruxcore-hosts.yml
- group: other
  href: https://artifacts.apis.io/acruxcore/vendors/acruxcore-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acruxcore-vendors.yml
- group: build
  href: https://artifacts.apis.io/acruxcore/packages/acruxcore-packages.yml
  title: ''
  type: Packages
  url: packages/acruxcore-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://acruxcore.com/security
- group: build
  title: ''
  type: SDKs
  url: https://acruxcore.com/sdk
- group: company
  title: ''
  type: Newsroom
  url: https://acruxcore.com/press
- group: auth
  href: https://artifacts.apis.io/acruxcore/security/acruxcore-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/acruxcore-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/acruxcore/security/acruxcore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acruxcore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acruxcore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.acruxcore.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://acruxcore.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.acruxcore.com/docs/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.acruxcore.com/api-reference
- group: company
  title: ''
  type: Blog
  url: https://docs.acruxcore.com/blog
- group: operate
  title: ''
  type: Support
  url: https://acruxcore.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acruxcore.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acruxcore.com/terms
created: '2026-10-15'
description: Acrux Core is an open-source LLMOps platform designed for engineering teams to manage, version, and evaluate prompts, gateways, and tools across multiple LLM providers. It offers self-hostable deployment via Docker, a hosted beta, and SDKs for TypeScript and Python. Features include prompt versioning, tool integration, tracing, audit trails, and cost monitoring, all under an Apache-2.0 license.
finops:
- has_sources: true
  method: derived
  name: Acruxcore Finops
  primary_unit: ''
  service_category: ''
  slug: acruxcore-finops
  template: true
image: https://acruxcore.com/og-image.png
json_schemas:
- name: GetAccountApiKeysResponse
  property_count: 4
  slug: acruxcore-get-account-api-keys-response
- name: PatchToolsIdResponse
  property_count: 11
  slug: acruxcore-patch-tools-id-response
- name: PostApiV1PromptsImportRequest
  property_count: 12
  slug: acruxcore-post-api-v1-prompts-import-request
- name: PostApiV1PromptsImportResponse
  property_count: 6
  slug: acruxcore-post-api-v1-prompts-import-response
- name: PostApiV1V1IdResponse
  property_count: 11
  slug: acruxcore-post-api-v1-v1-id-response
- name: PostToolsSyncRequest
  property_count: 4
  slug: acruxcore-post-tools-sync-request
jsonld:
- class_count: 29
  name: Acruxcore Context
  property_count: 49
  slug: acruxcore-context
layout: provider
modified: '2026-10-15'
name: Acrux Core
nav: Providers
network: true
overview: 'Acrux Core is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Acrux Core API, Prompts API, and 3 more. Tagged areas include LLMOps, Open Source, Platform, Engineering, and Artificial Intelligence.


  The Acrux Core catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Acrux Core''s developer surface includes authentication, documentation, pricing, getting-started guide, API reference, engineering blog, support, and 21 more developer resources.'
plans:
- name: Acruxcore Plans Pricing
  plan_count: 3
  slug: acruxcore-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Acruxcore Rate Limits
  slug: acruxcore-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Acrux Core API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: acruxcore-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 80.8
    catalog_earned_first_party: 20.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 43.3
    discoverability: 70.5
    operational_transparency: 26.3
  previous_composite: 46.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/acruxcore/acruxcore-2026-11-03T120208.png
security:
- kind: authentication
  name: Acruxcore Authentication
  slug: acruxcore-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Acruxcore Domain Security
  slug: acruxcore-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Acruxcore Vulnerability Disclosure
  slug: acruxcore-vulnerability-disclosure
  summary_line: no policy recorded
slug: acruxcore
tags:
- LLMOps
- Open Source
- Platform
- Engineering
- Artificial Intelligence
website: https://acruxcore.com/
---
