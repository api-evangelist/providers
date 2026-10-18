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
- description: API for accessing Peace Corps volunteer statistics, country programs, and development data.
  name: Peace Corps Data API
  slug: peace-corps-data-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/peace-corps/refs/heads/main/plans/peace-corps-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/peace-corps-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/peace-corps/refs/heads/main/rate-limits/peace-corps-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/peace-corps-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/peace-corps/refs/heads/main/finops/peace-corps-finops.yml
  title: ''
  type: FinOps
  url: finops/peace-corps-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.peacecorps.gov/connect/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/peace-corps/refs/heads/main/security/peace-corps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peace-corps-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peacecorps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peace-corps
- group: company
  title: ''
  type: Website
  url: https://www.peacecorps.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peacecorps.gov/privacy/
created: '2026-03-16'
description: The Peace Corps is a U.S. government agency that sends American volunteers abroad to work with communities on development projects. They provide data APIs for accessing Peace Corps volunteer data, country information, and project statistics.
finops:
- has_sources: false
  method: generated
  name: Peace Corps Finops
  primary_unit: ''
  service_category: API
  slug: peace-corps-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peace-corps.png
layout: provider
modified: '2026-10-06'
name: Peace Corps
nav: Providers
network: true
overview: 'Peace Corps is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government, International Development, and Volunteers.


  Peace Corps'' developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Peace Corps Plans Pricing
  plan_count: 3
  slug: peace-corps-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Peace Corps Rate Limits
  slug: peace-corps-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/peace-corps/refs/heads/main/screenshots/peace-corps-2026-06-20T191524.png
security:
- kind: domain-security
  name: Peace Corps Domain Security
  slug: peace-corps-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: peace-corps
tags:
- Government
- International Development
- Volunteers
website: https://www.peacecorps.gov/
---
