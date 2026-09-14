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
- description: CKAN Action API for IATI Registry, a consistent JSON-over-HTTP interface over a catalog of 13,656 datasets. Standard actions include package_search, package_show, package_list, organization_list, grou
  name: IATI Registry CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iatiregistry-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iatiregistry.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/iatiregistry-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iatiregistry-org-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iatiregistry-org-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: IATI Registry is a open data portal open-data portal running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 13,656 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Iatiregistry Org Finops
  service_category: Open Data
  slug: iatiregistry-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iatiregistry-org.png
layout: provider
modified: '2026-06-04'
name: IATI Registry
nav: Providers
network: true
overview: 'IATI Registry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  IATI Registry''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Iatiregistry Org Plans Pricing
  plan_count: 1
  slug: iatiregistry-org-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Iatiregistry Org Rate Limits
  slug: iatiregistry-org-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/iatiregistry-org/refs/heads/main/screenshots/iatiregistry-org-2026-06-20T183113.png
security:
- kind: domain-security
  name: Iatiregistry Org Domain Security
  slug: iatiregistry-org-domain-security
  summary_line: TLSv1.3
slug: iatiregistry-org
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- International
website: https://iatiregistry.org
---
