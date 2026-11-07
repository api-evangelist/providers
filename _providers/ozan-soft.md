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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.genderapi.io
  baseurl_source: declared
  description: The Gender inference API from Ozan Soft — 6 operation(s) for gender inference.
  name: Ozan Soft Gender inference API
  slug: ozan-soft-gender-inference-api
- baseURL: https://api.genderapi.io
  baseurl_source: declared
  description: The Phone API from Ozan Soft — 1 operation(s) for phone.
  name: Ozan Soft Phone API
  slug: ozan-soft-phone-api
- baseURL: https://api.genderapi.io
  baseurl_source: declared
  description: The Quota API from Ozan Soft — 1 operation(s) for quota.
  name: Ozan Soft Quota API
  slug: ozan-soft-quota-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/ozan-soft/security/ozan-soft-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ozan-soft-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ozan-soft/authentication/ozan-soft-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ozan-soft-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://www.genderapi.io/docs-authentication
- group: agent
  href: https://artifacts.apis.io/ozan-soft/llms/ozan-soft-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ozan-soft-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.genderapi.io/llms.txt
- group: agent
  href: https://artifacts.apis.io/ozan-soft/skills/ozan-soft-integrate-genderapi.md
  title: ''
  type: AgentSkill
  url: skills/ozan-soft-integrate-genderapi.md
- group: agent
  title: ''
  type: AgentSkill
  url: https://www.genderapi.io/skill.md
- group: other
  title: ''
  type: APIsJson
  url: https://www.genderapi.io/apis.json
- group: other
  href: https://artifacts.apis.io/ozan-soft/well-known/ozan-soft-apis-json.json
  title: ''
  type: APIsJson
  url: well-known/ozan-soft-apis-json.json
- group: build
  href: https://artifacts.apis.io/ozan-soft/packages/ozan-soft-packages.yml
  title: ''
  type: Packages
  url: packages/ozan-soft-packages.yml
- group: build
  href: https://artifacts.apis.io/ozan-soft/packages/ozan-soft-packages.yml
  title: ''
  type: SDKs
  url: packages/ozan-soft-packages.yml
- group: build
  title: ''
  type: JavaScript SDK
  url: https://github.com/GenderAPI/genderapi-js
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/GenderAPI/genderapi-python
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/GenderAPI/genderapi-php
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/GenderAPI/genderapi-ruby
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/GenderAPI/genderapi-java
- group: docs
  href: https://artifacts.apis.io/ozan-soft/overlays/ozan-soft-openapi-overlay.yaml
  title: ''
  type: OpenAPIOverlay
  url: overlays/ozan-soft-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/ozan-soft/conformance/ozan-soft-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ozan-soft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.genderapi.io/gdpr-compliance
- group: design
  href: https://artifacts.apis.io/ozan-soft/errors/ozan-soft-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ozan-soft-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ozan-soft/lifecycle/ozan-soft-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ozan-soft-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ozan-soft/lifecycle/ozan-soft-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ozan-soft-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ozan-soft/conventions/ozan-soft-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ozan-soft-conventions.yml
- group: design
  href: https://artifacts.apis.io/ozan-soft/data-model/ozan-soft-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ozan-soft-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/ozan-soft/plans/ozan-soft-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ozan-soft-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ozan-soft/rate-limits/ozan-soft-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ozan-soft-rate-limits.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.genderapi.io/gdpr-compliance
- group: other
  title: ''
  type: Subprocessors
  url: https://www.genderapi.io/subprocessors
- group: company
  title: ''
  type: Website
  url: https://www.genderapi.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.genderapi.io/api-documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.genderapi.io/price
- group: start
  title: ''
  type: SignUp
  url: https://app.genderapi.io/user/register
- group: start
  title: ''
  type: Login
  url: https://app.genderapi.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.genderapi.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genderapi.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.genderapi.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.genderapi.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GenderAPI
created: '2026-09-19'
description: Independent software company based in Ankara, Türkiye, whose flagship developer product is GenderAPI.io — a REST API for gender detection and name/email/username analysis, phone validation, and demographic data enrichment.
finops:
- has_sources: true
  method: derived
  name: Ozan Soft Finops
  primary_unit: credits
  service_category: ''
  slug: ozan-soft-finops
  template: false
layout: provider
modified: '2026-09-20'
name: Ozan Soft
nav: Providers
network: true
overview: 'Ozan Soft publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Gender inference API, Phone API, and Quota API. Tagged areas include Data Enrichment, Gender Detection, Name Analysis, Demographics, and Identity.


  The Ozan Soft catalog on APIs.io includes 1 Spectral governance ruleset.


  Ozan Soft''s developer surface includes authentication, pricing, signup flow, support, engineering blog, and 33 more developer resources.'
plans:
- name: Ozan Soft Plans Pricing
  plan_count: 13
  slug: ozan-soft-plans-pricing
- name: Ozan Soft Price Estimates
  plan_count: 0
  slug: ozan-soft-price-estimates
random_paper: 17
rate_limits:
- limit_count: 4
  name: Ozan Soft Rate Limits
  slug: ozan-soft-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Ozan Soft API Rules
  rule_count: 61
  severity_counts:
    error: 55
    hint: 0
    info: 4
    warn: 2
  slug: ozan-soft-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 63.5
    catalog_earned_first_party: 24.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 38.6
    developer_ergonomics: 57.1
    discoverability: 64.3
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - turkey
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
    - middle-east
  previous_composite: 58.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 3
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ozan-soft/ozan-soft-2026-10-11T112238.png
security:
- kind: authentication
  name: Ozan Soft Authentication
  slug: ozan-soft-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ozan Soft Domain Security
  slug: ozan-soft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: integrate-genderapi
  slug: ozan-soft-integrate-genderapi
slug: ozan-soft
tags:
- Data Enrichment
- Gender Detection
- Name Analysis
- Demographics
- Identity
- Marketing Data
- Developer API
- Phone Validation
website: https://www.genderapi.io/
---
