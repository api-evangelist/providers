---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.fabric.so
  baseurl_source: declared
  description: 'Fabric API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: Fabric API
  slug: fabric-so-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/fabric-so/rate-limits/fabric-so-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fabric-so-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fabric-so/plans/fabric-so-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fabric-so-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fabric-so/rules/fabric-so-rules.yml
  title: ''
  type: Spectral
  url: rules/fabric-so-rules.yml
- group: design
  href: https://artifacts.apis.io/fabric-so/json-ld/fabric-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fabric-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/fabric-so/vocabulary/fabric-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fabric-so-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fabric-so/data-model/fabric-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fabric-so-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fabric-so/authentication/fabric-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fabric-so-authentication.yml
- group: design
  href: https://artifacts.apis.io/fabric-so/conformance/fabric-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fabric-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fabric-so/llms/fabric-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fabric-so-llms.txt
- group: other
  href: https://artifacts.apis.io/fabric-so/hosts/fabric-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fabric-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/fabric-so/vendors/fabric-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fabric-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fabric.so/info/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fabric.so/info/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://fabric.so/pricing-and-plans-for-individuals
- group: company
  title: ''
  type: Newsroom
  url: https://fabric.so/info/press
- group: start
  title: ''
  type: Login
  url: https://fabric.so/signin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fabric.so/for/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://fabric.so/info/changelog
- group: company
  title: ''
  type: Blog
  url: https://fabric.so/blog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.fabric.so/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.fabric.so/developer-guide/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fabric.so/
- group: auth
  href: https://artifacts.apis.io/fabric-so/security/fabric-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fabric-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://fabric.so
created: '2026-10-23'
description: 'Fabric is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by seedcamp) and added to the network as a stub for full-pipeline profiling.'
image: https://framerusercontent.com/images/rbQSgh9vydaUzSZx1UhveZJ2Ho.png
json_schemas:
- name: GetV2MemoriesMemoryidResponse
  property_count: 5
  slug: fabric-so-get-v2-memories-memoryid-response
- name: GetV2ResourcesC99C57C334F54FdeA678F9815Cd99Db5Response
  property_count: 3
  slug: fabric-so-get-v2-resources-c99-c57-c334-f54-fde-a678-f9815-cd99-db5-response
- name: PostV2MemoriesAskRequest
  property_count: 1
  slug: fabric-so-post-v2-memories-ask-request
- name: PostV2MemoriesAskResponse
  property_count: 1
  slug: fabric-so-post-v2-memories-ask-response
- name: PostV2MemoriesSearchResponse
  property_count: 3
  slug: fabric-so-post-v2-memories-search-response
- name: PostV2ResourcesFilterRequest
  property_count: 3
  slug: fabric-so-post-v2-resources-filter-request
jsonld:
- class_count: 8
  name: Fabric So Context
  property_count: 13
  slug: fabric-so-context
layout: provider
modified: '2026-10-23'
name: Fabric
nav: Providers
network: true
overview: 'Fabric is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Workspace, File Storage, and Integration.


  The Fabric catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fabric''s developer surface includes authentication, pricing, changelog, engineering blog, API reference, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Fabric So Plans Pricing
  plan_count: 3
  slug: fabric-so-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Fabric So Rate Limits
  slug: fabric-so-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Fabric API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: fabric-so-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 72.0
    catalog_earned_first_party: 20.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 19.7
    contract_quality: 26.2
    developer_ergonomics: 32.1
    discoverability: 56.3
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
screenshot: https://apis.io/screenshots/fabric-so/fabric-so-2026-11-03T131752.png
security:
- kind: authentication
  name: Fabric So Authentication
  slug: fabric-so-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fabric So Domain Security
  slug: fabric-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fabric-so
tags:
- AI Workspace
- File Storage
- Integration
website: http://fabric.so
---
