---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: CKAN Action API for data.gov.hr, a consistent JSON-over-HTTP interface over a catalog of roughly 3,858 datasets. Standard actions include package_search, package_show, package_list, organization_list,
  name: data.gov.hr CKAN Action API
  slug: catalog
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-hr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.hr/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ckan.org/en/latest/api/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: data.gov.hr (Portal otvorenih podataka) is the national government open-data portal for Croatia, operated by the Ministry of Justice and Public Administration. It runs CKAN 2.9.9 and exposes the standard CKAN Action API over approximately 3,858 datasets, supporting programmatic dataset search, metadata retrieval, and resource access, plus DCAT-AP RDF/XML catalog feeds for EU harvesting. Note that the CKAN API is mounted under a non-default /ckan/ path prefix; root-level CKAN URLs return the Vue single-page-app HTML rather than JSON.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-hr.png
layout: provider
modified: '2026-06-23'
name: data.gov.hr
nav: Providers
network: true
overview: 'data.gov.hr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, DCAT, and DCAT-AP.


  data.gov.hr''s developer surface includes documentation and 3 more developer resources.'
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/data-gov-hr/refs/heads/main/screenshots/data-gov-hr-2026-07-25T211249.png
security:
- kind: domain-security
  name: Data Gov Hr Domain Security
  slug: data-gov-hr-domain-security
  summary_line: TLSv1.3
slug: data-gov-hr
tags:
- Open Data
- CKAN
- Data Catalog
- DCAT
- DCAT-AP
- Government Data
- National Government
- Croatia
- Europe
website: https://data.gov.hr/en/
---
