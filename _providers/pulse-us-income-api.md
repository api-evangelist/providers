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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: It was designed to solve the problem of calculating the future income trajectory of applicants in real-time.
  name: Pulse US Income API
  slug: pulse-us-income-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pulse-us-income-api-domain-security.yml
created: '2025-02-24'
description: It was designed to solve the problem of calculating the future income trajectory of applicants in real-time.
finops:
- name: Pulse Us Income Api Finops
  service_category: API
  slug: pulse-us-income-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pulse-us-income-api.png
layout: provider
modified: '2026-04-28'
name: Pulse US Income API
nav: Providers
network: true
overview: Pulse US Income API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Income, Underwriting, Financial, and Applicants.
plans:
- name: Pulse Us Income Api Plans Pricing
  plan_count: 3
  slug: pulse-us-income-api-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Pulse Us Income Api Rate Limits
  slug: pulse-us-income-api-rate-limits
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pulse-us-income-api/refs/heads/main/screenshots/pulse-us-income-api-2026-06-20T192257.png
security:
- kind: domain-security
  name: Pulse Us Income Api Domain Security
  slug: pulse-us-income-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pulse-us-income-api
tags:
- Income
- Underwriting
- Financial
- Applicants
---
