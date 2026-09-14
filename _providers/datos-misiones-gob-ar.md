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
- description: CKAN Action API for Datos Provincia de Misiones, a consistent JSON-over-HTTP interface over a catalog of 2 datasets. Standard actions include package_search, package_show, package_list, organization_l
  name: Datos Provincia de Misiones CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-misiones-gob-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.misiones.gob.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-misiones-gob-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-misiones-gob-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-misiones-gob-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Datos Provincia de Misiones is a state government open-data portal for Argentina running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 2 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Misiones Gob Ar Finops
  service_category: Open Data
  slug: datos-misiones-gob-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-misiones-gob-ar.png
layout: provider
modified: '2026-06-04'
name: Datos Provincia de Misiones
nav: Providers
network: true
overview: 'Datos Provincia de Misiones publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Datos Provincia de Misiones'' developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Misiones Gob Ar Plans Pricing
  plan_count: 1
  slug: datos-misiones-gob-ar-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Datos Misiones Gob Ar Rate Limits
  slug: datos-misiones-gob-ar-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-misiones-gob-ar/refs/heads/main/screenshots/datos-misiones-gob-ar-2026-06-20T175722.png
security:
- kind: domain-security
  name: Datos Misiones Gob Ar Domain Security
  slug: datos-misiones-gob-ar-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: datos-misiones-gob-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- Argentina
website: https://datos.misiones.gob.ar
---
