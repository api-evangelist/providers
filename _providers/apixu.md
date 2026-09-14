---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.apixu.com/doc/request.aspx'', ''status'': 301, ''note'': ''declared website redirects to https://weatherstack.com/ — a different registrable domain (apixu.com -> weatherstack.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: Weather
  name: APIXU
  slug: apixu
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apixu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apixu.com/doc/request.aspx
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Weather
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apixu.png
layout: provider
modified: '2026-05-28'
name: APIXU
nav: Providers
network: true
overview: APIXU publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/apixu/refs/heads/main/screenshots/apixu-2026-06-20T172302.png
security:
- kind: domain-security
  name: Apixu Domain Security
  slug: apixu-domain-security
  summary_line: TLSv1.3
slug: apixu
tags:
- Weather
- Public APIs
website: https://www.apixu.com/doc/request.aspx
---
