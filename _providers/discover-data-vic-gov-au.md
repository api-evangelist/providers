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
- description: CKAN Action API for DataVic Victoria, a consistent JSON-over-HTTP interface over a catalog of 5,585 datasets. Standard actions include package_search, package_show, package_list, organization_list, gr
  name: DataVic Victoria CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/discover-data-vic-gov-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://discover.data.vic.gov.au
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/discover-data-vic-gov-au-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/discover-data-vic-gov-au-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/discover-data-vic-gov-au-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: DataVic Victoria is a state government open-data portal for Australia running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 5,585 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Discover Data Vic Gov Au Finops
  service_category: Open Data
  slug: discover-data-vic-gov-au-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/discover-data-vic-gov-au.png
layout: provider
modified: '2026-06-04'
name: DataVic Victoria
nav: Providers
network: true
overview: 'DataVic Victoria publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  DataVic Victoria''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Discover Data Vic Gov Au Plans Pricing
  plan_count: 1
  slug: discover-data-vic-gov-au-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Discover Data Vic Gov Au Rate Limits
  slug: discover-data-vic-gov-au-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/discover-data-vic-gov-au/refs/heads/main/screenshots/discover-data-vic-gov-au-2026-06-20T180044.png
security:
- kind: domain-security
  name: Discover Data Vic Gov Au Domain Security
  slug: discover-data-vic-gov-au-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: discover-data-vic-gov-au
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- Australia
website: https://discover.data.vic.gov.au
---
