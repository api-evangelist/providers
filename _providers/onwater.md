---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://onwater.io/'', ''status'': 301, ''note'': ''declared website redirects to https://isitwater.com/ — a different registrable domain (onwater.io -> isitwater.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Determine if a lat/lon is on water or land
  name: OnWater
  slug: onwater
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onwater-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onwater.io/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Determine if a lat/lon is on water or land
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onwater.png
layout: provider
modified: '2026-05-28'
name: OnWater
nav: Providers
network: true
overview: OnWater publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/onwater/refs/heads/main/screenshots/onwater-2026-06-20T190722.png
security:
- kind: domain-security
  name: Onwater Domain Security
  slug: onwater-domain-security
  summary_line: TLSv1.3
slug: onwater
tags:
- Geocoding
- Public APIs
website: https://onwater.io/
---
