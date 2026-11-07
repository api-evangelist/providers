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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gender Api Agentic Access
  operation_count: 3
  slug: gender-api-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://gender-api.com/v2
  baseurl_source: spec
  description: The Country Of Origin API from Gender API — 1 operation(s) for country of origin.
  name: Gender API Country Of Origin API
  slug: gender-api-country-of-origin-api
- baseURL: https://gender-api.com/v2
  baseurl_source: spec
  description: The Gender API from Gender API — 6 operation(s) for gender.
  name: Gender API Gender API
  slug: gender-api-gender-api
- baseURL: https://gender-api.com/v2
  baseurl_source: spec
  description: The Statistic API from Gender API — 1 operation(s) for statistic.
  name: Gender API Statistic API
  slug: gender-api-statistic-api
- baseURL: https://gender-api.com/v2
  baseurl_source: spec
  description: The Signup API from Gender API — 1 operation(s) for signup.
  name: Gender API Signup API
  slug: gender-api-signup-api
artifact_total: 15
collections:
- collection_type: open
  name: Gender Get API
  slug: open-gender-api-get-api
- collection_type: open
  name: Gender Get Get Country Of Origin API
  slug: open-gender-api-get-country-of-origin-api
- collection_type: open
  name: Gender Get Get Stats API
  slug: open-gender-api-get-stats-api
- collection_type: open
  name: Gender API
  slug: open-gender-api
common:
- group: commercial
  href: https://artifacts.apis.io/gender-api/plans/gender-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gender-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gender-api/rate-limits/gender-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gender-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gender-api/finops/gender-api-finops.yml
  title: ''
  type: FinOps
  url: finops/gender-api-finops.yml
- group: agent
  href: https://artifacts.apis.io/gender-api/agentic-access/gender-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gender-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gender-api/security/gender-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gender-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gender-api/authentication/gender-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gender-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GenderAPI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genderapi
- group: company
  title: ''
  type: Website
  url: https://gender-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gender-api.com/en/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://gender-api.com/en/pricing
- group: start
  title: ''
  type: Signup
  url: https://gender-api.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://gender-api.com/en/login
- group: operate
  title: ''
  type: Contact
  url: https://gender-api.com/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gender-api.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gender-api.com/en/privacy
- group: company
  title: ''
  type: Blog
  url: https://gender-api.com/en/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://gender-api.com/llms.txt
created: '2025-01-07'
description: Gender-API is an AI-powered service that determines whether a first name is more likely to be used by males or females, with optional localization by country, IP address, or browser locale. The API returns a gender prediction with an accuracy score and supports multi-name lookups, email parsing, full-name splitting, and country-of-origin queries. Gender-API is delivered as a metered REST API with credit-based subscription plans and integrates with Zapier, Postman, Google Sheets, and HubSpot.
finops:
- has_sources: false
  method: generated
  name: Gender Api Finops
  primary_unit: request
  service_category: API
  slug: gender-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gender-api.png
layout: provider
modified: '2026-05-19'
name: Gender API
nav: Providers
network: true
overview: 'Gender API publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Country Of Origin API, Gender API, Statistic API, and 1 more. Tagged areas include Artificial Intelligence, Demographics, Gender, Identity, and Name.


  The Gender API catalog on APIs.io includes 1 Spectral governance ruleset.


  Gender API''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Gender Api Plans Pricing
  plan_count: 3
  slug: gender-api-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Gender Api Rate Limits
  slug: gender-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Gender API API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: gender-api-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 25.0
    contract_governance: 13.6
    contract_quality: 48.6
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 26.3
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gender-api/gender-api-2026-06-20T181719.png
security:
- kind: authentication
  name: Gender Api Authentication
  slug: gender-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gender Api Domain Security
  slug: gender-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gender-api
tags:
- Artificial Intelligence
- Demographics
- Gender
- Identity
- Name
- Personal Data
website: https://gender-api.com/
---
