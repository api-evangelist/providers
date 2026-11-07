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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Revenue and net margin API as documented
  name: DevMargin API
  slug: devmargin-api
- baseURL: https://devmargin.app
  baseurl_source: declared
  description: DevMargin pulls revenue from billing rails, subtracts each project's running
  name: DevMargin API Openapi API
  slug: devmargin-api-openapi-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/devmargin-app/rules/devmargin-app-rules.yml
  title: ''
  type: Spectral
  url: rules/devmargin-app-rules.yml
- group: design
  href: https://artifacts.apis.io/devmargin-app/json-ld/devmargin-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/devmargin-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/devmargin-app/vocabulary/devmargin-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/devmargin-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/devmargin-app/conformance/devmargin-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/devmargin-app-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/devmargin-app/plans/devmargin-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/devmargin-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/devmargin-app/data-model/devmargin-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/devmargin-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/devmargin-app/errors/devmargin-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/devmargin-app-problem-types.yml
- group: other
  href: https://artifacts.apis.io/devmargin-app/hosts/devmargin-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devmargin-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/devmargin-app/vendors/devmargin-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devmargin-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/devmargin-app/security/devmargin-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devmargin-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devmargin.app/
- group: docs
  title: ''
  type: Documentation
  url: https://devmargin.app/docs/push-api
- group: docs
  title: ''
  type: APIReference
  url: https://devmargin.app/api/openapi
- group: commercial
  title: ''
  type: Pricing
  url: https://devmargin.app/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devmargin.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devmargin.app/terms
- group: start
  title: ''
  type: SignUp
  url: https://devmargin.app/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://devmargin.app/api/mcp
  - status: 200
    url: https://devmargin.app/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: DevMargin provides a platform to calculate net margin across all billing rails for SaaS products. It integrates with Stripe, Lemon Squeezy, Paddle, Gumroad, Freemius, Shopify, Adapty, RevenueCat, App Store Connect, Google Play and custom sources, pulling revenue and costs to show true profitability per product. Users can push their own metrics via a Push API, view dashboards, and compare performance over time.
image: https://devmargin.app/opengraph-image?44732262d64f2730
json_schemas:
- name: NewCost
  property_count: 8
  slug: devmargin-app-new-cost
- name: Portfolio
  property_count: 14
  slug: devmargin-app-portfolio
- name: cost — a running bill
  property_count: 2
  slug: devmargin-app-push-cost-body
- name: earned — a month that already happened
  property_count: 2
  slug: devmargin-app-push-earned-body
- name: PushEarnedResult
  property_count: 5
  slug: devmargin-app-push-earned-result
- name: metrics — latest state
  property_count: 2
  slug: devmargin-app-push-metrics-body
jsonld:
- class_count: 11
  name: Devmargin App Context
  property_count: 43
  slug: devmargin-app-context
layout: provider
modified: '2026-11-05'
name: DevMargin
nav: Providers
network: true
overview: 'DevMargin publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Openapi API, and 1 more. Tagged areas include Company.


  The DevMargin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DevMargin''s developer surface includes documentation, API reference, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Devmargin App Plans Pricing
  plan_count: 2
  slug: devmargin-app-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: DevMargin API Rules
  rule_count: 58
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 1
  slug: devmargin-app-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 60.5
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devmargin App Domain Security
  slug: devmargin-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: devmargin-app
tags:
- Company
website: https://devmargin.app/
---
