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
- description: CKAN Action API for California Open Data, a consistent JSON-over-HTTP interface over a catalog of 4,456 datasets. Standard actions include package_search, package_show, package_list, organization_list
  name: California Open Data CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-ca-gov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-ca-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.ca.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-ca-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-ca-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-ca-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: California Open Data is a state government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 4,456 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Ca Gov Finops
  service_category: Open Data
  slug: data-ca-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-ca-gov.png
layout: provider
modified: '2026-06-04'
name: California Open Data
nav: Providers
network: true
overview: 'California Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  California Open Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Data Ca Gov Plans Pricing
  plan_count: 1
  slug: data-ca-gov-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Data Ca Gov Rate Limits
  slug: data-ca-gov-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-ca-gov/refs/heads/main/screenshots/data-ca-gov-2026-06-20T175511.png
security:
- kind: domain-security
  name: Data Ca Gov Domain Security
  slug: data-ca-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Data Ca Gov Vulnerability Disclosure
  slug: data-ca-gov-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: data-ca-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- United States
website: https://data.ca.gov
---
