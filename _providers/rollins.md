---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
- description: The Rollins API provides access to platform services and data for enterprise integration and automation.
  name: Rollins API
  slug: rollins-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rollins/refs/heads/main/plans/rollins-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rollins-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rollins/refs/heads/main/rate-limits/rollins-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rollins-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rollins/refs/heads/main/finops/rollins-finops.yml
  title: ''
  type: FinOps
  url: finops/rollins-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rollins/refs/heads/main/security/rollins-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rollins-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rollins.com/investors/press-releases/rss
- group: company
  title: ''
  type: Website
  url: https://www.rollins.com
created: '2026-04-19'
description: Rollins is a major US corporation and Fortune 1000 company. The Rollins API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Rollins Finops
  primary_unit: ''
  service_category: Pest Control Services
  slug: rollins-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rollins.png
layout: provider
modified: '2026-04-19'
name: Rollins
nav: Providers
network: true
overview: 'Rollins is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pest Control and Services.


  Rollins'' developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Rollins Plans Pricing
  plan_count: 1
  slug: rollins-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Rollins Rate Limits
  slug: rollins-rate-limits
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 5.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/rollins/refs/heads/main/screenshots/rollins-2026-06-20T193207.png
security:
- kind: domain-security
  name: Rollins Domain Security
  slug: rollins-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rollins
tags:
- Pest Control
- Services
website: https://www.rollins.com
---
