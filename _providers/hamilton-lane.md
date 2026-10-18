---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
- description: The Hamilton Lane API provides access to platform services and data for enterprise integration and automation.
  name: Hamilton Lane API
  slug: hamilton-lane-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hamilton-lane/refs/heads/main/plans/hamilton-lane-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hamilton-lane-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hamilton-lane/refs/heads/main/rate-limits/hamilton-lane-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hamilton-lane-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hamilton-lane/refs/heads/main/finops/hamilton-lane-finops.yml
  title: ''
  type: FinOps
  url: finops/hamilton-lane-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hamilton-lane/refs/heads/main/security/hamilton-lane-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hamilton-lane-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hamiltonlane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hamilton-lane
- group: company
  title: ''
  type: Website
  url: https://www.hamiltonlane.com
created: '2026-04-19'
description: Hamilton Lane is a major US corporation and Fortune 1000 company. The Hamilton Lane API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Hamilton Lane Finops
  primary_unit: ''
  service_category: Private Markets Data / Analytics Subscription
  slug: hamilton-lane-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hamilton-lane.png
layout: provider
modified: '2026-04-19'
name: Hamilton Lane
nav: Providers
network: true
overview: Hamilton Lane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Private Markets, Asset Management, and Investment.
plans:
- name: Hamilton Lane Plans Pricing
  plan_count: 1
  slug: hamilton-lane-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Hamilton Lane Rate Limits
  slug: hamilton-lane-rate-limits
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 9.8
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
screenshot: https://raw.githubusercontent.com/api-evangelist/hamilton-lane/refs/heads/main/screenshots/hamilton-lane-2026-06-20T182459.png
security:
- kind: domain-security
  name: Hamilton Lane Domain Security
  slug: hamilton-lane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hamilton-lane
tags:
- Private Markets
- Asset Management
- Investment
website: https://www.hamiltonlane.com
---
