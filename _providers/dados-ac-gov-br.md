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
- description: CKAN Action API for Acre Open Data, ~20 datasets. Base URL https://dados.ac.gov.br/api/3/action/.
  name: Acre Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-ac-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.ac.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-ac-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-ac-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-ac-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Acre Open Data is a state government open-data portal for Brazil running CKAN. It exposes the CKAN catalog API over approximately 20 datasets.
finops:
- name: Dados Ac Gov Br Finops
  service_category: ''
  slug: dados-ac-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-ac-gov-br.png
layout: provider
modified: '2026-06-07'
name: Acre Open Data
nav: Providers
network: true
overview: 'Acre Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Acre Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Ac Gov Br Plans Pricing
  plan_count: 1
  slug: dados-ac-gov-br-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Dados Ac Gov Br Rate Limits
  slug: dados-ac-gov-br-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-ac-gov-br/refs/heads/main/screenshots/dados-ac-gov-br-2026-06-20T175422.png
security:
- kind: domain-security
  name: Dados Ac Gov Br Domain Security
  slug: dados-ac-gov-br-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dados-ac-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- State-Government
- Brazil
website: https://dados.ac.gov.br
---
