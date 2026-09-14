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
- description: CKAN Action API for datos.misiones.gov.ar, a consistent JSON-over-HTTP interface over a catalog of 2 datasets. Standard actions include package_search, package_show, package_list, organization_list, g
  name: datos.misiones.gov.ar CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-misiones-gov-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datos.misiones.gov.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-misiones-gov-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-misiones-gov-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-misiones-gov-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: datos.misiones.gov.ar is a open data portal open-data portal for Argentina running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 2 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Misiones Gov Ar Finops
  service_category: Open Data
  slug: datos-misiones-gov-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-misiones-gov-ar.png
layout: provider
modified: '2026-06-04'
name: datos.misiones.gov.ar
nav: Providers
network: true
overview: 'datos.misiones.gov.ar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  datos.misiones.gov.ar''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Misiones Gov Ar Plans Pricing
  plan_count: 1
  slug: datos-misiones-gov-ar-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Datos Misiones Gov Ar Rate Limits
  slug: datos-misiones-gov-ar-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-misiones-gov-ar/refs/heads/main/screenshots/datos-misiones-gov-ar-2026-06-20T175723.png
security:
- kind: domain-security
  name: Datos Misiones Gov Ar Domain Security
  slug: datos-misiones-gov-ar-domain-security
  summary_line: DMARC
slug: datos-misiones-gov-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Argentina
website: https://www.datos.misiones.gov.ar
---
