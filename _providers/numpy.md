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
- description: Core numerical computing library for Python providing multi-dimensional arrays and mathematical functions.
  name: NumPy API
  slug: numpy-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/numpy/refs/heads/main/plans/numpy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/numpy-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/numpy/refs/heads/main/rate-limits/numpy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/numpy-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/numpy/refs/heads/main/finops/numpy-finops.yml
  title: ''
  type: FinOps
  url: finops/numpy-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/numpy/refs/heads/main/security/numpy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numpy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://numpy.org/
- group: docs
  title: ''
  type: Documentation
  url: https://numpy.org/doc/stable/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/numpy
- group: operate
  title: ''
  type: ChangeLog
  url: https://numpy.org/doc/stable/release.html
created: '2024-01-01'
description: The fundamental package for scientific computing with Python. NumPy provides multi-dimensional array objects, various derived objects, and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, FFT, and random number generation.
finops:
- has_sources: false
  method: generated
  name: Numpy Finops
  primary_unit: ''
  service_category: API
  slug: numpy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numpy.png
layout: provider
modified: '2026-04-28'
name: NumPy
nav: Providers
network: true
overview: 'NumPy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Science, Machine Learning, Numerical Analysis, Open Source, and Python Library.


  NumPy''s developer surface includes documentation, changelog, and 6 more developer resources.'
plans:
- name: Numpy Plans Pricing
  plan_count: 3
  slug: numpy-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Numpy Rate Limits
  slug: numpy-rate-limits
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 26.3
  previous_composite: 16.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/numpy/refs/heads/main/screenshots/numpy-2026-06-20T190524.png
security:
- kind: domain-security
  name: Numpy Domain Security
  slug: numpy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: numpy
tags:
- Data Science
- Machine Learning
- Numerical Analysis
- Open Source
- Python Library
- Scientific Computing
website: https://numpy.org/
---
