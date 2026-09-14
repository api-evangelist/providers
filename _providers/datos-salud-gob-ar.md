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
- description: CKAN Action API for Datos Abiertos Salud Argentina, a consistent JSON-over-HTTP interface over a catalog of 64 datasets. Standard actions include package_search, package_show, package_list, organizati
  name: Datos Abiertos Salud Argentina CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-salud-gob-ar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.salud.gob.ar
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-salud-gob-ar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-salud-gob-ar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-salud-gob-ar-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Datos Abiertos Salud Argentina is a government agency open-data portal for Argentina running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 64 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Salud Gob Ar Finops
  service_category: Open Data
  slug: datos-salud-gob-ar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-salud-gob-ar.png
layout: provider
modified: '2026-06-04'
name: Datos Abiertos Salud Argentina
nav: Providers
network: true
overview: 'Datos Abiertos Salud Argentina publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Datos Abiertos Salud Argentina''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Salud Gob Ar Plans Pricing
  plan_count: 1
  slug: datos-salud-gob-ar-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Datos Salud Gob Ar Rate Limits
  slug: datos-salud-gob-ar-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-salud-gob-ar/refs/heads/main/screenshots/datos-salud-gob-ar-2026-06-20T175724.png
security:
- kind: domain-security
  name: Datos Salud Gob Ar Domain Security
  slug: datos-salud-gob-ar-domain-security
  summary_line: DNSSEC
slug: datos-salud-gob-ar
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Argentina
website: https://datos.salud.gob.ar
---
