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
api_count: 1
apis:
- description: 'CKAN Action API for Official Ukrainian Government Portal, a consistent JSON-over-HTTP interface over a catalog of 38,895 datasets. Standard actions include package_search, package_show, package_list, '
  name: Official Ukrainian Government Portal CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-ua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.ua
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-gov-ua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-gov-ua-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-gov-ua-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Official Ukrainian Government Portal is a open data portal open-data portal for Ukraine running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 38,895 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Gov Ua Finops
  service_category: Open Data
  slug: data-gov-ua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-ua.png
layout: provider
modified: '2026-06-04'
name: Official Ukrainian Government Portal
nav: Providers
network: true
overview: 'Official Ukrainian Government Portal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Official Ukrainian Government Portal''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Gov Ua Plans Pricing
  plan_count: 1
  slug: data-gov-ua-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Data Gov Ua Rate Limits
  slug: data-gov-ua-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-ua/refs/heads/main/screenshots/data-gov-ua-2026-06-20T175540.png
security:
- kind: domain-security
  name: Data Gov Ua Domain Security
  slug: data-gov-ua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data-gov-ua
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Ukraine
website: https://data.gov.ua
---
