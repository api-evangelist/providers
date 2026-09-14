---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - '{''url'': ''https://donnees.ville.montreal.qc.ca'', ''status'': 302, ''note'': ''declared website redirects to https://donnees.montreal.ca/ — a different registrable domain (qc.ca -> montreal.ca), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: CKAN Action API for Montréal, Québec, a consistent JSON-over-HTTP interface over a catalog of 401 datasets. Standard actions include package_search, package_show, package_list, organization_list, grou
  name: Montréal, Québec CKAN Action API
  slug: catalog
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/donnees-ville-montreal-qc-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donnees.ville.montreal.qc.ca
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/donnees-ville-montreal-qc-ca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/donnees-ville-montreal-qc-ca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/donnees-ville-montreal-qc-ca-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-04'
description: Montréal, Québec is a open data portal open-data portal for Canada running CKAN. It exposes the CKAN catalog API, a standardized machine-readable interface over approximately 401 datasets, supporting programmatic dataset search, metadata retrieval, and resource access. Because it runs CKAN, it shares a consistent API surface with every other CKAN portal, making it uniformly harvestable and integrable.
finops:
- name: Donnees Ville Montreal Qc Ca Finops
  service_category: Open Data
  slug: donnees-ville-montreal-qc-ca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/donnees-ville-montreal-qc-ca.png
layout: provider
modified: '2026-06-04'
name: Montréal, Québec
nav: Providers
network: true
overview: 'Montréal, Québec publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and Government Data.


  Montréal, Québec''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Donnees Ville Montreal Qc Ca Plans Pricing
  plan_count: 1
  slug: donnees-ville-montreal-qc-ca-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Donnees Ville Montreal Qc Ca Rate Limits
  slug: donnees-ville-montreal-qc-ca-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/donnees-ville-montreal-qc-ca/refs/heads/main/screenshots/donnees-ville-montreal-qc-ca-2026-06-20T180150.png
security:
- kind: domain-security
  name: Donnees Ville Montreal Qc Ca Domain Security
  slug: donnees-ville-montreal-qc-ca-domain-security
  summary_line: TLSv1.3
slug: donnees-ville-montreal-qc-ca
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- Government Data
- Open Data Portal
- Canada
website: https://donnees.ville.montreal.qc.ca
---
