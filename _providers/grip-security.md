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
- description: Grip Security is a SaaS security control plane providing identity governance, shadow SaaS discovery, and data loss prevention for cloud applications.
  name: Grip Security
  slug: grip-security
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/grip-security/refs/heads/main/plans/grip-security-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/grip-security-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/grip-security/refs/heads/main/rate-limits/grip-security-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/grip-security-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/grip-security/refs/heads/main/finops/grip-security-finops.yml
  title: ''
  type: FinOps
  url: finops/grip-security-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grip-security/refs/heads/main/security/grip-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grip-security-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grip-security
- group: company
  title: ''
  type: Website
  url: https://www.grip.security
- group: docs
  title: ''
  type: Documentation
  url: https://www.grip.security/resources
- group: company
  title: ''
  type: Blog
  url: https://www.grip.security/blog
created: '2026-03-27'
description: Grip Security is a SaaS security control plane providing identity governance, shadow SaaS discovery, and data loss prevention for cloud applications.
finops:
- has_sources: false
  method: generated
  name: Grip Security Finops
  primary_unit: ''
  service_category: API
  slug: grip-security-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grip-security.png
layout: provider
modified: '2026-04-28'
name: Grip Security
nav: Providers
network: true
overview: 'Grip Security is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity Governance and SaaS Security.


  Grip Security''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Grip Security Plans Pricing
  plan_count: 3
  slug: grip-security-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Grip Security Rate Limits
  slug: grip-security-rate-limits
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 28.0
    catalog_earned_first_party: 0.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 39.3
    operational_transparency: 7.9
  previous_composite: 9.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/grip-security/refs/heads/main/screenshots/grip-security-2026-06-20T182412.png
security:
- kind: domain-security
  name: Grip Security Domain Security
  slug: grip-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: grip-security
tags:
- Identity Governance
- SaaS Security
website: https://www.grip.security
---
