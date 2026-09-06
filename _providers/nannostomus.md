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
- description: The Nannostomus Sex Offender API enables search of 771k+ offender records by state and name across all 50 U.S. states and 14 territories. Records are updated monthly with per-state change reporting an
  name: Nannostomus Sex Offender API
  slug: nannostomus
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nannostomus-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intsurfing
- group: company
  title: ''
  type: Website
  url: https://www.nannostomus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nannostomus.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nannostomus.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.nannostomus.com/contact/
created: '2024-11-13'
description: Nannostomus provides a sex offender search API covering 771k+ offender records across all 50 U.S. states and 14 territories. It supports search by state and name, with monthly per-state record updates, deduplication, and 99.9% uptime backed by cloud infrastructure. A free tier covers up to 100 requests per month with tiered pay-as-you-go pricing beyond that.
finops:
- name: Nannostomus Finops
  service_category: API
  slug: nannostomus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nannostomus.png
layout: provider
modified: '2026-04-28'
name: Nannostomus
nav: Providers
network: true
overview: 'Nannostomus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Public Safety, Sex Offenders, Government, Search, and Records.


  Nannostomus'' developer surface includes documentation, pricing, support, and 3 more developer resources.'
plans:
- name: Nannostomus Plans Pricing
  plan_count: 3
  slug: nannostomus-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Nannostomus Rate Limits
  slug: nannostomus-rate-limits
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nannostomus/refs/heads/main/screenshots/nannostomus-2026-06-20T185936.png
security:
- kind: domain-security
  name: Nannostomus Domain Security
  slug: nannostomus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nannostomus
tags:
- Public Safety
- Sex Offenders
- Government
- Search
- Records
website: https://www.nannostomus.com/
---
