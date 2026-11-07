---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Applyra API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Applyra API
  slug: applyra-io-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/applyra-io/rate-limits/applyra-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/applyra-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/applyra-io/plans/applyra-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/applyra-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/applyra-io/rules/applyra-io-rules.yml
  title: ''
  type: Spectral
  url: rules/applyra-io-rules.yml
- group: design
  href: https://artifacts.apis.io/applyra-io/json-ld/applyra-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/applyra-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/applyra-io/vocabulary/applyra-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/applyra-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/applyra-io/data-model/applyra-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/applyra-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/applyra-io/changelog/applyra-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/applyra-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/applyra-io/authentication/applyra-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/applyra-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/applyra-io/conformance/applyra-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/applyra-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/applyra-io/llms/applyra-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applyra-io-llms.txt
- group: other
  href: https://artifacts.apis.io/applyra-io/hosts/applyra-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applyra-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/applyra-io/vendors/applyra-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applyra-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.applyra.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.applyra.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.applyra.io/pricing
- group: start
  title: ''
  type: Login
  url: https://www.applyra.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.applyra.io/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.applyra.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.applyra.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.applyra.io/docs/getting-started/what-is-applyra
- group: auth
  href: https://artifacts.apis.io/applyra-io/security/applyra-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applyra-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.applyra.io/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are JavaScript‑rendered SPAs, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.applyra.io/docs/api/endpoints
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Applyra is an App Store Optimization (ASO) platform designed for indie developers, solo founders, and small mobile studios. It offers AI‑powered keyword tracking, competitor analysis, and metadata suggestions for both the Apple App Store and Google Play. Founded in 2025 by Aurélien Weiss, Applyra provides a free tier and affordable paid plans, serving over 7,000 apps and tracking more than 150,000 keywords. The service includes daily ranking updates, keyword discovery, and tools to monitor and improve app visibility, all through an intuitive dashboard.
image: https://www.applyra.io/applyra-logo.png
json_schemas:
- name: GetApiV1AccountUsageResponse
  property_count: 1
  slug: applyra-io-get-api-v1-account-usage-response
- name: GetApiV1AutocompleteHistoryResponse
  property_count: 1
  slug: applyra-io-get-api-v1-autocomplete-history-response
- name: GetApiV1AutocompleteResponse
  property_count: 1
  slug: applyra-io-get-api-v1-autocomplete-response
- name: PostApiV1CompetitorsRequest
  property_count: 5
  slug: applyra-io-post-api-v1-competitors-request
- name: PostApiV1MetadataCheckRequest
  property_count: 2
  slug: applyra-io-post-api-v1-metadata-check-request
- name: PostApiV1MetadataSimulateRequest
  property_count: 2
  slug: applyra-io-post-api-v1-metadata-simulate-request
jsonld:
- class_count: 16
  name: Applyra Io Context
  property_count: 7
  slug: applyra-io-context
layout: provider
modified: '2026-11-01'
name: Applyra
nav: Providers
network: true
overview: 'Applyra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include ASO, Mobile, Analytics, Artificial Intelligence, and Indie.


  The Applyra catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Applyra''s developer surface includes changelog, authentication, pricing, documentation, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Applyra Io Plans Pricing
  plan_count: 2
  slug: applyra-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Applyra Io Rate Limits
  slug: applyra-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Applyra API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: applyra-io-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 16.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 43.4
    contract_governance: 35.6
    contract_quality: 23.1
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 28.9
  previous_composite: 42.0
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
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Applyra Io Authentication
  slug: applyra-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Applyra Io Domain Security
  slug: applyra-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: applyra-io
tags:
- ASO
- Mobile
- Analytics
- Artificial Intelligence
- Indie
website: https://www.applyra.io/
---
