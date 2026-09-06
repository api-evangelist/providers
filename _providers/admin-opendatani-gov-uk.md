---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
- description: CKAN Action API for OpenDataNI (Northern Ireland), a consistent JSON-over-HTTP interface over a catalog of 1,066 datasets. Standard actions include package_search, package_show, package_list, organiza
  name: OpenDataNI (Northern Ireland) CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admin-opendatani-gov-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://admin.opendatani.gov.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/admin-opendatani-gov-uk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/admin-opendatani-gov-uk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/admin-opendatani-gov-uk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: OpenDataNI (Northern Ireland) is a regional government open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,066 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Admin Opendatani Gov Uk Finops
  service_category: Open Data
  slug: admin-opendatani-gov-uk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/admin-opendatani-gov-uk.png
layout: provider
modified: '2026-06-04'
name: OpenDataNI (Northern Ireland)
nav: Providers
network: true
overview: 'OpenDataNI (Northern Ireland) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  OpenDataNI (Northern Ireland)''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Admin Opendatani Gov Uk Plans Pricing
  plan_count: 1
  slug: admin-opendatani-gov-uk-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Admin Opendatani Gov Uk Rate Limits
  slug: admin-opendatani-gov-uk-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/admin-opendatani-gov-uk/refs/heads/main/screenshots/admin-opendatani-gov-uk-2026-06-20T164709.png
security:
- kind: domain-security
  name: Admin Opendatani Gov Uk Domain Security
  slug: admin-opendatani-gov-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: admin-opendatani-gov-uk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- United Kingdom
website: https://admin.opendatani.gov.uk
---
