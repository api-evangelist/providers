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
- description: CKAN Action API for Rondonia Open Data, ~14 datasets. Base URL https://dados.ro.gov.br/api/3/action/.
  name: Rondonia Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-ro-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.ro.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-ro-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-ro-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-ro-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Rondonia Open Data is a state government open-data portal for Brazil running CKAN. It exposes the CKAN catalog API over approximately 14 datasets.
finops:
- name: Dados Ro Gov Br Finops
  service_category: ''
  slug: dados-ro-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-ro-gov-br.png
layout: provider
modified: '2026-06-07'
name: Rondonia Open Data
nav: Providers
network: true
overview: 'Rondonia Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Rondonia Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Ro Gov Br Plans Pricing
  plan_count: 1
  slug: dados-ro-gov-br-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Dados Ro Gov Br Rate Limits
  slug: dados-ro-gov-br-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-ro-gov-br/refs/heads/main/screenshots/dados-ro-gov-br-2026-06-20T175434.png
security:
- kind: domain-security
  name: Dados Ro Gov Br Domain Security
  slug: dados-ro-gov-br-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC
slug: dados-ro-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- State-Government
- Brazil
website: https://dados.ro.gov.br
---
