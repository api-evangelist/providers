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
- description: ParkPow API for managing parking lots, tracking vehicles, alerts, and enforcement of parking rules.
  name: ParkPow
  slug: parkpow
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parkpow-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://parkpow.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parkpow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parkpow
- group: company
  title: ''
  type: Website
  url: https://parkpow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.parkpow.com/documentation/
created: '2025-02-08'
description: ParkPow is software to manage and enforce parking lots. It lets you track vehicles, get custom alerts, and enforce your parking rules. The ParkPow API documentation requires application access and is not publicly available.
finops:
- name: Parkpow Finops
  service_category: API
  slug: parkpow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parkpow.png
layout: provider
modified: '2026-04-28'
name: ParkPow
nav: Providers
network: true
overview: 'ParkPow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Parking, License Plate Recognition, and Enforcement.


  ParkPow''s developer surface includes engineering blog, documentation, and 4 more developer resources.'
plans:
- name: Parkpow Plans Pricing
  plan_count: 3
  slug: parkpow-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Parkpow Rate Limits
  slug: parkpow-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parkpow/refs/heads/main/screenshots/parkpow-2026-06-20T191414.png
security:
- kind: domain-security
  name: Parkpow Domain Security
  slug: parkpow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parkpow
tags:
- Parking
- License Plate Recognition
- Enforcement
website: https://parkpow.com/
---
