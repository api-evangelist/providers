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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: DKAN open-data API for Medicaid Open Data, covering a catalog of 255 datasets. Provides the DKAN search API (/api/1/search), the metastore (/api/1/metastore/schemas/dataset/items), and a CKAN-compatib
  name: Medicaid Open Data DKAN API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-medicaid-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.medicaid.gov
- group: docs
  title: ''
  type: Documentation
  url: https://dkan.readthedocs.io/en/latest/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-medicaid-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-medicaid-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-medicaid-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Medicaid Open Data is a federal government open-data portal for United States running DKAN. It exposes the DKAN catalog API, a standardized machine-readable interface over approximately 255 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs DKAN, it shares a consistent API surface with every other DKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Medicaid Gov Finops
  service_category: Open Data
  slug: data-medicaid-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-medicaid-gov.png
layout: provider
modified: '2026-06-04'
name: Medicaid Open Data
nav: Providers
network: true
overview: 'Medicaid Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, DKAN, Data Catalog, DCAT, and Government Data.


  Medicaid Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Medicaid Gov Plans Pricing
  plan_count: 1
  slug: data-medicaid-gov-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Data Medicaid Gov Rate Limits
  slug: data-medicaid-gov-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-medicaid-gov/refs/heads/main/screenshots/data-medicaid-gov-2026-06-20T175546.png
security:
- kind: domain-security
  name: Data Medicaid Gov Domain Security
  slug: data-medicaid-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: data-medicaid-gov
tags:
- Open Data
- DKAN
- Data Catalog
- DCAT
- Government Data
- Federal-Government
- United States
website: https://data.medicaid.gov
---
