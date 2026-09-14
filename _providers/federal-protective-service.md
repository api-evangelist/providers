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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-protective-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fpsdhs
- group: company
  title: ''
  type: Website
  url: https://www.dhs.gov/federal-protective-service
coverage:
  checked: '2026-09-09'
  detail: The Federal Protective Service publishes no host of its own (fps.dhs.gov does not resolve) and is absent from the Department of Homeland Security developer program at https://www.dhs.gov/developer, which lists only NTAS, MyTSA and FEMA APIs; the GSA federal API inventory carries no FPS row and the DHS Project Open Data catalog (1,168 datasets) has no FPS-published dataset or API distribution.
  evidence:
  - status: 200
    url: https://www.dhs.gov/developer
  - status: 200
    url: https://www.dhs.gov/data.json
  - status: 404
    url: https://www.dhs.gov/.well-known/api-catalog
  - status: 404
    url: https://www.dhs.gov/openapi.json
  - status: 200
    url: https://raw.githubusercontent.com/GSA/federal-apis/master/inventory/federal-API-list.csv
  reason: no-developer-program
  state: none
created: '2024-12-03'
description: The Federal Protective Service uses its security expertise and law enforcement authority to protect federal government facilities and safeguard the millions of employees and visitors who pass through them every day.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-protective-service.png
layout: provider
modified: '2026-09-09'
name: Federal Protective Service
nav: Providers
network: true
overview: Federal Protective Service is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Security, Law Enforcement, Public Safety, and Physical Security.
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-protective-service/refs/heads/main/screenshots/federal-protective-service-2026-06-20T181124.png
security:
- kind: domain-security
  name: Federal Protective Service Domain Security
  slug: federal-protective-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-protective-service
tags:
- Federal-Government
- Security
- Law Enforcement
- Public Safety
- Physical Security
- Homeland Security
website: https://www.dhs.gov/federal-protective-service
---
