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
- description: CKAN Action API for Data.gov Inventory, a consistent JSON-over-HTTP interface over a catalog of an open datasets. Standard actions include package_search, package_show, package_list, organization_list
  name: Data.gov Inventory CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inventory-data-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inventory.data.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/inventory-data-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inventory-data-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inventory-data-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Data.gov Inventory is a federal government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately an open datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Inventory Data Gov Finops
  service_category: Open Data
  slug: inventory-data-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inventory-data-gov.png
layout: provider
modified: '2026-06-04'
name: Data.gov Inventory
nav: Providers
network: true
overview: 'Data.gov Inventory publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Data.gov Inventory''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Inventory Data Gov Plans Pricing
  plan_count: 1
  slug: inventory-data-gov-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Inventory Data Gov Rate Limits
  slug: inventory-data-gov-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/inventory-data-gov/refs/heads/main/screenshots/inventory-data-gov-2026-06-20T183518.png
security:
- kind: domain-security
  name: Inventory Data Gov Domain Security
  slug: inventory-data-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: inventory-data-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Federal-Government
- United States
website: https://inventory.data.gov
---
