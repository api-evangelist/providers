---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.fishwatch.gov/developers'', ''status'': 301, ''note'': ''declared website redirects to https://www.fisheries.noaa.gov/topic/sustainable-seafood — a different registrable domain (fishwatch.gov -> noaa.gov), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Information and pictures about individual fish species
  name: FishWatch
  slug: fishwatch
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fishwatch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fishwatch.gov/developers
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Information and pictures about individual fish species
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fishwatch.png
layout: provider
modified: '2026-05-28'
name: FishWatch
nav: Providers
network: true
overview: FishWatch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Animals and Public APIs.
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/fishwatch/refs/heads/main/screenshots/fishwatch-2026-06-20T181254.png
security:
- kind: domain-security
  name: Fishwatch Domain Security
  slug: fishwatch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fishwatch
tags:
- Animals
- Public APIs
website: https://www.fishwatch.gov/developers
---
