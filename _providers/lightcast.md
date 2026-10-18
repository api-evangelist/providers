---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Career Coach Careers API is a RESTful API service that contains economic data for all careers in the Career Coach app stored in JSON format.
  name: Lightcast Careers API
  slug: lightcast
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lightcast/refs/heads/main/plans/lightcast-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lightcast-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lightcast/refs/heads/main/rate-limits/lightcast-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lightcast-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lightcast/refs/heads/main/finops/lightcast-finops.yml
  title: ''
  type: FinOps
  url: finops/lightcast-finops.yml
- group: company
  title: ''
  type: Website
  url: https://lightcast.dev
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lightcast/refs/heads/main/security/lightcast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lightcast-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lightcast-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lightcastdata
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lightcast.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://lightcast.io/resources/blog
created: '2025-01-07'
description: Lightcast (formerly Emsi Burning Glass) provides labor market data and analytics including the Career Coach Careers API, a RESTful service that contains economic data for careers stored in JSON format.
finops:
- has_sources: false
  method: generated
  name: Lightcast Finops
  primary_unit: ''
  service_category: API
  slug: lightcast-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lightcast.png
layout: provider
modified: '2026-09-16'
name: Lightcast
nav: Providers
network: true
overview: 'Lightcast is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Careers, Economics, Labor Market, and Workforce.


  Lightcast''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Lightcast Plans Pricing
  plan_count: 3
  slug: lightcast-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Lightcast Rate Limits
  slug: lightcast-rate-limits
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 10.5
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/lightcast/refs/heads/main/screenshots/lightcast-2026-06-20T184514.png
security:
- kind: domain-security
  name: Lightcast Domain Security
  slug: lightcast-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lightcast
tags:
- Careers
- Economics
- Labor Market
- Workforce
website: https://lightcast.dev
---
