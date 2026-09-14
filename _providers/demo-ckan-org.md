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
- description: 'CKAN Action API for CKAN Demo, a consistent JSON-over-HTTP interface over a catalog of 13 datasets. Standard actions include package_search, package_show, package_list, organization_list, group_list, '
  name: CKAN Demo CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demo-ckan-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demo.ckan.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/demo-ckan-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/demo-ckan-org-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/demo-ckan-org-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: CKAN Demo is a organization open-data portal running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 13 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Demo Ckan Org Finops
  service_category: Open Data
  slug: demo-ckan-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demo-ckan-org.png
layout: provider
modified: '2026-06-04'
name: CKAN Demo
nav: Providers
network: true
overview: 'CKAN Demo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Organization.


  CKAN Demo''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Demo Ckan Org Plans Pricing
  plan_count: 1
  slug: demo-ckan-org-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Demo Ckan Org Rate Limits
  slug: demo-ckan-org-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/demo-ckan-org/refs/heads/main/screenshots/demo-ckan-org-2026-06-20T175907.png
security:
- kind: domain-security
  name: Demo Ckan Org Domain Security
  slug: demo-ckan-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: demo-ckan-org
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Organization
- Global
website: https://demo.ckan.org
---
