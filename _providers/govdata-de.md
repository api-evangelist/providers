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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: CKAN Action API for GovData Deutschland, a consistent JSON-over-HTTP interface over a catalog of 151,112 datasets. Standard actions include package_search, package_show, package_list, organization_lis
  name: GovData Deutschland CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govdata-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.govdata.de/ckan
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/govdata-de-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/govdata-de-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/govdata-de-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: GovData Deutschland is a national government open-data portal for Germany running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 151,112 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Govdata De Finops
  service_category: Open Data
  slug: govdata-de-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/govdata-de.png
layout: provider
modified: '2026-06-04'
name: GovData Deutschland
nav: Providers
network: true
overview: 'GovData Deutschland publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  GovData Deutschland''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Govdata De Plans Pricing
  plan_count: 1
  slug: govdata-de-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Govdata De Rate Limits
  slug: govdata-de-rate-limits
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govdata-de/refs/heads/main/screenshots/govdata-de-2026-06-20T182305.png
security:
- kind: domain-security
  name: Govdata De Domain Security
  slug: govdata-de-domain-security
  summary_line: TLSv1.3 · HSTS
slug: govdata-de
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Germany
website: https://www.govdata.de/ckan
---
