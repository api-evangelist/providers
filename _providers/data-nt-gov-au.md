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
- description: CKAN Action API for Northern Territory Open Data, a consistent JSON-over-HTTP interface over a catalog of 1,071 datasets. Standard actions include package_search, package_show, package_list, organizat
  name: Northern Territory Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-nt-gov-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.nt.gov.au
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-nt-gov-au-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-nt-gov-au-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-nt-gov-au-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Northern Territory Open Data is a territorial government open-data portal for Australia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,071 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Nt Gov Au Finops
  service_category: Open Data
  slug: data-nt-gov-au-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-nt-gov-au.png
layout: provider
modified: '2026-06-04'
name: Northern Territory Open Data
nav: Providers
network: true
overview: 'Northern Territory Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Northern Territory Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Nt Gov Au Plans Pricing
  plan_count: 1
  slug: data-nt-gov-au-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Data Nt Gov Au Rate Limits
  slug: data-nt-gov-au-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-nt-gov-au/refs/heads/main/screenshots/data-nt-gov-au-2026-06-20T175608.png
security:
- kind: domain-security
  name: Data Nt Gov Au Domain Security
  slug: data-nt-gov-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data-nt-gov-au
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Territorial Government
- Australia
website: https://data.nt.gov.au
---
