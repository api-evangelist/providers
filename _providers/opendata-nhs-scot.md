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
- description: CKAN Action API for NHS Scotland Open Data, a consistent JSON-over-HTTP interface over a catalog of 104 datasets. Standard actions include package_search, package_show, package_list, organization_list
  name: NHS Scotland Open Data CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-nhs-scot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opendata.nhs.scot
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-nhs-scot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-nhs-scot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-nhs-scot-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: NHS Scotland Open Data is a government agency open-data portal for United Kingdom running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 104 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Nhs Scot Finops
  service_category: Open Data
  slug: opendata-nhs-scot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-nhs-scot.png
layout: provider
modified: '2026-06-04'
name: NHS Scotland Open Data
nav: Providers
network: true
overview: 'NHS Scotland Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  NHS Scotland Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Nhs Scot Plans Pricing
  plan_count: 1
  slug: opendata-nhs-scot-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Opendata Nhs Scot Rate Limits
  slug: opendata-nhs-scot-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-nhs-scot/refs/heads/main/screenshots/opendata-nhs-scot-2026-06-20T190944.png
security:
- kind: domain-security
  name: Opendata Nhs Scot Domain Security
  slug: opendata-nhs-scot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opendata-nhs-scot
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Government Agency
- United Kingdom
website: https://www.opendata.nhs.scot
---
