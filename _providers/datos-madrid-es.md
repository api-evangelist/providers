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
- description: CKAN Action API for Datos abiertos, a consistent JSON-over-HTTP interface over a catalog of 667 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_
  name: Datos abiertos CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-madrid-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.madrid.es
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-madrid-es-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-madrid-es-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-madrid-es-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Datos abiertos is a open data portal open-data portal for Spain running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 667 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Madrid Es Finops
  service_category: Open Data
  slug: datos-madrid-es-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-madrid-es.png
layout: provider
modified: '2026-06-04'
name: Datos abiertos
nav: Providers
network: true
overview: 'Datos abiertos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Datos abiertos'' developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Madrid Es Plans Pricing
  plan_count: 1
  slug: datos-madrid-es-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Datos Madrid Es Rate Limits
  slug: datos-madrid-es-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-madrid-es/refs/heads/main/screenshots/datos-madrid-es-2026-06-20T175723.png
security:
- kind: domain-security
  name: Datos Madrid Es Domain Security
  slug: datos-madrid-es-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datos-madrid-es
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Spain
website: https://datos.madrid.es
---
