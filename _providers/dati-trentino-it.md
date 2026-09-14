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
- description: 'CKAN Action API for Open Data Trentino, a consistent JSON-over-HTTP interface over a catalog of 1,381 datasets. Standard actions include package_search, package_show, package_list, organization_list, '
  name: Open Data Trentino CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-trentino-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.trentino.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-trentino-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-trentino-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-trentino-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Open Data Trentino is a open data portal open-data portal for Italy running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,381 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dati Trentino It Finops
  service_category: Open Data
  slug: dati-trentino-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-trentino-it.png
layout: provider
modified: '2026-06-04'
name: Open Data Trentino
nav: Providers
network: true
overview: 'Open Data Trentino publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Open Data Trentino''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Trentino It Plans Pricing
  plan_count: 1
  slug: dati-trentino-it-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Dati Trentino It Rate Limits
  slug: dati-trentino-it-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-trentino-it/refs/heads/main/screenshots/dati-trentino-it-2026-06-20T175707.png
security:
- kind: domain-security
  name: Dati Trentino It Domain Security
  slug: dati-trentino-it-domain-security
  summary_line: TLSv1.2
slug: dati-trentino-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Italy
website: https://dati.trentino.it
---
