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
- description: CKAN Action API for Portal de Dados Abertos – Prefeitura de Belo Horizonte, a consistent JSON-over-HTTP interface over a catalog of 588 datasets. Standard actions include package_search, package_show,
  name: Portal de Dados Abertos – Prefeitura de Belo Horizonte CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dados-pbh-gov-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dados.pbh.gov.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dados-pbh-gov-br-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dados-pbh-gov-br-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dados-pbh-gov-br-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Portal de Dados Abertos – Prefeitura de Belo Horizonte is a open data portal open-data portal for Brazil running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 588 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dados Pbh Gov Br Finops
  service_category: Open Data
  slug: dados-pbh-gov-br-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dados-pbh-gov-br.png
layout: provider
modified: '2026-06-04'
name: Portal de Dados Abertos – Prefeitura de Belo Horizonte
nav: Providers
network: true
overview: 'Portal de Dados Abertos – Prefeitura de Belo Horizonte publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Portal de Dados Abertos – Prefeitura de Belo Horizonte''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dados Pbh Gov Br Plans Pricing
  plan_count: 1
  slug: dados-pbh-gov-br-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Dados Pbh Gov Br Rate Limits
  slug: dados-pbh-gov-br-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dados-pbh-gov-br/refs/heads/main/screenshots/dados-pbh-gov-br-2026-06-20T175429.png
security:
- kind: domain-security
  name: Dados Pbh Gov Br Domain Security
  slug: dados-pbh-gov-br-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dados-pbh-gov-br
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Brazil
website: https://dados.pbh.gov.br
---
