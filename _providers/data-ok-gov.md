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
- description: 'CKAN Action API for Oklahoma, a consistent JSON-over-HTTP interface over a catalog of 391 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_list, '
  name: Oklahoma CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-ok-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.ok.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-ok-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-ok-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-ok-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Oklahoma is a open data portal open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 391 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Ok Gov Finops
  service_category: Open Data
  slug: data-ok-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-ok-gov.png
layout: provider
modified: '2026-06-04'
name: Oklahoma
nav: Providers
network: true
overview: 'Oklahoma publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Oklahoma''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Ok Gov Plans Pricing
  plan_count: 1
  slug: data-ok-gov-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Data Ok Gov Rate Limits
  slug: data-ok-gov-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-ok-gov/refs/heads/main/screenshots/data-ok-gov-2026-06-20T175601.png
security:
- kind: domain-security
  name: Data Ok Gov Domain Security
  slug: data-ok-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data-ok-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- United States
website: https://data.ok.gov
---
