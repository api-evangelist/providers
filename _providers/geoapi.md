---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://api.gouv.fr/api/geoapi.html'', ''status'': 301, ''note'': ''declared website redirects to https://www.data.gouv.fr/dataservices — a different registrable domain (api.gouv.fr -> data.gouv.fr), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: French geographical data
  name: GeoApi
  slug: geoapi
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geoapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.gouv.fr/api/geoapi.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: French geographical data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geoapi.png
layout: provider
modified: '2026-05-28'
name: GeoApi
nav: Providers
network: true
overview: GeoApi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/geoapi/refs/heads/main/screenshots/geoapi-2026-06-20T181744.png
security:
- kind: domain-security
  name: Geoapi Domain Security
  slug: geoapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: geoapi
tags:
- Geocoding
- Public APIs
website: https://api.gouv.fr/api/geoapi.html
---
