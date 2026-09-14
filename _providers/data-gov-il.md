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
- description: 'CKAN Action API for gov.il, a consistent JSON-over-HTTP interface over a catalog of 1,194 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_list, '
  name: gov.il CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-il-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.il
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-gov-il-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-gov-il-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-gov-il-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: gov.il is a open data portal open-data portal for isr running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,194 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Gov Il Finops
  service_category: Open Data
  slug: data-gov-il-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-il.png
layout: provider
modified: '2026-06-04'
name: gov.il
nav: Providers
network: true
overview: 'gov.il publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  gov.il''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Gov Il Plans Pricing
  plan_count: 1
  slug: data-gov-il-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Data Gov Il Rate Limits
  slug: data-gov-il-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-il/refs/heads/main/screenshots/data-gov-il-2026-06-20T175537.png
security:
- kind: domain-security
  name: Data Gov Il Domain Security
  slug: data-gov-il-domain-security
  summary_line: TLSv1.3 · HSTS
slug: data-gov-il
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- ISR
website: https://data.gov.il
---
