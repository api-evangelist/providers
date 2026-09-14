---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://finmark.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.bill.com:443/ — a different registrable domain (finmark.com -> bill.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finmark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finmark.com/
created: '2026-07-17'
description: 'Finmark was a financial planning, modeling, and forecasting SaaS platform for startups and small businesses, backed by Bessemer Venture Partners, letting founders build budgets, cash-flow runway, hiring plans, and scenario models without spreadsheets. It was acquired by BILL (bill.com) and wound down as a standalone product: as of this enrichment pass finmark.com and www.finmark.com return a 301 permanent redirect to https://www.bill.com/. There is no longer an independent Finmark developer portal, API, documentation, pricing, or status page to enrich; the domain-security probe below reflects the residual finmark.com DNS/TLS surface only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finmark.png
layout: provider
modified: '2026-07-19'
name: Finmark
nav: Providers
network: true
overview: Finmark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Financial Planning, Fintech, and Software-as-a-Service.
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/finmark/refs/heads/main/screenshots/finmark-2026-07-25T214541.png
security:
- kind: domain-security
  name: Finmark Domain Security
  slug: finmark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finmark
tags:
- Company
- Cloud
- Financial Planning
- Fintech
- Software-as-a-Service
- Startups
- Acquired
- Forecasting
website: https://finmark.com/
---
