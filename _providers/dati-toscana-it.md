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
- description: CKAN Action API for Open Data Regione Toscana, a consistent JSON-over-HTTP interface over a catalog of 12,382 datasets. Standard actions include package_search, package_show, package_list, organizatio
  name: Open Data Regione Toscana CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-toscana-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.toscana.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-toscana-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-toscana-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-toscana-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Open Data Regione Toscana is a open data portal open-data portal for Italy running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 12,382 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dati Toscana It Finops
  service_category: Open Data
  slug: dati-toscana-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-toscana-it.png
layout: provider
modified: '2026-06-04'
name: Open Data Regione Toscana
nav: Providers
network: true
overview: 'Open Data Regione Toscana publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Open Data Regione Toscana''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Toscana It Plans Pricing
  plan_count: 1
  slug: dati-toscana-it-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Dati Toscana It Rate Limits
  slug: dati-toscana-it-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-toscana-it/refs/heads/main/screenshots/dati-toscana-it-2026-06-20T175713.png
security:
- kind: domain-security
  name: Dati Toscana It Domain Security
  slug: dati-toscana-it-domain-security
  summary_line: TLSv1.3
slug: dati-toscana-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Italy
website: https://dati.toscana.it
---
