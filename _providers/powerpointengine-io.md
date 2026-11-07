---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Complete API documentation for PowerPoint Engine API: generate, edit, merge, translate and PDF-convert PowerPoint files over REST, MCP or the official SDKs.'
  name: PowerPoint Engine API
  slug: powerpoint-engine-api
- description: 'powerpointengine-io API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: powerpointengine-io API
  slug: powerpointengine-io-api
artifact_total: 15
common:
- group: commercial
  href: https://artifacts.apis.io/powerpointengine-io/plans/powerpointengine-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/powerpointengine-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/powerpointengine-io/rules/powerpointengine-io-rules.yml
  title: ''
  type: Spectral
  url: rules/powerpointengine-io-rules.yml
- group: design
  href: https://artifacts.apis.io/powerpointengine-io/json-ld/powerpointengine-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/powerpointengine-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/powerpointengine-io/vocabulary/powerpointengine-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/powerpointengine-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/powerpointengine-io/data-model/powerpointengine-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/powerpointengine-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/powerpointengine-io/authentication/powerpointengine-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/powerpointengine-io-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powerpointengine.io
- group: design
  href: https://artifacts.apis.io/powerpointengine-io/lifecycle/powerpointengine-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/powerpointengine-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/powerpointengine-io/errors/powerpointengine-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/powerpointengine-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/powerpointengine-io/conformance/powerpointengine-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/powerpointengine-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/powerpointengine-io/llms/powerpointengine-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/powerpointengine-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/powerpointengine-io/well-known/powerpointengine-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/powerpointengine-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/powerpointengine-io/hosts/powerpointengine-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/powerpointengine-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/powerpointengine-io/vendors/powerpointengine-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/powerpointengine-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/powerpointengine-io/packages/powerpointengine-io-packages.yml
  title: ''
  type: SDKs
  url: packages/powerpointengine-io-packages.yml
- group: build
  href: https://artifacts.apis.io/powerpointengine-io/packages/powerpointengine-io-packages.yml
  title: ''
  type: Packages
  url: packages/powerpointengine-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://powerpointengine.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://powerpointengine.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://powerpointengine.io/signin
- group: auth
  href: https://artifacts.apis.io/powerpointengine-io/security/powerpointengine-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powerpointengine-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://powerpointengine.io/
- group: docs
  title: ''
  type: Documentation
  url: https://powerpointengine.io/docs
- group: operate
  title: ''
  type: Support
  url: https://powerpointengine.io/support
- group: company
  title: ''
  type: Blog
  url: https://powerpointengine.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://powerpointengine.io/pricing
- group: build
  title: ''
  type: Postman
  url: https://powerpointengine.io/postman
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/powerpoint-engine-api
coverage:
  checked: '2026-10-31'
  detail: Documentation is public but no machine-readable spec (OpenAPI, AsyncAPI, GraphQL, etc.) is published.
  evidence:
  - status: 200
    url: https://powerpointengine.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: PowerPoint Engine API provides a powerful RESTful service that enables developers to generate PowerPoint (PPTX) presentations programmatically. With comprehensive documentation, SDKs for multiple languages, and flexible pricing plans, it supports automation of slide creation, template rendering, and integration into CI/CD pipelines. Backed by Cloud Peak EOOD, the service offers both free and paid tiers for developers and enterprises.
image: https://powerpointengine.io/logoAndName.png
json_schemas:
- name: PostApiPowerpointEditRequest
  property_count: 2
  slug: powerpointengine-io-post-api-powerpoint-edit-request
- name: PostApiPowerpointEditResponse
  property_count: 2
  slug: powerpointengine-io-post-api-powerpoint-edit-response
- name: PostApiPowerpointMergeRequest
  property_count: 1
  slug: powerpointengine-io-post-api-powerpoint-merge-request
- name: PostApiPowerpointReplaceRequest
  property_count: 3
  slug: powerpointengine-io-post-api-powerpoint-replace-request
- name: PostApiPowerpointTranslateRequest
  property_count: 2
  slug: powerpointengine-io-post-api-powerpoint-translate-request
- name: PostApiPowerpointTranslateResponse
  property_count: 1
  slug: powerpointengine-io-post-api-powerpoint-translate-response
jsonld:
- class_count: 12
  name: Powerpointengine Io Context
  property_count: 10
  slug: powerpointengine-io-context
layout: provider
modified: '2026-10-31'
name: powerpointengine-io
nav: Providers
network: true
overview: 'powerpointengine-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PowerPoint, Presentation, Automation, and SDK.


  The powerpointengine-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  powerpointengine-io''s developer surface includes authentication, documentation, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Powerpointengine Io Plans Pricing
  plan_count: 3
  slug: powerpointengine-io-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Powerpointengine Io Rate Limits
  slug: powerpointengine-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: powerpointengine-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: powerpointengine-io-rules
scopes:
- name: Powerpointengine Io Scopes
  scope_count: 0
  slug: powerpointengine-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 23.5
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 44.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/powerpointengine-io/powerpointengine-io-2026-11-03T141429.png
security:
- kind: authentication
  name: Powerpointengine Io Authentication
  slug: powerpointengine-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Powerpointengine Io Domain Security
  slug: powerpointengine-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: powerpointengine-io
tags:
- Company
- PowerPoint
- Presentation
- Automation
- SDK
website: https://powerpointengine.io/
---
