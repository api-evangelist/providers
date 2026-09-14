---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://reserve.com'', ''status'': 301, ''note'': ''declared website redirects to https://resy.com/ — a different registrable domain (reserve.com -> resy.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://reserve.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reserve-domain-security.yml
created: '2026-07-17'
description: Reserve was a restaurant-reservation startup backed by GV and surfaced in the API Evangelist network as a consumer-sector portfolio lead. Its domain reserve.com now issues an HTTP 301 redirect to resy.com, the Resy restaurant-reservation platform, indicating the product has been folded into Resy. During enrichment no independent developer portal, public API, OpenAPI, or developer documentation was found for Reserve, and no security.txt, bug bounty, or trust center is published on the domain. The profile is retained as an acquired/redirected consumer-sector lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reserve.png
layout: provider
modified: '2026-07-20'
name: Reserve *
nav: Providers
network: true
overview: Reserve * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Restaurant, Reservations, and Dining.
random_paper: 8
screenshot: https://raw.githubusercontent.com/api-evangelist/reserve/refs/heads/main/screenshots/reserve-2026-09-02T153529.png
security:
- kind: domain-security
  name: Reserve Domain Security
  slug: reserve-domain-security
  summary_line: TLSv1.2 · HSTS
slug: reserve
tags:
- Company
- Consumer
- Restaurant
- Reservations
- Dining
- Acquired
website: https://reserve.com
---
