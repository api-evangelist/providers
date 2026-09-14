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
- description: CKAN Action API for Montpellier Open Data, a consistent JSON-over-HTTP interface over a catalog of 0 datasets. Standard actions include package_search, package_show, package_list, organization_list, g
  name: Montpellier Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-montpellier3m-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.montpellier3m.fr
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-montpellier3m-fr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-montpellier3m-fr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-montpellier3m-fr-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-07'
description: Montpellier Open Data is a municipal government open-data portal for France running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 0 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Montpellier3M Fr Finops
  service_category: Open Data
  slug: data-montpellier3m-fr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-montpellier3m-fr.png
layout: provider
modified: '2026-06-07'
name: Montpellier Open Data
nav: Providers
network: true
overview: 'Montpellier Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Montpellier Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Montpellier3M Fr Plans Pricing
  plan_count: 1
  slug: data-montpellier3m-fr-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Data Montpellier3M Fr Rate Limits
  slug: data-montpellier3m-fr-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-montpellier3m-fr/refs/heads/main/screenshots/data-montpellier3m-fr-2026-06-20T175553.png
security:
- kind: domain-security
  name: Data Montpellier3M Fr Domain Security
  slug: data-montpellier3m-fr-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: data-montpellier3m-fr
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Municipal Government
- France
website: https://data.montpellier3m.fr
---
