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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: CKAN Action API for Alberta, a consistent JSON-over-HTTP interface over a catalog of 33,436 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_list
  name: Alberta CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-alberta-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open.alberta.ca
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/open-alberta-ca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-alberta-ca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-alberta-ca-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Alberta is a open data portal open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 33,436 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Open Alberta Ca Finops
  service_category: Open Data
  slug: open-alberta-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-alberta-ca.png
layout: provider
modified: '2026-06-04'
name: Alberta
nav: Providers
network: true
overview: 'Alberta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Alberta''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Open Alberta Ca Plans Pricing
  plan_count: 1
  slug: open-alberta-ca-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Open Alberta Ca Rate Limits
  slug: open-alberta-ca-rate-limits
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
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-alberta-ca/refs/heads/main/screenshots/open-alberta-ca-2026-06-20T190727.png
security:
- kind: domain-security
  name: Open Alberta Ca Domain Security
  slug: open-alberta-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-alberta-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Canada
website: https://open.alberta.ca
---
