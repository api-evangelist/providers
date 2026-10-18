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
- description: The Encompass Health API provides access to platform services and data for enterprise integration and automation.
  name: Encompass Health API
  slug: encompass-health-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/encompass-health/refs/heads/main/plans/encompass-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/encompass-health-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/encompass-health/refs/heads/main/rate-limits/encompass-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/encompass-health-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/encompass-health/refs/heads/main/finops/encompass-health-finops.yml
  title: ''
  type: FinOps
  url: finops/encompass-health-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.encompasshealth.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/encompass-health/refs/heads/main/security/encompass-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/encompass-health-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encompasshealth
- group: company
  title: ''
  type: Website
  url: https://www.encompasshealth.com
created: '2026-04-19'
description: Encompass Health is a major US corporation and Fortune 1000 company. The Encompass Health API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Encompass Health Finops
  primary_unit: ''
  service_category: Healthcare Integration
  slug: encompass-health-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encompass-health.png
layout: provider
modified: '2026-10-06'
name: Encompass Health
nav: Providers
network: true
overview: 'Encompass Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare and Rehabilitation.


  Encompass Health''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Encompass Health Plans Pricing
  plan_count: 1
  slug: encompass-health-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Encompass Health Rate Limits
  slug: encompass-health-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/encompass-health/refs/heads/main/screenshots/encompass-health-2026-06-20T180647.png
security:
- kind: domain-security
  name: Encompass Health Domain Security
  slug: encompass-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: encompass-health
tags:
- Healthcare
- Rehabilitation
website: https://www.encompasshealth.com
---
