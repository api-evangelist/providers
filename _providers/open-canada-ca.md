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
api_count: 2
apis:
- description: CKAN Action API for Open Government Canada, a consistent JSON-over-HTTP interface over a catalog of 47,344 datasets. Standard actions include package_search, package_show, package_list, organization_l
  name: Open Government Canada CKAN Action API
  slug: catalog
- description: Canadian Government Open Data
  name: Open Government, Canada
  slug: open-government-canada
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-canada-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open.canada.ca/data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/open-canada-ca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-canada-ca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-canada-ca-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Open Government Canada is a national government open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 47,344 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Open Canada Ca Finops
  service_category: Open Data
  slug: open-canada-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-canada-ca.png
layout: provider
modified: '2026-06-04'
name: Open Government Canada
nav: Providers
network: true
overview: 'Open Government Canada publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Open Government Canada''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Open Canada Ca Plans Pricing
  plan_count: 1
  slug: open-canada-ca-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Open Canada Ca Rate Limits
  slug: open-canada-ca-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/open-canada-ca/refs/heads/main/screenshots/open-canada-ca-2026-06-20T190739.png
security:
- kind: domain-security
  name: Open Canada Ca Domain Security
  slug: open-canada-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-canada-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Canada
website: https://open.canada.ca/data
---
