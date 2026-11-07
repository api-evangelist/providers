---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CKAN Action API for Data.gov Inventory, a consistent JSON-over-HTTP interface over a catalog of an open datasets. Standard actions include package_search, package_show, package_list, organization_list
  name: Data.gov Inventory CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/inventory-data-gov/security/inventory-data-gov-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inventory-data-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inventory.data.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  href: https://artifacts.apis.io/inventory-data-gov/plans/inventory-data-gov-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inventory-data-gov-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/inventory-data-gov/rate-limits/inventory-data-gov-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inventory-data-gov-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/inventory-data-gov/finops/inventory-data-gov-finops.yml
  title: ''
  type: FinOps
  url: finops/inventory-data-gov-finops.yml
- group: other
  href: https://artifacts.apis.io/inventory-data-gov/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Data.gov Inventory is a federal government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately an open datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- has_sources: true
  method: generated
  name: Inventory Data Gov Finops
  primary_unit: ''
  service_category: Open Data
  slug: inventory-data-gov-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inventory-data-gov.png
layout: provider
modified: '2026-06-04'
name: Data.gov Inventory
nav: Providers
network: true
overview: 'Data.gov Inventory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Data.gov Inventory''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Inventory Data Gov Plans Pricing
  plan_count: 1
  slug: inventory-data-gov-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Inventory Data Gov Rate Limits
  slug: inventory-data-gov-rate-limits
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/inventory-data-gov/inventory-data-gov-2026-06-20T183518.png
security:
- kind: domain-security
  name: Inventory Data Gov Domain Security
  slug: inventory-data-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: inventory-data-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Federal Government
- United States
website: https://inventory.data.gov
---
