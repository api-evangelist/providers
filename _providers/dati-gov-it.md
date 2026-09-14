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
- description: CKAN Action API for dati.gov.it, a consistent JSON-over-HTTP interface over a catalog of 65,388 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_
  name: dati.gov.it CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dati-gov-it-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dati.gov.it/opendata
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/dati-gov-it-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dati-gov-it-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dati-gov-it-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: dati.gov.it is a national government open-data portal for Italy running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 65,388 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Dati Gov It Finops
  service_category: Open Data
  slug: dati-gov-it-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dati-gov-it.png
layout: provider
modified: '2026-06-04'
name: dati.gov.it
nav: Providers
network: true
overview: 'dati.gov.it publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  dati.gov.it''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Dati Gov It Plans Pricing
  plan_count: 1
  slug: dati-gov-it-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Dati Gov It Rate Limits
  slug: dati-gov-it-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dati-gov-it/refs/heads/main/screenshots/dati-gov-it-2026-06-20T175659.png
security:
- kind: domain-security
  name: Dati Gov It Domain Security
  slug: dati-gov-it-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: dati-gov-it
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Italy
website: https://www.dati.gov.it/opendata
---
