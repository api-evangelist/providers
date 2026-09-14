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
- description: CKAN Action API for Western Australia Data Catalogue, a consistent JSON-over-HTTP interface over a catalog of 2,909 datasets. Standard actions include package_search, package_show, package_list, organ
  name: Western Australia Data Catalogue CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catalogue-data-wa-gov-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catalogue.data.wa.gov.au
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/catalogue-data-wa-gov-au-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/catalogue-data-wa-gov-au-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/catalogue-data-wa-gov-au-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Western Australia Data Catalogue is a state government open-data portal for Australia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 2,909 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Catalogue Data Wa Gov Au Finops
  service_category: Open Data
  slug: catalogue-data-wa-gov-au-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catalogue-data-wa-gov-au.png
layout: provider
modified: '2026-06-04'
name: Western Australia Data Catalogue
nav: Providers
network: true
overview: 'Western Australia Data Catalogue publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Western Australia Data Catalogue''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Catalogue Data Wa Gov Au Plans Pricing
  plan_count: 1
  slug: catalogue-data-wa-gov-au-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Catalogue Data Wa Gov Au Rate Limits
  slug: catalogue-data-wa-gov-au-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/catalogue-data-wa-gov-au/refs/heads/main/screenshots/catalogue-data-wa-gov-au-2026-06-20T174048.png
security:
- kind: domain-security
  name: Catalogue Data Wa Gov Au Domain Security
  slug: catalogue-data-wa-gov-au-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: catalogue-data-wa-gov-au
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- Australia
website: https://catalogue.data.wa.gov.au
---
