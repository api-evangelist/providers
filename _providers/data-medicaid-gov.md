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
- description: DKAN open-data API for Medicaid Open Data, covering a catalog of 255 datasets. Provides the DKAN search API (/api/1/search), the metastore (/api/1/metastore/schemas/dataset/items), and a CKAN-compatib
  name: Medicaid Open Data DKAN API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-medicaid-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.medicaid.gov
- group: docs
  title: ''
  type: Documentation
  url: https://dkan.readthedocs.io/en/latest/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-medicaid-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-medicaid-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-medicaid-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Medicaid Open Data is a federal government open-data portal for United States running DKAN. It exposes the DKAN catalog API, a standardized machine-readable interface over approximately 255 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs DKAN, it shares a consistent API surface with every other DKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Medicaid Gov Finops
  service_category: Open Data
  slug: data-medicaid-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-medicaid-gov.png
layout: provider
modified: '2026-06-04'
name: Medicaid Open Data
nav: Providers
network: true
overview: 'Medicaid Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, DKAN, Data Catalog, DCAT, and Government Data.


  Medicaid Open Data''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Medicaid Gov Plans Pricing
  plan_count: 1
  slug: data-medicaid-gov-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Data Medicaid Gov Rate Limits
  slug: data-medicaid-gov-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-medicaid-gov/refs/heads/main/screenshots/data-medicaid-gov-2026-06-20T175546.png
security:
- kind: domain-security
  name: Data Medicaid Gov Domain Security
  slug: data-medicaid-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: data-medicaid-gov
tags:
- Open Data
- DKAN
- Data Catalog
- DCAT
- Government Data
- Federal-Government
- United States
website: https://data.medicaid.gov
---
