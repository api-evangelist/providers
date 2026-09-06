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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-bureau-of-prisons-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/officialfbop
- group: company
  title: ''
  type: Website
  url: https://www.bop.gov
- group: company
  title: ''
  type: Careers
  url: https://www.bop.gov/jobs/
created: '2024-11-30'
description: The Federal Bureau of Prisons (BOP) is responsible for the custody and care of federal inmates in the United States. The BOP operates the inmate locator and publishes facility information online but does not currently offer a public, documented developer API.
finops:
- name: Federal Bureau Of Prisons Finops
  service_category: API
  slug: federal-bureau-of-prisons-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-bureau-of-prisons.png
layout: provider
modified: '2026-07-25'
name: Federal Bureau of Prisons
nav: Providers
network: true
overview: Federal Bureau of Prisons is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Corrections, Federal-Government, and Prisons.
plans:
- name: Federal Bureau Of Prisons Plans Pricing
  plan_count: 3
  slug: federal-bureau-of-prisons-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Federal Bureau Of Prisons Rate Limits
  slug: federal-bureau-of-prisons-rate-limits
score:
  band: minimal
  composite: 6.7
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
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-bureau-of-prisons/refs/heads/main/screenshots/federal-bureau-of-prisons-2026-06-20T181111.png
security:
- kind: domain-security
  name: Federal Bureau Of Prisons Domain Security
  slug: federal-bureau-of-prisons-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: federal-bureau-of-prisons
tags:
- Corrections
- Federal-Government
- Prisons
website: https://www.bop.gov
---
