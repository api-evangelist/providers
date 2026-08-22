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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: CKAN Action API for data.gov.uk CKAN Publishing Service, a consistent JSON-over-HTTP interface over a catalog of 57,757 datasets. Standard actions include package_search, package_show, package_list, o
  name: data.gov.uk CKAN Publishing Service CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ckan-publishing-service-gov-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ckan.publishing.service.gov.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/ckan-publishing-service-gov-uk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ckan-publishing-service-gov-uk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ckan-publishing-service-gov-uk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://dataingovernment.blog.gov.uk/feed/
created: '2026-06-04'
description: data.gov.uk CKAN Publishing Service is a national government open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 57,757 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Ckan Publishing Service Gov Uk Finops
  service_category: Open Data
  slug: ckan-publishing-service-gov-uk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ckan-publishing-service-gov-uk.png
layout: provider
modified: '2026-06-04'
name: data.gov.uk CKAN Publishing Service
nav: Providers
network: true
overview: 'data.gov.uk CKAN Publishing Service publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  data.gov.uk CKAN Publishing Service''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Ckan Publishing Service Gov Uk Plans Pricing
  plan_count: 1
  slug: ckan-publishing-service-gov-uk-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Ckan Publishing Service Gov Uk Rate Limits
  slug: ckan-publishing-service-gov-uk-rate-limits
score:
  band: emerging
  composite: 16.2
  delta: -0.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ckan-publishing-service-gov-uk/refs/heads/main/screenshots/ckan-publishing-service-gov-uk-2026-06-20T174433.png
security:
- kind: domain-security
  name: Ckan Publishing Service Gov Uk Domain Security
  slug: ckan-publishing-service-gov-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ckan-publishing-service-gov-uk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- United Kingdom
website: https://ckan.publishing.service.gov.uk
---
