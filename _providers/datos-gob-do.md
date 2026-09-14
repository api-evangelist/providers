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
- description: CKAN Action API for Portal de Datos Abiertos Republica Dominicana, a consistent JSON-over-HTTP interface over a catalog of 1,054 datasets. Standard actions include package_search, package_show, packag
  name: Portal de Datos Abiertos Republica Dominicana CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datos-gob-do-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datos.gob.do
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/datos-gob-do-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datos-gob-do-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datos-gob-do-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Portal de Datos Abiertos Republica Dominicana is a national government open-data portal for Dominican Republic running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 1,054 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Datos Gob Do Finops
  service_category: Open Data
  slug: datos-gob-do-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datos-gob-do.png
layout: provider
modified: '2026-06-04'
name: Portal de Datos Abiertos Republica Dominicana
nav: Providers
network: true
overview: 'Portal de Datos Abiertos Republica Dominicana publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Portal de Datos Abiertos Republica Dominicana''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Datos Gob Do Plans Pricing
  plan_count: 1
  slug: datos-gob-do-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Datos Gob Do Rate Limits
  slug: datos-gob-do-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/datos-gob-do/refs/heads/main/screenshots/datos-gob-do-2026-06-20T175717.png
security:
- kind: domain-security
  name: Datos Gob Do Domain Security
  slug: datos-gob-do-domain-security
  summary_line: TLSv1.3
slug: datos-gob-do
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Dominican Republic
website: https://datos.gob.do
---
