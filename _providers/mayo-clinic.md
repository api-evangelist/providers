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
- description: Review and try the existing APIs in the Mayo Clinic Apigee API catalog portal. Provides programmatic access to healthcare data and clinical services.
  name: Mayo Clinic API
  slug: mayo-clinic-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mayo-clinic/refs/heads/main/plans/mayo-clinic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mayo-clinic-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mayo-clinic/refs/heads/main/rate-limits/mayo-clinic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mayo-clinic-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mayo-clinic/refs/heads/main/finops/mayo-clinic-finops.yml
  title: ''
  type: FinOps
  url: finops/mayo-clinic-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mayo-clinic/refs/heads/main/security/mayo-clinic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mayo-clinic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mayo-clinic
- group: start
  title: ''
  type: Portal
  url: https://apiportal.mcc.mayo.edu/
- group: company
  title: ''
  type: Website
  url: https://www.mayoclinic.org/
created: '2025-02-12'
description: Mayo Clinic provides a developer API portal with access to clinical and healthcare APIs hosted on an Apigee API catalog. Developers can review, test, and integrate with available APIs for healthcare data and services.
finops:
- has_sources: false
  method: generated
  name: Mayo Clinic Finops
  primary_unit: ''
  service_category: API
  slug: mayo-clinic-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mayo-clinic.png
layout: provider
modified: '2026-04-28'
name: Mayo Clinic
nav: Providers
network: true
overview: 'Mayo Clinic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical Data, Healthcare, Hospitals, and Medical.


  Mayo Clinic''s developer surface includes developer portal and 6 more developer resources.'
plans:
- name: Mayo Clinic Plans Pricing
  plan_count: 3
  slug: mayo-clinic-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Mayo Clinic Rate Limits
  slug: mayo-clinic-rate-limits
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 10.7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/mayo-clinic/refs/heads/main/screenshots/mayo-clinic-2026-06-20T185105.png
security:
- kind: domain-security
  name: Mayo Clinic Domain Security
  slug: mayo-clinic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mayo-clinic
tags:
- Clinical Data
- Healthcare
- Hospitals
- Medical
website: https://www.mayoclinic.org/
---
