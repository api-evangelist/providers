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
  url: security/ruhnn-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ruhnn-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ruhnn.com
coverage:
  checked: '2026-08-13'
  detail: 'Ruhnn runs two client-rendered SPAs — the ruhnn.com corporate site and the www.kol18.com (爱推广) KOL/merchant platform — and neither exposes a developer surface: api., open., developer., dev., docs. and openapi.ruhnn.com all return NXDOMAIN, and every spec and /.well-known path on both hosts answers 200 with the identical HTML app shell rather than a document.'
  evidence:
  - status: 200
    url: https://ruhnn.com/openapi.json
  - status: 200
    url: https://ruhnn.com/.well-known/agent-card.json
  - status: 200
    url: https://www.kol18.com/v2/api-docs
  - status: 404
    url: https://api.github.com/orgs/ruhnn
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Ruhnn Holding Limited (如涵控股) is a Hangzhou-based Chinese influencer (KOL) incubation, marketing, and e-commerce company. It pioneered the "internet celebrity" (wanghong) commercialization model, signing and developing influencers and monetizing their audiences through self-operated online stores on marketplaces such as Taobao and Tmall, as well as through a platform/advertising business that connects its network of KOLs with third-party brands for social-marketing campaigns. The company listed on NASDAQ under the ticker RUHN in 2019 and was subsequently taken private. It is surfaced here as a portfolio company of Qiming Venture Partners. Ruhnn is a consumer-facing influencer marketing and commerce operator and does not publish a public developer platform, API, or SDK surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ruhnn.png
layout: provider
modified: '2026-08-13'
name: ruhnn
nav: Providers
network: true
overview: ruhnn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, E-Commerce, KOL, and Social Commerce.
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/ruhnn/refs/heads/main/screenshots/ruhnn-2026-09-02T154213.png
security:
- kind: domain-security
  name: Ruhnn Domain Security
  slug: ruhnn-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ruhnn
tags:
- Company
- Influencer Marketing
- E-Commerce
- KOL
- Social Commerce
- Marketing
- China
- Consumer
website: https://ruhnn.com
---
