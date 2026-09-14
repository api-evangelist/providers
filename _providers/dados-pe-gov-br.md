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
- description: CKAN Action API for Pernambuco Open Data, covering ~40 datasets. Base URL https://dados.pe.gov.br/api/3/action/.
  name: Pernambuco Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-pe-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.pe.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-pe-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-pe-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-pe-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Pernambuco Open Data is a state government open-data portal for Brazil running CKAN. It exposes the CKAN catalog API over approximately 40 datasets.
finops:
- name: Dados Pe Gov Br Finops
  service_category: ''
  slug: dados-pe-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-pe-gov-br.png
layout: provider
modified: '2026-06-07'
name: Pernambuco Open Data
nav: Providers
network: true
overview: 'Pernambuco Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Pernambuco Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Pe Gov Br Plans Pricing
  plan_count: 1
  slug: dados-pe-gov-br-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Dados Pe Gov Br Rate Limits
  slug: dados-pe-gov-br-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-pe-gov-br/refs/heads/main/screenshots/dados-pe-gov-br-2026-06-20T175429.png
security:
- kind: domain-security
  name: Dados Pe Gov Br Domain Security
  slug: dados-pe-gov-br-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dados-pe-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- Brazil
website: https://dados.pe.gov.br
---
