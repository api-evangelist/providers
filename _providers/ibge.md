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
- description: Aggregate services of IBGE (Brazilian Institute of Geography and Statistics)
  name: IBGE
  slug: ibge
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://servicodados.ibge.gov.br/api/docs/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Aggregate services of IBGE (Brazilian Institute of Geography and Statistics)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibge.png
layout: provider
modified: '2026-05-28'
name: IBGE
nav: Providers
network: true
overview: IBGE publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 8
screenshot: https://raw.githubusercontent.com/api-evangelist/ibge/refs/heads/main/screenshots/ibge-2026-07-25T221953.png
security:
- kind: domain-security
  name: Ibge Domain Security
  slug: ibge-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: ibge
tags:
- Geocoding
- Public APIs
website: https://servicodados.ibge.gov.br/api/docs/
---
