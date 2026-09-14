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
- description: CKAN Action API for Lazio Open Data, covering ~406 datasets. Base URL https://dati.lazio.it/api/3/action/.
  name: Lazio Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-lazio-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.lazio.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-lazio-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-lazio-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-lazio-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Lazio Open Data is a regional government open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 406 datasets.
finops:
- name: Dati Lazio It Finops
  service_category: ''
  slug: dati-lazio-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-lazio-it.png
layout: provider
modified: '2026-06-07'
name: Lazio Open Data
nav: Providers
network: true
overview: 'Lazio Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Lazio Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Lazio It Plans Pricing
  plan_count: 1
  slug: dati-lazio-it-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Dati Lazio It Rate Limits
  slug: dati-lazio-it-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-lazio-it/refs/heads/main/screenshots/dati-lazio-it-2026-06-20T175706.png
security:
- kind: domain-security
  name: Dati Lazio It Domain Security
  slug: dati-lazio-it-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dati-lazio-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Regional Government
- Italy
website: https://dati.lazio.it
---
