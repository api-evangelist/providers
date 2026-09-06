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
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://unamo.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unamo-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Unamo is dead — unamo.com returns NXDOMAIN with no A, NS or SOA records at all, and the pre-rebrand domain positionly.com is now a third-party WordPress rebuild of the 2017 Positionly marketing site whose own /api link 404s.
  evidence:
  - status: 0
    url: https://unamo.com
  - status: 404
    url: https://positionly.com/api
  - status: 404
    url: https://positionly.com/openapi.json
  - status: 404
    url: https://positionly.com/.well-known/agent-card.json
  - status: 200
    url: https://positionly.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: Unamo was a Warsaw, Poland based SaaS suite offering SEO monitoring, social media monitoring, and conversion rate optimization, formerly known as Positionly, and backed by Point Nine Capital. The company appears defunct as of July 2026, with unamo.com no longer resolving in DNS and the pre-rebrand positionly.com site serving stale 2017-era content whose API, signup, terms, and privacy pages return 404. No public API surface, client packages, or developer documentation remain online.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unamo.png
layout: provider
modified: '2026-08-13'
name: Unamo
nav: Providers
network: true
overview: Unamo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SEO, Social-Media, Analytics, and Monitoring.
random_paper: 19
slug: unamo
tags:
- Company
- SEO
- Social-Media
- Analytics
- Monitoring
- Marketing
website: https://unamo.com
---
