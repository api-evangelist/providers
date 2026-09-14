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
- description: 'CKAN Action API for London Datastore, a consistent JSON-over-HTTP interface over a catalog of an open datasets. Standard actions include package_search, package_show, package_list, organization_list, '
  name: London Datastore CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-london-gov-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.london.gov.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/data-london-gov-uk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/data-london-gov-uk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/data-london-gov-uk-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://data.london.gov.uk/feed/
created: '2026-06-04'
description: London Datastore is a open data portal open-data portal for GB running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately an open datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Data London Gov Uk Finops
  service_category: Open Data
  slug: data-london-gov-uk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-london-gov-uk.png
layout: provider
modified: '2026-06-04'
name: London Datastore
nav: Providers
network: true
overview: 'London Datastore publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  London Datastore''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Data London Gov Uk Plans Pricing
  plan_count: 1
  slug: data-london-gov-uk-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Data London Gov Uk Rate Limits
  slug: data-london-gov-uk-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/data-london-gov-uk/refs/heads/main/screenshots/data-london-gov-uk-2026-06-20T175547.png
security:
- kind: domain-security
  name: Data London Gov Uk Domain Security
  slug: data-london-gov-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data-london-gov-uk
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- GB
website: https://data.london.gov.uk
---
