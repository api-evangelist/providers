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
- description: 'CKAN Action API for CKAN Demo, a consistent JSON-over-HTTP interface over a catalog of 13 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_list, '
  name: CKAN Demo CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demo-ckan-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demo.ckan.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/demo-ckan-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/demo-ckan-org-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/demo-ckan-org-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: CKAN Demo is a organization open-data portal running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 13 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Demo Ckan Org Finops
  service_category: Open Data
  slug: demo-ckan-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demo-ckan-org.png
layout: provider
modified: '2026-06-04'
name: CKAN Demo
nav: Providers
network: true
overview: 'CKAN Demo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  CKAN Demo''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Demo Ckan Org Plans Pricing
  plan_count: 1
  slug: demo-ckan-org-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Demo Ckan Org Rate Limits
  slug: demo-ckan-org-rate-limits
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demo-ckan-org/refs/heads/main/screenshots/demo-ckan-org-2026-06-20T175907.png
security:
- kind: domain-security
  name: Demo Ckan Org Domain Security
  slug: demo-ckan-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: demo-ckan-org
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- Global
website: https://demo.ckan.org
---
