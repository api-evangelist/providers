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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Core numerical computing library for Python providing multi-dimensional arrays and mathematical functions.
  name: NumPy API
  slug: numpy-api
artifact_total: 5
common:
- group: auth
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
- name: Numpy Finops
  service_category: API
  slug: numpy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numpy.png
layout: provider
modified: '2026-04-28'
name: NumPy
nav: Providers
network: true
overview: 'NumPy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Science, Machine-Learning, Numerical Analysis, Open-Source, and Python Library.


  NumPy''s developer surface includes documentation, changelog, and 3 more developer resources.'
plans:
- name: Numpy Plans Pricing
  plan_count: 3
  slug: numpy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Numpy Rate Limits
  slug: numpy-rate-limits
score:
  band: emerging
  composite: 15.8
  delta: 3.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numpy/refs/heads/main/screenshots/numpy-2026-06-20T190524.png
security:
- kind: domain-security
  name: Numpy Domain Security
  slug: numpy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: numpy
tags:
- Data Science
- Machine-Learning
- Numerical Analysis
- Open-Source
- Python Library
- Scientific Computing
website: https://numpy.org/
---
