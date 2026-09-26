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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: CKAN Action API for Gouvernement ouvert Canada (FR), a consistent JSON-over-HTTP interface over a catalog of 47,344 datasets. Standard actions include package_search, package_show, package_list, organ
  name: Gouvernement ouvert Canada (FR) CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ouvert-canada-ca/refs/heads/main/security/ouvert-canada-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ouvert-canada-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ouvert.canada.ca/data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ouvert-canada-ca/refs/heads/main/plans/ouvert-canada-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ouvert-canada-ca-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ouvert-canada-ca/refs/heads/main/rate-limits/ouvert-canada-ca-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ouvert-canada-ca-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ouvert-canada-ca/refs/heads/main/finops/ouvert-canada-ca-finops.yml
  title: ''
  type: FinOps
  url: finops/ouvert-canada-ca-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ouvert-canada-ca/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Gouvernement ouvert Canada (FR) is a national government open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 47,344 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Ouvert Canada Ca Finops
  service_category: Open Data
  slug: ouvert-canada-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ouvert-canada-ca.png
layout: provider
modified: '2026-06-04'
name: Gouvernement ouvert Canada (FR)
nav: Providers
network: true
overview: 'Gouvernement ouvert Canada (FR) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Gouvernement ouvert Canada (FR)''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Ouvert Canada Ca Plans Pricing
  plan_count: 1
  slug: ouvert-canada-ca-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Ouvert Canada Ca Rate Limits
  slug: ouvert-canada-ca-rate-limits
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 54.4
    catalog_earned_first_party: 0.0
    catalog_gap: 60.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 26.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 18.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ouvert-canada-ca/refs/heads/main/screenshots/ouvert-canada-ca-2026-06-20T191244.png
security:
- kind: domain-security
  name: Ouvert Canada Ca Domain Security
  slug: ouvert-canada-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ouvert-canada-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Canada
website: https://ouvert.canada.ca/data
---
