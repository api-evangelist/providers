---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: DKAN API for Opolskie Open Data.
  name: Opolskie Open Data DKAN API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maps-opolskie-pl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maps-opolskie-pl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maps.opolskie.pl
- group: docs
  title: ''
  type: Documentation
  url: https://dkan.readthedocs.io/en/latest/
- group: commercial
  title: ''
  type: Plans
  url: plans/maps-opolskie-pl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maps-opolskie-pl-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/maps-opolskie-pl-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Opolskie Open Data is a regional government open-data portal for Poland running DKAN.
finops:
- name: Maps Opolskie Pl Finops
  service_category: ''
  slug: maps-opolskie-pl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maps-opolskie-pl.png
layout: provider
modified: '2026-06-07'
name: Opolskie Open Data
nav: Providers
network: true
overview: 'Opolskie Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, DKAN, Data Catalog, DCAT, and Government Data.


  Opolskie Open Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Maps Opolskie Pl Plans Pricing
  plan_count: 0
  slug: maps-opolskie-pl-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Maps Opolskie Pl Rate Limits
  slug: maps-opolskie-pl-rate-limits
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maps-opolskie-pl/refs/heads/main/screenshots/maps-opolskie-pl-2026-06-20T184952.png
security:
- kind: domain-security
  name: Maps Opolskie Pl Domain Security
  slug: maps-opolskie-pl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Maps Opolskie Pl Vulnerability Disclosure
  slug: maps-opolskie-pl-vulnerability-disclosure
  summary_line: disclosure policy published
slug: maps-opolskie-pl
tags:
- Open Data
- DKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- Poland
website: https://maps.opolskie.pl
---
