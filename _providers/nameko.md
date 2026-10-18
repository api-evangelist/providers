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
- description: Nameko is a microservices framework for Python that provides tools for building, testing, and running services. It supports RPC over AMQP, HTTP endpoints, WebSocket connections, and timer-based worker
  name: Nameko
  slug: nameko
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nameko/refs/heads/main/plans/nameko-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nameko-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nameko/refs/heads/main/rate-limits/nameko-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nameko-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/nameko/refs/heads/main/finops/nameko-finops.yml
  title: ''
  type: FinOps
  url: finops/nameko-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nameko/nameko/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/nameko/nameko/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/nameko/nameko/blob/master/docs/contributing.rst
- group: commercial
  title: ''
  type: License
  url: https://github.com/nameko/nameko/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://github.com/nameko/nameko
- group: docs
  title: ''
  type: Documentation
  url: https://nameko.readthedocs.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://nameko.readthedocs.io/en/stable/getting_started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nameko
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/nameko/nameko
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/nameko/
created: '2026-03-26'
description: Nameko is a microservices framework for Python that provides tools for building, testing, and running services. It supports RPC over AMQP, HTTP endpoints, WebSocket connections, and timer-based workers, with built-in dependency injection and a testing framework that allows services to be tested in isolation or integration.
finops:
- has_sources: false
  method: generated
  name: Nameko Finops
  primary_unit: ''
  service_category: API
  slug: nameko-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nameko.png
json_schemas:
- name: Nameko Service Configuration
  property_count: 11
  slug: nameko-configuration
layout: provider
modified: '2026-04-28'
name: Nameko
nav: Providers
network: true
overview: 'Nameko is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AMQP, Dependency Injection, Framework, Microservices, and Python.


  The Nameko catalog on APIs.io includes 1 Spectral governance ruleset.


  Nameko''s developer surface includes documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Nameko Plans Pricing
  plan_count: 3
  slug: nameko-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Nameko Rate Limits
  slug: nameko-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Nameko — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nameko-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 46.7
    catalog_earned_first_party: 0.0
    catalog_gap: 68.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 7.2
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/nameko/refs/heads/main/screenshots/nameko-2026-06-20T185938.png
slug: nameko
tags:
- AMQP
- Dependency Injection
- Framework
- Microservices
- Python
- RPC
- Testing
---
