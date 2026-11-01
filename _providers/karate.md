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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Karate is an open source API test automation framework combining API testing, mocks, and performance testing in a single tool using BDD syntax.
  name: Karate
  slug: karate
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/karate/plans/karate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/karate-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/karate/rate-limits/karate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/karate-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/karate/finops/karate-finops.yml
  title: ''
  type: FinOps
  url: finops/karate-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/karatelabs/karate/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/karatelabs/karate/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/karatelabs/karate/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/karatelabs/karate/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/karatelabs/karate/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/karatelabs/karate/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://karatelabs.github.io/karate/
- group: docs
  title: ''
  type: Documentation
  url: https://karatelabs.github.io/karate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/karatelabs/karate
created: '2026-03-25'
description: Karate is an open source API test automation framework combining API testing, mocks, and performance testing in a single tool using BDD syntax.
finops:
- has_sources: false
  method: generated
  name: Karate Finops
  primary_unit: request
  service_category: API
  slug: karate-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karate.png
layout: provider
modified: '2026-03-25'
name: Karate
nav: Providers
network: true
overview: 'Karate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Functional Testing and Testing.


  Karate''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Karate Plans Pricing
  plan_count: 3
  slug: karate-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Karate Rate Limits
  slug: karate-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 28.0
    catalog_earned_first_party: 0.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 39.3
    operational_transparency: 39.5
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/karate/karate-2026-06-20T183919.png
slug: karate
tags:
- Functional Testing
- Testing
website: https://karatelabs.github.io/karate/
---
