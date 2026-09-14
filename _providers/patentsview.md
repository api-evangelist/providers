---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://patentsview.org/apis/purpose'', ''status'': 301, ''note'': ''declared website redirects to https://data.uspto.gov/support/transition-guide/patentsview — a different registrable domain (patentsview.org -> uspto.gov), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 1
apis:
- description: API is intended to explore and visualize trends/patterns across the US innovation landscape
  name: PatentsView
  slug: patentsview
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patentsview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patentsview.org/apis/purpose
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: API is intended to explore and visualize trends/patterns across the US innovation landscape
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patentsview.png
layout: provider
modified: '2026-05-28'
name: PatentsView
nav: Providers
network: true
overview: PatentsView publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Patent and Public APIs.
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/patentsview/refs/heads/main/screenshots/patentsview-2026-06-20T191439.png
security:
- kind: domain-security
  name: Patentsview Domain Security
  slug: patentsview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: patentsview
tags:
- Patent
- Public APIs
website: https://patentsview.org/apis/purpose
---
