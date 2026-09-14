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
- description: CKAN Action API for BC Data Catalogue, a consistent JSON-over-HTTP interface over a catalog of 3,346 datasets. Standard actions include package_search, package_show, package_list, organization_list, g
  name: BC Data Catalogue CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catalogue-data-gov-bc-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catalogue.data.gov.bc.ca
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/catalogue-data-gov-bc-ca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/catalogue-data-gov-bc-ca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/catalogue-data-gov-bc-ca-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: BC Data Catalogue is a provincial government open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 3,346 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Catalogue Data Gov Bc Ca Finops
  service_category: Open Data
  slug: catalogue-data-gov-bc-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catalogue-data-gov-bc-ca.png
layout: provider
modified: '2026-06-04'
name: BC Data Catalogue
nav: Providers
network: true
overview: 'BC Data Catalogue publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  BC Data Catalogue''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Catalogue Data Gov Bc Ca Plans Pricing
  plan_count: 1
  slug: catalogue-data-gov-bc-ca-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Catalogue Data Gov Bc Ca Rate Limits
  slug: catalogue-data-gov-bc-ca-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/catalogue-data-gov-bc-ca/refs/heads/main/screenshots/catalogue-data-gov-bc-ca-2026-06-20T174050.png
security:
- kind: domain-security
  name: Catalogue Data Gov Bc Ca Domain Security
  slug: catalogue-data-gov-bc-ca-domain-security
  summary_line: TLSv1.3
slug: catalogue-data-gov-bc-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Provincial Government
- Canada
website: https://catalogue.data.gov.bc.ca
---
