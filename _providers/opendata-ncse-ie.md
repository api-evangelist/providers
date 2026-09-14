---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: CKAN Action API for NCSE Open Data, ~70 datasets. Base URL https://opendata.ncse.ie/api/3/action/.
  name: NCSE Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-ncse-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.ncse.ie
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-ncse-ie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-ncse-ie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-ncse-ie-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: NCSE Open Data is a government agency open-data portal for Ireland running CKAN. It exposes the CKAN catalog API over approximately 70 datasets.
finops:
- name: Opendata Ncse Ie Finops
  service_category: ''
  slug: opendata-ncse-ie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-ncse-ie.png
layout: provider
modified: '2026-06-07'
name: NCSE Open Data
nav: Providers
network: true
overview: 'NCSE Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  NCSE Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Ncse Ie Plans Pricing
  plan_count: 0
  slug: opendata-ncse-ie-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Opendata Ncse Ie Rate Limits
  slug: opendata-ncse-ie-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-ncse-ie/refs/heads/main/screenshots/opendata-ncse-ie-2026-06-20T190943.png
security:
- kind: domain-security
  name: Opendata Ncse Ie Domain Security
  slug: opendata-ncse-ie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opendata-ncse-ie
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Ireland
website: https://opendata.ncse.ie
---
