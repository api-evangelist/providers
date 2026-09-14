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
- description: CKAN Action API for DATA GO JP, a consistent JSON-over-HTTP interface over a catalog of 18,366 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_l
  name: DATA GO JP CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-go-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.data.go.jp/data
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-go-jp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-go-jp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-go-jp-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: DATA GO JP is a national government open-data portal for Japan running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 18,366 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data Go Jp Finops
  service_category: Open Data
  slug: data-go-jp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-go-jp.png
layout: provider
modified: '2026-06-04'
name: DATA GO JP
nav: Providers
network: true
overview: 'DATA GO JP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  DATA GO JP''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Data Go Jp Plans Pricing
  plan_count: 1
  slug: data-go-jp-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Data Go Jp Rate Limits
  slug: data-go-jp-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-go-jp/refs/heads/main/screenshots/data-go-jp-2026-06-20T175626.png
security:
- kind: domain-security
  name: Data Go Jp Domain Security
  slug: data-go-jp-domain-security
  summary_line: TLSv1.3 · HSTS
slug: data-go-jp
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- National Government
- Japan
website: https://www.data.go.jp/data
---
