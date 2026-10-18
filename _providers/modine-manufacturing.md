---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
- description: The Modine Manufacturing API provides access to platform services and data for enterprise integration and automation.
  name: Modine Manufacturing API
  slug: modine-manufacturing-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/modine-manufacturing/refs/heads/main/plans/modine-manufacturing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/modine-manufacturing-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/modine-manufacturing/refs/heads/main/rate-limits/modine-manufacturing-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/modine-manufacturing-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/modine-manufacturing/refs/heads/main/finops/modine-manufacturing-finops.yml
  title: ''
  type: FinOps
  url: finops/modine-manufacturing-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.modine.com/who-we-are/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.modine.com/feed/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/modine-manufacturing/refs/heads/main/security/modine-manufacturing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modine-manufacturing-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/modine-manufacturing-company
- group: company
  title: ''
  type: Website
  url: https://www.modine.com
created: '2026-04-19'
description: Modine Manufacturing is a major US corporation and Fortune 1000 company. The Modine Manufacturing API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Modine Manufacturing Finops
  primary_unit: ''
  service_category: Industrial / Thermal Management
  slug: modine-manufacturing-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modine-manufacturing.png
layout: provider
modified: '2026-10-06'
name: Modine Manufacturing
nav: Providers
network: true
overview: 'Modine Manufacturing is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Thermal Management, Automotive, and HVAC.


  Modine Manufacturing''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Modine Manufacturing Plans Pricing
  plan_count: 1
  slug: modine-manufacturing-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Modine Manufacturing Rate Limits
  slug: modine-manufacturing-rate-limits
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 9.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/modine-manufacturing/refs/heads/main/screenshots/modine-manufacturing-2026-06-20T185655.png
security:
- kind: domain-security
  name: Modine Manufacturing Domain Security
  slug: modine-manufacturing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modine-manufacturing
tags:
- Thermal Management
- Automotive
- HVAC
website: https://www.modine.com
---
