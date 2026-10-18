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
- description: The HealthEquity API provides access to platform services and data for enterprise integration and automation.
  name: HealthEquity API
  slug: healthequity-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/healthequity/refs/heads/main/plans/healthequity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/healthequity-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/healthequity/refs/heads/main/rate-limits/healthequity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/healthequity-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/healthequity/refs/heads/main/finops/healthequity-finops.yml
  title: ''
  type: FinOps
  url: finops/healthequity-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.healthequity.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/healthequity/refs/heads/main/security/healthequity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/healthequity-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/healthequity/refs/heads/main/security/healthequity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/healthequity-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/healthequity
- group: company
  title: ''
  type: Website
  url: https://www.healthequity.com
created: '2026-04-19'
description: HealthEquity is a major US corporation and Fortune 1000 company. The HealthEquity API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Healthequity Finops
  primary_unit: ''
  service_category: Healthcare Benefits / HSA Custodian Partner API
  slug: healthequity-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/healthequity.png
layout: provider
modified: '2026-10-06'
name: HealthEquity
nav: Providers
network: true
overview: 'HealthEquity is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, HSA, Benefits, and Employee Benefits.


  HealthEquity''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Healthequity Plans Pricing
  plan_count: 1
  slug: healthequity-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Healthequity Rate Limits
  slug: healthequity-rate-limits
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 8
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
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/healthequity/refs/heads/main/screenshots/healthequity-2026-07-25T220836.png
security:
- kind: domain-security
  name: Healthequity Domain Security
  slug: healthequity-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Healthequity Vulnerability Disclosure
  slug: healthequity-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: healthequity
tags:
- Healthcare
- HSA
- Benefits
- Employee Benefits
website: https://www.healthequity.com
---
