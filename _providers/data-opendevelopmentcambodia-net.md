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
- description: CKAN Action API for Open Development Cambodia, a consistent JSON-over-HTTP interface over a catalog of 13,484 datasets. Standard actions include package_search, package_show, package_list, organizatio
  name: Open Development Cambodia CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-opendevelopmentcambodia-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.opendevelopmentcambodia.net
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-opendevelopmentcambodia-net-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-opendevelopmentcambodia-net-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-opendevelopmentcambodia-net-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://opendevelopmentcambodia.net/feed/
created: '2026-06-04'
description: Open Development Cambodia is a organization open-data portal for Cambodia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 13,484 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Opendevelopmentcambodia Net Finops
  service_category: Open Data
  slug: data-opendevelopmentcambodia-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-opendevelopmentcambodia-net.png
layout: provider
modified: '2026-06-04'
name: Open Development Cambodia
nav: Providers
network: true
overview: 'Open Development Cambodia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  Open Development Cambodia''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Data Opendevelopmentcambodia Net Plans Pricing
  plan_count: 1
  slug: data-opendevelopmentcambodia-net-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Data Opendevelopmentcambodia Net Rate Limits
  slug: data-opendevelopmentcambodia-net-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-opendevelopmentcambodia-net/refs/heads/main/screenshots/data-opendevelopmentcambodia-net-2026-06-20T175603.png
security:
- kind: domain-security
  name: Data Opendevelopmentcambodia Net Domain Security
  slug: data-opendevelopmentcambodia-net-domain-security
  summary_line: TLSv1.3
slug: data-opendevelopmentcambodia-net
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- Cambodia
website: https://data.opendevelopmentcambodia.net
---
