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
- description: CKAN Action API for San Bernardino County ATC OpenData, a consistent JSON-over-HTTP interface over a catalog of 8 datasets. Standard actions include package_search, package_show, package_list, organiz
  name: San Bernardino County ATC OpenData CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-sbcountyatc-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.sbcountyatc.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/opendata-sbcountyatc-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opendata-sbcountyatc-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opendata-sbcountyatc-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: San Bernardino County ATC OpenData is a county government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 8 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Opendata Sbcountyatc Gov Finops
  service_category: Open Data
  slug: opendata-sbcountyatc-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-sbcountyatc-gov.png
layout: provider
modified: '2026-06-04'
name: San Bernardino County ATC OpenData
nav: Providers
network: true
overview: 'San Bernardino County ATC OpenData publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  San Bernardino County ATC OpenData''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Opendata Sbcountyatc Gov Plans Pricing
  plan_count: 1
  slug: opendata-sbcountyatc-gov-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Opendata Sbcountyatc Gov Rate Limits
  slug: opendata-sbcountyatc-gov-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-sbcountyatc-gov/refs/heads/main/screenshots/opendata-sbcountyatc-gov-2026-06-20T190946.png
security:
- kind: domain-security
  name: Opendata Sbcountyatc Gov Domain Security
  slug: opendata-sbcountyatc-gov-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opendata-sbcountyatc-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- County Government
- United States
website: https://opendata.sbcountyatc.gov
---
