---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: CKAN API for Consip Open Data, ~16 datasets.
  name: Consip Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-consip-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dati.consip.it
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-consip-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-consip-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-consip-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Consip Open Data is a government agency open-data portal for Italy running CKAN. It exposes the CKAN catalog API over approximately 16 datasets.
finops:
- name: Dati Consip It Finops
  service_category: ''
  slug: dati-consip-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-consip-it.png
layout: provider
modified: '2026-06-07'
name: Consip Open Data
nav: Providers
network: true
overview: 'Consip Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Consip Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Consip It Plans Pricing
  plan_count: 0
  slug: dati-consip-it-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Dati Consip It Rate Limits
  slug: dati-consip-it-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-consip-it/refs/heads/main/screenshots/dati-consip-it-2026-06-20T175659.png
security:
- kind: domain-security
  name: Dati Consip It Domain Security
  slug: dati-consip-it-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dati-consip-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- Italy
website: https://dati.consip.it
---
