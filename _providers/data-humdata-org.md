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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: CKAN Action API for Humanitarian Data Exchange, a consistent JSON-over-HTTP interface over a catalog of 27,880 datasets. Standard actions include package_search, package_show, package_list, organizati
  name: Humanitarian Data Exchange CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-humdata-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.humdata.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-humdata-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-humdata-org-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-humdata-org-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Humanitarian Data Exchange is a organization open-data portal running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 27,880 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Humdata Org Finops
  service_category: Open Data
  slug: data-humdata-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-humdata-org.png
layout: provider
modified: '2026-06-04'
name: Humanitarian Data Exchange
nav: Providers
network: true
overview: 'Humanitarian Data Exchange publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  Humanitarian Data Exchange''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Humdata Org Plans Pricing
  plan_count: 1
  slug: data-humdata-org-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Data Humdata Org Rate Limits
  slug: data-humdata-org-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
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
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-humdata-org/refs/heads/main/screenshots/data-humdata-org-2026-06-20T175541.png
security:
- kind: domain-security
  name: Data Humdata Org Domain Security
  slug: data-humdata-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: data-humdata-org
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- Global
website: https://data.humdata.org
---
