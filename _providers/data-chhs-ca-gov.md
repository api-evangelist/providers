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
- description: CKAN Action API for California Health and Human Services, a consistent JSON-over-HTTP interface over a catalog of 481 datasets. Standard actions include package_search, package_show, package_list, org
  name: California Health and Human Services CKAN Action API
  slug: catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-chhs-ca-gov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-chhs-ca-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.chhs.ca.gov
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-chhs-ca-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-chhs-ca-gov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-chhs-ca-gov-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: California Health and Human Services is a state government open-data portal for United States running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 481 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Chhs Ca Gov Finops
  service_category: Open Data
  slug: data-chhs-ca-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-chhs-ca-gov.png
layout: provider
modified: '2026-06-04'
name: California Health and Human Services
nav: Providers
network: true
overview: 'California Health and Human Services publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  California Health and Human Services'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Data Chhs Ca Gov Plans Pricing
  plan_count: 1
  slug: data-chhs-ca-gov-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Data Chhs Ca Gov Rate Limits
  slug: data-chhs-ca-gov-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-chhs-ca-gov/refs/heads/main/screenshots/data-chhs-ca-gov-2026-06-20T175514.png
security:
- kind: domain-security
  name: Data Chhs Ca Gov Domain Security
  slug: data-chhs-ca-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Data Chhs Ca Gov Vulnerability Disclosure
  slug: data-chhs-ca-gov-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: data-chhs-ca-gov
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- State-Government
- United States
website: https://data.chhs.ca.gov
---
