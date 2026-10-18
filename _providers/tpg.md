---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
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
- description: The TPG Inc API provides access to platform services and data for enterprise integration and automation.
  name: TPG Inc API
  slug: tpg-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tpg/refs/heads/main/plans/tpg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tpg-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tpg/refs/heads/main/rate-limits/tpg-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tpg-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tpg/refs/heads/main/finops/tpg-finops.yml
  title: ''
  type: FinOps
  url: finops/tpg-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tpg/refs/heads/main/security/tpg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tpg-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tpginc
- group: company
  title: ''
  type: Website
  url: https://www.tpg.com
- group: company
  title: ''
  type: Blog
  url: https://www.tpg.com/news-and-insights
created: '2026-04-19'
description: TPG Inc is a major US corporation and Fortune 1000 company. The TPG Inc API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Tpg Finops
  primary_unit: ''
  service_category: Alternative Asset Management
  slug: tpg-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tpg.png
layout: provider
modified: '2026-04-19'
name: TPG
nav: Providers
network: true
overview: 'TPG is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Private Equity, Alternative Assets, and Investment.


  TPG''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Tpg Plans Pricing
  plan_count: 1
  slug: tpg-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Tpg Rate Limits
  slug: tpg-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/tpg/refs/heads/main/screenshots/tpg-2026-06-20T195511.png
security:
- kind: domain-security
  name: Tpg Domain Security
  slug: tpg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tpg
tags:
- Private Equity
- Alternative Assets
- Investment
website: https://www.tpg.com
---
