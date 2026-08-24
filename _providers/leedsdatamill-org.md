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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: CKAN Action API for Leeds Data Mill, a consistent JSON-over-HTTP interface over a catalog of an open datasets. Standard actions include package_search, package_show, package_list, organization_list, g
  name: Leeds Data Mill CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leedsdatamill-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leedsdatamill.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/leedsdatamill-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leedsdatamill-org-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leedsdatamill-org-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Leeds Data Mill is a open data portal open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately an open datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Leedsdatamill Org Finops
  service_category: Open Data
  slug: leedsdatamill-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leedsdatamill-org.png
layout: provider
modified: '2026-06-04'
name: Leeds Data Mill
nav: Providers
network: true
overview: 'Leeds Data Mill publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Leeds Data Mill''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Leedsdatamill Org Plans Pricing
  plan_count: 1
  slug: leedsdatamill-org-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Leedsdatamill Org Rate Limits
  slug: leedsdatamill-org-rate-limits
score:
  band: emerging
  composite: 15.7
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leedsdatamill-org/refs/heads/main/screenshots/leedsdatamill-org-2026-06-20T184406.png
security:
- kind: domain-security
  name: Leedsdatamill Org Domain Security
  slug: leedsdatamill-org-domain-security
  summary_line: TLSv1.3
slug: leedsdatamill-org
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- United Kingdom
website: https://leedsdatamill.org
---
