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
api_count: 2
apis:
- description: Bespoke REST API for opendata.gov.al at same-origin /api, with action-style routes. Known endpoints include POST /api/Dataset/filter (dataset search/listing), GET /api/Dataset/get/{slug}, GET /api/Dca
  name: Open Data Albania REST API
  slug: rest
- description: SPARQL query endpoint for the linked-data / DCAT-AP graph powering the portal.
  name: Open Data Albania SPARQL endpoint
  slug: sparql
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-gov-al-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.gov.al/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: opendata.gov.al is the national government open-data portal for Albania (Open Data Albania). It is a custom, DCAT-AP-compliant platform (an Angular single-page-app front end over a bespoke REST API) with a dedicated SPARQL query endpoint, and it is harvested into the EU data portal (data.europa.eu). It is not CKAN or DKAN. Read endpoints live under the /api prefix using PascalCase, action-style routes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-gov-al.png
layout: provider
modified: '2026-06-23'
name: opendata.gov.al (Open Data Albania)
nav: Providers
network: true
overview: opendata.gov.al (Open Data Albania) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, Custom Platform, DCAT-AP, SPARQL, and Linked Data.
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-gov-al/refs/heads/main/screenshots/opendata-gov-al-2026-08-07T190550.png
security:
- kind: domain-security
  name: Opendata Gov Al Domain Security
  slug: opendata-gov-al-domain-security
  summary_line: TLSv1.2
slug: opendata-gov-al
tags:
- Open Data
- Custom Platform
- DCAT-AP
- SPARQL
- Linked Data
- Government Data
- National Government
- Albania
- Europe
website: https://opendata.gov.al/
---
